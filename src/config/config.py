# src/config/config.py
"""
Author: 우재현
Date: 2025-10-23
Description: 프로젝트 전체 공통 설정 파일 | DB 연결, 파일 경로, API 키 등 전역 설정 관리
"""

import os
from dotenv import load_dotenv

# .env 파일 호출(db 접속을 위한 민감 정보)
load_dotenv()

# 이름, 비밀번호 설정 필요
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", ""),
    "port": int(os.getenv("DB_PORT", 3306))
}

# 데이터 경로
DATA_PATH = {
    "RAW": "data/raw",
    "PROCESSED": "data/processd"

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
}