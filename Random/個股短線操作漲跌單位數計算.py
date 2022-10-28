import math
import numpy
import matplotlib.pyplot as plt

# Shares = int(input("買入股數："))
# Money = int(input("輸入投入總資金："))

PRICE = []
UNIT = []
BuyingPrice = 9
while BuyingPrice <= 3000:

    # Shares = Money // BuyingPrice
    Shares = 1000

    BuyingFee = math.floor(BuyingPrice * Shares * 0.1425 / 100)  # 計算手續費

    # 零股手續費最低為1元
    if BuyingFee == 0:
        BuyingFee = 1

    BuyingCost = int(math.floor(BuyingPrice * Shares + BuyingFee))  # 計算買入成本

    # 股價變動級距
    if BuyingPrice < 10:
        interval = 0.01
    elif BuyingPrice < 50:
        interval = 0.05
    elif BuyingPrice < 100:
        interval = 0.1
    elif BuyingPrice < 500:
        interval = 0.5
    elif BuyingPrice < 1000:
        interval = 1
    else:
        interval = 5

    for price in numpy.arange(BuyingPrice, BuyingPrice + 500, interval):
        SellingFee = math.floor(price * Shares * 0.1425 / 100)
        TransferTax = math.floor(price * Shares * 0.15 / 100)
        if SellingFee == 0:
            SellingFee = 1
        if TransferTax == 0:
            TransferTax = 1
        profit = price * Shares - SellingFee - TransferTax - BuyingCost
        if profit >= 0:
            PRICE.append(round(BuyingPrice, 2))
            UNIT.append(round((price-BuyingPrice)/interval))
            if round((price-BuyingPrice)/interval) == 1:
                print(round(BuyingPrice, 2), round(price, 2), 1)
            elif round((price-BuyingPrice)/interval) == 2:
                print(round(BuyingPrice, 2), round(price, 2), 2)
            break

    if BuyingPrice < 3000:
        if round(BuyingPrice, 2) == 10.00:
            BuyingPrice += 0.05
        elif round(BuyingPrice, 2) == 50.00:
            BuyingPrice += 0.1
        elif round(BuyingPrice, 2) == 100.00:
            BuyingPrice += 0.5
        elif round(BuyingPrice, 2) == 500.00:
            BuyingPrice += 1
        elif round(BuyingPrice, 2) == 1000.00:
            BuyingPrice += 5
        else:
            BuyingPrice += interval
    else:
        break

# plt.plot(PRICE, UNIT)
# plt.show()
# f06641022