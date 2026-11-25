# Boss Sprites
define ch2_boss_idle_p1 = "images/Sprites/Rise/Boss2.png"
define ch2_boss_attack_p1 = "images/Sprites/Rise/RiseBoss_Attack_Smile.png"
#define ch2_boss_hurt_p1 = "images/Sprites/Rise/3.png"
#define ch2_boss_idle_p2 = "images/Sprites/Rise/Boss1injured.png"
define ch2_boss_attack_p2 = "images/Sprites/Rise/RiseBoss_Attack_Frown.png"
#define ch2_boss_hurt_p2 = "images/Sprites/Rise/3injured.png"

screen boss_rise_s2(transition = False):

    image ch2_boss_attack_p1:
        xanchor 0.5
        yanchor 0.5
        pos 0.7, 0.5178
        if transition == True:
            at boss_rise_s1_s2

transform boss_rise_s1_s2:
    ypos -1.0
    easein 0.5 ypos 0.5178 

screen rise_hp_bars():

    # Rise's Health
    image "New Assets/Fight/name_others.png":
        xanchor 1.0
        yanchor 0.5
        pos 1876, 144

    text "Rise":
        xanchor 1.0
        yanchor 0.5
        pos 1866, 148

    bar:
        xanchor 0.0
        yanchor 0.5
        pos 1365, 80
        xysize 511,57
        value rise_current_hp
        range rise_hp
        left_bar "New Assets/Fight/enemy_hp_full.png"
        right_bar "New Assets/Fight/enemy_hp_empty.png"
        left_gutter 130
        right_gutter 15

    text "[rise_current_hp]/[rise_hp]":
        xanchor 1.0
        yanchor 0.5
        pos 1841, 84

    # Jona's Health
    image "New Assets/Fight/name_others.png":
        xanchor 1.0
        yanchor 0.5
        pos 1876, 284

    text "Jona":
        xanchor 1.0
        yanchor 0.5
        pos 1866, 288

    bar:
        xanchor 0.0
        yanchor 0.5
        pos 1365, 220
        xysize 511,57
        value jona_current_mp
        range jona_mp
        left_bar "New Assets/Fight/enemy_mp_full.png"
        right_bar "New Assets/Fight/enemy_mp_empty.png"
        left_gutter 130
        right_gutter 15

    text "[jona_current_mp]/[jona_mp]":
        xanchor 1.0
        yanchor 0.5
        pos 1841, 224

# Nagen's Available Actions
screen chapter2_boss_battle_menu():

    # Attack Button
    imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_attacks"):
        focus_mask True
        idle "New Assets/Fight/attack_idle.png"
        hover "New Assets/Fight/attack_hover.png"
        xanchor 0.0
        yanchor 0.5
        ypos 630
        xysize 405, 132
        at attack_button2

    if rise_vulnerable == False:

        # Hide Button
        imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_hides"):
            focus_mask True
            idle "New Assets/Fight/blank_button_idle.png"
            hover "New Assets/Fight/blank_hover.png"
            xanchor 0.0
            yanchor 0.5
            ypos 735
            xysize 437, 165
            at hide_button

        text "Hide":
            xanchor 0.0
            yanchor 0.5
            size 80
            pos 180, 760

    else:
        # Defend Button
        imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_defends"):
            focus_mask True
            idle "New Assets/Fight/blank_button_idle.png"
            hover "New Assets/Fight/blank_hover.png"
            xanchor 0.0
            yanchor 0.5
            ypos 735
            xysize 437, 165
            at hide_button

        text "Defend":
            xanchor 0.0
            yanchor 0.5
            size 80
            pos 180, 760

    # Flee Button
    imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_flees"):
        focus_mask True
        idle "New Assets/Fight/defend_idle.png"
        hover "New Assets/Fight/defend_hover.png"
        xanchor 0.0
        yanchor 0.5
        ypos 860
        xysize 405, 132
        at flee_button

    text "Flee":
        color "#000000"
        xanchor 0.0
        yanchor 0.5
        size 80
        pos 180, 850

