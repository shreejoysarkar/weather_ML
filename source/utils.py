import os
import sys
from source.exception import CustomException
from source.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host=os.getenv('host')
user = os.getenv('user')
passs = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info('reading sql database started')
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password = passs ,
            db = db
        )

        logging.info("connection established", mydb)
        df = pd.read_sql_query('SELECT * FROM weather_dataset',mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)
    
    
