from datetime import datetime
import sqlite3


def create_database():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()

    # Expense table definition. Stores expenses id, date, category, description and amount of the stored expenses 
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
    category = category_selector()
    while True:
        description = input("Add a little description about the expense: ").strip()
        if description:
            break
        print("Description must be provided. Try again")
    amount = input_number("amount")
    expense_data = (expense_date, category, description, amount)
    insert_expense(expense_data)

def show_all_expenses():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    res = cur.execute("SELECT * FROM expenses")
    expenses = res.fetchall()
    if not expenses:
        print("There are no expenses to show")
        db.close()
    else: 
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
    res = cur.execute("SELECT SUM(amount) FROM expenses")
    total_spent = res.fetchone()[0]
    print(total_spent)
    db.close()

def modify_expense():  
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    show_all_expenses()
    expense_data = ''
    while not expense_data:
        expense_id = input_number("id")
        cur.execute("SELECT * from expenses WHERE id = ?",(expense_id,))
        expense_data = cur.fetchone()
        if expense_data:
            print("Expense found, printing data...")
            exp_id, date, category, description, amount = expense_data
            print(f"""
                {'='*25} 
                Expense details
                expense: {exp_id}
                expense date: {date}
                category: {category}
                description: {description}
                amount: {amount}
                {'='*25}""")
        else:
            print("Expense not found try again")
        
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
                modify_description(expense_id)
            case '4':
                print("Modify amount")
                modify_amount(expense_id)
            case '5':
                print("Back to main menu")
                break
            case _:
                print("Invalid Option. Try again")
    db.close()
    

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
    new_category = category_selector()
    print("new category: ", new_category)
    cur.execute("SELECT category FROM expenses WHERE id = ?",(expense_id,))
    current_category = cur.fetchone()[0]
    print("Current category: ",current_category)
    # Handle the case where modified category is same as the old category 
    if current_category == new_category:
        while True:
            confirmation = input("Selected category is alrady the category for the expense. Would you like to continie anyway? 'Y' | 'N' \n -> ").lower().strip()
            if confirmation in ('y', 'yes'):
                cur.execute("UPDATE expenses SET category = ? WHERE id = ?",(new_category, expense_id))
                db.commit()
                print("Category was updated! :D")
                db.close()
                break
            if confirmation in ('n', 'no'):
                print("Category selection cancelled")
                db.close()
                break
            print("Please select a valid option")
    else:
        cur.execute("UPDATE expenses SET category = ? WHERE id = ?",(new_category, expense_id))

def modify_description(expense_id):
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    while True:
        new_description = input("Insert the new description of the expense \n -> ").strip()
        if new_description:
            break
        print("Description must be provided. Try again")
    cur.execute("UPDATE expenses SET description = ? WHERE id = ?",(new_description, expense_id))
    print("Description was updated! :D")
    db.commit()
    db.close()


def modify_amount(expense_id):
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()
    new_amount = input_number("amount")
    cur.execute("UPDATE expenses SET amount = ? WHERE id = ?", (new_amount, expense_id))
    print("Amount was updated! :D")
    db.commit()
    db.close()

def delete_expense():
    db = sqlite3.connect("expense_tracker.db")
    cur = db.cursor()

    while True:
        expense_id = input_number("ID")
        cur.execute("SELECT * FROM expenses WHERE id = ?",(expense_id,))
        expense_data = cur.fetchone()

        if not expense_data:
            print("No expense found with that ID. Please try again")
            continue

        expense_id, date, category, description, amount = expense_data
        print("Expense for deleting, printing data...")
        print(f"""
            {'='*25} 
            Expense details
            expense: {expense_id}
            expense date: {date}
            category: {category}
            description: {description}
            amount: {amount}
            {'='*25}""")
        while True:
            confirmation = input("Delete this expense Y/N").lower().strip()
            if confirmation in ("y", "yes"):
                cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
                db.commit()
                print("Expense deleted successfully")
                db.close()
                return
            if confirmation in ("n", "no"):
                print("Expense deletion cancelled")
                db.close()
                return
            print("Please type yes or no")
            
# Returns valid numbers for amount and categories menu selector
def input_number(action):
        while True:
            num = input(f"Insert the {action} of the expense\n -> ")
            try:
                num = int(num)
                if num <= 0:
                    print("Number not valid. Must be higher than 0")
                    continue
                return num
            except ValueError:
                        print("Input value not a number. Please type a number")

# Returns the category of the expense
def category_selector():
    category = ''
    # Categories menu option selector
    while not category:
        category = input("""
            Insert the new category for the expense
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
    return category
        
create_database()

while True:
    opt = input(f"""
    {'*' * 30}
    1. Add new expense
    2. Modify expense
    3. Show all expenses
    4. Show total spent
    5. Delete expense
    6. Exit
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
            print('Delete expense')
            delete_expense()
        case '6':
            print('Goodbye')
            break
        case _:
            print('Invalid option, try again')
