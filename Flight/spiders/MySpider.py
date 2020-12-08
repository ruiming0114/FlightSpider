import scrapy
from Flight.items import FlightItem
from scrapy import FormRequest
import json
import time


class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["hongkongairport.com"]

    # 爬取的url为网站的获取航班信息接口，其中的日期根据爬取时的日期进行拼接
    def start_requests(self):
        return [FormRequest(
            "https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1&date="
            + time.strftime("%Y-%m-%d") +
            "&lang=en&cargo=false&arrival=true",
            callback=self.parse,
            dont_filter=True
        )]

    # 处理爬取的方法，同时负责数据的清洗和封装
    def parse(self, response, **kwargs):
        item = FlightItem()
        # 爬取的json为一个数组列表
        datalist = json.loads(response.text)
        for i in datalist:
            # 遍历列表中的每一个数组
            for j in i['list']:
                # 获取预计到达时间
                expected_time = i['date'] + ' ' + j['time']
                # 获取始发地
                origin = j['origin']
                # 获取停机位
                parking_stand = j['stand']
                # 获取航站楼
                hall = j['hall']
                # 获取行李带
                belt = j['baggage']
                # 获取当前状态
                current_status = j['status']
                # 遍历航班数组的每一个航班元素
                for k in j['flight']:
                    # 获取航班号
                    flight_no = k['no']
                    # 获取航空公司
                    airline = k['airline']
                    # 将每个航班的信息按顺序独立封装为一条记录并返回
                    item['flight_no'] = flight_no
                    item['airline'] = airline
                    item['expected_time'] = expected_time
                    item['current_status'] = current_status
                    item['origin'] = origin
                    item['parking_stand'] = parking_stand
                    item['hall'] = hall
                    item['belt'] = belt
                    yield item
