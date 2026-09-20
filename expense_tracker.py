from datetime import datetime

def expense_data():
    date = datetime.today().strftime('%Y-%m-%d')
    category = ''
    while not category:
        category = input("""
            Insert the category of the expense
            1.- Service
            2.- Food
            3.- Emergency
            4.- Hobby
        """)
        match category:
            case '1':
                category = 'Service'
            case '2':
                category = 'Food'
            case '3':
                category = 'Emergency'
            case '4':
                category = 'Hobby' 
            case _:
                category = ''
                print('No category selected. Try again')
    description = input("Add a little description about the expense")

    while True:
        amount = input("Insert the amount of the expense")
        try:
            amount = int(amount)
            break
        except ValueError:
            print("Invalid amount. Please type a number")

    new_expense = (date, category, description, amount)
    print(type(new_expense))
    print("expense details", new_expense)

while True:
    opt = input(f"""
    {'*' * 30}
    1. Add new expense
    2. Modify expense
    3. Show all expenses
    4. Show total spent
    5. Exit
    {'*' * 30}
    Option: """)

    match opt:
        case '1':
            print("Add new expense:")
            expense_data()
        case '2':
            print("Modify an expense")
             
        case '3': 
            print("Show all expenses")
            
        case '4':
            print("Show total expense")

        case '5':
            print('Option number 5, Goodbye')
            break
        case _:
            print('Invalid option, try again')