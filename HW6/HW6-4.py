# 定義一個函式，用來處理字串
def str_format(element):
    differ = width - len(element)  # 要加幾個空白
    if differ >= 0:  # 如果字串沒有超過指定的長度
        str_new = ""
        for j in range(differ):
            str_new += " "
        str_new += element
        data[i] = str_new
    else:
        str_new = ""
        for j in range(width - 1):
            str_new += element[j]
        str_new += "~"
        data[i] = str_new
    return data[i]


# 輸入指定長度和格式串
width = int(input())
form = input().split(",")

data_str = []
while True:
    data = input().split(",")
    if data == ["RECORD_END"]:  # 當碰到"RECORD_END"時，停止
        break
    for i in range(len(form)):
        if form[i] == "f":
            data[i] = str(f"{float(data[i]):0.2f}")  # 將格式為數字的部分轉為浮點數
    for i in range(len(data)):
        str_format(data[i])
    data_str.append(data)

# 逐行輸出結果
for i in range(len(data_str)):
    print(" ".join(data_str[i]))