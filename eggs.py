import math

eggs_per_box = 1
no_of_boxes = 1
eggs_per_omelette = 7
box_variable = "boxes"
omelette_variable = "omelettes"

no_of_omelettes = math.floor((eggs_per_box * no_of_boxes) / eggs_per_omelette)
output = ("You can make {} {} with {} {} of eggs."
          .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))

if no_of_boxes == 1:
    box_variable = "box"
    output = ("You can make {} {} with {} {} of eggs."
              .format(no_of_omelettes, omelette_variable, no_of_boxes, box_variable))
if no_of_omelettes == 1:
    omelette_variable = "omelette"
if no_of_boxes < 0:
    output = "You can't have a minus number of egg boxes."
if eggs_per_box < 0:
    output = "You can't have a minus number of egg boxes."

print(output)