transform attack_button2:
    alpha 0.0 xpos -405
    linear 0.15 alpha 1.0 xpos 40

transform hide_button:
    alpha 0.0 xpos -381 rotate 3
    pause 0.07
    linear 0.13 alpha 1.0 xpos 30

transform flee_button:
    alpha 0.0 xpos -361
    pause 0.14
    linear 0.13 alpha 1.0 xpos 60

# Attributes
default jona_current_mp = 100
default jona_mp = 100
default rise_current_hp = 100
default rise_hp = 100

# Fight State Variables
default rise_encounter = -1
default encounter_questions = 5
default rise_vulnerable = False
default rise_halfway = False

default current_maze = maze

default rise_eyes = {
    48: fine,
    57: fine,
    83: fine,
    85: fine
}

default tile_events = {
    1: False,
    2: False,
    3: False,
    4: False
}

define fine = 0
define hurt = 1
define badly_hurt = 2

# Fight Resolution

# Location
define maze = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0,
    0, 1, 2, 1, 2, 1, 2, 2, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
    0, 1, 0, 2, 3, 0, 1, 2, 0, 0, 0,
    0, 1, 3, 0, 0, 1, 1, 1, 2, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 2, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

define maze2 = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 2, 1, 2, 1, 2, 2, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0,
    0, 1, 0, 2, 3, 0, 1, 2, 0, 1, 0,
    0, 1, 3, 0, 0, 1, 1, 1, 2, 1, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 1, 2, 0, 1, 0, 3, 0, 3, 1, 0,
    0, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

define maze_region = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 3, 3, 3, 1, 1, 4, 4, 4, 0, 0,
    0, 3, 0, 3, 0, 1, 0, 0, 4, 4, 0,
    0, 3, 3, 3, 1, 1, 1, 1, 0, 4, 0,
    0, 3, 0, 0, 0, 0, 1, 0, 0, 4, 0,
    0, 3, 0, 0, 0, 1, 1, 1, 0, 4, 0,
    0, 3, 0, 1, 1, 1, 0, 1, 0, 4, 0,
    0, 3, 0, 0, 1, 0, 0, 0, 0, 4, 0,
    0, 2, 2, 2, 1, 0, 2, 2, 0, 4, 0,
    0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

default maze_minimap = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

define wall = 0
define empty_tile = 1
define not_eyes = 2
define eyes = 3

define starting_position = 61
default direction = None
default current_position = None
default region = None

default valid_left = None
default valid_forward = None
default valid_right = None
default valid_back = None

# Direction Constants
define west = 0
define north = 1
define east = 2
define south = 3

# Movement Constants
define move_west = -1
define move_north = -11
define move_east = 1
define move_south = 11

## Relative Direction Offsets
define turn_left =   { north: west,  west:  south, south: east, east: north }
define turn_right =  { north: east,  east:  south, south: west, west: north }
#define turn_around = { north: south, south: north, east:  west, west: east  }

image lfr4 = "images/Interactables/Maze/MazeAll.png"
image lf4 = "images/Interactables/Maze/MazeForwardLeft.png"
image lr4 = "images/Interactables/Maze/MazeLeft_Right.png"
image l4 = "images/Interactables/Maze/MazeLeft.png"
image fr4 = "images/Interactables/Maze/MazeForwardRight.png"
image f4 = "images/Interactables/Maze/MazeForwardBack.png"
image r4 = "images/Interactables/Maze/MazeRight.png"
image d = "images/Interactables/Maze/Mazedeadend.png"

