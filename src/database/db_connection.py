#src/database/db_connection.py

"""
Author: 우재현
Date: 2025-10-23
Description: MySQL 연결 관리 모듈 
"""

import pymysql
from pymysql.cursors import DictCursor
from config.config import DB_CONFIG 

# MySQL DB 연결 객체를 반환

print(DB_CONFIG)

def get_connection():
    try:
        # print(DB_CONFIG)
        conn = pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"],
            cursorclass=DictCursor,
            charset="utf8mb4"
        )
        return conn
    except Exception as e:
        print(f"❌ DB 연결 실패: {e}")
