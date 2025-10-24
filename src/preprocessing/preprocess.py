#src/preporcessing/preprocess.py

"""
Author: 안혜빈, 우재현
Date: 2025-10-23
Description: 데이터 전처리 모듈
"""

# data/raw 에서 데이터 호출
# 명준씨가 준 방법대로 데이터 가공
# data/processed 폴더에 가공한 데이터 파일 저장



#pip install pandas
#pip install xlrd

import pandas as pd
import os


#csv파일로 변경
xls_file= '/Users/anhyebin/Documents/SKN21/SKN21-1st-2Team/SKN21-1st-2Team/data/raw/지역별_전기차_충전기_구축현황(누적).xls'
df = pd.read_excel(xls_file, engine='xlrd')

csv_file = "data/raw/지역별_전기차_충전기_구축현황(누적).csv"
df.to_csv(csv_file, index=False, encoding="utf-8")



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

file_path="/Users/anhyebin/Documents/SKN21/SKN21-1st-2Team/SKN21-1st-2Team/data/raw/수소충전소.csv"

df = pd.read_csv(file_path, header=2)

df_new = df[['충전소', '주소', '요금', '연락처']].copy()

df_new.columns = ['h2_name', 'addr', 'pay', 'tel']
df_new.insert(0, 'no', range(1, len(df_new)+1))

df.to_csv(file_path, index=False, encoding='utf-8-sig')


# CSV 불러오기
df = pd.read_csv("data/raw/h2hub_clean.csv", encoding='utf-8-sig')

# 컬럼 이름 확인
#print("컬럼명:", df.columns.tolist())

# 컬럼 이름 변경
df.rename(columns={'주소': 'addr', '충전소': 'h2_name', '요금': 'pay', '연락처': 'tel'}, inplace=True)

#주소 매핑
addr_map = {
    '서울': '서울', '서울특별시': '서울', 
    '세종':'세종,', '세종특별자치시':'세종', 
    '부산': '부산', '부산광역시': '부산',
    '대구': '대구', '대구광역시': '대구',
    '인천': '인천', '인천광역시': '인천',
    '광주': '광주', '광주광역시': '광주',
    '대전': '대전',
    '울산': '울산', '울산광역시': '울산',
    '전남':'전남', '전라남도': '전남',
    '전북':'전북', '전라북도': '전북',
    '경기':'경기', '경기도': '경기',
    '강원도': '강원', '강원특별자치도': '강원',
    '충북':'충북', '충청북도': '충북',
    '충남':'충남', '충청남도': '충남',
    '경북':'경북', '경상북도': '경북',
    '경남':'경남', '경상남도': '경남', 
    '제주':'제주', '제주특별자치도': '제주'
}

#addr(주소)
def simplify_addr(addr):
    if pd.isna(addr) or str(addr).strip() == "":
        return 'None'
    for key in addr_map:
        if addr.startswith(key):
            return addr_map[key]
    return addr

df['addr'] = df['addr'].apply(simplify_addr)

#pay(요금)
# 쉼표와 '원' 제거, 숫자형 변환
df['pay'] = df['pay'].astype(str).str.replace(',', '', regex=False)  # 쉼표 제거
df['pay'] = df['pay'].str.replace('원', '', regex=False)             # '원' 제거
df['pay'] = df['pay'].str.strip()                                     # 앞뒤 공백 제거
df['pay'] = df['pay'].replace('', '0')                                # 빈 문자열은 0으로
df['pay'] = df['pay'].astype(int)  

#tel(연락처)
def clean_tel(tel):
    if pd.isna(tel) or str(tel).strip() == "":
        return 'None'
    return str(tel).replace('-', '').strip()

df['tel'] = df['tel'].apply(clean_tel)


# 상위 5줄 확인
print(df.head())

save_path = '/Users/anhyebin/Documents/SKN21/SKN21-1st-2Team/data/processed'
df.to_csv(save_path, index=False, encoding='utf-8-sig')




#FAQ 데이터 전처리
def pre_faq():
    pass