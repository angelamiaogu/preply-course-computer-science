import tkinter as tk

angela = tk.Tk()
angela.geometry('400x400')

ev = tk.StringVar()
entry1 = tk.Entry(angela, textvariable=ev, font=('Arial', 12), width=20)
entry1.grid(row=0, columnspan=50)

button_color = '#ffc0cb'  # Pink color

button7 = tk.Button(angela, bg=button_color, text='7', command=lambda i='7': general("7"))
button7.grid(row=1, column=0, padx=10, pady=10)

button8 = tk.Button(angela, bg=button_color, text='8', command=lambda i='8': general("8"))
button8.grid(row=1, column=1, padx=10, pady=10)

button9 = tk.Button(angela, bg=button_color, text='9', command=lambda i='9': general("9"))
button9.grid(row=1, column=2, padx=10, pady=10)

button10 = tk.Button(angela, bg=button_color, text='/', command=lambda i='/': general("/"))
button10.grid(row=1, column=3, padx=10, pady=10)

button4 = tk.Button(angela, bg=button_color, text='4', command=lambda i='4': general("4"))
button4.grid(row=2, column=0, padx=10, pady=10)

button5 = tk.Button(angela, bg=button_color, text='5', command=lambda i='5': general("5"))
button5.grid(row=2, column=1, padx=10, pady=10)

button6 = tk.Button(angela, bg=button_color, text='6', command=lambda i='6': general("6"))
button6.grid(row=2, column=2, padx=10, pady=10)

button11 = tk.Button(angela, bg=button_color, text='*', command=lambda i='*': general("*"))
button11.grid(row=2, column=3, padx=10, pady=10)

def one():
    x = ev.get()
    y = x + '1'
    ev.set(y)

button1 = tk.Button(angela, bg=button_color, text='1', command=one)
button1.grid(row=3, column=0, padx=10, pady=10)

def general(bb):
    x = ev.get()
    y = x + bb
    ev.set(y)

button2 = tk.Button(angela, bg=button_color, text='2', command=lambda i='2': general("2"))
button2.grid(row=3, column=1, padx=10, pady=10)

button3 = tk.Button(angela, bg=button_color, text='3', command=lambda i='3': general("3"))
button3.grid(row=3, column=2, padx=10, pady=10)

button12 = tk.Button(angela, bg=button_color, text='-', command=lambda i='-': general("-"))
button12.grid(row=3, column=3, padx=10, pady=10)

def ac():
    ev.set('')

button13 = tk.Button(angela, bg=button_color, text='ac', command=ac)
button13.grid(row=4, column=0, padx=10, pady=10)

button0 = tk.Button(angela, bg=button_color, text='0', command=lambda i='0': general("0"))
button0.grid(row=4, column=1, padx=10, pady=10)

def angela_calculate():
    x = entry1.get()
    y = eval(x)
    label1.configure(text=f'Result: {y}')

button14 = tk.Button(angela, bg=button_color, text='=', command=angela_calculate)
button14.grid(row=4, column=2, padx=10, pady=10)

def plus():
    x = ev.get()
    y = x + '+'
    ev.set(y)

button15 = tk.Button(angela, bg=button_color, text='+', command=plus)
button15.grid(row=4, column=3, padx=10, pady=10)

label1 = tk.Label(angela, text="Result: ", font=('Arial', 15))
label1.grid(row=5, columnspan=50)

angela.mainloop()
