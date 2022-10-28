account1 = int(input())  # 第一個戶頭的金額
account2 = int(input())  # 第二個戶頭的金額
ratio = int(input())  # 匯率
transfer = int(input())  # 轉帳金額

if account1 > transfer:  # 轉帳金額是否大於第一個戶頭的金額
    account1 = account1 - transfer
    account2 = account2 + ratio * transfer
    print(account1, account2, sep=",")
else:
    account2 = account2 + ratio * account1
    account1 = 0
    print(account1, account2, sep=",")