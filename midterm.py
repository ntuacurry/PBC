num = input().split(",")
for i in range(len(num)):
    num[i] = int(num[i])

rS = input().split(",")
for i in range(num[1] + 1):
    rS[i] = float(rS[i])
    
rL = input().split(",")
for i in range(num[2] + 1):
    rL[i] = float(rL[i])

# 最外圈為時間分配
finalProfit = 0
for i in range(num[0] + 1):
    totalProfit = 0
    rS_num = i * num[3]  # 小炭生產個數
    rL_num = (num[0] - i) * num[4]  # 大炭生產個數
    
    if rS_num > num[1]:  # 決定機率的圈數
        rS_num = num[1]
    if rL_num > num[2]:
        rL_num = num[2]

    profit_S = 0
    for n in range(rS_num + 1):
        profit_S += (n * rS[n]) * num[5]

    profit_L = 0
    for m in range(rL_num + 1):
        profit_L += (m * rL[m]) * num[6]

    totalProfit = profit_S + profit_L

    if finalProfit < totalProfit:
        finalProfit = totalProfit

print(int(finalProfit))