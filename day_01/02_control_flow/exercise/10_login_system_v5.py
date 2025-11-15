# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

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


########################################## correct user input OR admin creds
username_input_admin = username_input == admin_username
password_input_admin = password_input == admin_password
correct_username_given_2 = username_input == correct_username
correct_password_given_2 = password_input == correct_password

correct_user_credentials =  correct_password_given_2 and correct_username_given_2
correct_admin_credentials = username_input_admin and password_input_admin

if correct_user_credentials or correct_admin_credentials:
    print("Access Granted")
else:
    print("Access Denied")