# -*- coding: UTF-8 -*-
import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host='shibaski.ckhkci0toeh4.ap-northeast-2.rds.amazonaws.com',
                                  port=3306,
                                  user='shibaski',
                                  password='shibaskiepdlxjqpdltm12!',
                                  database='shibaski',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        ret = self.cursor.execute(query, args)
        # self.cursor.close()
        return ret

    def executeLastrowid(self, query, args={}):
        self.cursor.execute(query, args)
        return self.cursor.lastrowid

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        self.cursor.close()
        return row

    def executeMany(self, query, args={}):
        self.cursor.executemany(query, args)
        row = self.cursor.fetchall()
        self.db.commit()
        self.cursor.close()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        # self.cursor.close()
        return row

    def executeAllNoClose(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row


    def allClose(self):
        self.db.commit()
        self.cursor.close()

    def commit(self):
        self.db.commit()