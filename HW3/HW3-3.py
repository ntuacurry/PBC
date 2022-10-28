# 輸入各筆測資
basic_string = input()  # [0]是物品個數，[1]是負重上限
weight_string = input()  # 重量
value_string = input()  # 效用aka價值
carry_string = input()  # 要不要帶

# 切割字串，存成List
basic = basic_string.split(",")
weightList = weight_string.split(",")
valueList = value_string.split(",")
carryList = carry_string.split(",")

thingList = []

# 將各物品的重量、效用和要不要帶存成一個List
# 再存入一個大List中，成為List中List
for i in range(int(basic[0])):
    thing = [0] * 3
    thing[0] = int(weightList[i])
    thing[1] = int(valueList[i])
    thing[2] = int(carryList[i])
    thingList.append(thing)

totalweight = 0
totalvalue = 0

# 判斷各物品要不要帶，加總要帶的物品的重量和效用
for i in range(int(basic[0])):
    if thingList[i][2] != 0:
        totalweight += thingList[i][0]
        totalvalue += thingList[i][1]

# 輸出結果
if totalweight <= int(basic[1]):
    print(totalweight, totalvalue, sep=",")
else:
    print(-1)