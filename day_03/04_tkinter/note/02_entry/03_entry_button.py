import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter any text")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event=None): #so it will work in our 
    given_text = entry.get()
    user_input.set(given_text)

def main():
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        
            save(inventory)
        elif command == "load":
            inventory = load(inventory)
        elif command == "exit":
            running = False
            print("Exiting...")


main()


button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()
root.mainloop()