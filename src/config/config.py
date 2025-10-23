"""
Author: 
Date: 
Description: 환경변수 설정을 위한 config 파일
"""

# src/config/config.py
import os

# 이름, 비밀번호 설정 필요
DB_INFO = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "eco_car_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}