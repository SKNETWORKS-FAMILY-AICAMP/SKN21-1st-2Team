# Streamlit 시각화나 API에서 사용할 데이터 조회 기능"""
# fetch_data.py
# DB에서 데이터 조회 (시각화용)

import pandas as pd
from src.database.db_connection import get_connection


def fetch_vehicle_trend():
    """
    연도별 전기차/수소차 등록 현황 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()

    query = """
    SELECT year, type, SUM(count) AS total
    FROM vehicle_data
    GROUP BY year, type
    ORDER BY year;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def fetch_station_count_by_region():
    """
    지역별 충전소 개수 조회
    """
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()

    query = """
    SELECT region, COUNT(*) AS count
    FROM station_data
    GROUP BY region
    ORDER BY count DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df