import os
import sys
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))  # SKN21-1ST-2TEAM
    
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
        sys.path.append(src_path)


import streamlit as st
import pandas as pd
from database import fetch_data


def app(): 
        st.title("❓ 자주 묻는 질문들")
        

        #print(fetch_data.fetch_data())
        #with st.expander():
           # st.write() 


faq_data = fetch_data()

# 데이터가 존재하면 질문을 선택할 수 있는 드롭다운 메뉴 생성
if not faq_data.empty:
    questions = faq_data['question'].tolist()
    
    # 사용자가 질문을 선택할 수 있는 드롭다운 메뉴
    selected_question = st.selectbox("질문을 선택하세요:", questions)

    # 선택된 질문에 대한 답변 표시
    if selected_question:
        # 해당 질문에 대한 답변 찾기
        selected_answer = faq_data[faq_data['question'] == selected_question]['answer'].values[0]
        st.write(f"**답변**: {selected_answer}")
else:
    st.write("FAQ 데이터가 없습니다.")

