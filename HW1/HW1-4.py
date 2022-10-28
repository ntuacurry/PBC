num1 = int(input())  # 輸入第一個數字
num2 = int(input())  # 輸入第二個數字

H1 = num1 // 100  # 取數字一的百位數
T1 = num1 % 100 // 10  # 取數字一的十位數
O1 = num1 % 10  # 取數字一的個位數

H2 = num2 // 100  # 取數字二的百位數
T2 = num2 % 100 // 10  # 取數字二的十位數
O2 = num2 % 10  # 取數字二的個位數

A1 = 0
A2 = 0
A3 = 0
B1 = 0
B2 = 0
B3 = 0

# 判斷各個位數是否相等且在對應的位置

if H1 == H2:
    A1 = 1
elif H1 == T2:
    B1 = 1
elif H1 == O2:
    B1 = 1

if T1 == H2:
    B2 = 1
elif T1 == T2:
    A2 = 1
elif T1 == O2:
    B2 = 1

if O1 == H2:
    B3 = 1
elif O1 == T2:
    B3 = 1
elif O1 == O2:
    A3 = 1

A = A1 + A2 + A3  # 加總數字相同且位置相同的個數
B = B1 + B2 + B3  # 加總數字相同且位置不同的個數

print(str(A) + "A" + str(B) + "B")