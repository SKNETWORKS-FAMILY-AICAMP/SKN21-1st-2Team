# SKN21-1st-2Team

1️⃣ 팀 소개

팀명: NeedH2

팀원 & GitHub

| 이름   | 업무            | GitHub |
|:-----:|:---------------:|:------:|
| 이명준 | DB              | [nature0022](https://github.com/nature0022) |
| 박민정 | Frontend        | [silentkit12w](https://github.com/silentkit12w) |
| 우재현 | Backend         | [Wjaehyun](https://github.com/Wjaehyun) |
| 안혜빈 | Data Processing | [hyebinhy](https://github.com/hyebinhy) |
| 정덕규 | Web Crawling    | [duck213](https://github.com/duck213) |

세부 담당 업무

정덕규: 데이터 크롤링 (FAQ)    Selenium으로 정부지원 FAQ 수집, 백앤드(DB 데이터 insert, fetch)

안혜빈: 데이터 전처리            CSV 정리, 결측치 처리, 표준화

우재현: 백엔드 (핵심 데이터 로직, DB 연동, 설정 관리, 시각화 백단)    MySQL 연결, config 관리, 데이터 insert/select API, 시각화용 데이터 가공

이명준: 데이터베이스 설계 및 구축    ERD 설계, 테이블 생성, 스키마 구축

박민정: Streamlit 프론트엔드    UI/UX 구성, 차트 시각화, 페이지 이동

2️⃣ 프로젝트 개요
#### 프로젝트 명
    국내 친환경 자동차 비교분석과 수소차 지원 정보 서비스


#### 프로젝트 목표
1. 지역별 수소차 소유자의 관리 편리성 및 근접성 확보
2. 충전소 위치 정보 확인을 통해 수소차 방전 위험성 감소
3. 정부의 친환경 정책에 대비하여 수소차 구매 독려 및 인프라 확충


#### 주요 목표 기능

    📈📉📊📋 전기차/ 수소차 연도별 증감 추세 도식화

    📊 전기차충전소/수소차충전소 그래프 도식화

    📋 수소차 (충전소) 관련 정부 지원 정보 제공 FAQ

    🔍전국구 수소차 충전소 지역별로 조회



#### 📂 프로젝트 구조
│
├── 📁 data/                # 데이터 관련 폴더
│   ├── raw/                # 크롤링 원본 데이터 (엑셀, csv 등)
│   ├── processed/          # 전처리 후 데이터
│   └── db_dump/            # MySQL 백업 파일 (.sql)
│

├── 📁 src/                 # 주요 파이썬 소스코드
│   ├── crawling/           # Selenium 크롤링 스크립트
│   │   ├── ev_data_crawler.py
│   │   ├── hydrogen_data_crawler.py
│   │   ├── station_data_crawler.py
│   │   └── faq_data_crawler.py
│   │
│   ├── database/           # MySQL 연동 관련 코드
│   │   ├── db_config.py    # DB 연결 정보 (환경변수로 관리)
│   │   ├── db_schema.sql   # 테이블 생성 쿼리
│   │   └── db_utils.py     # insert/select 등 함수
│   │
│   ├── preprocessing/      # 데이터 정제, 전처리 코드
│   │   ├── clean_ev_data.py
│   │   ├── merge_trends.py
│   │   └── utils.py
│   │
│   └── visualization/      # 시각화 및 분석 코드
│       ├── plot_trends.py
│       ├── plot_station_map.py
│       └── chart_utils.py
│

├── 📁 streamlitapp/        # 서비스 페이지 관련 코드
│   ├── Home.py              # 메인 페이지
│   ├── pages/
│   │   ├── 1📈연도별증감추세.py
│   │   ├── 2⛽충전소분포.py
│   │   ├── 3💬FAQ정보.py
│   │   └── 4📍충전소_조회.py
│   └── components/          # 공통 컴포넌트 (그래프, 지도 등)
│       ├── chart_block.py
│       ├── map_view.py
│       └── faq_display.py
│

├── 📁 docs/                 # 문서 및 기획자료
│   ├── ERD.png
│   ├── data_sources.md
│   ├── project_plan.md
│   └── requirements.md
│

├── .env.example             # 환경변수 예시 (DB 접속정보, API키)
├── requirements.txt         # 필요 패키지 목록
├── README.md                # 프로젝트 개요 및 실행 방법
└── LICENSE                  # 라이선스 (MIT 권장)


---

##  ERD


##  수행결과(테스트/시연 페이지)
---

별도로 시연(?)




⚡이슈 해결 과정

JavaScript 항목 웹 크롤링 일부 해결
csv, 전처리 수정, DB 재설계


🔎 아쉬운점 & 개선점

DB 테이블 재설계로 인한 시간 및 비용 초과

궁금한 점 있으면 연락주세요. 