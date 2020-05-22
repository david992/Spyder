import urllib.request
import urllib.parse
import random
import re,csv,requests

headers_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
headers = random.choice(headers_list)
# baseurl = "http://httpbin.org/get"
baseurl = "https://www.whatismyip.com/"

proxies ={"http":"http://114.105.182.72:42168"} 
# key = input("请输入搜索内容：")
# params = {"wd":key}

res = requests.get(baseurl,headers=headers,proxies=proxies)
res.encoding = "utf-8"
print(res.text)
print(res.status_code)