#encoding=utf-8
from com.jbding.common.util import url_manager, html_downloader
from com.jbding.tr.trip.xialv.spider1 import html_parser, html_outputer
import re

class SpiderMain(object):
    def __init__(self):
        #初始化
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownloader() #下载器
        self.parser = html_parser.HtmlParser() # 解析器
        self.outputer = html_outputer.HtmlOutputer() # 输出器
        self.root_url = 'http://www.xialv.com'

    def craw(self, url):
        # 爬虫的调度程序
        html_cont = self.downloader.download(url)
        pagset = regx.findall(str(html_cont))
        if not pagset:
            pagset = ['0']

        for i in range(int(pagset[0])):
            new_url = url + "?&page=" + str(i+1)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(self.root_url, html_cont)

        #     self.urls.add_new_urls(new_urls)
        #     self.outputer.collect_data(new_data)
        #
        #     while self.urls.has_new_url():
        #         try:
        #             new_url = self.urls.get_new_url()
        #             html_cont = self.downloader.download(new_url)
        #             new_urls, new_data = self.parser.parse(new_url, html_cont)
        #
        #             self.urls.add_new_urls(new_urls)
        #             self.outputer.collect_data(new_data)
        #         except:
        #             print("craw failed!")
        # self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://www.xialv.com/beijing/zhoubianyou"
    regx = re.compile(r'下一页</a><a href=\'/beijing/zhoubianyou\?&page=(.*?)\'  rel=\'nofollow\' >末页')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
