# Boss Sprites
default boss_active = "images/Sprites/MarikoBoss1.png"
define boss_idle = "images/Sprites/Mariko/Boss1.png"
define boss_attack = "images/Sprites/Mariko/4.png"
define boss_hurt = "images/Sprites/Mariko/3.png"

# UI Panels
default info_overlay = "images/Icons/Bossboxesv1.png"
define fight_overlay1 = "images/Icons/Bossboxesv1.png"
define fight_overlay2 = "images/Icons/Bossboxesv2.png"

# Attributes
default chapter1_nagen = Character_Stats()
default nagen_current_health = -1
default nagen_health = -1
default nagen_attack = -1
default nagen_defense = -1

default mariko_current_health = 25
define mariko_health = 25
default mariko_fatigue = 0
define mariko_fatigue_max = 100

# Fight State Variables
default turns_passed = 0

default nagen_defending = False
default mariko_next_attack = 0
define mariko_weak_attack = 0
define mariko_strong_attack = 1
default mariko_halfway = False
default mariko_attack_line = ""

default turn_order = 0
define nagen_turn = 0
define mariko_turn = 1
define round_end = 2

# Fight Resolution
default fight_end_state = -1
define lose = 0
define win = 1

screen boss_mariko:

    image "[boss_active]":
        xanchor 0.5
        yanchor 0.5
        pos 0.5, 0.7
        xysize 949, 1401

screen boss_overlay:

    image "[info_overlay]"

    text "Nagen":
        color "#000000"
        xanchor 0.0
        yanchor 0.5
        pos 1600, 615

    # Nagen's Health
    bar:
        xanchor 0.0
        yanchor 0.5
        pos 1600, 665
        xmaximum 200
        value nagen_current_health
        range nagen_health
        left_bar "gui/HealthLight6.png"
        right_bar "gui/HealthDark6.png"

    text "Mariko":
        xanchor 0.0
        yanchor 0.5
        pos 1600, 75

    # Mariko's Health
    bar:
        xanchor 0.0
        yanchor 0.5
        pos 1600, 125
        xmaximum 200
        value mariko_current_health
        range mariko_health
        left_bar "gui/HealthLight6.png"
        right_bar "gui/HealthDark6.png"

    bar:
        xanchor 0.0
        yanchor 0.5
        pos 1600, 225
        xmaximum 200
        value mariko_fatigue
        range mariko_fatigue_max
        left_bar "gui/HealthLight5.png"
        right_bar "gui/HealthDark5.png"

# Battle Start
label chapter1_boss_battle_initial:

    # Nagen's Stats
    $ chapter1_nagen.AutoConfigure()
    $ nagen_health = chapter1_nagen.HP
    $ nagen_attack = chapter1_nagen.ATK
    $ nagen_defense = chapter1_nagen.Secondary
    $ nagen_current_health = nagen_health

    # Mariko's Sprite
    $ boss_active = boss_idle
    scene backgroundmariko
    show screen boss_mariko

    # Mariko's Stats
    $ mariko_current_health = mariko_health
    $ mariko_fatigue = 0
    $ mariko_next_attack = mariko_weak_attack
    $ turns_passed = 0
    $ mariko_halfway = False
    $ mariko_halfway_post_turns = 0

    # Battle Order
    $ turn_order = nagen_turn
    $ fight_end_state = -1

    show screen boss_overlay
    with dissolve

    # Temporary?
    g "Nagen gets first action!"

    jump chapter1_boss_battle_loop

# Turns go back and forth strictly
label chapter1_boss_battle_loop:
    while turn_order is not round_end:

        if turn_order is nagen_turn:

            call nagen_turn
            call post_nagen_turn

        elif turn_order is mariko_turn:

            call mariko_turn
            call post_mariko_turn

            $ turns_passed += 1

        call chapter1_boss_battle_conditions

    jump chapter1_boss_battle_evaluations

# Nagen's Available Actions
screen chapter1_boss_battle_menu:

    image "gui/button/AttackButton.png":
        xanchor 0.5
        yanchor 0.5
        pos 215, 0.33
        xysize 400, 300
    
    textbutton _("Attack"):
        xanchor 0.5
        yanchor 0.5
        pos 225, .33
        text_size 60
        text_color "#000000"
        text_hover_color "#444444"
        action Hide("chapter1_boss_battle_menu"), Hide("floating_text"), Jump("nagen_attacks")

    image "gui/button/PlainCombatButton.png":
        xanchor 0.5
        yanchor 0.5
        pos 225, 0.67
        xysize 300, 150

    textbutton _("Defend"):
        xanchor 0.5
        yanchor 0.5
        pos 225, 0.67
        text_size 60
        text_color "#000000"
        text_hover_color "#444444"
        action Hide("chapter1_boss_battle_menu"), Hide("floating_text"), Jump("nagen_defends")

transform boss_hint1:
    alpha 0.0
    pause 1.0
    parallel:
        ease 2.0 alpha 1.0
    pause 3.0
    parallel:
        ease 10.0 xpos 1210
        pause 2.0
        ease 10.0 xpos 710
        pause 2.0
        repeat
    parallel:
        ease 1 alpha 0.0
        pause 2.5
        ease 1.5 alpha 1.0
        pause 3
        repeat

