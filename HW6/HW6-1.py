# 輸入連續詞長度和字串
length = int(input())
word = input()

symbol = ['。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"', "#$%&'()*+,-./:;<=>?@[]^_`{¦}~"]  # 會用到的標點符號
symbol_num = []  # 儲存標點符號的UTF-8編碼
# 將各個標點符號轉成UTF-8編碼並存入List
for i in range(len(symbol[0])):
    symbol_num.append(ord(symbol[0][i]))
for i in range(len(symbol[1])):
    symbol_num.append(ord(symbol[1][i]))
for i in range(len(symbol_num)):
    symbol_num[i] = int(symbol_num[i])

# 是否符合指定的連續詞長度之判斷
# 若指定的連續詞長度小於2，則輸出ILLEGAL_N
if length < 2:
    print("ILLEGAL_N")
else:
    for i in range(len(word) - length + 1):
        string = ""
        # 字串處理迴圈
        for m in range(i, i + length):
            # 若UTF-8編碼與標點符號之編碼相同，則跳出字串處理的迴圈；如果不是，則把字元串起來
            if ord(word[m]) in symbol_num:
                break
            else:
                string += word[m]
        # 如果字串長度與指定連續詞長度相等，輸出該字串
        if len(string) == length:
            print(string)