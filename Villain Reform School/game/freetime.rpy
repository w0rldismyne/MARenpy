screen freetime:
    modal True

    hbox:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5

        imagebutton:
            xysize (456, 442)
            xpos 0.5
            ypos 0.5
            xanchor 0.5
            yanchor 0.5    
            idle "images/Interactables/Investigate_1.png"
            hover "Investigate_Hover"
            action Hide("freetime")

        imagebutton:
            xysize (456, 442)
            xpos 0.5
            ypos 0.5
            xanchor 0.5
            yanchor 0.5    
            idle "images/Interactables/Hangout_2.png"
            hover "Hangout_Hover"
            action Hide("freetime")

image Investigate_Hover:
    "images/Interactables/Investigate_1.png"
    pause 0.5
    "images/Interactables/Investigate_2.png"
    pause 0.5
    "images/Interactables/Investigate_3.png"
    pause 0.5
    repeat

image Hangout_Hover:
    "images/Interactables/Hangout_1.png"
    pause 0.5
    "images/Interactables/Hangout_3.png"
    pause 0.5
    repeat