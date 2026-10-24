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
        idle "New Assets/Fight/attack_idle.png"
        hover "New Assets/Fight/attack_hover.png"
        xanchor 0.0
        yanchor 0.5
        pos 40, 630
        xysize 405, 132
        at attack_button

    # Dodge Button
    imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_dodges"):
        idle "New Assets/Fight/defend_idle.png"
        hover "New Assets/Fight/defend_hover.png"
        xanchor 0.0
        yanchor 0.5
        pos 45, 735
        xysize 371, 87
        at dodge_button

    # Flee Button
    imagebutton action Hide("chapter2_boss_battle_menu"), Jump("ch2_nagen_flees"):
        idle "New Assets/Fight/defend_idle.png"
        hover "New Assets/Fight/defend_hover.png"
        xanchor 0.0
        yanchor 0.5
        pos 50, 840
        xysize 371, 87
        at flee_button

transform attack_button2:
    alpha 0.0 xpos -405
    linear 0.15 alpha 1.0 xpos 40

transform dodge_button:
    alpha 0.0 xpos -376
    pause 0.07
    linear 0.13 alpha 1.0 xpos 45

transform flee_button:
    alpha 0.0 xpos -371
    pause 0.14
    linear 0.13 alpha 1.0 xpos 50

# Attributes
default jona_current_mp = 100
default jona_mp = 100
default rise_current_hp = 100
default rise_hp = 100

# Fight State Variables
default rise_encounter = -1
default encounter_questions = 5

# Fight Resolution

# Location
define maze = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 2, 0, 1, 0, 1, 0, 1, 1, 2, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
)

define maze2 = (
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
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
)

define maze_region = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0,
    0, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0,
    0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 2, 2, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 3, 0, 1, 0, 1, 1, 0, 0,
    0, 3, 0, 3, 0, 1, 1, 1, 0, 0, 0,
    0, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0,
    0, 0, 3, 0, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
)

define wall = 0
define empty_tile = 1
define eyes = 2

define starting_position = 71
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
image e = "images/Backgrounds/mazegoalwall.png"
image e0 = "images/Interactables/Maze/MazeForwardWall.png"
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

screen maze_control():

    if valid_forward:
        key "w" action Return("Move Forward")
    if valid_left:
        key "a" action Return("Move Left")
    if valid_back:
        key "s" action Return("Move Backward")
    if valid_right:
        key "d" action Return("Move Right")
    key "q" action Return("Turn Left")
    key "e" action Return("Turn Right")

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

    $ nagen_health = 12
    $ nagen_current_health = 12

    show screen nagen_hp_bars
    show screen rise_hp_bars
    with Dissolve(0.1)

    jump chapter2_boss_battle_explore_loop

label chapter2_boss_maze_background:
    $ valid_left = maze[current_position + move_offsets[direction]["Left"]] == empty_tile
    $ valid_forward = maze[current_position + move_offsets[direction]["Forward"]] == empty_tile
    $ valid_right = maze[current_position + move_offsets[direction]["Right"]] == empty_tile
    $ valid_back = maze[current_position + move_offsets[direction]["Backward"]] == empty_tile

    if maze[current_position] == eyes:
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
        if maze[current_position + move_offsets[direction]["Forward"]] == eyes:
            show e0
        else:
            show expression ("f" + "[region]")
    elif valid_right:
        show expression ("r" + "[region]")
    else:
        show d

    return

label chapter2_boss_battle_explore_loop:

    scene mazerose
    call chapter2_boss_maze_background

    if rise_encounter == 0:
        $ rise_encounter = renpy.random.randint(8, 18)
        $ encounter_type = renpy.random.randint(1, 2)
        if encounter_type == 1 and encounter_questions > 0:
            call chapter2_boss_battle_encounter1
        else:
            call chapter2_boss_battle_encounter2_initial

    $ input = renpy.call_screen("maze_control")

    if input == "Move Forward":
        $ current_position += move_offsets[direction]["Forward"]
        $ rise_encounter-= 1
    elif input == "Move Left":
        $ current_position += move_offsets[direction]["Left"]
        $ rise_encounter-= 1
    elif input == "Move Right":
        $ current_position += move_offsets[direction]["Right"]
        $ rise_encounter-= 1
    elif input == "Move Backward":
        $ current_position += move_offsets[direction]["Backward"]
        $ rise_encounter-= 1
    elif input == "Turn Left":
        $ direction = turn_left[direction]
    elif input == "Turn Right":
        $ direction = turn_right[direction]

    $ region = maze_region[current_position]
    
    jump chapter2_boss_battle_explore_loop