image lfr1 = "images/Interactables/Maze/MazeAllDark.png"
image lf1 = "images/Interactables/Maze/MazeForwardLeftDark.png"
image lr1 = "images/Interactables/Maze/MazeLeft_RightDark.png"
image l1 = "images/Interactables/Maze/MazeLeftDark.png"
image fr1 = "images/Interactables/Maze/MazeForwardRightDark.png"
image f1 = "images/Interactables/Maze/MazeForwardBackDark.png"
image r1 = "images/Interactables/Maze/MazeRightDark.png"
#mage d1 = "images/Interactables/Maze/MazedeadendDark.png"

image lfr2 = "images/Interactables/Maze/MazeAllPale.png"
image lf2 = "images/Interactables/Maze/MazeForwardLeftPale.png"
image lr2 = "images/Interactables/Maze/MazeLeft_RightPale.png"
image l2 = "images/Interactables/Maze/MazeLeftPale.png"
image fr2 = "images/Interactables/Maze/MazeForwardRightPale.png"
image f2 = "images/Interactables/Maze/MazeForwardBackPale.png"
image r2 = "images/Interactables/Maze/MazeRightPale.png"
#image d2 = "images/Interactables/Maze/MazedeadendPale.png"

image lfr3 = "images/Interactables/Maze/MazeAllWarm.png"
image lf3 = "images/Interactables/Maze/MazeForwardLeftWarm.png"
image lr3 = "images/Interactables/Maze/MazeLeft_RightWarm.png"
image l3 = "images/Interactables/Maze/MazeLeftWarm.png"
image fr3 = "images/Interactables/Maze/MazeForwardRightWarm.png"
image f3 = "images/Interactables/Maze/MazeForwardBackWarm.png"
image r3 = "images/Interactables/Maze/MazeRightWarm.png"
#image d3 = "images/Interactables/Maze/MazedeadendWarm.png"

# Eyeball Wall
image e4 = "images/Interactables/Maze/MazeForwardWall.png"
image e1 = "images/Interactables/Maze/MazeForwardWallDark.png"
image e2 = "images/Interactables/Maze/MazeForwardWallPale.png"
image e3 = "images/Interactables/Maze/MazeForwardWallWarm.png"

# Relative Position Offsets - Array of Dictionaries
define move_offsets = {
    west:  { "Left": move_south, "Forward": move_west,  "Right": move_north, "Backward": move_east},
    north: { "Left": move_west,  "Forward": move_north, "Right": move_east,  "Backward": move_south},
    east:  { "Left": move_north, "Forward": move_east,  "Right": move_south, "Backward": move_west},
    south: { "Left": move_east,  "Forward": move_south, "Right": move_west,  "Backward": move_north}
}

screen maze_minimap_display():
    frame:
        xsize 425
        ysize 425
        xpos 0.95
        ypos 0.85
        xanchor 1.0
        yanchor 1.0
        padding (0, 0)
        background "images/Interactables/Maze/map_frame.png"
        fixed:
            xsize 395
            ysize 395
            xalign 0.5
            yalign 0.5
            grid 11 11:
                xalign 0.5
                yalign 0.5
                spacing 1
                for tile in maze_minimap:
                    if tile == 1:
                        image "images/Interactables/Maze/maze_tile.png":
                            xsize 35
                            ysize 35
                    elif tile == 2:
                        image "images/Interactables/Maze/maze_tile.png" at darker:
                            xsize 35
                            ysize 35
                    else:
                        null
            add "images/Interactables/Maze/maze_observer_large.png":
                xsize 34
                ysize 34
                xanchor 0.5
                yanchor 0.5
                xoffset 17.5
                yoffset 17.5
                xpos current_position%11 * 36
                ypos int(current_position/11) * 36
                if direction == 0:
                    rotate -90
                elif direction == 1:
                    rotate 0
                elif direction == 2:
                    rotate 90
                else:
                    rotate 180

screen maze_control():

    if valid_forward:
        key "w" action Return("Move Forward")
    #if valid_left:
    #    key "a" action Return("Move Left")
    #if valid_back:
    #    key "s" action Return("Move Backward")
    #if valid_right:
    #    key "d" action Return("Move Right")
    key "a" action Return("Turn Left")
    key "d" action Return("Turn Right")

