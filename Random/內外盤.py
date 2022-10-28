import twstock

code = input()
data = twstock.realtime.get(code)
realtime = data["realtime"]
best_bid_price = realtime["best_bid_price"]  # 委買價
best_bid_volume = realtime["best_bid_volume"]  #委買量
best_ask_price = realtime["best_ask_price"]  # 委賣價
best_ask_volume = realtime["best_ask_volume"]  # 委賣量
# 將價格轉為適當格式
for i in range(5):
    best_bid_price[i] = float(best_bid_price[i])
    best_ask_price[i] = float(best_ask_price[i])
    if best_bid_price[i] < 50:
        best_bid_price[i] = round(best_bid_price[i], 2)
    elif best_bid_price[i] < 500:
        best_bid_price[i] = round(best_bid_price[i], 1)
    else:
        best_bid_price[i] = round(best_bid_price[i])

    if best_ask_price[i] < 50:
        best_ask_price[i] = round(best_ask_price[i], 2)
    elif best_ask_price[i] < 500:
        best_ask_price[i] = round(best_ask_price[i], 1)
    else:
        best_ask_price[i] = round(best_ask_price[i])
# 在當下價格不為空時，將價格轉為適當格式
if realtime["latest_trade_price"] != None:
    latest_trade_price = float(realtime["latest_trade_price"])
    if latest_trade_price < 50:
        latest_trade_price = round(latest_trade_price, 2)
    elif latest_trade_price < 500:
        latest_trade_price = round(latest_trade_price, 1)
    else:
        latest_trade_price = round(latest_trade_price)
# 判斷目前的成交發生在內盤或外盤
if latest_trade_price < best_ask_price[0]:
    print("成交在內盤")
else:
    print("成交在外盤")
print(best_bid_price)
print(best_ask_price)


# print(best_bid_volume)
# print(best_bid_price)
# print(best_ask_price)
# print(best_ask_volume)