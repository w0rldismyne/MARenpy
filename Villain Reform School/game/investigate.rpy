default reveal1 = False
default reveal2 = False
default reveal3 = False
default reveal4 = False
default reveal5 = False

screen investigate:
    modal True

    image "#FFFFFF"

    text "WE HERE":
        xpos 0.5
        ypos 0.85
        xanchor 0.5
        yanchor 0.5
        size 55

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Clues/Manga_Ch1_Panel_1.png"
        hover "images/Clues/Manga_Ch1_Panel_1.png"
        if reveal1 is False:
            foreground "images/Clues/Manga_Ch1_Panel_1black.png"
        action SetVariable("reveal1", not reveal1), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Clues/Manga_Ch1_Panel_2.png"
        hover "images/Clues/Manga_Ch1_Panel_2.png"
        if reveal2 is False:
            foreground "images/Clues/Manga_Ch1_Panel_2black.png"
        action SetVariable("reveal2", not reveal2), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Clues/Manga_Ch1_Panel_3.png"
        hover "images/Clues/Manga_Ch1_Panel_3.png"
        if reveal3 is False:
            foreground "images/Clues/Manga_Ch1_Panel_3black.png"
        action SetVariable("reveal3", not reveal3), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Clues/Manga_Ch1_Panel_4.png"
        hover "images/Clues/Manga_Ch1_Panel_4.png"
        if reveal4 is False:
            foreground "images/Clues/Manga_Ch1_Panel_4black.png"
        action SetVariable("reveal4", not reveal4), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Clues/Manga_Ch1_Panel_5.png"
        hover "images/Clues/Manga_Ch1_Panel_5.png"
        if reveal5 is False:
            foreground "images/Clues/Manga_Ch1_Panel_5black.png"
        action SetVariable("reveal5", not reveal5), renpy.restart_interaction
