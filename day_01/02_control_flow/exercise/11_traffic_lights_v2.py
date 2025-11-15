# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"
# Everything else   -> print "Malfunction"


################################# answer

# TODO: Print the following depending on the color input
if color_input == "green": # "green"   -> print "Go"
    print("Go")
elif color_input =="yellow": # "yellow"  -> print "Wait..."
    print("Wait...")
elif color_input == "red": # "red"     -> print "Stop"
    print("Stop")
else:
    print("Malfunction")


########################### alternative answer

match color_input:
    case "green":
        print("Go")
    case "yellow":
        print("Wait...")
    case "red":
        print("Stop")
    case _:
        print("Malfunction")