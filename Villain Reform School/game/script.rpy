# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nagen Tesuta")
define u = Character("Uitto Hanatabe")

label variables:

    # Player's Stats
    $ Vigor = 0
    $ Vision = 0
    $ Intel = 0
    $ Charm = 0

# PlayerData
    $ VigorSP = 0
    $ VigorMax = 3
    $ VisionSP = 0
    $ VisionMax = 3
    $ IntelSP = 0
    $ IntelMax = 3
    $ CharmSP = 0
    $ CharmMax = 3

# Story Reputation Points
    $ Hero = 0
    $ Villain = 4

    # Daily Life
    $ XTurn = 0
    $ Day = 0
    $ Turn = 0

    # Investigation
    $ Clue1 = False

    # Player Relationships
    $ uRep = 0

    # Character Flags
    $ uTurn = 0
return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    call variables
    
    label Event1:
        #day1 Event 1
        "Event 1"

        call menutree
        jump Event2
    return

    label menutree:
        if Turn == 0:
            if Vigor >= 2:
                "Extra vigor, yay!"
                if XTurn < 1:
                    $ XTurn += 1
                    "Turn 1"
                    jump coremenuCh1
                elif XTurn >= 1:
                    "No More turns."
                    $ Turn = 1
                    jump coremenuCh1
                    return
            else:
                "No Extra Turn"
                $ Turn 
                jump coremenuCh1
                return
        elif Turn >= 1:
            $ Turn = 1
            "No Vigor"
            jump coremenuCh1
            return
        else:
             return

    label coremenuCh1:

        "Core Menu goes here"
        menu:
            "Hang out":
                $ uRep += 1
                call menutree
            "Investigate":
                $ Clue1 = True
                call menutree
            "Study":
                $ Vigor += 2
                call menutree

    return

    label Event2:
        #day1 Event 2

        "Event 2"
        $ XTurn = 0
        $ Turn = 0
        call menutree
        jump Event3
    return

    label Event3:
        "Event 3"
    return




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

        
    return
