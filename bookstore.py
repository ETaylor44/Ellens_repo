# A program which allows the user to search for, add, modify and delete books in the database.

import sqlite3
import os

# Create books class.
class Book():
    def __init__(self, id, title, author, qty):
        self.id = id
        self.title = title
        self.author = author
        self.qty = qty

    # def get_book_as_tuple(self):
    #     return (self.id,self.title,self.author,self.qty)
    
    def create_rows(self, table_name, column_list):
        cursor.execute(f'''INSERT INTO {table_name} ({column_list})
                    VALUES (?,?,?,?)''', 
                    (self.id, self.title, self.author, self.qty))
        db.commit()

    def get_new_id(self):
        new_id = book_records[-1].id + 1
        return new_id



# book_records = [book1.get_book_as_tuple(), book2.get_book_as_tuple(), book3.get_book_as_tuple(), 
#                     book4.get_book_as_tuple(), book5.get_book_as_tuple()]

book_records = []
table_already_exists = True

table_name = 'ebookstore'
column_list = "id,title,author,qty"

# Create database

if os.path.isfile('ebookstore.db') == False:
    table_already_exists = False

db = sqlite3.connect('ebookstore.db')

cursor = db.cursor()

if table_already_exists == False:
    # Create table with default data.
    cursor.execute('''
        CREATE TABLE ebookstore(id INTEGER PRIMARY KEY, title TEXT UNIQUE, 
                author VARCHAR, qty INTEGER)''')
    
    db.commit()

    book1 = Book(3001, "A Tale of Two Cities", "Charles Dickens", 30)
    book2 = Book(3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40)
    book3 = Book(3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25)
    book4 = Book(3004, "The Lord of the Rings", "J.R.R Tolkien", 37)
    book5 = Book(3005, "Alice in Wonderland", "Lewis Carroll", 12)
    book_records = [book1, book2, book3, book4, book5]

    for book in book_records:
        book.create_rows(table_name, column_list)
    print("ebookstore table successfully created.")


else:
    cursor.execute(f'''SELECT * FROM ebookstore''')
    existing_books = cursor.fetchall()
    for tuple in existing_books:
        book = Book(tuple[0], tuple[1], tuple[2], tuple[3])
        book_records.append(book)
        


# Variables
get_id_to_update_book = "\nPlease enter the ID of the book to update: "
get_id_to_delete_book = "\nPlease enter the ID of the book to delete: "
get_user_edit_option = '''\nWhich data category would you like to edit?
    1. Title
    2. Author
    3. Quantity
    4. Cancel
                           
    Enter selection: '''
get_user_search_option = '''\nPlease select a category to search by:
    1. Title
    2. Author
    3. Quantity
    4. Cancel
                           
    Enter selection: '''

# Create an id for new book entry (add one to previous book id).
def generate_new_id(book_records):
    last_record = book_records[-1]
    last_record_id = last_record[0]
    new_record_id = last_record_id + 1
    return new_record_id
        
        
def get_title_from_user():
    new_title = input("\nPlease enter a book title: ")
    return new_title


def get_author_from_user():
    new_author = input("Please enter an author: ")
    return new_author


def get_qty_from_user(new_title):
    while True:
        new_qty = input(f"How many copies of {new_title} do you have? ")
        try:
            new_qty_as_int = int(new_qty)
            return new_qty_as_int
        except ValueError:
            print("Please enter a number.")

def add_new_book_to_book_records(last_book_record_id):
    last_book_record_id
            

def get_valid_id(input_message):
    is_id_in_db = False
    while True:
        user_id_input = input(input_message)
        try:
            user_id_input_as_int = int(user_id_input)
            for i in range(0, len(book_records)):
                if user_id_input_as_int == book_records[i][0]:
                    is_id_in_db = True
                    valid_id = user_id_input_as_int
                    return valid_id
            if is_id_in_db == False:
                print(f"{user_id_input_as_int} is not a valid ID.")
        except ValueError:
            print("Please enter a number.")


def get_user_edit_or_search_option(user_edit_or_search_input_prompt):
    while True:
        user_edit_or_search_option = input(user_edit_or_search_input_prompt)

        if user_edit_or_search_option == "1":
            user_edit_or_search_option = "title"
            return user_edit_or_search_option
        
        elif user_edit_or_search_option == "2":
            user_edit_or_search_option = "author"
            return user_edit_or_search_option
        
        elif user_edit_or_search_option == "3":
            user_edit_or_search_option = "qty"
            return user_edit_or_search_option
        
        elif user_edit_or_search_option == "4":
            user_edit_or_search_option = 4
            return user_edit_or_search_option
        
        else:
            print("\nPlease enter a valid option.")

