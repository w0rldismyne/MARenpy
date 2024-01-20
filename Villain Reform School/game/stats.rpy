style Stats:
    color "#000000"
    hover_color "#1215CF"

screen stats():

    modal True
    image "images/Clues/Cork.png"

    # Return Button
    textbutton _("Return") action Hide("stats"):
        xalign 1.0
        yalign 0.0
        text_color "#FF0000"
        text_hover_color "#000000"

    vbox:
        xanchor 0.0
        yanchor 0.5
        xpos 0.0
        ypos 0.5

        textbutton _("Prologue"):
            xanchor 0.0
            yanchor 0.5
            xpos 0.0
            ypos 0.5
            text_style "Stats"
            action Show("stats_prologue")

        textbutton _("Chapter One"):
            xanchor 0.0
            yanchor 0.5
            xpos 0.0
            ypos 0.5
            text_style "Stats"
            action Show("stats_chapter_one")

        text "Vigor: [Vigor]"
        text "Vision: [Vision]"
        text "Intel: [Intel]"
        text "Charm: [Charm]"
        text "Alignment - Hero: [Hero]"
        text "Alignment - Villain: [Villain]"

screen stats_prologue():

    modal True
    image "images/Clues/Cork.png"

    # Return Button
    textbutton _("Return") action Hide("stats_prologue"):
        xalign 1.0
        yalign 0.0
        text_color "#FF0000"
        text_hover_color "#000000"

    vbox:
        xanchor 0.0
        yanchor 0.5
        xpos 0.0
        ypos 0.5

        text "Searches: [prologueSearches]"
        text "Friends Found: [prologueFriendsFound]"

screen stats_chapter_one():

    modal True
    image "images/Clues/Cork.png"

    # Return Button
    textbutton _("Return") action Hide("stats_chapter_one"):
        xalign 1.0
        yalign 0.0
        text_color "#FF0000"
        text_hover_color "#000000"

    vbox:
        xanchor 0.0
        yanchor 0.5
        xpos 0.0
        ypos 0.5