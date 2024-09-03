import tkinter as tk

window = tk.Tk()
window.title("ListBox")
window.geometry("200x300")

labelVal = tk.StringVar()
label = tk.Label(window, bg = 'yellow', width = 10, textvariable = labelVal)
label.pack()

def print_selection():
    val = lb.get(lb.curselection())
    labelVal.set(val)

button = tk.Button(window, text = "print selection", width = 20, 
    height = 2, command = print_selection)
button.pack()

listVar = tk.StringVar()
listVar.set((11, 12, 13, 14))
lb = tk.Listbox(window, listvariable = listVar)
list_item = [1, 2, 3, 4]
for item in list_item:
    lb.insert('end', item)

lb.insert(1, "first")
lb.insert(2, "second")
# lb.delete(2)
lb.pack()

window.mainloop()