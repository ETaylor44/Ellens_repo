# This is the central script for my admin program. The branches of the program are imported as libraries.
# Here user enters a username and password, and choose a branch of the program. The main function from the corresponding library is then called.

import email
import dob_database_manager 
import task_manager

username_prompt = "\nPlease enter your username: "
password_prompt = "Please enter your password: "
error_message = "\nYour username or password is incorrect. Please try again."
error_message_two = "\nOops - Please try again."

# Get username and password input.
def get_username_password_input(username_input_prompt, password_input_prompt):
    while True:
        username_input = input(username_input_prompt)
        password_input = input(password_input_prompt)
        return username_input, password_input

# Read user.txt to see if username and password match existing ones.
def read_txt_file(username_input, password_input, error_message):
    f = None
    try: 
        with open("user.txt", "r", encoding='utf-8') as f:
            all_data = f.readlines()
            for line in all_data:
                data_as_list = line.split(", ")
                if data_as_list[0] == username_input and data_as_list[1].strip("\n") == password_input:
                    return username_input, password_input
            # If no match, recall get_username_password_input function.
            print(error_message)
            return get_username_password_input(username_prompt, password_prompt)
    except FileNotFoundError:
        print("Please open the user text file.")
    finally:
        if f is not None:
            f.close()

def get_user_input(error_message):
    while True:
        user_input = input('''\n\033[0mSelect one of the following options:
    1. view emails
    2. enter task manager
    3. enter date of birth database manager
    4. logout
                           
Enter selection: ''').lower()
        if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":
            return user_input
        else:
            print(error_message)


# Script.  
# Get valid username and password from user.               
username_password = get_username_password_input(username_prompt, password_prompt)
read_txt_file(username_password[0], username_password[1], error_message)

# Display menu and get valid user input.
print("\n\033[1mMain Menu")
user_input = get_user_input(error_message_two)

if user_input == "1":
    user_selection = "view emails."
    email.run_emails()
    user_input = get_user_input(error_message_two)

elif user_input == "2":
    user_selection = "enter task manager."
    task_manager.run_task_manager(username_password[0])
    user_input = get_user_input(error_message_two)

elif user_input == "3":
    user_selection = "enter date of birth database manager."
    dob_database_manager.run_dob_database_manager()
    user_input = get_user_input(error_message_two)

else:
    print("\nGoodbye!")

    
