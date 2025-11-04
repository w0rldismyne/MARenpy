# May need to switch Show to an Enum of states if want to add a lock/hint state

style Inventory:
    color "#000000"
    hover_color "#444444"
   

python early:
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
    # $ inventory.ShowClue(clue_account)
    $ inventory.AddClue(clue_baton_pass)
    # $ inventory.ShowClue(clue_baton_pass)
    $ inventory.AddClue(clue_brag)
    # $ inventory.ShowClue(clue_brag)
    $ inventory.AddClue(clue_friends_list)
    # $ inventory.ShowClue(clue_friends_list)
    $ inventory.AddClue(clue_missing_phone)
    # $ inventory.ShowClue(clue_missing_phone)
    $ inventory.AddClue(clue_mysterious_noise)
    # $ inventory.ShowClue(clue_mysterious_noise)
    $ inventory.AddClue(clue_pa_access)
    # $ inventory.ShowClue(clue_pa_access)
    $ inventory.AddClue(clue_prank)
    # $ inventory.ShowClue(clue_prank)
    $ inventory.AddClue(clue_second_locker)
    # $ inventory.ShowClue(clue_second_locker)
    $ inventory.AddClue(clue_cheerad)

    return

screen inventory():
    modal True

    image "New Assets/Inventory/inv_background.png"

    # Selected Clue Inspection

    text "[selected_clue_name]":
        xpos 1279
        ypos 243
        xsize 447
        ysize 73
        xanchor 0.0
        yanchor 0.5
        size 55

    text "[selected_clue_description]":
        xpos 1283
        ypos 294
        xsize 463
        ysize 695
        xanchor 0.0
        yanchor 0.0

    $ width = 4
    $ height = 2

    # Menu Exit

    imagebutton action SetVariable("selected_clue_name", ""), SetVariable("selected_clue_description", ""), Hide("inventory"):
        focus_mask True
        idle "New Assets/Inventory/inv_idle.png"
        hover "New Assets/Inventory/inv_hover.png"

    # Clue Layout

    grid width height:
        xanchor 0.5
        yanchor 0.5
        xpos 625
        ypos 640
        xsize 1000
        ysize 700
        xspacing 30
        yspacing 68

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
                        idle "New Assets/Inventory/inv_box.png"
                        hover "New Assets/Inventory/inv_box_light.png"
                        selected_idle "New Assets/Inventory/inv_box_dark.png"
                        selected_hover "New Assets/Inventory/inv_box_dark.png"
                        action SetVariable("selected_clue_name", clue.GetName), SetVariable("selected_clue_description", clue.GetDescription), renpy.restart_interaction

                        if selected_clue_name is clue.GetName:
                            selected True

                else:
                    continue

    # Clue Labels

    grid width height:
        xanchor 0.5
        yanchor 0.5
        xpos 625
        ypos 640
        xsize 1000
        ysize 700
        xspacing 30
        yspacing 68

        $ list_tracker = 0
        $ list_page_minimum = (page - 1) * width * height
        $ list_page_maximum = page * width * height

        for clue in inventory.Clues:
            if (clue.Show is True):
                $ list_tracker += 1
                if (list_tracker > list_page_minimum and list_tracker <= list_page_maximum):
                    
                    frame:
                        background None
                        xsize 227
                        ysize 56
                        xanchor 0.0
                        yanchor 0.0

                        if (list_tracker > list_page_maximum - (width * height / 2)):
                            ypos 191

                        text [clue.GetName]:
                            xpos 0.5
                            xanchor 0.5
                            ypos 0.5
                            yanchor 0.5
                            size 24

                else:
                    continue

    # Page Controls
    hbox:
        xanchor 0.5
        yanchor 0.5
        xpos 625
        ypos 240
        xsize 1000
        ysize 100

        textbutton _("<<"):
            xalign 0.5
            yalign 0.5
            text_size 50
            text_style "Inventory"
            if (page > 1):
                action SetVariable("page", page - 1), renpy.restart_interaction

        text "[page]":
            bold True
            xalign 0.5
            yalign 0.5
            size 50

        textbutton _(">>"):
            xalign 0.5
            yalign 0.5
            text_size 50
            text_style "Inventory"
            if (page < inventory.Count / (width * height)):
                action SetVariable("page", page + 1), renpy.restart_interaction