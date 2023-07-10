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
    $ FreeActions = 0
    $ DefaultActionCount = 1
    $ ExtraActionCount = 2
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

    call variables

label Event1:
    #day1 Event 1
    "Event 1"

    call FreeDay
    jump Event2

label Event2:
    #day1 Event 2
    "Event 2"

    call FreeDay
    jump Event3

label Event3:
    "Event 3"

return

label FreeDay:

    # Determine Available Actions
    if Vigor < 2:
        $ FreeActions = DefaultActionCount
    else:
        $ FreeActions = ExtraActionCount

label menutree:
    while FreeActions > 0:
        "Actions Remaining: [FreeActions]"
        $ FreeActions -= 1
        call coremenuCh1
    return

label coremenuCh1:

    "Core Menu goes here"
    menu:
        "Hang out":
            $ uRep += 1
            pass
        "Investigate":
            $ Clue1 = True
            pass
        "Study":
            $ Vigor += 2
            pass
return