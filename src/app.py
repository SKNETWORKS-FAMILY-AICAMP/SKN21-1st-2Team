from database import db_connection
from database import insert_data
from database import fetch_data
from visualization import plot

if __name__ == "__main__":

    # 수소차 연도별 line plot
    # plot.h2_line_plot()

    # 전기차 연도별 line plot
    # plot.ev_line_plot()

    # 수소차 충전소 지역별 pie plot
    # plot.station_pie_plot()


    db_connection.get_connection()


    # 데이터 insert(1회)
    # insert_data.region("data\processed\\region.csv")
    # insert_data.h2_faq("data\processed\h2_faq_clean.csv")
    # insert_data.annual_h2_ev_registrations("data\processed\\annual_h2_ev_registrations.csv")
    # insert_data.h2_station_info("data\processed\h2_station_info_map.csv")
    # insert_data.h2_stations_by_region("data\processed\h2_stations_by_region_map.csv")
    # insert_data.ev_stations_by_region("data\processed\ev_stations_by_region_map.csv")
    
    # fetch_data.fetch_faq() # faq select test, 이후 주석처리해야함
    # fetch_data.fetch_h2_station_info() # 수소차 충전소 조회
    # fetch_data.fetch_annual_h2_ev_registrations() # 연도별 H2/EV 자동차 등록 현황 조회
    # fetch_data.h2_stats() # 지역별 수소, 전기차 충전소 개수
    # fetch_data.fetch_h2_stations_by_region() #지역별 수소차 충전소 개수 조회
    #fetch_data.fetch_ev_stations_region() # 지역별 전기차 충전소 개수
