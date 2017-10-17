# -*- coding: utf-8 -*-
__author__ = '157517301@qq.com'

import logging
import pymysql

class MySQLCommand(object):
    def __init__(self,host,port,user,passwd,db,table):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.table = table

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db,charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def queryMysql(self):
        sql = "SELECT * FROM " + self.table

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            print(row)

        except:
            print(sql + ' execute failed.')

    def insertMysql(self,sql,):
        try:
            self.cursor.execute(sql)
        except:
            print("insert failed.")

    def updateMysqlSN(self,sql):
        print("update sn:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()
# mysql = MySQLCommand('10.35.22.91','3306','root','adminadmin','tr_trip_temp','t_bj_zhoubian')
# sql = 'INSERT INTO tr_trip_temp.t_bj_zhoubian(bianhao, name, father_url, father, description, liangdian ) VALUES ("3891", "天津Hello Ki...", "http://www.xialv.com/tianjin/haowan", "天津", "天津Hello Kitty主题公园，目前正在建设之中，是天津市民期待已久的开心乐园。在建成...", "None")'
# mysql.insertMysql(sql)
