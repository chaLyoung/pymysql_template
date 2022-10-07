# -*- coding: UTF-8 -*-
import pymysql
import json


try:
    try:
        config_file = r"./dbInfo.json"
        with open(config_file, 'rt', encoding='utf-8') as f:
            config = json.load(f)
    finally:
        f.close()
except Exception as e:
    print(e)

HOST = config["HOST"]
PORT = config["PORT"]
USER = config["USER"]
PASSWORD = config["PASSWORD"]
DATABASE = config["DATABASE"]


class Database():
    def __init__(self):
        self.db = pymysql.connect(host=HOST,
                                  port=PORT,
                                  user=USER,
                                  password=PASSWORD,
                                  database=DATABASE,
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