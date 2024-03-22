image background1 = "Backgrounds/Courtyard.png"
image background2 = "Backgrounds/Field.png"
image background3 = "Backgrounds/ForestClearing.png"
image background4 = "Backgrounds/Lake.png"

image sprite 1 = "Sprites/TestSprite.png"
image sprite 2 = "Sprites/TestSprite2.png"
image sprite 3 = "Sprites/TestSprite3.png"
image sprite 4 = "Sprites/TestSprite4.png"

# THE GAMES STARTS HERE!
label sandbox:
    "Entering Sandbox"
    "What are we testing?"
    menu:
        "Event Loop":
            pass
        "Character Test":
            jump CharacterTest
        "Minigame":
            jump mini_game

label Event1:

    scene background1
    show sprite 1
    "Event 1"

    call FreeDay

label Event2:
    
    scene background2
    show sprite 2
    "Event 2"

    call FreeDay

label Event3:

    scene background3
    show sprite 3
    "Event 3"

    call FreeDay

label Event4:

    scene background4
    show sprite 4
    "Event 4: The End"

return

label FreeDay:

    # Determine available actions.
    if Vigor < 2:
        $ FreeActions = DefaultActionCount
    else:
        $ FreeActions = ExtraActionCount

    # While actions remain, perform free day activities.
    while FreeActions > 0:
        "Actions Remaining: [FreeActions]"
        $ FreeActions -= 1
        call FreeDayActivities
    return

label FreeDayActivities:

    #Core menu goes here
    menu:
        "Hang out":
            $ uRep += 1
            pass
        "Investigate":
            call CharacterList
            pass
        "Study":
            $ Vigor += 2
            pass
return

label CharacterList:

    menu:
        "[m]":
            pass
        "[y]":
            pass
        "[nk]":
            pass
        "[u]":
            pass
return

label CharacterTest:
    "Two Different Show"
    show sprite 1 at left
    show sprite 2 at right
    "Next"
    hide sprite 1
    hide sprite 2
    "Double Show"
    show sprite 1 at center
    show sprite 1 at right
    "Done"
    return
