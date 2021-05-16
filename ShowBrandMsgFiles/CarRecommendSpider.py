# -*- coding = utf-8 -*-

import sys
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


def askURL(url):
    head = {  # 模拟头部信息向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
    }  # 用户代理：表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
    request = urllib.request.Request(url, headers=head)  # 默认是get?
    html = " "
    findImgSrc = re.compile(r'<img src="(.*?)"/>', re.S)  # 匹配图片
    findName = re.compile(r'target="_blank">(.*?)</a>', re.S)
    findScore = re.compile(r'<span class="score-number">(.*?)</span>', re.S)
    findType = re.compile(r'<span class="info-gray">(.*?)</span>', re.S)
    findEngine = re.compile(r'<span title=""><a href="(.*?)">(.*?)</a>', re.S)

    list = [[], [], [], [], [], [], [], [], [], [], [], []]  # 存储品牌车辆全部信息
    data_ImgSrc = []
    data_Name = []
    data_Score = []
    data_Type = []
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("GB2312", "ignore")
        bs = BeautifulSoup(html, "html.parser")
        number = 0
        for item in bs.find_all('div', class_="list-cont"):
            if number >= 12:
                break
            item = str(item)
            ImgSrc0 = re.findall(findImgSrc, item)[0]
            ImgSrc = 'http:' + str(ImgSrc0)
            Name = re.findall(findName, item)[0]
            if (re.findall(findScore, item)):
                Score0 = re.findall(findScore, item)[0]
            else:
                Score0 = ' '
            Score = "用户评分：" + Score0

            Type0 = re.findall(findType, item)[0]
            Type = "级别：" + Type0
            if (re.findall(findEngine, item)):
                Engine = re.findall(findEngine, item)[0][1]
            else:
                Engine = ' '
            # Title = re.findall(findTitle, item)[0]
            # Rating = re.findall(findRating, item)[0]
            # People = re.findall(findPeople, item)[0]

            # 将页面每辆车的信息加入总列表中，一共12项
            list[number].append(Name)
            list[number].append(ImgSrc)
            list[number].append(Score)
            list[number].append(Type)
            list[number].append(Engine)

            data_ImgSrc.append(ImgSrc)
            data_Name.append(Name)
            data_Score.append(Score)
            data_Type.append(Type)
            number = number + 1
        # pic_info = bs.find_all('img')
        #
        # #file = open('info.csv', 'w')
        # # for i in pic_info:
        # #     file.write(str(i)+'\n')
        # for i in range(2, len(pic_info)-1):
        #     link0 = pic_info[i].get('src')
        #     link = 'http:'+ str(link0)
        #     picture.append(link)
        #     #file.write('http:'+ str(link) + '\n')

        # with open('info.csv', 'w') as f:
        #     for i in pic_info:
        #         f.write(str(i)+'\n')

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")
        if hasattr(e, "reason"):
            print(e.reason)
    return list


def main(carEname):
    # 将所有信息保存到字典dict中，品牌名：品牌信息
    baseurl = "https://car.autohome.com.cn/price/brand-"
    brand_dic = {34: 'Alfa Romeo', 33: 'Audi', 15: 'BMW', 71: 'Chevrolet', 72: 'Citroen',  42: 'Ferrari', 8: 'Ford',
                 14: 'Honda', 12: 'Hyundai', 44: 'Jaguar', 46: 'Jeep', 62: 'Kia', 49: 'Land Rover', 52: 'Lexus',
                 57: 'Maserati',
                 58: 'Mazda', 36: 'Mercedes', 68: 'Mitsubishi', 63: 'Nissan', 13: 'Peugeot', 40: 'Porsche',
                 10: 'Renault', 49: 'Rover', 67: 'Skoda',
                 65: 'Subaru', 3: 'Toyota', 70: 'Volvo'
                 }
    #共27个品牌
    list = [34, 33, 15, 71, 72, 42, 8, 14, 12, 44, 46, 62, 49, 52, 57, 58, 36, 68, 63, 13, 40, 10, 49, 67, 65, 3, 70]


    #dict = {}
    for i in (list):
        if brand_dic[i] == carEname:
            url = baseurl + str(i) + '.html'
            listtest = askURL(url)
            print(listtest)
        # dict.update({brand_dic[i]: listtest})
        # #测试
        # print(brand_dic[i]+':'+str(listtest))


if __name__ == '__main__':
    main("Audi")
