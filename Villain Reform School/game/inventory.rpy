init python:
    class Clue:
        def __init__(self, Name):
            self.Name = Name
            self.Show = False
    
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

label inventory:
    $ inventory = Inventory()

    # Test Inventory

    $ clue1 = Clue("Clue1")
    $ clue2 = Clue("Clue2")
    $ clue3 = Clue("Clue3")
    $ clue4 = Clue("Clue4")
    $ clue5 = Clue("Clue5")
    $ clue6 = Clue("Clue6")
    $ clue7 = Clue("Clue7")

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
    $ height = 1 + int(inventory.Count/3)

    image "images/Clues/Tape.png":
        xalign 0.5
        yoffset 27
        xsize 960
        ysize 162

    text "INVENTORY":
        xalign 0.5
        yoffset 54
        size(50)
        italic True

    image "images/Clues/Paper.png":
        xalign 1.0
        yalign 1.0
        xsize 768
        ysize 864

    image "images/Clues/PushPin.png":
        xpos 1536
        ypos 216

    text "Place Holder Text 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8":
        xpos 1536
        ypos 366
        xsize 500
        ysize 691
        xanchor 0.5
        yanchor 0.5


    grid width height:
        xalign 0.0
        yalign 1.0
        spacing 24
        xmargin 24
        ymargin 24
        
        for clue in inventory.Clues:
            if (clue.Show is True):
                image "images/Clues/[clue.Name].png":
                    xsize 344
                    ysize 396

    grid width height:
        xalign 0.0
        yalign 1.0
        xspacing 282
        yspacing 363
        xmargin 150
        bottom_margin 382

        for clue in inventory.Clues:
            if (clue.Show is True):
                image "images/Clues/PushPin.png":
                    xsize 86
                    ysize 57