import requests
from bs4 import BeautifulSoup

headers = {"USer-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"}
response = requests.get("https://goodinfo.tw/tw/StockList.asp?RPT_TIME=&MARKET_CAT=熱門排行&INDUSTRY_CAT=成交張數+%28高→低%29%40%40成交張數%40%40由高→低", headers = headers)
response.encoding = "UTF-8"
soup = BeautifulSoup(response.text, "html.parser")

ATB_results = soup.find_all(["a", "br"], class_="link_black", style="cursor:pointer;")

ATB = []  # 屬性：attribute
for result in ATB_results:
    if result.text not in ATB:
        ATB.append(result.text)
"""
代號, 名稱, 市場, 股價日期, 成交,
漲跌價, 漲跌幅, 成交張數, 成交額(百萬),
昨收, 開盤, 最高, 最低, 振幅(%),
PER, PBR
"""

DT_results = soup.find_all("tr", bgcolor=["#ffffff", "#f0f0f0"])

DT = []
count = 0
for result in DT_results:
    subDT = []
    for data in result:
        subDT.append(data.text)
    del subDT[17:22]
    del subDT[5]
    del subDT[0]
    DT.append(subDT)
    count += 1
    if count == 300:
        break

for i in range(300):
    DT[i][4] = float(DT[i][4])
    DT[i][13] = float(DT[i][13])
    DT[i][7] = float(DT[i][7].replace(",", ""))

FINAL = []
for i in range(300):
    if len(DT[i][0]) <= 4 and DT[i][2] == "市":
        if DT[i][13] >= 5.00 and DT[i][4] >= 10.00 and DT[i][4] <= 30:
            FINAL.append(DT[i])
            
FINAL.sort(key = lambda x: x[4])  # 按照價格由小到大排序

print(ATB[0].ljust(8), ATB[1].ljust(8), ATB[4].ljust(6), ATB[13].ljust(6), ATB[6].ljust(6), ATB[7])
for i in range(len(FINAL)):
    for j in range(10 - 2 * len(FINAL[i][1])):
        FINAL[i][1] += " "
    print(FINAL[i][0].ljust(10), FINAL[i][1], str(FINAL[i][4]).ljust(8), str(FINAL[i][13]).ljust(8), str(FINAL[i][6]).ljust(9), int(FINAL[i][7]))

# 開高走高
# 開低走高
# 開高走低
# 開低走低