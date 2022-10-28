import tkinter as tk

def command(event):
    print(label1.cget("text"))

root = tk.Tk()

label1 = tk.Label(text="Click me!", width=50, height=10, master=root)
label1.pack()
label1.bind("<Button-1>", command)

label2 = tk.Label(text="Click!", width=50, height=10, master=root)
label2.pack()
label2.bind("<Button-1>", command)

root.mainloop()