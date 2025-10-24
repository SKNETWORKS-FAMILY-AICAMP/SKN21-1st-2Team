from database import db_connection
#from database import insert_data
#from src.database import fetch_data
import database.fetch_data as fs
from visualization import plot as pt


if __name__ == "__main__":

    pt.plot_graph()
    #plot.plot()

    # db_connection.get_connection()
    #insert_data.h2_faq("./../data/processed/h2_faq_clean.csv")
    #insert_data.annual_H2_ev_registrations("./../data/processed/annual_h2_ev_registrations.csv")
    #insert_data.h2_station_info("./../data/processed/h2_station_info_map.csv")
    #insert_data.h2_stations_by_region("./../data/processed/h2_stations_by_region_map.csv")
    #insert_data.ev_stations_by_region("./../data/processed/ev_stations_by_region_map.csv")
    #insert_data.region("./../data/processed/region.csv")

    
    # fetch_data.fetch_faq() # faq select test, 이후 주석처리해야함
    #fs.fetch_h2_station_info() # 수소차 충전소 조회
    #fs.fetch_h2_stations_by_region() #지역별 수소차 충전소 개수 조회
    #fs.fetch_annual_h2_ev_registrations() # 연도별 H2/EV 자동차 등록 현황 조회
    # fs.h2_stats()
    #fs.fetch_ev_stations_region() # 지역별 전기차 충전소 개수
    # fs.fetch_faq()
