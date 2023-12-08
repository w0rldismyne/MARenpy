# May need to switch Show to an Enum of states if want to add a lock/hint state

init python:
    class Clue:
        def __init__(self, Name, Description):
            self.Name = Name
            self.Description = Description
            self.Show = False

        @property
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
default page = 1

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

    # Background
    image "images/Clues/Cork.png"

    # Inventory Banner - X 40.0%-60.0%, Y 2.5%-12.5% + M 2.5% = 5.0%-15.0%
    image "images/Clues/Tape.png":
        xanchor 0.5
        yanchor 0.5

        # 50%
        xpos 960

        # 7.5%
        ypos 81

        # 20%
        xsize 384

        # 10%
        ysize 108

    text "INVENTORY":
        xanchor 0.5
        yanchor 0.5

        # 50%
        xpos 960

        # 7.5%
        ypos 81

        size(50)
        italic True

    # Description Box - X 70.0%-100% + M (-54) = 67%~-97%~, Y 20.0%-95.0% + M(10%) = 15.0%-100%
    image "images/Clues/Paper.png":
        xanchor 0.5
        yanchor 0.5

        # 85% -> 82.1875%~
        xpos 1632
        xoffset -54

        # 56.25%~
        ypos 607

        # 30%
        xsize 576

        # 77.5%
        ysize 837

    image "images/Clues/PushPin.png":
        xanchor 0.5
        yanchor 0.5

        xpos 1632
        xoffset -54

        ypos 243

    frame:
        xpos 1609
        ypos 604
        xanchor 0.5
        yanchor 0.5
        xsize 450
        ysize 641


    text "[description]":
        xpos 1536
        ypos 366
        xsize 500
        ysize 691
        xanchor 0.5
        yanchor 0.5

    # Return Button
    textbutton _("Return") action Hide("inventory"):
        xalign 1.0
        yalign 0.0


    # Clue Arrangement
    $ width = 3
    $ height = 2
    # height = 1 + int(inventory.Count/3)

    grid width height:
        spacing 64
        xanchor 0.5
        yanchor 0.5
        xpos 576
        ypos 648
        
        $ list_tracker = 0
        $ list_page_minimum = (page - 1) * width * height
        $ list_page_maximum = page * width * height

        for clue in inventory.Clues:

            if (clue.Show is True):

                $ list_tracker += 1

                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    imagebutton:
                        xsize 192
                        ysize 216
                        idle "images/Clues/Cluecard_blank_small.jpg"
                        hover "images/Clues/Cluecard_hover_small.jpg"
                        action SetVariable("description", clue.GetDescription), renpy.restart_interaction
                
                else:
                    continue

    grid width height:
        spacing 64
        xanchor 0.5
        yanchor 0.5
        xpos 576
        ypos 648

        $ list_tracker = 0

        for clue in inventory.Clues:

            if (clue.Show is True):

                $ list_tracker += 1

                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    image "images/Clues/PushPin.png":
                        xsize 91
                        ysize 60
                        
                else:
                    continue

    # Page Controls
    textbutton _("Previous Page"):
        xalign 0.0
        yalign 1.0
        if (page > 1):
            action SetVariable("page", page - 1), renpy.restart_interaction

    text "[page]":
        xalign 0.5
        yalign 0.5

    textbutton _("Next Page"):
        xalign 1.0
        yalign 1.0
        if (page < inventory.Count / 6):
            action SetVariable("page", page + 1), renpy.restart_interaction