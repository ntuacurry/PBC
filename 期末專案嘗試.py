'''
2022/01/03 新增了刪除吃完食品的功能
2022/01/03 提醒天數到時黃底紅字 及 過期浪費食物會有標語
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import urllib.parse
from datetime import date, datetime, time ,timedelta
from sqlalchemy import Column, ForeignKey, Integer, String, Text

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
                today = datetime.combine(date.today(), datetime.min.time())
                self.date_like_today = datetime.strptime(self.date, "%Y%m%d")
                if self.date_like_today < today:
                    self.result = tk.messagebox.showwarning(title="注意", message="這項食品已過期！")
                else:
                    self.datestr = self.date[0:4] + "/" + self.date[4:6] + "/" + self.date[6:8]
                    self.food_date_tuple = (self.food, self.date, self.remind)
                    self.food_datestr_tuple = (self.food, self.datestr, self.remind)

                #  有效期限快到的在上面
                    if len(self.food_date_list) == 0:
                        self.food_date_list.append(self.food_date_tuple)
                        self.table.tag_configure('nearly_expired', background='yellow', foreground='red')
                        if self.remind_color_for_new(self.days_between(self.date)) == 'nearly_expired':
                            self.table.insert("", "end", values=self.food_datestr_tuple, tags = ('nearly_expired',))
                        else:
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
                            self.table.tag_configure('nearly_expired', background='yellow', foreground='red')
                            if self.remind_color_for_new(self.days_between(self.date)) == 'nearly_expired':
                                self.table.insert("", self.food_date_list.index(self.food_date_tuple), values=self.food_datestr_tuple, tags = ('nearly_expired',))
                            elif self.remind_color_for_new(self.days_between(self.date)) == 'not_expired':
                                self.table.insert("", self.food_date_list.index(self.food_date_tuple), values=self.food_datestr_tuple)
                        except:
                            self.table.tag_configure('nearly_expired', background='yellow', foreground='red')
                            self.food_date_list.append(self.food_date_tuple)
                            if self.remind_color_for_new(self.days_between(self.date)) == 'nearly_expired':
                                self.table.insert("", "end", values=self.food_datestr_tuple, tags = ('nearly_expired',))
                            elif self.remind_color_for_new(self.days_between(self.date)) == 'not_expired':
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
                # 判斷新輸入的食物是否接近到期日
    def remind_color_for_new(self, diff_days):
        if diff_days <= int(self.remind):
            return 'nearly_expired'
        else:
            return 'not_expired'
    
    # 判斷舊資料的食物是否接近到期日
    def remind_color_for_old(self, diff_days, before_days):
        if diff_days <= before_days:
            return 'nearly_expired'
        else:
            return 'not_expired'
   
    # 算出到期日期與今天的差距
    def days_between(self, date1):
        self.str1 = ''
        self.diff = 0
        import datetime
        self.str1 = datetime.datetime.strptime(date1, "%Y%m%d")
        today = datetime.datetime.today()
        self.diff = (self.str1 - today).days + 1
        return self.diff
    
    # 刪除吃完的食品
    def remove(self):
        des = self.table.selection()
        for de in des:
            item_text = self.table.item(de,"values")
            self.table.delete(des)
        for i in range(len(self.food_date_list)):
            if self.food_date_list[i][0] == item_text[0]:
                self.food_date_list.pop(i)
                break

        path = "./RECORD.txt"  # 路徑可再修改
        with open(path, "w", encoding="utf-8") as file:
            for data in self.food_date_list:
                file.write(data[0])
                file.write(",")
                file.write(data[1])
                file.write(",")
                file.write(data[2] + "\n")

    # 搜尋功能的刪除函數
    def FoodselectdeleteClick(self):
        self.Foodselect.configure(text = "（請點擊左方食材）")
    
    # 搜尋功能搜尋函數
    def Foodselectsearch(self):
        if self.Foodselect.cget('text') != "（請點擊左方食材）": 
            urL_food = '食材：' + str(self.Foodselect.cget('text'))
            urL_food = urllib.parse.quote(urL_food) # url裡有中文的話，要解碼
            urL='https://icook.tw/search/' + str(urL_food) + '/'
            webbrowser.open(urL)
    def window(self):
        self.FoodNameLabel = tk.Label(self, text="食物名稱")
        self.FoodNameLabel.grid(column=0, row=0, pady=10)
        self.FoodName = tk.Entry(self, width=15)
        self.FoodName.grid(column=1, row=0, padx=5, pady=10)
        self.BestBeforeLabel = tk.Label(self, text="保存期限")
        self.BestBeforeLabel.grid(column=0, row=1, pady=10)
        self.DateNoteLabel = tk.Label(self, text="(YYYYMMDD)")
        self.DateNoteLabel.grid(column=2, row=1)
        self.BestBefore = tk.Entry(self, width=15)
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
        
        self.remove = tk.Button(self, text='刪除食品', command = self.remove)
        self.remove.grid(column=5, row=3, pady=10)
        
        # 搜尋功能
        self.RecipeLabel = tk.Label(self, text="食譜搜尋區")
        self.RecipeLabel.grid(column=6, row=0, columnspan=2)
        self.Foodselect = tk.Label(self, text="（請點擊左方食材）")
        self.Foodselect.grid(column=6, row=1, columnspan=2)
        self.Foodselectdelete = tk.Button(self, text="刪除", command = self.FoodselectdeleteClick)
        self.Foodselectdelete.grid(column=6, row=2)
        self.Foodselectsearch = tk.Button(self, text="搜尋", command = self.Foodselectsearch)
        self.Foodselectsearch.grid(column=7, row=2)
        
        def treeviewClick(event):#單擊
            item_text =  self.table.item(self.table.selection(),"values")
            if self.Foodselect.cget('text') == "（請點擊左方食材）":
                self.Foodselect.configure(text = item_text[0])
            elif item_text[0] not in self.Foodselect.cget('text'):
                self.Foodselect.configure(text = self.Foodselect.cget('text') + ',' + item_text[0])

        self.table.bind('<ButtonRelease-1>', treeviewClick) #  繫結單擊離開事件
        # 刪除過期食品
        today = datetime.combine(date.today(), datetime.min.time())
        path = "./RECORD.txt"
        self.eatable_food_list = []
        try:
            with open(path, "r", encoding="utf-8") as file:
                for data in file.readlines():
                    self.food_date = data.strip().split(",")
                    self.food_date_list.append(tuple(self.food_date))
        except:
            path = "./RECORD.txt"
        with open(path, "w", encoding="utf-8") as file:
            expired_number = 0
            for i in range(len(self.food_date_list)):
                self.food_date = self.food_date_list[i][1]
                expired_date = datetime.strptime(self.food_date, "%Y%m%d")
                if expired_date >= today:
                    self.eatable_food_list.append(self.food_date_list[i])
                elif expired_date < today:
                    expired_number += 1
            if expired_number != 0:
                self.Warning_former = tk.Label(self, text="⚠️您今日浪費了" + str(expired_number) + '樣食物，請懺悔🥴')
                self.Warning_former.grid(column=3, row=3, pady=0)
            for line in self.eatable_food_list:
                file.write(line[0])
                file.write(",")
                file.write(line[1])
                file.write(",")
                file.write(line[2] + "\n")
        self.food_date_list = []
        # 讀入RECORD.txt的資料
        try:
            path = "./RECORD.txt"  # 路徑可再修改
            with open(path, "r", encoding="utf-8") as file:
                for data in file.readlines():
                    self.food_date = data.strip().split(",")
                    self.only_date = self.food_date[1]
                    self.food_date_list.append(tuple(self.food_date))
                    self.food_date[1] = self.food_date[1][0:4] + "/" + self.food_date[1][4:6] + "/" + self.food_date[1][6:8]
                    self.table.tag_configure('nearly_expired', background='yellow', foreground='red')
                    if self.remind_color_for_old(self.days_between(self.only_date), int(self.food_date_list[-1][-1])) == 'nearly_expired':
                        self.table.insert("", "end", values=self.food_date, tags = ('nearly_expired',))
                    else:
                        self.table.insert("", "end", values=self.food_date)
        except:
            path = "./RECORD.txt"

        #self.Warning_latter = tk.Label(self, text="樣食物")
        #self.Warning_latter.grid(column=3, row=1, padx=5, pady=10)

# 記錄區
food = FoodReserve()
food.master.title("Food Record")
food.mainloop()