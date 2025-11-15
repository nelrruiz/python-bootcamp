import tkinter

root = tkinter.Tk()
label = tkinter.Label(
    root,
    text="Hello",
    font=("Arial", 14, "bold italic"), #computer-based
    fg="red", #foreground = color of font
    bg="yellow", #backgroun
    width=100,
    height=20,
    padx=10,
    pady=200,
)

label.pack()
root.mainloop()
