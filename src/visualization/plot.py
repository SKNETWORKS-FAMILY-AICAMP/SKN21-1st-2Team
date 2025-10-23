import pandas as pd
import matplotlib.pyplot as plt
import io

# DB에서 연도별/수소차 등록 데이터 불러오기"
# 쿼리문구 작성해야함
# 박민정씨는 plot.py 에서 함수를 가져가서 출력물을 보이면 됩니다. 아래 주석 참고
# import streamlit as st
# from src.visualization.trend_plot import get_vehicle_trend_data, plot_vehicle_trend
# from src.database.db_connection import get_connection

# conn = get_connection()
# df = get_vehicle_trend_data(conn)
# fig = plot_vehicle_trend(df)
# st.pyplot(fig)

def get_vehicle_trend_data(conn):
    query = """
    SELECT year, type, SUM(count) as total
    FROM vehicle_data
    GROUP BY year, type
    ORDER BY year;
    """
    df = pd.read_sql(query, conn)
    return df

# 시각화용 Matplotlib 그래프 생성
# 쿼리문구 작성해야함
def plot_vehicle_trend(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    for t in df['type'].unique():
        temp = df[df['type'] == t]
        ax.plot(temp['year'], temp['total'], marker='o', label=t)
    ax.set_title("전기차/수소차 연도별 등록 추세")
    ax.set_xlabel("연도")
    ax.set_ylabel("등록 대수")
    ax.legend()
    plt.tight_layout()
    return fig