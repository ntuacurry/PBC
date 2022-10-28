import requests
from bs4 import BeautifulSoup

r = requests.get("https://dasc.cyc.org.tw/api") #將此頁面的HTML GET下來
print(r.text)
print(r.text[9])
input("Press the <Enter> key on the keyboard to exit.")
