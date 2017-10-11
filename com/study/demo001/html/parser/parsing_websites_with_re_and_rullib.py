import urllib.request
import urllib.parse
import re

def tryDecode(s, decoding="utf-8"):
    try:
        print(s.decode(decoding))
    except UnicodeDecodeError as err:
        print(err)

url = 'http://beijing.cncn.com/jingdian/gugong/profile'
values = {'s':'basics','submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
# resp = urllib.request.urlopen(url)

respData = resp.read().decode(resp.headers.get_content_charset())

# print(respData)

paragraphs = re.findall(r'<title>(.*?)</title>',str(respData))
for eachP in paragraphs:
    print(eachP)


