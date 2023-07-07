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
    $ Turn = 0
    $ Day = 0

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

        if Vigor >= 2:
            if Turn <= 1:
                $ Turn += 1
                call coremenuCh1
            else:
                call coremenuCh1
        else:
            call coremenuCh1

    label coremenuCh1:

        "Core Menu goes here"
    return

    label Event2:
        #day1 Event 2

        "Event 2"
    return




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

        
    return
