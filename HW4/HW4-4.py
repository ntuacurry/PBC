num = input().split(",")
num[0] = int(num[0])
num[1] = int(num[1])

coin = input().split(",")
coinnumber = input().split(",")
food = input().split(",")

# 將coin和coinnumber轉為整數型態，並相乘加總以獲取總收入
totalProfit = 0
for i in range(num[0]):
    coin[i] = int(coin[i])
    coinnumber[i] = int(coinnumber[i])
    totalProfit += coin[i] * coinnumber[i]

# 將食材價格轉為整數型態
for i in range(num[1]):
    food[i] = int(food[i])


# 製作出要買or不買的List
list = []
lst2 = [1] * num[1]
n = 2 ** num[1] - 1
for m in range(n):
    lst = [0] * num[1]
    for i in range(num[1]):
        if m >= 2 ** ((num[1] - 1) - i):
            lst[((num[1] - 1) - i)] = 1
            m -= 2 ** ((num[1] - 1) - i)
    list.append(lst)
list.append(lst2)

# 計算最大化食材總價值
finalcost = 0
for m in range(n + 1):
    totalcost = 0
    for i in range(num[1]):
        cost = food[i] * list[m][i]
        totalcost += cost
    if finalcost < totalcost and totalcost <= totalProfit:
        finalcost = totalcost
finalProfit = totalProfit - finalcost

print(finalProfit)