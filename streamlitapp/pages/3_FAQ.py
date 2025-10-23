import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Select Box")
####### selectbox
option = st.selectbox(
    "지역을 선택하세요",
    ("서울", "인천", "부산", "광주"),
    # index=None
)
st.write("**선택한 지역**:", option)