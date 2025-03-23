from source.logger import logging
from source.exception import CustomException
from source.components.data_ingestion import DataIngestion
from source.components.data_ingestion import DataIngestionConfig

import sys
if __name__=="__main__":
    logging.info('the excetur')

    try :
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info('CustomException')
        raise CustomException(e,sys)