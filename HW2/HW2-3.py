method_id = int(input())  # 輸入方法數

final_profit = 0  # 最終輸出的利潤，起始值設為0
final_method = 0  # 最終輸出的方法編號，起始值設為0
final_price = 0  # 最終輸出的價格，起始值設為0

for method in range(1, method_id + 1):  # 一組一組的輸入測資並執行計算，method用來代表目前是第幾個方法
    demand = int(input())  # 輸入基本需求量
    price_sensitivity = int(input())  # 輸入價格敏感度
    cost = int(input())  # 輸入成本

    maxProfit = 0  # 每組測資的最大利潤，起始值設為0
    maxPrice = 0  # 每組測資的最佳價格，起始值設為0

    for price in range(cost + 1, demand // price_sensitivity):  # 計算最佳價格和最大利潤
        profit = (demand - price_sensitivity * price) * (price - cost)

        if maxProfit < profit:
            maxProfit = profit
            maxPrice = price
        elif maxProfit == profit:  # 當同一組測資中最大利潤有兩種最佳價格時，選擇輸出較高之最佳價格
            maxProfit = profit
            if maxPrice < price:
                maxPrice = price

    if maxPrice <= cost:  # 如果最佳價格小於成本，將最佳價格指定為1000，最大利潤指定為0
        maxPrice = 1000
        maxProfit = 0
    else:
        maxProfit = maxProfit

    if final_profit < maxProfit:
        final_profit = maxProfit
        final_method = method
        final_price = maxPrice
    elif final_profit == maxProfit:  # 當不同組測資之間有相同的最大利潤，選擇輸出編號較小的方法
        if final_price < maxPrice:
            final_price = final_price

if final_profit == 0:
    print(1, 1000, 0, sep=",")  # 輸出無法獲利之情形
else:
    print(final_method, final_price, final_profit, sep=",")  # 輸出最佳方法、最佳價格和最大利潤