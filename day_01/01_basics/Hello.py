print("Hello World")
print("Hello Again!")

print("I", "am","happy")
print("I am happy!", "This is great")

print("Hello! My name is Nelica")
print("I am learning Python")

##Comments
# Practice for printing in multiple lines
# ctrl+/ to be comment and to remove as comment
# Multiple line comment 3 double quotes top and 3 below

# variable printing
message="Test Message"
print (message)

#exercise on combining texts and variables
name ="Nelica"
language = "Python"
print("Hello! My name is", name)
print("I am learning", language)

#variable reassignment
total = 10
print(total) #result is 10
total = 5
print(total) #result is 5

#setting the type of the variable
total: int = 5
type(total)


#large numbers in millions or billions
sana_salary = 123_456_789
print(sana_salary)

total_1=None
type(total_1)

# input function
user_input = input()
print("The user said:", user_input)

user_input = input("Enter your name:")
print("The user said:", user_input)


# placeholder {}
message = "Hello {}! Nice to meet you!"
new_message = message.format("John")
print(new_message)
new_message2 = message.format("Jeff")
print(new_message2)

#########

login_input = input("Login: ")

user_logged_in = login_input=="Yes"

if user_logged_in:
    print("Welcome")
    print("Back")
print("End")

################################

class Parent:
    def parent_method(self):
        print("Parent Method")
    def parent_method2(self):
        print("Parent method2")

class Child(Parent):
    def child_method(self):
        print("child method")
        
child = Child()
child.parent_method2()