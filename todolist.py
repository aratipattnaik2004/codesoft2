from tkinter import *
from tkinter import messagebox

def entertask():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter a task!")

def deletetask():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showerror("Error", "No task selected!")
ws = Tk()
ws.geometry("400x400")
ws.title("To-Do List App")
ws.config(bg='pink')

frame = Frame(ws)
frame.pack(pady=10)
listbox = Listbox(frame, width=30, height=10)
listbox.pack(side=LEFT)
scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(ws, font=("Helvetica", 16))
entry.pack(pady=20)

add_btn = Button(ws, text="Add Task", command=entertask)
add_btn.pack()

delete_btn = Button(ws, text="Delete Task", command=deletetask)
delete_btn.pack()

ws.mainloop()
