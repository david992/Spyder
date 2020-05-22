import pymysql,warnings,re,random,requests
class LianjiaSpyder():
    def __init__(self):
        baseurl = "https://maoyan.com/board/4"
        self.baseurl=baseurl
        # self.proxies = {"":""}
        
        header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                    {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                    {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
        # 随机获取一个user-agent
        headers = random.choice(header_list)
        self.headers = headers
        self.offset=0
        
        # self.proxies ={"https":"https://163.125.132.185:8118"} 
        # 创建数据库连接对象
        self.db = pymysql.connect(host="localhost",port=3306,user="root",password="123456",
                      charset="utf8")
        # 创建游标
        self.cur = self.db.cursor()
        
        
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        print(html)
        print("解析页面ing......")
        self.parsePage(html)

    def parsePage(self,html):
        str ='<dd>.*?title="(.*?)".*?class="star">.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>'
        p = re.compile(str,re.S)
        r_list = p.findall(html)
        print("完成解析，正在存储数据......")
        print(r_list)
        print(111)
        self.writeMysql(r_list)
        
    def writeMysql(self,r_list):
        # 过滤警告
        warnings.filterwarnings("ignore")
        try:
            self.cur.execute("create database if not exists spyder")
            self.cur.execute("use spyder")
            self.cur.execute("create table if not exists movie (id int primary key auto_increment ,name varchar(200),actor varchar(100),time varchar(50))")
        except Warning:
            pass
        ins = "insert into movie (name,actor,time ) values(%s,%s,%s)"
        for r_tuple in r_list:
            self.cur.execute(ins,[r_tuple[0].strip(),r_tuple[1].strip(),r_tuple[2].strip()])
            self.db.commit()
    
        
        
        
    def workOn(self):
        while True:
            c = input("爬取按y/退出按q:")
            if c.strip().lower()=="y":
                url = self.baseurl + "?offset=" + str(self.offset)
                self.getPage(url)
                self.offset += 10
            else:
                print("****结束*****")
                self.cur.close()
                self.db.close()
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