transform boss_hint2:
    rotate 90
    block:
        parallel:
            choice:
                xoffset -10
            choice:
                xoffset -5
            choice:
                xoffset 0
            choice:
                xoffset 5
            choice:
                xoffset 10
            choice:
                xoffset 15
            choice:
                xoffset 20
            choice:
                xoffset 30
            choice:
                xoffset 40
        parallel:
            choice:
                yoffset -10
            choice:
                yoffset 0
            choice:
                yoffset 10
            choice:
                yoffset 20
            choice:
                yoffset 30
            choice:
                yoffset 35
            choice:
                yoffset 40
            choice:
                yoffset 45
        pause 0.4
        repeat

screen floating_text:
    if turns_passed % 3 is 1:
        text "Mariko brandishes her claws ...":
            xanchor 0.5
            yanchor 0.5
            xpos 710
            ypos 0.1
            at boss_hint1

    if mariko_fatigue >= 50:
        text "CRACK":
            xanchor 0.5
            yanchor 0.5
            xpos 1210
            ypos 0.8
            at boss_hint2

label nagen_turn:
    $ boss_active = boss_idle

    show screen floating_text
    call screen chapter1_boss_battle_menu

label nagen_turn_end:
    $ turn_order = mariko_turn

    return

label nagen_attacks:

    g "Nagen attacks Mariko!"

    $ boss_active = boss_hurt

    $ nagen_damage = renpy.random.randint(nagen_attack - 1, nagen_attack)

    $ mariko_current_health -= nagen_damage

    g "Hit Mariko for [nagen_damage] Damage!"

    $ mariko_fatigue += 10

    jump nagen_turn_end

label nagen_defends:

    g "Nagen prepares himself for Mariko's next attack ..."

    $ nagen_defending = True

    jump nagen_turn_end

label mariko_turn:

    $ boss_active = boss_attack

    if turns_passed % 3 is 1:

        $ mariko_next_attack = mariko_strong_attack

        g "Mariko attacks with her claws!"

    else:

        $ mariko_next_attack = mariko_weak_attack

        $ mariko_attack_line = renpy.random.choice(["Mariko goes for a punch!", "Mariko kicks Nagen with her right foot!"])

        g "[mariko_attack_line]"

    # Damage Calculation
    
    if mariko_next_attack is mariko_strong_attack:

        if mariko_fatigue < 50:

            $ mariko_damage = renpy.random.randint(8, 12)
        else:

            $ mariko_damage = renpy.random.randint(4, 6)

    elif mariko_fatigue < 50:  # Weak Attack

        $ mariko_damage = renpy.random.randint(2, 4)
        
    else:
        $ mariko_damage = renpy.random.randint(1, 3)

    # Defense Calculation
    if nagen_defending is True:

        $ nagen_defending = False

        $ mariko_damage -= nagen_defense

        if mariko_damage < 0:

            $ mariko_damage = 0

            g "Nagen was prepared and blocks the attack!"

        else:

            $ nagen_current_health -= mariko_damage

            g "Nagen was prepared and blocks most of the attack!"

            g "Nagen is hit for [mariko_damage] damage!"

    else:

        $ nagen_current_health -= mariko_damage

        g "Nagen is hit for [mariko_damage] damage!"

        

    $ mariko_fatigue += 10
    $ turn_order = nagen_turn

    return

label chapter1_boss_battle_conditions:

    $ boss_active = boss_idle

    if nagen_current_health <= 0:

        $ turn_order = round_end
        $ fight_end_state = lose

    if mariko_current_health <= 12 or mariko_fatigue >= 50:

        if mariko_halfway is False:
            
            $ mariko_halfway = True
            $ mariko_halfway_post_turns = turns_passed

            hide screen boss_overlay
            with dissolve
            
            call chapter1_boss_battle_midfight_scene

            $ info_overlay = fight_overlay2

            show screen boss_overlay
            with dissolve
        
        if mariko_current_health <= 0:

            $ turn_order = round_end
            $ fight_end_state = lose

    if mariko_fatigue >= 100:

        $ turn_order = round_end
        $ fight_end_state = win

    return

label chapter1_boss_battle_evaluations:

    if fight_end_state is win:
        
        jump chapter1_boss_player_choice

    else:

        if nagen_current_health <= 0:

            "Crap, I am too hurt ..."

            g "You Lose!"

        elif mariko_current_health <= 0:

            jump chapter1_boss_player_choice
    
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
        if turns_passed == 2:

            m "You’re making this too easy. Even the bottom left of the pyramid could deck you with one punch."

            "She says that, but she can barely move in that costume."

        elif turns_passed == 3:

            m "This isn’t going to work if you don’t fight back. C’mon! Don’t you want to save your friend?"

    elif mariko_halfway is True:
        if turns_passed == mariko_halfway_post_turns + 1:

            m "Kanon would have gone for your eyes."
        
        elif turns_passed == mariko_halfway_post_turns + 3:

            m "Did any of them think of me at all while I was looking for them? If I can just... take you down. They’ll forgive me... they’ll have to forgive me."

        elif turns_passed == mariko_halfway_post_turns + 4:

            m "Please... forgive me."

            "But I know she isn’t talking to me."

    return

label chapter1_boss_player_choice:

    menu:
        "Spare":
            jump chapter1_boss_spare
        "Punish":
            jump chapter1_boss_punish