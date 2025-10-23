# Streamlit 시각화나 API에서 사용할 데이터 조회 기능"""
# fetch_data.py
# DB에서 데이터 조회 (시각화용)

"""
Author:
Date: 2025-10-23
Description: 데이터 패치 파일
"""

import pandas as pd
from src.database.db_connection import get_connection
#import db_connection as db_conn

def fetch_station_info():
    """
    수소차 충전소 정보
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT region, AVG(price)
    FROM h2_station_info
    GROUP BY region
    ORDER BY station_id;
    """
    df = pd.read_sql(query, conn)

    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    print("fetched:", resultset)

    conn.commit()
    conn.close()
    return df

def fetch_vehicle_trend():
    """
    연도별 H2/EV 자동차 등록 현황 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT year, h2_car_total, h2_car_total
    FROM annual_h2_ev_registrations
    GROUP BY year
    ORDER BY year desc;
    """
    df = pd.read_sql(query, conn)

    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    print("fetched:", resultset)

    conn.commit()
    conn.close()
    return df


def fetch_station_count_by_region():
    """
    지역별 수소차 충전소 개수 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT * 
    FROM h2_stations_by_region;
    """
    df = pd.read_sql(query, conn)

    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    print("fetched:", resultset)

    cursor.execute(query)
    conn.commit()
    conn.close()
    return df

def fetch_ev_stations_region():
    """
    지역별 전기차 충전소 개수
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM ev_stations_by_region
    """
    df = pd.read_sql(query, conn)

    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    print("fetched:", resultset)

    cursor.execute(query)
    conn.commit()
    conn.close()
    return df

def fetch_faq():
    """
    수소차 충전소 인프라 FAQ
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    cursor = conn.cursor()

    query = """
    SELECT faq_id, question, answer
    FROM h2_faq;
    """
    df = pd.read_sql(query, conn)

    result = cursor.execute(query)
    print("query:", result)
    resultset = cursor.fetchall()
    print("fetched:", resultset)

    cursor.execute(query)
    conn.commit()
    conn.close()
    return df