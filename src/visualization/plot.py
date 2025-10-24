import pandas as pd
import io

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import ScalarFormatter

from database import fetch_data

def plot():
    df = fetch_data.fetch_annual_h2_ev_registrations()  # DB에서 데이터 불러오기
    print(df)
    font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False

    #scale 설정
    formatter = ScalarFormatter(useMathText=False)
    formatter.set_scientific(False)

    #수소차 연도별
    plt.figure(figsize=(10, 5))
    plt.plot(df["year"], df["h2_car_total"], marker="o", label="수소차 개수", color="blue")
    plt.title("연도별 수소차 개수", fontsize=16)
    plt.xlabel("연도")
    plt.ylabel("차량 대수")
    plt.grid(True)
    plt.legend()
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()

    #전기차 연도별
    plt.figure(figsize=(10, 5))
    plt.plot(df["year"], df["ev_car_total"], marker="o", label="전기차 개수", color="green")
    plt.title("연도별 전기차 개수", fontsize=16)
    plt.xlabel("연도")
    plt.ylabel("차량 대수")
    plt.grid(True)
    plt.legend()
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()

#     #수소차 연도별 
#     plt.figure(figsize=(10, 5))
#     plt.plot(df["year"], df["h2_car_total"], marker="o", label="수소차 개수", color="blue")
#     plt.title("연도별 수소차 개수", fontsize=16)
#     plt.xlabel("연도")
#     plt.ylabel("차량 대수")
#     plt.grid(True)
#     plt.legend()
#     plt.gca().yaxis.set_major_formatter(formatter)
#     plt.show()

#     #전기차 연도별
#     plt.figure(figsize=(10, 5))
#     plt.plot(df["year"], df["ev_car_total"], marker="o", label="전기차 개수", color="green")
#     plt.title("연도별 전기차 개수", fontsize=16)
#     plt.xlabel("연도")
#     plt.ylabel("차량 대수")
#     plt.grid(True)
#     plt.legend()
#     plt.gca().yaxis.set_major_formatter(formatter)
#     plt.show()

#     # print("123")


def plot_graph():
    conn = get_connection()

    df = fetch_data.fetch_annual_h2_ev_registrations()

    if df.empty:
        print("데이터가 없습니다. 그래프를 그릴 수 없습니다.")
    else:
        # --- Mac 한글 폰트 설정
        font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
        font_prop = font_manager.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
        plt.rcParams['axes.unicode_minus'] = False

        # --- y축 숫자 그대로 표시
        formatter = ScalarFormatter(useMathText=False)
        formatter.set_scientific(False)

        # --- 수소차 연도별 그래프
        plt.figure(figsize=(10,5))
        plt.plot(df["year"], df["h2_car_total"], marker="o", label="수소차 개수", color="blue")
        plt.title("연도별 수소차 개수", fontsize=16)
        plt.xlabel("연도")
        plt.ylabel("차량 대수")
        plt.grid(True)
        plt.legend()
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()

        # --- 전기차 연도별 그래프
        plt.figure(figsize=(10,5))
        plt.plot(df["year"], df["ev_car_total"], marker="o", label="전기차 개수", color="green")
        plt.title("연도별 전기차 개수", fontsize=16)
        plt.xlabel("연도")
        plt.ylabel("차량 대수")
        plt.grid(True)
        plt.legend()
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()



    # --- 전기차 연도별 그래프
    plt.figure(figsize=(10,5))
    plt.plot(df["year"], df["ev_car_total"], marker="o", label="전기차 개수", color="green")
    plt.title("연도별 전기차 개수", fontsize=16)
    plt.xlabel("연도")
    plt.ylabel("차량 대수")
    plt.grid(True)
    plt.legend()
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()