
import re
# a="123456abc789"
#result = re.findall("(([0-9]*)([a-z]*))([0-9]*)",a)
#print(result)         #[('123456abc', '123456', 'abc', '789'), ('', '', '', '')]
# a="123456abc789123456abc789123456abc789"
# result = re.findall("(([0-9]*)([a-z]*))([0-9]*)",a)
# #这个是怎么得到的

# print(result)  #[('123456abc', '123456', 'abc', '789123456'), ('abc', '', 'abc', '789123456'), ('abc', '', 'abc', '789'), ('', '', '', '')]
 
# print("----------------------------------------------------")
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group())    #123456abc789             123456abc789123456
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group(0))  #123456abc789              123456abc789123456
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group(1))  #123456abc                 123456abc
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group(2))  #123456                    123456
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group(3))  #abc                       abc
# print(re.search("(([0-9]*)([a-z]*))([0-9]*)",a).group(4))  #789    
# print("----------------------------------------------------")

# s = """<div class="animal">
# <p class="name">
#     <a title="Tiger"></a>
# </p>
# <p class="contents">
#     two tigers two tigers run fast
# </p>
# </div>

# <div class="animal">
# <p class="name">
#     <a title="Rabbit"></a>
# </p>
# <p class="contents">
#     Small white rabbit white and white
# </p>
# </div>"""

# p = re.compile('<div class="animal".*?title="(.*?)">.*?contents">(.*?)</p>',re.S)
# r = p.findall(s)
# print(r)

import urllib.request
import urllib.parse
import random

class NeihanSpyder():    
    def __init__(self):      
        header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
        # 随机获取一个user-agent
        headers = random.choice(header_list)
        self.headers = headers
        self.page = 1
        baseurl ="https://www.neihanba.com/dz/"  
        self.baseurl =baseurl 
        
    # 页面读取
    def loadPage(self,url): 
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("gbk")
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html): 
        p = re.compile('<li class="piclist[0-9]".*?<h4>.*?<b>(.*?)</b>.*?<div class="f18 mb20">(.*?)</div>',re.S)
        r_list = p.findall(html)
        for content in r_list:
            for i in content:
            #将每个段子挨个处理
                i = i.replace("hellip;","").replace("&ldquo;","").replace("&rdquo;","").replace("&amp;","")
            #处理完后调用write_page()函数将每个段子写入文件内
                self.writePage(i)

    
    # 文件写入
    def writePage(self,r_list):
        with open ("段子.txt","a",encoding="utf-8") as f :       
            f.write(r_list.strip()+"\n")
            
            
    def work(self):         
        self.loadPage(self.baseurl)
        while True:
            c = input("爬取成功，是否继续（y/n）：")
            if c.strip().lower()=="y":
                self.page += 1
                url = self.baseurl+"list_"+str(self.page)+".html"
                self.loadPage(url)
            else:
                print("停止爬取") 
                break
        print("*"*30)            





if __name__ == "__main__":
    N = NeihanSpyder()
    N.work()




















