import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

#need a signal to do a certain action
def show_input(event):
    print("You pressed enter!") #showing in console

root.bind("<Return>", show_input) #root.bind(key (any key in the keyboard; <>), function_name (action))
root.mainloop()