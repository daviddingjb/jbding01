#encoding=utf-8
from com.study.demo001.html.baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        #初始化
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownloader() #下载器
        self.parser = html_parser.HtmlParser() # 解析器
        self.outputer = html_outputer.HtmlOutputer() # 输出器

    def craw(self, root_url):
        # 爬虫的调度程序
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d：%s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 5:
                    break
                count = count + 1
            except:
                print("craw failed!")
        self.outputer.output_html()
if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
