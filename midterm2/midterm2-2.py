def printresult(lst):
    for i in range(len(lst)):
        name = lst[i][0]
        value = float(f"{lst[i][1]:.1f}")
        print(f"{name} {value:.2f}")
    return 0

total_data = []
while True:
    data = input()
    if data == "RECORDSTOP":
        break
    data_lst = data.split("_")
    total_data.append(data_lst)

for i in range(len(total_data)):
    total_data[i][-1] = float(total_data[i][-1])
    total_data[i][-2] = float(total_data[i][-2])

# 去掉不符合條件的list
pop_lst = []
for i in range(len(total_data)):
    subdata = total_data[i]
    if "點" in subdata[0] or "點數" in subdata[0] or "折扣" in subdata[0] or subdata[-1] <= 0:
        pop_lst.append(i)
pop_lst.reverse()
for i in pop_lst:
    total_data.pop(i)

# 運算
final_lst = []
for i in range(len(total_data)):
    lst = []
    lst.append(total_data[i][0])
    lst.append(total_data[i][-1] / total_data[i][-2])
    lst.append(i)
    final_lst.append(lst)

final_lst.sort(key=lambda i: i[2])
final_lst.sort(key=lambda i: -i[1])

printresult(final_lst)