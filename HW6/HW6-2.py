# 輸入指定連續詞長度、目標文本以及參考文本
length = int(input())
target = input()
source = input()

symbol = ['。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"', "#$%&'()*+,-./:;<=>?@[]^_`{¦}~"]  # 會用到的標點符號
symbol_num = []  # 儲存標點符號的UTF-8編碼
# 將各個標點符號轉成UTF-8編碼並存入List
for i in range(len(symbol[0])):
    symbol_num.append(ord(symbol[0][i]))
for i in range(len(symbol[1])):
    symbol_num.append(ord(symbol[1][i]))
for i in range(len(symbol_num)):
    symbol_num[i] = int(symbol_num[i])

# 計算目標文本中的連續詞數量
LEN = 0  # 連續詞數量計數器
for i in range(len(target) - length + 1):
    count = 0
    for m in range(i, i + length):
        if ord(target[m]) in symbol_num:
            break
        else:
            count += 1
    if count == length:
        LEN += 1

# 計算目標文本與參考文本中重疊之連續詞及其數量
MATCH_COUNT = 0  # 重疊之連續詞數量
MATCH_SEGMENTS = []  # 重疊之連續詞
for i in range(len(target) - length + 1):
    # 目標文本中的連續詞
    target_str = ""
    for j in range(i, i + length):
        if ord(target[j]) in symbol_num:
            break
        else:
            target_str += target[j]
    # 若目標文本之連續詞長度符合指定之連續詞長度時，開始進行參考文本中連續詞之產生，並一一進行比較是否重疊
    if len(target_str) == length:
        for m in range(len(source) - length + 1):
            # 參考文本中的連續詞
            source_str = ""
            for n in range(m, m + length):
                if ord(source[n]) in symbol_num:
                    break
                else:
                    source_str += source[n]
            if target_str == source_str:  # 若目標文本之連續詞與參考文本之連續詞相同(重疊)，則重疊數量加一，並將該連續詞存入List中
                MATCH_COUNT += 1
                MATCH_SEGMENTS.append(target_str)

print("LEN=", LEN, sep="")
print("MATCH_COUNT=", MATCH_COUNT, sep="")
print("SIMILARITY=", f"{(MATCH_COUNT / LEN):0.4f}", sep="")  # 格式化輸出相似度
print("MATCHED SEGMENTS:")
for i in MATCH_SEGMENTS:
    print(i)