# This program was created during my work for a youth orchestra in preparation for and during a residential course.
# We needed up-to-date daily registers for mealtimes, orchestral rehearsals and other intervals throughout the day, each containing different information.
# Using a central excel file, I pulled the required columns, stored them in a database and wrote them to csv's to create custom registers.

import csv
import sqlite3
import os

# Variables:

membership_permissions_csv = "NOFA 2023 24 Membership Permissions .csv"
db_filename = "NOFA_member_info.db"
# membership_permissions_csv_columns_needed = ["House Group", "Young person's first name", 
#                 "Young person’s surname", "Young person’s pronouns", "SP2024 Room Number", 
#                 "If yes, please give more information. This includes any allergies to medication.", 
#                 "Medication time", "If yes, please give us more information.", "Small Sectional",
#                 "Which instrument will your young person play in NOFA?"]

# Does database exist?
if(os.path.isfile(db_filename)):
    os.remove(db_filename)
    
db = sqlite3.connect(db_filename)

def create_table(db, db_columns, db_title):
    cursor = db.cursor()
    cursor.execute(f'''
        CREATE TABLE {db_title}({db_columns})''')
    db.commit()
    return cursor


# Read membership permissions csv file.
def read_csv_file(csv_filename, db_title, membership_permissions_csv_columns_needed, columns, row_length):
    with open(csv_filename, "r", encoding='UTF-8') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            useful_data_as_tuple = []
            if row["Attending summer 2024"].lower() == "yes":
                for column_header in membership_permissions_csv_columns_needed:
                    useful_data_as_tuple.append(row[column_header])

                # Insert data into database.
                cursor.execute(f'''
                            INSERT INTO {db_title} ({columns})
                            VALUES ({row_length})''', useful_data_as_tuple)
                
        db.commit()

# Create new CSV and write data for each house.
def write_csv_file(db_title, new_csv, list_of_csv_columns, upper_range, user_input, list_of_small_sectionals):

    for i in range(1, upper_range):
        if user_input == "1":
            cursor.execute(f'''SELECT * FROM {db_title}
                            WHERE house = {i}''')
            j = "_" + str(i)
        elif user_input == "3":
            cursor.execute(f'''SELECT * FROM {db_title}
                            WHERE small_sectional = '{list_of_small_sectionals[i-1]}' ''')
            j = "_" + list_of_small_sectionals[i-1]
        else:
            cursor.execute(f'''SELECT * FROM {db_title}''')
            j = ''
        students = cursor.fetchall()
        with open(f"{new_csv}{j}.csv", "w", encoding='UTF-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(list_of_csv_columns)
            for student in students:
                csv_writer.writerow(student)


while True:
    user_input = input('''Which register would you like to generate? 
                       
    1 - House registers
    2 - Dinner register
    3 - Small sectional registers
                       
    Enter selection: ''')

    if user_input == "1":
        db_columns = "house INTEGER, first_name VARCHAR, surname VARCHAR, pronouns VARCHAR, room_number INT, allergies VARCHAR, medication VARCHAR"
        db_title = "houses"
        membership_permissions_csv_columns_needed = ["House Group", "Young person’s preferred name", 
                                                     "Young person’s surname", "Young person’s pronouns", 
                                                     "SP2024 Room Number", 
                                                     "If yes, please give more information. This includes any allergies to medication.", "Medication time"]
        row_length = "?,?,?,?,?,?,?"
        columns = "house,first_name,surname,pronouns,room_number,allergies,medication"
        new_csv = f"house_registers"
        list_of_csv_columns = ["House", "First name", "Surname", "Pronouns", "Room", 
                             "Allergies", "Medication", "Afternoon register", "Evening register"]
        upper_range = 8
        list_of_small_sectionals = []
        break

    elif user_input == "2":
        db_columns = "first_name VARCHAR, surname VARCHAR, room INT, dietaries VARCHAR, allergies VARCHAR"
        db_title = "dietaries"
        membership_permissions_csv_columns_needed = ["Young person’s preferred name", "Young person’s surname", "SP2024 Room Number",  
                                                     "If yes, please give us more information.", 
                                                     "If yes, please give more information. This includes any allergies to medication."] 
        row_length = "?,?,?,?,?"        
        columns = "first_name,surname,room,dietaries,allergies"
                                   
        new_csv = "dinner_register"
        list_of_csv_columns = ["First name", "Surname", "room", "dietaries", "allergies", ""]
        
        upper_range = 2
        list_of_small_sectionals = []

        break

    elif user_input == "3":
        db_columns = "small_sectional CHAR, first_name VARCHAR, surname VARCHAR, pronouns VARCHAR, instrument CHAR"
        db_title = "small_sectionals"
        membership_permissions_csv_columns_needed = ["Small Sectional", "Young person’s preferred name", 
                                                     "Young person’s surname", "Young person’s pronouns", 
                                                     "Which instrument will your young person play in NOFA?" 
                                                     ]
        row_length = "?,?,?,?,?"
        columns = "small_sectional,first_name,surname,pronouns,instrument"
        new_csv = f"small_sectional_register"
        list_of_csv_columns = ["Small sectional", "First name", "Surname", "Pronouns", "Instrument", 
                             "Present"]
        list_of_small_sectionals = ["Piano, keyboard & melodica", "Flute", "Trumpet, french horn & cornet",
                                     "Violin 1", "Violin 2", "Violin 3", "Clarinet & Sax", "Double Bass", "Euph, trombone & tuba", 
                                     "Cello", "Guitars, bass & ukulele", "Bassoon & Oboe", "Percussion"]
        upper_range = 13

        break

    else:
        print("Oops - Please try again.")

cursor = create_table(db, db_columns, db_title)
read_csv_file(membership_permissions_csv, db_title, membership_permissions_csv_columns_needed, columns, row_length)
write_csv_file(db_title, new_csv, list_of_csv_columns, upper_range, user_input,list_of_small_sectionals)


                        





        
