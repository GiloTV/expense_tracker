from datetime import datetime
import sqlite3

def create_database():
    db = sqlite3.connect("expenses.db")
    cur = db.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date VARCHAR NOT NULL,
            category VARCHAR NOT NULL,
            description TEXT NOT NULL,
            amount INTEGER NOT NULL
        )
    """)
    
 
    db.close()

def insert_expense(data):
    db = sqlite3.connect("expenses.db")
    cur = db.cursor()

    cur.execute(
        """
        INSERT INTO expenses(
            expense_date,
            category,
            description,
            amount
        )
        VALUES (?, ?, ?, ?)
    """,
    data
    )
    db.commit()
    db.close()

def add_expense():
    expense_date = datetime.today().strftime('%Y-%m-%d')
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
    description = input("Add a little description about the expense\n")

    while True:
        amount = input("Insert the amount of the expense")
        try:
            amount = int(amount)
            break
        except ValueError:
            print("Invalid amount. Please type a number")

    new_expense = (expense_date, category, description, amount)
    
    insert_expense(new_expense)

create_database()

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
            add_expense()
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