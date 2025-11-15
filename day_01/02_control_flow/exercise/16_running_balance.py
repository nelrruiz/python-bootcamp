total = 0
running = True
# while running:
#     command = input("Provide command: ")

#     if command == "add":
#         # TODO: Ask for number
#         # TODO: Add that number to the total
#         # TODO: Print the current total
#         pass
#     if command == "sub":
#         # TODO: Ask for number
#         # TODO: Subtract that number to the total
#         # TODO: Print the current total
#         pass
#     elif command == "exit":
#         running = False

############################################### answer

while running:
    command = input("Provide command: ")

    if command == "add":
        given_number = int(input("Give a number:"))
        total = given_number + total
        print(total)
        pass
    if command == "sub":
        given_number = int(input("Give a number:"))
        total = total - given_number
        print(total)
        pass
    elif command == "exit":
        running = False