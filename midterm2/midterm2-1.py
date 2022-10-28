num_lst = input().split(",")
for i in range(len(num_lst)):
    num_lst[i] = float(num_lst[i])

# 做2階自我相關函數
def autocor_2(ts):
    length = len(ts)
    lst_A = ts[:(length - 2)]
    lst_B = ts[2:length]
    
    # 計算A和B的平均數
    sum_A = 0
    for a in lst_A:
        sum_A +=  a
    avg_A = sum_A / (length - 2)
    sum_B = 0
    for b in lst_B:
        sum_B +=  b
    avg_B = sum_B / (length - 2)
    
    # 計算VAR(A)和VAR(B)
    sqr_A = 0
    for a in lst_A:
        sqr_A += (a - avg_A) ** 2
    var_A = sqr_A / (length - 3)
    sqr_B = 0
    for b in lst_B:
        sqr_B += (b - avg_B) ** 2
    var_B = sqr_B / (length - 3)
    
    sqr_COV = 0
    for i in range(length - 2):
        sqr_COV += (lst_A[i] - avg_A) *(lst_B[i] - avg_B)
    COV = sqr_COV / (length - 3)
    
    cor_AB = COV / ((var_A * var_B) ** 0.5)
    
    return cor_AB

ans = autocor_2(num_lst)
if ans >= 0.000001 or ans <= -0.000001:
    print(f"{ans:.4f}")
else:
    print("0.0000")