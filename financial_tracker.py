# This programme interacts with a database to store expenses, incomes, budgets and financial goals.
# The user can add expenses, incomes, budgets and financial goals manually.
# The programme also generates budgets automatically for each category, the budget depending on total expenses and income.

import sqlite3
import datetime
import os.path

class Transaction():
    def __init__(self, reference, amount, category, 
                 year, month, day, incoming):
        self.id = id
        self.reference = reference
        self.amount = amount
        self.category = category
        self.date = datetime.datetime(year, month, day)
        self.incoming = incoming
    
    def format_date(self):
        formatted_date = self.date.strftime("%d/%m/%y")
        return formatted_date

    def create_rows(self, table_name, column_list):
        formatted_date = self.format_date()
        cursor.execute(f'''INSERT INTO {table_name} ({column_list})
                    VALUES (?,?,?,?,?)''', 
                    (self.reference, self.amount, self.category, 
                     formatted_date, self.incoming))
        db.commit()

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def create_rows(self, table_name, column_list):
        cursor.execute(f'''INSERT INTO {table_name} ({column_list})
                    VALUES (?,?)''', 
                    (self.category, self.amount))
        db.commit()

class Financial_goal():
    def __init__(self):
        self.goal_desc = "Not set"
        self.complete = False
        self.id = -1

    def init_new(self, goal_desc):
        self.goal_desc = goal_desc
        
    def init_from_db(self, id, goal_desc, complete):
        self.id = id
        self.goal_desc = goal_desc
        self.complete = complete

    def set_as_complete(self):
        self.complete = True
        return True

    def create_rows(self, table_name, column_list):
        cursor.execute(f'''INSERT INTO {table_name} ({column_list})
                    VALUES (?,?)''', 
                    (self.goal_desc, self.complete))
        db.commit()
    

# Variables

all_transactions = []
all_budgets = []

expenses_as_list_of_tuples = []
new_data = []
all_goals = []
table_already_exists = True

transactions_table_name = "transactions"
transactions_table_columns = "reference TEXT, amount VARCHAR, category TEXT, date VARCHAR, outgoing BIT NOT NULL"
transactions_column_list = "reference,amount,category,date,outgoing"
expense_category_list = ["Eating out", "Groceries", "Travel", "Household", "Clothing", "Other"]
expense_category_list_index = [0, 1, 2, 3, 4, 5]
income_category_list = ["Salaried work", "Sold item", "Freelance work", "Reimbursement", "Gift", "Other"]
income_category_list_index = [0, 1, 2, 3, 4, 5, 6]
data_entry_headers = ["reference", "amount", "category", "year", "month", "day"]

financial_goals_table_columns = "goal VARCHAR, complete BIT"
financial_goals_column_list = "goal,complete"

budget_table_columns = "category TEXT, amount VARCHAR"
budget_table_column_list = "category,amount"

max_ref_length = 20
default_budgets_by_category = [10, 20, 25, 20, 10, 25]
header = "Financial Goals"


# Functions
def create_table(table_name, table_columns):
    cursor.execute(f'''CREATE TABLE {table_name} 
                ({table_columns})
                ''')
    db.commit()

def get_existing_data(table_name):
    cursor.execute(f"SELECT ROWID, * FROM {table_name}")
    existing_data = cursor.fetchall()
    return existing_data

def add_data_to_class(existing_data, class_name, list_of_objects):
    list_of_objects = []
    if class_name == "transaction":
        for tuple in existing_data:
            date_split = tuple[4].split("/")
            new_transaction = Transaction(tuple[1], tuple[2], tuple[3],
                                          int(date_split[0]), int(date_split[1]), 
                                          int(date_split[2]), tuple[5])
            list_of_objects.append(new_transaction)
    elif class_name == "goal":
        for tuple in existing_data:
            new_goal = Financial_goal()
            new_goal.init_from_db(tuple[0], tuple[1], tuple[2])
            list_of_objects.append(new_goal)
    else:
        for tuple in existing_data:
            new_budget = Budget(tuple[1], tuple[2])
            list_of_objects.append(new_budget)
    return list_of_objects


