# Expense Tracker

## About 

This program is part of my project portfolio documenting my transition from a Jr. Test Engineer 
to a Backend developer. It is my first approach to applications that uses a database. 

The main purpose of this project was to practice a basic CRUD operations and begin combining python with SQL. The program allows users to
Create new expenses, view, modify and delete expenses as well as calculate the amount spent.

## Features

- Add new expenses
- Automatically register the current date
- Select an expense category
- Display all expenses
- Calculate the total amount spent
- Modify an existing expense
- Delete an expense after confirmation
- Store expenses persistently in SQLite

## Technologies

- Python 3
- SQLite
- Python 'Datetime' module

## Database structure

'id' | Unique identifier for each expense
'expense_date' | Date associated with the expense
'category' | Expense category
'Description' |  Short explanation of the expense
'amount' | Amount spent in "MXN"

## How to run

1. Clone the repository.
2. Open the project directory.
3. Run:

​```bash
python expense_tracker.py
​```

The SQLite database and expenses table are created automatically if they do not already exists.

## Current limitations

The main purpose of this version was to practice basic CRUD operations and combine SQL with python. 
Because of that, I am aware of the following limitations:

- Amounts are stored as positive whole numbers
- Decimal MXN amounts and centavos are not currently supported
- New expenses automatically receive the current date
- Reports and category-based summaries are not implemented
- The program uses four predefined categories

  ## Possible Future Improvements

After improving in other areas and developing more projects I would like to return to this project and modify it
so I can see how much I grow and how much my programming skills have grown :D

- Support decimal amounts safely
- Allow users to select transaction dates
- Add spending reports by categories and dates
- Add monthly expense summaries
- Improve the command-line presentation (even change the interface to a graphic one)
- Separate database operations into another python module
- Add automated tests.

## What I learned

- Performing CRUD operations
- Connecting python to an SQLite database
- Using parameterized SQL queries
- Improve the logic for yes-or-no confirmation prompts
- Validating user input
- Handling records by ID
- Dividing my program into functions
- Working with tuples
- Identifying duplicated code and extracting it into reusable functions
