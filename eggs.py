import math

print("This programme will tell you how many omelettes you can make. "
      "Please follow the instructions to proceed.")

eggs_per_box = 0
no_of_boxes = 0
eggs_per_omelette = 7
box_variable = "boxes"
omelette_variable = "omelettes"
invalid_eggs_per_box = True
invalid_no_of_boxes = True

no_of_omelettes = math.floor((eggs_per_box * no_of_boxes) / eggs_per_omelette)
output = ("You can make {} {} with {} {} of eggs."
          .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))

while invalid_eggs_per_box:
    eggs_per_box_input = input("How many eggs per box? ")
    try:
        eggs_per_box += int(eggs_per_box_input)
        if eggs_per_box < 0:
            print("You can't have a minus number of eggs per box.")
        else:
            no_of_omelettes = math.floor((eggs_per_box * no_of_boxes) / eggs_per_omelette)
            output = ("You can make {} {} with {} {} of eggs."
          .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))
            invalid_eggs_per_box = False
    except ValueError:
        print("Please enter a number.")

while invalid_no_of_boxes:
    no_of_boxes_input = input("How many boxes do you have? ")
    try:
        no_of_boxes = int(no_of_boxes_input)
        if no_of_boxes < 0:
            print("You can't have a minus number of egg boxes")
        elif no_of_boxes == 1:
            box_variable = "box"
            no_of_omelettes = math.floor((eggs_per_box * no_of_boxes) / eggs_per_omelette)
            output = ("You can make {} {} with {} {} of eggs."
          .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))
            invalid_no_of_boxes = False
        else:
            no_of_omelettes = math.floor((eggs_per_box * no_of_boxes) / eggs_per_omelette)
            output = ("You can make {} {} with {} {} of eggs."
          .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))
            invalid_no_of_boxes = False
    except ValueError:
        print("Please enter a number. ")

if no_of_omelettes == 1:
    omelette_variable = "omelette"


print(output)





