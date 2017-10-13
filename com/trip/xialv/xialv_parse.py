import urllib.request
import urllib.parse
import re
import numpy as np
import pymysql
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    container = ""
    def handle_data(self, data):
        self.container += data.strip().replace("	","").replace(" ","").replace("None"," ")
        return str(self.container)

def liangdian_parser(url,i):
    url_r = url + str(i)
    resp = urllib.request.urlopen(url_r)
    try:
        respData = resp.read().decode(resp.headers.get_content_charset())
    except:
        print("2222222222")
    # print(respData) # debug
    reg_1 = re.compile(r'<section class="Ask_left main">((?:.|\n)*?)\s*</section>\s*<div class="pageNav">')
    if str(respData):
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

url = 'http://www.xialv.com/beijing/zhoubianyou'
resp = urllib.request.urlopen(url)
# respData = resp.read()
try:
    respData = resp.read().decode(resp.headers.get_content_charset())
except:
    print("33333333333")

# print(respData) # debug
regular = re.compile(r'<ul class="scen-list">((?:.|\n)*?)<div class="pageNav">')
name_reg = re.compile(r'target=\'_blank\'>(.*?)</a></h3>')
description_reg = re.compile(r'<p>(.*?)</p>')
father_reg = re.compile(r'\' >(.*?)</a></span></header>')
fatherurl_reg = re.compile(r'</a></h3><span><a href=\'(.*?)\' title')
bianhao_reg = re.compile(r'<h3><a href="/scenery/(.*?)" title')

# 打开数据库连接
db = pymysql.connect("10.35.22.91", "root", "adminadmin", "tr_trip_temp")
if not respData:
    respData = "  "
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
        print(sql)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            # print(sql)
            print("111111111111111")
            db.rollback()

# 关闭数据库连接
db.close()
