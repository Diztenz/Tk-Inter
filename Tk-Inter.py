from tkinter import *

ws = Tk()

nameLb = Label(ws, text="Enter First Value").pack()
nameTf = Entry(ws).pack()
name2Lb = Label(ws, text="Enter Second Value").pack()
name2Tf = Entry(ws).pack()

def submit():
    name = nameTf.get()
    name2 = name2Tf.get()
    return Label(ws, text=f'name + name2').pack()

submitBtn = Button(ws, text="submit", command=submit)
submitBtn.pack()

ws.mainloop()