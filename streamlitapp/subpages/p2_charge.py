import os
import sys
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))  # SKN21-1ST-2TEAM
    
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
        sys.path.append(src_path)
        

import pandas as pd
import plotly.express as px

st.title("⛽지역별 충전소 분포")

# 시도별 위도/경도 데이터
def app():
            data = {
                'region': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
                        '경기', '충북', '충남', '전북', '전남', '경북', '경남', '강원'],
                'lat': [37.5665, 35.1796, 35.8714, 37.4563, 35.1595, 36.3504, 35.5384, 36.4800,
                        37.4138, 36.6357, 36.5184, 35.7175, 34.8679, 36.4919, 35.2383, 37.8228],
                'lon': [126.9780, 129.0756, 128.6014, 126.7052, 126.8526, 127.3845, 129.3114, 127.2890,
                        127.5183, 127.4917, 126.8000, 127.1530, 126.9910, 128.8889, 128.6924, 128.1555]
            }

            df = pd.DataFrame(data)

            st.subheader("대한민국 시·도 지도")
            st.map(df)


            # 예시 데이터
            data = {
                "city": ["서울", "부산", "대구"],
                "lat": [37.5665, 35.1796, 35.8714],
                "lon": [126.9780, 129.0756, 128.6014],
                "value1": [60, 30, 50],
                "value2": [40, 70, 50],
            }

            df = pd.DataFrame(data)
            df["total"] = df["value1"] + df["value2"]
            df["ratio"] = df["value1"] / df["total"]

            # scattermapbox로 원 크기와 색깔로 비율 표시
            fig = px.scatter_mapbox(
                df,
                lat="lat",
                lon="lon",
                size="total",  # 원 크기
                color="ratio",  # 색상(0~1 비율)
                color_continuous_scale=px.colors.sequential.Plasma,
                size_max=30,
                zoom=5,
                mapbox_style="carto-positron",
                hover_name="city",
                hover_data={"value1": True, "value2": True, "ratio": ':.2f'},
            )

            st.plotly_chart(fig)


#"지도에 원형그래프를 넣고 싶다. 어떻게 구현하지?
# 비슷한 폼을 찾긴 했는데, pip install plotly  필요.
# 지역별 위도 및 경도 데이터 찾아옴.
#. gpt야.. 모르겠어 ㅋㅋㅋㅋㅋㅋㅋㅋ