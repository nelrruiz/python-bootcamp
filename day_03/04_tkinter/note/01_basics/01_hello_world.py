import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400") #widthxlength

label = tkinter.Label(root, text="Hello World") #root=anong container or window magaapply, default arguments
label.pack() #confirm to show in the window

next_label = tkinter.Label(root, text="Hello Again")
next_label.pack()

root.mainloop() #to show the application
