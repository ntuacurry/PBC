order_id = int(input())  # 訂單數
price_single = int(input())  # 玩具車單價的最低限度
time_1 = int(input())  # 員工一組裝一輛玩具車所需的時間
time_2 = int(input())  # 員工二包裝一輛玩具車所需的時間

staff_1 = 8 * 60  # 員工一有8小時可以工作
staff_2 = 8 * 60  # 員工二有8小時可以工作
totalProfit = 0  # 公司總營收，初始值設為0
order_list = ""  # 所有被接受的訂單編號

for order in range(1, order_id + 1):
    car = int(input())  # 輸入該筆訂單之玩具車數量
    price_total = int(input())  # 輸入該筆訂單之總金額

    if price_total / car >= price_single:  # 玩具車單價是否超過最低限度
        time_1_total = car * time_1
        time_2_total = car * time_2

        if time_1_total <= staff_1 and time_2_total <= staff_2:  # 若員工一、二皆有足夠之剩餘時間，則接受該筆訂單
            staff_1 = staff_1 - time_1_total
            staff_2 = staff_2 - time_2_total

            totalProfit = totalProfit + price_total
            order_list = order_list + str(order) + ","

if totalProfit == 0:  # 輸出沒有任何一張訂單被接受的情形
    print(-1)
    print(480, 480, 0, sep=",")
else:  # 輸出所有被接受之訂單的情形
    print(order_list.rstrip(","))
    print(staff_1, staff_2, totalProfit, sep=",")