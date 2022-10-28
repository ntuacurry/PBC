'''
目標：即時刷新的圖表(呈現目前的損益)
顯示庫存、成交均價、損益平衡、目前損益的區域
顯示五檔圖
顯示目前股價走勢
加減碼的區域
重複執行函式的方法(或許從當下時間和庫存來判斷？)
即時股價可能會是"-"
'''

import tkinter as tk
# from tkintertable import TableCanvas, TableModel
import time
import TWS

def button_event():
    if Entry_Price.get() != "" and Entry_Amount.get() != "":
        Price = float(Entry_Price.get())
        Amount = float(Entry_Amount.get())
    Label_Cost["text"] = StrategyValue.get()
    # print(TWS.BreakEven(StrategyValue.get(), Price, Amount))
    print(TWS.BreakEven_Now(StrategyValue.get(),Entry_Target.get(), Price, Amount))

app = tk.Tk()
app.title("進出場判斷")
# app.geometry('380x400')
app.resizable(False, False)

Input = tk.Frame(app)
Input.pack(side="left")

# 策略選擇
Label_Strategy = tk.Label(Input, text="策略")
Label_Strategy.grid(column=0, row=0, padx=20)
StrategyValue = tk.IntVar() 
Strategy_Long = tk.Radiobutton(Input, text="Long", variable=StrategyValue, value=1) 
Strategy_Short = tk.Radiobutton(Input, text="Short", variable=StrategyValue, value=2)
Strategy_Long.grid(column=1, row=0, sticky="W")
Strategy_Short.grid(column=2, row=0, sticky="W")

#標的
Label_Target = tk.Label(Input, text="股票代碼")
Label_Target.grid(column=0, row=1, padx=20)
Entry_Target = tk.Entry(Input, width=10)
Entry_Target.grid(column=1, row=1)

#買進/賣出價格；張數
Label_Price = tk.Label(Input, text="價格")
Label_Price.grid(column=0, row=2, padx=20)
Entry_Price = tk.Entry(Input, width=5)
Entry_Price.grid(column=1, row=2, sticky="W")

Label_Amount = tk.Label(Input, text="數量")
Label_Amount.grid(column=0, row=3, padx=20)
Entry_Amount = tk.Entry(Input, width=5)
Entry_Amount.grid(column=1, row=3, sticky="W")

# 送出按鈕
Submit = tk.Button(Input, text="計算", command=button_event)
Submit.grid(column=1, row=4)

Label_Cost = tk.Label(Input, text="成本")
Label_Cost.grid(column=1, row=5, padx=20)

# 五檔圖子視窗
# BidAsk = tk.Frame(app)
# BidAsk.pack(side="right")

# Table_BidAsk = tk.ttk.Treeview(BidAsk)
# Table_BidAsk["show"] = "headings"
# Table_BidAsk["column"] = ("委買量", "委買價", "委賣價", "委賣量")
# for column in Table_BidAsk["column"]:
    # Table_BidAsk.column(column)
    # Table_BidAsk.heading(column, text=column)

# Table_BidAsk.pack()

app.mainloop()