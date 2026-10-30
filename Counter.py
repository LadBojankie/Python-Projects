import tkinter as tk

root = tk.Tk()
root.title("Counter")
root.geometry("230x226")
root.resizable(False, False)

x = 0

def add():
    global x
    x = x + 1
    Counter.config(text=x)

def subtract():
    global x
    x = x - 1
    Counter.config(text=x)

Title = tk.Entry(root, justify='center', width=36)
Add = tk.Button(root, text="+", command=add, width=20, font=("Arial", 22))
Subtract = tk.Button(root, text="-", command=subtract, width=20, font=("Arial", 22))
Counter = tk.Label(root, text="0", font=("Arial", 50))

Title.pack(pady=5)
Add.pack()
Counter.pack()
Subtract.pack()

root.mainloop()