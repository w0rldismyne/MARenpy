# May need to switch Show to an Enum of states if want to add a lock/hint state

style Inventory:
    color "#000000"
    hover_color "#444444"
   

init python:
    class Clue:
        def __init__(self, Identifier, Name, Description):
            self._Identifier = Identifier
            self._Name = Name
            self._Description = Description
            self.Show = False

        @property
        def GetID(self):
            return self._Identifier
        
        @property
        def GetName(self):
            return self._Name
        
        @property
        def GetDescription(self):
            return self._Description

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
                if (clue.GetName is Clue.GetName):
                    clue.Show = True
                    self.Count += 1
                    break

        def HideClue(self, Clue):
            for clue in self.Clues:
                if (clue.GetName is Clue.GetName):
                    clue.Show = False
                    self.Count -= 1
                    break

        def CheckClue(self, Clue):
            for clue in self.Clues:
                if (clue.GetName is Clue.GetName):
                    if(Clue.Show is True):
                        return True
                    else:
                        break
            return False

        def Clear(self):
            self.Clues.Clear()
            self.Count = 0

default inventory = None
default selected_clue_name = ""
default selected_clue_description = ""
default page = 1

define clue_account = Clue("clue_account", "Account", "There's a number of students with echo accounts.")
define clue_baton_pass = Clue("clue_baton_pass", "Baton Pass", "Kazz's phone got passed around by a few people.")
define clue_brag = Clue("clue_brag", "Brag", "Kazz told anyone who'd listen about the tech he smuggled in.")
define clue_friends_list = Clue("clue_friends_list","Friend's List", "Everyone knows someone.")
define clue_missing_phone = Clue("clue_missing_phone", "Missing Phone", "Kazz claims it's stolen.")
define clue_mysterious_noise = Clue("clue_mysterious_noise", "Mysterious Noise", "At the early hours, something was alarming at school.")
define clue_pa_access = Clue("clue_pa_access", "PA Access", "Only a few people were allowed in the AV Room.")
define clue_prank = Clue("clue_prank", "Prank", "Kazz's friends thought messing with his stuff was funny.")
define clue_second_locker = Clue("clue_second_locker", "Second Locker", "Someone took Mu's locker for themselves.")
define clue_cheerad = Clue("clue_cheerad", "Club Ad", "A radio announcement submitted to Kazz.")


label inventory:

    # Test Inventory
    $ inventory = Inventory()

    $ inventory.AddClue(clue_account)
    #$ inventory.ShowClue(clue_account)
    $ inventory.AddClue(clue_baton_pass)
    #$ inventory.ShowClue(clue_baton_pass)
    $ inventory.AddClue(clue_brag)
    #$ inventory.ShowClue(clue_brag)
    $ inventory.AddClue(clue_friends_list)
    #$ inventory.ShowClue(clue_friends_list)
    $ inventory.AddClue(clue_missing_phone)
    #$ inventory.ShowClue(clue_missing_phone)
    $ inventory.AddClue(clue_mysterious_noise)
    #$ inventory.ShowClue(clue_mysterious_noise)
    $ inventory.AddClue(clue_pa_access)
    #$ inventory.ShowClue(clue_pa_access)
    $ inventory.AddClue(clue_prank)
    #$ inventory.ShowClue(clue_prank)
    $ inventory.AddClue(clue_second_locker)
    #$ inventory.ShowClue(clue_second_locker)
    $ inventory.AddClue(clue_cheerad)

    return

screen inventory():
    
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

        ypos 0.3

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
    textbutton _("Return") action SetVariable("selected_clue_name", ""), SetVariable("selected_clue_description", ""), Hide("inventory"):
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
                        foreground f"images/Clues/{clue.GetID}.png"
                        xanchor 0.0
                        yanchor 0.0
                        idle "images/Clues/Cluecard_blank_small.jpg"
                        hover "images/Clues/Cluecard_hover_small.jpg"
                        action SetVariable("selected_clue_name", clue.GetName), SetVariable("selected_clue_description", clue.GetDescription), renpy.restart_interaction
                
                else:
                    continue

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

        for clue in inventory.Clues:

            if (clue.Show is True):

                $ list_tracker += 1

                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    image "images/Clues/PushPin.png":
                        xanchor 0.0
                        yanchor 0.0
                        
                else:
                    continue