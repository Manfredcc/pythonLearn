import tkinter as tk

window = tk.Tk()
window.title("Title")
window.geometry("300x150")

var = tk.StringVar()

label = tk.Label(window, bg = 'yellow', width = 20, text = 'empty')
label.pack()

def print_selection():
    label.config(text = "you have selected " + var.get())

radioButton1 = tk.Radiobutton(window, text = "Option A", 
    variable = var, value = 'A', command = print_selection)
radioButton1.pack()

radioButton2 = tk.Radiobutton(window, text = "Option B", 
    variable = var, value = 'B', command = print_selection)
radioButton2.pack()

radioButton3 = tk.Radiobutton(window, text = "Option C", 
    variable = var, value = 'C', command = print_selection)
radioButton3.pack()

window.mainloop()