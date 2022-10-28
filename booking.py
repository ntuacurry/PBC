# from calendar import *
import tkinter as tk
from tkinter import ttk
# import bk_calendar
import time

bk = tk.Tk()
bk.title("預約")  # 標題設為預約
bk.state("zoomed")  # 將視窗最大化

choose_month = ttk.Combobox(bk, values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"])
choose_month.grid(column=0, row=1)
now_sec = time.time()
now = time.localtime(now_sec)
choose_month.current(now.tm_mon - 1)

frame = tk.Frame(bk, width=100, height=100)
frame.grid()




bk.mainloop()