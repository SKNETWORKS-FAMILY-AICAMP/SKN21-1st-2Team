# streamlitapp/home.py

"""
Author: 
Date: 
Description: 메인 구동 파일. streamlit run home.py로 실행할 예정
"""

import streamlit as st
import pandas as pd
import numpy as np


# docs에 넣은 H2car 이미지를 메인에 넣어보고 싶은데 안 되네요.
# 못 하면 메인 페이지 꾸밀만한 다른 거 찾아보기.


import streamlit as st
from streamlit_option_menu import option_menu
import importlib


# 🔧 페이지 설정
st.set_page_config(
    page_title="친환경 자동차 비교 분석 서비스",
    page_icon="🚗",
    layout="wide",
)

# 🚗 사이드바 네비게이션 메뉴
with st.sidebar:
    selected = option_menu(
        " 친환경 자동차",
        ["메인", "친환경차 그래프", "충전소 분포", "FAQ", "충전소 조회"],
        icons=["house", "bar-chart", "fuel-pump", "question-circle", "geo-alt"],
        menu_icon="car-front",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "#1f77b4", "font-size": "16px"},
            "menu-title": { #메뉴 타이틀 수정
            "font-size": "17px",
                },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#e9ecef",
            },
            "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
        },
    )

# 🧭 페이지 라우팅
if selected == "메인":
    st.title("🚗 국내 친환경 자동차 비교 분석 서비스")
    st.markdown("---")
    st.subheader("📊 서비스 소개")
    st.write(
        """
        이 애플리케이션은 국내 친환경 자동차에 대한 데이터를 기반으로
        연도별 증감, 충전소 분포, FAQ, 그리고 충전소 조회 기능을 제공합니다.

        좌측 사이드바에서 원하는 기능을 선택하여 탐색해보세요! 🔍
        """
    )

elif selected == "친환경차 그래프":
    importlib.import_module("subpages.p1_graph").app()

elif selected == "충전소 분포":
    importlib.import_module("subpages.p2_charge").app()

elif selected == "FAQ":
    importlib.import_module("subpages.p3_faq").app()

elif selected == "충전소 조회":
    importlib.import_module("subpages.p4_search").app()