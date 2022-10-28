cost = int(input())  # 輸入消費金額
change = 1000 - cost  # change是要找的錢

FH = change // 500  # FH是500的張數
OH = (change % 500) // 100  # OH是100的張數
FT = (change % 100) // 50  # FT是50的個數
Ten = (change % 50) // 10  # Ten是10的個數
Five = (change % 10) // 5  # Five是5的個數
One = change % 5  # One是1的個數

# 檢查各面額之個數是否為零，若為零則不輸出

if FH >= 1:  # FH是否不為0
    fh = "500, " + str(FH) + "; "
    if OH == FT == Ten == Five == One == 0:
        fh = "500, " + str(FH)
else:
    fh = ""

if OH >= 1:  # OH是否不為0
    oh = "100, " + str(OH) + "; "
    if FT == Ten == Five == One == 0:
        oh = "100, " + str(OH)
else:
    oh = ""

if FT >= 1:  # FT是否不為0
    ft = "50, " + str(FT) + "; "
    if Ten == Five == One == 0:
        ft = "50, " + str(FT)
else:
    ft = ""

if Ten >= 1:  # Ten是否不為0
    ten = "10, " + str(Ten) + "; "
    if Five == One == 0:
        ten = "10, " + str(Ten)
else:
    ten = ""

if Five >= 1:  # Five是否不為0
    five = "5, " + str(Five) + "; "
    if One == 0:
        five = "5, " + str(Five)
else:
    five = ""

if One >= 1:  # One是否不為0
    one = "1, " + str(One)
else:
    one = ""

print(fh + oh + ft + ten + five + one)


'''
# 檢查各面額之個數是否為零，若為零則不輸出

if FH != 0:
    fh = "500, " + str(FH)
else:
    fh = ""
if OH != 0:
    oh = "100, " + str(OH)
else:
    oh = ""
if FT != 0:
    ft = "50, " + str(FT)
else:
    ft = ""
if Ten != 0:
    ten = "10, " + str(Ten)
else:
    ten = ""
if Five != 0:
    five = "5, " + str(Five)
else:
    five = ""
if One != 0:
    one = "1, " + str(One)
else:
    one = ""

print(fh, oh, ft, ten, five, one, sep = "; ", end = "")
'''