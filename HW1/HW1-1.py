money = int(input())  # 輸入帶的錢
pancake = int(input())  # 輸入蔥抓餅價格
drink = int(input())  # 輸入飲料價格

if money >= pancake:  # 帶的錢夠買蔥抓餅嗎？
    balance = money - pancake
    if balance >= drink:  # 剩的錢夠買飲料嗎？
        balance = balance - drink
        print(balance)
    else:
        print(balance)
elif money >= drink:  # 買不了蔥抓餅，買的了飲料嗎？
    balance = money - drink
    print(balance)
else:
    print(money)