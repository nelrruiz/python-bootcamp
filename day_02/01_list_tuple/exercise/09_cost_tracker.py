def spend(expenses):
    """TODO: Add a new cost in expenses"""
    expense = int(input("Enter expense: "))
    expenses.append(expense)


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    
    if expenses:
        expenses.pop(-1)
    else:
        print("Warning: Expenses is empty")

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print("Total:", sum(expenses))

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        else:
            print("No action provided")
        


main()
