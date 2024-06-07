import random

riff = []
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
invalid_character = True

# Function to generate random musical notes for a riff.
def initialse_riff(riff, notes, number_of_notes):
    for i in range(0, number_of_notes):
        random_number = random.randrange(0, len(notes)-1)
        riff.append(notes[random_number])
    print(riff)

print("This programme will generate random notes to create a riff.")
while invalid_character == True:
    user_number_of_notes = input("How many notes do you want in the riff? ")
    try:
        number_of_notes = int(user_number_of_notes)
        invalid_character = False
    except ValueError:
        print("Please enter a number.")

initialse_riff(riff, notes, number_of_notes)

maj_scale = [0, 2, 4, 5, 7, 9, 11]
min_scale = [0, 2, 3, 5, 7, 8, 11]

print("\nThis programme will generate the notes of any major or minor key.")

#natural_notes = ["F", "G", "A", "B", "C", "D", "E"]
natural_notes = ["E", "D", "C", "B", "A", "G", "F"]


# Loop to check if user input corresponds to a musical note.
invalid_note = True
not_a_note = True
while invalid_note == True:
    user_note = input("Please enter a starting note: ")
    for i in range(0, len(notes)):
        if user_note.lower() == notes[i].lower():
            user_input_note_index = i
            invalid_note = False
            not_a_note = False
    if not_a_note == True:
        print("This isn't a valid musical note.")

# if user_input_note_index has a '#' in it, then remove it and store in another variable
if len(user_note) == 2:
    user_nat_note = user_note[0]
else:
    user_nat_note = user_note

for i in range(0, len(natural_notes)):
    if user_nat_note.lower() == natural_notes[i].lower():
        user_nat_note_index = i

#Function to print stave with musical note.
def print_stave(user_nat_note):
    print(" " * 2)
    print("-" * 5)
    for i in range(0, 7):
        if i % 2 == 1:
            if i == user_nat_note:
                if len(user_note) == 2:
                    print("--o#-")
                else:
                    print("--o--")
            else:
                print("-" * 5)
        else:
            if i == user_nat_note:
                if len(user_note) == 2:
                    print("  o#")
                else:
                    print("  o")
            else:
                print(" " * 2)
    print("-" * 5)

print_stave(user_nat_note_index)

def create_key(user_input_note_index, notes, is_major_key):
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

# Function to call triad function or create key function.
def user_key_input_func(user_key_input, call_triad_func):
    if user_key_input.lower() == "major" or user_key_input == "maj":
        is_major_key = True
        if call_triad_func == False:
            call_create_key_func = True
        else:
            call_create_key_func = False
    elif user_key_input.lower() == "minor" or user_key_input == "min":
        is_major_key = False
        if call_triad_func == False:
            call_create_key_func = True
        else: 
            call_create_key_func = False
    else:
        print("Please enter a valid option.")
        call_create_key_func = False
        user_key_input = input("\nWould you like the Major or Minor key? ")
        user_key_input_func(user_key_input)
    if call_create_key_func == True:
        create_key(user_input_note_index, notes, is_major_key)
    else:
        create_chords(user_note_input, notes, is_major_key)

user_key_input = input("\nWould you like the Major or Minor key? ")
call_triad_func = False

user_key_input_func(user_key_input, call_triad_func)


def create_chords(user_note_input, notes, is_major_key):
    triad = []
    for j in range(0, len(notes)):
        if user_note_input.lower() == notes[j].lower():
            user_note_index = j
            if is_major_key == True:
                third_index = user_note_index + 4
                if third_index >= 12:
                    third_index -= 12
                third = notes[third_index]
            else:
                third_index = user_note_index + 3
                if third_index >= 12:
                    third_index -= 12
                third = notes[third_index]
            fifth_index = user_note_index + 7
            if fifth_index >= 12:
                fifth_index -= 12
            fifth = notes[fifth_index]
            triad.extend([notes[user_note_index], third, fifth])
            print(triad)

print("\nThis programme will construct a Major or Minor triad.")
user_note_input = input("Please enter the tonic of a triad: ")
user_key_input = input("Would you like the Major or Minor chord? ")
call_triad_func = True

user_key_input_func(user_key_input, call_triad_func)











