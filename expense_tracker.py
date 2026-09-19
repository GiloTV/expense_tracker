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