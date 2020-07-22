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

root.mainloop()