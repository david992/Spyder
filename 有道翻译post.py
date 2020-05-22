
import random
import json,requests

key = input("请输入要翻译的内容：")

data = {"i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15894632831176",
        "sign": "d5adccfcec1136e1814437568424d9e0",
        "ts": "1589463283117",
        "bv": "70244e0061db49a9ee62d341c5fed82a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
}


# /有道翻译  去掉translate_o?  中的_o
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
# 随机获取一个user-agent
headers = random.choice(header_list)

# data为form表单中数据
res = requests.post(url,data=data,headers=headers)


res.enconding="utf-8"
html = res.text


# json格式字符串转换为python中字典
r_dict = json.loads(html)
print("翻译结果：",r_dict['translateResult'][0][0]['tgt'])

  















