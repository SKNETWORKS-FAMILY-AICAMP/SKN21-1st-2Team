from database import db_connection
from database import insert_data
<<<<<<< HEAD
from database import fetch_data
from src.database import fetch_data

=======
import database.fetch_data as fs
>>>>>>> a3845bc6289c662da8add65d3db38ac17961d731

if __name__ == "__main__":
    # insert_data.h2_FAQ("data\processed\h2_faq.csv")
    # insert_data.annual_H2_ev_registrations("data\processed\\annual_h2_ev_registrations.csv")
    # insert_data.h2_station_info("data\processed\h2_station_info.csv")
    # insert_data.h2_station_by_region("data\processed\h2_stations_by_region.csv")
    # insert_data.ev_station_by_region("data\processed\ev_stations_by_region.csv")
<<<<<<< HEAD
    
    fetch_data.fetch_faq() # faq select test, 이후 주석처리해야함
=======

    #fs.fetch_h2_station_info() # 수소차 충전소 조회
    #fs.fetch_h2_stations_by_region() #지역별 수소차 충전소 개수 조회
    #fs.fetch_annual_h2_ev_registrations() # 연도별 H2/EV 자동차 등록 현황 조회

    fs.h2_stats()
    #fs.fetch_ev_stations_region() # 지역별 전기차 충전소 개수
    #fs.fetch_faq()
>>>>>>> a3845bc6289c662da8add65d3db38ac17961d731
