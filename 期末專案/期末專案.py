"""
2021.12.20 22:29
不用手動建txt & 用相對路徑（應該適用於每部電腦）

2021.12.20 00:27 更新
只是加了個把提醒時間也存進txt的code

2021.12.19 15:47 更新
新增數據儲存功能(目前仍需須先在桌面建立一個txt檔才能發揮功能，可參考讀檔路徑並修改)

2021.12.19 00:35 更新
新增表格照日期排序功能

2021.12.17 12:59 更新
新增表格填入與簡單的欄位驗證功能
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FoodReserve(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.food_date_list = []  # 表格內容的清單：[(food name, datestr), (food name, datestr), (food name, datestr)....]
        self.window()

    def add_event(self):
        self.food = self.FoodName.get()
        self.date = self.BestBefore.get()
        self.remind = self.Remind.get()
        self.BigMon = ["1", "3", "5", "7", "8", "10", "12"]
        self.SmallMon = ["4", "6", "9", "11"]
        if self.food == "":
            self.result = tk.messagebox.showwarning(title="注意", message="請輸入食物名稱！")
        elif self.date == "":
            self.result = tk.messagebox.showwarning(title="注意", message="請輸入保存期限！")
        elif len(self.date) != 8:
            self.result = tk.messagebox.showwarning(title="注意", message="請依照格式輸入日期！")
        elif self.date.isdigit() == False:
            self.result = tk.messagebox.showwarning(title="注意", message="請在保存期限中輸入數字！")
        elif self.food != "" and self.date != "" and len(self.date) == 8:
            if int(self.date[4:6]) > 12:
                self.result = tk.messagebox.showwarning(title="注意", message="一年只有12個月！")
            elif self.date[4:6] in self.BigMon and int(self.date[6:8]) > 31:
                self.result = tk.messagebox.showwarning(title="注意", message=date[4:6] + "月只有31天！")
            elif self.date[4:6] in self.SmallMon and int(self.date[6:8]) > 30:
                self.result = tk.messagebox.showwarning(title="注意", message=date[4:6] + "月只有30天！")
            elif self.date[4:6] == "2" and int(self.date[6:8]) > 28:
                self.result = tk.messagebox.showwarning(title="注意", message="2月只有28天！")
            else:
                self.datestr = self.date[0:4] + "/" + self.date[4:6] + "/" + self.date[6:8]
                self.food_date_tuple = (self.food, self.date, self.remind)
                self.food_datestr_tuple = (self.food, self.datestr, self.remind)

                #  有效期限快到的在上面
                if len(self.food_date_list) == 0:
                    self.food_date_list.append(self.food_date_tuple)
                    self.table.insert("", "end", values=self.food_datestr_tuple)
                else:
                    for i in range(len(self.food_date_list)):
                        if int(self.food_date_tuple[1][0:4]) < int(self.food_date_list[i][1][0:4]):
                            self.food_date_list.insert(i, self.food_date_tuple)
                            break
                        elif int(self.food_date_tuple[1][0:4]) > int(self.food_date_list[i][1][0:4]):
                            continue
                        elif int(self.food_date_tuple[1][0:4]) == int(self.food_date_list[i][1][0:4]):
                            if int(self.food_date_tuple[1][4:6]) < int(self.food_date_list[i][1][4:6]):
                                self.food_date_list.insert(i, self.food_date_tuple)
                                break
                            elif int(self.food_date_tuple[1][4:6]) > int(self.food_date_list[i][1][4:6]):
                                continue
                            elif int(self.food_date_tuple[1][4:6]) == int(self.food_date_list[i][1][4:6]):
                                if int(self.food_date_tuple[1][6:]) < int(self.food_date_list[i][1][6:]):
                                    self.food_date_list.insert(i, self.food_date_tuple)
                                    break
                                elif int(self.food_date_tuple[1][6:]) > int(self.food_date_list[i][1][6:]):
                                    pass
                                elif int(self.food_date_tuple[1][6:]) == int(self.food_date_list[i][1][6:]):
                                    self.food_date_list.insert(i + 1, self.food_date_tuple)
                                    break
                    try:
                        self.table.insert("", self.food_date_list.index(self.food_date_tuple), values=self.food_datestr_tuple)
                    except:
                        self.food_date_list.append(self.food_date_tuple)
                        self.table.insert("", "end", values=self.food_datestr_tuple)
                # 寫入RECORD.txt儲存
                path = "./RECORD.txt"  # 路徑可再修改
                with open(path, "w", encoding="utf-8") as file:
                    for data in self.food_date_list:
                        file.write(data[0])
                        file.write(",")
                        file.write(data[1])
                        file.write(",")
                        file.write(data[2] + "\n")
                    
                self.FoodName.delete("0", "end")
                self.BestBefore.delete("0", "end")

    def window(self):
        self.FoodNameLabel = tk.Label(self, text="食物名稱")
        self.FoodNameLabel.grid(column=0, row=0, pady=10)
        self.FoodName = tk.Entry(self, width=15)
        self.FoodName.grid(column=1, row=0, padx=5, pady=10)
        self.BestBeforeLabel = tk.Label(self, text="保存期限")
        self.BestBeforeLabel.grid(column=0, row=1, pady=10)
        self.DateNoteLabel = tk.Label(self, text="(YYYYMMDD)")
        self.DateNoteLabel.grid(column=2, row=1)
        self.BestBefore = tk.Entry(self,width=15)
        self.BestBefore.grid(column=1, row=1, padx=5, pady=10)

        self.Remind_prefix = tk.Label(self, text="我想要在")
        self.Remind_prefix.grid(column=0, row=2, pady=10)
        self.Remind = tk.Entry(self, width=5)
        self.Remind.insert(0, 3)  # 在第0個字元位置插入數字3(預設為3)
        self.Remind.grid(column=1, row=2, pady=10)
        self.Remind_suffix = tk.Label(self, text="天前提醒")
        self.Remind_suffix.grid(column=2, row=2, pady=10)

        # 清單
        self.table = ttk.Treeview(self, show="headings")
        self.table["column"] = ("食物名稱", "保存期限")
        self.table.column("食物名稱", width=150)
        self.table.column("保存期限", width=150)
        self.table.heading("食物名稱", text="食物名稱")
        self.table.heading("保存期限", text="保存期限")
        self.table.grid(column=3, row=0, columnspan=3, rowspan=3)

        self.submit = tk.Button(self, text="送出", command=self.add_event)
        self.submit.grid(column=1, row=3, pady=10)
        
        # 讀入RECORD.txt的資料
        try:        
            path = "./RECORD.txt"  # 路徑可再修改
            with open(path, "r", encoding="utf-8") as file:
                for data in file.readlines():
                    self.food_date = data.strip().split(",")
                    self.food_date_list.append(tuple(self.food_date))
                    self.food_date[1] = self.food_date[1][0:4] + "/" + self.food_date[1][4:6] + "/" + self.food_date[1][6:8]
                    self.table.insert("", "end", values=self.food_date)
        except:
            path = "./RECORD.txt"

# 記錄區
food = FoodReserve()
food.master.title("Food Record")
food.mainloop()