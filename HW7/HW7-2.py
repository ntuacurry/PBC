filename = input()

# 讀入檔案
company_information = open(filename, "r", encoding="utf-8")

# 將從檔案中讀到的各行測資切開成List
information_lst = []
for data in company_information:
    information = data.strip().split(",")
    if information[0][0] == '"' and information[1][-1] == '"':
        information[0] = information[0] + "," + information[1]
        information.remove(information[1])
    information_lst.append(information)

# 計算各欄位的長度並比較出最大長度
for i in range(len(information_lst[0])):
    maxLength = 0
    for j in range(len(information_lst)):
        length = len(information_lst[j][i])
        if maxLength < length:
            maxLength = length

    # 若欄位為地址或公司名，其長度需先扣掉兩個引號
    if i == 0 or i == 3:
        print(maxLength - 2)
    else:
        print(maxLength)