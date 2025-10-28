import matplotlib.pyplot as plt
from matplotlib import rc
from database import fetch_data
import pandas as pd

rc('font', family='Malgun Gothic')  
plt.rcParams['axes.unicode_minus'] = False

# 수소차 연도별
def h2_line_plot():
    data = fetch_data.fetch_annual_h2_ev_registrations()  # DB에서 데이터 불러오기
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize = (10, 5))

    ax.plot(df["year"], df["h2_car_total"], marker='o', color='blue', label='수소차')
    
    ax.set_xlabel("연도")
    ax.set_ylabel("등록 대수")
    ax.set_title("연도별 수소차 등록 대수")
    ax.legend()
    ax.grid(True)

    return fig

# 전기차 연도별
def ev_line_plot():
    data = fetch_data.fetch_annual_h2_ev_registrations()  # DB에서 데이터 불러오기
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize = (10, 5))

    ax.plot(df["year"], df["ev_car_total"], marker='o', color='red', label='전기차')
    
    ax.set_xlabel("연도")
    ax.set_ylabel("등록 대수")
    ax.set_title("연도별 전기차 등록 대수")
    ax.legend()
    ax.grid(True)
    
    return fig

# 지역별 수소차 충전소 개수
def station_pie_plot():
    data = fetch_data.fetch_h2_stations_by_region()
    df = pd.DataFrame(data, columns=["region", "number_of_station"])
    fig, ax = plt.subplots(figsize=(8, 8))

    ratio = df['number_of_station'].astype(int)
    labels = df['region']
    

    explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    ax.set_title("지역별 수소차 충전소 비율")
    ax.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode)
    ax.legend(loc = (1, 0.7))
    
    return fig