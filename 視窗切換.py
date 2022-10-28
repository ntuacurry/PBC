import tkinter as tk
from tkinter import ttk

class basic():
    def __init__(self, master):
        self.root = master
        self.root.title("期末專案測試")
        Record(self.root)

class Record():
    def __init__(self, master):
        self.master = master
        
        self.initface = tk.Frame(self.master)
        self.initface.grid(column=0, row=0)
        # 記錄區
        FoodNameLabel = tk.Label(self.initface, text="食物名稱")
        FoodNameLabel.grid(column=0, row=0, pady=5)
        FoodName = tk.Entry(self.initface, width=15)
        FoodName.grid(column=1, row=0, padx=5, pady=5)
        BestBeforeLabel = tk.Label(self.initface, text="保存期限")
        BestBeforeLabel.grid(column=0, row=1, pady=5)
        BestBefore = tk.Entry(self.initface,width=15)
        BestBefore.grid(column=1, row=1, padx=5, pady=5)

        Remind_prefix = tk.Label(self.initface, text="我想要在")
        Remind_prefix.grid(column=0, row=2, pady=5)
        Remind = tk.Entry(self.initface, width=5)
        Remind.insert(0, 3)  # 在第0個字元位置插入數字3(預設為3)
        Remind.grid(column=1, row=2, pady=5)
        Remind_suffix = tk.Label(self.initface, text="天前收到提醒")
        Remind_suffix.grid(column=2, row=2, pady=5)

        submit = tk.Button(self.initface, text="送出", width=10)
        submit.grid(column=1, row=3)
        
        self.button = tk.Frame(self.master)
        self.button.grid(column=0, row=1)
        # 選單(？)
        button = tk.Button(self.button, 
                            text="記錄", 
                            relief="flat", 
                            width=15, 
                            )
        button.grid(column=0, row=5)
        button1 = tk.Button(self.button, 
                            text="食物清單", 
                            relief="flat", 
                            width=15, 
                            command=self.change)
        button1.grid(column=2, row=5)
        
    def change(self):
        self.initface.destroy()
        self.button.destroy()
        FoodList(self.master)

class FoodList():
    def __init__(self, master):
        self.master = master
        self.foodlist = tk.Frame(self.master)
        self.foodlist.grid(column=0, row=0)
        # 清單
        table = ttk.Treeview(self.foodlist, show="headings")
        table["column"] = ("食物名稱", "保存期限")
        table.column("食物名稱", width=150)
        table.column("保存期限", width=150)
        table.heading("食物名稱", text="食物名稱")
        table.heading("保存期限", text="保存期限")
        table.grid(column=0, row=0)
        
        self.button = tk.Frame(self.master)
        self.button.grid(column=0, row=1)
        # 選單(？)
        button = tk.Button(self.button, 
                            text="記錄", 
                            relief="flat", 
                            width=15, 
                            command=self.back)
        button.grid(column=0, row=1)
        button1 = tk.Button(self.button, 
                            text="食物清單", 
                            relief="flat", 
                            width=15, 
                            )
        button1.grid(column=1, row=1)
        
    def back(self):
        self.foodlist.destroy()
        self.button.destroy()
        Record(self.master)

if __name__ == "__main__":
    app = tk.Tk()
    basic(app)
    app.mainloop()