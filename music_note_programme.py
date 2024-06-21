import random

riff = []
sharp_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
user_number_of_notes = "How many notes do you want in the riff? "
not_a_number_statement = "Please enter a number."
invalid_character = True
maj_scale = [0, 2, 4, 5, 7, 9, 11]
min_scale = [0, 2, 3, 5, 7, 8, 11]
natural_notes = ["G", "F", "E", "D", "C", "B", "A", "G", "F", "E", "D"]
list_of_notes = []
starting_note_for_key = "Please enter a starting note: "
invalid_note_message = "This isn't a valid musical note."
starting_note_for_triad = "Please enter the tonic of a triad: "
user_key_prompt = "Please enter the major or minor key: "
invalid_key_message = "That is not a valid imput."

# Function to get number from user.
def get_numeric_input(question, error_message):
    while True:
        user_input = input(question)
        try:
            return int(user_input)
        except ValueError:
            print(error_message)

# Function to generate random musical notes for a riff.
def initialse_riff(riff, note_list, number_of_notes):
    for i in range(0, number_of_notes):
        random_number = random.randrange(0, len(note_list)-1)
        riff.append(note_list[random_number])
    print(riff)

# Function to check that user input is a musical note.
def get_note_input(user_input_prompt, error_message):
    while True:
        user_note = input(user_input_prompt)
        for i in range(0, len(sharp_notes)):
            if user_note.lower() == sharp_notes[i].lower():
                return user_note
        print(error_message)

# Get index of note in list of notes.
def get_note_index_in_list(user_note):
    for i in range(0, len(sharp_notes)):
            if user_note.lower() == sharp_notes[i].lower():
                return i

# Convert user note (as string) to a list.
def convert_user_note_to_list(user_note, list_of_notes):
    list_of_notes.append(user_note)
    return list_of_notes

#Function to print stave with musical note.
def print_stave(natural_triad, list_of_notes):
    notes_printed = 0
    for j in range(0, 11):
        for i in range(0, len(natural_triad)):
            if natural_notes[j].lower() == natural_triad[i].lower():
                is_match = True
                break
            else:
                is_match = False
        if is_match == True and notes_printed < len(list_of_notes):
            notes_printed += 1
            if len(list_of_notes[i]) == 2:
                if j % 2 == 0:
                    print("  o#")
                else:
                    print("--o#--")
            else:
                if j % 2 == 0:
                    print("  o")
                else:
                    print("--o--")
        elif is_match == False or notes_printed >= len(list_of_notes):
            if j % 2 == 0:
                print("  ")
            else:
                print("-----")


# if user_input_note_index has a '#' in it, then remove it and store in another variable
def check_for_sharp(list_of_notes):
    natural_triad = []
    for i in range(0, len(list_of_notes)):
        # if length of note in list of notes equals 2
        if len(list_of_notes[i]) == 2:
            user_nat_note = list_of_notes[i][0]
        else:
            user_nat_note = list_of_notes[i]
        natural_triad.append(user_nat_note)
    print_stave(natural_triad, list_of_notes)


# Function to generate the note names of all notes of either the minor or major key.
def create_key(user_input_note_index, notes, is_major_key, user_note):
    new_key = []
    if is_major_key == True:
        scale = maj_scale
        statement = f"Notes of the {user_note.upper()} Major scale: "
    else:
        scale = min_scale
        statement = f"Notes of the {user_note.upper()} Minor scale: "
    for i in range(0, len(scale)):
        note_position = scale[i] + user_input_note_index
        if note_position > len(notes)-1:
            note_position -= 12
        new_key.append(notes[note_position])
    print(statement)
    print(new_key)

# Get major or minor key from user.
def get_user_input_maj_min(input_message, error_message):
    while True:
        user_key_input = input(input_message)
        if user_key_input.lower() == "major" or user_key_input.lower() == "maj":
            return user_key_input
        elif user_key_input.lower() == "minor" or user_key_input.lower() == "min":
            return user_key_input
        else:
            print(error_message)

# Function to call triad function or create key function.
def user_key_input_func(user_key_input, call_triad_func):
    if user_key_input.lower() == "major" or user_key_input == "maj":
        is_major_key = True
        if call_triad_func == False:
            create_key(user_input_note_index, sharp_notes, is_major_key, user_note)
        else:
            create_chords(user_note, sharp_notes, is_major_key)
    elif user_key_input.lower() == "minor" or user_key_input == "min":
        is_major_key = False
        if call_triad_func == False:
            create_key(user_input_note_index, sharp_notes, is_major_key, user_note)
        else:
            create_chords(user_note, sharp_notes, is_major_key)

# Function to construct a major or minor triad.
def create_chords(user_note, note_list, is_major_key):
    triad = []
    not_a_note = True
    for j in range(0, len(note_list)):
        if user_note.lower() == note_list[j].lower():
            not_a_note = False
            user_note_index = j
            if is_major_key == True:
                statement = f"Notes of the {user_note.title()} Major triad:"
                third_index = user_note_index + 4
                if third_index >= 12:
                    third_index -= 12
                third = note_list[third_index]
            else:
                statement = f"Notes of the {user_note.title()} Minor triad:"
                third_index = user_note_index + 3
                if third_index >= 12:
                    third_index -= 12
                third = note_list[third_index]
            fifth_index = user_note_index + 7
            if fifth_index >= 12:
                fifth_index -= 12
            fifth = note_list[fifth_index]
            triad.extend([note_list[user_note_index], third, fifth])
            print(statement)
            print(triad)
            check_for_sharp(triad)
    if not_a_note == True:
        print("This isn't a valid musical note.")
        


#1 riff
print("This programme will generate random notes to create a riff.")
user_input = get_numeric_input(user_number_of_notes, not_a_number_statement)
initialse_riff(riff, sharp_notes, user_input)

#2 scale
print("\nThis programme will generate the notes of any major or minor key.")
user_note = get_note_input(starting_note_for_key, invalid_note_message)
user_input_note_index = get_note_index_in_list(user_note)
list_of_notes = convert_user_note_to_list(user_note, list_of_notes)
check_for_sharp(list_of_notes)

call_triad_func = False
user_key_input = user_key_input = get_user_input_maj_min(user_key_prompt, invalid_key_message)

user_key_input_func(user_key_input, call_triad_func)

# 3 Triad 
print("\nThis programme will construct a Major or Minor triad.")

user_input = get_note_input(starting_note_for_triad, invalid_note_message)

call_triad_func = True
user_key_input = get_user_input_maj_min(user_key_prompt, invalid_key_message)

user_key_input_func(user_key_input, call_triad_func)