# Get a valid number for qty data category.
def is_new_qty_int(new_qty_input):
    while True:
        try:
            new_qty_input_cast = int(new_qty_input)
            return new_qty_input_cast
        except ValueError:
            new_qty_input = input("Please enter a number: ")


def update_book(user_edit_option, new_user_data, valid_id):
    if user_edit_option != "qty":
        cursor.execute(f'''UPDATE ebookstore 
                    SET {user_edit_option} = '{new_user_data}'
                    WHERE id = {valid_id}''')
    else:
        cursor.execute(f'''UPDATE ebookstore 
                    SET {user_edit_option} = {new_user_data}
                    WHERE id = {valid_id}''')
    db.commit()


def confirm_book_in_question(valid_id):
    for i in range(0, len(book_records)):
        if valid_id == book_records[i][0]:
            title_in_question = book_records[i][1]
            return title_in_question
        

def delete_book(valid_id):
    cursor.execute(f'''DELETE FROM ebookstore
                   WHERE id = {valid_id}''')
    db.commit()
    

def search_books(user_search_input, user_search_by_option):
    if user_search_by_option == "qty":
        cursor.execute(f'''SELECT * FROM ebookstore 
                       WHERE {user_search_by_option} = {user_search_input} ''')
    else:                                            
        cursor.execute(f'''SELECT * FROM ebookstore 
                       WHERE {user_search_by_option} = '{user_search_input}' ''')
    
    user_search_result = cursor.fetchall()
    return user_search_result

def display_book_details(user_search_result):
    if user_search_result == []:
        print("\nNo results.")
    else:
        print(f'''\n\tBook ID: {user_search_result[0]}
    Book Title: {user_search_result[1]}
    Book Author: {user_search_result[2]}
    Book Quantity: {user_search_result[3]}''')



# Main script.
while True:
    user_input = input('''\n        Main Menu
\nPlease select an option:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit

    Enter selection: ''')
    # Enter book
    if user_input == "1":
        # Get new book details.
        new_record_id = generate_new_id(book_records)
        new_title = get_title_from_user()
        new_author = get_author_from_user()
        new_qty_cast = get_qty_from_user(new_title)
        
        # Add new book details to database
        cursor.execute('''INSERT INTO ebookstore(id,title,author,qty)
                       VALUES(?,?,?,?)''', 
                       (new_record_id,new_title,new_author,new_qty_cast))
        db.commit()

        print(f"\n{new_title} has been added to the database!")

        book_records.append((new_record_id,new_title,new_author,new_qty_cast))


    # Update book
    elif user_input == "2":
        valid_id = get_valid_id(get_id_to_update_book)
        title_to_update = confirm_book_in_question(valid_id)
        print(f"You have selected to edit {title_to_update}")

        # Get data category that user wants to edit, e.g. title.
        user_edit_option = get_user_edit_or_search_option(get_user_edit_option)
        if user_edit_option != 4:
            # Get new value for the category, e.g. The Hunger Games
            new_user_data = input(f"\nPlease enter a new {user_edit_option}: ")
            if user_edit_option == "qty":
                # If user opts to edit quantity, get valid number.
                new_user_data = is_new_qty_int(new_user_data) 
            update_book(user_edit_option, new_user_data, valid_id)
            print("\nBook updated successfully.")

        
    # Delete book
    elif user_input == "3":
        valid_id = get_valid_id(get_id_to_delete_book)
        title_to_delete = confirm_book_in_question(valid_id)
        # Ask user to confirm whether they want to delete book.
        while True:
            user_input = input(f'''\nWould you like to delete {title_to_delete} from the database?
    
    Enter selection: ''').lower()
            if user_input == "y" or user_input == "yes":
                delete_book(valid_id)
                print(f"\n{title_to_delete} has been deleted from the database.")
                break
            elif user_input == "n" or user_input == "no":
                print(f"\n{title_to_delete} has not been deleted from the database.")
                break
            else:
                print("\nPlease try again")


    # Search books.
    elif user_input == "4":
        # Get the category user wants to search books by, e.g. qty
        user_search_by_option = get_user_edit_or_search_option(get_user_search_option)
        if user_search_by_option != 4:
            # Get a value of that category, e.g. 10.
            user_search_input = input(f"\nPlease enter the {user_search_by_option}: ")
            if user_search_by_option == "qty":
                user_search_input = is_new_qty_int(user_search_input) 
            # Select books in the database matching users criteria and print.
            user_search_result = search_books(user_search_input, user_search_by_option)
            display_book_details(user_search_result[0])


    elif user_input == "0":
        print("\nGoodbye!")
        break
    

    else:
        print(f"\n{user_input} is not a valid option.")


