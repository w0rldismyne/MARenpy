# Hotkeys & Shortcuts for VS Code
#     Multiselect: CTRL + ALT + Up/Down Arrow Keys - Lets you edit more than a line at a time

# JUST LOOK AT DOCUMENTATION
#RenPy Keywords Glossary

#    Declare Variable: $ - replaces normal declarations like int, string, bool

#define variable = Character("name", color = "#HEX")
# May see init: - This is old Python code and should not be used generally

#image variable = im.Scale("image name", resolution_x, resolution_y)

#scene (name of file/variable) - Show name of file/variable as background - one of these shown at a time, fits the screen

#show (name of image) - Show name of image as a sprite, scaled to resolution, goes on top of other images
#show expression      - Look it up, really
#hide (name of image) - removes images from show

#while - loop, constant? works differently than normal
#[] (square brackets) - evaluate what is inside

#menu:
#   "Choice 1":
#       pass
#   "Choice 2":
#       call (label name)
#   "Choice 3":
#       return
# Brings up a menu with choice selection

#pass   - means do nothing
#call   - goes to the block of code (label name), but continues until it finds "return" then it goes back to this point
#jump   - goes to the block of code (label name)
#return - goes back to where it was called previously or ends the game if there is no previous instance

#label  - new code block, can be referenced as branching code, games always starts in label start
#         Labels in other files can be jumped/called without further modifications

# str functions
#   zfill - Fixes string length (for numbers)

#screens.rpy - UI Stuff
#screen say - Lets you put text on the UI
#frame, hbox, vbox
#xpos, ypos, xminimum, yminimum, xalign, yalign

#init python
# run python at beginning of the game
# class(object)
#    def __init__(variables)
#        self.variable

# WISHLIST:
# Text animation (typewriter)
# Image gallery
# Battle system
# Skip API for mechanics
# Investigation stuff