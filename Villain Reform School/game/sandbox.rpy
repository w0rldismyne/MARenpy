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

default info_overlay = "images/Icons/Bossboxesv1.png"
default fight_overlay1 = "images/Icons/Bossboxesv1.png"
default fight_overlay2 = "images/Icons/Bossboxesv2.png"

default nagen_health = 10
default mariko_health = 12

default turns_passed = 0
default mariko_halfway = False
default mariko_fatigue = 0
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
    $ mariko_current_health = 12
    $ mariko_fatigue = 0
    $ turns_passed = 0
    $ mariko_halfway = False
    $ mariko_halfway_post_turns = 0
    $ mariko_attack_type = -1
    $ nagen_damage = 0
    $ mariko_damage = 0

    $ turn_order = nagen_turn
    $ fight_end_state = -1

    show screen fight_health

    g "Nagen gets first action!"

    jump fight_loop

label fight_loop:

    while turn_order is not fight_end:

        if turn_order is nagen_turn:

            call your_turn
            call post_nagen_turn

        elif turn_order is mariko_turn:

            call opponent_turn
            call post_mariko_turn

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
        pos 0.5, 0.7
        xysize 949, 1401

screen fight_health:

    image "[info_overlay]"

    text "Nagen":
        color "#000000"
        xanchor 0.5
        yanchor 0.5
        pos 1600, 75

    # Nagen's Health
    bar:
        pos 1600, 100
        xmaximum 200
        value nagen_current_health
        range nagen_health
        left_bar "gui/HealthLight6.png"
        right_bar "gui/HealthDark6.png"

    text "Mariko":
        xanchor 0.5
        yanchor 0.5
        pos 1600, 275

    # Mariko's Health
    bar:
        pos 1600, 325
        xmaximum 200
        value mariko_current_health
        range mariko_health
        left_bar "gui/HealthLight6.png"
        right_bar "gui/HealthDark6.png"

    bar:
        pos 1600, 425
        xmaximum 200
        value mariko_fatigue
        range 100
        left_bar "gui/HealthLight5.png"
        right_bar "gui/HealthDark5.png"

screen fight_menu:

    hbox:
        xanchor 0.5
        yanchor 0.5
        pos 0.5, 0.85
        spacing 0.25
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

    $ nagen_damage = renpy.random.randint(1, 3)

    $ mariko_current_health -= nagen_damage

    g "Hit Mariko for [nagen_damage] Damage!"

    jump your_turn_end

label nagen_defends:

    g "Nagen prepares himself for Mariko's next attack ..."

    $ defending = True

    jump your_turn_end

label check_conditions:

    if nagen_current_health <= 0:

        $ turn_order = fight_end
        $ fight_end_state = lose

    if mariko_current_health <= 6 or mariko_fatigue >= 50:

        if mariko_halfway is False:
            
            $ mariko_halfway = True
            $ mariko_halfway_post_turns = turns_passed

            hide screen fight_health

            call midfight_cutscene

            show screen fight_health

            $ info_overlay = fight_overlay2
        
        if mariko_current_health <= 0:

            $ turn_order = fight_end
            $ fight_end_state = lose

    if mariko_fatigue >= 100:

        $ turn_order = fight_end
        $ fight_end_state = win

    return

label opponent_turn:

    $ boss_active = boss_attack

    $ mariko_attack_type = renpy.random.randint(1, 2)

    if mariko_attack_type == 1:

        g "Mariko attacks!"

    elif mariko_attack_type == 2:

        g "Mariko makes a strong attack!"

    if defending is True:

        $ defending = False

        g "Nagen was prepared and blocks the attack!"

    else:
        
        if mariko_attack_type == 1:

            $ mariko_damage = renpy.random.randint(1, 2)

        elif mariko_attack_type == 2:
        
            $ mariko_damage = renpy.random.randint(3, 4)

        $ nagen_current_health -= mariko_damage

        g "Nagen is hit for [mariko_damage] damage!"

    $ mariko_fatigue += 10
    $ turn_order = nagen_turn

    return

label fight_mid_cutscene: #Temp
    
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

label post_nagen_turn:
    $ boss_active = boss_idle

    if mariko_halfway is False:

        if turns_passed == 0:

            m "It doesn’t matter what you do, Nagen, I won’t feel a thing."

            "But just because she can’t feel it, doesn’t mean she can’t be injured."

        elif turns_passed == 1:

            m "This is nothing compared to cheer camp. Do you know how many broken bones I’ve walked off? What’s the matter, Nagen, scared to fight a girl?"

            "Why is she purposely egging me on?"

    elif mariko_halfway is True:
        if turns_passed == mariko_halfway_post_turns + 2:

            m "Hiyoko would probably be scolding me alongside Rei."

        elif turns_passed == mariko_halfway_post_turns + 3:

            m "Ty and Kiki… They stayed together the whole time, brainwashing be damned..."

        elif turns_passed == mariko_halfway_post_turns + 4:

            "Mariko’s ankle gives out beneath her. A tangled mess of belts and heels lays helpless on the ground."

    return

label post_mariko_turn:
    $ boss_active = boss_idle

    if mariko_halfway is False:
        if turns_passed == 3:

            m "You’re making this too easy. Even the bottom left of the pyramid could deck you with one punch."

            "She says that, but she can barely move in that costume."

        elif turns_passed == 4:

            m "This isn’t going to work if you don’t fight back. C’mon! Don’t you want to save your friend?"

            "Wait, does she... want me to hit her?"

    elif mariko_halfway is True:
        if turns_passed == mariko_halfway_post_turns + 1:

            m "Kanon would have gone for your eyes."
        
        elif turns_passed == mariko_halfway_post_turns + 3:

            m "Did any of them think of me at all while I was looking for them? If I can just... take you down. They’ll forgive me... they’ll have to forgive me."

        elif turns_passed == mariko_halfway_post_turns + 4:

            m "Please... forgive me."

            "But I know she isn’t talking to me."

    return