# Question Setup
default questions = []

label chapter2_boss_battle_initial:

    $ direction = north
    $ current_position = starting_position
    $ region = maze_region[current_position]

    $ questions = [1, 2, 3, 4]
    $ renpy.random.shuffle(questions)
    $ questions.append(5)

    $ rise_encounter = renpy.random.randint(12, 18)

    $ nagen_hp = 12
    $ nagen_current_hp = 12

    $ fight_end_state = -1

    show screen nagen_hp_bars()
    show screen rise_hp_bars()
    show screen maze_minimap_display()
    with Dissolve(0.1)

    show screen ch2_tutorial()

    $ maze_minimap[current_position] = 1

    jump chapter2_boss_battle_explore_loop

label chapter2_boss_maze_background:
    if current_maze[current_position + move_offsets[direction]["Forward"]] == eyes:
        if rise_eyes[current_position + move_offsets[direction]["Forward"]] != fine:
            scene mazeeyes
        else:
            scene mazegoalwall
    else:
        scene mazerose

    $ valid_left = current_maze[current_position + move_offsets[direction]["Left"]] != wall
    $ valid_forward = current_maze[current_position + move_offsets[direction]["Forward"]] != wall
    $ valid_right = current_maze[current_position + move_offsets[direction]["Right"]] != wall
    $ valid_back = current_maze[current_position + move_offsets[direction]["Backward"]] == empty_tile

    if current_maze[current_position] == eyes:
        if rise_eyes[current_position] != fine:
            show mazeeyes
        else:
            show mazegoalwall
    elif current_maze[current_position] == not_eyes:
        show mazerose
    elif current_maze[current_position + move_offsets[direction]["Forward"]] == eyes or current_maze[current_position + move_offsets[direction]["Forward"]] == not_eyes:
        show expression ("e" + "[region]")
    elif valid_left and valid_forward and valid_right:
        show expression ("lfr" + "[region]")
    elif valid_left and valid_forward:
        show expression ("lf" + "[region]")
    elif valid_left and valid_right:
        show expression ("lr" + "[region]")
    elif valid_forward and valid_right:
        show expression ("fr" + "[region]")
    elif valid_left:
        show expression ("l" + "[region]")
    elif valid_forward:
        show expression ("f" + "[region]")
    elif valid_right:
        show expression ("r" + "[region]")
    else:
        show d

    return

label chapter2_boss_battle_explore_loop:

    call chapter2_boss_maze_background

    $ encounter_type = renpy.random.randint(1, 2)

    if current_position == 19 and tile_events[1] == False:
        $ rise_encounter = 0
        $ encounter_type = 1
    elif current_position == 31 and tile_events[2] == False:
        $ rise_encounter = 0
        $ encounter_type = 1
    elif current_position == 53 and tile_events[3] == False:
        $ rise_encounter = 0
        $ encounter_type = 1
    elif current_position == 75 and tile_events[4] == False:
        $ rise_encounter = 0
        $ encounter_type = 1

    if rise_encounter <= 0 and current_maze[current_position] == empty_tile:
        $ rise_encounter = renpy.random.randint(8, 18)
        hide screen maze_minimap_display with dissolve
        if encounter_type == 1 and encounter_questions > 0:
            call chapter2_boss_battle_encounter1
        else:
            call chapter2_boss_battle_encounter2_initial
        show screen maze_minimap_display() with dissolve

    if current_maze[current_position] == eyes or current_maze[current_position] == not_eyes:
        hide screen maze_minimap_display with dissolve
        $ maze_minimap[current_position] = 2
        call chapter2_boss_battle_eye()
        show screen maze_minimap_display() with dissolve
    else:
        $ maze_minimap[current_position] = 1
        $ input = renpy.call_screen("maze_control")

    $ renpy.restart_interaction()

    if fight_end_state != -1:
        hide screen ch2_tutorial
        hide screen boss_rise_s2
        hide screen boss_overlay
        hide screen nagen_hp_bars
        hide screen rise_hp_bars
        hide screen maze_minimap_display
        jump chapter2_boss_battle_resolutions

    if input == "Move Forward":
        $ current_position += move_offsets[direction]["Forward"]
        $ rise_encounter-= 1
    #elif input == "Move Left":
    #    $ current_position += move_offsets[direction]["Left"]
    #    $ rise_encounter-= 1
    #elif input == "Move Right":
    #    $ current_position += move_offsets[direction]["Right"]
    #    $ rise_encounter-= 1

        # Required for moving back in eye scenes
    elif input == "Move Backward":
        $ current_position += move_offsets[direction]["Backward"]
        $ rise_encounter-= 1
    elif input == "Turn Left":
        $ direction = turn_left[direction]
    elif input == "Turn Right":
        $ direction = turn_right[direction]

    $ region = maze_region[current_position]
    
    jump chapter2_boss_battle_explore_loop

