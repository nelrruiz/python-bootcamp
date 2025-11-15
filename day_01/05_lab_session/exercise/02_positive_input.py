# TODO: Ask the user for an input that should be a number
number = input("Enter number: ")

# TODO: Then try to convert this into an integer using the following:
# number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case
# line_break = "="*100
# print(line_break)
# try:
#     print(number_converted)
# except ValueError:
#     print("Invalid input")
# print(line_break)

# The user could give a negative number
# TODO: Handle this case


# Challenge: TODO: Give the user infinite times to retry




try:
    number_converted = int(number)
    
    if number_converted < 0:
        raise ValueError()
    else:
        print(number_converted)
except ValueError:
    print("Invalid input or Negative number")
