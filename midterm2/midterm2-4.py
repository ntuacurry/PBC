# 輸入欲讀取之檔案名稱
filename = input()
text = open(filename, "r", encoding="utf-8")  # 開啟檔案並讀取

total_lst = text.readlines()

new_lst = []
for i in range(len(total_lst)):
    total_lst[i] = total_lst[i].strip()
    if total_lst[i] != "":
        new_lst.append([len(total_lst[i]), total_lst[i], i])

symbol = ['。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"', "#$%&'()*+,-./:;<=>?@[]^_`{¦}~"]  # 會用到的標點符號
symbol_num = []  # 儲存標點符號的UTF-8編碼
# 將各個標點符號轉成UTF-8編碼並存入List
for i in range(len(symbol[0])):
    symbol_num.append(ord(symbol[0][i]))
for i in range(len(symbol[1])):
    symbol_num.append(ord(symbol[1][i]))
for i in range(len(symbol_num)):
    symbol_num[i] = int(symbol_num[i])

for i in range(len(new_lst)):
    count = 0
    for j in range(len(new_lst[i][1])):
        if ord(new_lst[i][1][j]) in symbol_num:
            new_lst[i][0] -= 1

new_lst.sort(key=lambda i: i[-1])
new_lst.sort(key=lambda i: -i[0])

if len(new_lst) < 3:
    for i in range(len(new_lst)):
        print(new_lst[i][0], new_lst[i][1])
else:
    print(new_lst[0][0], new_lst[0][1])
    print(new_lst[1][0], new_lst[1][1])
    print(new_lst[2][0], new_lst[2][1])
    for i in range(3, len(new_lst)):
        if new_lst[i][0] == new_lst[2][0]:
            print(new_lst[i][0], new_lst[i][1])