# Streamlit 시각화나 API에서 사용할 데이터 조회 기능"""
# fetch_data.py
# DB에서 데이터 조회 (시각화용)

"""
Author: 우재현, 정덕규
Date: 2025-10-23
Description: 데이터 패치 파일
"""

import pandas as pd
from database.db_connection import get_connection
#import db_connection as db_conn

def fetch_h2_station_info():
    """
    수소차 충전소 정보
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT region, format(avg(price),2) "평균가"
    FROM h2_station_info
    group by region;
    """

    print("수소차 충전소 정보")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    #print("fetched:", resultset)
    for row in resultset:
        print(row)

    conn.commit()
    conn.close()
    #return df

def fetch_h2_stations_by_region():
    """
    지역별 수소차 충전소 개수 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT region, number_of_station
    FROM h2_stations_by_region;
    """
    #df = pd.read_sql(query, conn)

    print("지역별 수소차 충전소 개수 조회")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    #print("fetched:", resultset)
    for row in resultset:
        print(row)

    cursor.execute(query)
    conn.commit()
    conn.close()
    #return df

def fetch_annual_h2_ev_registrations():
    """
    연도별 H2/EV 자동차 등록 현황 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT year "연도", ev_car_total "전기차 등록대수", h2_car_total "수소차 등록대수"
    FROM annual_h2_ev_registrations;
    """
    #df = pd.read_sql(query, conn)

    print("연도별 H2/EV 자동차 등록 현황 조회")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    #print("fetched:", resultset)
    for row in resultset:
        print(row)

    cursor.execute(query)
    conn.commit()
    conn.close()
    #return df

def fetch_ev_stations_region():
    """
    지역별 전기차 충전소 개수
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT region, number_of_station
    FROM ev_stations_by_region
    """
    #df = pd.read_sql(query, conn)

    print("지역별 전기차 충전소 개수")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    #print("fetched:", resultset)
    for row in resultset:
        print(row)

    cursor.execute(query)
    conn.commit()
    conn.close()
    #return df

def h2_stats():
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
       SELECT h2.region "지역", h2.number_of_station "수소차 충전소", ev.number_of_station "전기차 충전소"
       FROM h2_stations_by_region h2
       JOIN ev_stations_by_region ev ON h2.region_id = ev.region_id;
       """
    # df = pd.read_sql(query, conn)
    # select e.emp_id, e.emp_name, e.salary, e.comm_pct, d.dept_name, d.loc
    # from emp e join dept d on e.dept_id = d.dept_id
    # where e.comm_pct is not null;

    print("지역별 수소차 및 전기차 등록대수")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    # print("fetched:", resultset)

    for row in resultset:
        print(row)

    cursor.execute(query)
    conn.commit()
    conn.close()
    #return df

def fetch_faq():
    """
    수소차 충전소 인프라 FAQ
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT question, answer
    FROM h2_faq;
    """
    #df = pd.read_sql(query, conn)

    print("수소차 충전소 인프라 FAQ")
    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    #print("fetched:", resultset)

    for row in resultset:
        print(row)

    cursor.execute(query)
    conn.commit()
    conn.close()
    #return df