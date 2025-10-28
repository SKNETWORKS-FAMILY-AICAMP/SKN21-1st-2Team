# 전처리된 CSV 데이터를 MySQL 테이블에 저장하는 코드
# (전처리 담당자 안혜빈 씨가 만든 CSV를 DB로 옮김)

"""
Author: 우재현, 정덕규
Date: 2025-10-24
Description: 데이터 패치 파일
"""

import pandas as pd
from database.db_connection import get_connection

#csv_path = h2_faq.csv
def h2_faq(csv_path):
    # df = pd.read_csv(csv_path)
    # print(df.columns) # ['Unnamed: 0', '0', '1']
    conn = get_connection()
    df = pd.read_csv(csv_path, names=["question", "answer"], header=0, skiprows=1)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO h2_faq (question, answer) 
    VALUES (%s, %s);
    """
    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["question"], row["answer"]))
        
    conn.commit()
    conn.close()


#csv_path = annual_h2_ev_registrations.csv
def annual_H2_ev_registrations(csv_path):
    # df = pd.read_csv(csv_path) 
    # print(df.columns) # ['year', 'h2_car_total', 'ev_car_total']
    conn = get_connection()
    df = pd.read_csv(csv_path, names=["year", "h2_car_total", "ev_car_total"], header = 0)
    print(df.columns)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO annual_H2_ev_registrations (year, h2_car_total, ev_car_total) 
    VALUES (%s, %s, %s);
    """
    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["year"], row["h2_car_total"], row["ev_car_total"]))
        
    conn.commit()
    conn.close()


# csv_path = h2_station_info.csv
def h2_station_info(csv_path):
    # df = pd.read_csv(csv_path)
    # print(df.columns) # ['Unnamed: 0', 'station_name', 'price', 'tel', 'region']
    conn = get_connection()
    df = pd.read_csv(csv_path, names=["station_name", "region", "price", "tel", "region_id"], header= 0, skiprows=1)
    # df = df.where((pd.notnull(df)), 0)
    # print(df)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO h2_station_info (station_name, region, price, tel, region_id) 
    VALUES (%s, %s, %s, %s, %s);
    """

    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["station_name"], row["region"], int(row["price"]), row["tel"], int(row["region_id"])))
        
    conn.commit()
    conn.close()

#csv_path = h2_station_by_region.csv
def h2_stations_by_region(csv_path):
    # df = pd.read_csv(csv_path) 
    # print(df.columns) # ['region', 'number_of_station']
    conn = get_connection()
    # region,number_of_station,region_id
    df = pd.read_csv(csv_path, names=["region", "number_of_station", "region_id"], header = 0)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO h2_stations_by_region (region_id, number_of_station) 
    VALUES (%s, %s);
    """
    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["region_id"], int(row["number_of_station"])))
        
    conn.commit()
    conn.close()

#csv_path = ev_station_by_region.csv
def ev_stations_by_region(csv_path):
    # df = pd.read_csv(csv_path) 
    # print(df.columns) # ['region', 'number_of_station']
    conn = get_connection()
    df = pd.read_csv(csv_path, names=["region", "number_of_station", "region_id"], header = 0)
    # region,number_of_station,region_id
    # print(df.columns)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO ev_stations_by_region (region_id, number_of_station) 
    VALUES (%s, %s);
    """
    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["region_id"], int(row["number_of_station"])))
        
    conn.commit()
    conn.close()


def region(csv_path):

    #df = pd.read_csv(csv_path)
    #print(df.columns)

    conn = get_connection()
    

    df = pd.read_csv(csv_path, names=["region", "region_id"], header=0)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO region (region, region_id) 
    VALUES (%s, %s);
    """
    for _, row in df.iterrows():
        curs.execute(insert_sql, (row["region"], int(row["region_id"])))


    conn.commit()
    conn.close()

