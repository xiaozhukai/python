# coding:utf8

from baike import url_manager
from baike import html_downloader
from baike import html_outputer
from baike import html_parser


class SpiderMain(object):
    # 构造函数初始化对象
    def __init__(self):
        # url的管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.htmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出信息
        self.outputer = html_outputer.htmlOutputer()

    # 爬虫中调度程序
    def craw(self, root_url):
        count = 1
        # 入口url添加到url管理器中
        self.urls.add_new_urls(root_url)
        # 判断管理器中是否有新的待爬取的url
        while self.urls.has_new_url():
            try:
                # 待爬取的url
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                # 使用下载器来下载这个页面
                html_cont = self.downloader.download(new_url)
                # 解析器解析新的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 进行数据的处理，讲解析的url添加到url管理器中
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                #判断爬取数量,数量到达1000就这接break
                if count == 1000:
                    break

                count = count+1
            except:
                #打印爬取失败信息
                print 'craw failed'
        #输入到文件中
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    # 启动这个函数方法
    obj_spider.craw(root_url)
