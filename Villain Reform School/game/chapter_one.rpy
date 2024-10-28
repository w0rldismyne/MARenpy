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
    call chapter1_boss_scene

    call chapter1_day5_event_night

    # Chapter 2
    return

label chapter1_freetime:

    if chapter1_event is chapter1_free_time_morning_break:
        scene backgroundschool
    elif chapter1_event is chapter1_free_time_after_school:
        scene backgroundschoolnoon
    elif chapter1_event is chapter1_free_time_evening:
        scene backgroundcourtyardnight

    menu:
        "Freetime"
        "Hang Out":
            menu:
                "Uitto":
                    call UittoVisit
                "Jona":
                    call JonaVisit
                "Hiro":
                    call HiroVisit
                "Nanase":
                    call NanaseVisit
                "Mariko":
                    call MarikoVisit
                "Yoku":
                    call YokuVisit

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
            call KazzInv1

        "Mariko":
            call MarikoInv1

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


#(Investigation ending successful, bypass boss battle to tape scene then this goes after sleepover scene in chapter 1!)

#Bg forbidden door

"I gave up on sleep and walked around the school. I hoped to find a dry fantasy novel or something to quit feeling so restless."
"But the computer lab was glowing. I thought no one was supposed to be in there. So why does it feel like, no, I know someone’s in there."
"I tested the handle and it opened. There were rows of dead monitors. The room lacked the telltale hum of machinery. At the end of the room as light.*
    menu:
        "Fuck this":
            "I’ve seen too many horror movies to go blindly into strange places. I should just go to bed."
            # (end scene)
	    "Go in":
            #continue scene
"I used one of the old books to keep the door from closing behind me. 
"The last thing I need is to get locked in a place I’m not supposed to be in."
"The further down I went, the brighter and more high tech things got. The basement level was a wide hall with rooms in glass boxes."
"It's too reminiscent of my dad’s old lab. At the end of the hall, one cubical was lit up."
"Under the florescent lights, the person inside looked gaunt and pale.*

n "Mariko?”

m "....."

#(if punish = yes)

"She turned away from me and turned out her light. The teachers just said she was in detention not that she’d been detained. What the hell is going on here?"
 
#(continue to main branch)

#(else)

m "Nagen!? What are you doing here? No one’s supposed to be down here, especially S-T-U-D-E-N-T-Ss”

n "Then what are you doing here?”

"Something chirped in her room. She sat down on the floor, not wanting to look at me."

m "Apparently I’m sick, physically. Most people in my position wouldn’t be able to stand, but I don’t feel pain so… I’m on a week of strict bedrest.”

"That might have been what the beeping was, some kind of bed alarm.*

m "...Please don’t tell anyone I’m here.”

n "Why?”

m "It’s embarrassing! They have to watch me eat and…” 

"She sniffles"

"It’s not as easy as it sounds. And that’s what everyone will say."
"Just do it and you’ll get out faster, but it’s so hard. Being forced to sit around all day is hard too. I don’t want people to see me like this.”

n "Okay. I’ll pretend like I was never here. Can I at least tell people you’re okay?”

m "Yeah.”

n "Is it just you down here?”

m "Kinda… I don’t want to jinx it, but… We’re not exactly alone right now.”

"I don’t like the sound of that. I don’t get the feeling she feels threatened though."

#(Main branch)

q "Hello?”

m "Oh no, it’s awake.”

"A hologram of a stuffed rabbit projected itself on the glass. It reminded me of the old point and click games I used to play as a kid."

n "What the hell is that?”

q "Please don’t use bad language, it hurts people’s feelings.”

m "My feelings are not hurt by this twink cursing.”

"She rubbed her temples."

m "This is the school’s therapist. Or at least, it’s supposed to be, but it’s for kids, like kid kids. It won’t even let me say the ‘s’ word.”

n "What ‘s’ word?”

m "...stupid.”

q "Now Mariko, we’ve talked about this. There are better words you can use that describe your situation without being mean to yourself.”

m "Ugh! Nagen, don’t ever get in trouble, you’ll have this thing as a roommate.”

q "Nagen? I don’t recognize that name. Are you a student or a teacher?”
    menu:
        "Teacher":
            q "Ah! Please don’t tell the other faculty about this.”

            n "Why?”

            q "Well, I’m supposed to be on firewall duty, but my students need me!”

	    "Student":
            q "Righty-o. I promise to keep all your secrets!"
            q "Oh, but I’m not sure how you can fill out your profile without your friend hearing."
            q "Once everything’s back online we can fill it out together.”

            n "If you’re the school therapist, shouldn’t that be set up already?”

            q "I agree.”

#-mainbranch-

q "I just wasnt to do what I was designed to do. Even if everyone is older than I’m used to.”

n "And what exactly are you?”

ci "Chiriyo!”

n "...right… but are you a demon bunny?”

ci "I’m a babbit! Half bunny, half bat. The two most loveable animals combined.”

n "Since when?”

ci "Since my students voted. They picked out this design for me and by golly I won’t change it!”

"Designed by children for children, that explains a lot actually. Though I really question the focus group they used."

ci "While it is good to talk to friends, the average teen needs ten hours of sleep.”

"There’s no way anyone here is getting that."

ci "Will you be by to visit again?”

    menu:
        "Yes":
            # (+M, +R, +Ki, +Na)

            "Something scanned me head to toe."

            ci "Access granted! Playdates are a good way to foster healthy social skills.”

            "It’s so proud of itself, it’s kind of sad."

            ci "Next time you come by, the door will open.”
	    "No":

            ci "Your friend is in good paws. Please be safe on your way back.”

"I started to make my way up the stairs."

ci "See, I told you people would miss you!”

m "Shut up, he still might be able to hear you!”

"I think I’d go crazy if I was locked up with that thing. Maybe I should come back here again."

#(The final part of Mariko’s pathway is unlocked)

----

#(Investigation failure. 0 items found AND 0 visits with Mariko, goes before Day 5 event 4. Ability to guess who done it is locked?)

u "Nagen, what have you been doing all this time?”

n "What do you mean?”

u "I thought you were going to do something about the person who threatened Hiro?”

n "I was busy.”

u "Busy with what!?”

"Poking around would just make us look bad. It’s not like I don’t care, I just figured looking like a normal student would do a better job."
"I know I said I’d do something about it, but I wasn’t that serious."

N "Hiro asked us to drop it.”

u "That’s funny, because the only reason he’d want you to stay out of it, was because he had his own idea.” 

"She slaps her forehead."

u "I can’t find him anywhere. So help me, if he got hurt while you were dicking around, I’ll beat you with my legs.”

#----

#(Add to the Day 5, Event night, right after Uitto’s "knock knock” line)

u "Oh, and you forgot something on the practice field.”

"She kicks me in the shin. Turns out, the platform part of her heels are solid wood. I crumple in case she was thinking about aiming higher."
n "Why?”

"She narrows her eyes. I was already on thin ice with Uitto before."
"Best not to do anything to make her even more angry. As soon as the others arrive, she puts on an angelic smile. I should sleep with one eye open tonight."