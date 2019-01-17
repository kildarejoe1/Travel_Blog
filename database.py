__author__="henry Morrin"
import psycopg2

class Database():
    @staticmethod
    def db_connect():
        conn=psycopg2.connect(database="Travel_blog",user="postgres", password="passwd", host="127.0.0.1", port="5432")
        print("Opened datbase successfully")
        return conn

    @staticmethod
    def db_table_create(conn_obj):
        cur=conn_obj.cursor()
        cur.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        blog_id          INT     NOT NULL,
        content TEXT,
        title         CHAR(50));''')
        print "Table created successfully"
        conn.commit()
        conn.close()

    def insert(self,collections, data):
        conn=Database.db_connect()
        with conn.cursor() as cursor:
            pass
        conn.commit()
        conn.close()
