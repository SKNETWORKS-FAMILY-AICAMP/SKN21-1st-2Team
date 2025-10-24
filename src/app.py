from database import db_connection
from database import insert_data

import database.fetch_data as fs

from visualization import plot

if __name__ == "__main__":
    #insert_data.h2_FAQ("data\processed\h2_faq.csv")
    # insert_data.annual_H2_ev_registrations("data\processed\\annual_h2_ev_registrations.csv")
    # insert_data.h2_station_info("data\processed\h2_station_info.csv")
    # insert_data.h2_station_by_region("data\processed\h2_stations_by_region.csv")
    # insert_data.ev_station_by_region("data\processed\ev_stations_by_region.csv")

    plot.plot()