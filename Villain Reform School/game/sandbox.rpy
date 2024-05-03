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
        "Menu":
            jump new_menu
        "Battle":
            jump fight

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

label new_menu:

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
        "Location 05":
            pass
        "Location 06":
            pass
        "Location 07":
            pass
        "Location 08":
            pass
        "Location 09":
            pass
        "Location 10":
            pass
        "Location 11":
            pass
        "Location 12":
            pass
        "Location 13":
            pass
        "Location 14":
            pass
        "Location 15":
            pass

    $ choice_many_choices = False
return

default boss_active = "images/Sprites/MarikoBoss1.png"
default boss_idle = "images/Sprites/Mariko/Boss1.png"
default boss_attack = "images/Sprites/Mariko/4.png"
default boss_hurt = "images/Sprites/Mariko/3.png"

default nagen_health = 10
default mariko_health = 10
default turns_passed = 0
default mariko_halfway = False

default turn_order = 0
default nagen_turn = 0
default mariko_turn = 1
default fight_end = 2

default fight_end_state = -1
default lose = 0
default win = 1

label fight:

    $ boss_active = boss_idle

    show screen fight_background

    n "It's starting!"

    $ nagen_current_health = 10
    $ mariko_current_health = 10
    $ turns_passed = 0
    $ mariko_halfway = False

    $ turn_order = nagen_turn
    $ fight_end_state = -1

    show screen fight_health

    g "Nagen gets first action!"

    jump fight_loop

label fight_loop:

    while turn_order is not fight_end:

        if turn_order is nagen_turn:

            call your_turn

        elif turn_order is mariko_turn:

            call opponent_turn

            $ turns_passed += 1

        call check_conditions

    jump evaluate_result

label fight_end:

    n "It's over!"

screen fight_background:

    image "images/Backgrounds/MarikoStage.png"

    image "[boss_active]":
        xanchor 0.5
        yanchor 0.5
        pos 0.5, 0.5

screen fight_health:

    text "Nagen":
        color "#000000"
        xanchor 0.5
        yanchor 0.5
        pos 1500, 150

    # Nagen's Health
    bar:
        pos 1500, 200
        xmaximum 200
        value nagen_current_health
        range nagen_health

    text "Mariko":
        color "#000000"
        xanchor 0.5
        yanchor 0.5
        pos 1500, 350

    # Mariko's Health
    bar:
        pos 1500, 400
        xmaximum 200
        value mariko_current_health
        range mariko_health

screen fight_menu:

    hbox:
        xanchor 0.5
        yanchor 0.5
        pos 0.5, 0.85
        spacing 0.1
        xsize 0.5

        textbutton _("Attack"):
            text_color "#000000"
            text_hover_color "#444444"
            action Hide("fight_menu"), Jump("nagen_attacks")

        textbutton _("Defend"):
            text_color "#000000"
            text_hover_color "#444444"
            action Hide("fight_menu"), Jump("nagen_defends")

default defending = False

label your_turn:

    $ boss_active = boss_idle

    call screen fight_menu

    label your_turn_end:
        pass

    $ turn_order = mariko_turn

    return

label nagen_attacks:

    g "Nagen attacks Mariko!"

    $ boss_active = boss_hurt

    $ mariko_current_health -= 1

    g "Hit Mariko for 1 Damage!"

    jump your_turn_end

label nagen_defends:

    g "Nagen prepares himself for Mariko's next attack ..."

    $ defending = True

    jump your_turn_end

label check_conditions:
    if nagen_current_health <= 0:

        $ turn_order = fight_end
        $ fight_end_state = lose

    if mariko_current_health <= 5:

        if mariko_halfway is False:
            
            $ mariko_halfway = True

            jump fight_mid_cutscene
        
        if mariko_current_health <= 0:

            $ turn_order = fight_end
            $ fight_end_state = lose

    if turns_passed >= 10:

        $ turn_order = fight_end
        $ fight_end_state = win

    return

label opponent_turn:

    $ boss_active = boss_attack

    g "Mariko attacks!"

    if defending is True:

        $ defending = False

        g "Nagen was prepared and blocks the attack!"

    else:

        $ nagen_current_health -= 1

        g "Nagen is hit for 1 damage!"

    $ turn_order = nagen_turn

    return

label fight_mid_cutscene:
    
    g "Nagen and Mariko yapped."
    
    return

label evaluate_result:

    if fight_end_state is win:
        
        m "I'm too tired."

        n "Well, I guess I won then."

    else:

        if nagen_current_health <= 0:

            "Crap, I am too hurt ..."

            g "You Lose!"

        elif mariko_current_health <= 0:

            "I won!!! ... Did I?"

            g "You Lose!"
    
    return
