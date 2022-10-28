def submitdata():
    if amount.get().isdigit() == True:
        # 寫入Excel
        import xlwings as xw
        workbook = xw.Book("記帳.xlsx")
        sheet = workbook.sheets["記帳"]
        
        info = sheet.used_range.last_cell.row

        sheet.range("A" + str(info + 1)).value = time.strftime("%Y.%m.%d", time.localtime())
        if category.get() == 0:
            sheet.range("B" + str(info + 1)).value = "支出"
            sheet.range("B" + str(info + 1)).api.Font.Color = 0x0000ff
        else:
            sheet.range("B" + str(info + 1)).value = "收入"
            sheet.range("B" + str(info + 1)).api.Font.Color = 0xff0000
        sheet.range("C" + str(info + 1)).value = amount.get()
        sheet.range("D" + str(info + 1)).value = purpose.get()
        workbook.sheets["記帳"].autofit()
        workbook.save()
        # workbook.close()
        amount.delete(0, "end")
    else:
        warning = tkinter.messagebox.showwarning(title = "注意", message = "小提醒：金額請輸入數字！")
        amount.delete(0, "end")



import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import time

app = tk.Tk()
app.title("記帳小幫手")

# 日期
# ttk.Button(app, text = "Calendar").grid(row = 4, column = 0)
# ttk.Button(app, text = "DateEntry").grid(row = 4, column = 1)

# 收入 or 支出
category = tk.IntVar()

pay = tk.Radiobutton(app, text = "支出", variable = category, value = 0)
income = tk.Radiobutton(app, text = "收入",variable = category, value = 1)

pay.grid(row = 0, column = 0)
income.grid(row = 0, column = 1)

# 金額
# 要再加是否為數字的判定式
amount_label = tk.Label(app, text = "金額：")
amount = tk.Entry(app)
amount_label.grid(row = 1, column = 0)
amount.grid(row = 1, column = 1)

# 用途
purpose = ttk.Combobox(app, value = ["--請選擇--", "食物", "飲料", "日常", "交通", "爸爸匯款", "薪水", "發票中獎"], state = "readonly")
purpose_label = tk.Label(app, text = "用途：")
purpose_label.grid(row = 2, column = 0)
purpose.current(0)
purpose.grid(row = 2, column = 1)

submit = tk.Button(app, text = "送出", command = submitdata)  # command用來呼叫函式
submit.grid(row = 3, column = 1)
app.mainloop()