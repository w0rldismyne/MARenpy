label chapter_one:

    ### 1 ###
    $ chapter1_day = 1

    call chapter1_day1_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_day1_event1 # Classes

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_day1_event2

    $ chapter1_event = chapter1_free_time_evening

    call chapter1_day1_event3

    call chapter1_day1_event_night

    ### 2 ###
    $ chapter1_day = 2

    call chapter1_day2_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    # Woke up late, no free time
    call chapter1_day2_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day2_event2

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_freetime
    call chapter1_day2_event3

    call chapter1_day2_event_night

    ### 3 ###
    $ chapter1_day = 3

    call chapter1_day3_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_freetime
    call chapter1_day3_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day3_event2

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_freetime
    call chapter1_day3_event3

    call chapter1_day3_event_night

    ### 4 ###
    $ chapter1_day = 4

    call chapter1_day4_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_freetime
    call chapter1_day4_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day4_event2

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_freetime

    call chapter1_day4_event_night

    ### 5 ###
    $ chapter1_day = 5

    call chapter1_day5_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_freetime
    call chapter1_day5_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day5_event2 # Special Event - Requires Vision

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_day5_event3
    
    # Dusk

    call chapter1_day5_event4 

    # Boss Battle

    call chapter1_day5_event_night

    # Chapter 2

label chapter1_freetime:
    menu:
        "Freetime"
        "Hang Out":
            menu:
                "Uitto":
                    pass
                "Jona":
                    pass
                "Hiro":
                    pass
                "Nanase":
                    pass
                "Mariko":
                    pass
                "Yoku":
                    pass

        "Investigate":
            call chapter1_investigation

    return

label chapter1_investigation:
    #INVESTIGATION SCENES 
    #[These scenes can be played during freetime by selecting the character from the investigation menu.]
    #Clues from Ch1... 
        #CDs, Computer, Microphone, Announcement List
    #Clues to find in Investigation... 
        #Mysterious Noise, Prank, Brag, PA Access, ID Account, Second locker, Missing Phone, Alexa Commands (might replace with more ID Account), Baton Pass
    scene backgroundroom
    menu:

        "Ask For Help":
            jump Ask_For_Help

        "Yoku":
            call YokuInv1

        "Rei":
            call ReiInv1

        "Momoko":
            call MomokoInv1

        "Rise":
            call RiseInv1

        "Nanase":
            call NanaseInv1

        "Next Page":
            jump chapter1_investigation2

    return

label chapter1_investigation2:

    menu:

        "Kietsu":
            call KietsuInv1

        "Taiga":
            call TaigaInv1

        "Dyre":
            call DyreInv1

        "Chisei":
            call ChiseiInv1

        "Shoma":
            call ShomaInv1

        "Ichita":
            call IchitaInv1

        "Next Page":
            jump chapter1_investigation3

    return

label chapter1_investigation3:

    menu:

        "Setsuna":
            call SetsunaInv1

        "Kitsune":
            call KitsuneInv1
            
        "Mu":
            call MuInv1

        "Kazz":
            pass

        "Mariko":
            pass

        "Next Page":
            jump chapter1_investigation

    return

label Ask_For_Help:

    menu:

        "Change Your Mind":
            jump chapter1_investigation

        "Uitto":
            call UittoInv1

        "Jona":
            call JonaInv1
            
        "Hiro":
            call HiroInv1

    return