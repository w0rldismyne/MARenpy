label chapter_one_sequence:

    #1111111111
    $ chapter1_day = 1

    call chapter1_day1_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_day1_event1
    call chapter1_day1_event1_classes

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_day1_event2

    $ chapter1_event = chapter1_free_time_evening

    call investigation

    call chapter1_day1_event_night

    #2222222222
    $ chapter1_day = 2

    call chapter1_day2_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_freetime
    call chapter1_day2_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day2_event2

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_freetime
    call chapter1_day2_event3

    call chapter1_day2_event_night

    #3333333333
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

    #4444444444
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
    call chapter1_day4_event3

    call chapter1_day4_event_night

    #5555555555
    $ chapter1_day = 5

    call chapter1_day5_event_morning

    $ chapter1_event = chapter1_free_time_morning_break

    call chapter1_freetime
    call chapter1_day5_event1

    $ chapter1_event = chapter1_free_time_after_school

    call chapter1_freetime
    call chapter1_day5_event2

    $ chapter1_event = chapter1_free_time_evening
    
    call chapter1_freetime
    call chapter1_day5_event3

    # Boss Battle

    call chapter1_day5_event_night

    # Chapter 2

label chapter1_freetime:
    menu:
        "Freetime"
        "Hang Out":
            call chapter1_freetime_hangout
        "Investigate":
            call investigation
    return

#11111
label chapter1_day1_event_morning:
    return

label chapter1_day1_event1:
    return

label chapter1_day1_event1_classes:
    return

label chapter1_day1_event1_classes_vigor:
    return

label chapter1_day1_event1_classes_charm:
    return

label chapter1_day1_event1_classes_intelligence:
    return

label chapter1_day1_event1_classes_vision:
    return

label chapter1_day1_event2:
    return

label chapter1_day1_event_night:
    return

#22222
label chapter1_day2_event_morning:
    return

label chapter1_day2_event1:
    return

label chapter1_day2_event2:
    return

label chapter1_day2_event3:
    return

label chapter1_day2_event_night:
    return

#33333
label chapter1_day3_event_morning:
    return

label chapter1_day3_event1:
    return

label chapter1_day3_event2:
    return

label chapter1_day3_event3:
    return

label chapter1_day3_event_night:
    return

#44444
label chapter1_day4_event_morning:
    return

label chapter1_day4_event1:
    return

label chapter1_day4_event2:
    return

label chapter1_day4_event3:
    return

label chapter1_day4_event_night:
    return

#55555
label chapter1_day5_event_morning:
    return

label chapter1_day5_event1:
    return

label chapter1_day5_event2:
    return

label chapter1_day5_event3:
    return

label chapter1_day5_event_night:
    return