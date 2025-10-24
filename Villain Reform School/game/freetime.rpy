default next_scene = None

label chapter1_freetime:

    if chapter1_event is chapter1_free_time_morning_break:
        scene backgroundschool
    elif chapter1_event is chapter1_free_time_after_school:
        scene backgroundschoolnoon
    elif chapter1_event is chapter1_free_time_evening:
        scene backgroundcourtyardnight

    # Reset clipboard animation
    $ clipboard = True

    call screen freetime

    return

default selected_freetime_action = ""

screen freetime:
    modal True

    text "[selected_freetime_action]":
        xpos 0.5
        ypos 0.85
        xanchor 0.5
        yanchor 0.5
        size 55
        color "#EEEEEE"

    hbox:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        spacing 60

        imagebutton:
            xysize 456, 442
            xpos 0.5
            ypos 0.5
            xanchor 0.5
            yanchor 0.5    
            idle "images/Interactables/Investigate.png"
            hover "Investigate_Hover"
            hovered SetVariable("selected_freetime_action", "Investigate"), renpy.restart_interaction
            unhovered SetVariable("selected_freetime_action", ""), renpy.restart_interaction
            action Jump("investigation_interaction_mode")

        imagebutton:
            xysize 456, 442
            xpos 0.5
            ypos 0.5
            xanchor 0.5
            yanchor 0.5    
            idle "images/Interactables/Hangout.png"
            hover "Hangout_Hover"
            hovered SetVariable("selected_freetime_action", "Hang Out"), renpy.restart_interaction
            unhovered SetVariable("selected_freetime_action", ""), renpy.restart_interaction

image Investigate_Hover:
    xysize (501, 486)
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5    
    "images/Interactables/Investigate_Highlight_1.png"
    pause 0.6
    "images/Interactables/Investigate_Highlight_2.png"
    pause 0.6
    "images/Interactables/Investigate_Highlight_3.png"

image Hangout_Hover:
    xysize (501, 486)
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    "images/Interactables/Hangout_Highlight.png"
    pause 0.5
    block:
        "images/Interactables/Hangout_Highlight_1.png"
        pause 0.7
        "images/Interactables/Hangout_Highlight_2.png"
        pause 0.7
        repeat