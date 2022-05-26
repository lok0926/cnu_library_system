import pymysql


from config.config_db import connection_db


# 도서목록 조회
def get_books():


    conn = connection_db()  # Connection -> MariaDB