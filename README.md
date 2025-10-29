# SKN21-1st-2Team
---
## 1. 팀 소개

`팀명: NeedH2`

`팀원 & GitHub`
 
|| 이름   | 업무            | GitHub |       세부사항     |
|:-----:|:---------------:|:------:| :---------------:|:----------:|
|<img src="https://icons.veryicon.com/png/o/internet--web/digital-monster/tokomon.png" alt=tokomon\ width="64px" height="64px">| 이명준 | DB              | [nature0022](https://github.com/nature0022) | 팀장, git builder, ERD 설계, 테이블 생성, 스키마 구축, 데이터 포멧 설계, sql query 작성, 조회 page (back, front)  |
|<img src="https://icons.veryicon.com/png/o/internet--web/digital-monster/koromon.png" alt=agumon\ width="64px" height="64px">| 박민정 | Frontend        | [silentkit12](https://github.com/silentkit12) | UI/UX 구성, 차트 시각화, 페이지 이동
|<img src="https://icons.veryicon.com/png/o/internet--web/digital-monster/tentomon.png" alt=tentomon\ width="64px" height="64px">| 우재현 | Backend         | [Wjaehyun](https://github.com/Wjaehyun) | MySQL 연결, config 관리, 데이터 insert/select API, 시각화용 데이터 가공
|<img src="https://icons.veryicon.com/png/o/internet--web/digital-monster/koromon.png" alt=agumon\ width="64px" height="64px">| 안혜빈 | Data processing | [hyebinhy](https://github.com/hyebinhy) |  CSV 정리, 결측치 처리, 표준화  |
|<img src="https://icons.veryicon.com/png/o/internet--web/digital-monster/koromon.png" alt=agumon\ width="64px" height="64px">| 정덕규 | Web Crawling    | [duck213](https://github.com/duck213) |  Selenium으로 정부지원 FAQ 수집, 백앤드(DB 데이터 insert, fetch)  |

---

## 2. 프로젝트 개요
### 2.1. 프로젝트 명
    국내 친환경 자동차 비교분석과 수소차 지원 정보 서비스


### 2.2. 프로젝트 목표
1. 지역별 수소차 소유자의 관리 편리성 및 근접성 확보
2. 충전소 위치 정보 확인을 통해 수소차 방전 위험성 감소
3. 정부의 친환경 정책에 대비하여 수소차 충전소 인프라 확충
4. 연도별 친환경차 등록대수 비교를 통해 수소차 구매 독려


### 2.3. 주요 목표 기능

    📈 웹 크롤링(Beautifulsoup, Selenium)과 MySQL 기반 통계 수치화

    📊 전기차/수소차 및 충전소 연도별 증감 추세 그래프 도식화

    📋 수소차 충전소 관련 정부 지원 정보 제공 FAQ

    🔍 전국구 수소차 충전소 지역별로 조회


---

## 3. 프로젝트 설계 

### 3.1. 프로젝트 디렉토리 구조

```
├── README.md                      # 프로젝트 개요 및 실행 가이드
├── requirements.txt               # 의존성 패키지 목록
├── tree.txt                       # 전체 디렉토리 트리
│
├── data/                          # 원본(raw) 및 전처리(processed) 데이터 저장 폴더
├── docs/                          # 참고 문서 및 이미지 등 자료
├── images/                        # Streamlit 페이지용 GIF 및 시각 자료
├── sql/                           # SQL 쿼리 및 테이블 스키마 정의
│
├── src/                           # 백엔드 및 데이터 처리 로직
│   ├── __init__.py
│   ├── app.py                     # 메인 실행 스크립트 (DB 삽입 등 실행)
│   ├── ex.ipynb                   # 테스트/예시용 노트북
│   │
│   ├── config/                    # 설정 관련 모듈
│   │   ├── __init__.py
│   │   └── config.py              # DB, 경로, 로그, 앱 환경 설정
│   │
│   ├── crawling/                  # 데이터 크롤링 모듈
│   │   └── faq_data_crawler.py    # 정부 FAQ 데이터 수집 스크립트
│   │
│   ├── database/                  # DB 연동 관련 모듈
│   │   ├── __init__.py
│   │   ├── db_connection.py       # MySQL 연결 설정
│   │   ├── fetch_data.py          # DB에서 데이터 조회 함수
│   │   ├── insert_data.py         # CSV → DB 삽입 함수
│   │   └── 참고자료.txt
│   │
│   ├── preprocessing/             # 데이터 전처리 관련 모듈
│   │   └── preprocess.py          # CSV 파일 전처리 및 정제 로직
│   │
│   └── visualization/             # 그래프 및 시각화 모듈
│       ├── __init__.py
│       ├── plot.py                # matplotlib 기반 시각화 코드
│       └── 참고자료.txt
│
└── streamlitapp/                  # Streamlit 프론트엔드 애플리케이션
    ├── __init__.py
    ├── home.py                    # 홈 화면
    └── subpages/                  # 서브 페이지
        ├── __init__.py
        ├── p1_graph.py            # 전기차/수소차 통계 그래프
        ├── p2_charge.py           # 충전소 위치 시각화
        ├── p3_faq.py              # FAQ 조회 페이지
        └── p4_search.py           # 지역별 충전소 검색 페이지
```
### 3.2. ERD

<img width="1200" height="400" alt="ERD" src="https://github.com/user-attachments/assets/0bb1e200-1b26-45fc-8b44-5ad1a95ce792" />


### 3.3. 테이블 요약
| `entity` | `info` | `attribute` | `relationship` |
| :--- | :--- | :--- | :--- |
| **`region`** | 지역 정보 | `region` (PK), `region_id` | |
| **`h2_stations_by_region`** | 지역별 수소차 충전소 개수 | `region_id` (FK), `number_of_station` | region (1:1)|
| **`ev_stations_by_region`** | 지역별 전기차 충전소 개수 | `region_id` (FK), `number_of_station` | region (1:1)|
| **`ev_station_info`** | 수소차 충전소 정보 | `station_id` (PK), `region_id` (FK), `station_name`, `price`, `tel` | region (1:N)|
| **`annual_h2_ev_registrations`** | 연도별 h2/ev 자동차 등록대수 | `year_id` (PK), `year`, `h2_car_total`, `ev_car_total` |   |
| **`h2_faq`** | 수소 충전소 정부 인프라 제공 관련 FAQ | `faq_id` (PK), `question`, `answer`  | |

---

## 4️. 수행결과(테스트/시연 페이지)

 0. 홈
 <img width="1200" height="400" alt="home" src=".//images/0_home.gif" >
 1. 전기차/수소차 연도별 등록수 증감 추세 그래프 도식화
<img width="1200" height="400" alt="statics" src=".//images/1_statics.gif" />
 2. 지역별 수소차 충전소 통계 수치화
<img width="1200" height="400" alt="graph" src=".//images/2_graph.gif" />
 3. 수소차 충전소 관련 정부 지원 정보 제공 FAQ
<img width="1200" height="400" alt="faq" src=".//images/3_faq.gif" />
 4. 수소차 충전소 지역별로 조회
<img width="1200" height="400" alt="select" src=".//images/4_select.gif" />


---

## 💭 회고록

#### `이명준`
>  팀장을 맡았지만 팀원을 이끌어 감에 있어서, 부족함이 정말 많았던 것 같습니다. 
> 프로젝트 중에는 첫 날에 데이터 분석, 데이터 전처리 형식 작성, .env, .gitignore, requirements 등 프로젝트에 필요한 builder를 했던 것 같습니다. 두 번째 날에는 erd 구축 및 수정, db insert, fetch 등을 도왔습니다.  
>  
> 프로젝트 종단에는 미쳐 마무리 하지 못했던 back과 front의 연결을 직접 해보며, top-down structure의 package import error를 직접 겪어가며 상위/하위 디렉토리 구조, 상대경로와 절대경로에 대한 공부를 하게 되었습니다. 또 python io system의 기본이 되는 os, sys 등의 library의 소중함도 소소하게나마 알게되었습니다.
> 
> 사실 자동차 domain 지식이 너무도 부족하여, 미약하게 나마 데이터 분석을 하고 전처리를 부탁드렸습니다. 수소차, 수소차 충전소에 관한 통계같은 domain 지식에 대해 아는게 없어서, 완결된 형태의 ERD가 쉽게 설계되지 않아 ERD 수정을 하게 된 점을 정말 팀원 분 들에게 죄송하게 생각했습니다.
> 
> 그래도 프로젝트 중 ERD 수정을 하며 SQL 문에 대한 이해와, PK, FK, 각 entity간의 relation을 다루는 데에 익숙해진 것을 다행으로 생각합니다.
>  
> 이번에는 프로젝트의 허브가 되는 DB를 해봤으니, 다음 프로젝트에는 꼭 Front와 back 둘 중에 하나를 담당하고 싶습니다.
> 또한 다음 프로젝트에서는 설계단계에서 ERD 설계, 프로젝트 디렉토리 트리의 설계, Front에 보여질 목업, 함수명-변수명의 통일, git branch-main merge 등을 할 수 있게끔 부족한 부분을 채워서 오겠습니다.
---

#### `박민정`
> 작성 중

---

#### `안혜빈`
> 작성 중

---

#### `우재현`
> 아키텍쳐 설정의 중요성 및 디렉토리 구조, 경로 설정 시 필요한 내용을 학습할 수 있었다. 코드의 작동 상태를 확인 후 패키지화 했어야 하는데, 패키지화를 먼저 하고 작동 여부를 확인하려 하니 디버깅에서 시간이 더 소요되어 프로젝트 진행이 상대적으로 더뎠다. 이 점을 보완하여 다음 프로젝트에 임하도록 하겠다.

---

#### `정덕규`

>먼저 팀원들과 어떤 주제로 시작할지 고민이 많았었는데 국내 수소차 인프라 확충이 필요해 보여서 이 프로젝트로 시작하게 되었습니다. 담당 업무는 웹 크롤링이었으며 처음부터 Javascript로 짜여진 페이지에서 원하는 데이터를 추출하기가 쉽진 않았습니다. 하지만 팀원들과 아이디어 및 진행 상황을 공유하고 피드백 받았던 일들이 많아지니 원하는 결과를 만들어 낼 수 있었습니다. 비록 역할분담 후 단기간에 많은 업무를 진행하여 몸이 지친 감이 있었으나 함께 프로젝트를 할 수 있다는 경험이 있기에 앞으로도 더 잘할 수 있을거라는 확신이 들었습니다.

---
