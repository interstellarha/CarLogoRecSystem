#-*- coding = utf-8 -*-
#@Time : 2021年5月5日
#@Author : 苏婉芳
#@File : car_spider.py
#@Software: vscode

from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error,urllib.parse      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作
import string
from w3lib import html as HTML #去除标签


def main():
    #基本url，后+
    baseurl = "https://baike.baidu.com/item/"

    #爬取数据
    datalist = getData(baseurl) #每项是一个品牌
    
    #保存到数据库
    dbpath = "database.db"
    saveData2DB(datalist,dbpath)



#规则

#车名
#find_title = re.compile(r'<dd class="lemmaWgt-lemmaTitle-title">\n<h1>(.*?)</h1>')
find_title = re.compile(r'<dd class="lemmaWgt-lemmaTitle-title">[\w\W]*?<h1>(.*?)</h1>')
#车图片链接
find_img = re.compile(r'<img src="(.*?)"[/]*>')
#品牌简介
find_intro = re.compile(r'<span class="score-number">(.*?)</span>')



#爬取数据
def getData(baseurl):
    #40个品牌
    brand_list = ['Alfa Romeo','Audi','BMW','Chevrolet','Citroen','Dacia','Daewoo','Dodge','Ferrari','Fiat','Ford','Honda','Hyundai','Jaguar','Jeep','Kia','Lada','Lancia','Land Rover','Lexus','Maserati','Mazda','Mercedes','Mitsubishi','Nissan','Opel','Peugeot','Porsche','Renault','Rover','Saab','Seat','Skoda','Subaru','Suzuki','Tata','Tesla','Toyota','Volkswagen','Volvo']
    #print(len(brand_list))
    
    datalist = [] #存40项，每项是1个list：[品牌中文名，品牌英文名，简介，百度百科链接]

    #1次循环处理1个页面（1个品牌）
    #for i in range(0,2): #test
    for i in range(0,40): #all
        if(brand_list[i]=="Hyundai"):
            brand = "现代"
            # url = "https://baike.baidu.com/item/%E7%8E%B0%E4%BB%A3"
        elif(brand_list[i]=="Land Rover"):
            brand = "路虎/916396"
            #url = "https://baike.baidu.com/item/%E8%B7%AF%E8%99%8E"
        elif(brand_list[i]=="Jaguar"):
            brand = "捷豹"
        elif(brand_list[i]=="Daewoo"):
            brand = "大宇" 
        elif(brand_list[i]=="Lada"):
            brand = "拉达"
        elif(brand_list[i]=="Rover"):
            brand = "罗孚汽车"
        elif(brand_list[i]=="Seat"):
            brand = "西雅特"
        elif(brand_list[i]=="Mazda"):
            brand = "马自达"
        else:
            brand = brand_list[i]
        url = baseurl + brand
        url = urllib.parse.quote(url,safe=string.printable)

        #获取网页源码
        html = askURL(url)
        html_file = open("html.html",'w',encoding='utf-8') #存储原始完整html
        html_file.write(html)

        #解析html源码 转成树形结构
        soup = BeautifulSoup(html,"html.parser")
        #print(soup)

        #爬取数据
        for item in soup.find_all('div',class_="main-content"): #只有1标签（百度百科头部）
            brand_data=[] #1个品牌的信息，[品牌中文名，品牌英文名，车标图片链接，简介，百度百科链接]
            
            item = str(item)

            brand_data.append(brand_list[i]) #品牌英文名
            #print(brand_list[i])

            title = re.findall(find_title,item) #品牌中文名
            if(len(title)):
                brand_data.append(title[0])
            else:
                brand_data.append("")
            #print(title)
            
            #车标
            for item in soup.find_all('div',class_="side-content"):
                item = str(item)
                #print(item)
                img = re.findall(find_img,item)
                if(len(img)): 
                    brand_data.append(img[0])
                else: 
                    brand_data.append("")
                print(brand,":",img)
            
            #简介
            for item in soup.find_all('div',class_="lemma-summary"):
                #print(type(item))
                intro = ""
                for para in item.find_all('div',class_ = "para"):
                    para = str(para)
                    para_text = HTML.remove_tags(para) #去除html标签
                    para_text = re.sub('\[\d\]', "", para_text)
                    para_text = re.sub('\n', "", para_text)

                    intro = intro + para_text + "\n\n"
                    
                #print(intro)
                if(len(intro)):
                    brand_data.append(intro)
                else:
                    brand_data.append("")

            brand_data.append(url) #百度百科链接
            #print(url)

            datalist.append(brand_data) #一种品牌
            #print(brand_data)

    #print(len(datalist))
    return datalist


#获取页面
def askURL(url):
    #模拟浏览器头部信息
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    

    #封装请求
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#保存到数据库
def saveData2DB(datalist,dbpath):
    #创建数据表

    #[品牌中文名，品牌英文名，车标图片链接，简介，百度百科链接]
    sql = '''
        CREATE TABLE IF NOT EXISTS CAR_BRAND
        (
            cname varchar,
            ename varchar,
            pic_link varchar,
            introduction varchar,
            baidu_link varchar,
            link int
        )
    '''
    print("打开数据库...")
    conn = sqlite3.connect(dbpath) #数据库：dbpath
    cursor = conn.cursor()
    cursor.execute(sql) #数据表：CAR_BRAND
    conn.commit()
    
    for data in datalist:
        if(len(data)!=5): 
            print(data)
        sql = '''
            insert into CAR_BRAND 
            (cname,ename,pic_link,introduction,baidu_link)
            values(\"{cname}\", \"{ename}\",\"{pic_link}\", \"{introduction}\",\"{baidu_link}\")
        '''.format(cname = data[0], ename = data[1],pic_link = data[2],introduction = data[3],baidu_link = data[4])

        cursor.execute(sql)
        conn.commit()

    cursor.close()
    conn.close()
    print("关闭数据库...")

    # print("save....")
    # book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    # sheet = book.add_sheet('汽车品牌信息.csv',cell_overwrite_ok=True)    #创建工作表
    # col = ("品牌中文名","品牌英文名","车标","品牌简介","百度百科链接")
    # for i in range(0,5):
    #     sheet.write(0,i,col[i]) #列名
    # for i in range(0,40):
    #     data = datalist[i]
    #     for j in range(0,5):
    #         sheet.write(i+1,j,data[j])      #数据

    # book.save("汽车品牌信息.csv")       #保存
    

if __name__ == "__main__":       
    main()
    #init_db("movietest.db")
    print("爬取完毕！")