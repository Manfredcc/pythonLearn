import tkinter as tk


window = tk.Tk()
window.title("Title")
window.geometry("300x200")

entry = tk.Entry(window, show = None)
entry.pack()

def insert_point():
    var = entry.get()
    text.insert('insert', var)

def insert_end():
    var = entry.get()
    text.insert('end', var)

button1 = tk.Button(window, text = "point", width = 15, height = 2, 
    command = insert_point)
button1.pack()

button2 = tk.Button(window, text = "end", width = 15, height = 2, 
    command = insert_end)
button2.pack()

text = tk.Text(window, height = 2)
text.pack()

window.mainloop()