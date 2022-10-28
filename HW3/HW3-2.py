# 輸入含有商品數和成本的字串並切割成List
basic = input()
basicList = basic.split(",")

# 輸入商品價格和對應需求數的字串，並將其切割成List
string_price = input()
string_demand = input()
price = string_price.split(",")
demand = string_demand.split(",")

maxProfit = -2500000  # 為了避免成本大於所有商品價格的情況，設定最大利潤的起始值為(0-500)*5000=-2500000
price_final = 0
amount = 0

# 計算各商品之利潤
for number in range(int(basicList[0])):
    profit = (int(price[number]) - int(basicList[1])) * int(demand[number])

# 比較當前利潤是否大於最大利潤
    if maxProfit < profit:
        maxProfit = profit
        price_final = int(price[number])
        amount = int(demand[number])
    elif maxProfit == profit:
        if amount < int(demand[number]):  # 比較同樣利潤下，該價格對應之需求數
            price_final = int(price[number])
            amount = int(demand[number])

print(price_final, maxProfit, sep=",")