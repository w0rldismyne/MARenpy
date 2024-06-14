init python:
    grades = ["D", "C", "B", "A"]

    def get_grades(convert):
        if convert >= 3:
            return "A"
        elif convert <= 0:
            return "D"
        else:
            return grades(convert)

    def get_rep():
        if Reputation > 0:
            return "Pass"
        else:
            return "Fail"

style Stats:
    color "#000000"
    hover_color "#1215CF"

screen stats():

    modal True
    image "images/Clues/Cork.png"

    image "images/Backgrounds/Progress Report.png"

    # Return Button
    textbutton _("Return") action Hide("stats"):
        xalign 1.0
        yalign 0.0
        text_color "#FF0000"
        text_hover_color "#000000"

    text "Reputation":
        xanchor 0.5
        yanchor 0.5
        xpos 1577
        ypos 367

    text "Subject":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 230

    text "MASTERY":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 230

    text "Intelligence":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 374

    text "[Intel]":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 374

    text "Charisma":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 519

    text "[Charm]":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 519

    text "Vigor":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 664

    text "[Vigor]":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 664

    text "Vision":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 809

    text "[Vision]":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 809

    text "Recovery":
        xanchor 0.5
        yanchor 0.5
        xpos 464
        ypos 954

    text "[Reputation]":
        xanchor 0.5
        yanchor 0.5
        xpos 997
        ypos 954

    image "images/Icons/Intelligence.png":
        xanchor 0.5
        yanchor 0.5
        xpos 128
        ypos 374
        xysize 144, 108

    image "images/Icons/Charm.png":
        xanchor 0.5
        yanchor 0.5
        xpos 128
        ypos 519
        xysize 144, 108

    image "images/Icons/Vigor.png":
        xanchor 0.5
        yanchor 0.5
        xpos 128
        ypos 664
        xysize 144, 108

    image "images/Icons/Vision.png":
        xanchor 0.5
        yanchor 0.5
        xpos 128
        ypos 809
        xysize 144, 108

    image "images/Icons/Shield with Outline V3 O1 (game icon).png":
        xanchor 0.5
        yanchor 0.5
        xpos 128
        ypos 954
        xysize 144, 108


screen stats_char_reputation():

    modal True
    image "images/Clues/Cork.png"

    # Return Button
    textbutton _("Return") action Hide("stats_char_reputation"):
        xalign 1.0
        yalign 0.0
        text_color "#FF0000"
        text_hover_color "#000000"

    vbox:
        xanchor 0.0
        yanchor 0.5
        xpos 0.0
        ypos 0.5

        text "Chisei Reputation: [chRep]"
        text "Dyre Reputation: [dRep]"
        text "Hiro Reputation: [hRep]"
        text "Ichita Reputation: [iRep]"
        text "Jona Reputation: [jRep]"
        text "Kitsune Reputation: [kRep]"
        text "Kazz Reputation: [kkRep]"
        text "Kietsu Reputation: [kiRep]"
        text "Mariko Reputation: [mRep]"
        text "Momoko Reputation: [mhRep]"
        text "Oshin Reputation: [muRep]"
        text "Nanase Reputation: [nkRep]"
        text "Rei Reputation: [rRep]"
        text "Rise Reputation: [reRep]"
        text "Setsuna Reputation: [sRep]"
        text "Shoma Reputation: [shRep]"
        text "Taiga Reputation: [tRep]"
        text "Yoku Reputation: [yRep]"
        text "Uitto Reputation: [uRep]"

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

        text "Day: [chapter1_day]"
        text "Event: [chapter1_event]"