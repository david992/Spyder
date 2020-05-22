import urllib.request
import urllib.parse
import random
import re,csv,requests
  


headers = { 
    "Host": "www.renren.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "anonymid=kagn2bhl-86w2vq; depovince=GW; _r01_=1; JSESSIONID=abcLN7muHCQSw8cZpZ2ix; ick_login=3323ad47-6dca-4d72-92e8-62f131cb70cb; taihe_bi_sdk_uid=bf44a9e6be9e6029e536f8266e690f03; taihe_bi_sdk_session=0f5cfcc260ca972fda22b4f5b8d8bcc9; ick=1d7d3546-ec00-4984-9199-7bd1ce6be885; XNESSESSIONID=fa112af6dfa0; WebOnLineNotice_974479116=1; wp_fold=0; jebecookies=d16428a5-c5dd-4176-9fc5-926ea775104c|||||; _de=CFC1D288C9FD5A1EFCB6A787F424D132; p=5d624a98d8c70db751164171211bf9d56; first_login_flag=1; ln_uact=18971451784; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=330eb851a081a0a7106956f91c6807e56; societyguester=330eb851a081a0a7106956f91c6807e56; id=974479116; xnsid=c9315167; loginfrom=syshome", 
    "Referer": "http://www.renren.com/SysHome.do",
    
    
            }

baseurl = "http://www.renren.com/974479116/profile"

        
    # 页面读取
# req = urllib.request.Request(url,headers=self.headers)
# res = urllib.request.urlopen(req)
res = requests.get(baseurl,headers=headers)
# html = res.read().decode("utf-8")
res.encoding="utf-8"
print(res.text)
# print(html)
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    