def get_user_transaction_category(list_of_transaction_categories):
    category_menu = "Please choose a category:\n"
    for index, item in enumerate(list_of_transaction_categories, 1):
        category_menu += f"\n{index}. {item}"

    user_input = input(f"{category_menu}\n\nEnter selection: ")
    return user_input


def get_user_input(data_category, list_of_transaction_categories):
    while True:
        if data_category == "category":
            user_input = get_user_transaction_category(list_of_transaction_categories)
        else:
            user_input = input(f"Please enter the {data_category}: ")
        return user_input
    
def validate_user_input(user_input, data_category, category_list):
    if data_category == "reference":
        while True:
            if len(user_input) > max_ref_length:
                user_input = input("Too many characters. Please try again: ")
            else:
                return user_input
    
    elif data_category == "amount":
        while True:
            try:
                user_input = float(user_input)
                if user_input > 0:
                    return user_input
                else: user_input = input("Please enter a positive number: ")
            except ValueError:
                user_input = input("Please enter a number: ")  

        
    elif data_category == "category":
        while True:
            for i in range(0, len(category_list)):
                if int(user_input) == i+1:
                    user_input = convert_category_input_to_string(user_input, category_list)
                    return user_input
            user_input = input("Please try again: ")
            
                    
    elif data_category == "year":
        while True:
            try:
                user_input = int(user_input)
                if user_input > 0 and user_input < 3000:
                    return user_input
                else: 
                    user_input = input("Please enter a valid year: ")
            except ValueError:
                user_input = input("Please enter a number: ") 
    
    elif data_category == "month":
        while True:
            try:
                user_input = int(user_input)
                if user_input > 0 and user_input < 13:
                    return user_input
                else:
                    user_input = input("Please enter a valid number: ")
            except ValueError:
                user_input = input("Please enter a number: ")  

    elif data_category == "day":
        while True:
            try:
                user_input = int(user_input)
                if user_input > 0 and user_input < 31:
                    return user_input
                else: user_input = input("Please enter a valid number: ")
            except ValueError:
                user_input = input("Please enter a number: ")


def get_valid_user_input(data_category, category_list):
    user_input = get_user_input(data_category, category_list)
    user_input = validate_user_input(user_input, data_category, category_list)
    return user_input

 
def convert_string_to_float(user_input_string):
    try:
        return float(user_input_string)
    except:
        return None  
      

def convert_string_to_int(user_input_string):
    try:
        return int(user_input_string)
    except:
        return None


def convert_category_input_to_string(user_input, category_list):
    for i in range(0, len(category_list)+1):
        if int(user_input) == i:
            user_input = category_list[i-1]
            return user_input
    

def get_transactions(table_name, incoming_value):
    cursor.execute(f'''SELECT reference, amount, date FROM {table_name}
                    WHERE outgoing = {incoming_value}''')
    all_transactions = cursor.fetchall()
    return all_transactions


def get_transactions_by_category(table_name, chosen_category, incoming_value):
    cursor.execute(f'''SELECT reference, amount, date FROM {table_name}
                   WHERE category = '{chosen_category}' 
                   and outgoing = {incoming_value} ''')
    transactions_in_category = cursor.fetchall()
    return transactions_in_category


def format_transaction_list(list_of_transactions, income_or_expense):
    for tuple in list_of_transactions:
        formatted_expenses = f'''
        {income_or_expense} reference: {tuple[0]}
        Amount: {display_amount_as_gbp(float(tuple[1]))}
        Date of transaction: {tuple[2]}'''

        print(formatted_expenses)
    if len(list_of_transactions) == 0:    
        print(f"You have recorded no {income_or_expense.lower()} in this category.") 


def display_amount_as_gbp(amount):
    pence = str(amount).split(".")[-1]
    if float(amount) == int(amount):
        amount_as_gbp = f"£{int(amount)}.00"

    elif str(amount)[-2] == ".":
        amount_as_gbp = f"£{amount}0"
    
    elif len(pence) > 2:
        amount_as_gbp = f"£{'%.2f' % float(amount)}"

    else:
        amount_as_gbp = f"£{amount}"
        
    return amount_as_gbp


