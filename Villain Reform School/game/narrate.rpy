default panel_counter = -1

screen investigation_panel_narration(initial = False):

    $ temp_counter = panel_counter

    for panels, data in i_chapter_layouts[current_chapter][current_i_page].items():
    
        $ new_image = data.display.image

        image new_image:
            xpos 0.5
            xanchor 0.5
            if initial == True:
                at narrating
            elif temp_counter > 0:
                at narrated
            elif temp_counter == 0:
                at narrating
            else:
                at to_narrate
        $ temp_counter -= 1

# The culprit menu
screen temp():
    vbox:
        xpos 0.5
        ypos 0.5
        xanchor 0.1
        yanchor 0.5

        for character, data in i_profile_list.items():
            textbutton data["name"]:
                xanchor 0.5
                yanchor 0.5
                text_size 50
                text_color "#aa22ee"
                text_hover_color "#aa68cb"
                action Return(character)
                
# Purpose is to start every narration scene the same way
label investigation_narration_introduction:

    # For clean transition
    show screen investigation_panel_narration(True)
    hide screen investigation_panel_narration with dissolve
    # -----

    scene backgroundblack with dissolve

    $ current_i_page = 1
    $ panel_counter = -1

    return

label chapter1_investigation_narration:

    call investigation_narration_introduction

    show screen investigation_panel_narration() with dissolve

    "To recall the situation ..."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Kazz dropped his phone during move in, in front of the door."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Kitsune and Ichita found Kazz's phone."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Then Kitsune volunteered to find the owner. She thought Rei or Mariko would know who it belonged to."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "The culprit scheduled a message on Kazz's phone and hid it in Mu's locker."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "At the last minute, they hid Kazz's echo in the sound booth and left the microphone for the announcements on."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "The culprit ran so they'd have an alibi when the message went off."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "So who did it?"

    # Recreate dialogue window?
    $ answer = renpy.call_screen("temp")

    hide screen investigation_panel_narration

    $ current_i_page = 1
    if answer == "mariko":
        call chapter1_interrogation
    else:
        call chapter1_investigation_fail

    return

label chapter2_investigation_narration:

    call investigation_narration_introduction

    show screen investigation_panel_narration() with dissolve

    "To recall the situation ..."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Whoever did this has hated Jona from the beginning. They even defaced his sketchbook and used a method to make it look like anyone at the school could want him gone."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "As the class representative, Ichita was the last student in the Vision classroom, and locked the classroom up for the night."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    if i_chapter_layouts[current_chapter][current_i_page]["panel3"].display == ch2_p1panel3i:
        
        "The note was left in the classroom overnight?"
        "No, that isn't right. Principal Vivaldi would have spotted it during lock up."
        "It had to have been placed after the teachers went to bed, but before first period."

        hide screen investigation_panel_narration with fade
        jump investigation_board

    elif i_chapter_layouts[current_chapter][current_i_page]["panel3"].display == ch2_p1panel3r:
        
        "They also had painted their nails pink, and fairly recently before making the note."


    $ panel_counter += 1
    $ renpy.restart_interaction()

    "They cut the letters needed out of magazines, and felt comfortable doing so, since other students had a copy of the issue they owned."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "While making the note, one of their hairs dropped into the glue."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    if i_chapter_layouts[current_chapter][current_i_page]["panel6"].display == ch2_p1panel6i:
        "Then they placed a hair from a different student to frame them… but why?"
        "Couldn't they just removed the hair they dropped and keep it perfectly anonymous?"
        "Or removed their hair and only left behind the false lead?"

        hide screen investigation_panel_narration with fade
        jump investigation_board

    elif i_chapter_layouts[current_chapter][current_i_page]["panel6"].display == ch2_p1panel6r:
        "They tried to get the hair out, and that's when their nail polish rubbed off in the glue."


    $ current_i_page = 2
    $ panel_counter = 0
    $ renpy.restart_interaction()


    if i_chapter_layouts[current_chapter][current_i_page]["panel1"].display == ch2_p2panel1i:
        "The culprit panicked and added pink to the page to further disguise who made it, then tried to cover up the evidence by moving the magazine pieces as best they could before the glue dried ... "
        "But then why was Uitto so certain it was nail polish? We don't have pink paint here and a marker wouldn't look pearly pink."

        hide screen investigation_panel_narration with fade
        jump investigation_board

    elif i_chapter_layouts[current_chapter][current_i_page]["panel1"].display == ch2_p2panel1r:
        "The culprit panicked, unable to hide the nail polish."
        "They tried to hide it with the letter placement, and even put another student's hair on it to try and confuse use."
        "I bet they didn't have time to make another given it was also misspelled."


    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Our first student council meeting was an hour and a half before classes started. We had all the classroom keys, so they must have been put away properly the night before."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "We met with the class representatives. I didn't realize it at the time, but the culprit was planting the seeds for Jona's capture then, and pressured everyone to go along with their idea."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Hiro, Rise and Ichita left the office as soon as we agreed to hold the dance."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "The classroom keys go to all the classrooms. The culprit took the chance to place the note on Jona's desk for homeroom before a teacher could spot it."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "Since Jona didn't make a big deal out of finding it, I bet the culprit was super frustrated that there weren't a bunch of rumors going around like when Mariko attacked."

    $ panel_counter += 1
    $ renpy.restart_interaction()

    "So who did it?"

    # Recreate dialogue window?
    $ answer = renpy.call_screen("temp")

    hide screen investigation_panel_narration

    $ current_i_page = 1
    if answer == "rise":
        call chapter2_interrogation
    else:
        call chapter2_investigation_fail

    return

transform narrated:
    alpha 0.5

transform narrating:
    alpha 1.0

transform to_narrate:
    alpha 0.075