import math
import numpy
# import matplotlib.pyplot as plt
import pandas

# shares = 1000
# PRICE = []
# COST = []
# for price in numpy.arange(10, 30, 0.05):
    # fee =  math.floor(price * shares * 0.1425 / 100)
    # if fee < 20:
        # fee = 20
    # tax = math.floor(price * shares * 0.15 / 100)
    # cost = fee * 2 + tax
    # PRICE.append(round(price, 2))
    # COST.append(cost)
    # discount = fee * 2 * 0.4

# plt.plot(PRICE, COST)
# plt.show()


# 在某價位買進 BuyingPrice
# 價格跳動時
# 獲利/虧損的變化以及報酬率

data = dict()
for key in ["BUY", "SELL", "BE", "PBE", "BER", "PBER"]:
    if key not in data:
        data[key] = []

for BuyingPrice in numpy.arange(10, 10.5, 0.05):
    BuyingCost = BuyingPrice * 1000
    BuyingFee = math.floor(BuyingCost * 0.1425 / 100)
    if BuyingFee < 20:
        BuyingFee = 20
    for Spread in numpy.arange(-1, 1, 0.05):
        SellingPrice = BuyingPrice + Spread
        SellingProfit = SellingPrice * 1000
        SellingFee = math.floor(SellingProfit * 0.1425 / 100)
        if SellingFee < 20:
            SellingFee = 20
        SellingTax = math.floor(SellingProfit * 0.15 / 100)
        TotalProfit = SellingProfit - SellingFee - SellingTax
        BreakEven = TotalProfit - BuyingCost - BuyingFee
        BreakEven_Real = BreakEven + math.floor((BuyingFee + SellingFee) * 0.4)
        Per_of_BreakEven = round((BreakEven / BuyingCost * 100), 2)
        Per_of_BreakEven_Real = round((BreakEven_Real / BuyingCost * 100), 2)
        data["BUY"].append(round(BuyingPrice, 2))
        data["SELL"].append(round(SellingPrice, 2))
        data["BE"].append(round(BreakEven))
        data["PBE"].append(Per_of_BreakEven)
        data["BER"].append(round(BreakEven_Real))
        data["PBER"].append(Per_of_BreakEven_Real)


frame = pandas.DataFrame(data)
frame.columns = ["買入價格", "賣出價格", "損益", "報酬率", "實際損益", "實際報酬率"]
print(frame)