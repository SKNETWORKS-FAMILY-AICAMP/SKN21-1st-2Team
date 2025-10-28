import os
import sys
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))

src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.append(src_path)

from app import select_optional_station


import pandas as pd
import numpy as np


def app():
        st.subheader("📍충전소를 찾을 지역을 선택하세요")
        option = st.selectbox(
            " ",
            ("서울", "인천", "부산", "광주","대전","울산","세종","경기","충북","충남","전북","전남","경북","경남","강원"
        ),
        )
        
        st.write("선택한 지역:", option)
        # st.write(project_root, src_path)

        df_select_optional_station = pd.DataFrame(select_optional_station(option))
        st.dataframe(df_select_optional_station)


#. 지역을 선택하면, 데이터를 불러오게 만들 방법 찾기.
#. 도출되는 데이터는 표로 구성하기. (위치 별 가나다 순 정렬이 가능할까? ex) 강원도 > 원주시 > ㅇㅇ동 끼리 모은다던지.. 근데 모을 게 있긴 한가.))