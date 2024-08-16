# A program which takes 2 numbers and an arithmetic operator from the user. It then performs the calculation and stores the equation in a text file. 
# The user can view all previous calculations stored in the text file.

# Variable list.
perform_or_view_message = '''\nPlease choose an option:
    1 - Perform a calculation
    2 - View previous calculations
    e - Exit

Enter selection: '''
error_message = "Please try again."
ask_for_number = "Please enter a number: "
not_an_int_message = "This is not a valid number. "
ask_for_another_number = "Please enter another number: "
ask_for_operation = "\nWould you like to add(+), subtract(-), multiply(*) or divide(/)? "
operation_error = "Please enter a valid mathematical operation."
alternative_num_message = "Please enter a different number to divide by: "
run_calculator = True

# Get valid user input and store in a variable.
def user_perform_or_view(question, error_message):
    while True:
        user_input = input(question)
        if user_input == "1":
            print("You have selected the 'perform calculation' option.\n")
            return user_input
        elif user_input == "2":
            print("\nPrevious calculations:\n")
            return user_input
        elif user_input.lower() == "e":
            return user_input.lower()
        else:
            print(error_message)

# Get valid user input and cast to float.
def get_number_input(question, error_message):
    while True:
        user_input = input(question)
        try:
            user_number = float(user_input)
            return user_number
        except ValueError:
            print(error_message)

# Get operation from user and call corresponding function.
def get_operation_input(question, error_message):
    while True:
        user_operation = input(question)
        match user_operation:
            case "+":
                print("You have selected addition.")
                addition_func(user_number_a, user_number_b, user_operation)
                return user_operation
            case "-":
                print("You have selected subtraction.")
                subtraction_func(user_number_a, user_number_b, user_operation)
                return user_operation
            case "*":
                print("You have selected multiplication.")
                multiply_func(user_number_a, user_number_b, user_operation)
                return user_operation
            case "/":
                print("You have selected division.")
                divide_func(user_number_a, user_number_b, user_operation)
                return user_operation
            case _:
                print(error_message)

# Functions to perform mathematical operations.
def addition_func(user_number_a, user_number_b, user_operation="+"):
    answer = user_number_a + user_number_b
    print_equation(answer, user_operation, user_number_a, user_number_b)

def subtraction_func(user_number_a, user_number_b, user_operation="-"):
    answer = user_number_a - user_number_b
    print_equation(answer, user_operation, user_number_a, user_number_b)


def multiply_func(user_number_a, user_number_b, user_operation="*"):
    answer = user_number_a * user_number_b
    print_equation(answer, user_operation, user_number_a, user_number_b)

def divide_func(user_number_a, user_number_b, user_operation="/"):
    # While loop to prevent error if user tries to divide by 0.
    while user_number_b == 0:
        print("You cannot divide by 0")
        user_number_b = get_number_input(alternative_num_message, not_an_int_message)
    answer = user_number_a / user_number_b
    print_equation(answer, user_operation, user_number_a, user_number_b)
    
# Prints users equation.
def print_equation(answer, user_operation, user_number_a, user_number_b):
    answer = check_if_decimal(answer)
    user_number_a = check_if_decimal(user_number_a)
    user_number_b = check_if_decimal(user_number_b)
    equation = f"{user_number_a} {user_operation} {user_number_b} = {answer}"
    print(equation)
    write_to_txt_file(equation)

# Cast answer to integer if it's a whole number.
def check_if_decimal(answer):
    if int(answer) == answer:
        return int(answer)
    else:
        return answer

# Store calculations in a text file.
def write_to_txt_file(equation):
    f = open("equations.txt", "a")
    f.write(equation + "\n")
    f.close()

# Print the text files or error message if file not found.
def read_txt_file():
    f = None
    try: 
        f = open("equations.txt", "r", encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("You have not made any previous calculations.")
    finally:
        if f is not None:
            f.close()

# Programme script.
print("\nThis programme will allow you to perform calculations or view previous calculations.")

while run_calculator == True:
    user_input = user_perform_or_view(perform_or_view_message, error_message)
    if user_input == "1":
        user_number_a = get_number_input(ask_for_number, not_an_int_message)
        user_number_b = get_number_input(ask_for_another_number, not_an_int_message)
        user_operation = get_operation_input(ask_for_operation, operation_error)
    elif user_input == "2":
        read_txt_file()
    else:
        print("\nGoodbye!")
        run_calculator = False


