import twstock
import math
import numpy

def Data(code):
    data = twstock.realtime.get(code)
    price = data["realtime"]["latest_trade_price"]
    return price

# 損益平衡計算
def BreakEven(strategy, price, amount):
    # 股價變動級距
    if price < 50:
        interval = 0.05
    elif price < 100:
        interval = 0.1
    elif price < 500:
        interval = 0.5
    elif price < 1000:
        interval = 1
    else:
        interval = 5
        
    Shares = amount * 1000
    Cost = price * Shares
    BuyingFee = math.floor(Cost * 0.1425 / 100)  # 計算手續費
    if BuyingFee < 20:
        BuyingFee = 20
    
    if strategy == 1:  # 做多
        TotalCost = Cost + BuyingFee
        # 計算損益平衡價
        for Price in numpy.arange(price, price + 50, interval):
            SellingFee = math.floor(Price * Shares * 0.1425 / 100)
            TransferTax = math.floor(Price * Shares * 0.15 / 100)
            if SellingFee < 20:
                SellingFee = 20
            profit = Price * Shares - SellingFee - TransferTax - TotalCost
            if profit >= 0:
                return(round(Price, 2))
                break
    else:
        TransferTax = math.floor(Cost * 0.15 / 100)
        TotalCost = Cost - TransferTax - BuyingFee
        # 計算損益平衡價
        for Price in numpy.arange(price, price - interval * 6, -interval):
            SellingFee = math.floor(Price * Shares * 0.1425 / 100)
            if SellingFee < 20:
                SellingFee = 20
            profit = TotalCost - Price * Shares - SellingFee
            if profit >= 0:
                return(round(Price, 2))
                break

# 計算目前的損益
def BreakEven_Now(strategy, code, price, amount):
    Shares = amount * 1000
    Cost = price * Shares
    BuyingFee = math.floor(Cost * 0.1425 / 100)  # 計算手續費
    if BuyingFee < 20:
        BuyingFee = 20

    # 目前的價格
    Price = float(Data(code))
    if strategy == 1:
        TotalCost = Cost + BuyingFee
        SellingFee = math.floor(Price * Shares * 0.1425 / 100)
        TransferTax = math.floor(Price * Shares * 0.15 / 100)
        if SellingFee < 20:
            SellingFee = 20
        profit = Price * Shares - SellingFee - TransferTax - TotalCost
        return profit
    else:
        TransferTax = math.floor(Cost * 0.15 / 100)
        TotalCost = Cost - TransferTax - BuyingFee
        SellingFee = math.floor(Price * Shares * 0.1425 / 100)
        if SellingFee < 20:
            SellingFee = 20
        profit = TotalCost - Price * Shares - SellingFee
        return profit