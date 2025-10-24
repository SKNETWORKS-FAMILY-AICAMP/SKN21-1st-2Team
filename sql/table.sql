SHOW TABLES;

DROP table IF exists region;
CREATE TABLE region
(
	region_id 	INT 		NOT NULL COMMENT '지역 식별 코드',
    region 		VARCHAR(20) NOT NULL COMMENT '지역',
    primary KEY (region_id)
) COMMENT '지역 식별';

DROP table IF exists h2_FAQ;
CREATE TABLE h2_FAQ
(
  faq_id   INT          AUTO_INCREMENT COMMENT '식별코드',
  question VARCHAR(500) NOT NULL COMMENT '질문',
  answer   VARCHAR(2000) NOT NULL COMMENT '답변',
  PRIMARY KEY (faq_id)
) COMMENT '수소차 충전소 인프라 FAQ';

DROP table IF exists annual_h2_ev_registrations;
CREATE TABLE annual_H2_ev_registrations
(
  year_id      	INT   AUTO_INCREMENT COMMENT '식별코드',
  year			varchar(10)  NOT NULL COMMENT '연도',
  h2_car_total 	INT  NULL     COMMENT '수소차  등록 대수',
  ev_car_total 	INT  NULL     COMMENT '전기차  등록 대수',
  PRIMARY KEY (year_id)
) COMMENT '연도별 H2/ EV 자동차 등록대수';

DROP table IF exists h2_stations_by_region;
CREATE TABLE h2_stations_by_region
(
  region_id         INT         NOT NULL COMMENT '지역 식별 코드',
  number_of_station INT         NOT NULL COMMENT '충전소 개수',
  foreign key (region_id) REFERENCES region(region_id)
) COMMENT '지역별 수소차 충전소 개수';

DROP table IF exists ev_stations_by_region;
CREATE TABLE ev_stations_by_region
(
  region_id         INT  NULL COMMENT '지역 식별 코드',
  number_of_station INT  NOT NULL COMMENT '충전소 개수',
  foreign key (region_id) REFERENCES region(region_id)
) COMMENT '지역별 전기차 충전소 개수';

DROP table IF exists h2_station_info;
CREATE TABLE h2_station_info
(
  station_id   INT         AUTO_INCREMENT COMMENT '식별코드',
  station_name VARCHAR(100)NOT NULL COMMENT '충전소 이름',
  price        INT         NULL     COMMENT '충전 가격',
  tel          VARCHAR(20) NULL     COMMENT '전화번호',
  region_id    INT         			COMMENT '지역 식별 코드',
  PRIMARY KEY (station_id),
  foreign key (region_id) REFERENCES region(region_id)
) COMMENT '수소차 충전소 정보';

/*
-- CONSTRAINT 제약조건 조회
-- PK, FK 조회
select * from information_schema.table_constraints
where TABLE_NAME = 'h2_station_info';
*/