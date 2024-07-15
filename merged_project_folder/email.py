    
def email_programme_function():
    # Define class, method and create attributes.
    class Email():
        has_been_read = False
        def __init__(self, email_address, subject_line, email_content):
            self.email_address = email_address
            self.subject_line = subject_line
            self.email_content = email_content
            
        def mark_as_read(self):
            self.has_been_read = True

    inbox_list = []
    prompt_message = "\nPlease enter the number of the email to view: "

    #Functions.
    # Print emails in inbox when programme starts.
    def populate_inbox():
        email_one = Email("ellen.t845@gmail.com", "Classes", "Instructions")
        email_two = Email("callum.t845@gmail.com", "Pasta", "Recipe")
        email_three = Email("help@gmail.com", "FAQ", "How to use classes")
        inbox_list.extend([email_one, email_two, email_three])
        return inbox_list
        
    # List subject lines of emails with a corresponding number.
    def list_emails(inbox_list):
        subject_list = []
        index = 0
        for email in inbox_list:
            subject = email.subject_line
            subject_list.append(subject)
            print(index, subject)
            index += 1
        return subject_list


    def read_email(index):
        print(f"\nEmail Sender:\t{inbox_list[index].email_address}")
        print(f"Subject Line:\t{inbox_list[index].subject_line}")
        print(f"Email Content:\t{inbox_list[index].email_content}")
        inbox_list[index].has_been_read = True


    def get_user_input(prompt_message):
        while True:
            is_number_an_email = False
            user_input = input(prompt_message)
            # Check whether user_input is a number
            try:
                user_input_as_num = int(user_input)
                # Check whether user_number corresponds to any of the emails in inbox.
                for i in range(0, len(subject_list)):
                    if i == user_input_as_num:
                        is_number_an_email = True
                        return user_input_as_num
            except ValueError:
                print("\nOops - Please enter a number.")
                is_number_an_email = True
            if is_number_an_email == False:
                print("\nOops - Please try again.")
            
                

    # Script.
    print("\nInbox:")
    populate_inbox()
    subject_list = list_emails(inbox_list)

    while True:
        user_choice = input('''\nWould you like to:
    r - read an email
    v - view unread emails
    e - exit 

    Enter selection: ''')
        
        if user_choice == "r":
            # Call function to get valid user input.
            user_input = get_user_input(prompt_message)
            read_email(user_input)
            
        elif user_choice == "v":
            print("\nUnread Emails:")
            # Identify emails which are unread and print subject lines.
            for index in range(0, len(inbox_list)):
                if inbox_list[index].has_been_read != True:
                    print(inbox_list[index].subject_line)
                
        elif user_choice == "e":
            print("\nGoodbye!")
            return 

        else:
            print("\nOops - Please try again.")



