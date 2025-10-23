#src/preporcessing/preprocess.py

"""
Author: 안혜빈, 우재현
Date: 2025-10-23
Description: 데이터 전처리 모듈

"""

# data/raw 에서 데이터 호출

import pandas as pd
import os


xls_file= '/Users/anhyebin/Documents/SKN21/SKN21-1st-2Team/SKN21-1st-2Team/data/raw/201007_202510_전기차등록현황.xls'
df = pd.read_excel(xls_file)

csv_file = "data/raw/file1.csv"
df.to_csv(csv_file, index=False, encoding="utf-8")


# 명준씨가 준 방법대로 데이터 가공
# data/processed 폴더에 가공한 데이터 파일 저장

#전기차 등록 연도별 데이터 전처리
def pre_ev_year():
    pass

#수소차 등록 연도별 데이터 전처리
def pre_h2_year():
    pass

#전기차 충전소 지역별 데이터 전처리
def pre_ev_station():
    pass
#수소차 충전소 지역별 데이터 전처리
def pre_h2_station():
    pass

#FAQ 데이터 전처리
def pre_faq():
    pass