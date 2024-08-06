    
def dob_database_manager_func():

    import datetime

    month_list = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]
    
    def is_txt_file_open():
        try:
            f = open("dob.txt", "r")
            is_file_open = True
        except Exception as e:
            is_file_open = False
        return is_file_open

    # Define function to find data and return as list..
    def find_function():
        while True:
            name_input = input("\nEnter the first name of the person whose info you want: ")
            with open("DOB.txt", "r") as f:
                all_data = f.readlines()
                for line in all_data:
                    details_as_list = line.split(" ")
                    if details_as_list[0].lower() == name_input.lower():
                        return details_as_list
                print("This name isn't in the list.")

    # Convert month as word into a number.
    def convert_month_word_to_number(details_as_list):
        for i in range(0, len(month_list)):
            if month_list[i] == details_as_list[3]:
                month_number = i+1
                return month_number
    
    def calculate_age(born):
        today = datetime.datetime.now()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age 


    def get_valid_name_to_remove():
        while True:
            info_to_remove_user_input = input("\nPlease enter the first name of the person" 
                                            " whose information you would like to remove: ")
            f = open("DOB.txt", "r+")
            for line in f:
                line_split = line.split(" ")
                if line_split[0].lower() == info_to_remove_user_input.lower():
                    line_to_remove = line
                    return line_to_remove
            print("This name isn't in the database.")


    def confirm_removal(line_to_remove):
        while True:
            remove_choice = input(f'''\nWould you like to remove\033[1m {line_to_remove.strip("\n")}\033[0m? (y or n) 
                    
            Enter selection: ''').lower()
            match remove_choice:
                case "y":
                    return remove_choice
                case "n":
                    return remove_choice
                case _:
                    print("You did not enter a valid input.") 
    

    # Script.
    is_file_open = is_txt_file_open()
    if is_file_open == False:
        print("Error. Please open the Date of Birth Database.")
    else:
    # Get valid user input.
        while True:
            user_input = input('''\nPlease select one of the following options:
                f - find information
                a - add information
                r - remove information
                e - exit date of birth database manager

                Enter selection: ''')
            match user_input:

                # Find details.
                case "f":
                    # Get valid first name from user.
                    details_as_list = find_function()
                    # Ask which details to display.

                    while True:
                        user_choice = input('''\nWould you like to view:
        f - full name
        i - initials
        d - date of birth
        a - age
        ad - all details

        Enter selection: ''')
                        match user_choice:
                            # Display full name.
                            case "f":
                                print(f"\nFull name: {details_as_list[0]} {details_as_list[1]}")   
                                break   
                            # Display dob (dd/mm/yyyy)      
                            case "d":
                                month_number = convert_month_word_to_number(details_as_list)
                                print(f"\nDate of birth: {str(details_as_list[2])}/{str(month_number)}/{str(details_as_list[4])}")
                                break
                            # Display initals.
                            case "i":
                                print(f"\nInitials: {details_as_list[0][0]}{details_as_list[1][0]}")
                                break
                            # Display age. Not working correctly
                            case "a":
                                month_number = convert_month_word_to_number(details_as_list)
                                formatted_dob = datetime.datetime(int(details_as_list[4]), int(month_number), int(details_as_list[2]))
                                age = calculate_age(formatted_dob)
                                print(f"\nAge: {age} years old.")
                            # Display all details as string.
                            case "ad":
                                details_as_string = " ".join(details_as_list)
                                print(f"\n{details_as_string}")
                                break
                            case _:
                                print("Not a valid input.")


                # Add details.
                case "a":
                    all_lines = ""
                    f = open("DOB.txt", "r")
                    for line in f:
                        all_lines += line

                    # TO DO: enter first name, surname, date, month, year as separate inputs.
                    while True:
                        user_data_input = input("\nPlease enter 'firstname surname date month year' in this format: ")
                        user_data_input_titled = user_data_input.title()
                        user_data_input_as_list = user_data_input_titled.split(" ")
                        if len(user_data_input_as_list) == 5:
                            with open("DOB.txt", "w") as f:
                                f.write(all_lines + "\n" + user_data_input_titled)
                            print(f"\n\033[1m{user_data_input_titled}\033[0m has been Successfully added to the database")
                            break
                        else:
                            print("\nPlease make sure to use the specified formatting.")


                # Remove details.
                case "r":
                    line_to_remove = get_valid_name_to_remove()
                    remove_choice = confirm_removal(line_to_remove)
                    line_to_remove_as_list = line_to_remove.split(" ")
                    if remove_choice == "y":
                        with open("DOB.txt", "r") as f:
                            lines = f.readlines()
                        with open("DOB.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != line_to_remove_as_list.strip("\n"):
                                    f.write(line)
                        print(f"\n{line_to_remove_as_list[0].title()} {line_to_remove_as_list[1].title()}"
                            " has been removed from the file.")
                    else:
                        print(f"\n{line_to_remove_as_list[0].title()} {line_to_remove_as_list[1].title()}"
                            " has not been removed from the file.")
                
                case "e":
                    print("\nYou are exiting the DOB database manager.")
                    break
                            
                case _:
                    print("\nYou did not enter a valid option.")

        #function GetUserStringInput (string question)
        #   ask question
        #   get valid user input (while loop)
        #   return user input

        #function GetUserIntInput (string question)
        #   same as previous, but validate for int

        #function GetAllInfoForOnePerson(int id)
        #   firstName = GetUserStringInput("What is the first name?")
        #   secondName = GetUserStringInput("What is the second name?")
        #   age = GetUserIntInput("What is the age?")

