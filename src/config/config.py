"""
Author: 우재현
Date: 25-10-23
Description: 환경변수 설정을 위한 config 파일
"""
 
# src/config/config.py
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# PROJECT_ROOT = Path(__file__).reslove().parent.parent.parent
# sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv()

# 이름, 비밀번호 설정 필요
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", ""),
    "port": int(os.getenv("DB_PORT", ""))
}

# 데이터 경로
DATA_PATH = {
    "RAW": "data/raw",
    "PROCESSED": "data/processed"
    
}

# 로깅 설정
LOG_CONFIG = {
    "level": "INFO",
    "format": "[%(asctime)s] %(levelname)s - %(message)s",
}

# Streamlit 관련
APP_CONFIG = {
    "title": "국내 친환경 자동차 비교 분석 서비스",
    "page_icon": "🚗",
    "database": os.getenv("DB_NAME", "eco_car_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}