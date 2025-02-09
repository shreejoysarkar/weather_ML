from source.logger import logging
from source.exception import CustomException
import sys
if __name__=="__main__":
    logging.info('the excetur')

    try :
        a=1/0
    except Exception as e:
        logging.info('CustomException')
        raise CustomException(e,sys)