import pymysql,warnings,re,random,requests
import pymongo
class LianjiaSpyder():
    def __init__(self):
        baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.baseurl=baseurl
        
        # header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
        #            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
        #            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
        # # 随机获取一个user-agent
        # headers = random.choice(header_list)
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.page = 1
        
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Lianjia
        self.myset = self.db.housePrice
        
        
    def getPage(self,url):
        print("****start*****")
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        print(html)
        print("解析页面ing......")
        self.parsePage(html)
        
        
        
    def parsePage(self,html):
        str = '<div class="title".*?class="positionInfo".*?data-el="region">(.*?)</a>.*?target="_blank">(.*?)</a>.*?<div class="totalPrice"><span>(.*?)</span>"(.*?)"</div>'
        p = re.compile(str,re.S)
        r_list = p.findall(html)
        print("完成解析，正在存储数据......")
        self.writeTomongo(r_list)
        
    def writeTomongo(self,r_list):
   
        for r_tuple in r_list:
            D = {"houseadd":r_tuple[0].strip(),
                "price":float(r_tuple[1].strip())*10000}
            self.myset.insert(D)
    
        
        
        
    def workOn(self):

        while True:
            c = input("爬取按y/退出按q:")
            if c.strip().lower()=="y":
                url = self.baseurl+str(self.page)+"/"
                self.getPage(url)
                self.page += 1

            else:
                print("****结束*****")
                break
    
if __name__ == "__main__":
    L=LianjiaSpyder()
    L.workOn()
    
    





# # 游标执行方法
# # 提交
# db.commit()

# # 关闭
# cur.close()
# db.close()

