import tkinter
import json

root = tkinter.Tk()

# TODO: Create StringVar for name
# TODO: Create StringVar for name

# TODO: Add label for instructions
root.title("Password Checker")
# root.geometry("300x500") #widthxlength

# varlist = ["Name", "Age", "Preferred Theme", "Subscribe", "Rate us"]
# TODO: Add label using StringVar
name_framer = tkinter.Frame(root)
name_framer.pack()
label_name = tkinter.StringVar(name_framer, value="Name")
label1 = tkinter.Label(name_framer, textvariable=label_name)
label1.pack(side="left")
entry_name = tkinter.Entry(name_framer)
entry_name.pack(side="right")


age_frame = tkinter.Frame(root)
age_frame.pack()
label_age = tkinter.StringVar(age_frame, value="Age")
label2 = tkinter.Label(age_frame, textvariable=label_age)
label2.pack(side="left")
entry_age = tkinter.Entry(age_frame)
entry_age.pack(side="right")

# # TODO: Create StringVar for theme
# # TODO: Create StringVar for theme

theme_frame = tkinter.Frame(root)
theme_frame.pack()
label_theme = tkinter.StringVar(theme_frame, value="Preferred Theme")
label3 = tkinter.Label(theme_frame, textvariable=label_age)
label3.pack(side="left", padx= "10")

radio_var = tkinter.StringVar(value="Light") #if "" it will return all radio buttons selected
radio1 = tkinter.Radiobutton(
theme_frame, text="Light", variable=radio_var, value="Light")
radio1.pack(side="left")

radio2 = tkinter.Radiobutton(
theme_frame, text="Dark", variable=radio_var, value="Dark")
radio2.pack(side="right")

# # TODO: Create BooleanVar for subscribe
# # TODO: Create BooleanVar for subscribe

subscribe_frame = tkinter.Frame(root)
subscribe_frame.pack()
check_value = tkinter.BooleanVar() # default FALSE
checkbox = tkinter.Checkbutton(
    subscribe_frame,
    text="Subscribe to newsletter",
    variable=check_value
)
checkbox.pack()

# # TODO: Create IntVar for rating
# # TODO: Create IntVar for rating
rating_frame = tkinter.Frame(root)
rating_frame.pack()
label_rating = tkinter.StringVar(rating_frame, value="Rate us")
label5 = tkinter.Label(rating_frame, textvariable=label_rating)
label5.pack(side="left", padx= "10")
slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    rating_frame,
    from_=1,
    to=5,
    orient="horizontal",
    variable=slider_value
)
slider.pack()


# # TODO: Create function for saving values to JSON
# # TODO: Create button for submit + save

# def save_data(event=None):
#     data = {
#         "Name": entry_name.get(),
#         "Age": entry_age.get(),
#         "Theme": radio_var.get(),
#         "Subscribe":check_value.get(),
#         "Rating": slider_value.get()
#     }
    


# submit_button = tkinter.Button(root, text="Submit", save_data)
# submit_button.pack()

root.mainloop()
