import urllib.request
import urllib.parse
import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    container = ""
    def handle_data(self, data):
        # print("Data     :", data)
        self.container += data
        return self.container

url = 'http://beijing.cncn.com/jingdian/gugong/profile'

############################################################
#### method1
# values = {'s':'basics','submit':'search'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)

#### method2
resp = urllib.request.urlopen(url)
############################################################
respData = resp.read().decode(resp.headers.get_content_charset())

# print(respData)
comment = re.compile(r'<div class="top">((?:.|\n)*?)<div class="sideR">')
paragraphs = comment.findall(str(respData))
for eachP in paragraphs:
    parser = MyHTMLParser()
    parser.feed(eachP)
    print (parser.container)
    # print(eachP)


