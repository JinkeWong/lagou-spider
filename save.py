import threading,csv
from threading import Lock
from pathlib import Path
from setting import log

logging = log()
class Saver:
    def __init__(self):
        self.__lock = Lock()
        self.__path = Path('reslut.csv')
        self.__columname = ['positionName', 'positionId', 'salary', 'workYear', 'education', 'stationname',
                       'jobNature', 'createTime', 'companyShortName', 'companyFullName', 'financeStage',
                       'companySize', 'companyId', 'link']

    def reslut_saver(self,page_reslut):
        logging.info('reslut saving')
        with self.__lock:
            with open(self.__path, 'a+') as f:
                writer = csv.writer(f)
                writer.writerows(page_reslut)

    def column_name_saver(self):
        with self.__lock:
            with open(self.__path, 'a+') as f:  # 存入csv表头
                logging.info('write column name')
                writer = csv.writer(f)
                writer.writerow(self.__columname)
                logging.info('write done')