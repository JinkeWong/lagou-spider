import requests,math
from setting import log

logging = log()

class LagouSpider:
    def __init__(self,url,headers):
        self.__url = url
        self.__headers = headers

    def get_json(self, data):  # 发送post请求，获取response并提取json
        logging.info('json getting')
        response = requests.post(data=data,url=self.__url,headers=self.__headers)
        response.encoding = 'utf-8'
        job_info = response.json()
        if not job_info['success'] == 'flase':
            logging.info('get_json success')
            return job_info

    @staticmethod
    def parse_json(job_info):  # 解析json，获取需要信息
        logging.info('json parsing')
        job_info = job_info['content']['positionResult']['result']
        print(type(job_info))
        page_result = []
        for i in range(len(job_info)):
            print(type(job_info))
            job_infor = job_info[i]
            print(type(job_infor), type(job_info))
            job_result = []
            job_result.append(job_infor['positionName'])  # 职位名
            job_result.append(job_infor['positionId'])  # 职位id
            job_result.append(job_infor['salary'])  # 薪水
            job_result.append(job_infor['workYear'])  # 经验
            job_result.append(job_infor['education'])  # 学历
            job_result.append(job_infor['stationname'])  # 地区
            job_result.append(job_infor['jobNature'])  # 工作性质
            job_result.append(job_infor['createTime'])  # 发布时间
            job_result.append(job_infor['companyShortName'])  # 公司简称
            job_result.append(job_infor['companyFullName'])  # 公司全称
            job_result.append(job_infor['financeStage'])  # 融资
            job_result.append(job_infor['companySize'])  # 公司规模
            job_result.append(job_infor['companyId'])  # 公司id
            job_result.append('https://www.lagou.com/jobs/{}.html'.format(str(job_infor['positionId'])))  # 职位链接
            page_result.append(job_result)
        return page_result

    @staticmethod
    def get_pagenum(job_info):  # 从json中提取出页数
        logging.info('pagenum getting')
        total_count = job_info['content']['positionResult']['totalCount']
        total_pages = math.ceil(total_count / 15)  # 除以15，向上取整
        if total_pages > 30:  # 拉勾最多显示30页
            total_pages = 30
        return total_pages