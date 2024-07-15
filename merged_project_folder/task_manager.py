def task_manager_func(username):
    import datetime 

    # Variables.
    invalid_date_message = "Please enter a valid date using the format given."

    # Functions
    # Return valid date.
    def get_valid_date(invalid_date_message):
        while True:
            task_deadline = input("Please enter a deadline for the task in the format dd/mm/yyyy: ")
            date_deadline = task_deadline[:2]
            month_deadline = task_deadline[3:5]
            year_deadline = task_deadline[6:]
            if len(task_deadline) == 10 and task_deadline[2] == "/" and task_deadline[5] == "/":
                try:
                    date_deadline_as_int = int(date_deadline)
                    month_deadline_as_int = int(month_deadline)
                    year_deadline_as_int = int(year_deadline)
                    if date_deadline_as_int < 32 and month_deadline_as_int < 13 and year_deadline_as_int > 2023:
                        return task_deadline
                    else:
                        print(invalid_date_message)
                except ValueError:
                    print(invalid_date_message)
            else:
                print(invalid_date_message)

    # Script.                 
    # Display different menus depending on whether user is 'admin'.
    while True:
        if username == "admin":
            menu = input('''\nSelect one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - view statistics
    e - exit
                        
    Enter selection: ''').lower()
        else:
            menu = input('''\nSelect one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
                         
    Enter selection: ''').lower()

        # Register new user.
        if menu == 'r':
            do_passwords_match = False
            # Get new username and password from user and write to text file.
            new_username = input("\nPlease enter a new username: ")
            while do_passwords_match == False:
                new_password = input("Please enter a new password: ")
                password_confirmation = input("Please re-enter the password: ")
                if new_password == password_confirmation:
                    with open("user.txt", "a") as f:
                        f.write(f"\n{new_username}, {new_password}")
                    print("\nYou have successfully added a new user.")
                    do_passwords_match = True
                else:
                    print("The passwords do not match.")

        # Add new task and write to text file.
        elif menu == 'a':
            invalid_username = True
            # Get valid username input from user.
            while invalid_username == True:
                task_username = input("\nWho is this task for? Please enter their username: ")
                with open("user.txt", "r") as f:
                    all_data = f.readlines()
                    for line in all_data:
                        data_as_list = line.split(", ")
                        if data_as_list[0] == task_username:
                            invalid_username = False
                if invalid_username == True:
                    print("This username does not exist.")    

            # Get task details from user.
            task_title = input("Please enter a task title: ")
            task_description = input("Please enter a description of the task: ")
            task_deadline = get_valid_date(invalid_date_message)
            current_date = datetime.datetime.today().strftime('%m/%d/%Y')
            is_complete = "No"

            with open("tasks.txt", "a") as f:
                f.write(f"\n{task_username}, {task_title}, {task_description}, "
                        f"{current_date}, {task_deadline}, {is_complete}")
            print("\nTask added.")

        # Display all tasks using a readable format.
        elif menu == 'va':
            with open("tasks.txt", "r") as f:
                all_lines = f.readlines()
                for line in all_lines:
                    line_as_list = line.split(", ")
                    print(f"\nTask:\t\t\t{line_as_list[1]}\nAssigned to:\t\t{line_as_list[0]}\n"
                        f"Date assigned:\t\t{line_as_list[3]}\nDue date:\t\t{line_as_list[4]}\n"
                        f"Task complete?:\t\t{line_as_list[5].strip("\n")}\nTask description: \n "
                        f"{line_as_list[2]}\n")

        # Display the tasks of the user using a readable format.
        elif menu == 'vm':
            i = 0
            with open("tasks.txt", "r") as f:
                all_lines = f.readlines()
                for line in all_lines:
                    line_as_list = line.split(", ")
                    if line_as_list[0] == username:
                        i += 1
                        print(f"\nTask:\t\t\t{line_as_list[1]}\nAssigned to:\t\t{line_as_list[0]}\n"
                        f"Date assigned:\t\t{line_as_list[3]}\nDue date:\t\t{line_as_list[4]}\n"
                        f"Task complete?:\t\t{line_as_list[5].strip("\n")}\nTask description: \n "
                        f"{line_as_list[2]}")
                if i == 0:
                    print("\nYou have no tasks to complete.")

        # Read each text file and display statistics in a readable format.
        elif menu == 's':
            with open("tasks.txt", "r") as f:
                all_lines = f.readlines()
                i = 0
                for line in all_lines:
                    i += 1
            with open("user.txt", "r") as f:
                all_lines = f.readlines()
                j = 0
                for line in all_lines:
                    j += 1
                print(f"\nTotal number of tasks:\t\t{i}\nTotal number of users:\t\t{j}")

        elif menu == 'e':
            print('\nGoodbye!')
            break

        else:
            print("\nOops - Please try again.")


            
