#. 꺾은 선 그래프 두개. 비교
#. x축 연도 18년도 ~ 25년도 / y축 증가율(10,000대 단위로 눈금 표시) 최저 0~ 100

import streamlit as st
import pandas as pd
import numpy as np

def app():
     st.set_page_config(page_title='연도별 친환경차 등록 그래프', page_icon="📊")

     st.title("📊 연도별 친환경차 등록 그래프")
     st.subheader("2018년~2025년 사이의 전기차와 수소차의 비교")
     st.header('라인 차트')

     chart_data = pd.DataFrame(
          np.random.randn(20, 3),
          columns=['a', 'b', 'c'])

     st.line_chart(chart_data)







