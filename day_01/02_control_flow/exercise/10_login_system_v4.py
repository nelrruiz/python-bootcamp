# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
correct_credentials = None
print("Access Granted")
print("Access Denied")

####################################### answer
correct_username_given = username_input == correct_username
correct_password_given = password_input == correct_password

correct_credentials =  correct_password_given and correct_username_given

if correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")