# 引入math套件
import math

# 輸入欲讀取之檔案名稱
filename = input()
# name = "C:\\Users\\user\\Desktop\\" + filename
company_information = open(filename, "r", encoding="utf-8")  # 開啟檔案並讀取

# 將讀取到的各行資料切開成List，並存入一個大的List中
information_lst = []
for data in company_information:
    information = data.strip().split(",")
    if information[0][0] == '"' and information[1][-1] == '"':  # 如果地址中因包含逗號而不慎被切開，則把它們接回去
        information[0] = information[0] + "," + information[1]
        information.remove(information[1])
    information_lst.append(information)

# industrial code: 行業代號，變數設為IC
# industrial name: 行業名稱，變數設為IN
# registered capital: 資本額，變數設為RC

# 將行業代碼、行業名稱、資本額存入dictionary中
pair = dict()
for i in range(1, len(information_lst)):
    for j in 8, 10, 12, 14:
        IC = information_lst[i][j]
        IN = information_lst[i][j + 1]
        RC = int(information_lst[i][4])
        if IC != "" and IN != "":
            if IC not in pair:
                pair[IC] = [IN, RC]
            else:
                pair[IC].append(RC)

pair_lst = []
for key in pair:
    lst = pair[key][1:]
    amount = len(pair[key]) - 1
    lst.sort()
    if amount % 2 == 0:  # 如果資本額的個數為偶數，則中位數為中間兩個數的平均
        index = int(amount / 2)
        median = round((lst[index] + lst[index - 1]) / 2)  # 四捨五入
    else:  # 如果資本額的個數為奇數，則中位數為中間那個數
        index = int((amount - 1) / 2)
        median = round(lst[index])  # 四捨五入
    pair_lst.append([key, pair[key][0], median, amount])  # 將行業代碼、行業名稱、資本額中位數和數量存入List中

# 依條件排序
pair_lst.sort(key=lambda i: i[0])  # 行業代號由小到大
pair_lst.sort(key=lambda i: -i[2])  # 資本額中位數由大到小

# 依序輸出，最多10筆
count = 0
for i in range(len(pair_lst)):
    code = pair_lst[i][0]
    name = pair_lst[i][1]
    med = pair_lst[i][2]
    num = pair_lst[i][3]
    print(f"{code} ({name}): ${med}; N={num}")
    count += 1

    if count == 10:
        break