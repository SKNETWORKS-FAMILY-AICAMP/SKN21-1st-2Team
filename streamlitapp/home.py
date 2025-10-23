# streamlitapp/home.py

"""
Author: 
Date: 
Description: 메인 구동 파일. streamlit run home.py로 실행할 예정
"""
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='국내 친환경 자동차 비교 분석 서비스', page_icon="🚗", layout="wide")

st.title('국내 친환경 자동차 비교 분석 서비스')

# docs에 넣은 H2car 이미지를 메인에 넣어보고 싶은데 안 되네요.
# 못 하면 메인 페이지 꾸밀만한 다른 거 찾아보기.