import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import lxml

Directory = 'ooxx/'
base_url = "http://jandan.net/ooxx/page-"
path = "D:\chrome\chromedriver.exe"
#driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome(executable_path=path)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
img_url = []
urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(200, 201)]

def getImg():
    n = 1
    for url in img_url:
        print('第' + str(n) + ' 张', end='')
        with open(Directory + url[-15:], 'wb') as f:
            f.write(requests.get(url).content)
        print('...OK!')
        n = n+1

def getImgUrl(url):
    driver.get(url)
    data = driver.page_source
    soup = BeautifulSoup(data, "html.parser")  # 解析网页
    images = soup.select("a.view_img_link")  # 定位元素
    for i in images:
        z = i.get('href')
        if str('gif') in str(z):
            pass
        else:
            http_url = "http:" + z
            img_url.append(http_url)
            print(http_url)


if __name__ == "__main__":
    for url in urls:
        getImgUrl(url)
    getImg()
    print("")