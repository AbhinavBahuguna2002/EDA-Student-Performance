'''
This code generates a timestamped log file name, configures the logging system to write log messages to the generated log file, 
and specifies the format and logging level for the log messages.

'''

import logging
import os 
from datetime import datetime 

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH= os.path.join(logs_path, LOG_FILE)

logging.basicConfig (

    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level= logging.INFO, 
)
