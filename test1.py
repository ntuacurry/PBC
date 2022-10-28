def now_cd():
    global year, month, CALENDAR, frame2
    frame2 = tk.Frame(app)

    month_label = tk.Label(frame2, 
                            text=str(month.current() + 1) + "月", 
                            font=("微軟正黑體", 16),
                            width=10)
    month_label.grid(column=3, row=0)
    weekday_lst = ["日", "一", "二", "三", "四", "五", "六"]
    for i in range(7):
        weekday = tk.Label(frame2, 
                            text=weekday_lst[i], 
                            font=("微軟正黑體", 10),
                            width=10)
        weekday.grid(column=i, row=1)

    year_selected = year.current() + 2021
    month_selected = month.current() + 1

    CD = CALENDAR(year_selected, month_selected)
    for i in range(7):
        for j in range(len(CD)):
            name = ("day" + str(CD[j][i]))
            name = tk.Label(frame2, 
                                text=CD[j][i], 
                                font=("Arial", 10),
                                width=10, 
                                )
            name.grid(column=i, row=j + 2)
            # name.bind("<Button-1>", ifclick)
    frame2.grid(column=0, row=1)

def reset():
    frame2.destroy()

# def ifclick(event):
    # return print(day23.cget("text"))

import tkinter as tk
from tkinter import ttk
import time
from test import *

app = tk.Tk()
app.title("selector")

now = time.localtime()

# frame1
frame1 = tk.Frame(app)
year = ttk.Combobox(frame1, 
                    values=["2021", "2022"], 
                    font=("微軟正黑體"), 
                    state="readonly", 
                    width=5)
year.current(now.tm_year - 2021)
year.grid(column=0, row=0)
month = ttk.Combobox(frame1, 
                    values=["1", "2", "3", "4", "5", "6", \
                            "7", "8", "9", "10", "11", "12"], 
                    font=("微軟正黑體"), 
                    state="readonly", 
                    width=5)
month.current(now.tm_mon - 1)
month.grid(column=1, row=0)

button = tk.Button(frame1, 
                    text="送出", 
                    font=("微軟正黑體", 10), 
                    width=5, 
                    command=lambda: [reset(), now_cd()])
button.grid(column=2, row=0)

frame1.grid(column=0, row=0)

# frame2
now_cd()

app.mainloop()