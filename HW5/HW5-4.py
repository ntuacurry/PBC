# 題目提供之格式化輸出函式
def printrec(records):
    for arec in records:
        # 避免浮點數誤差
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")


# 名為apply_discount的函式，parameter為records
# records用來接收雙層List
def apply_discount(records):
    discount = 0  # 折扣總和
    totalprice = 0  # 價格總和
    for i in range(len(records)):
        # List中每個List的最後一個element為金額
        if records[i][-1] > 0:  # 若金額為正，則為價格
            totalprice += records[i][-1]
        else:  # 若金額為負，則為折扣
            discount += records[i][-1]
    global original_lst  # 傳入全域變數original_lst
    for i in range(len(records)):
        original_lst.append(records[i].copy())  # 複製原始的List
        if records[i][-1] > 0:
            # 計算折扣後的價格
            records[i][-1] += (records[i][-1] / totalprice) * discount
            # 折扣若大於價格，只能折到剩0元
            if records[i][-1] < 0:
                records[i][-1] = 0
    records_final = []  # 用來儲存有獲得折扣之品項
    for i in range(len(records)):
        if records[i][-1] >= 0:
            records_final.append(records[i])
    return printrec(records_final)  # 回傳經格式化輸出處理之獲得折扣之品項List


# 輸入第一筆測資並將其切成List
data = input().split("_")
lst = []
lst.append(data)
# 接著繼續輸入剩於測資，直到輸入的是RECORDSTOP
while data != "":
    data = input()
    if data == "RECORDSTOP":
        break
    else:
        lst.append(data.split("_"))
# 將可轉成浮點數的部分轉為浮點數
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j != 0:
            lst[i][j] = float(lst[i][j])

original_lst = []  # 用來在apply_discount中儲存複製的原始List

apply_discount(lst)  # 輸出折扣完之品項
print("---Original---")  # 分隔線
printrec(original_lst)  # 格式化輸出原始的List