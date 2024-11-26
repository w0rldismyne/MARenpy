default persistent.sandbox_menu_choice = 0

image background1 = "Backgrounds/Courtyard.png"
image background2 = "Backgrounds/Field.png"
image background3 = "Backgrounds/ForestClearing.png"
image background4 = "Backgrounds/Lake.png"

image sprite 1 = "Sprites/TestSprite.png"
image sprite 2 = "Sprites/TestSprite2.png"
image sprite 3 = "Sprites/TestSprite3.png"
image sprite 4 = "Sprites/TestSprite4.png"

transform room_1:
    matrixcolor TintMatrix("#FFFFFF")

transform room_2:
    matrixcolor TintMatrix("#FF8000")

transform room_3:
    matrixcolor TintMatrix("#0037FF")

# THE GAMES STARTS HERE!
label sandbox:
    
    "Entering Sandbox"
    "What are we testing?"

    menu:
        "Event Loop":
            pass
        "New UI":
            jump new_ui
        "Menu":
            jump new_menu
        "Room of Persistence":
            jump sandbox_persistence
        "Image Map Ver.":
            jump image_map_point_and_click

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

label new_ui:

    call screen settings
    call screen settings_2
    jump sandbox

label new_menu:

    show screen test_button

    $ choice_many_choices = True
    menu:
        "Location 01":
            pass
        "Location 02":
            pass
        "Location 03":
            pass
        "Location 04":
            pass

    $ choice_many_choices = False

    hide screen test_button
return

label sandbox_persistence:

    menu:
        "Visit the Room":
            jump sandbox_room

        "Change to Starting Room":
            $ persistent.sandbox_menu_choice = 0
            "Room 1 Applied"
            jump sandbox_persistence

        "Change to Variant Room 1":
            $ persistent.sandbox_menu_choice = 1
            "Room 2 Applied"
            jump sandbox_persistence

        "Change to Variant Room 2":
            $ persistent.sandbox_menu_choice = 2
            "Room 3 Applied"
            jump sandbox_persistence

        "Leave":
            jump sandbox

label sandbox_room:
    if persistent.sandbox_menu_choice is 0:
        scene backgroundschool at room_1
        "Room 1"
        
    elif persistent.sandbox_menu_choice is 1:
        scene backgroundschool at room_2
        "Room 2"

    elif persistent.sandbox_menu_choice is 2:
        scene backgroundschool at room_3
        "Room 3"
        
    jump sandbox_persistence

label image_map_point_and_click:
    call screen test

screen test:
    modal True

    imagemap:
        alpha False

        ground None
        idle "images/Interactables/ch1idle.png"
        hover "images/Interactables/ch1hover.png"

        hotspot (10, 570, 291, 167) action Jump("sandbox")
        hotspot (1319, 26, 368, 389) action Jump("sandbox")
        hotspot (267, 6, 785, 717) action Jump("sandbox")
        hotspot (1393, 523, 407, 323) action Jump("sandbox")