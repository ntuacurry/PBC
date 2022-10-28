# mono_inc用來找出第一個連續上升天數足夠長的區段
def mono_inc(inlist, k):
    lst_dif = []  # 宣告一個空的list，用來存lst中相鄰兩數的差
    for i in range(len(lst)):
        if i == len(lst) - 1:
            break
        else:
            lst_dif.append(lst[i + 1] - lst[i])

    count = 0  # 這是計數器
    for i in range(len(lst_dif)):
        if lst_dif[i] > 0:  # 依序檢查lst_dif中的元素，若該元素大於0，則計數器加一
            count += 1
            if i == len(lst_dif) - 1 and count >= k:  # 若該元素的index到達盡頭  and 計數器大於k，則輸出起始和終止index
                print((i + 1) - count)
                print(i + 1)
                return (i - count), i
        elif lst_dif[i - 1] > 0 and count >= k:  # 若該元素小於0，但前一個元素大於零 and 計數器大於k，則輸出起始和終止index
            print(i - count)
            print(i)
            return (i - count), i
        else:
            count = 0
    print("None")  # 若整個lst_dif中皆無連續k天以上的上升天數，則輸出None
    return 0


# 輸入測資並切開成List
lst = input().split(",")
for i in range(len(lst)):
    lst[i] = int(lst[i])
k = int(input())

# 如果k小於3，就把k指定為3
if k < 3:
    k = 3

mono_inc(lst, k)  # 執行mono_inc，argument分別為一開始輸入的lst和k