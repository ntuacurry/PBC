import requests
from bs4 import BeautifulSoup

response = requests.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")

list_of_dicts = response.json()

"""
"Code": "string",
"Name": "string",
"TradeVolume": "string",
"TradeValue": "string",
"OpeningPrice": "string",
"HighestPrice": "string",
"LowestPrice": "string",
"ClosingPrice": "string",
"Change": "string",
"Transaction"
"""


for i in list_of_dicts:
    print(i["Code"])

