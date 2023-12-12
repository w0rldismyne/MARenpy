# May need to switch Show to an Enum of states if want to add a lock/hint state

style Inventory:
    color "#000000"
    hover_color "#444444"
   

init python:
    class Clue:
        def __init__(self, Name, Description):
            self.Name = Name
            self.Description = Description
            self.Show = False

        @property
        def GetName(self):
            return self.Name
        
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

        def CheckClue(self, Clue):
            for clue in self.Clues:
                if (clue.Name is Clue.Name):
                    if(Clue.Show is True):
                        return True
                    else:
                        break
            return False

        def Clear(self):
            self.Clues.Clear()
            self.Count = 0

default inventory = Inventory()
default selected_clue_name = "Name"
default selected_clue_description = "Place Holder Text 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"
default page = 1

label inventory:

    # Test Inventory

    $ clue01 = Clue("Clue1", "This is Clue 1")
    $ clue02 = Clue("Clue2", "This is Clue 2")
    $ clue03 = Clue("Clue3", "This is Clue 3")
    $ clue04 = Clue("Clue4", "This is Clue 4")
    $ clue05 = Clue("Clue5", "This is Clue 5")
    $ clue06 = Clue("Clue6", "This is Clue 6")
    $ clue07 = Clue("Clue7", "This is Clue 7")
    $ clue08 = Clue("Clue8", "This is Clue 8")
    $ clue09 = Clue("Clue9", "This is Clue 9")
    $ clue10 = Clue("Clue10", "This is Clue 10")
    $ clue11 = Clue("Clue11", "This is Clue 11")
    $ clue12 = Clue("Clue12", "This is Clue 12")
    $ clue13 = Clue("Clue13", "This is Clue 13")
    $ clue14 = Clue("Clue14", "This is Clue 14")
    $ clue15 = Clue("Clue15", "This is Clue 15")
    $ clue16 = Clue("Clue16", "This is Clue 16")
    $ clue17 = Clue("Clue17", "This is Clue 17")
    $ clue18 = Clue("Clue18", "This is Clue 18")
    $ clue19 = Clue("Clue19", "This is Clue 19")
    $ clue20 = Clue("Clue20", "This is Clue 20")
    $ clue21 = Clue("Clue21", "This is Clue 21")
    $ clue22 = Clue("Clue22", "This is Clue 22")
    $ clue23 = Clue("Clue23", "This is Clue 23")
    $ clue24 = Clue("Clue24", "This is Clue 24")
    $ clue25 = Clue("Clue25", "This is Clue 25")
    $ clue26 = Clue("Clue26", "This is Clue 26")
    $ clue27 = Clue("Clue27", "This is Clue 27")
    $ clue28 = Clue("Clue28", "This is Clue 28")
    $ clue29 = Clue("Clue29", "This is Clue 29")
    $ clue30 = Clue("Clue30", "This is Clue 30")
    $ clue31 = Clue("Clue31", "This is Clue 31")
    $ clue32 = Clue("Clue32", "This is Clue 32")

    $ test_number = 10

    $ inventory.AddClue(clue01)
    $ inventory.ShowClue(clue01)
    $ inventory.AddClue(clue02)
    $ inventory.ShowClue(clue02)
    $ inventory.AddClue(clue03)
    $ inventory.ShowClue(clue03)
    $ inventory.AddClue(clue04)
    $ inventory.ShowClue(clue04)
    $ inventory.AddClue(clue05)
    $ inventory.ShowClue(clue05)
    $ inventory.AddClue(clue06)
    $ inventory.ShowClue(clue06)
    $ inventory.AddClue(clue07)
    $ inventory.ShowClue(clue07)
    $ inventory.AddClue(clue08)
    $ inventory.ShowClue(clue08)
    $ inventory.AddClue(clue09)
    $ inventory.ShowClue(clue09)
    $ inventory.AddClue(clue10)
    $ inventory.ShowClue(clue10)
    $ inventory.AddClue(clue11)
    $ inventory.ShowClue(clue11)
    $ inventory.AddClue(clue12)
    $ inventory.ShowClue(clue12)
    $ inventory.AddClue(clue13)
    $ inventory.ShowClue(clue13)
    $ inventory.AddClue(clue14)
    $ inventory.ShowClue(clue14)
    $ inventory.AddClue(clue15)
    $ inventory.ShowClue(clue15)
    $ inventory.AddClue(clue16)
    $ inventory.ShowClue(clue16)
    $ inventory.AddClue(clue17)
    $ inventory.ShowClue(clue17)
    $ inventory.AddClue(clue18)
    $ inventory.ShowClue(clue18)
    $ inventory.AddClue(clue19)
    $ inventory.ShowClue(clue19)
    $ inventory.AddClue(clue20)
    $ inventory.ShowClue(clue20)
    $ inventory.AddClue(clue21)
    $ inventory.ShowClue(clue21)
    $ inventory.AddClue(clue22)
    $ inventory.ShowClue(clue22)
    $ inventory.AddClue(clue23)
    $ inventory.ShowClue(clue23)
    $ inventory.AddClue(clue24)
    $ inventory.ShowClue(clue24)
    $ inventory.AddClue(clue25)
    $ inventory.ShowClue(clue25)
    $ inventory.AddClue(clue26)
    $ inventory.ShowClue(clue26)
    $ inventory.AddClue(clue27)
    $ inventory.ShowClue(clue27)
    $ inventory.AddClue(clue28)
    $ inventory.ShowClue(clue28)
    $ inventory.AddClue(clue29)
    $ inventory.ShowClue(clue29)
    $ inventory.AddClue(clue30)
    $ inventory.ShowClue(clue30)
    $ inventory.AddClue(clue31)
    $ inventory.ShowClue(clue31)
    $ inventory.AddClue(clue32)
    $ inventory.ShowClue(clue32)

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
        xpos 0.5

        # 7.5%
        ypos 0.075

        # 20%
        xsize 0.2

        # 10%
        ysize 0.1

    text "INVENTORY":
        xanchor 0.5
        yanchor 0.5

        # 50%
        xpos 0.5

        # 7.5%
        ypos 0.075

        size(50)
        italic True

    # Description Box - X 70.0%-100% + M (-54) = 67%~-97%~, Y 20.0%-95.0% + M(10%) = 15.0%-100%
    image "images/Clues/Paper.png":
        xanchor 0.5
        yanchor 0.5

        # 85% -> 82.1875%~
        xpos 0.821875

        # 56.25%~
        ypos 0.5625

        # 30%
        xsize 0.3

        # 77.5%
        ysize 0.775

    image "images/Clues/PushPin.png":
        xanchor 0.5
        yanchor 0.5

        xpos 0.821875

        ypos 0.225

    text "[selected_clue_name]":
        xanchor 0.0
        yanchor 0.0
        xpos 1384
        ypos 284
        xsize 450
        ysize 100

    text "[selected_clue_description]":
        xanchor 0.0
        yanchor 0.0
        xpos 1384
        ypos 334
        xsize 450
        ysize 540

    # Return Button
    textbutton _("Return") action Hide("inventory"):
        xalign 1.0
        yalign 0.0
        text_style "Inventory"
        #text_color "#FF0000"
        #text_hover_color "#000000"

    # Page Controls
    hbox:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3359375
        ypos 0.27
        xsize 0.671875
        ysize 0.1
        spacing 50

        textbutton _("<<"):
            xalign 0.0
            yalign 1.0
            text_style "Inventory"
            if (page > 1):
                action SetVariable("page", page - 1), renpy.restart_interaction

        text "[page]":
            bold True
            xalign 0.5
            yalign 0.5

        textbutton _(">>"):
            xalign 1.0
            yalign 1.0
            text_style "Inventory"
            if (page < inventory.Count / 6):
                action SetVariable("page", page + 1), renpy.restart_interaction


    # Clue Arrangement
    #    Old Parameters
    #    xanchor 0.5
    #    yanchor 0.5
    #    xpos 0.3359375
    #    ypos 0.575
    #    xsize 0.671875
    #    ysize 0.85
    ##################

    $ width = 3
    $ height = 2
    # height = 1 + int(inventory.Count/3)

    grid width height:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3359375
        ypos 0.61
        xsize 0.671875
        ysize 0.58

        xspacing 0.028125
        yspacing 0.05
        
        $ list_tracker = 0
        $ list_page_minimum = (page - 1) * width * height
        $ list_page_maximum = page * width * height

        for clue in inventory.Clues:

            if (clue.Show is True):

                $ list_tracker += 1

                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    imagebutton:
                        xanchor 0.0
                        yanchor 0.0
                        idle "images/Clues/Cluecard_blank_small.jpg"
                        hover "images/Clues/Cluecard_hover_small.jpg"
                        action SetVariable("selected_clue_name", clue.GetName), SetVariable("selected_clue_description", clue.GetDescription), renpy.restart_interaction
                
                else:
                    continue

    grid width height:
        xanchor 0.0
        yanchor 0.0
        xpos 0.3359375
        ypos 0.575
        xsize 0.671875
        ysize 0.85

        $ list_tracker = 0

        for clue in inventory.Clues:

            if (clue.Show is True):

                $ list_tracker += 1

                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    image "images/Clues/PushPin.png":
                        xanchor 0.5
                        yanchor 0.5
                        
                else:
                    continue