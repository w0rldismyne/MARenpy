# May need to switch Show to an Enum of states if want to add a lock/hint state

init python:
    class Clue:
        def __init__(self, Name, Description):
            self.Name = Name
            self.Description = Description
            self.Show = False
    
        def GetDescription(self):
            return self.Description

    class Inventory:
        def __init__(self):
            self.Clues = []
            self.Count = 0

        def AddClue(self, Clue):
            self.Clues.append(Clue)

        def RemoveClue(self, Clue):
            self.Clues.remove(Clue)

        def ShowClue(self, Clue):
            for clue in self.Clues:
                if (clue.Name is Clue.Name):
                    clue.Show = True
                    self.Count += 1
                    break

        def HideClue(self, Clue):
            for clue in self.Clues:
                if (clue.Name is Clue.Name):
                    clue.Show = False
                    self.Count -= 1
                    break

        def Clear(self):
            self.Clues.Clear()
            self.Count = 0

default inventory = Inventory()
default description = "Place Holder Text 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"

label inventory:

    # Test Inventory

    $ clue1 = Clue("Clue1", "This is Clue 1")
    $ clue2 = Clue("Clue2", "This is Clue 2")
    $ clue3 = Clue("Clue3", "This is Clue 3")
    $ clue4 = Clue("Clue4", "This is Clue 4")
    $ clue5 = Clue("Clue5", "This is Clue 5")
    $ clue6 = Clue("Clue6", "This is Clue 6")
    $ clue7 = Clue("Clue7", "This is Clue 7")

    $ inventory.AddClue(clue1)
    $ inventory.AddClue(clue2)
    $ inventory.AddClue(clue3)
    $ inventory.AddClue(clue4)
    $ inventory.AddClue(clue5)
    $ inventory.AddClue(clue6)
    $ inventory.AddClue(clue7)

    $ inventory.ShowClue(clue1)
    $ inventory.ShowClue(clue2)
    $ inventory.ShowClue(clue3)
    $ inventory.ShowClue(clue4)
    $ inventory.ShowClue(clue5)

    return

screen inventory(inventory = inventory):
    
    modal True
    image "images/Clues/Cork.png"

    $ width = 3
    $ height = 3
    # height = 1 + int(inventory.Count/3)

    image "images/Clues/Tape.png":
        xalign 0.5
        yoffset 27
        xsize 1280
        ysize 120

    text "INVENTORY":
        xalign 0.5
        yoffset 54
        size(50)
        italic True
#5 15 2.5 15 2.5 15 5 40
    image "images/Clues/Paper.png":
        xalign 1.0
        yalign 1.0
        xsize 768
        ysize 864
#5 20 5 20 5 20 5
    image "images/Clues/PushPin.png":
        xpos 1536
        ypos 216

    grid width height:
        spacing 64
        xanchor 0.5
        yanchor 0.5
        xpos 576
        ypos 648
        
        for clue in inventory.Clues:
            if (clue.Show is True):
                imagebutton:
                    xsize 192
                    ysize 216
                    idle "images/Clues/Cluecard_blank_small.jpg"
                    hover "images/Clues/Cluecard_hover_small.jpg"
                    action Hide("inventory_description"), SetVariable("description", clue.GetDescription()), Show("inventory_description")
                #image "images/Clues/[clue.Name].png":
                #    xsize 192
                #    ysize 216

    grid width height:
        xspacing 170
        yspacing 201
        xanchor 0.5
        yanchor 0.5
        xpos 576
        ypos 540

        for clue in inventory.Clues:
            if (clue.Show is True):
                image "images/Clues/PushPin.png":
                    xsize 91
                    ysize 60

screen inventory_description:
    modal False
    text "[description]":
        xpos 1536
        ypos 366
        xsize 500
        ysize 691
        xanchor 0.5
        yanchor 0.5