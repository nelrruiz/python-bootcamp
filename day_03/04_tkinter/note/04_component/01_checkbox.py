import tkinter

root = tkinter.Tk()

check_value = tkinter.BooleanVar() # default FALSE
checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value
)
checkbox.pack()

root.mainloop()
