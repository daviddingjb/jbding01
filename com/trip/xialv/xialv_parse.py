import urllib.request
import urllib.parse
import re
import numpy as np
import pymysql
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    container = ""
    def handle_data(self, data):
        # self.container += data.strip().replace("	","").replace(" ","").replace("None"," ")
        self.container += data.strip().replace("\"","")
        return str(self.container)

def liangdian_parser(url,i):
    url_r = url + str(i)
    resp = urllib.request.urlopen(url_r)
    try:
        respData = resp.read().decode(resp.headers.get_content_charset())
    except:
        respData = ""
        print("*****urllib.request.urlopen error!*****", url_r)
    # print(respData) # debug
    reg_1 = re.compile(r'<section class="Ask_left main">((?:.|\n)*?)\s*</section>\s*<div class="pageNav">')
    if respData:
        ld_1 = reg_1.findall(str(respData))
        for ld in ld_1:
            # print(url_r) # debug
            # print("ldldldldlddld",ld) # debug
            if ld:
                parser = MyHTMLParser()
                parser.feed(ld)
                # print (parser.container) # debug
                if parser.container:
                    i = i + 1
                    return str(parser.container) + str(liangdian_parser(url,i))

def main():
    url = 'http://www.xialv.com/beijing/zhoubianyou'
    resp = urllib.request.urlopen(url)
    # respData = resp.read()
    try:
        respData = resp.read().decode(resp.headers.get_content_charset())
    except:
        respData = " "
        print("*****urllib.request.urlopen error!*****", url)
    if not respData:
        respData = "  "

    # print(respData) # debug
    pagset_reg = re.compile(r'下一页</a><a href=\'/beijing/zhoubianyou\?&page=(.*?)\'  rel=\'nofollow\' >末页')
    regular = re.compile(r'<ul class="scen-list">((?:.|\n)*?)<div class="pageNav">')
    name_reg = re.compile(r'target=\'_blank\'>(.*?)</a></h3>')
    description_reg = re.compile(r'<p>(.*?)</p>')
    father_reg = re.compile(r'\' >(.*?)</a></span></header>')
    fatherurl_reg = re.compile(r'</a></h3><span><a href=\'(.*?)\' title')
    bianhao_reg = re.compile(r'<h3><a href="/scenery/(.*?)" title')

    pagset = pagset_reg.findall(str(respData)) #获取总页数
    print("获取总页数", pagset)

    # 打开数据库连接
    db = pymysql.connect("10.35.22.91", "root", "adminadmin", "tr_trip_temp")
    db.set_charset('utf8')
    paragraphs = regular.findall(str(respData))
    for eachP in paragraphs:
        # print(eachP) # debug

        nameList = name_reg.findall(str(eachP))
        descriptionList = description_reg.findall(eachP)
        fatherList = father_reg.findall(str(eachP))
        fatherurlList = fatherurl_reg.findall(str(eachP))
        bianhaoList = bianhao_reg.findall(str(eachP))

        for i in range(len(nameList)):
            bianhao = bianhaoList[i]
            name = nameList[i]
            description = descriptionList[i]
            father = fatherList[i]
            father_url = "http://www.xialv.com" + fatherurlList[i]
            url = "http://www.xialv.com/scenery/item/" + bianhaoList[i] + "?&page="
            liangdian = liangdian_parser(url,1)
            # print(liangdian) #debug
            sql = 'INSERT INTO tr_trip_temp.t_bj_zhoubian(bianhao, name, father_url, father, description, liangdian ) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % \
                (bianhao, name, father_url, father, description, liangdian)
            sql = sql.replace("None"," ")
            print(sql)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            cursor.execute('SET NAMES utf8;')
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                # print(sql)
                print("*******insert SQL error!*******")
                db.rollback()

    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    main()
