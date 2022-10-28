# 輸入測資並將其切開成List，再轉成整數
num = input().split(",")
num[0] = int(num[0])
num[1] = int(num[1])

fire = input().split(",")

town_lst = []
for i in range(num[0]):
    town = input().split(",")
    for n in range(num[0]):
        town[n] = int(town[n])
    fire[i] = int(fire[i])
    town_lst.append(town)

"""
num[0]:城鎮數、num[1]:消防局數
fire:各城鎮可能失火的次數
town_lst:各城鎮與其他城鎮的距離
town_lst_1:town_lst的備份
"""

# 計算出第一間消防局所在的城鎮
maxLength = 20 * 20 * 1000
for i in range(num[0]):
    totalLength = 0
    for n in range(num[0]):
        length = town_lst[i][n] * fire[n]
        totalLength += length
    if maxLength > totalLength:
        maxLength = totalLength
        index = i

# town_remain中裝有尚未被選擇的城鎮
town_remain = []
for i in range(num[0]):
    town_remain.append(i)
town_remain.pop(index)

# 設定一個List來儲存有消防局的城鎮index
FB_lst = []
FB_lst.append(index)

if num[1] == 1:
    print(index + 1, maxLength, sep=";")
# index:第一間消防局所在城鎮的index，輸出時記得加1
elif num[1] == 2:
    maxLength = 0
    for i in range(num[0]):
        if maxLength < town_lst[index][i] and town_lst[index][i] != 0:
            maxLength = town_lst[index][i]
            FB = i
    town_remain.remove(FB)  # 現在town_remain中剩下除了有消防局的兩座城鎮以外的城鎮，並依序由小到大排著
    FB_lst.append(FB)

    # 開始計算剩餘城鎮要被分配給哪個有消防局的城鎮，選近的
    final_length = 0
    for i in town_remain:
        minLength = 1000
        for n in FB_lst:
            if minLength > town_lst[i][n] and town_lst[i][n] != 0:
                minLength = town_lst[i][n]
        final_length += minLength * fire[i]
    FB_str = ""
    for i in FB_lst:
        if i == FB_lst[0]:
            FB_str += str(i + 1) + ","
        else:
            FB_str += str(i + 1)
    print(FB_str, final_length, sep=";")
else:
    maxLength = 0
    for i in range(num[0]):
        if maxLength < town_lst[index][i] and town_lst[index][i] != 0:
            maxLength = town_lst[index][i]
            FB = i
    town_remain.remove(FB)  # 現在town_remain中剩下除了有消防局的兩座城鎮以外的城鎮，並依序由小到大排著
    FB_lst.append(FB)
    # 這段是從上面選第二間的程式碼搬來的

    for m in range(num[1] - 2):
        maxLength = 0
        for i in town_remain:
            minLength = 1000
            for n in FB_lst:
                if minLength > town_lst[i][n]:
                    minLength = town_lst[i][n]
            if maxLength < minLength:
                maxLength = minLength
                FB = i
        FB_lst.append(FB)
        town_remain.remove(FB)

    final_length = 0
    for i in town_remain:
        minLength = 1000
        for n in FB_lst:
            if minLength > town_lst[i][n] and town_lst[i][n] != 0:
                minLength = town_lst[i][n]
        final_length += minLength * fire[i]
    FB_str = ""
    for i in FB_lst:
        if i != FB_lst[-1]:
            FB_str += str(i + 1) + ","
        else:
            FB_str += str(i + 1)
    print(FB_str, final_length, sep=";")