label chapter2_boss_battle_eye:
    if current_position in rise_eyes:
        if rise_eyes[current_position] != fine:
            scene mazeeyes
    menu:
        "Inspect the wall":
            if current_maze[current_position] == eyes:
                n "I am getting the feeling that something is watching me."
            else:
                n "I don't see anything out of the ordinary here."
            jump chapter2_boss_battle_eye
        "Attack the wall":
            if current_maze[current_position] == eyes:
                scene mazeeyes with Dissolve(0.2)
                $ rise_vulnerable = True
                call chapter2_boss_battle_encounter2_initial
                $ input = "None"
            else:
                g "Nothing happens."
                jump chapter2_boss_battle_eye
        "Go back":
            $ input = "Move Backward"
            return
    return

label chapter2_boss_battle_encounter1:
    #Question

    show rise boss guard talk with dissolve
    if rise_halfway == True:
        jump phone_events

    $ question = questions.pop()
    $ encounter_questions -= 1

    if question == 1:
        
        r "You are just too close to the situation to realize you are being used. Let me protect you."

        hide rise

        menu:
            "This again?":

                show rise boss guard talk

                n "I never asked for your help or protection."
                n "My friends aren't using me, I'm trying to help them because I want to."
            
            "Maybe":
                $ jona_current_mp -= 35
                if jona_current_mp <= 0:
                    $ jona_current_mp = 0
                    $ fight_end_state = lose
                n "Even if I did want help, this is definitely not helping."
                n "How do I know you're not going to use me too."

    elif question == 2:

        r "You were in my position once, with no one to rely on. Why do you refuse to see the ends justify the means?"

        hide rise

        menu: 
            "Not like this":

                show rise boss guard talk
                $ jona_current_mp -= 35
                if jona_current_mp <= 0:
                    $ jona_current_mp = 0
                    $ fight_end_state = lose
                n "This... this isn't the same as back then."
                n "No one was in danger until you started shit again."
                n "You're hurting way more people than you're helping"
            
            "You chose not to rely on anyone":

                show rise boss guard talk

                n "You're the one that won't talk to your old friends."
                n "You didn't even bother to make new ones."
                n "The reason you think you're alone is you keep choosing to be."

    elif question == 3:

        r "He hurt so many people. He lied to you so you would defend him."

        hide rise

        menu:
            "He didn't have to":

                show rise boss guard talk
                $ jona_current_mp -= 35
                if jona_current_mp <= 0:
                    $ jona_current_mp = 0
                    $ fight_end_state = lose
                n "I'd defend him regardless."
                n "People like you always pick on guys weaker than them."
            
            "He doesn't lie":

                show rise boss guard talk
                
                n "He hasn't said anything hoping you'd give up and be normal!"
                "I didn't think it would work, but he certainly wasn't manipulating me into being here."
                n "I may not always understand him, but I know he'd never lie to me."
                n "You're the one making stuff up about my friends."

    elif question == 4:

        r "I should have been more clear; this will not kill you. It will just put you to sleep for a while."
        r "Be a dear and step into one of those clouds. I really would like to avoid hurting you."

        hide rise

        menu:
            "I'm not giving up!":

                show rise boss guard talk
                
                n "I'm not turing a blind eye to this."
                n "You're blaming someone else for your family's failings."
            
            "-hesitate-":

                show rise boss guard talk

                $ jona_current_mp -= 35
                if jona_current_mp <= 0:
                    $ jona_current_mp = 0
                    $ fight_end_state = lose
                n "I'm not turing a blind eye to this."
                n "You're blaming someone else for your family's failings."

    elif question == 5:

        r "My parents may not have been the best people, but they did not deserve to die just because he said so. I'm trying to make things better."

        hide rise

        menu:
            "Yeah, for you":

                show rise boss guard talk

                n "Not the best people?"
                n "They used their money to hurt people on purpose."
                n "All Jona ever did was point out where 'rich people' were throwing their money."
                n "If other people thought it was that included your parents, they're the problem, not him."
            
            "He didn't mean it":

                show rise boss guard talk

                $ jona_current_mp -= 35
                if jona_current_mp <= 0:
                    $ jona_current_mp = 0
                    $ fight_end_state = lose
                n "People took a metaphor out of context."
                n "He never asked people to literally kill them."
                n "We all just wanted one thing in Guwon to not be horrible."

    hide rise

    return

