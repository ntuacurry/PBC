# 定義一個函式用來輸出結果
def printresult(i, count):
    if i >= count:
        # 將前面幾個字串的字首轉換成大寫字母的編碼
        alpha_num = []  # 儲存字首的編碼
        full_name = []
        for m in range(i - count, i):
            if ord(text_new[m][0]) >= 97 and ord(text_new[m][0]) <= 122:
                alpha_num.append(ord(text_new[m][0]) - 32)
            else:
                alpha_num.append(ord(text_new[m][0]))
            full_name.append(text_new[m])
        # 比較兩組編碼(ABBREV_num和alpha_num)是否相同
        whether_print = 0
        for n in range(len(ABBREV_num)):
            if ABBREV_num[n] != alpha_num[n]:
                whether_print = 1
        if whether_print == 0 and ABBREV != "":
            print(ABBREV + ": ", (" ").join(full_name), sep="")


# 輸入文本
text = input().split(" ")

symbol = ['。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"', "#$%&'*+,-./:;<=>?@[]^_`{¦}~"]  # 會用到的標點符號
symbol_lst = []  # 儲存標點符號
# 將各個標點符號存入List
for i in range(len(symbol[0])):
    symbol_lst.append(symbol[0][i])
for i in range(len(symbol[1])):
    symbol_lst.append(symbol[1][i])

# 處理輸入的文本，去除括號以外的標點符號
text_new = []
for i in range(len(text)):
    subtext = ""
    for j in range(len(text[i])):
        if text[i][j] not in symbol_lst:
            subtext += text[i][j]
    text_new.append(subtext)
for i in range(text_new.count("")):
    text_new.remove("")

for i in range(len(text_new)):
    # 找到左右皆為括號的字串
    if text_new[i][0] == "(":
        count = 0  # 縮寫字數計數器
        ABBREV_num = []  # 記錄縮寫字母的各代碼
        ABBREV = ""  # 記錄縮寫的字母是什麼
        # 判斷括號中是否為字母
        for j in range(len(text_new[i])):
            if ord(text_new[i][j]) >= 65 and ord(text_new[i][j]) <= 90:
                count += 1
                ABBREV_num.append(ord(text_new[i][j]))
                ABBREV += text_new[i][j]
            elif ord(text_new[i][j]) >= 97 and ord(text_new[i][j]) <= 122:
                count += 1
                ABBREV_num.append(ord(text_new[i][j]))
                ABBREV += text_new[i][j]
        printresult(i, count)