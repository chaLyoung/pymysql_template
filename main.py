from DB import sqlJson
import re

def init():
    sql = sqlJson.SqlJson()

    RESORT_INFO = {
        'resort_name': '하이원'
        , 'resort_address': '강원도 정선군 고한읍 고한7길 399'
        , 'resort_phone_no': '1588-7789'
        , 'start_time': None
        , 'end_time': None
    }
    slope = [
        '제우스Ⅱ',
        '제우스Ⅲ',
        '제우스Ⅲ-1',
        '빅토리아Ⅰ',
        '빅토리아Ⅱ',
        '헤라Ⅰ',
        '헤라Ⅱ',
        '헤라Ⅲ',
        '아폴로Ⅰ',
        '아폴로Ⅲ',
        '아테나Ⅱ',
        '아테나Ⅲ'
    ]
    level = [
        '초급'
        , '초급'
        , '초급'
        , '상급'
        , '상급'
        , '중급'
        , '중상급'
        , '상급'
        , '상급'
        , '상급'
        , '중급'
        , '초급'
    ]

    slope_time = {
        "주간": {
            'start_time': '09:00:00'
            , 'end_time': '16:30:00'
        }
        , "야간": {
            'start_time': '18:00:00'
            , 'end_time': '22:00:00'
        }
    }

    if len(slope) == len(level):
        try:
            slope_time_list = []
            # 마지막 슬로프 코드 조회
            has_same_name = sql.has_same_resort_name(RESORT_INFO['resort_name'])
            if has_same_name is None:
                last_resort_code = sql.select_last_resort_code()['resort_code']
                last_resort_number = int(re.sub(r'[^0-9]', '', last_resort_code))
                new_resort_number = last_resort_number + 1

                resort_code = 'R' + str(new_resort_number).zfill(4)
                resort_insert_result = sql.insert_resort('R0004', RESORT_INFO['resort_name'], RESORT_INFO['resort_address'],
                                                         RESORT_INFO['resort_phone_no'], RESORT_INFO['start_time'],
                                                         RESORT_INFO['end_time'])


                # # 마지막 슬로프 코드 / 슬로프 타임 코드 조회
                last_slope_code = sql.select_last_slope_code()['slope_code']
                last_slope_number = int(re.sub(r'[^0-9]', '', last_slope_code))

                last_slope_time_code = sql.select_last_slope_time_code()['slope_time_code']
                last_slope_time_number = int(re.sub(r'[^0-9]', '', last_slope_time_code))

                for idx, name in enumerate(slope):
                    new_slope_number = last_slope_number + idx + 1
                    slope_code = 'S' + str(new_slope_number).zfill(4)
                    slope_insert_result = sql.insert_slope(resort_code, slope_code, name, level[idx])

                    for sub_idx, (time_name, time) in enumerate(slope_time.items()):
                        last_slope_time_number = last_slope_time_number + 1
                        new_slope_time_number = last_slope_time_number
                        slope_time_code = 'ST' + str(new_slope_time_number).zfill(4)
                        slope_time_data = [resort_code, slope_code, slope_time_code, time_name, time['start_time'], time['end_time']]
                        slope_time_list.append(slope_time_data)

                slope_time_insert_result = sql.insert_slope_time(slope_time_list)
            else:
                print('has same resort name')
        except Exception as e:
            print(e)

def make_slope_time_data():
    slope_time_data = {}
    slope_time_data['resort_code'] = 'rr'


if __name__ == '__main__':
    init()