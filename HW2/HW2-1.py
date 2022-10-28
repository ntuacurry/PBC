order_threshold = int(input())  # 達成獎勵的訂單數門檻
pay1 = int(input())  # 未達訂單門檻的報酬
pay2 = int(input())  # 超過訂單門檻的報酬
order_complete = int(input())  # 外送員完成的訂單數

if order_complete <= order_threshold:  # 如果完成的訂單數少於門檻
    print(order_complete * pay1)
else:  # 如果完成的訂單數超過門檻
    print(order_threshold * pay1 + (order_complete - order_threshold) * pay2)