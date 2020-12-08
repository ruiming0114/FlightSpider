import os
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


# 单次启动爬虫的方法
def doScrapy():
    os.system("scrapy crawl MySpider")


# 调度程序
scheduler = BlockingScheduler()
# 每间隔15分钟调用一次爬虫方法进行数据爬取
scheduler.add_job(doScrapy, 'interval', minutes=15, next_run_time=datetime.datetime.now())
# 调度程序启动
scheduler.start()
