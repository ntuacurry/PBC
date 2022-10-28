information_string = input()  # [0]為面額種類數，[1]為食材數
coinvalue_string = input()
coinnumber_string = input()
food_string = input()

# 將字串切開成List
information = information_string.split(",")
information[0] = int(information[0])
information[1] = int(information[1])
coinvalue = coinvalue_string.split(",")
coinnumber = coinnumber_string.split(",")
food = food_string.split(",")

totalProfit = 0

# 將List中的資料轉為整數格式
# 同時計算總收益，以及買完食材後剩下的餘額
for i in range(information[0]):
    coinvalue[i] = int(coinvalue[i])
    coinnumber[i] = int(coinnumber[i])
    profit = coinvalue[i] * coinnumber[i]
    totalProfit += profit

for i in range(information[1]):
    food[i] = int(food[i])
    if totalProfit >= food[i]:
        totalProfit -= food[i]

# 輸出結果
print(totalProfit)