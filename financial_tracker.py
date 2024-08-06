import sqlite3
import datetime
import os.path

class Transaction():
    def __init__(self, id, reference, amount, category, 
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
                    VALUES (?,?,?,?,?,?)''', 
                    (self.id, self.reference, self.amount, self.category, 
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
    goal_desc = "No description"
    complete = False

    def __init__(self, goal_desc, complete):
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
transactions_table_columns = "id INT PRIMARY KEY, reference TEXT, amount VARCHAR, category TEXT, date VARCHAR, outgoing BIT NOT NULL"
transactions_column_list = "id,reference,amount,category,date,outgoing"
expense_category_list = ["Eating out", "Groceries", "Travel", "Household", "Clothing", "Other"]
income_category_list = ["Salaried work", "Sold item", "Freelance work", "Reimbursement", "Gift", "Other"]
data_entry_headers = ["reference", "amount", "category", "year", "month", "day"]

financial_goals_table_columns = "goal VARCHAR, complete BIT"
financial_goals_column_list = "goal,complete"

budget_table_columns = "category TEXT, amount VARCHAR"
budget_table_column_list = "category,amount"

get_user_expense_category = f'''Please choose a category
                                                        
1. Eating out
2. Groceries
3. Travel
4. Household
5. Clothing
6. Other
                                
Enter selection: '''

get_user_income_category = f'''Please choose a category
                                                        
1. Salaried job
2. Sold item
3. Freelance work
4. Reimbursement
5. gift
6. Other
                                
Enter selection: '''


# Functions
def create_table(table_name, table_columns):
    cursor.execute(f'''CREATE TABLE {table_name} 
                ({table_columns})
                ''')
    db.commit()

def get_existing_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    existing_data = cursor.fetchall()
    return existing_data

def add_data_to_class(existing_data, class_name, list_of_objects):
    if class_name == "transaction":
        for tuple in existing_data:
            date_split = tuple[4].split("/")
            new_transaction = Transaction(tuple[0], tuple[1], tuple[2], tuple[3], 
                                          int(date_split[0]), int(date_split[1]), 
                                          int(date_split[2]), tuple[5])
            list_of_objects.append(new_transaction)
    elif class_name == "goal":
        for tuple in existing_data:
            new_goal = Financial_goal(tuple[0], tuple[1])
            list_of_objects.append(new_goal)
    else:
        for tuple in existing_data:
            new_budget = Budget(tuple[0], tuple[1])
            list_of_objects.append(new_budget)
    return list_of_objects



# Add expenses
def get_user_input(data_category, get_user_category_message):
    while True:
        if data_category == "category":
            user_input = input(get_user_category_message)
        else:
            user_input = input(f"Please enter the {data_category}: ")
        return user_input
    
def validate_user_input(user_input, data_category, category_list):
    if data_category == "reference":
        while True:
            if len(user_input) > 20:
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
            if user_input not in ("1", "2", "3", "4", "5", "6"):
                user_input = input("Please choose a valid option: ")
            else:
                for i in range(0, len(category_list)+1):
                    if int(user_input) == i:
                        user_input = category_list[i-1]
                        return user_input
                    
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
                    

# View all expenses or incomes
def get_transactions(table_name, incoming_value):
    cursor.execute(f'''SELECT reference, amount, date FROM {table_name}
                    WHERE outgoing = {incoming_value}''')
    all_transactions = cursor.fetchall()
    return all_transactions

# View transactions by category
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

# Add budget
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
    if user_budget_category == "Eating out":
        budget_percentage = 10
    elif user_budget_category == "Groceries":
        budget_percentage = 20
    elif user_budget_category == "Travel":
        budget_percentage == 25
    elif user_budget_category == "Household":
        budget_percentage = 20
    elif user_budget_category == "Clothing":
        budget_percentage = 10
    else:
        budget_percentage = 25
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







# Script

if os.path.isfile('financial_tracker.db') == False:
    table_already_exists = False

db = sqlite3.connect('financial_tracker.db')

cursor = db.cursor()

# If db doesn't already exist, create new tables and insert default data.
if table_already_exists == False:
    create_table(transactions_table_name, transactions_table_columns)

    expense1 = Transaction(1, "tshirt", 12.3, "Clothing", 2024, 4, 14, True)
    expense2 = Transaction(2, "eggs", 2.5, "Groceries", 2024, 4, 14, True)
    expense3 = Transaction(3, "Zizzi", 20, "Eating out", 2024, 4, 14, True)
    expense4 = Transaction(4, "mop", 5.55, "Household", 2024, 4, 14, True)
    income1 = Transaction(5, "SCO", 1650.0, "Salaried work", 2024, 5, 12, False)
    income2 = Transaction(6, "Flat warming", 50.0, "Gift", 2024, 6, 13, False)
    income3 = Transaction(7, "OFA", 3200.0, "Freelance work", 2024, 8, 12, False)
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
11. Quit

Enter selection: ''')
    
    # Add expense
    if user_input_main_script == "1":
        
        new_data = []
        for data_entry_header in data_entry_headers:
            user_input = get_user_input(data_entry_header, get_user_expense_category)
            user_input = validate_user_input(user_input, data_entry_header, expense_category_list)
            new_data.append(user_input)

        new_id = all_transactions[-1].id + 1
        new_expense = Transaction(new_id, new_data[0], new_data[1], new_data[2], 
                                  new_data[3], new_data[4], new_data[5], True)
        all_transactions.append(new_expense)
        new_expense.create_rows(transactions_table_name, transactions_column_list)

        

    # View expenses
    elif user_input_main_script == "2":
        all_expenses = get_transactions(transactions_table_name, 1)
        format_transaction_list(all_expenses, "Expense")  

    # View expenses by category
    elif user_input_main_script == "3":
        user_input_category = get_user_input("category", get_user_expense_category)
        user_input_category = validate_user_input(user_input_category, "category", expense_category_list)
        expenses_in_category = get_transactions_by_category(transactions_table_name, user_input_category, 1)
        format_transaction_list(expenses_in_category, "Expense") 

    # Add income
    elif user_input_main_script == "4":
        new_data = []
        for data_entry_header in data_entry_headers:
            user_input = get_user_input(data_entry_header, get_user_income_category)
            user_input = validate_user_input(user_input, data_entry_header, income_category_list)
            new_data.append(user_input)

        new_id = all_transactions[-1].id + 1
        new_income = Transaction(new_id, new_data[0], new_data[1], new_data[2], 
                                  new_data[3], new_data[4], new_data[5], False)
        all_transactions.append(new_income)
        new_income.create_rows(transactions_table_name, transactions_column_list)

    # View all incomes
    elif user_input_main_script == "5":
        all_incomes = get_transactions(transactions_table_name, 0)
        format_transaction_list(all_incomes, "Income")  
    
    # View incomes by category
    elif user_input_main_script == "6":
        user_input_category = get_user_input("category", get_user_income_category)
        user_input_category = validate_user_input(user_input_category, "category", income_category_list)
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
        user_budget_category = get_user_input("category", get_user_expense_category)
        user_budget_category = validate_user_input(user_budget_category, "category", expense_category_list)
        
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
                user_budget_amount = get_user_input("amount", get_user_expense_category)
                user_budget_amount = validate_user_input(user_budget_amount, "amount", expense_category_list)
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
                    user_budget_amount = get_user_input("amount", get_user_expense_category)
                    user_budget_amount = validate_user_input(user_budget_amount, "amount", expense_category_list)
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

                # existing_budget_in_category.amount = user_budget_amount
                # budget_set_message(existing_budget_in_category)
            else:
                budget_set_message(existing_budget_in_category)

    # View budget by category
    elif user_input_main_script == "8":
        # Get category from user
        user_budget_category = get_user_input("category", get_user_expense_category)
        user_budget_category = validate_user_input(user_budget_category, "category", expense_category_list)

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
        new_goal = Financial_goal(user_goal_input, False)
        is_complete = new_goal.complete
        new_goal.create_rows('financial_goals', financial_goals_column_list)
        all_goals.append(new_goal)
        print("New goal set.")

    # View financial goals
    elif user_input_main_script == "10":
        if all_goals == []:
            print("\nNo financial goals")
        else:
            header = "Financial Goals"
            print(f'''\n\033[1m{header.center(43)}\033[0m''')
            for goal in all_goals:
                if goal.complete == False:
                    is_complete = "Not complete"
                else:
                    is_complete = "Complete"
                print(f"\nGoal: {goal.goal_desc}\t{is_complete}")


    elif user_input_main_script == "11":
        print("Goodbye!")
        break
    
    else:
        print("Please try again.")