label chapter2_boss_battle_encounter1:
    #Question

    $ question = questions.pop()
    $ encounter_questions -= 1

    show rise boss guard talk with dissolve

    if question == 1:
        
        r "You are just too close to the situation to realize you are being used. Let me protect you."

        hide rise

        menu:
            "This again?":

                show rise boss guard talk

                n "I never asked for your help or protection."
                n "My friends aren't using me, I'm trying to help them because I want to."
            
            "Maybe":
                #bad end point
                n "Even if I did want help, this is definitely not helping."
                n "How do I know you're not going to use me too."

    elif question == 2:

        r "You were in my position once, with no one to rely on. Why do you refuse to see the ends justify the means?"

        hide rise

        menu: 
            "Not like this":

                show rise boss guard talk
                #bad end point
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
                #bad end point
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

                #bad end point
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

                #bad end point
                n "People took a metaphor out of context."
                n "He never asked people to literally kill them."
                n "We all just wanted one thing in Guwon to not be horrible."

    hide rise

    return

label chapter2_boss_battle_encounter2_initial:

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

    return

#label chapter2_boss_battle_encounter2_resolution:
#
#    hide screen boss_overlay
#    with dissolve
#
#    return

label ch2_nagen_turn:

    call screen chapter2_boss_battle_menu()

label ch2_nagen_attacks:

    g "Nagen focuses and tries to punch Rise..."

    g "...but Nagen misses!"

    g "Rise lightly kicks Nagen in response."

    $ rise_damage = renpy.random.randint(1, 2)

    $ nagen_current_hp -= rise_damage

    g "Nagen is hit for [rise_damage] damage!"

    "The jetpack is making it too hard for me to hit her..."

    return

label ch2_nagen_dodges:

    g "Nagen waits for an opportunity..."

    g "Rise throws a grenade and it explodes!"

    $ rise_damage = renpy.random.randint(1, 2)

    g "Nagen is partially hit for [rise_damage] damage!"

    hide screen boss_rise_s2
    hide screen boss_overlay
    show backgroundblack zorder 1
    with dissolve

    $ possible_tiles = []
    if valid_forward:
        $ possible_tiles.append(move_offsets[direction]["Forward"])
    if valid_left:
        $ possible_tiles.append(move_offsets[direction]["Left"])
    if valid_back:
        $ possible_tiles.append(move_offsets[direction]["Backward"])
    if valid_right:
        $ possible_tiles.append(move_offsets[direction]["Right"])
    
    $ current_position += renpy.random.choice(possible_tiles)
    $ direction = renpy.random.randint(0, 3)
    $ region = maze_region[current_position]

    call chapter2_boss_maze_background

    g "Nagen hides nearby using the explosion's smoke."

    hide backgroundblack with dissolve

    g "Rise flies away."

    $ turn_order = round_end

    return

label ch2_nagen_flees:

    g "Nagen starts running away!"

    hide screen boss_rise_s2
    hide screen boss_overlay
    show backgroundblack zorder 1
    with dissolve

    $ renpy.pause(2.5, hard = True)

    g "After a while, Nagen manages to lose Rise in the maze."

    $ direction = north
    $ current_position = starting_position
    $ region = maze_region[current_position]

    call chapter2_boss_maze_background

    hide backgroundblack with dissolve

    "This place seems familiar..."

    $ turn_order = round_end

    return

#label ch2_rise_turn:
#    return

#screen ch2_boss_sandbox_actions:
    # Attack/Flee/Ask Jona/Hit Eye
    # Ask questions -> wrong answer depletes Jona's mp
    # If Rise catches nagen, make them run back to spawn
    # Hit Rise's wall too much -> game over, normally flying so can't hit, hit eye wall once will bring her down
    # total of 3 eye walls in the first phase
    # nagen can choose to either dodge or tank hits from rise's flying bomb attack, will always make nagen change direction, dodging will move nagen 1-2 spaces from where he was attacked
    # Phase 2 (post mid fight cutscene)
    # Event counter, events will always fire near the exit
    # Ask questions -> damages Jona's MP -> correct answer restores Jona's MP
    # Rise will never fly down, Rise will only fly down during the last boss fight
    # jona will heal nagen as well after the questions from the events are answered correctly
    # if jona's mp ever hits 0 automatic game over
    # jona will provide hints maybe more detailed after finishing the event questions
    # only 1 eye wall in phase 2
    # around 4 events for the questions in phase 2
    # the map gets bigger, more like an extension from phase 1-> phase 2 post mid fight cutscene
