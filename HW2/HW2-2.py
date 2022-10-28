order_threshold_day = int(input())  # 每日達成獎勵的訂單數門檻
order_threshold_week = int(input())  # 每周達成獎勵的訂單數門檻
pay = int(input())  # 未達訂單門檻的報酬
bonus_day = int(input())  # 超過訂單門檻的報酬
bonus_week = int(input())  # 外送員完成的訂單數
order_Mon = int(input())  # 星期一完成之訂單數
order_Tue = int(input())  # 星期二完成之訂單數
order_Wen = int(input())  # 星期三完成之訂單數
order_Thu = int(input())  # 星期四完成之訂單數
order_Fri = int(input())  # 星期五完成之訂單數
order_Sat = int(input())  # 星期六完成之訂單數
order_Sun = int(input())  # 星期日完成之訂單數

totalProfit = 0  # 總獲利
totalOrder = 0  # 一周的總訂單數
i = 0  # 一周的第幾天

# 以for迴圈處理每一天的訂單數量，確認是否可獲得額外的獎勵

for order in order_Mon, order_Tue, order_Wen, order_Thu, order_Fri, order_Sat, order_Sun:
    if order <= order_threshold_day:  # 如果當日完成的訂單數少於每日門檻
        profit = order * pay
    else:  # 如果當日完成的訂單數超過每日門檻
        profit = order_threshold_day * pay + (order - order_threshold_day) * bonus_day

    totalProfit = totalProfit + profit  # 將每天的獲利加總
    totalOrder = totalOrder + order  # 將每天的訂單數加總
    i = i + 1  # 計算目前計算到一周的第幾天

if i == 7:  # 當計算完星期日的獲利時
    if totalOrder < order_threshold_week:  # 如果一周的總訂單數少於每周門檻
        print(totalProfit)
    else:  # 如果一周的總訂單數達到每周門檻
        print(totalProfit + bonus_week)