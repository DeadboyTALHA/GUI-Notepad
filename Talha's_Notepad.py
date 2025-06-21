from tkinter import *
from tkinter import filedialog

fun = Tk()
fun.geometry("600x600")
fun.title("Talha's Notepad")
fun.config(bg = "Aqua")
fun.resizable(False, False)

def save_file():
    open_file = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode = 'r', filetypes = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(INSERT, content)

b1 = Button(fun, width = '20', height = '2', bg = '#fff', text = 'save file', command = save_file)
b1.place(x = 100, y = 5)
b2 = Button(fun, width = '20', height = '2', bg = '#fff', text = 'open file', command = open_file)
b2.place(x = 300, y = 5)

entry = Text(fun, height = '33', width = '72', wrap = WORD)
entry.place(x = 10, y = 60)

fun.mainloop()