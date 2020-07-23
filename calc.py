import tkinter as tk
import sys

root = tk.Tk()


if sys.platform.startswith('darwin'):
    height = 297
    width = 250
if sys.platform.startswith('win32'):
    height = 528
    width = 300
font_type = 'Calibri 25'

root.title('Calculator')

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

in_output = '0'

frame = tk.Frame(root, bg='#2b2929')
frame.place(relheight=1, relwidth=1)

out_var = tk.StringVar()
output = tk.Label(frame, textvariable=out_var, bg='#2b2929', fg='#ffffff', font="Calibri 40")
output.grid()
out_var.set('0')

clear = tk.Button(frame, text='Clear', height=1, width=7, font='Calibri 25')
clear.grid(row=1, column=0, columnspan=2, sticky='w', ipadx=10)

percent = tk.Button(frame, text='%', height=1, width=3, font='Calibri 25')
percent.grid(row=1, column=2, ipadx=6, padx=1, sticky='w')

divide = tk.Button(frame, text='÷', height=1, width=4, font='Calibri 25')
divide.grid(row=1, column=3, padx=1, sticky='w')

num_7 = tk.Button(frame, text='7', height=2, width=4, font='Calibri 23')
num_7.grid(row=2, column=0, sticky='w', padx=0, pady=1)

num_8 = tk.Button(frame, text='8', height=2, width=4, font='Calibri 23')
num_8.grid(row=2, column=1, sticky='w', padx=1, pady=1)

num_9 = tk.Button(frame, text='9', height=2, width=4, font='Calibri 23')
num_9.grid(row=2, column=2, padx=1, pady=1, sticky='w')

multiply = tk.Button(frame, text='×',  height=2, width=4, font='Calibri 23')
multiply.grid(row=2,column=3,padx=1, pady=1, sticky='w')

num_4 = tk.Button(frame, text='4', height=2, width=4, font='Calibri 23')
num_4.grid(row=3, column=0, sticky='w', pady=1)

num_5 = tk.Button(frame, text='5', height=2, width=4, font='Calibri 23')
num_5.grid(row=3, column=1, sticky='w', padx=1, pady=1)

num_6 = tk.Button(frame, text='6', height=2, width=4, font='Calibri 23')
num_6.grid(row=3, column=2)

minus = tk.Button(frame, text='-')
minus.grid(row=3, column=3)

num_1 = tk.Button(frame, text='1', height=2, width=4, font='Calibri 23')
num_1.grid(row=4, column=0, sticky='w', pady=1)

num_2 = tk.Button(frame, text='2', height=2, width=4, font='Calibri 23')
num_2.grid(row=4, column=1, sticky='w', padx=1, pady=1)

num_3 = tk.Button(frame, text='3', height=2, width=4, font='Calibri 23')
num_3.grid(row=4, column=2, sticky='w', padx=1, pady=1)

plus = tk.Button(frame, text='+')
plus.grid(row=4, column=3)

num_0 = tk.Button(frame, text='0', height=1, width=8, font='Calibri 25')
num_0.grid(row=5, column=0, columnspan=2, ipadx=2, sticky='w', pady=1)

decimal = tk.Button(frame, text='.')
decimal.grid(row=5, column=2)

equals = tk.Button(frame, text='=')
equals.grid(row=5, column=3)

root.mainloop()

