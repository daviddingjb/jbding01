#encoding=utf-8
import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        resp = urllib.request.urlopen(url)
        if resp.getcode() != 200:
            return None
        return resp.read()
        # return resp.read().decode(resp.headers.get_content_charset())
