cost = int(input())
price = int(input())
demand_possible = int(input())
recycle = int(input())

rateList = []

for demand in range(demand_possible + 1):
    rate = float(input())
    rateList.append(rate)

maxProfit = 0
demand_final = 0

for demand in range(demand_possible + 1):
    totalrate = 0
    profit_total = 0

    for require in range(demand + 1):
        profit = require * price - demand * cost + (demand - require) * recycle  # 成本不用乘上機率
        profit_total += profit * rateList[require]
        if require == demand:
            profit_total_final = int(profit_total - profit * rateList[require] + profit * (1 - totalrate))
            break
        totalrate += rateList[require]
    
    if maxProfit < profit_total_final:
        maxProfit = profit_total_final
        demand_final = demand

print(demand_final, maxProfit)