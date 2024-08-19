def run_dob_database_manager():

    import datetime
    import csv
    import os

    month_list = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]
    main_menu_list = ["find information", "add information", "remove information", "exit"]
    find_menu_list = ["full name", "date of birth", "initials", "age", "all details", "cancel"]
    data_headers = ["first name", "surname", "day", "month", "year"]
    yes_or_no = ["Yes", "No"]

    menu_output = "\nPlease choose an option:"
    
    def is_csv_open():
        if(os.path.isfile("dob.csv")):
            return True
        else:
            return False
        
    def get_menu_choice(menu_list, menu_first_line):
        for index, item in enumerate(menu_list, 1):
            menu_first_line += f"\n{index}. {item}"
        user_input = input(f"{menu_first_line}\n\nEnter selection: ")
        return user_input


    def get_valid_name(name_input):
        while True:
            with open('dob.csv', "r") as csv_file:
                all_data = csv.DictReader(csv_file) 
                for line in all_data:
                    if line["first name"].lower() == name_input.lower():
                        return line
                name_input = input('''This name isn't in the database.
Please try again: ''')
                
    def get_full_name(all_details):
        full_name = f"{all_details["first name"]} {all_details["surname"]}"
        return full_name

    # Convert month as word into a number.
    def convert_month_word_to_number(all_details):
        for i in range(0, len(month_list)):
            if month_list[i] == all_details["month"]:
                month_number = i+1
                return month_number
    
    def calculate_age(born):
        today = datetime.datetime.now()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age 
    
    def get_details_to_add(data_headers):
        new_row_dict = {}
        while True:
            for header in data_headers:
                entry_data = input(f"Please enter the {header}: ")
                entry_data = is_entry_valid(entry_data, header)
                new_row_dict[header] = entry_data

            return new_row_dict

    def is_entry_valid(entry_data, header):
        if header in ["first name", "surname"]:
            while True: 
                if len(entry_data) < 0 or len(entry_data) > 15:
                    entry_data = input("Too many characters. Please try again: ")
                else: 
                    return entry_data
                    
        elif header == "day":
            while True:
                try:
                    entry_data = int(entry_data)
                    if entry_data < 1 or entry_data > 31:
                        entry_data = input("Please enter a valid number: ")
                    else:
                        return entry_data
                except ValueError:
                    entry_data = input("Please enter a number: ")

        elif header == "month":
            while True:
                try:
                    # If user enters number, check validity then convert to month as string.
                    entry_data = int(entry_data)
                    if entry_data < 1 or entry_data > 12:
                        entry_data = input("Please enter a valid number")
                    else:
                        entry_data = convert_month_int_to_string(entry_data)
                        return entry_data
                    # If user enters month as string, 
                    # check if first 3 characters are equal to first 3 characters of any month in month_list.
                except ValueError:
                    for month in month_list:
                        if entry_data.lower()[:3] == month.lower()[:3]:
                            return entry_data
                    entry_data = input("Please try again: ")

        else:
            while True:
                try:
                    entry_data = int(entry_data)
                    if entry_data < 1 or entry_data > 2024:
                        entry_data = input("Please enter a valid year: ")
                    else:
                        return entry_data
                except ValueError:
                    entry_data = input("Please enter a number: ")

    def convert_month_int_to_string(entry_data):
        for i in range(0, len(month_list)):
            if i+1 == entry_data:
                entry_data = month_list[i]
                return entry_data


    def add_to_csv(row_dict):
        with open('dob.csv', 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data_headers)
            writer.writerow(row_dict)
        print("\nNew data added to the database!")


# Script.
    if is_csv_open() == False:
        print("Error. Please open the Date of Birth Database.")
    else:
    # Get valid user input.
        while True:
            user_input = get_menu_choice(main_menu_list, menu_output)
            # Find details.
            if user_input == "1":
                name_input = input("\nEnter the first name of the person whose info you want: ")
                all_details = get_valid_name(name_input)
                while True:
                    # Ask which details to display.
                    find_menu_input = get_menu_choice(find_menu_list, menu_output)

                    # Display full name.
                    if find_menu_input == "1":
                        full_name = get_full_name(all_details)
                        print(f"\nFull name: {full_name}")   

                     # Display dob (dd/mm/yyyy)      
                    elif find_menu_input == "2":
                        print(f"\nDate of birth: {str(all_details["day"])} " 
                              f"{all_details["month"]} {str(all_details["year"])}")

                    # Display initals.
                    elif find_menu_input == "3":
                        print(f"\nInitials: {all_details["first name"][0]}{all_details["surname"][0]}")

                    # Display age.
                    elif find_menu_input == "4":
                        month_number = convert_month_word_to_number(all_details)
                        formatted_dob = datetime.datetime(int(all_details["year"]), int(month_number), int(all_details["day"]))
                        age = calculate_age(formatted_dob)
                        print(f"\nAge: {age} years old.")

                    # Display all details as string.
                    elif find_menu_input == "5":
                        details_as_string = ""
                        for key in all_details:
                            details_as_string += f"{all_details[key]} "
                        print(f"\n{details_as_string}")
                    
                    # Cancel.
                    elif find_menu_input == "6":
                        break

                    else:
                        print("Not a valid input.")
                    break

                # Add details.
            elif user_input == "2":

                new_row_dict = get_details_to_add(data_headers)
                add_to_csv(new_row_dict)


                # Remove details.
            elif user_input == "3":
                name_input = input("\nEnter the first name of the person whose information to remove: ")
                all_details = get_valid_name(name_input)

                full_name = get_full_name(all_details)

                confirmation_message = f"\nWould you like to remove\033[1m {full_name}\033[0m from the database?"
                
                while True:
                    remove_choice = get_menu_choice(yes_or_no, confirmation_message)
                    if remove_choice == "1":

                        data_from_file = []

                        with open("dob.csv", mode="r") as csv_file:
                            file_reader = csv.DictReader(csv_file)
                            for row in file_reader:
                                data_from_file.append(row)


                        with open("dob.csv", "w") as csv_file:
                            writer = csv.DictWriter(csv_file, fieldnames=data_headers)
                            writer.writeheader()
                            for row in data_from_file:
                                if row["first name"].lower() != all_details["first name"].lower():
                                    writer.writerow(row)

                        print(f"\n{full_name} has been removed from the database.")
                        break
                    else:
                        print(f"\n{full_name} has not been removed from the database.")
                        break
                
            elif user_input == "4":
                print("\nGoodbye!.")
                break
                            
            else:
                print("\nYou did not enter a valid option.")




