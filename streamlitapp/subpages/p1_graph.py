#. 꺾은 선 그래프 두개. 비교
#. x축 연도 18년도 ~ 25년도 / y축 증가율(10,000대 단위로 눈금 표시) 최저 0~ 100
import os
import sys
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
src_path = os.path.join(project_root, "src")

if src_path not in sys.path:
    sys.path.append(src_path)

from visualization import plot

import pandas as pd
import numpy as np

def app():
     st.set_page_config(page_title='연도별 친환경차 등록 그래프', page_icon="📊")

     st.title("📊 연도별 친환경차 등록 그래프")
     st.subheader("2018년~2025년 사이의 전기차와 수소차의 비교")
     
     h2_fig = plot.h2_line_plot()
     st.pyplot(h2_fig)

     ev_fig = plot.ev_line_plot()
     st.pyplot(ev_fig)