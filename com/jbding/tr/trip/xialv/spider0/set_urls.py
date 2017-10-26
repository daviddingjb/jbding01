import urllib.request
import urllib.parse
import re
import numpy as np
import pymysql
import time
from html.parser import HTMLParser
from com.jbding.common.db.mysql_connection import getConnection

def request_url(url):
    print(url)
    try:
        resp = urllib.request.urlopen(url)
        return resp.read().decode(resp.headers.get_content_charset())
        # print(respData) #debug
    except:
        return " "
        print("*****urllib.request.urlopen error!*****", url)

def main():
    url = 'http://www.xialv.com/beijing/zhoubianyou'
    respData = request_url(url)

    pagset = pagset_reg.findall(str(respData)) #获取总页数
    if not pagset:
        pagset = ['0']
    # print("获取总页数", pagset)

    for i in range(int(pagset[0])):
        url = 'http://www.xialv.com/beijing/zhoubianyou'
        url = url + "?&page=" + str(i+1)

        sql = 'INSERT INTO crawler.urls(category_1, category_2, url, is_crawled ) VALUES ("%s", "%s", "%s", "%s")' % \
              ('北京', '周边', url, 'n')
        print(sql)

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

if __name__ == '__main__':
    # Regular Expressions:
    pagset_reg = re.compile(r'下一页</a><a href=\'/beijing/zhoubianyou\?&page=(.*?)\'  rel=\'nofollow\' >末页')

    db,cursor = getConnection("10.35.22.91", "root", "adminadmin", "crawler")

    # # 打开数据库连接
    # db = pymysql.connect("10.35.22.91", "root", "adminadmin", "crawler")
    #
    # db.set_charset('utf8')
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # cursor.execute('SET NAMES utf8;')
    # cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')

    main()

    # 关闭数据库连接
    db.close()
