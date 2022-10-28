id1 = int(input())  # 學生一
id2 = int(input())  # 學生二
id3 = int(input())  # 學生三
dept1 = int(input())  # 科系一
dept2 = int(input())  # 科系二
dept3 = int(input())  # 科系三
code1 = int(input())  # 老師提供的科系編號一
code2 = int(input())  # 老師提供的科系編號二

# 比較學生的科系編號是否與老師提供的科系編號相符
if dept1 == code1 or dept1 == code2:
    dept1 = id1
else:
    dept1 = 0

if dept2 == code1 or dept2 == code2:
    dept2 = id2
else:
    dept2 = 0

if dept3 == code1 or dept3 == code2:
    dept3 = id3
else:
    dept3 = 0

# 學號比大小並依大小輸出結果

if dept1 != 0:  # 學生一可以加簽的情況
    if dept1 > dept2 and dept1 > dept3:
        if dept2 > dept3 and dept3 != 0:
            print(dept3, dept2, dept1, sep=",")
        elif dept2 > dept3 and dept3 == 0:
            print(dept2, dept1, sep=",")
        elif dept3 > dept2 and dept2 == 0:
            print(dept3, dept1, sep=",")
        elif dept3 > dept2 and dept2 != 0:
            print(dept2, dept3, dept1, sep=",")
        else:
            print(dept1)
    elif dept3 > dept1 and dept3 > dept2:
        if dept1 > dept2 and dept2 != 0:
            print(dept2, dept1, dept3, sep=",")
        elif dept1 > dept2 and dept2 == 0:
            print(dept1, dept3, sep=",")
        elif dept2 > dept1 and dept1 == 0:
            print(dept2, dept3, sep=",")
        elif dept2 > dept1 and dept1 != 0:
            print(dept1, dept2, dept3, sep=",")
        else:
            print(dept1)
    elif dept2 > dept1 and dept2 > dept3:
        if dept1 > dept3 and dept3 != 0:
            print(dept3, dept1, dept2, sep=",")
        elif dept1 > dept3 and dept3 == 0:
            print(dept1, dept2, sep=",")
        elif dept3 > dept1 and dept1 == 0:
            print(dept3, dept2, sep=",")
        elif dept3 > dept1 and dept1 != 0:
            print(dept1, dept3, dept2, sep=",")
        else:
            print(dept1)
    else:
        print(-1)
else:  # 學生一不能加簽的情況
    if dept2 > dept3 and dept3 == 0:
        print(dept2)
    elif dept2 > dept3 and dept3 != 0:
        print(dept3, dept2, sep=",")
    elif dept3 > dept2 and dept2 == 0:
        print(dept3)
    elif dept3 > dept2 and dept2 != 0:
        print(dept2, dept3, sep=",")
    else:
        print(-1)