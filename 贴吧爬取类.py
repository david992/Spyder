import urllib.parse
import urllib.request
import random,time

class TiebaSpyder():
    
    def __init__(self):      
        header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}]
        # 随机获取一个user-agent
        headers = random.choice(header_list)
        self.headers = headers
        baseurl ="https://tieba.baidu.com/f?"  
        self.baseurl =baseurl 
        
    # 页面读取
    def readPage(self,url):
        
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
    
    # 文件写入
    def writePage(self,filename,html):
        with open (filename,"w",encoding="utf-8") as f :       
            f.write(html)
    # 主函数
    def work(self):         
        name  = input("请输入贴吧名：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入结束页："))
        # 对贴吧名进行编码
        kw = {"kw":name}
        kw = urllib.parse.urlencode(kw)
   
        # 拼接url 发请求  获取响应
        for i in range(begin,end+1):
            # 拼接url
            pn = (i-1) * 50
            url = self.baseurl+kw +"&pn=" + str(pn)
            time.sleep(2)
            # 发起请求
            html = self.readPage(url) 
            filename = name+"吧第"+str(i)+"页.html"
            print("正在获取第"+str(i)+"页")
            self.writePage(filename, html)  
            print("第"+str(i)+"页获取成功")
            print("*"*30)
    



if __name__ == "__main__":
    T = TiebaSpyder()
    T.work()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


