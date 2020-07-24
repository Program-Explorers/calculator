import tkinter as tk

expression = ''


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    print(expression)


def clear_exp():
    global expression
    expression = ''
    equation.set('0')


root = tk.Tk()

height = 300
width = 260

font_size = 40

root.title('Calculator')

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='#2b2929')
frame.place(relheight=1, relwidth=1)

equation = tk.StringVar()

output = tk.Label(frame, textvariable=equation, bg='#2b2929', fg='#ffffff', font="Calibri " + str(font_size))
output.grid(columnspan=4, sticky='w')
equation.set('0')

clear = tk.Button(frame, text='Clear', height=1, width=7, font='Calibri 25', command=lambda: clear_exp())
clear.grid(row=1, column=0, columnspan=2, padx=1, sticky='w', ipadx=7, pady=1)

percent = tk.Button(frame, text='%', height=1, width=3, font='Calibri 25')
percent.grid(row=1, column=2, ipadx=6, padx=1, sticky='w', pady=1)

divide = tk.Button(frame, text='÷', height=1, width=3, font='Calibri 25')
divide.grid(row=1, column=3, padx=1, sticky='w', pady=1, ipadx=6)

num_7 = tk.Button(frame, text='7', height=2, width=4, font='Calibri 23', command=lambda: press(7))
num_7.grid(row=2, column=0, sticky='w', padx=1, pady=1)

num_8 = tk.Button(frame, text='8', height=2, width=4, font='Calibri 23',  command=lambda: press(8))
num_8.grid(row=2, column=1, sticky='w', padx=1, pady=1)

num_9 = tk.Button(frame, text='9', height=2, width=4, font='Calibri 23', command=lambda: press(9))
num_9.grid(row=2, column=2, padx=1, pady=1, sticky='w')

multiply = tk.Button(frame, text='×', height=2, width=4, font='Calibri 23')
multiply.grid(row=2, column=3, padx=1, pady=1, sticky='w')

num_4 = tk.Button(frame, text='4', height=2, width=4, font='Calibri 23', command=lambda: press(4))
num_4.grid(row=3, column=0, sticky='w', pady=1, padx=1)

num_5 = tk.Button(frame, text='5', height=2, width=4, font='Calibri 23', command=lambda: press(5))
num_5.grid(row=3, column=1, sticky='w', padx=1, pady=1)

num_6 = tk.Button(frame, text='6', height=2, width=4, font='Calibri 23', command=lambda: press(6))
num_6.grid(row=3, column=2)

minus = tk.Button(frame, text='-', height=2, width=4, font='Calibri 23')
minus.grid(row=3, column=3, sticky='w', padx=1)

num_1 = tk.Button(frame, text='1', height=2, width=4, font='Calibri 23', command=lambda: press(1))
num_1.grid(row=4, column=0, sticky='w', pady=1, padx=1)

num_2 = tk.Button(frame, text='2', height=2, width=4, font='Calibri 23', command=lambda: press(2))
num_2.grid(row=4, column=1, sticky='w', padx=1, pady=1)

num_3 = tk.Button(frame, text='3', height=2, width=4, font='Calibri 23', command=lambda: press(3))
num_3.grid(row=4, column=2, sticky='w', padx=1, pady=1)

plus = tk.Button(frame, text='+', height=2, width=4, font='Calibri 23')
plus.grid(row=4, column=3, padx=1, pady=1, sticky='w')

num_0 = tk.Button(frame, text='0', height=1, width=7, font='Calibri 25', command=lambda: press(0))
num_0.grid(row=5, column=0, columnspan=2, ipadx=7, sticky='w', pady=1, padx=1)

decimal = tk.Button(frame, text='.', height=1, width=3, font='Calibri 25')
decimal.grid(row=5, column=2, sticky='w', padx=1, pady=1, ipadx=6)

equals = tk.Button(frame, text='=', height=1, width=3, font='Calibri 25')
equals.grid(row=5, column=3, padx=1, pady=1, ipadx=6)

root.mainloop()