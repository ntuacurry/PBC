'''
Name	Description
tlong	epoch毫秒數
f	揭示賣量(配合「a」，以_分隔資料)
ex	上市別(上市:tse，上櫃:otc，空白:已下市或下櫃)
g	揭示買量(配合「b」，以_分隔資料)
d	最近交易日期(YYYYMMDD)
b	揭示買價(從高到低，以_分隔資料)
c	股票代號
a	揭示賣價(從低到高，以_分隔資料)
n	公司簡稱
o	開盤
l	最低
h	最高
w	跌停價
v	累積成交量
u	漲停價
t	最近成交時刻(HH:MM:SS)
tv	當盤成交量
nf	公司全名
z	當盤成交價
y	昨收
'''
# 更新頻率5秒內不能超過3次

import requests

TWII = requests.get("https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_t00.tw&json=1&delay=0")
TWII_lst_dict = TWII.json()
TWII_data = TWII_lst_dict["msgArray"][0]

TWOI = requests.get("https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=otc_o00.tw&json=1&delay=0")
TWOI_lst_dict = TWOI.json()
TWOI_data = TWOI_lst_dict["msgArray"][0]

# 加權指數
TWII_PRICE_min = TWII_data["l"]  # 最低價
TWII_PRICE_max = TWII_data["h"]  # 最高價
TWII_Limit_down = TWII_data["w"]  # 跌停價
TWII_Limit_up = TWII_data["u"]  # 漲停價
TWII_yesterday = TWII_data["y"]  # 昨收
TWII_opening = TWII_data["o"]  # 開盤價

# 櫃買指數
TWOI_PRICE_min = TWOI_data["l"]  # 最低價
TWOI_PRICE_max = TWOI_data["h"]  # 最高價
TWOI_Limit_down = TWOI_data["w"]  # 跌停價
TWOI_Limit_up = TWOI_data["u"]  # 漲停價
TWOI_yesterday = TWOI_data["y"]  # 昨收
TWOI_opening = TWOI_data["o"]  # 開盤價