label phone_events:
    if tile_events[1] == False:
        call chapter2_boss_battle_tile_event1
        $ tile_events[1] = True
        hide rise
        return
    elif tile_events[2] == False:
        call chapter2_boss_battle_tile_event2
        $ tile_events[2] = True
        hide rise
        return
    elif tile_events[3] == False:
        call chapter2_boss_battle_tile_event3
        $ tile_events[3] = True
        hide rise
        return
    elif tile_events[4] == False:
        call chapter2_boss_battle_tile_event4
        $ tile_events[4] = True
        hide rise
        return

label chapter2_boss_battle_encounter2_initial:

    if rise_vulnerable is True:
        if rise_eyes[current_position] == fine:
            r "Ow! Stupid contacts."
            $ rise_eyes[current_position] = hurt
            $ rise_current_hp -= 10
        elif rise_eyes[current_position] == hurt:
            r "Nagen, stop! It burns! Please!"
            $ rise_eyes[current_position] = badly_hurt
            $ rise_current_hp -= 25
        else:
            r "F-fuck, I can't get them out! I-I can't see. It hurts so much."
            $ rise_current_hp -= 100
        if rise_current_hp <= 0:
            $ rise_current_hp = 0
            $ fight_end_state = lose
            return
    else:
        r "I found you!"

    show screen boss_rise_s2(True) zorder -1

    pause 0.5

    hide screen boss_rise_s2
    show screen boss_rise_s2() zorder -1
    
    show screen boss_overlay() zorder -1
    with dissolve

    $ turn_order = nagen_turn

    jump chapter2_boss_battle_encounter2_loop

label chapter2_boss_battle_encounter2_loop:
    while turn_order is not round_end:
        call ch2_nagen_turn
    $ rise_vulnerable = False
    call chapter2_boss_battle_evaluations
    return

label chapter2_boss_battle_evaluations:

    if rise_current_hp <= 0:
        $ fight_end_state = lose
    elif rise_eyes[85] != fine:
        $ fight_end_state = win
    elif rise_eyes[48] != fine and rise_eyes[57] != fine and rise_eyes[83] != fine and rise_halfway == False:
        $ rise_halfway = True

        call chapter2_boss_battle_midfight_scene

        $ current_maze = maze2
        $ temp_counter = 0
        while temp_counter < len(maze_minimap):
            if maze_minimap[temp_counter] == 2:
                $ maze_minimap[temp_counter] = 0
            $ temp_counter += 1
    return

