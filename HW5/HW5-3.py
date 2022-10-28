# 題目提供之格式化輸出函式
def printresult(value):
    print(f"{value:.4f}")


# my_hhi用來計算HHI(產業競爭程度)
# parameters為ylist和htype，分別為廠商營收的List和HHI的計算方式
def my_hhi(ylist, htype):
    totalcompany = 0  # 各公司營收絕對值的總和
    for i in ylist:
        # 若該公司營收為負，將其變正值
        if i < 0:
            i = -i
        totalcompany += i

    total_market_share = 0  # 市場占有率的總和
    for i in ylist:
        total_market_share += (i / totalcompany) ** 2  # Original的計算方式

    # 若計算方法為Original，則回傳上面計算的結果
    # 若為Normalized，則先將Original得到的值再作運算並回傳
    if htype == "Original":
        value = total_market_share
        return value
    elif htype == "Normalized":
        value = (total_market_share - 1 / len(ylist)) / (1 - 1 / len(ylist))
        return value


# 輸入測資
company_lst = input().split(",")
for i in range(len(company_lst)):
    company_lst[i] = float(company_lst[i])  # 將各element轉為浮點數
htype = input()

printresult(my_hhi(company_lst, htype))  # 格式化輸出回傳的值