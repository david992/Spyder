import urllib.request
import urllib.parse
import random
import re,csv
  

class DoubanSpyder():
    def __init__(self):
        headers_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
        headers = random.choice(headers_list)
        self.headers = headers
        self.offset=0
        baseurl = "https://maoyan.com/board/4"
        self.baseurl = baseurl
        
    # 页面读取
    def loadPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        # print(html)
        self.parsePage(html)
        
    
    # 页面解析
    def parsePage(self,html):
        str ='<dd>.*?title="(.*?)".*?class="star">.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>'
        p = re.compile(str,re.S)
        r_list =p.findall(html)
        self.writePage(r_list)
    
    # 文件写入
    def writePage(self,r_list):
        # print(r_list)
        if self.offset == 0:
            with open ("猫眼.csv","a",newline="") as f:
                w = csv.writer(f)
                w.writerow(["电影名称","主演","上映时间"])
        for i in r_list:
            with open("猫眼.csv","a",newline="") as f:
                writer = csv.writer(f)
                # L = list(i)
                L=[i[0].strip(),i[1].strip(),i[2].strip(),]
                writer.writerow(L)        

    
    # 主函数
    def workOn(self):
        self.loadPage(self.baseurl)
        while True:
            c = input("爬取成功，是否继续（y/n）：")
            if c.strip().lower()=="y":
                self.offset += 10
                url = self.baseurl+"?offset="+str(self.offset)
                self.loadPage(url)
            else:
                print("停止爬取") 
                break
        print("*"*30)            
        

            
if __name__ == "__main__":
    D = DoubanSpyder()
    D.workOn()
   