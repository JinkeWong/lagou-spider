from setting import log

logging = log()

class InfoBulider:

    def __init__(self,postion,city):
        self.__postion = postion
        self.__city = city

    def urlbulider(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?{}&needAd' \
              'dtionalResult=false'.format(self.__city)
        return url

    def headersbulider(self):
        headers = {
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&s'
                       'uginput='.format(self.__postion),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like' \
                          ' Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': None,
            'X-Requested-With': 'XMLHttpRequest'
        }
        return headers

    def databulider(self,page):
        logging.info('data bulider working')
        data = {'first': 'true', 'fn': {}, 'kd': '{}'.format(page, self.__postion)}
        return data