import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Database():
    def __init__(self):
        try:
            self.conn =  psycopg2.connect(                                                  
                user = os.getenv("DB_USER"),                                      
                password = os.getenv("DB_PASSWORD"),                                  
                host = os.getenv("DB_HOST"),                                            
                port = os.getenv("DB_PORT"),                                          
                database = os.getenv("DB_NAME")                                       
            )
            self.cur = self.conn.cursor()
        except:
            print("Cannot connect to database")    

    def get_stickers(self):
        self.cur.execute("SELECT * FROM stickers")
        stickers = self.cur.fetchall()
        self.close()
        return stickers

    def close(self):
        self.cur.close()
        self.conn.close()    
