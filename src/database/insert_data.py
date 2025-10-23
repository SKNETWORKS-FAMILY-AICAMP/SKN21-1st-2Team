# 전처리된 CSV 데이터를 MySQL 테이블에 저장하는 코드
# (전처리 담당자 안혜빈 씨가 만든 CSV를 DB로 옮김)

import pandas as pd
from database.db_connection import get_connection


# def insert_ChargerByYear(csv_path):
#     conn = get_connection()

#     df = pd.read_csv(csv_path)
#     curs = conn.cursor()
#     insert_sql = ""
#     # for

#     conn.commit()
#     conn.close()



# def insert_EvStationTotal(csv_path):
#     conn = get_connection()

#     df = pd.read_csv(csv_path)
#     curs = conn.cursor()
#     insert_sql = ""
#     # for

#     conn.commit()
#     conn.close()


def H2Faq(csv_path):
    conn = get_connection()

    df = pd.read_csv(csv_path)
    # print(df)
    curs = conn.cursor()
    insert_sql = """
    INSERT INTO h2_faq(que, ans) 
    VALUES ("a", "b");
    """
    curs.execute(insert_sql)
    conn.commit()
    conn.close()

# def H2Station(csv_path):
#     conn = get_connection()

#     df = pd.read_csv(csv_path)
#     curs = conn.cursor()
#     insert_sql = ""
#     # for

#     conn.commit()
#     conn.close()


# def H2StationTotal(csv_path):
#     conn = get_connection()

#     df = pd.read_csv(csv_path)
#     curs = conn.cursor()
#     insert_sql = ""
#     # for

#     conn.commit()
#     conn.close()
