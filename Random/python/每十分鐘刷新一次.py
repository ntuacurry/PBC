import requests
import time
from bs4 import BeautifulSoup

r = requests.get("https://dasc.cyc.org.tw/api") #將此頁面的HTML GET下來
print(time.strftime('%m-%d %H:%M', time.localtime()), r.text)



tenminutes = 600

while True: 
 time.sleep(tenminutes) 
 import requests
 from bs4 import BeautifulSoup

 r = requests.get("https://dasc.cyc.org.tw/api") #將此頁面的HTML GET下來
 print(time.strftime('%m-%d %H:%M', time.localtime()), r.text)