# 輸入欲讀取之檔案名稱
filename = input()
index = int(input())  # 輸入欲查詢之第幾筆資料
# name = "C:\\Users\\user\\Desktop\\" + filename
company_information = open(filename, "r", encoding="utf-8")  # 開啟檔案並讀取

# 將讀取到的各行資料切開成List，並存入一個大的List中
information_lst = []
for data in company_information:
    information = data.strip().split(",")
    if information[0][0] == '"' and information[1][-1] == '"':
        information[0] = information[0] + "," + information[1]
        information.remove(information[1])
    information_lst.append(information)

print("營業人名稱: " + information_lst[index][3].strip('"'))
print("統一編號: " + information_lst[index][1])
print("營業地址: " + information_lst[index][0].strip('"'))