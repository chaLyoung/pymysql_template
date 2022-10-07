# -*- coding: UTF-8 -*-
from DB import dbModule
import os
import re

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql.sql"), "rt", encoding="utf-8") as f:
    sqlFile = f.read()
    f.close()
    sqlCommands = sqlFile.split(';')


def repl(m):
    inner_word = list(m.group(2))
    print("m", inner_word)
    return m


def clean_str(text):
    pattern = '[^\w\s]'  # 특수기호제거
    text = re.sub(pattern=pattern, repl='\\\\\g<0>', string=text)
    text = re.sub(r'\\%', r'%%', text)

    return text


class SqlJson:
    def __init__(self):
        self.tHas_same_resort_name = sqlCommands[0]
        self.tSelect_last_resort_code = sqlCommands[1]
        self.tInsert_resort = sqlCommands[2]
        self.tSelect_last_slope_code = sqlCommands[3]
        self.tInsert_slope = sqlCommands[4]
        self.tSelect_last_slope_time_code = sqlCommands[5]
        self.tInsert_slope_time = sqlCommands[6]

    # 0. 같은 이름 리조트 유무
    def has_same_resort_name(self, resort_name):
        db = dbModule.Database()
        query = self.tHas_same_resort_name.format(resort_name=resort_name)
        result = db.executeOne(query)
        return result

    # 1. 마지막 리조트 코드 select
    def select_last_resort_code(self):
        db = dbModule.Database()
        query = self.tSelect_last_resort_code.format()
        result = db.executeOne(query)
        return result

    # 2. 리조트 insert
    def insert_resort(self, resort_code, resort_name, resort_address, resort_phone_no, start_time, end_time):
        db = dbModule.Database()
        query = self.tInsert_resort.format(resort_code=resort_code, resort_name=resort_name, resort_address=resort_address
                                           , resort_phone_no=resort_phone_no, start_time=start_time, end_time=end_time)
        result = db.executeOne(query)
        db.commit()
        return result

    # 3. 마지막 슬로프 코드 select
    def select_last_slope_code(self):
        db = dbModule.Database()
        query = self.tSelect_last_slope_code.format()
        result = db.executeOne(query)
        return result

    # 4. 슬로프 insert
    def insert_slope(self, resort_code, slope_code, slope_name, slope_level):
        db = dbModule.Database()
        query = self.tInsert_slope.format(resort_code=resort_code, slope_code=slope_code, slope_name=slope_name, slope_level=slope_level)
        result = db.executeOne(query)
        db.commit()
        return result

    # 5. 슬로프 타임 코드 select
    def select_last_slope_time_code(self):
        db = dbModule.Database()
        query = self.tSelect_last_slope_time_code.format()
        result = db.executeOne(query)
        return result

    # 6 슬로프 타임 insert
    def insert_slope_time(self, slope_time_list):
        db = dbModule.Database()
        query = self.tInsert_slope_time.format()
        result = db.executeMany(query, slope_time_list)
        db.commit()
        return result