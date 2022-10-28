import tkinter as tk
from tkinter import ttk
from date import *  # 引入自建的日期函數

app = tk.Tk()
app.title("儀器借用系統")  # 標題設為儀器借用系統
# app.state("zoomed")  # 將視窗最大化

# 創建表格
sheet = ttk.Treeview(app) #
sheet["column"] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
sheet['show'] = 'headings'  # 刪除空欄(第一欄)
sheet.pack()

sheet.column("Sunday", width=150)
sheet.column("Monday", width=150)
sheet.column("Tuesday", width=150)
sheet.column("Wednesday", width=150)
sheet.column("Thursday", width=150)
sheet.column("Friday", width=150)
sheet.column("Saturday", width=150)

sheet.heading("Sunday", text="Sunday")
sheet.heading("Monday", text="Monday")
sheet.heading("Tuesday", text="Tuesday")
sheet.heading("Wednesday", text="Wednesday")
sheet.heading("Thursday", text="Thursday")
sheet.heading("Friday", text="Friday")
sheet.heading("Saturday", text="Saturday")

date(sheet)  # 產生日期


mybutton = tk.Button(app, text='button')
mybutton.pack()

app.mainloop()



