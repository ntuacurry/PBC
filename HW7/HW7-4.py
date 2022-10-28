# 輸入欲讀取之檔案名稱
filename = input()
# name = "C:\\Users\\user\\Desktop\\" + filename
company_information = open(filename, "r", encoding="utf-8")  # 將檔案打開並讀取

# 將讀取到的各行資料切開成List，並存入一個大的List中
information_lst = []
for data in company_information:
    information = data.strip().split(",")
    if information[0][0] == '"' and information[1][-1] == '"':  # 如果地址中因包含逗號而不慎被切開，則把它們接回去
        information[0] = information[0] + "," + information[1]
        information.remove(information[1])
    information_lst.append(information)

# industrial code: 行業代號，變數設為IC
# industrial name: 行業名稱，變數設為IN

IC_dict = dict()  # 存取行業代碼與行業名稱作為對照
IC_lst = []
for i in range(1, len(information_lst)):
    IC_sublst = []  # 存取單筆資料中行業代碼與行業名稱的組合
    for j in 8, 10, 12, 14:
        IC = information_lst[i][j]
        IN = information_lst[i][j + 1]
        if IC != "" and IN != "":
            # 將行業代碼與行業名稱對應，並存入dictionary。
            if IC not in IC_dict:
                IC_dict[IC] = IN
            IC_sublst.append(IC)
    # 單筆資料中要存在兩種以上行業代碼才能將其兩兩成對，因此以其長度為二作為篩選
    if len(IC_sublst) >= 2:
        IC_lst.append(sorted(IC_sublst))  # 將符合條件的資料先由小至大排序，再存入IC_lst

# 在單筆資料中產生兩兩成對的組合
pair_lst = []
for i in range(len(IC_lst)):
    pair = []
    for j in range(len(IC_lst[i])):
        for m in range(j + 1, len(IC_lst[i])):
            subPair = [IC_lst[i][j], IC_lst[i][m]]
            pair.append(subPair)
    pair_lst.append(pair)

# 賴用dictionary來計算同一組合的出現次數
pair_dict = dict()
for i in range(len(pair_lst)):
    for j in pair_lst[i]:
        key = tuple(j)
        if key not in pair_dict:
            pair_dict[key] = 1
        else:
            pair_dict[key] += 1

# 將計算完之結果存成List，以進行排序
total_ans = []
for key in pair_dict:
    ans = list(key)
    ans.append(pair_dict[key])
    total_ans.append(ans)

# 依條件排序
total_ans.sort(key=lambda i: i[1])
total_ans.sort(key=lambda i: i[0])
total_ans.sort(key=lambda i: -i[2])

# 依序輸出，最多輸出20筆
for i in range(len(total_ans)):
    ans1 = IC_dict[total_ans[i][0]]
    ans2 = IC_dict[total_ans[i][1]]
    ans3 = total_ans[i][2]
    print(ans1, ans2, ans3)
    if i == 19:
        break