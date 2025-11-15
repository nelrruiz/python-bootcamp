import tkinter

root = tkinter.Tk()


# TODO: Add label for instructions
root.title("Password Checker")
root.geometry("250x100") #widthxlength


label = tkinter.Label(root, text="Enter your password:") 
label.pack() 

# TODO: Add entry for instructions
# TODO: Add StringVar for instruction
entry = tkinter.Entry(root, show="*")
entry.pack()

# TODO: Add label using StringVar

label_var = tkinter.StringVar(root, value="Enter your password and press Enter.")
label = tkinter.Label(root, textvariable=label_var)
label.pack()

def check_password(event=None):
    correct_password = "pass"

    # TODO: Check if entry.get() has correct value
    if correct_password == entry.get():
        label_var.set("Password correct! Access granted.")
    else:
        label_var.set("Incorrect password. Try again.")
        

# TODO: Add button that uses check_password
button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()
root.bind("<Return>", check_password)
root.mainloop()
