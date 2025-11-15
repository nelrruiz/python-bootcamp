import tkinter

root = tkinter.Tk()

entry_var = tkinter.StringVar(root, value="Enter something")
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()

user_input = tkinter.StringVar(root, value="")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
    given_text = entry_var.get()
    user_input.set(given_text)

root.bind("<Return>", show_input)
# root.bind("<space>", show_input)
root.mainloop()