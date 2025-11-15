# message = """
# Loops within loops again
# A silent function returns
# The logic is clear
# """

# TODO: Show message using a label
import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("1200x400") #widthxlength

message = """
Loops within loops again,
A silent function returns,
The logic is clear.
""" 

label = tkinter.Label(root, text=message) #root=anong container or window magaapply, default arguments
label.pack() #confirm to show in the window

root.mainloop()