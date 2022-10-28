# 引入datetime模組
import datetime

# 輸入欲讀取之檔案
filename = input()
index = input()  # 欲搜尋之字串
# name = "C:\\Users\\user\\Desktop\\" + filename
company_information = open(filename, "r", encoding="utf-8")  # 開啟檔案並讀取

# 將讀取到的各行資料切開成List，並存入一個大的List中
information_lst = []
for data in company_information:
    information = data.strip().split(",")
    if information[0][0] == '"' and information[1][-1] == '"':
        information[0] = information[0] + "," + information[1]
        information.remove(information[1])
    information_lst.append(information)

# name of business entity: 營業人名稱，變數設為NBE
# uniform number: 統一編號，變數設為UN
# head office uniform number: 總機構統一編號，變數設為HOUN
# date of incorporation: 設立日期，變數設為DI
# registered capital: 資本額，變數設為RC
# business address: 營業地址，變數設為BA

# 將營業人名稱、統一編號、設立日期、資本額和營業地址轉換為適當格式並存入List中
data_lst = []
for i in range(1, len(information_lst)):
    NBE = information_lst[i][3].strip('"')
    UN = information_lst[i][1]
    HOUN = information_lst[i][2]
    if HOUN != "":
        UN += "(" + HOUN + ")"
    # 將設日期轉為西元格式
    DI = information_lst[i][5]
    DI = datetime.date((int(DI[0:3]) + 1911), int(DI[3:5]), int(DI[5:7]))
    DI = DI.strftime("%Y-%m-%d")

    # 將資本額每隔三位數加一個逗號
    RC = information_lst[i][4]
    RC = format(int(RC), "0,")

    BA = information_lst[i][0].strip('"')
    data_sublst = [NBE, UN, DI, RC, BA]

    # 如果字串長度不滿20，以空格補滿
    for j in range(5):
        if len(data_sublst[j]) < 20:
            for m in range(20 - len(data_sublst[j])):
                if j == 0:
                    data_sublst[j] += "　"
                else:
                    data_sublst[j] += " "
    data_lst.append(data_sublst)

# 依條件排序
data_lst.sort(key=lambda i: i[1])  # 統一編號由小到大
data_lst.sort(key=lambda i: -int(i[3].replace(",", "")))  # 資本額由大到小
data_lst.sort(key=lambda i: i[2])  # 設立日期由小到大

count = 0  # 計算輸出的資料數
check = 0  # 用以確定是否有符合的資料。0為無，1為有
for i in range(len(data_lst)):
    # 如果欲搜尋之字串存在統一編號中，則輸出該筆資料
    if index in data_lst[i][1]:
        check = 1
        count += 1
        print(" ".join(data_lst[i]))

    # 如果輸出20筆，則停止
    if count == 20:
        break

    # 如果都沒有符合的資料，則輸出NO_DATA_FOUND
    if i == (len(data_lst) - 1) and check == 0:
        print("NO_DATA_FOUND")