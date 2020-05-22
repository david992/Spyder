import urllib.request
import urllib.parse 



#     baseurl = "http://www.baidu.com/s?"


baseurl = "http://www.baidu.com/s?wd="
key = input("搜索的内容：")
# urlencode(字典)
# wd = {"wd":key}
# key = urllib.parse.urlencode(wd)

#     quote(字符串)
key = urllib.parse.quote(key)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
url = baseurl+key

# 创建User-Agent
req = urllib.request.Request(url,headers=headers)
# 获取响应对象
res = urllib.request.urlopen(req)


html = res.read().decode("utf-8")
print(html)

with open("搜索2.html","w",encoding="utf-8") as f:
    f.write(html)
