import tkinter as tk

root = tk.Tk()

height = 300
width = 225

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

clear = tk.Button(frame, text='Clear')
clear.grid(row=1, column=0, columnspan=2)

percent = tk.Button(frame, text='%')
percent.grid(row=1, column=2)

divide = tk.Button(frame, text='÷')
divide.grid(row=1, column=3)

num_7 = tk.Button(frame, text='7')
num_7.grid(row=2,column=0)

num_8 = tk.Button(frame, text='8')
num_8.grid(row=2,column=1)

num_9 = tk.Button(frame, text='9')
num_9.grid(row=2,column=2)

multiply = tk.Button(frame, text='×')
multiply.grid(row=2,column=3)

num_4 = tk.Button(frame, text='4')
num_4.grid(row=3,column=0)

num_5 = tk.Button(frame, text='5')
num_5.grid(row=3, column=1)

num_6 = tk.Button(frame, text='6')
num_6.grid(row=3, column=2)

minus = tk.Button(frame, text='-')
minus.grid(row=3, column=3)

root.mainloop()