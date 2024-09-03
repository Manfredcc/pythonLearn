import tkinter as tk


window = tk.Tk()
window.title("Title")
window.geometry("300x150")

textVar = tk.StringVar()
onHit = False

def hitMe():
    global onHit
    if not onHit:
        onHit = True
        textVar.set("U hit me")
    else:
        onHit = not onHit
        textVar.set("")

l = tk.Label(window, textvariable = textVar, bg = 'green', font = ('Arial', 12), 
    width = 15, height = 2)
l.pack()

button = tk.Button(window, text = "hit me", width = 15, height = 2, 
    command = hitMe)
button.pack()

window.mainloop()