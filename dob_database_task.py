# Ask user: do you want to find information, add information or remove information?

find = True
remove = False
invalid_entry = True
while invalid_entry == True:
    read_or_write = input("Do you want to find information(f), add information(a) or remove information(r)? ")
    match read_or_write:
        case "f":
            find = True
            invalid_entry = False
        case "a":
            find = False
            remove = False
            invalid_entry = False
        case "r":
              remove = True
              find = False
              invalid_entry = False
        case _:
            print("You did not enter a valid option.")

# Find:

invalid_character = True
is_name_in_list = False
name_entered_by_user = ""
month_list = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
month_list_index = 0

if find == True:
    f = open("DOB.txt", "r")
    user_name_input = input("Enter the first name of the person whose info you want: ")
    for line in f:
        line_split = line.split(" ")
        if line_split[0].lower() == user_name_input.lower():
            is_name_in_list = True
            matching_details = line
            details_as_list = matching_details.split()

    if is_name_in_list == False:
        print("This name isn't in the list.")

    # Convert month as word into a number.
    if is_name_in_list == True:
        for i in range(0, len(month_list)):
            if month_list[i] == details_as_list[3]:
                month_number = i+1
        
    # If name is in the database, ask which details to display.
    while invalid_character == True and is_name_in_list == True:
                    user_choice = input("Do you want full name (f), date of birth (d)," 
                                        " initials (i) or everything (e)? ")
                    match user_choice:
                        case "f":
                            print(details_as_list[0] + " " + details_as_list[1])            
                            invalid_character = False
                        case "d":
                            print(str(details_as_list[2]) + "/" + str(month_number) + "/" + str(details_as_list[4][2:]))
                            invalid_character = False
                        case "i":
                            print(details_as_list[0][0] + details_as_list[1][0])
                            invalid_character = False
                        case "e":
                            print(matching_details)
                            invalid_character = False
                        case _:
                            print("Not a valid input.")
                            invalid_character = True
            
    

# Add:
all_lines = ""
f = open("DOB.txt", "r")
for line in f:
    all_lines += line

invalid_data = True
if find == False and remove == False:
    while invalid_data == True:
        user_data_input = input("Please enter 'firstname surname date month year' in this format: ")
        user_data_input_titled = user_data_input.title()
        user_data_input_as_list = user_data_input_titled.split(" ")
        if len(user_data_input_as_list) == 5:
            with open("DOB.txt", "w") as f:
                f.write(all_lines + "\n" + user_data_input_titled)
            print(f"{user_data_input_titled} has been Successfully added to the database")
            invalid_data = False
        else:
            print("Please make sure to use the specified formatting.")

# Remove:

name_in_database = False
invalid_name = True
if remove == True:
    while invalid_name == True:
        info_to_remove_user_input = input("Please enter the first name of the person" 
                                        " whose information you would like to remove: ")
        f = open("DOB.txt", "r+")
        for line in f:
                line_split = line.split(" ")
                if line_split[0].lower() == info_to_remove_user_input.lower():
                    line_to_remove = line
                    line_to_remove_split = line_to_remove.split(" ")
                    invalid_name = False
                    name_in_database = True
    if name_in_database == False:
        print("This name isn't in the database.")

invalid_input = True
if remove == True:
    while invalid_input:
        remove_choice = input("Would you like to remove " + "\033[1m" + 
                            line_to_remove.strip("\n").title() + "\033[0m" + "? (y or n) ")
        match remove_choice:
            case "y":
                with open("DOB.txt", "r") as f:
                    lines = f.readlines()
                with open("DOB.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != line_to_remove.strip("\n"):
                            f.write(line)
                print(f"{line_to_remove_split[0].title()} {line_to_remove_split[1].title()} 
                      has been removed from the file.")
                invalid_input = False
            case "n":
                print(f"{line_to_remove_split[0].title()} {line_to_remove_split[1].title()} 
                      has not been removed from the file.")
                invalid_input = False
            case _:
                print("You did not enter a valid input.") 






f.close()  

