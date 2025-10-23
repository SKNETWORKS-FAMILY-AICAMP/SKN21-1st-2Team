# src/crawling/faq_data_crawler

"""
Author: Jung Deokkyu
Date: 2025-10-23
Description: 수소차 (충전소) 관련 정부 지원 정보 제공 FAQ 크롤러
 
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument("--headless") # not to open browser

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service,options=option)

browser.implicitly_wait(3)
browser.maximize_window()

browser.get('https://ev.or.kr/nportal/partcptn/initFaqAction.do') # 무공해차 통합누리집
crawling_list = []

try:
    browser.find_element(By.ID, "3").click() # "수소충전소 인프라 사업"

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "contentList")))  # Loading

    for i in range(1,3):

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        qna_section = soup.find_all('div', class_='board_faq')
        if not qna_section:
            print("There is no Q&A section!")

        # crawling
        for qna in qna_section:
            question = qna.find('div', class_='title')  # Question
            answer = qna.find('div', class_='faq_con')  # Reply

            if question and answer:
                Q = question.text.strip()
                A = answer.text.lstrip("A")
                print("Q: ", Q)
                print("A: ", A)
                crawling_list.append([Q,A])
                print("-" * 50)



        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pageList"))) # Loading

        if i == 1:
            browser.find_element(By.LINK_TEXT, '2').click()  # Turn to next page

        time.sleep(1)


finally:
    df = pd.DataFrame.from_records(crawling_list)
    df.to_excel('../../data/processed/H2_FAQ.xlsx')
    browser.close() # exit browser

