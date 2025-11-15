import tkinter

root = tkinter.Tk()

radio_var = tkinter.StringVar(value="Option A") #if "" it will return all radio buttons selected
radio1 = tkinter.Radiobutton(
root, text="Option A", variable=radio_var, value="Option A")
radio1.pack()

radio2 = tkinter.Radiobutton(
root, text="Option B", variable=radio_var, value="Option B")
radio2.pack()

radio3 = tkinter.Radiobutton(
root, text="Option C", variable=radio_var, value="Option C")
radio3.pack()

root.mainloop()