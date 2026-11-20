from loguru import logger
import os


LOG_DIR = os.path.join(os.getcwd(),'logs')
os.makedirs(LOG_DIR,exist_ok=True)

BASIC_LOG_FILE = os.path.join(LOG_DIR,'basic.log')


logger.add(BASIC_LOG_FILE, level='DEBUG',
           format='''<green>{time:YYYY-MM-DD HH:mm:ss.SSS Z}</green> | 
           <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'''
           )

logger.info('Logging Initialized')