def get_valid_budget_options(user_budget_type):
    while True:
        if user_budget_type not in ("1", "2"):
            user_budget_type = input("Please enter a valid option: ")
        else:
            return user_budget_type


def does_budget_exist_in_category(all_budgets, user_budget_category):
    for budget in all_budgets:
        if user_budget_category == budget.category:
            return budget.amount.display_amount_as_gbp()
    return False


def get_amount_left_over(sum_of_expenses, sum_of_incomes):
    for transaction in all_transactions:
        if transaction.incoming == 1:
            sum_of_expenses += float(transaction.amount)
        else:
            sum_of_incomes += float(transaction.amount)
    amount_left_over = sum_of_incomes - sum_of_expenses
    return amount_left_over


def get_budget_percentage(user_budget_category):
    for i in range(0, len(expense_category_list)):
        if user_budget_category == expense_category_list[i]:
            budget_percentage = default_budgets_by_category[i]
            return budget_percentage


def calculate_budget(amount_left_over, budget_percentage):
    user_budget_amount = (float(amount_left_over)/100) * budget_percentage
    return user_budget_amount


def budget_set_message(new_budget):
    budget_as_gbp = display_amount_as_gbp(float(new_budget.amount))
    print(f"You have set your {new_budget.category} budget to {budget_as_gbp}")


def confirm_budget_replace(user_input):
    while True:
        if user_input == "y" or user_input == "yes":
            return True
        elif user_input == "n" or user_input == "no":
            return False
        user_input = input("Please enter a valid option: ")


def view_financial_goals(header, all_goals):
    print(f'''\n\033[1m{header.center(43)}\033[0m\n''')
    for goal in all_goals:
        if goal.complete == False:
            is_complete = "Not complete"
        else:
            is_complete = "Complete"
        print(f"{goal.id}: {goal.goal_desc} \t\t\t{is_complete}")


def format_goal_list(goal_list):
    message = f"\nWhich goal have you completed?"
    for goal in goal_list:
        message += f"\n{goal[0]}. {goal[1]}"
    message += "\nEnter selection: "
    goal_to_complete = input(message)
    return goal_to_complete


def get_valid_goal(goal_to_complete, goal_list):
    while True:
        for goal in goal_list:
            if goal_to_complete == str(goal[0]):
                goal_to_complete = check_if_complete(goal_to_complete)
                return goal_to_complete
        goal_to_complete = input("Please enter a valid number: ")


def check_if_complete(goal_to_complete):
    while True:
        cursor.execute(f'''SELECT * FROM financial_goals
                    WHERE rowid = {goal_to_complete}''')
        goal = cursor.fetchone()
        if goal[1] == False:
            return goal_to_complete
        else:
            goal_to_complete = input("This goal is already complete. Please try again: ")
        

def set_as_complete_in_db(goal_id_to_complete):

    cursor.execute(f'''UPDATE financial_goals SET complete = 1
                   WHERE rowid = {goal_id_to_complete}''')
    db.commit()


# Script

if os.path.isfile('financial_tracker.db') == False:
    table_already_exists = False

db = sqlite3.connect('financial_tracker.db')

cursor = db.cursor()

# If db doesn't already exist, create new tables and insert default data.
if table_already_exists == False:
    create_table(transactions_table_name, transactions_table_columns)

    # Default expenses and income data.
    expense1 = Transaction("tshirt", 12.3, "Clothing", 2024, 4, 14, True)
    expense2 = Transaction("eggs", 2.5, "Groceries", 2024, 4, 14, True)
    expense3 = Transaction("Zizzi", 20, "Eating out", 2024, 4, 14, True)
    expense4 = Transaction("mop", 5.55, "Household", 2024, 4, 14, True)
    income1 = Transaction("SCO", 1650.0, "Salaried work", 2024, 5, 12, False)
    income2 = Transaction("Flat warming", 50.0, "Gift", 2024, 6, 13, False)
    income3 = Transaction("OFA", 3200.0, "Freelance work", 2024, 8, 12, False)
    all_transactions = [expense1, expense2, expense3, expense4, income1, income2, income3]

    for item in all_transactions:
        item.create_rows(transactions_table_name, transactions_column_list)
    print("Transactions table successfully created.")

    create_table('financial_goals', financial_goals_table_columns)
    print("Financial Goals table successfully created.")

    create_table('budgets', budget_table_columns)
    print("Budgets table successfully created.")


