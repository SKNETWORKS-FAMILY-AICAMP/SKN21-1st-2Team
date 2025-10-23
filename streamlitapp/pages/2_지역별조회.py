import streamlit as st
import pandas as pd
import numpy as np


st.subheader("Checkbox")
@st.cache_data
def get_data():
    # csv 파일을 읽어 DataFrame(판다스의 표)로 생성(read_csv)
    # 앞 10개 행만 조회(head(10))
    df = pd.read_csv("data/boston_housing.csv").head(10)
    return df

bool_value = st.checkbox("**표를 보시겠습니까?**") # check: True, check 해제: False 반환
if bool_value:
    df = get_data()
    st.dataframe(df)
else:
    st.write("데이터가 없습니다.")