label chapter2_boss_battle_resolutions:
    if fight_end_state == lose:
        jump chapter2_boss_punish
    elif fight_end_state == win:
        jump chapter2_boss_spare

label ch2_nagen_turn:

    call screen chapter2_boss_battle_menu()

label ch2_nagen_attacks:

    g "Nagen focuses and tries to punch Rise..."

    if rise_vulnerable == True:

        $ rise_current_hp -= 5

        if rise_current_hp <= 0:
            $ rise_current_hp = 0

        g "It hits, dealing 5 damage!"

        if rise_current_hp <= 0:
            $ turn_order = round_end
            return

        jump rise_post_vulnerable

    else:

        g "...but Nagen misses!"

        g "Rise lightly kicks Nagen in response."

        $ rise_damage = renpy.random.randint(1, 2)

        $ nagen_current_hp -= rise_damage

        g "Nagen is hit for [rise_damage] damage!"

        "The jetpack is making it too hard for me to hit her..."

        return

label ch2_nagen_hides:

    g "Nagen waits for an opportunity..."

    g "Rise throws a grenade and it explodes!"

    $ rise_damage = renpy.random.randint(1, 3)
    $ nagen_current_hp -= rise_damage

    g "Nagen is partially hit for [rise_damage] damage!"

    hide screen boss_rise_s2
    hide screen boss_overlay
    show backgroundblack zorder 1
    show smoke zorder 1
    with dissolve

    $ direction = renpy.random.randint(0, 3)

    call chapter2_boss_maze_background
    show backgroundblack zorder 1
    show smoke zorder 1

    g "Nagen hides nearby using the explosion's smoke."

    $ maze_minimap[current_position - 12] = 0
    $ maze_minimap[current_position - 11] = 0
    $ maze_minimap[current_position - 10] = 0
    $ maze_minimap[current_position - 1] = 0
    $ maze_minimap[current_position + 1] = 0
    $ maze_minimap[current_position + 10] = 0
    $ maze_minimap[current_position + 11] = 0
    $ maze_minimap[current_position + 12] = 0

    hide backgroundblack with dissolve

    hide smoke with dissolve

    g "Rise flies away."

    $ turn_order = round_end

    return

label ch2_nagen_defends:
    g "Nagen braces himself for Rise's next attacks..."
    
    g "However..."

    jump rise_post_vulnerable

label ch2_nagen_flees:

    g "Nagen starts running away!"

    hide screen boss_rise_s2
    hide screen boss_overlay
    show backgroundblack zorder 1
    with dissolve

    $ renpy.pause(2.0, hard = True)

    g "After a while, Nagen manages to lose Rise in the maze."

    $ direction = renpy.random.randint(0, 3)
    $ current_position = renpy.random.randint(0, 120)
    while maze[current_position] != 1:
        $ current_position = renpy.random.randint(0, 120)
    $ region = maze_region[current_position]

    call chapter2_boss_maze_background
    show backgroundblack zorder 1

    hide backgroundblack with dissolve

    "I should be safer now."

    $ turn_order = round_end

    return

label rise_post_vulnerable:

    hide screen boss_rise_s2
    hide screen boss_overlay
    show backgroundblack zorder 1
    with dissolve

    g "Rise recovers and flies away promptly."

    hide backgroundblack with dissolve

    $ turn_order = round_end

    return

#label ch2_rise_turn:
#    return

#screen ch2_boss_sandbox_actions:
    # Ask questions -> wrong answer depletes Jona's mp
    # Event counter, events will always fire near the exit
    # Ask questions -> damages Jona's MP -> correct answer restores Jona's MP
    # Rise will never fly down, Rise will only fly down during the last boss fight
    # jona will heal nagen as well after the questions from the events are answered correctly
    # if jona's mp ever hits 0 automatic game over
    # jona will provide hints maybe more detailed after finishing the event questions
    # only 1 eye wall in phase 2
    # around 4 events for the questions in phase 2