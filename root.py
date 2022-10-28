
import tkinter as tk
import tkinter.ttk as ttk
     
root = tk.Tk()
root.title('my window')
root.geometry('300x200')

choose_month = ttk.Combobox(root,
                            values=["1月", "2月", "3月", "4月", "5月", "6月",\
                                    "7月", "8月", "9月", "10月", "11月", "12月"],
                            width=5
                            )
choose_month.grid(column=0, row=0)

def action():
    print(choose_month.current())

submit = tk.Button(root, text="送出", width=5, command=action)
submit.grid(column=1, row=0)


root.mainloop()