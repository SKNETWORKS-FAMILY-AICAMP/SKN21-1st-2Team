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


# 시도별 위도/경도 데이터
def app():
        st.title("⛽지역별 충전소 분포")

        station_pie_fig = plot.station_pie_plot()
        st.pyplot(station_pie_fig)
