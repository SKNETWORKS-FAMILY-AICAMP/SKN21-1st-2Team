# 전처리된 CSV 데이터를 MySQL 테이블에 저장하는 코드
# (전처리 담당자 안혜빈 씨가 만든 CSV를 DB로 옮김)

import pandas as pd
from database.db_connection import get_connection

#csv_path = h2_faq.csv
def h2_FAQ(csv_path):
    conn = get_connection()
    # df = pd.read_csv(csv_path)
    df = pd.read_csv(csv_path, names=["question", "answer"], header=0)
    print(df.columns)

    curs = conn.cursor()
    insert_sql = """
    INSERT INTO h2_faq (question, answer) 
    VALUES (%s, %s);
    """
    # for _, row in df.iterrows():
    #     curs.execute(insert_sql, (row["question"], row["answer"]))
        
    # curs.execute(insert_sql, "a", "b")    
    conn.commit()
    conn.close()


# #csv_path = annual_h2_ev_registrations.csv
# def annual_H2_ev_registrations(csv_path):
#     conn = get_connection()
#     df = pd.read_csv(csv_path, names=["year", "h2_car_total", "ev_car_total"], header=0)
#     print(df.columns)

#     curs = conn.cursor()
#     insert_sql = """
#     INSERT INTO annual_H2_ev_registrations (year, h2_car_total, ev_car_total) 
#     VALUES (%s, %s, %s);
#     """

#     # for _, row in df.iterrows():
#     #     curs.execute(insert_sql, (row["year"], row["h2_car_total"], row["ev_car_total"]))
        
#     conn.commit()
#     conn.close()


# #csv_path = h2_station_info.csv
# def h2_station_info(csv_path):
#     conn = get_connection()
#     df = pd.read_csv(csv_path, names=["station_name", "region", "price", "tel", "region_id"], header=0)
#     print(df.columns)

#     curs = conn.cursor()
#     insert_sql = """
#     INSERT INTO h2_station_info (station_name, region, price, tel, region_id) 
#     VALUES (%s, %s, %d, %s, %d);
#     """
#     # for _, row in df.iterrows():
#     #     curs.execute(insert_sql, (row["station_name"], row["region"], int(row["price"]), row["tel"], int(row["region_id"])))
        
#     conn.commit()
#     conn.close()


# #csv_path = h2_station_by_region.csv
# def h2_station_by_region(csv_path):
#     conn = get_connection()
#     df = pd.read_csv(csv_path, names=["region_id", "region", "number_of_station"], header=0)
#     print(df.columns)

#     curs = conn.cursor()
#     insert_sql = """
#     INSERT INTO h2_station_by_region (region_id, region, number_of_station) 
#     VALUES (%s, %s, %d);
#     """
#     # for _, row in df.iterrows():
#         # curs.execute(insert_sql, (row["region_id"], row["region"], int(row["number_of_station"])))
        
#     conn.commit()
#     conn.close()    


# #csv_path = ev_station_by_region.csv
# def ev_station_by_region(csv_path):
#     conn = get_connection()
#     df = pd.read_csv(csv_path, names=["region", "number_of_station", "region_id"], header=0)
#     print(df.columns)

#     curs = conn.cursor()
#     insert_sql = """
#     INSERT INTO ev_station_by_region (region, number_of_station, region_id) 
#     VALUES (%s, %s, %d);
#     """
#     # for _, row in df.iterrows():
#     #     curs.execute(insert_sql, (row["region"], int(row["number_of_station"]), row["region_id"]))
        
#     conn.commit()
#     conn.close()    