# If db does already exist, retrieve existing data from tables.
else:
    existing_expenses_data = get_existing_data(transactions_table_name)
    all_transactions = add_data_to_class(existing_expenses_data, "transaction", all_transactions)

    existing_goal_data = get_existing_data('financial_goals')
    all_goals = add_data_to_class(existing_goal_data, "goal", all_goals)

    existing_budget_data = get_existing_data('budgets')
    all_budgets = add_data_to_class(existing_budget_data, "budget", all_budgets)

while True:
    # \033[1m = Bold text
    user_input_main_script = input('''\n
                \033[1mMain Menu\033[0m

1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View imcome by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. View progress towards financial goals
11. Set financial goal as complete
12. Quit

Enter selection: ''')
    
    # Add expense
    if user_input_main_script == "1":
        
        new_data = []
        for data_entry_header in data_entry_headers:
            user_input = get_valid_user_input(data_entry_header, expense_category_list)
            new_data.append(user_input)

        new_expense = Transaction(new_data[0], new_data[1], new_data[2], 
                                  new_data[3], new_data[4], new_data[5], True)
        all_transactions.append(new_expense)
        new_expense.create_rows(transactions_table_name, transactions_column_list)

        

    # View expenses
    elif user_input_main_script == "2":
        all_expenses = get_transactions(transactions_table_name, 1)
        format_transaction_list(all_expenses, "Expense")  

    # View expenses by category
    elif user_input_main_script == "3":
        user_input_category = get_valid_user_input("category", expense_category_list)
        expenses_in_category = get_transactions_by_category(transactions_table_name, user_input_category, 1)
        format_transaction_list(expenses_in_category, "Expense") 

    # Add income
    elif user_input_main_script == "4":
        new_data = []
        for data_entry_header in data_entry_headers:
            user_input = get_valid_user_input(data_entry_header, income_category_list)
            new_data.append(user_input)

        new_income = Transaction(new_data[0], new_data[1], new_data[2], 
                                  new_data[3], new_data[4], new_data[5], False)
        all_transactions.append(new_income)
        new_income.create_rows(transactions_table_name, transactions_column_list)

    # View all incomes
    elif user_input_main_script == "5":
        all_incomes = get_transactions(transactions_table_name, 0)
        format_transaction_list(all_incomes, "Income")  
    
    # View incomes by category
    elif user_input_main_script == "6":
        user_input_category = get_valid_user_input("category", income_category_list)
        incomes_in_category = get_transactions_by_category(transactions_table_name, user_input_category, 0)
        format_transaction_list(incomes_in_category, "Income") 
    
    # Set budget for a category
    elif user_input_main_script == "7":
        user_budget_type = input('''Please choose a budget option:
                                 
    1. Manually enter budget
    2. Automatically generate budget
                            
    Enter selection: ''')
        
        user_budget_type = get_valid_budget_options(user_budget_type)
        
        # Get category from user
        user_budget_category = get_valid_user_input("category", expense_category_list)
        
        # Check whether a budget within chosen category already exists.
        is_budget_existing = False
        for budget in all_budgets:
            if user_budget_category == budget.category:
                existing_budget_in_category = budget
                existing_budget_amount_in_category = budget.amount
                is_budget_existing = True
                break

        # If there is no existing budget for chosen category.
        if is_budget_existing == False or all_budgets == []:
            # Enter budget manually.
            if user_budget_type == "1":
                user_budget_amount = get_valid_user_input("amount", expense_category_list)
            else:
                # Get budget automatically.
                amount_left_over = get_amount_left_over(0, 0)
                budget_percentage = get_budget_percentage(user_budget_category)
                user_budget_amount = calculate_budget(amount_left_over, budget_percentage)

            
            # Add budget to class and table
            new_budget = Budget(user_budget_category, user_budget_amount)
            new_budget.create_rows('budgets', budget_table_column_list)
            all_budgets.append(new_budget)
            budget_set_message(new_budget)

        else:
            amount_as_gbp = display_amount_as_gbp(float(existing_budget_amount_in_category))
            print(f"The {user_budget_category} budget is currently set to "
                f"{amount_as_gbp}")
            
            user_input_confirmation = input('''Would you like to replace this with a new budget?
                    
    y - yes
    n - no
                    
    Enter selection: ''')

            is_replace_budget = confirm_budget_replace(user_input_confirmation)
            if is_replace_budget == True:
                # Get budget manually.
                if user_budget_type == "1":
                    user_budget_amount = get_valid_user_input("amount", expense_category_list)
                else:
                    # Get budget automatically.
                    amount_left_over = get_amount_left_over(0, 0)
                    budget_percentage = get_budget_percentage(user_budget_category)
                    user_budget_amount = calculate_budget(amount_left_over, budget_percentage)

                # Replace existing budget with new budget in Budget class.
                existing_budget_in_category.amount = user_budget_amount
                cursor.execute(f'''UPDATE 'budgets' SET amount = {user_budget_amount}
                                WHERE category = '{user_budget_category}' ''')
                db.commit()
                budget_set_message(existing_budget_in_category)

            else:
                budget_set_message(existing_budget_in_category)

    # View budget by category
    elif user_input_main_script == "8":
        # Get category from user
        user_budget_category = get_valid_user_input("category", expense_category_list)
        # Check if budget already exists for users chosen category.
        budget_exists = False
        for budget in all_budgets:
            if user_budget_category == budget.category:
                existing_budget_amount_in_category = budget.amount
                amount_as_gbp = display_amount_as_gbp(float(existing_budget_amount_in_category))
                print(f"The {user_budget_category} budget is currently set to "
                f"{amount_as_gbp}")

                budget_exists = True
                break
            
        if budget_exists == False or all_budgets == []:
            print(f"There is no {user_budget_category} budget set.")

    # Set financial goals
    elif user_input_main_script == "9":
        user_goal_input = input("Please enter a financial goal: ")
        while True:
            if user_goal_input == "" or len(user_goal_input) > 30:
                user_goal_input = input("Please enter between 1 and 30 characters: ")
            else:
                break
        new_goal = Financial_goal()
        # Initialize new goal.
        new_goal.init_new(user_goal_input)
        is_complete = new_goal.complete
        # Insert into financial_goals table.
        new_goal.create_rows('financial_goals', financial_goals_column_list)
        # Get rowid of new goal.
        cursor.execute('''SELECT last_insert_rowid() FROM financial_goals''')
        new_id = cursor.fetchone()
        # Pass rowid into financial_goals class.
        new_goal.init_from_db(new_id[0], user_goal_input, is_complete)
        all_goals.append(new_goal)
        print("New goal set.")

    # View financial goals
    elif user_input_main_script == "10":
        if all_goals == []:
            print("\nNo financial goals")
        else:
            view_financial_goals(header, all_goals)

    # Complete financial goals
    elif user_input_main_script == "11":
        existing_goal_data = get_existing_data('financial_goals')
        # Get valid goal to set as complete.
        goal_to_complete = format_goal_list(existing_goal_data)
        goal_to_complete = get_valid_goal(goal_to_complete, existing_goal_data)
        set_as_complete_in_db(goal_to_complete)
        all_goals = add_data_to_class(existing_goal_data, "goal", all_goals)
        # Set as complete in class object
        for goal in all_goals:
            if int(goal_to_complete) == goal.id:
                goal.set_as_complete()

    elif user_input_main_script == "12":
        print("Goodbye!")
        break
    
    else:
        print("Please try again.")

