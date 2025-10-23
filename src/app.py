from database import db_connection
from database import insert_data

if __name__ == "__main__":
    insert_data.H2Faq("data\processed\h2_faq.csv")
    