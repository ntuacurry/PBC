# 輸入城鎮數、預期失火次數
num = int(input())
fire_str = input()
fire = fire_str.split(",")

# 輸入各城鎮與其他城鎮的距離
town_lst = []
for i in range(num):
    town_str = input()
    town = town_str.split(",")
    for index in range(num):
        town[index] = int(town[index])
    town_lst.append(town)
    fire[i] = int(fire[i])

# 計算各城鎮之消防車移動路徑長
# 並選出最小移動路徑長以及該城鎮編號
maxLength = 20 * 20 * 1000
for i in range(num):
    totalLength = 0
    for index in range(num):
        length = town_lst[i][index] * fire[index]
        totalLength += length
    if maxLength > totalLength:
        maxLength = totalLength
        town_num = i + 1

# 輸出結果
print(town_num, maxLength, sep=",")