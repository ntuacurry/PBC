def ifclick():
    CLASS = class_select.get()
    MON = month_select.current()
    if CLASS != "-請選擇-" and MON != 0:
        return print(CLASS, MON)
    else:
        return print("輸入錯誤")
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("教室借用系統")
app.geometry("900x600")

frame_top = tk.Frame(app)
frame_top.pack(side="top")
frame_bottom = tk.Frame(app)
frame_bottom.pack(side="bottom")

classLabel = tk.Label(frame_top, 
                    text="教室：", 
                    font=("微軟正黑體"), 
                    width=5)
classLabel.grid(column=0, row=0)

class_select = ttk.Combobox(frame_top, 
                            values=["-請選擇-", "101", "102", "103"], 
                            font=("微軟正黑體"), 
                            width=7, 
                            state="readonly"
                            )
class_select.current(0)
class_select.grid(column=1, row=0)

dateLabel = tk.Label(frame_top, 
                    text="日期：", 
                    font=("微軟正黑體"), 
                    width=5)
dateLabel.grid(column=2, row=0)

month_select = ttk.Combobox(frame_top, 
                            values=["-請選擇-", "1月", "2月", "3月", 
                                    "4月", "5月", "6月", "7月", "8月", 
                                    "9月", "10月", "11月", "12月"], 
                            font=("微軟正黑體"), 
                            width=7, 
                            state="readonly"
                            )
month_select.current(0)
month_select.grid(column=3, row=0)

search = tk.Button(frame_top, 
                    text="查詢", 
                    font=("微軟正黑體", 10), 
                    width=5, 
                    command=ifclick  # 這裡放呼叫預約狀況Frame的函式 
                    )
search.grid(column=4, row=0, padx=7)

app.mainloop()