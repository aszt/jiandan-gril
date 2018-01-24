# python-煎蛋妹子图

> 准备工作
- Python3.5
- requests
- BeautifulSoup
- selenium

> selenium作用

煎蛋做了反爬虫的机制，图片的URL做了加密处理，F12能看到，但是beautifulsoup解析不出来。
本来是想找解密的方法，无意中搜到selemium这个神器。
selenium 是一个web的自动化测试工具，可以模拟用户操作浏览器。这样就可以直接获取图片URL了

> 下载路径

内网：https://npm.taobao.org/mirrors/chromedriver/

外网：https://sites.google.com/a/chromium.org/chromedriver/downloads

注：源码中存放了最新版，支持Chrome v62-64

PS：爬煎蛋不要太过分，对煎蛋服务器压力很大，练手后去爬其他大站吧。
