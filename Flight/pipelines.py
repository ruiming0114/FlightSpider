import json
import os


class FlightPipeline(object):

    # 起始打开一个临时文件作为写入
    def __init__(self):
        self.file = open('temp.json', 'w+', encoding='utf-8')

    # 对每个item向文件写入一条json记录
    def process_item(self, item, spider):
        line = ",\n" + json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item

    def open_spider(self, spider):
        pass

    # 爬取结束后将temp文件中的记录封装为一个数组，包含完整的json格式返回新的json文件
    def close_spider(self, spider):
        self.file.seek(0)
        self.file.readline()
        jsonFile = open('data.json', 'w', encoding='utf-8')
        # 添加数组头部和尾部的中括号
        jsonFile.write('[\n')
        jsonFile.write(self.file.read())
        jsonFile.write('\n]')
        self.file.close()
        jsonFile.close()
        # 删除临时文件temp
        os.remove('temp.json')
