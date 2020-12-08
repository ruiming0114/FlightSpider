import scrapy


class FlightItem(scrapy.Item):

    # 航班号
    flight_no = scrapy.Field()

    # 航空公司
    airline = scrapy.Field()

    # 计划到达时间
    expected_time = scrapy.Field()

    # 目前状态
    current_status = scrapy.Field()

    # 始发地和经停地
    origin = scrapy.Field()

    # 停机位
    parking_stand = scrapy.Field()

    # 航站楼
    hall = scrapy.Field()

    # 行李带
    belt = scrapy.Field()

