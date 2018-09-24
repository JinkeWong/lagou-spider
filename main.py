import save,infobulider,spider,random,time
from setting import log
from threading import Thread
from input import ask_to_input

logging =log()

def crow(bulider,sa,sp,startpage=2,totalpages=30,step=3):
    for i in range(startpage,totalpages+1,3):
        logging.info('start to crowing page {}'.format(i))
        data=bulider.databulider(i) #构建data
        try:
            reslut=sp.parse_json(sp.get_json(data=data))
        except KeyError:
            logging.info('keyerror raise,data={}'.format(data))
            reslut = data
        finally:
            sa.reslut_saver(reslut) #请求页面、获取json、解析json、保存结果
            sa.reslut_saver(data)

        time.sleep(random.randint(23, 31))  # 休眠防止被封

def main(): #调度函数
    postion,city=ask_to_input() #获取查询职位及城市
    bulider = infobulider.InfoBulider(postion=postion,city=city) #初始化构造模块
    url = bulider.urlbulider() #构造url
    headers = bulider.headersbulider() #构造headers
    data = bulider.databulider(1) #构造data

    sp = spider.LagouSpider(url=url, headers=headers) #初始化爬取功能
    job_info = sp.get_json(data=data) #获得第一页的json
    total_pages = sp.get_pagenum(job_info=job_info) #通过第一页json得到总页数

    sa = save.Saver() #初始化save模块
    sa.column_name_saver() #写入csv表头
    page_result= sp.parse_json(job_info=job_info) #解析第一页json取得数据
    sa.reslut_saver(page_reslut=page_result) #保存第一页的结果

    time.sleep(random.randint(23,31)) #休眠防止被封

    for i in range(2,5):
        logging.info('线程{}开始启动'.format(i-1))
        t =Thread(target=crow,args=(bulider,sa,sp,i,total_pages,3),daemon=False)
        t.start()
        logging.info(('线程{}启动完成').format(i-1))
        time.sleep(random.randint(23,31))


if __name__ =='__main__':
    main()






