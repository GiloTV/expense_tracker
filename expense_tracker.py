from datetime import datetime
import sqlite3

def create_database():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()

    # Expense table definition. Stores expenses id, the expense date, expense category, description and amount of the stored expenses 
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
    db = sqlite3.connect("expense_tracker.db")
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
                print('No category selected. Try again')
                category = ''

    description = input("Add a little description about the expense: ")
    amount = input_number("amount")

    new_expense = (expense_date, category, description, amount)
    insert_expense(new_expense)

def show_all_expenses():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    res = cur.execute(
        """
        SELECT * FROM expenses
    """)
    expenses = res.fetchall()
    for expense_id, expense_date, category, description, amount in expenses:
        print(f"""
        {'='*25} 
        Expense details
        expense: {expense_id}
        expense date: {expense_date}
        category: {category}
        description: {description}
        amount: {amount}
        {'='*25}""")

    db.close()

def calculate_total_spent():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    res = cur.execute("SELECT amount FROM expenses")

    amounts = res.fetchall()
    total = 0
    for amount in amounts:
        total += amount[0]

    print(total)

def modify_expense():
    show_all_expenses()
    
    expense_id = input_number("id")
    


    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    cur.execute("SELECT * from expenses WHERE id = ?",(expense_id,))
    res = cur.fetchall()
    if res == []:
        print("No expense found with that ID try again!")
        
    
    
    while True:
        modify_option = input(f"""
        {'*' * 30}
        1. Modify date
        2. Modify category
        3. Modify description
        4. Modify amount
        5. Exit
        {'*' * 30}
        """).strip()
        match modify_option:
            case '1':
                print("Modify date")
                modify_date(expense_id)
            case '2':
                print("Modify category")
                modify_category(expense_id)
            case '3':
                print("Modify description")
            case '4':
                print("Modify amount")
            case '5':
                print("Back to main menu")
                break
            case _:
                print("Try again")

def modify_date(expense_id):
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    current_date = datetime.today().strftime('%Y-%m-%d')
    cur.execute("UPDATE expenses SET expense_date = ? WHERE id = ?", (current_date, expense_id))
    print("Date was updated succesfully")
    
    db.commit()
    db.close()

def modify_category(expense_id):
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    new_category = ''
    # Categories menu option to modify the category of a expense
    while not new_category:
        new_category = input("""
            Insert the new category for the expense
            1.- Service
            2.- Food
            3.- Emergency
            4.- Hobby
        """)
        match new_category:
            case '1':
                new_category = 'Service'
            case '2':
                new_category = 'Food'
            case '3':
                new_category = 'Emergency'
            case '4':
                new_category = 'Hobby' 
            case _:
                print('No category selected. Try again')

        print("new category: ", new_category)
        cur.execute("SELECT category FROM expenses WHERE id = ?",(expense_id,))
        current_category = cur.fetchone()[0]
        print("Current category: ",current_category)
        if current_category == new_category:
            while True:
                duplicated_case = input("Selected category is alrady the category for the expense. Would you like to continie anyway? 'Y' | 'N'").lower().strip()
                match duplicated_case:
                    case 'y' | 'yes':
                        cur.execute("UPDATE expenses SET category = ? WHERE id = ?",(new_category, expense_id))
                        break
                    case 'n' | 'no':
                        print("Returning to the previous menu. Select a new category")
                        new_category = ''
                        break
        else:
            cur.execute("UPDATE expenses SET category = ? WHERE id = ?",(new_category, expense_id))

    print("Category was updated succesfully")
    
    db.commit()
    db.close()

# def modify_description():

# def modify_amount():

def input_number(action):
        while True:
            num = input(f"Insert the {action} of the expense")
            try:
                num = int(num)
                if num <= 0:
                    print("Number not valid. Must be higher than 0")
                    continue
                return num
            except ValueError:
                        print("Input value not a number. Please type a number")
        

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
    Option: """).strip()

    match opt:
        case '1':
            print("Add new expense:")
            add_expense()
        case '2':
            print("Modify expense menu")
            modify_expense()
        case '3': 
            print("Show all expenses")
            show_all_expenses()
        case '4':
            print("Show total spent")
            calculate_total_spent()
        case '5':
            print('Option number 5, Goodbye')
            break
        case _:
            print('Invalid option, try again')