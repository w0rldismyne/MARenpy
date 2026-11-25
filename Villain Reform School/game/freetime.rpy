label freetime:

    if chapter_event is chapter1_free_time_morning_break:
        scene backgroundschool
    elif chapter_event is chapter1_free_time_after_school:
        scene backgroundschoolnoon
    elif chapter_event is chapter1_free_time_evening:
        scene backgroundcourtyardnight

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
            action Jump("investigation_board")

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
            action Jump("hangout_area")

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

label hangout_area:
    scene nagenhouse
    "Who should I hang out with right now?"

    $ choice_many_choices = True

    menu:
        extend ""
        "By Myself":
            $ choice_many_choices = False
            return
        "Chisei":
            $ choice_many_choices = False
            jump ChiseiVisit
        "Hiro":
            $ choice_many_choices = False
            jump HiroVisit
        "Jona":
            $ choice_many_choices = False
            jump JonaVisit
        "Kitsune":
            $ choice_many_choices = False
            jump KitsuneVisit
        "Mariko":
            $ choice_many_choices = False
            jump MarikoVisit
        "Momoko":
            $ choice_many_choices = False
            jump MomokoVisit
        "Nanase":
            $ choice_many_choices = False
            jump NanaseVisit
        "Rise":
            $ choice_many_choices = False
            jump RiseVisit
        "Taiga":
            $ choice_many_choices = False
            jump TaigaVisit
        "Uitto":
            $ choice_many_choices = False
            jump UittoVisit
        "Yoku":
            $ choice_many_choices = False
            jump YokuVisit