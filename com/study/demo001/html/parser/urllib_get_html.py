from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法:')
resp1 = request.urlopen(url)
print(resp1.getcode())
print(resp1.read)
# print(len(resp1.read().decode('utf-8')))

print('第二种方法')
req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
resp2 = request.urlopen(req)
print(resp2.getcode())
print(resp2.read)
# print(len(resp2.read().decode('utf-8')))

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
resp3 = request.urlopen(url)
print(resp3.getcode())
print(cj)
print(resp3.read)
# print(resp3.read().decode('utf-8'))
