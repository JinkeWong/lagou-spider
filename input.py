from urllib.parse import urlencode
from setting import log

logging = log()

def ask_to_input(): #获取查询职位及地区
    postion = input('输入您想查询的职位名称：')
    while not postion:
        postion = input('未输入内容，请重新输入：')
    postion = urlencode({'postion': postion}, encoding='utf-8').split('=')[1]
    print(postion)

    city = input('请输入您想查询的城市：')
    while not city:
        city = input('未输入内容，请重新输入：')
    city = urlencode({'city':city})
    logging.info('get input,start crawling {} jobs in {}'.format(postion,city))
    return postion, city