label chapter1_introduction:

    scene backgroundschool
    with dissolve
    pause 0.5

    play music "music/CryingOverYou.mp3"

    show nanase smile
    with dissolve

    nk "Good morning!" id chapter1_introduction_4dd02cf0

    n "AH!"

    show nanase surprised

    nk "I'm sorry, I didn't mean to startle you." id chapter1_introduction_e696e9a7

    show nanase smile talk

    nk "My name's Nanase Keisan. I'm helping with orientation during move in week." id chapter1_introduction_c45b6a63
    nk "Will you be staying on campus this year?" id chapter1_introduction_d8c6435b

    n "....."

    "Good god man, have you forgotten how to talk to people like a normal human being?"
    "Don't just stand there, say something!"

    hide nanase

    menu:
        "Say something witty":

            $ Charm += 1

            show nanase smile talk

            n "Well, all my stuff is here already, so I might as well."

            "I motion to my garishly decorated luggage; my guardians said I needed more than my usual duffle bag of necessities."
            "Pretty sure I have more bags than clothes. They would have been a nice way to carry my rifles... had they let me keep them."

            show nanase sad1

            nk "R-right, of course." id chapter1_introduction_fad5f5ce

            "She sighs."

            show nanase sad smile

            nk "You'll want to head to Classroom E-103." id chapter1_introduction_d5c94819
            nk "Let me know if you need any help." id chapter1_introduction_bc753ec6

            n "Thanks, I got it."

        "Just answer the question":

            $ Vigor += 1

            show nanase smile

            n "Yeees..."

            "Did that sound weird? I feel like it sounded super weird."
            "I'm drawing a blank. Why did I only get four hours of sleep last night? This is a nightmare."

            nk "Alright, then you'll want to head over to Classroom E-103." id chapter1_introduction_6e349e3b

            n "She points to a towering building a few yards west."

            "103, that'll probably be on the ground floor. I grab my many bags, fumbling a little."

            nk "Do you need any help?" id chapter1_introduction_e146476a

            "Have I taken too long? I really can handle it, it'll just be a little awkward balancing five bags."
            "Though now that I think of it, I most certainly don't own enough junk to warrant this much luggage."
            
        "Introduce yourself":
            $ Intel += 1

            show nanase smile

            n "My name's Nagen Tesuta. Orientation is in E-103, right?"

            "I memorized today's schedule well in advance."
            "If I get there early, I'll have five hours to try and finish Dracula."

            nk "Yep. Do you need any help?" id chapter1_introduction_7b983e4d

            hide nanase

            menu:
                "Yes":
                    $ nkRep += 1
                    show nanase smile

                    n "Actually, yeah, I could use an extra pair of hands."

                    show nanase smile talk

                    nk "Great, I'll walk with you! What do you need me to carry?" id chapter1_introduction_e52921af

                    "She insists on taking three of the five bags, which is more than I actually need."
                    "But she seems happy to have someone to talk to."
                    "I notice other students helping with orientation are in red volunteer shirts, but she doesn't have one."
                    "Is she actually helping with orientation?"

                    n "You seem pretty new here yourself. How'd you get to be a volunteer?"

                    nk "Hunh? Oh, no, I'm not with them." id chapter1_introduction_2427fcf9
                    nk "I got here yesterday night, but I figured helping out was better than just standing around waiting for the meeting." id chapter1_introduction_3fdfc4aa
                    nk "Not much to do around here other than unpacking and wandering around the school." id chapter1_introduction_2c7e288c

                    n "To each their own, I guess."

                    hide nanase

                "No":
                    show nanase sad2

                    n "I'm fine, really. Thanks anyways."

                    nk "O-okay then." id chapter1_introduction_1b687e81

                    "She doesn't seem convinced, but I'm in a bit of a hurry."
    
    hide nanase

    scene backgroundroom

    play audio "405454__ranne_madsen__bag-drop (x1).ogg"

    "I get to the room and set down my things."
    "I'm not sure what I can expect from this school, but I do know one thing."
    "By the end of the year, the student body will be in the palm of my hand."
    "I mean, why else does someone become student body president, resume material? I think not."
    "I may not be able to clear my name through the DVP, but if I make enough of an impression, they can't just lock me away and pretend nothing happened."
    "After I've gotten settled, I'll take a look around the school."

    g "You will be given the opportunity to explore the school and look for your friends."
    g "This is a good chance to meet your future classmates as well."

    # New Game +

    g "Of course, you can always skip ahead to the next scene."
    g "But this will give you a baseline affinity of 0 with all students."

    # Else

label introduction_meet_students:

    scene backgroundschool

    play music "music/CosimoFogg.mp3"

    if introductionFriendsFound is 3:
        "Well, I found all my friends, should I go start the meeting?"

        menu:
            extend ""
            "Keep Looking Around" if introductionSearches is not 18:
                pass
            "Start the Meeting":
                jump Meeting

    if introductionSearches is 0:
        "Okay, where should I start looking?"
    else:
        "Where should I look now?"

    $ choice_many_choices = True

    menu:
        extend ""
        "Lecture Hall" (sensitive = (introductionHiroMet is False)):

            $ choice_many_choices = False

            jump introduction_lecture_hall

        "Field" (sensitive = (introductionMarikoMet is False)):

            $ choice_many_choices = False

            jump introduction_field

        "Hallway" (sensitive = (introductionYokuMet is False)):

            $ choice_many_choices = False

            jump introduction_hallway

        "Courtyard" (sensitive = (introductionUittoMet is False)):

            $ choice_many_choices = False

            jump introduction_courtyard

        "Stage" (sensitive = (introductionKitsuneMet is False)):

            $ choice_many_choices = False

            jump introduction_stage

        "Audio Visual Room" (sensitive = (introductionKazzMet is False)):

            $ choice_many_choices = False

            jump introduction_av

        "Nurse's Office" (sensitive = (introductionOshinMet is False)):

            $ choice_many_choices = False

            jump introduction_nurse_office

        "Pond" (sensitive = (introductionIchitaMet is False)):

            $ choice_many_choices = False

            jump introduction_pond

        "Roof" (sensitive = (introductionTaigaMet is False)):

            $ choice_many_choices = False

            jump introduction_roof

        "Library" (sensitive = (introductionChiseiMet is False)):

            $ choice_many_choices = False

            jump introduction_library

        "Sewing Room" (sensitive = (introductionShomaMet is False)):

            $ choice_many_choices = False

            jump introduction_sewing_room

        "Gymnasium" (sensitive = (introductionSetsunaMet is False)):

            $ choice_many_choices = False

            jump introduction_gym

        "Cafe" (sensitive = (introductionKietsuMet is False)):

            $ choice_many_choices = False

            jump introduction_cafe

        "Lab" (sensitive = (introductionMomokoMet is False)):

            $ choice_many_choices = False

            jump introduction_lab

        "Classroom" (sensitive = (introductionReiMet is False)):

            $ choice_many_choices = False

            jump introduction_classroom

        "Student Council Room" (sensitive = (introductionRiseMet is False)):

            $ choice_many_choices = False

            jump introduction_student_council_room

        "Forbidden Door" (sensitive = (introductionDyreMet is False)):

            $ choice_many_choices = False

            jump introduction_forbidden_door

        "Ampitheater" (sensitive = (introductionJonaMet is False)):

            $ choice_many_choices = False

            jump introduction_ampitheater

label introduction_lecture_hall:
    
    $ introductionSearches += 1
    
    scene backgroundcharm
        
    $ introductionFriendsFound += 1
    $ introductionHiroMet = True
        
    call introduction_hiro

    jump introduction_meet_students

label introduction_field:

    $ introductionSearches += 1

    scene backgroundfield
        
    $ introductionMarikoMet = True

    call introduction_mariko
    
    jump introduction_meet_students

label introduction_hallway:

    $ introductionSearches += 1

    scene backgroundhall1

    $ introductionYokuMet = True

    call introduction_yoku
    
    jump introduction_meet_students

label introduction_courtyard:

    $ introductionSearches += 1

    scene backgroundcourtyard

    $ introductionFriendsFound += 1
    $ introductionUittoMet = True

    call introduction_uitto
    
    jump introduction_meet_students

label introduction_stage:

    $ introductionSearches += 1

    scene backgroundstage

    $ introductionKitsuneMet = True

    call introduction_kitsune
    
    jump introduction_meet_students

label introduction_av:

    $ introductionSearches += 1

    scene backgroundavroom

    $ introductionKazzMet = True

    call introduction_kazz
    
    jump introduction_meet_students

label introduction_nurse_office:

    $ introductionSearches += 1

    scene backgroundnurse
        
    $ introductionOshinMet = True

    call introduction_oshin
    
    jump introduction_meet_students

label introduction_pond:
    
    $ introductionSearches += 1

    scene backgroundpond

    $ introductionIchitaMet = True

    call introduction_ichita

    jump introduction_meet_students

label introduction_roof:
    
    $ introductionSearches += 1

    scene backgroundroof

    $ introductionTaigaMet = True

    call introduction_taiga

    jump introduction_meet_students

label introduction_library:
    
    $ introductionSearches += 1

    scene backgroundlibrary

    $ introductionChiseiMet = True

    call introduction_chisei

    jump introduction_meet_students

label introduction_sewing_room:
    
    $ introductionSearches += 1

    scene backgroundsew

    $ introductionShomaMet = True

    call introduction_shoma

    jump introduction_meet_students

label introduction_gym:
    
    $ introductionSearches += 1

    # BG:Gym

    $ introductionSetsunaMet = True

    call introduction_setsuna

    jump introduction_meet_students

label introduction_cafe:
    
    $ introductionSearches += 1

    scene backgroundcafe

    $ introductionKietsuMet = True

    call introduction_kietsu

    jump introduction_meet_students

label introduction_lab:
    
    $ introductionSearches += 1

    scene backgroundlab

    $ introductionMomokoMet = True

    call introduction_momoko

    jump introduction_meet_students

label introduction_classroom:
    
    $ introductionSearches += 1

    scene backgroundclass

    $ introductionReiMet = True

    call introduction_rei

    jump introduction_meet_students

label introduction_student_council_room:
    
    $ introductionSearches += 1

    scene backgroundstuco

    $ introductionRiseMet = True
        
    call introduction_rise

    jump introduction_meet_students

label introduction_forbidden_door:
    
    $ introductionSearches += 1

    scene backgrounddoor

    $ introductionDyreMet = True

    call introduction_dyre

    jump introduction_meet_students

label introduction_ampitheater:
    
    $ introductionSearches += 1

    scene backgroundamp

    $ introductionFriendsFound += 1
    $ introductionJonaMet = True
        
    call introduction_jona

    jump introduction_meet_students

label introduction_hiro:

    play music "music/WeAre.mp3"
        
    "I arrive at the room where the student council meets."
    "Everything looks too new, too clean, like no one has set foot in here since the school opened."
    "I stand for a while, admiring the leather office chair at the end of the table possibly meant for the student council president."
    "I would give anything to be in charge and shape the future of this school."
    "It may take a while, but I'm sure I can get there."

    show hiro

    h "Nagen? Nagen, is that you?" id introduction_hiro_8e9df4a7

    "I turn and see one of the last people I expected to see. My former teammate and rival, Hiro Morine."
    "I mean, I say rival, but it was purely for Odori's attention."
    "He cheated off all my tests while leaving me in the dust when it came to sports or fighting."
    "Any way you slice it, it was never a fair competition. One of us would always have an advantage over the other."
    "But I'd be lying if I said I wasn't bitter that everyone liked hanging out with him at recess."
    "I'm getting off track."

    n "It's good to see you, I uh, haven't seen you since before..."

    "I trail off. There's no way of knowing how much he knows about the deal that was cut with the DVP."
    "If I say the wrong thing, I could jeopardize his chance at getting pardoned."

    show hiro happy

    h "Yeah, I'm surprised they're letting us go to school together." id introduction_hiro_bcab52b9
    h "My lawyer said they were going to separate us and we weren't allowed to see each other again. I wonder what changed?" id introduction_hiro_bce3cdc5

    hide hiro

    menu:

        "Pretend to speculate":

            $ Intel += 1

            show hiro happy

            n "I don't know, maybe Uitto worked her magic and cried us into a lighter sentence."

            show hiro talk2

            h "We could do that? Shoot, if I'da known that, I woulda taken a lemon into the courtroom or something." id introduction_hiro_f877f647

            show hiro smug

            h "I mean, yeah I was kinda scared, but I totally coulda cried my way to freedom." id introduction_hiro_0b8c8e68

            "He's as determined as ever."

            n "I was thinking more along the lines of using her Proficiency. It was Diplomacy, remember?"

            show hiro empty

            "He stares at me blankly."

            n "She could talk people into doing things for her."

            show hiro sassy

            h "Right, she was a Charisma major at the time." id introduction_hiro_e1ef44de

            show hiro

            h "Oh! That reminds me." id introduction_hiro_86bd6e50

            show hiro talk1

            h "There's been a rumor going around that you can change your major, have you heard anything about that?" id introduction_hiro_84866946

            n "No, I haven't."

            show hiro hmm

            h "Oh, that sucks. I was hoping you could explain it to me." id introduction_hiro_a8f8aba4
            h "Something to do with how Proficiencies can apply to different majors depending on how they're used." id introduction_hiro_39d55a3b

            show hiro suppress

            h "But I just don't get injured easily. I don't see how that would make me smarter or more likable." id introduction_hiro_1b8d1ab4

            "That is odd, I'll have to look into that."
            
            hide hiro

        "Ask how he's doing":

            $ Charm += 1
            $ hRep += 1

            show hiro happy

            n "Crazy, right? But it's good to see you. How have you been?"

            show hiro sad talk

            h "I'm living in a group home right now. It's not too bad, a little cramped, but they were willing to take me." id introduction_hiro_04368f98

            n "That's kinda surprising."

            show hiro sad smile

            h "Well, I mean, it's like a rehab center for troubled kids." id introduction_hiro_b5721bdc
            h "We have to go to classes, and therapy sessions, and they've got this little reward system and junk." id introduction_hiro_0a6107f8

            show hiro sad talk

            h "I had to work really hard just to be able to leave the building on my own." id introduction_hiro_fcff3029

            n "Oh, well, I mean that's good to hear. Is it nice?"

            show hiro sassy

            h "I only have the bottom half of a bedroom door, and one of the other kids punched a hole in the wall last week." id introduction_hiro_4d3f3c9d

            show hiro sad smile

            h "But the grown-ups are nice, they give me plenty of space... But it's like a respect thing, not 'cause they're scared." id introduction_hiro_87f6a0b0

            "Well that's good. He has a bad habit of lashing out if people get too close too suddenly."
            "That thing about the kid punching the wall kinda concerns me though."

            n "I'm glad that's working out for you."
            n "My foster family's a little... strange. They live in this huge house, but they don't really take care of it."
            n "It's like living in a museum. Lots of dusty old expensive things I'm not allowed to touch."

            hide hiro

        "Lawyers are dumb":

            show hiro happy

            n "Why would they tell you that?"
            n "It wasn't a standard case, it's not like he could flip through a handbook and find the standard punishment on taking over a city."
            
            show hiro suppress

            h "Well, no, I guess not." id introduction_hiro_3de84c1a

            n "He was probably trying to scare you or something. That's so unethical..."
            n "I think."
            n "I'm not sure to be honest. See, this is why I chose to represent myself."

            show hiro talk2

            h "You shoulda been my lawyer instead, I'm sure you were awesome." id introduction_hiro_a233735d

            n "I hope so."

            h "What do you mean? You're here, aren't you? That means you won, right?" id introduction_hiro_ece73b55
            
            n "Something like that; I'm on probation. Do you think the others are here?"
            
            h "I mean, it's possible. They had Proficiencies too... Maybe we could start our club back up!?" id introduction_hiro_7985c8c0

            hide hiro

            menu:
                "Yes":

                    $ Villain += 1

                    show hiro smirk

                    n "Shh, keep your voice down. We can't have the DVP finding out about this."

                    h "I gotcha. Well, let me know if anything changes. I got your back, man." id introduction_hiro_c111f067
                    
                    n "Oh, and Hiro?"

                    h "Hmm?" id introduction_hiro_426b4ba2

                    n "This time we're doing things my way."

                "Maybe":

                    $ Hero += 1

                    n "As tempting as that sounds, it'd be best if we lay low for a while. At least wait and see how things pan out for us here."

                    show hiro empty

                    h "What's bread got to do with this?" id introduction_hiro_b5f3cfa9

                    show hiro smirk

                    "I must look like I'm about to clock him or something because he starts laughing like a mad man."

                    show hiro smug

                    h "Dude, I'm just kidding, cool your jets." id introduction_hiro_753f3f8e

                    n "You know how I feel about puns."

                    h "Yeah, yeah; look I can't make any promises, but I'll try." id introduction_hiro_e649c6f4

                    n "To knock it off with the puns, or to keep out of trouble?"

                    h "Both." id introduction_hiro_3885d42f

                "No":

                    show hiro sad fine

                    n "I don't know. I mean, we can't use the same group name, and it wouldn't feel right without Odori anyway."

                    h "Yeah, that's true." id introduction_hiro_816d242a

                    "Odori was the one who brought us all together in the first place."
                    "The Junior Gladiators was her dream, and a part of it died with her."

                    show hiro

                    h "Hey man, are you okay?" id introduction_hiro_ce0183ad

    show hiro sad fine

    n "We'll be meeting later."

    show hiro talk2

    h "We?" id introduction_hiro_b3a70c77

    show hiro happy

    h "Wait, no way, are the other's here too?" id introduction_hiro_4c2a933e

    # Has Nagen found someone?
    if introductionFriendsFound is 2:
        n "I don't know for sure, but I'm looking for them. Until then, play it cool."
    else:

        # Change this thanks

        n "Yup."

    hide hiro
    
    "I've spent way too long listening to what other people tell me to do."
    "Once I've finished scoping out the school, I'm breaking out the strategy board."
    "I should get going. There's still more of the school to see."

    return

label introduction_mariko:
            
    "A few years ago, I probably wouldn't be anywhere near here. Maybe this year will be different."
    "In the corner of my eye, I see a girl in black spandex bound over, a pile of papers in her hands."

    show mariko sheepish

    m "Hold on a second!" id introduction_mariko_49c1700b
    m "Hey, the name's Mariko Genki, I'm gathering signatures to start up a Cheer Squad!" id introduction_mariko_4aaa006e
    m "Some may say it's a little early, but it's never too early to start practic-" id introduction_mariko_c77438b5

    show mariko mad talk

    "Her chipper demeanor falters once she looks up. It's as if the life has been sucked right out of her."
    "She shifts, using her papers as a physical barrier between us."
    "Floundering for a proper social response, she goes with the first thing I imagine comes to mind."
    
    show mariko cry

    m "You wouldn't happen to be interested in being a cheerleader, would you?" id introduction_mariko_adffd92d

    "Her tone is tight, her smile forced. I'd judge, but I have always been awkward around people myself."
    "Being an ex-villain just makes things that more difficult, I guess."

    hide mariko

    menu:

        "Try to calm her down":
            
            $ mRep += 1

            show mariko judge

            n "I'm not against the idea, but do you actually want me on your team?"

            "Her defensiveness eases, but it's clear she's still wary."
            "Not that I blame her, she was once a member of my army. One of the more resistant."
            "I don't know if it was her Proficiency or pure determination, but she had fought the brainwashing harder than anyone else."
            "With an ability like being unable to feel pain, it can be tricky figuring out if she should be a Vigor or Intelligence major."
            "Well I say my army, but Hiro was the one that gathered and directed everyone."
            "I kinda just watched from rooftops and corrected his orders through radio and the like."
            "If it had actually been my army, things might have gone smoother."

            m "I mean, anyone's allowed to join. I just never took you for the 'cheery' type. You've always been so..." id introduction_mariko_f86002a1

            hide mariko

            menu:

                "Dreary":

                    $ Charm += 1

                    show mariko sad talk
                    
                    "She smiles that polite, forced smile one receives out of pity."
                    "To be fair, I wasn't exactly the most outgoing kid in the world and I didn't have the best lasting impression on her."

                    m "Hey, uh, rhyming is a key ingredient to cheer." id introduction_mariko_a015acfc

                    "That was the roughest shift in a conversation I've heard since my dad."
                    "A lot of examples come to mind, but I have to focus on the task at hand."

                    n "Good luck with the cheer thing. I'm... really sorry about what happened."

                    show mariko

                    "Her face hardens."

                    m "Sorry isn't going to fix anything." id introduction_mariko_684f022c

                    "She takes a deep breath."

                    show mariko upset talk

                    m "But it helps... I just- I'm not going to let my girls down this time. And guys. Really, uh, really should recruit more-" id introduction_mariko_e33952db

                    "Her eyes drift to me, then shaking her head."

                    m "I've got to go." id introduction_mariko_e1a0c30c

                    "She hurries off. Not that I blame her."

                    hide mariko

                "Hostile":

                    $ Vigor += 1

                    show mariko upset talk

                    m "I should have seen it coming." id introduction_mariko_44b3a804

                    "She shakes her head, regret evident on her face."
                    "When Hiro had gone around recruiting our first members, Mariko declined."
                    "She was the only cheerleader who declined, and her position as the captain didn't matter to anyone when Guwon was already in chaos."

                    n "I was just trying to protect everyone."

                    show mariko glare

                    m "No, I was trying to protect everyone; you wanted to fight back!" id introduction_mariko_6c441555

                    n "Fighting is what kept us alive. It's what kept you alive."
                    n "You fought longer and harder than any of us, it was quite impressive."
                    n "You'd have made an excellent general."

                    show mariko talk

                    m "A general hunh?" id introduction_mariko_c3a95297

                    "She laughs bitterly."

                    m "They don't give medals of honor to villains, Tesuta." id introduction_mariko_72f1a68f

                    n "You're only the villain once you lose."

                    "She may be done fighting, but I'm not. I'll keep pushing forward until there's nothing of me left."

                    n "It was good to see you again. You know, to know that you're okay."

                    hide mariko

                    "I turn around and leave."
                    "Though I'm surprised she's here considering what I was sent here to do. I'm sure she had hoped to never see me again."
                    "Does that mean there are other kids from the Junior Gladiators at this school?"

                "Uninterested":

                    $ Intel += 1

                    show mariko talk

                    n "I never really had a lot of free time back then."

                    "Between Odori's hero club and my dad's endless examinations, I didn't have a lot of time for anything."
                    "I was constantly underslept to the point that anything involving standing seemed taxing."

                    m "Right, I don't suppose your mind has changed all of a sudden either?" id introduction_mariko_e5e0aa02

                    n "Not especially, no."

                    "She breathes a huge sigh of relief. Still a little anxious, but no longer petrified."

                    show mariko smile talk

                    m "Then I'll be on my way. Byeee!" id introduction_mariko_e2e3d1b7

                    hide mariko

                    "She immediately turns around and leaves. I doubt she'll be coming my way anytime soon."

        "Say anything to make her go away":

            show mariko talk

            n "Not interested."

            "She clearly recognizes me from the Guwon Riots."
            "Mariko had been a member of my army, and not of her own volition. She was one of the last who fell under our control."
            "I doubt she'd want anything to do with me, and I'm not going to pretend I like the idea of seeing her anyway."
            "What were they thinking, sending both of us to the same school?" 
            "The whole point of witness protection is to maintain a normal life, and she is an obvious threat."

            m "Good, then you'll have no business being around my girls." id introduction_mariko_8bccc42d

            n "Excuse me? I was minding my own business, you were the one who came running up to me."
            n "I'm not out here to get anyone, I'm trying to live a normal school life."

            "She sputters in outrage. There are a million things I'm sure she wants to say to me, but it wouldn't change anything."
            "I don't have time for her to collect her thoughts."
            "As I begin to walk away, she shouts after me."

            show mariko mad talk

            m "I don't want any trouble from you, Tesuta." id introduction_mariko_02daeef2
            m "Anyone wearing this emblem is under my protection, you understand?" id introduction_mariko_a2209773

            "She gestures to her earrings like I'm going to look at every girls' ears before talking to them."
            
            m "If you try anything-" id introduction_mariko_9a368bb1

            n "The only thing I'm trying to do is start over."
            n "I don't have the time nor desire to mess around with a handful of powder puffs." 
            n "I've got my own problems to deal with."

            show mariko judge

            m "Just don't drag my squad into it." id introduction_mariko_4d761ec6

            hide mariko

            "It's almost admirable how fervently she defends this so-called 'squad' when she hasn't even gotten permission to lead one in the first place."
            "Old habits die hard, I suppose."
            "Though she wasn't a terribly good leader. All bark and no bite."

    "I should look around some more."

    return

label introduction_yoku:

    "The grounds of this school are a lot larger than I anticipated."
    "I'll need at least an hour before classes start in order to figure out where I'm going."
    "I wander into a back hallway on the second floor."
    "I assume all of the art classes will be taking place here based on the glass display cases."
    "With all the classrooms locked, there isn't much to see right now."
    "Though I don't seem to be the only person wandering around."
    "He has a beaten-up piece of paper in his hand and seems lost."
    "When he looks up at me, I feel a chill run down my spine."

    show yoku eyeroll

    y "Oh, it's you..." id introduction_yoku_f0b979a0

    n "What's that supposed to mean?"

    "A few things come to mind, most tracing back to the last two years."
    "In the course of a year, Odori and I had raised an army of three hundred with the education collars."
    "They essentially hijacked a person's body through their central nervous system."
    "With it, we could train our troops in a matter of hours."
    "However, not everyone was as keen on this idea. Most of the soldiers had been students at our school."
    "Granted, I never came in contact with a lot of recruits, so the question is, how does this kid know me?"
    "I recognize him from the posters at Estella back when we were kids, a real wiz-kid with a piano."
    "We never crossed paths since I spent most of my time studying in my room."
    "My room, of course, being an anti-social hotspot."

    show yoku furious1

    y "What are you doing here?" id introduction_yoku_c7c18567

    hide yoku

    menu:

        "None of your business":

            $ yRep += 1

            n "Just looking for where my new classes are going to be. And talking to you, I guess."

            show yoku furious2

            y "...You can't be serious." id introduction_yoku_10ada24b

            n "What?"

            show yoku eyeroll

            y "I thought this was supposed to be a school for the e-e-elite, not a co-common murderer." id introduction_yoku_77911f30

            n "First of all; common!? I know having a good memory isn't the most exciting Proficiency, but it's better than you Mr. Music Man."
            n "Secondly, being involved in the Guwon Riots has nothing to do with how capable I am as a student."
            n "The definition of 'elite' here is slightly above average, don't delude yourself."

            show yoku furious2

            y "So defensive over your Pr-proficiency, yet you're going to g-gloss over the murderer comment?" id introduction_yoku_27772163

            n "....."

            "Okay, so I'm a little self-conscious about my so-called 'powers'."
            "But it isn't like I think being able to remember everything is pointless or lame, it's served me fairly well."
            "The thing is, my Proficiency is artificial."
            "Unlike child prodigies like Yoku, my father had to spend every waking moment forcing my brain to process memories the way it does."

            show yoku furious1

            y "Hh-ow long are you going to keep staring into space?" id introduction_yoku_2b1d3b10

            n "Sorry, that happens sometimes."

            y "As much as I'd like to continue this ffffascinating discussion, I have business eh-elsewhere." id introduction_yoku_7217dbbc
            y "Until next time." id introduction_yoku_0ac7120e

            hide yoku

        "I'm lost":

            $ yRep += 1

            show yoku furious1

            y "...Obviously." id introduction_yoku_a985fb29

            n "Hey! You're wandering around here too! You're probably more lost than I am."

            "He freezes."

            show yoku blush2

            y "You... you don't know that." id introduction_yoku_e2de7867

            n "Really, then where are we?"

            "His face pinches up, as if his lower lip is trying to retreat up his nose."

            show yoku

            y "First-" id introduction_yoku_9e7df65a

            "I shake my head as he speaks."

            show yoku think

            y "Lower-" id introduction_yoku_9428d6f9

            n "Getting colder. We're on the second floor."

            show yoku furious1

            y "If you kn-know that, how a-re you lost?" id introduction_yoku_4595beeb

            n "I'm trying to find the dorms. These are not dorms."

            "I'll be fine once I map out the entire school, but my cheapo emergency phone is almost dead and Maimai will flip if she calls and I don't answer."

            n "Also I have to ask..."

            hide yoku

            menu:
                "How do you know me?":

                    $ Charm += 1

                    show yoku

                    y "You really don't know?" id introduction_yoku_266410e2
                    y "W-well, whe-ere do I start..." id introduction_yoku_f297acd2

                    "That's never a good phrase to hear."

                    show yoku talk

                    y "Professor Tesuta co-constantly talked about you at galla sssocials, and everyone was dying to kn-know what you'd been up to desp..des..de-" id introduction_yoku_77159ddb

                    "He sighs."
                    
                    show yoku furious2

                    y "Despite never being invited." id introduction_yoku_e2720db4
                    y "You got in detention mu-m-multiple times for fighting, and you t-took o-over the city." id introduction_yoku_0b5832f2

                    n "Well, yeah, but... how did you know that was me?"

                    show yoku furious1

                    y "You didn't even do something as simple as wear a mask. What p-possibly made you think no one would recognize you?" id introduction_yoku_5e539633

                    n "I was really good at hiding."

                    show yoku furious2

                    y "Y-you were good at camping, that isn't the same thing." id introduction_yoku_de7155b1
                    y "Honestly, I can't believe you were capable of a-anything on that large a scale." id introduction_yoku_1152c2f8
                    y "I assume you had additional help." id introduction_yoku_4bb80614

                    hide yoku

                    "He quickly turns arounds to leave."

                    n "HEY!"

                    "Granted, I shouldn't be proud of the things I did, but it's okay to feel a little insulted by this, right?"
                    "I'm just mad he's calling me stupid."

                "What are you doing here?":

                    $ Intel += 1

                    show yoku talk

                    y "I was looking for the auditorium, I he-heard that this school was going to provide a Wurlitzer." id introduction_yoku_c641df87
                    y "As the future's leading co-com-composer, I'd like to find it." id introduction_yoku_08860b48

                    n "A Wurlitzer?"

                    show yoku bummed

                    y "Like a giant music box, an orchestra without... people." id introduction_yoku_a08a65c3

                    "I've never seen someone so disgusted at the mention of other human beings. And I thought I was antisocial, dang."

                    n "What do you need a Wurlitzer for?"

                    show yoku talk
                    
                    y "I've composed for a number of high scale events, but it's been a while since I've had a steady stream of clientele." id introduction_yoku_a2ab46d9
                    y "Making everything on my own will expedite the process." id introduction_yoku_d18900a6

                    hide yoku

                "Is your hair naturally green?":

                    $ Vision += 1

                    show yoku furious2

                    y "....."

                    n "I've seen a couple of people at this school with crazy hair colors. I just had to ask."
                    n "Mine isn't. In case you were curious."

                    y "....."

                    n "So is it? I feel like it'd be a pain to dye it and do the little buzz thing."
                    n "Not that it looks bad, it just sends a certain message y'know."

                    y "I'm going." id introduction_yoku_491c1e91

                    n "Was it something I said?"

                    hide yoku

                    "He just walks off, shaking his head."
                    "I don't think I said anything that weird. People ask me about my hair all the time... I think."
                    "It's been a while since I've talked to people on relatively friendly terms. Maybe crazy is the new normal."
                    "If that's true, my friends might actually have a shot at freedom."

    "He didn't seem to have that much to say to me. That's fine, I'm not here to make new friends."
    "The sooner I can find a way out of here, the better."

    return

label introduction_uitto:

    play music "music/CoolNights.mp3"

    "I decide to check the back of the school."
    "Sun pours down into the center of the courtyard. It should feel warm and inviting."
    "Devoid of any activity, it's unsettling. I feel like I shouldn't be here."
    "I'm not alone, though. In the corner of my eye, I see a girl with a brilliant stream of scarlet hair."
    "She's looking out towards the sky with a forlorn grimace."

    n "Hey... uh, come here often?"

    show uitto smile

    u "No way, Nagen!?" id introduction_uitto_f7b33ed4

    "Her voice is definitely familiar. She turns to me with a wicked grin."
    
    show uitto smirk

    u "Did you seriously just hit on me? Good god, man, keep it together. You've been here, what, one day?" id introduction_uitto_e8e6308d

    "Oh no."

    n "Uitto, I didn't realize it was you!"

    show uitto serious

    u "That's supposed to make me feel better?" id introduction_uitto_2f86e2f4

    n "No. I mean kinda. I wasn't even flirting, I just-"

    show uitto talk

    u "Stop, stop. You're just digging yourself deeper, short stack." id introduction_uitto_f2190066

    n "I'm not that short!"

    show uitto playful

    u "Still shorter than me." id introduction_uitto_0a035f13

    n "You're in heels!"

    u "I'm 5' 7” without them." id introduction_uitto_c4d82eac

    n "....."

    show uitto smirk

    u "That's what I thought." id introduction_uitto_7c699b65

    n "You're evil."

    show uitto

    u "Only when I want to be." id introduction_uitto_981be6a2

    "I'll be honest, out of everyone, I'm not surprised she made it."
    "When we were kids, they used to call her 'The Closer'."
    "She could talk her way into and out of any situation and was a headliner in the pageant circuit."
    "It's not surprising she's taller than me either, just disappointing."
    "I had hoped to be taller than at least one of my friends."

    show uitto smirk

    u "Oh quit pouting. Size isn't everything, y'know." id introduction_uitto_f68145d8

    n "Knock it off, wench."

    u "Oooh, 'wench', going old English on me are we? What's next, 'harlot' or hauling myself to a nunnery?" id introduction_uitto_b238e09f

    n "Don't tempt me."

    show uitto talk

    u "With a sharp tongue like that, I'm surprised you're here." id introduction_uitto_ba84d43f
    
    n "Really? You were worried about me?"

    show uitto

    u "I'm serious, between the three of you, you're the last person I expected to see on the outside." id introduction_uitto_9946f09f
    u "Jona's an idiot and Hiro's basically harmless, but you?" id introduction_uitto_95c5b1ee
    u "You're smart and you're really bad about pretending to be nice." id introduction_uitto_5ae7396a

    n "Yeah, well, so are you."

    show uitto sad talk

    u "Yes, but I'm a poor defenseless girly that was bossed around by a scary guy with piercings and torn up pants." id introduction_uitto_7f3f77cb

    n "You're hideously manipulative. Is that really the story you went with?"

    show uitto

    u "Story? It's the truth." id introduction_uitto_d1ff3ab5
    u "You're the one that pitched a fit over not being leader, you should be flattered I gave you credit." id introduction_uitto_f12f817c

    show uitto yell

    u "Unless you told them something else..." id introduction_uitto_5c8123f2

    hide uitto

    menu:

        "I missed you":

            $ uRep += 1

            show uitto embarrassed

            u "Ugh, don't be gross." id introduction_uitto_dc0f0847

            n "I'm serious! I thought I'd never see you again."

            u "Yeah, me too..." id introduction_uitto_268abada

            show uitto sad

            u "Listen, if anything I said got you in trouble, I'm sorry." id introduction_uitto_d085ae4f
            u "I was just trying to think of what you guys would probably say and stick with the most common stuff." id introduction_uitto_cb60c1eb

            show uitto

            u "Well, you and Hiro. I figured you both would probably lie to protect the other." id introduction_uitto_084d242d

            n "So you lied to protect us?"

            u "And Jona would just lie to lie. All of us were doomed, it was just a matter of damage control." id introduction_uitto_04b9faa1

            n "Well that's a defeatist attitude."

            show uitto sad

            u "Yeah, being defeated tends to do that to a person." id introduction_uitto_19ea3d3a

        "It doesn't matter":

            $ uRep -= 1

            show uitto

            n "We're all here now, so why does it matter?"

            show uitto yell

            u "All of us?" id introduction_uitto_92b8d556

            n "Yeah; you, me, Hiro, and Jona."

            show uitto cringe

            u "That's not... How do you know they're here?" id introduction_uitto_01e18977

            n "Didn't they tell you?"

            u "They? Please tell me this is one of your paranoid delusions." id introduction_uitto_24987839

            n "No, the DVP's Secretary of BS told me during her dumb monologue."
            
            show uitto serious

            u "....."

            n "Didn't she talk to you?"

            u "....."

        "Of course I did":

            $ Charm += 1

            show uitto

            n "You were not a defenseless girly that was bossed around by a scary dude with awesome piercings."
            n "And these are my favorite jeans!"

            show uitto playful

            u "You're right! Who'd believe you?" id introduction_uitto_7fa99478

            n "Nah, I went with the silent, brooding approach. The less you say, the better."

            show uitto smirk

            u "You're joking, right? Brooding definitely, but silent?" id introduction_uitto_13039cc1

            n "Hey, I'm hella stoic."

            show uitto serious

            u "Nagen, your oversharing's one evil laugh away from a cartoon monologue. I mean, seriously, you need help. No offense." id introduction_uitto_1b797e64

            n "You wound me. My fragile ego can not handle an ounce of criticism."
            n "End your vicious slander or I shall end you. Muahahaha."

            show uitto smile

            u "I wilt not be-est tamed or commanded, foul villain. I wilt doeth what I wanteth." id introduction_uitto_45af3d43

    show uitto

    n "Anyway, we'll be meeting in the office room on the third floor."

    show uitto cringe

    u "We?" id introduction_uitto_e566768c

    n "I'm looking for the others right now. We're going to talk about our next move."

    show uitto yell

    u "Nagen, what are you talking about? We shouldn't be doing anything right now." id introduction_uitto_945d465e
    u "You know what's on the line." id introduction_uitto_f611094c

    n "Uitto, you gotta trust me on this, I know what I'm doing."

    #if Vision >= 10:
    #    n "Well, yeah... Uitto, is something wrong?"
#
    #    hide uitto yell
    #    show uitto cringe
#
    #    u "How did you know where to find me?"
#
    #    n "Well, I didn't know you were here. I've just been kinda wandering around." 
    #    n "We're meeting in 313 by four at the latest. Make sure you're there."
    #    hide uitto cringe
    #    show uitto sad talk
    #    u "...Yeah... whatever you say."
#
    #    hide uitto sad talk

    hide uitto

    "There are still other places to look at. I should go."

    return

label introduction_kitsune:

    "I'm honestly surprised they bothered to build this when there was a functional amphitheater on the grounds."
    "There's only enough seating for twenty to thirty people, but the walls are decorated to create the illusion of a vast balcony."
    "At least they didn't fill the fake seats with human silhouettes."
    "The stage itself is polished and well lit. It has more than enough space for rehearsals."

    show kitsune

    k "Isn't it beautiful?" id introduction_kitsune_56cebd29
    k "I was so worried when they picked this place that they'd shove us into a dingy room and call it 'rehearsal' space." id introduction_kitsune_c43e74a1

    n "It's a little small, don't you think?"

    show kitsune smug

    k "Compared to the pathetic platform most bars offer, this is an opera house." id introduction_kitsune_01f429bb
    k "There's even changing stalls! We'll be able to do great things with it." id introduction_kitsune_4f1cbf45

    n "We?"

    show kitsune shocked

    k "Aren't you a fellow performer? You're all dressed up and studying the stage." id introduction_kitsune_58813a66
    k "What else am I supposed to think; that you're just some Intelligence major?" id introduction_kitsune_23ab4c7b

    n "I {i}am{/i} an Intelligence major."

    show kitsune teary

    k "Oh..." id introduction_kitsune_2e9bd230

    n "Nagen Tesuta, proficient in memorization, can't get more common than that."

    show kitsune sulk

    k "N-nagen!? I- Oh my goodness, I didn't know it was you." id introduction_kitsune_26d0c65b
    k "I'm so sorry, you must think I'm a monster." id introduction_kitsune_660c522c

    "No harm was done, but it would be fun to mess with her a bit."

    n "It's okay. Since we're going with blind assumptions, I'm guessing Charisma major?"

    show kitsune shocked

    k "You mean you don't recognize me?" id introduction_kitsune_c8fab351

    n "No, why would I? Have we met or something?"

    "I never forget a face, but she's wearing so much makeup it's hard to tell where her face starts and the contouring ends."

    show kitsune apathetic

    k "W-well, I'm a rising star, everyone at this school should recognize me." id introduction_kitsune_f278b966
    
    show kitsune
    
    k "Like a phoenix from the ashes, I will guide our nation's culture with my brilliant light!" id introduction_kitsune_a20dda9f
    k "You are looking at living, breathing art; the face and voice of the future." id introduction_kitsune_b55a0aeb

    "Good god did I hit the nail on the head with this one."
    "I'd bet money she rehearsed that speech in the mirror while brushing her hair."

    n "Right... and what is it you do exactly?"

    show kitsune catty

    k "I am Kitsune." id introduction_kitsune_6aa67033

    "This girl is full of nothing answers, isn't she?"

    hide kitsune

    menu:
        "That's not a talent":

            $ kRep -= 1

            show kitsune mad

            k "Excuse me? Do you know how many years it took to perfect this?" id introduction_kitsune_a08f7bd7
            k "I woke up at 4AM to get ready and your only takeaway is 'she has no talent'!?" id introduction_kitsune_6620a48e

            n "They don't hand out Proficiency scholarships for being yourself." 
            n "Not that you're even doing that."

            k "I have enough class and good taste to pick out shoes brighter than your future." id introduction_kitsune_d6ca6b43

            show kitsune mad2
            k "You keep insulting people like that and someone's going to punch you so hard your piercings will get drilled into your gums." id introduction_kitsune_0c617268

            "What the ever-loving fuck did I do to her?"

            show kitsune apathetic

            k "But my dainty hands belong wrapped around a mic, so you're safe. For now." id introduction_kitsune_99e79e32
            k "I dazzle audiences with my angelic voice and you..." id introduction_kitsune_c62eb8fe
            k "Well, I suppose most people would be impressed by an 'iron clad' memory for a few minutes." id introduction_kitsune_5d239d42
            k "Even without my Proficiency, people would rather be me." id introduction_kitsune_983a7ea3

            "She seems to have calmed down now, but what was that? Does she want to fight me or not?"

        "Like the fox spirit?":

            $ kRep += 1

            show kitsune smug

            "I only know Uitto by her stage name; maybe this girl picked out her own?"

            k "Exactly! It embodies everything I am; enchanting, elusive and practically unkillable." id introduction_kitsune_4f7d164c

            n "Why not go by Tenko then? Aren't they more powerful or something?"

            k "They're old and wise; neither of which has ever been used to describe me, let alone powerful." id introduction_kitsune_20134fdf

            show kitsune talk2

            n "You'll get there eventually... in a thousand years."

            show kitsune mad
            k "Hey! I am a star right now. Just ask anyone who's gone to my show." id introduction_kitsune_94a63686

            n "I thought you were a fox?"

            k "Not literally! It's a metaphor. You know, to invoke imagery and imagination." id introduction_kitsune_73306cdd

            n "I imagine wise old men when people talk about fox spirits."
            n "Maybe it does suit you. You already have the white hair."

            show kitsune sulk

            k "Mom always said my white hair made me look elegant." id introduction_kitsune_7ffed8b4

            "Shoot, I didn't mean to upset her. Gotta backtrack."

            n "You saying old people aren't elegant? That's ageist."

            show kitsune apathetic

            k "...Is that your backwards way of complimenting me?" id introduction_kitsune_c759a51e

            n "I can forwards compliment you too if you want. You're just so fun to mess with, it's hard not to."

            k "Fun? After you've seen one of my performances, you may compliment me." id introduction_kitsune_dbc2cec1
            k "O-otherwise it would just feel like empty pandering." id introduction_kitsune_3a91a5d9

            "Says the person who was fishing for compliments five minutes ago."

        "And your Proficiency is...":

            $ Vigor += 1

            show kitsune talk1

            k "I specialize in vocal manipulation. My range is A0 to C8 in relation to a piano." id introduction_kitsune_5183cc53
            k "No other singer can compare to me without the use of technology." id introduction_kitsune_87b239d9

            n "That doesn't sound like a Charm Proficiency."

            show kitsune apathetic

            k "Because it's not." id introduction_kitsune_f12a7f66
            k "Not every Vigor major you meet is going to be some meathead jock." id introduction_kitsune_ea1c394f
            
            show kitsune talk1
            
            k "Still, I'm trying to see if they'll let me switch courses." id introduction_kitsune_2b53f00d
            k "I feel like Ms. Sato would help me become a more successful idol." id introduction_kitsune_c3320969

            n "I don't think this is that kind of school. You should focus on vocal training."
            
            show kitsune sulk

            k "I'm almost too old to start making my debut." id introduction_kitsune_ad6be019
            k "If I want to get anywhere, I have to start building my fan base now." id introduction_kitsune_270c19a5
            
            show kitsune

            k "Vocal training and dance lessons can happen while I'm on tour." id introduction_kitsune_40ae2cae

            n "That sounds backwards and exhausting."

            k "It's part and parcel with being in the industry." id introduction_kitsune_fc7dba0c

            n "But why even bother?"

            show kitsune talk1

            k "I like the attention." id introduction_kitsune_51ee40aa

            "At least she's honest. Seems like a lot of work for little reward."
            "There's no guarantee she'll ever get any fans."

    show kitsune smug

    k "I can tell you still have your doubts, but you'll be pleased to know I've already started working on my first album." id introduction_kitsune_5ea6e86a
    k "Make good use of this insider info, because people are going to eat it up!" id introduction_kitsune_d2e85db1

    n "With what? I thought all file sharing electronics were banned."

    show kitsune

    k "With CDs of course!" id introduction_kitsune_795c9dbf

    n "I don't own anything that plays CDs."

    show kitsune shocked

    k "Y-you don't? The school issued laptops, didn't they?" id introduction_kitsune_44246e95

    n "Yeah, but they don't have CD drives."

    k "Then how do you listen to music?" id introduction_kitsune_e22a1803

    n "Normally I'd use my phone and listen to stuff for free online."
    n "Now I'm stuck with whatever came on the burner phone."

    show kitsune teary

    k "Free!? Oh no, that's no good." id introduction_kitsune_ee8b55ff

    n "It's pretty standard nowadays."

    show kitsune talk2
    
    k "Well I'll just need to find a way to get music into the school." id introduction_kitsune_5f143fa1
    k "Maybe they'll allow older models of MP3 players and I could have the album on that?" id introduction_kitsune_04de6f6d

    n "That's not a horrible idea."

    show kitsune

    k "Great! I'll put you down for a preorder then." id introduction_kitsune_51e89d61

    n "I didn't mean-"

    show kitsune smug

    k "I'm sending your confirmation number through the school messenger aaaand, you're all set." id introduction_kitsune_49c0c66b
    k "The release date will be next spring." id introduction_kitsune_32180010

    hide kitsune

    "She blows me a kiss and runs off before I can finish objecting."

    return

label introduction_kazz:

    "I stumble across a dingy room tucked in the back of the second floor."
    "The furniture here is considerably older than the classrooms and in worse condition."
    "If it wasn't for a small, glass-paneled recording booth, I would have assumed this room was for storage."
    "Through the windows, I can see purple egg crate walls lined with foam."
    "A mic dangles from the booth's ceiling, hooked up to three different computers."
    "I try to go inside, but the door is locked."

    show kazz oh

    kk "What are you doing here? No one's supposed to be here, bromigo." id introduction_kazz_192d556c

    n "You're here, aren't you?"

    show kazz shine

    kk "I asked if I could check out the recording booth before I finished setting up in my room." id introduction_kazz_70a53425
    kk "I guess there are rules against soundproofing the dorms." id introduction_kazz_d5cb49a1
    kk "I'll be so bummed if the quality of my content worsens 'cause of cheap equipment." id introduction_kazz_3d823657

    n "What does that have to do with me being here?"

    show kazz complain

    kk "If something breaks or goes missing, I'll be the first person they blame." id introduction_kazz_f2a75827
    kk "I didn't mean to offend you, but my faith in humanity took a bummer turn by at least 46%% this year." id introduction_kazz_ed7484db
    kk "As long as I can record my show and no one leaves a mess for me to clean up, I'll make due." id introduction_kazz_6b06aee4

    n "You plan on making videos?"

    show kazz grin

    kk "Hell no, editing's boring and I look weird on camera. I'm trying to do an independent radio show." id introduction_kazz_206dc823
    kk "It's half audience engagement, half whatever the hell I feel like." id introduction_kazz_7ab711d5
    kk "I only have six listeners right now, but hopefully I'll be able to double that by this fall." id introduction_kazz_17d5ec8f
    kk "If you're interested, I could always use another editor." id introduction_kazz_6c75c7d5

    n "Radio isn't really my thing, but I'll, uhh, let you know later."

    kk "Right on! The name's Kazz by the way, Kataki, if that matters." id introduction_kazz_32e18956

    "It very much does matter if he is who I think he is."
    "Professor Kataki worked as an administrator at Estella alongside my father."
    "His research in neuroscience perpetuated the illusion that Estella Prep was helping people."
    "If this kid's his son, he could be one of the students that made competing for top marks a living hell."
    "Especially since he was proficient in math."

    show kazz talk

    kk "You look hella familiar." id introduction_kazz_3c28928a

    n "I used to go to Estella."

    show kazz grin

    kk "That's right! You're the kid that bailed on the nerd ward to hang out with all the criminals." id introduction_kazz_724fca85
    kk "I heard someone threw a desk at you the first day." id introduction_kazz_deed7e14

    n "...Yeah."

    "I had gotten into a fight with Hiro on my first day and I flipped a desk over in the process."
    "It's a wonder we ever became friends."

    kk "That's so cool! We never had anything interesting happen in our class." id introduction_kazz_1ba1ecb1
    kk "I kept hoping I'd get to join you guys, but my dad wouldn't let them transfer me." id introduction_kazz_2cc5c9d6

    hide kazz

    menu:
        "What did you do?":

            $ kkRep += 1

            show kazz grin

            kk "The correct question is, what didn't I do?" id introduction_kazz_d0e42c66

            n "....."

            show kazz talk

            kk "My homework. I didn't do my homework, any of it." id introduction_kazz_6e900c11
            kk "They never reported me, so I turned myself in, but they kept trying to sweep the whole thing under the rug." id introduction_kazz_9c17b1b3
            
            n "You stopped doing your homework to move to Special Ed?"

            kk "Oh, I never did it to begin with." id introduction_kazz_630dfed9
            kk "Busy work like that is just fluff that diversifies the grade points so one bad exam doesn't force you to repeat a grade." id introduction_kazz_c60cc17a
            kk "I did fine on exams, the assignments were a waste of everyone's time." id introduction_kazz_114c4717
            kk "I gave my homework to a willing volunteer and just copied their work in my handwriting." id introduction_kazz_443d659f
            kk "But apparently, that wasn't a 'real' problem." id introduction_kazz_aef2f276

            n "To be fair, that doesn't seem like a transferable occurrence."
            n "Not everyone in my class cheated on tests or had bad grades."

            show kazz sad talk

            kk "I guess that's true, but it seemed logical at the time." id introduction_kazz_250d9200
            kk "Dyre was an argumentative shit-head, all the teachers hated him, but they couldn't get rid of him because of his grades." id introduction_kazz_fef6d92b
            kk "Still, I hope this place won't be boring. The least they could do after bussing us here is to make it interesting." id introduction_kazz_e045f3d0

        "I didn't bail":

            $ kkRep -= 1

            show kazz talk

            n "They didn't give me a choice when they moved me. I would have gladly stayed in Regular Ed."

            "Granted, I wasn't terribly close with anyone in my old class."
            "It was more the embarrassment of being removed I hoped to avoid."

            n "Most of the kids were brought in for causing trouble at other schools."
            n "I was friends with the few normal kids in my class, the rest of it was a gigantic headache."
            n "It wasn't 'so cool'."

            kk "Woah there, Edgar Allen Bro, no need to be a downer. That was forever ago." id introduction_kazz_746d92ae

            n "It's barely been two years."

            kk "Exactly, it's all in the past." id introduction_kazz_59d81b67
            kk "If talking about this is going to bring up an ocean of salt, then forget I said anything." id introduction_kazz_b7f3ae0b

            n "My point was just that-"

            show kazz sad talk

            kk "No, I get it, middle school sucked donkey nards, sorry." id introduction_kazz_774cc3ea

            "I can't argue with that."

        "Why not?":

            $ Intel += 1

            show kazz talk

            kk "I'm not sure." id introduction_kazz_c734c3b2
            kk "Even after they knew I was plagiarizing all my work, they still kept giving me full points." id introduction_kazz_74bb4797
            kk "I turned in a paper that was the same page twelve times and I got an A." id introduction_kazz_e26e4faa

            n "That's some dedicated nepotism right there."

            "Why couldn't I reap the benefits of being a teacher's kid?"

            show kazz sad talk

            kk "Anything bad I did ended up making my dad look bad." id introduction_kazz_affb9ae4
            kk "My only guess is that he donated his time to the school in exchange for their silence." id introduction_kazz_15670eb6
            kk "The more boring answer would be that they didn't care enough to do anything." id introduction_kazz_68b17271
            
            n "No, the school cared way too much about their image to let a loose nail go unhammered."

            show kazz shine
            kk "I don't enjoy getting hammered. If I'm gonna party, I want to remember it." id introduction_kazz_c4bff718

            n "That's not even remotely related to what we were talking about."

            kk "Yeah, but it was funny." id introduction_kazz_e90643e4

            n "....."

            show kazz grin

            kk "You know, like a play on words." id introduction_kazz_33934715

            n "....."

            kk "I'm sure you're a blast at parties." id introduction_kazz_623ebdda
    
    show kazz talk

    kk "It's so trippy though, 91%% of the people I've met here used to go to Estella." id introduction_kazz_d26f20db
    kk "Most high schools pull in students from four to fifteen different primary schools." id introduction_kazz_cbd04e70
    kk "I should have found more people from different places by now." id introduction_kazz_dbfeff8b

    "No, no way. There can't be that many people from Estella here."
    "These people didn't just seek us out based on where we came from, did they?"

    n "This is basically like a private school, right? Maybe it just appeals to similar types of families."
    n "I'm sure there are plenty of kids here from other places."
    n "Or maybe it's so remote, the average commuter student can't go. Or... or-"

    "We're being collected here on purpose."
    "Why do they want us all in one place? What are they planning?"
    "There has to be a reason."

    n "I'm fine. I just need some fresh air."

    "I gotta move. I have to breathe."
    "Focus on walking. Kazz looks scared."
    "I need to calm down."
    "Shit!"

    show kazz worry

    kk "Do you need to go to the nurse?" id introduction_kazz_c436a0f4

    n "NO! I mean, no, I'm fine. I promise."
    n "I won't mess with your shit in the recording booth."
    n "I'm sorry, I'm fine, really."
    
    hide kazz

    "He still looks worried, but I'm already out the door."

    return

label introduction_oshin:
    
    "The nurse's office is small, to say the least."
    "It can barely fit two pennies in between all the filing cabinets and office supplies."
    "There's no needles out, which is good, sharps freak me out."
    "In fact, even the smell of latex and hand sanitiser can sometimes set me off, but this place reeks of something else."
    "Like bitter, musty salad that rotted in a pool of Ax body spray." 
    "Do people still even use that stuff?"

    mu "For the love of- Where on Earth did that lighter go?" id introduction_oshin_f75733d8

    "That doesn't sound like a nurse." 
    "I see rustling behind the curtain of the back cot. It couldn't be..."

    n "Are you seriously smoking in here? Who's dumb enough to try and smoke in the nurse's office?"

    "The curtain flies back and I have to say, I am severely disappointed."

    show mu

    "If you're going to break the rules, at least look cool doing it."
    "Or shower first."
    "He used to take so much pride in 'knowing' more than me in biology and anatomy; I wonder if he still has that competitive streak."

    show mu cringe
    mu "Some nurse's office. I can't find a single compression wrap or ice pack, let alone an O2 tank." id introduction_oshin_710b1e93
    mu "Granted, that means the building isn't at risk for exploding right now, but I feel bad for anyone with asthma." id introduction_oshin_2bc0e829
    mu "They're screwed." id introduction_oshin_bd1c190e

    n "You're going to give someone asthma smelling like that. Besides, we both know that's not why you're here."

    show mu smug

    mu "As the nurse's assistant, it's my job to take inventory. So yeah, that's why I'm here." id introduction_oshin_32b00122
    mu "What I do on my fifteen-minute break is another matter." id introduction_oshin_00e9932f

    n "You're the nurse's aid?"

    show mu laugh

    mu "For part of the day." id introduction_oshin_0ffa07e3
    mu "They don't have a sports medicine program, so shadowing the school nurse was the only way I could use my Proficiency in biology here." id introduction_oshin_4962eec3
    
    show mu irate
    
    mu "Well, it was that or be a TA for the Intel Professor during science lectures but... blegh, I hate theory." id introduction_oshin_c8c1e042
    mu "I came here to learn, not to grade papers." id introduction_oshin_2d504784

    "That's something I can sympathize with as a fellow Intelligence major. When they ran out of things to teach you, they'd give you busy work."
    "So this is the limit to having a Medicine Proficiency."
    "When he'd go off in class about internal organs, I thought he'd grow up to be a serial killer, not a stoner."
    "Still, he isn't the first person I'd choose to patch my wounds."

    n "Let me guess, you get paid in 'experience'."

    show mu greet

    mu "And college credit." id introduction_oshin_399af8b0

    hide mu

    menu:

        "You should have TA'd":

            $ muRep -= 1

            show mu angry

            n "Sure you'd have to grade papers and junk, but it's less work for the same grade."
            
            mu "I hate theory, and explaining the theory to the uneducated- Ugh!" id introduction_oshin_ce8b0b34
            mu "Every part of the human body is connected, you can't understand one of them without knowing the others." id introduction_oshin_0e139123
            mu "Unless someone knows the basics, I can't begin to help them and no one knows the basics." id introduction_oshin_7625680f

            n "Your idea of basic is above average. It can't be that bad."

            show mu cringe

            mu "I was in class with someone who asked if you could get pregnant through your stomach." id introduction_oshin_eac8884d
            mu "I couldn't help it. I laughed at the poor girl, but she was serious." id introduction_oshin_f1305049

            n "...Why'd a girl ask you that?"

            show mu irate

            mu "I. Don't. Know." id introduction_oshin_8799f8e6
            mu "People hear my Proficiency and think it's permission to ask and show me all the gross things they're too scared to talk to an actual doctor about." id introduction_oshin_39a132c9

            n "Oh."

            show mu irate talk

            mu "People will ask me weird stuff no matter what I do." id introduction_oshin_0b2c008a
            mu "At least this way it's less people and I won't have to read essays." id introduction_oshin_823fc497

        "Are you going to use it?":

            $ Intel += 1

            show mu awkward

            mu "Maybe. I mean, I guess it'd cover A and P, but..." id introduction_oshin_0e7faf3a
            mu "I don't know if it's worth the money or effort." id introduction_oshin_db454c3a

            show mu disgust
            
            mu "If I'm taking on heaps of debt, I need to be certain it's for something I actually want to do." id introduction_oshin_353cc2f6
            mu "Med school doesn't look kindly on the uncertain." id introduction_oshin_655f4c1b

            n "What else would you do?"

            show mu talk2

            mu "Homeopathy, pharmacology, farming; whatever's easiest." id introduction_oshin_cab49130

            n "Farming?"

            mu "Yeah." id introduction_oshin_5e069057

            show mu laugh

            "He blows out a cloud of smoke."

            mu "Agricultural farming." id introduction_oshin_99b38992

            n "Must be nice to have so many options."

            show mu pout

            mu "Yeah, if only those options didn't cost the same as a new house." id introduction_oshin_cdbfcdc4

        "Need any help?":

            $ muRep += 1

            show mu angry

            mu "What do you know about medicine?" id introduction_oshin_5b711623

            "Ironically, I know quite a bit about medicine."
            "My father was particularly enchanted with using me as a test subject for all his patent drugs."
            "Most of what he made were stimulants or Proficiency enhancers, neither of which would be applicable here."
            "However..."

            n "I meant with finding your lighter."
            n "I didn't hear anything fall, so it's probably on the bed somewhere."

            show mu grin

            mu "Oh dang, yeah. It's not mine though. It's the nurse's." id introduction_oshin_a9f5ce91

            n "What would they need a lighter for?"

            show mu pout

            mu "You really think I'd be smoking in here without permission?" id introduction_oshin_2b2494ff

            n "Well, no, but I assumed you didn't care. I didn't think you'd ask-"

            mu "Of course I'd tell the nurse if I was smoking; she's the one I'd have to go to if I overdo it." id introduction_oshin_195c8fe5
            mu "Found it!" id introduction_oshin_76fd57e3

            "He holds aloft a small lighter with a skeleton on it."

    show mu talk1

    mu "Why did you come here anyway? Have any allergies or scripts the nurse needs?" id introduction_oshin_5bb56cb4

    n "No. Just figuring out where everything is."
    n "If they make us participate in P.E., I'll end up here eventually."
    n "I have a strange knack for getting hit in the face with sports equipment."

    show mu grin

    mu "Wait, no way. Were you the kid that got a bloody nose from a sprout ball?" id introduction_oshin_61220cc8

    n "They're harder than they look."

    mu "They're made of yarn, man, it doesn't get cushier than that." id introduction_oshin_66acd8f0
    mu "I thought Dyre was exaggerating all those times. That's too rich." id introduction_oshin_795edc54

    "I don't think he's going to stop laughing any time soon."

    n "Well, now I know where the nurse is supposed to be. I'll be going now."

    mu "Hey, hey; watch out for flying pompoms. Wouldn't want you to have to check in on your first day." id introduction_oshin_356ca426

    n "Hilarious."

    hide mu

    "Unfortunately, I've been injured by less threatening objects."
    "What he said in jest could very well happen if I run into the wrong cheerleader."

    return

label introduction_ichita:

    "When I think of high school, I imagine a gray cement building with crowded halls and an oppressive air about the place."
    "The kind that's earned from decades of kids grinding gum into the pavement."
    "Maybe it's because this place hasn't been a school for very long, but the entryway doesn't feel haunted."
    "It makes it all the more jarring to see someone declaring how happy he is to be here."

    show ichita grin

    i "I finally fuckin' made it!!!" id introduction_ichita_82db06dd

    "Waaay too happy for the first day of school."
    "I'm spotted and held socially hostage before I can escape the predatory grip of an excited, one-legged extrovert."

    i "My. Dude. Do you know where we are?" id introduction_ichita_bd32e5c1

    n "...Outside?"

    i "Exactly!" id introduction_ichita_b87f94ab
    i "No stupid bleach smell or 'round the clock nannies or time-eating fluorescent lights." id introduction_ichita_e5fd6727
    
    show ichita mock
    
    i "Just actual dirt and the actual G.D. sun!" id introduction_ichita_26eab235
    i "I'm sure you could care less about the sun, but I missed it." id introduction_ichita_99215c44
    
    "He's almost shaking me as he speaks. Or maybe he's struggling to stand."
    "I'm not entirely sure which, I just wish he'd stop touching me."

    n "Have we met before? You're being really... friendly with someone you just met."

    "Just as I'm contemplating peeling his hands off my jacket, he lets me go and laughs."

    show ichita grin

    i "I don't think anyone's ever called me that before. Ichita, maybe you've heard of me." id introduction_ichita_874ff11f

    "I have."
    "A competitive martial artist that chased after championship titles and treated his opponents like rag dolls."
    "Hiro was the only one who could withstand his brutal strength Proficiency in a match."

    n "Yeah, though nothing flattering comes to mind."

    show ichita mock

    i "That figures; can't say I'm surprised." id introduction_ichita_070cbbaa
    i "Don't listen to anything those sore losers told you. They got left behind for a reason." id introduction_ichita_cafa0b35

    "Wasn't he the one that always came in second place? If anyone was a sore loser, it was him."

    i "No need to look so scared. I don't bite." id introduction_ichita_c0ca92be

    hide ichita

    menu:

        "I wasn't scared!":

            $ Vision += 1

            show ichita sad talk1

            i "You were making a little scared face." id introduction_ichita_7720aa4e
            i "Your eyes got all wide and you kept looking at my teeth. You're like an open book." id introduction_ichita_85a7d09f

            n "I wasn't making a face. This is how my face always looks."

            i "....."

            n "I'm serious; I don't know what you're talking about."

            i "Oh you poor cinnamon roll, you're going to be eaten alive." id introduction_ichita_0ee21ff2

            n "I don't need your pity... and quit laughing."

        "Hiro said you do":

            $ iRep -= 1

            show ichita lecture

            i "Hiro?" id introduction_ichita_69828990

            "His whole demeanor changes. I regret bringing him up."

            show ichita angry

            i "That shit storm loved to run his mouth in front of a willing audience." id introduction_ichita_fab8b657
            i "Too bad most people didn't have the sense to ignore him." id introduction_ichita_7b451d46

            "I know better than anyone that Hiro had a tendency to exaggerate."
            "I still believe this guy was willing to jump him in the parking lot after he lost a match."

            i "So you're that stray's plaything? How funny." id introduction_ichita_62f80577

            "Neither of us are laughing."

            n "I think you got the wrong idea. I'm not-"

            show ichita mock

            i "Relax. I know you have nothing to do with what he says." id introduction_ichita_09853a46

            "He seems happy with whatever decision he's made about me, but his smile doesn't put me at ease."

        "Neither do I":

            $ iRep += 1

            show ichita grin

            i "Hah, look at you." id introduction_ichita_14ff9278

            "I feel like he's treating me like a little kid."

            n "You don't know my rep sheet. I could be a dangerous drug dealer or something."

            i "I don't buy it. You're giving off more aggressive social outcast vibes." id introduction_ichita_69335f91

            "This conceited-"

            i "Maybe with our combined forces, we'll be able to change how people see us." id introduction_ichita_1948aade

            "Hunh? Wait, that wasn't even remotely sarcastic."
            "He's looking at me with so much hope..."

            n "Yeah, sure."

            i "I can work with that!" id introduction_ichita_16034ee8

            "At least his expectations are low."
    
    show ichita sad talk1

    i "Sorry for coming on super intense. It's been a while since I've talked with another person my own age." id introduction_ichita_ce9e8abe
    
    show ichita sad talk2
    
    i "Oh shit, I didn't even ask you what your name is." id introduction_ichita_c43354dc

    n "It's Nagen. But yeah, I wanted to ask you why you're so jazzed to be here."
    n "You're acting like you just got out of jail instead of walking towards one."

    show ichita sad talk1

    i "Compared to a hospital, this place is a theme park!" id introduction_ichita_13849e8b
    i "Okay, maybe closer to a themed restaurant or summer camp, but you get the idea." id introduction_ichita_f9e4287e

    n "How long were you in the hospital?"

    i "Almost a year and a half in and out. I was really sick when they found me." id introduction_ichita_0f36be7b
    i "Who knew a scraped knee could take your whole leg?" id introduction_ichita_c4d1f415
    i "Agh, too dark, sorry. Still working on 'positive thinking' or whatever they call it." id introduction_ichita_5e26922d

    n "You don't have to force yourself to act happy for my sake."
    n "Half of what I talk about with my friends is stuff that pisses us off."

    show ichita grin

    i "Thanks, but if I stop now, it won't be pretty." id introduction_ichita_405e055b
    i "Besides, I promised I'd try to 'perk up' and- ugh- yeah. It'd suck if I threw in the towel on the first day." id introduction_ichita_4cf853be

    n "Suit yourself."

    i "I gotta check out what kind of gym they threw together." id introduction_ichita_f7f52ba1

    n "That's all you. I'll see you around."

    hide ichita grin

    "There are still some other places I haven't checked yet. I'll keep looking."

    return

label introduction_taiga:

    "I make my way to the uppermost floor of the main building."
    "The entryway to the stairs is blocked off with piles of wood and neglected supplies strewn about."
    "I wonder if they put a hold on renovations; I don't see any tools laying around."
    "I slip through a gap in the tarp and get blinded by sunlight."
    "Anything that couldn't be salvaged has been left to rot in the elements."
    "However, the palettes and busted shelves are too carefully arranged to say they were abandoned."
    "Looking out over the expansive grounds is a kid in loose-fitting festival robes."
    "He gives me a passing glance and resumes glaring at the horizon."
    "There's an obligatory fence, but nothing to stop students from sitting on the edge."

    show taiga

    t "Looking for a way out too?" id introduction_taiga_e2a241c5
    t "If you were thinking of running off into that forest, you best forget about it." id introduction_taiga_cd9c9aa8

    n "Did you read about that in the brochure?"

    "He shudders."

    show taiga grumpy

    t "If there was a way to escape this place, I would have found it." id introduction_taiga_7cc6797f
    t "It's not fair!" id introduction_taiga_ea85a185
    t "I didn't do anything to get stuck in a place full of criminals; nothing criminal about wanting freedom." id introduction_taiga_1ec42404

    show taiga grimace

    t "So, what'd ya do to end up here?" id introduction_taiga_c48f812c

    n "What makes you think I did something?"

    show taiga gasp

    t "If your folks could trust you, you'd be getting schooled in some refugee camp, but you're not, you're here." id introduction_taiga_874e0963
    t "So either you kept running away from where they put ya or ya did something." id introduction_taiga_143e9454

    "His attention is more focused on something in his lap."

    n "It's kind of a long story, I really don't want to get into it."

    show taiga

    t "That's cool." id introduction_taiga_9c18c8cf

    "A small furry face pops out from under his sleeve."

    n "What the-"

    hide taiga
    show taiga sad talk2

    t "Shh. You'll spook him." id introduction_taiga_7e92f99c

    "It's a gray lop-eared bunny with a blue-collar."
    "His coat is broken up with a handful of scars, but overall, he seems healthy."
    "I've never seen a rabbit so calm before."

    hide taiga

    menu:

        "Can I pet him?":

            $ tRep += 1

            show taiga smile talk

            "Perhaps I was too eager with the way I asked."
            "He stares, shell shocked, before nodding."

            t "Just don't move too fast, he's been a little skittish since the move." id introduction_taiga_72422588

            "I sit down next to him and hold out my hand to the rabbit."
            "It cautiously sniffs my hand before sinking its teeth into the leather of my glove."

            n "Hey!"

            "I try to pull back, but the rabbit won't let go, all while his owner laughs."

            show taiga sad talk2

            t "Okay, okay; I get it. I'll make him take the glove off, but you have to let go first." id introduction_taiga_53ee74a1

            "Freedom!"
            "I make sure there are no holes before looking back at the offended rabbit."

            show taiga suspicious

            t "Sorry about that, he just really hates gloved hands. One too many V.E.T. visits." id introduction_taiga_a1b8d838
            t "I promise he won't bite. Isn't that right?" id introduction_taiga_235202e5

            "I've never seen an animal look so personally attacked before."
            "He keeps licking his owner's hand as I pocket my glove."

            show taiga grin

            t "Deep breath, keep a steady hand and go for the cheeks." id introduction_taiga_3fac89c1

            "I follow his instructions and get immediately rewarded. The bunny practically melts in his lap."

        "Pets are forbidden":

            $ tRep -= 1

            show taiga sad talk1

            t "Houdini isn't a pet." id introduction_taiga_f34b2317

            n "Oh, don't tell me he's an emotional support animal or something."

            "His cheeks light up bright red and his eyes narrow."

            show taiga annoyed

            t "This stupid faculty thought I wouldn't cooperate, so they used my assistants as bait to get me to stay." id introduction_taiga_4eca6481
            t "The others are still being held hostage somewhere." id introduction_taiga_3e7f57f2

            "Does that mean there are more rabbits hiding in the school?"

            n "And what exactly does this little guy do to help you?"

            t "Anything within reason. For example..." id introduction_taiga_55a0a1fc

            show taiga scheme

            t "Hou, don't you think it'd be funny to piss on the little rich boy's boots?" id introduction_taiga_38b93b23

            "Rich is an overstatement, but before I can form a response, there's a rabbit on my foot."

            n "Nonono-"

            show taiga smile talk

            t "Good boy, Hou." id introduction_taiga_b8d5af1a

            "The little gray monster scampers into his sleeve to hide."

        "Aren't you scared?":

            $ Charm += 1

            show taiga grin

            t "Scared? Scared of what, the school?" id introduction_taiga_0fbda608
            t "The teachers are just people diving into a collective midlife crisis. I'm more annoyed than anything." id introduction_taiga_29ffe0b4

            n "I meant about having an animal this close to the edge of the roof. He could fall."

            "He stares off into space, retracing the conversation in his mind."

            show taiga

            t "No. I told him to stay away from the edge." id introduction_taiga_189fda8c

            n "O-okay?"

            "There's nothing keeping that animal in his lap other than sheer willpower."

            show taiga grimace

            t "Just, don't tell the teachers you saw him out here." id introduction_taiga_911db477
            t "He's supposed to be in his stupid cage in my dorm." id introduction_taiga_6f6d3933
            t "But bunnies are social creatures. They aren't supposed to be alone." id introduction_taiga_738ec746

            n "If you say so..."

            t "....."

            n "....."

            show taiga

            t "He's not going to jump out of my lap to become an angel. It's okay." id introduction_taiga_221df70e

            "I can't help but be concerned when he doesn't even have a hand on him."
    
    show taiga smile talk

    t "His full name is Houdini; Angel and Blaine are still somewhere under lock and key." id introduction_taiga_ba60f1f1
    t "We're already trapped in the facility, additional cages are just over the top." id introduction_taiga_0912a0ef

    n "I assume Angel and Blaine are also bunnies?"

    t "Yeah." id introduction_taiga_3c0d50d6

    n "And your name would be..."

    show taiga

    t "Oh, Taiga." id introduction_taiga_48ae3a4a

    "The longer the silence goes on, the more puzzled he looks."

    n "I'm Nagen Tesuta, my Proficiency is Memory."

    t "Oh, well then. I'm Taiga... Sakurai, I guess. My family wasn't big on formalities." id introduction_taiga_4bbd5c7c
    t "I can talk to animals, but I don't understand what they say back if that makes any sense." id introduction_taiga_0100d1e9

    "Did he make up the last name?"
    "It does sound familiar, but I don't remember anyone with that name going to Estella Academy."

    t "Just Taiga is fine. I hope the teachers remember that." id introduction_taiga_b8fa49af
    t "Having someone call me Mr. Sakurai would be weird." id introduction_taiga_eb19559a

    n "They'd do that?"

    show taiga grimace

    t "If you get in trouble, probably." id introduction_taiga_beafdcd0

    "I really hope not. It was weird enough getting called that by the principal."
    "Both of my parents were teachers, so any time I hear 'Mr. Tesuta', I think of my dad."

    t "It's going to be a long couple of years." id introduction_taiga_ec7dadac

    hide taiga

    "I couldn't agree more, but this conversation's kind of bumming me out. Not that I blame him, but I should go."

    return

label introduction_chisei:

    "Out of all the rooms in the whole school, this is the only one that hasn't been remodeled."
    "The bookshelves are molded into the walls, floor to ceiling."
    "A walkway splits the shelves in half, allowing access to the topmost shelves."
    "To think that the whole building once looked like this."
    "Hidden amongst the shelves is a girl with dark hair."

    scene backgroundP5

    ch "Am I in your way?" id introduction_chisei_e567cf98

    "She stands fixed in place in front of one of the shelves, refusing to look at me."

    n "No, you're good, didn't mean to scare you. I'm just surprised someone else wanted to come here."
    n "Y'know, since there are books all over the place."
    n "Having another room dedicated to them when they won't fit is a little odd."

    "At least this part seems organized as opposed to books crammed randomly anywhere they fit."
    "She looks down at the floor."

    ch "I will admit, I was hoping to postpone meeting new peers until the last possible moment." id introduction_chisei_1af12464
    ch "I supposed it would be better to introduce myself to one individual at a time then to the whole class..." id introduction_chisei_cde1c5ec
    ch "I am going to turn around." id introduction_chisei_94a66c8b

    n "Okay..."

    ch "I just do not mean to startle you. My appearance is substantially damaged." id introduction_chisei_7746be2a

    scene backgroundlibrary

    show chisei
    with dissolve

    ch "It was from an accident. No, it does not still hurt and please do not touch me." id introduction_chisei_297bf1d8

    "I summon all my willpower not to yelp in surprise."
    "Despite my best efforts, I can feel my eyes wander back to her torn-up arm."
    "I'm no expert, but I'm pretty sure she's missing some muscles in her arm and... is that a robot hand?"
    "I've been staring too long, I've got to say something."
    
    ch "....."

    hide chisei

    menu:

        "I'm so sorry":

            $ chRep -= 1

            show chisei frown2

            ch "All you have done is stare." id introduction_chisei_4ae92512
            ch "Unless you have thought something uncouth, there is no need to apologize." id introduction_chisei_2807d50a

            n "What? No!"

            show chisei sad talk2

            ch "No laughter. Perhaps my delivery was not whimsical enough?" id introduction_chisei_5d8bd27e

            n "O-oh."

            ch "It is human nature to stare. We will both just have to wait until it gets boring for you." id introduction_chisei_2100fcda

            "She talks with barely any emotion at all."
            "It's hard to tell if she's trying to make another joke or if she's being sincere."

            n "....."

            show chisei frown2

            ch "Another botched attempt." id introduction_chisei_c4620f75

            "She sighs."

            ch "This is going to be a long year." id introduction_chisei_fde54abe

        "Sick robot hand":

            $ chRep += 1

            show chisei sad talk3

            ch "It is not humanoid, but it serves me well. You are the second person to compliment it." id introduction_chisei_4e21103b

            "She hides her gaping smile behind her other hand."

            show chisei smile

            ch "I guess you could say, its appeal has had a mass effect on people?" id introduction_chisei_892e7828

            "She giggles as I realize with dawning horror she's one of those people who loves puns."

            n "Oh, that one hurt. Why?"

            show chisei smile talk1

            ch "I have been waiting for someone to set me up for that all day!" id introduction_chisei_e341f7b5

            n "Why'd you have to inflict your bad joke on me?"

            show chisei smile talk2

            ch "The best person to share a pun with is someone who hates them. That is just common knowledge." id introduction_chisei_fbfecdcf

            "I can practically feel her adding me to a list of victims."

        "What's your major?":

            $ Vision += 1
            
            show chisei talk3

            "It's basic small talk, so why does she look so down?"

            ch "I am a playwright." id introduction_chisei_dd558aab

            n "I thought you were an Intelligence major?"

            show chisei talk1

            ch "I should be." id introduction_chisei_d3403f61
            ch "I should be in classes that help me improve my skills as a writer and collaborate with other creatives." id introduction_chisei_93547aaa
            ch "But Guwon does not recognize 'dual' proficiencies so it does not matter how good my writing skills are anymore." id introduction_chisei_0709462f
            ch "Because something strange happens to me, I had to change majors." id introduction_chisei_5d4df083

            n "...You're a Vision major?"

            ch "Not by choice. Until I can gain full control of my other hand, I am stuck there." id introduction_chisei_f4d3e0f0

            "Having a prosthetic shouldn't affect your major. Maybe she can't write as well with her left hand?"
    
    show chisei talk1

    ch "We likely will not be in any of the same classes this year. I hope to be able to change that soon." id introduction_chisei_a92a70ab
    ch "Until then, if you happen upon any unsettling rumors, please feel free to address them with me directly." id introduction_chisei_1a51a7bb

    n "Unsettling how?"

    show chisei sad talk1

    ch "I have become a channel for the unseen; well, my hand has anyway." id introduction_chisei_652ded61
    ch "People could claim any number of things about my writing; about me." id introduction_chisei_c198b46a
    ch "I figured the best plan is to handle it with complete transparency." id introduction_chisei_45f8ae99

    n "So you're a medium of some kind?"

    show chisei sad talk2

    ch "No. That is not something I have ever wanted to be." id introduction_chisei_1a7041ca
    ch "However, there is something at this school that is trying to take advantage of my hand's weakness and write messages with it." id introduction_chisei_98b4174d

    n "Has this 'thing' told you anything about me?"

    hide chisei

    if Hero >= Villain:

        show chisei smile

        ch "...Yes." id introduction_chisei_abce4fc9
        ch "It does not want me to believe what others may say about you; that you are a good friend and an honest person." id introduction_chisei_3283aa03

        "Not exactly the creepy mentalist stuff I was expecting."
        

    else:

        show chisei frown1

        ch "....."
        ch "Sometimes I think my mind is playing tricks on me." id introduction_chisei_91107c21
        ch "Maybe the teachers will see that and put me back with the normal Intelligence majors." id introduction_chisei_996b2af2

    show chisei sad talk3

    ch "I do not like the idea of invading someone's privacy." id introduction_chisei_92f035c8

    n "You really believe you're being contacted by some unseen entity?"

    ch "It is hard for me to deny at this point. I just hold onto the prospect that one day I can get it to stop." id introduction_chisei_584dc6ef

    n "Good luck with that."

    show chisei smile talk1

    ch "Thank you." id introduction_chisei_ae4a09a7
    ch "Well then, I must be off. Good day, Nagen. I hope you are able to find what you are looking for." id introduction_chisei_5db3d1fa

    hide chisei

    "She shuffles away, carrying with her a heavy black book... I never told her my name."

    return

label introduction_shoma:

    "As I exit the third floor, I see light trickling through the bottom of an unmarked door."
    "Curiosity gets the better of me and I take a step inside. The air is thick and humid."
    "A small swamp cooler rattles in the back window, struggling to cool the room by a degree."
    "A boy is setting up a retro sewing machine that looks like it's been fetched out of a dump."
    "He looks up with a smirk, eyeing me up and down."

    show shoma observe
    
    sh "Ah, I see we've dressed ourselves today." id introduction_shoma_c5e7e91d
    
    n "Hey, just because you know how to plug in a sewing machine doesn't mean you can judge me for what I'm wearing."

    show shoma sparkle

    sh "Okay, okay; just an observation. I never took you for the punk type." id introduction_shoma_823bcfab
    sh "Having no uniform restrictions has really opened my eyes to what our classmates are comfortable wearing." id introduction_shoma_83b7b90d

    "Eyes... Oh, this is that kid from the Vigor program that Hiro always told me about."
    "All the Vigor majors he'd met before gravitated towards sports, but not him."
    "The guy's got eyes able zoom in and out like a camera."
    "He used to sit in the back of the class, a bit of a loner type."

    show shoma talk1

    sh "Shoma Nishimoto, but you probably remember that, hunh?" id introduction_shoma_dca325ec

    n "Yeah, though this is probably the longest we've ever talked."

    "...Probably shouldn't have led with that."

    n "But it's good to see you. The more kids I find from our old homeroom, the better I feel."

    show shoma manic

    sh "Yeah, I know what you mean. I'm kinda glad there's more crossover classes than just homeroom." id introduction_shoma_156e8db9
    sh "Hopefully, it will help all the majors get along better. It's gotten so competitive lately." id introduction_shoma_3020c731

    n "So what are you doing here?"

    show shoma talk2

    sh "Well, the school couldn't supply a proper costume shop of any kind, but they said I could use this room." id introduction_shoma_68b1c290
    sh "So... I'm trying to make due." id introduction_shoma_88d98381

    "This place has multiple theaters but no place to make the costumes? That doesn't make sense."

    hide shoma

    menu:

        "What's with the machine?":

            $ shRep += 1

            show shoma talk1

            n "I know they're low on funds, but the least they could do is get you a modern sewing machine." 
            n "That thing looks ancient."

            sh "Well, actually, this is mine from home. I know it's pretty old, but at least it works." id introduction_shoma_f34fc9b3
            sh "Besides, this way it doesn't fall under the tech restrictions." id introduction_shoma_14d1c535

            n "I suppose that's true."

            sh "More modern machines try to take the human element out of fashion." id introduction_shoma_270d4033
            sh "A pair of pants is far more impressive if you know a person made it without the aid of factory machines." id introduction_shoma_756cfead

            n "Do you make your clothes on this thing?"

            show shoma sparkle

            sh "Most of them! I'm not good with knitwear, but other than that, it's all me!" id introduction_shoma_5ac91779

            n "Honestly, I wouldn't have been able to tell."
            n "I attempted a wallet stitch in grade school and found it wasn't for me."

            sh "That's quite the compliment considering your taste." id introduction_shoma_d12c45b6

        "Your stuff's going to melt":

            $ Vigor += 1

            show shoma sad smile

            sh "I'm not sure that's possible." id introduction_shoma_6852dacd

            n "It is stupidly hot in here considering it's still spring. What are you going to do in the summer?"

            sh "Well, we won't be here during the summer." id introduction_shoma_ff8ffcc9
            sh "The room may be warm now, but it'll get cooler as the year goes... I hope." id introduction_shoma_a9bfe25f

            n "They're not going to fix it?"

            show shoma sad

            sh "Technically this was a storage closet, so air conditioning is really low on the list of things the school needs." id introduction_shoma_c107407d

            n "Then ask for a different room. There has to be someplace more comfortable for you to set up shop."

            show shoma sad smile

            sh "Oh no, I could never." id introduction_shoma_d53f75aa
            sh "They've already been generous enough to lend me this space, as long as I don't throw out anything they store here." id introduction_shoma_a306402a

            "He doesn't seem the least bit annoyed by that."
            "If that had been me, I would have already marched down the hall demanding a room change."
            "Well, if it really doesn't bother him, there's nothing I can do."

        "This is boring":

            $ shRep -= 1

            show shoma observe

            sh "Ah, yes. Unpacking generally isn't fun. You could offer to help instead of complaining." id introduction_shoma_0d1e9bf0

            n "I could. I could also rip on you for wearing fall clothes in an unairconditioned sweatshop."
            n "But I'm not going to do either."

            sh "You're not a very creative person, are you?" id introduction_shoma_ac0f9670

            "I can tell he's not trying to be rude, which makes it worse."

            n "....."

            show shoma

            sh "If you come back after I'm done setting up, I'll try harder to be an entertaining host." id introduction_shoma_bac4734d

            "So not helping."

    show shoma talk2

    sh "I'm sorry, it seems my mind is all over the place." id introduction_shoma_959755da
    sh "I honestly wasn't expecting to talk to another human being until class started." id introduction_shoma_0f01d193

    n "Really? Then why did you come onto campus the day before?"

    show shoma mad

    sh "Well... This place... I need a place to create that isn't where I sleep." id introduction_shoma_73cb9cca
    sh "Then I'd be spending way too much time in my room and I... I'm trying to break myself of that habit." id introduction_shoma_baee56a8

    n "I see... what exactly do you plan to do here?"

    show shoma lie

    sh "Mostly alterations, unless I can get my hands on some larger materials." id introduction_shoma_768dd5ea
    sh "I could buy some, but it would mean taking commissions." id introduction_shoma_4dd2ea58

    n "What's wrong with that?"

    show shoma sad

    sh "I'm not really... comfortable with women's wear, and I have a feeling that would be in the highest demand here." id introduction_shoma_95b8b66e
    sh "There are only so many vague gown requests I can handle. I'd much rather do something new." id introduction_shoma_368f2e37

    n "You might have to adjust those biases if you want any clients."

    sh "I know, I know. I just need to find a way to get motivated to sew a circle skirt." id introduction_shoma_0a822c6b

    "It's as if he's peering into a dark void off into the horizon. I'm not sure what he's seeing."
    "He shudders a bit and then smiles at me."

    show shoma sparkle

    sh "But if you or your friends ever need something, I'm always up for a challenge." id introduction_shoma_cd82b23a
    sh "I could make some really cool 'punk' stuff out of some strange materials if you find stuff for me." id introduction_shoma_96a28033

    n "Are you sure?"

    "Even though we were in the same homeroom, we weren't friends exactly."
    "He's just someone I kind of grew up with. That's not exactly the relationship that gets you free stuff."

    sh "Of course! Just... I'll need money, or the materials, upfront if I want to make anything new." id introduction_shoma_790c0c11
    sh "I hope coming here will be worth my time." id introduction_shoma_c0ea3040
    sh "Beats sheltering at my uncle's place and rotting in front of a TV, that's for sure." id introduction_shoma_36828be9
    sh "At least here, I can sew without people bugging me." id introduction_shoma_e570ca19

    n "I'm sure it will be fine. Granted, it'll suck being cut off from... everything."
    n "But there's other things to do too. You just got to get creative is all."

    show shoma talk1

    sh "Y-yeah... thanks, Nagen, but I think I'm going to wrap up here for now." id introduction_shoma_cb321dde
    sh "Maybe I'll see you around." id introduction_shoma_f4226804

    hide shoma

    "With that, he ushers me out of the room. He wanders off with a heavy step."
    "I should get going too."

    return

label introduction_setsuna:

    scene backgroundgym

    "My footsteps squeak as the smell of floor polish and vinyl hits me in the face."
    "It must have been built recently for the place to be so clean."
    "I had heard there was supposed to be a pool here, but this is clearly a basketball court."

    n "Well, this is disappointing."

    show setsuna
    with dissolve

    s "The gym or being at school?" id introduction_setsuna_b17f2392

    "What the- where did that come from?"

    show setsuna apathetic

    s "...You weren't talking to me, were you?" id introduction_setsuna_1392a81d

    n "I didn't realize you were here, sorry."

    show setsuna relaxed

    s "It happens all the time, don't sweat it." id introduction_setsuna_c98d9250

    "She smiles with such ease. I can't help but feel a little jealous."

    show setsuna laugh

    s "The name's Setsuna Hori. I won't be offended if you forget it." id introduction_setsuna_df884504

    n "That's highly unlikely. I can't forget anything, eidetic memory."
    
    show setsuna scoff

    s "Is that what you go by?" id introduction_setsuna_c5fd9c04

    n "No, I'm Nagen."

    "She hums, deep in thought as she messes with the face of her watch."

    s "I guess it's only fair to tell you my Proficiency." id introduction_setsuna_5acc0d47

    show setsuna sad talk

    s "I'm told I'm basically invisible; people don't notice me or remember me as much as other people." id introduction_setsuna_ed3ae321
    
    show setsuna relaxed
    
    s "I prefer the term Social Chameleon, but the bow-ties in charge of labels don't want to change my status without a retest." id introduction_setsuna_af73c080

    "A Charisma major that specializes in being unnoticed, how odd."

    show setsuna apathetic

    s "Having the wrong label has its perks though." id introduction_setsuna_f7553491
    s "As long as I act like I belong, I can go pretty much anywhere I want." id introduction_setsuna_cf956e5d
    s "Which is good, since I never get invited anyway." id introduction_setsuna_9ba59a2d

    "She laughs at her own joke."

    s "I don't know what you expected to find here that's got you so down. It's just a gym." id introduction_setsuna_8776b906

    hide setsuna

    menu:

        "My friends":

            $ sRep += 1

            show setsuna shocked

            s "You know other people that go here?" id introduction_setsuna_d47ceeca
            s "Lucky you, I feel like a fish out of water. It's like everyone here grew up together or something." id introduction_setsuna_16d4a06c

            n "If they're from Estella, they may have."
            n "It depends on what class they were in. Some of the courses were highly insulated."

            show setsuna mourning
            
            s "Shoot, that'll make things extra hard." id introduction_setsuna_90ada1fd

            n "Make what extra hard?"

            s "Meeting everyone. Ever try introducing yourself while people are talking to their friends?" id introduction_setsuna_5212e78d
            s "It's like shoving your leg in a closing elevator." id introduction_setsuna_82825813
            s "People just stare and you have, like, half a second to make a good impression before they hit close again." id introduction_setsuna_41a529e8
            
            show setsuna apathetic
            
            s "It's going to be a lot of that or go back to my corner being ignored." id introduction_setsuna_717ed53f

            "She shudders."

            n "Well you've already met me, so if you run into someone, you can always open with that."

            s "Thanks. I'll keep that in mind, but I'm really trying to stand on my own." id introduction_setsuna_7c284de4

        "The pool":

            $ Charm += 1

            show setsuna scoff

            "She pounds on the gym floor, it sounds... hollow?"

            s "I don't think there'll be any free swim days for a while. Huge bummer, I miss having an indoor pool." id introduction_setsuna_60e0d67a

            n "So the pool's under the court?"

            s "There's a concrete bucket below the gym, but I doubt it has any water in it." id introduction_setsuna_92cd939e
            s "This place is trying so hard to look competent, but in the end, it's not much better than outside." id introduction_setsuna_1fcd7ccd

            n "It's better at being impractical."

            show setsuna laugh
            
            "That got her to laugh."

            s "I guess that's true, but there's potential at least." id introduction_setsuna_bf50726a
            s "You'd be surprised how many people can't even manage that." id introduction_setsuna_65da2d2a

        "Something interesting":

            $ sRep -= 1

            show setsuna glare

            s "Sorry to disappoint you then." id introduction_setsuna_bcdea01d

            "I wasn't talking about her, so why's she taking it personally?"
            "There are a million other things I could have said that would be worse."
            "Ugh, but the way she keeps glaring at me..."

            show setsuna sad talk

            s "By all means, feel free to object at any time." id introduction_setsuna_6cba11ff

            n "You're the one that chose to self-deprecate. It's not my job to boost your self-esteem."

            s "I can see why you've been wandering around by yourself all this time." id introduction_setsuna_4261af60

            n "Hey, I have friends, they're just not here right now."

            s "Hmm..." id introduction_setsuna_b3b9c0e8

            "I can't tell if she doesn't believe me or just doesn't care. Either way, it pisses me off."

    show setsuna

    play audio "274806__barkerspinhead__alarm-timer-watch-countdown(edit).ogg"

    "A high pitched alarm rings from her wristwatch."

    show setsuna impatient

    s "Well, that was painful." id introduction_setsuna_a53f4166

    "She immediately turns to leave."

    n "Wait, what's going on?"

    show setsuna glare

    s "I've met my bare minimum for giving a shit and this conversation is clearly going nowhere." id introduction_setsuna_146f7b1a
    s "You're not nearly as interesting as I hoped, so I'm leaving." id introduction_setsuna_1b18000c
    
    show setsuna scoff
    
    s "Honestly, I don't understand why everyone's so worried that you're here." id introduction_setsuna_a390a47b
    s "Outshining you will be a cakewalk." id introduction_setsuna_45cb5fa1

    "Does this person crave attention so much she sees rumors as competition or... she couldn't be a copycat, could she?"

    n "What do you mean? Who have you been talking to?"

    s "Of course that's what you'd say. It doesn't matter and I didn't sneak in here to walk you through my thoughts." id introduction_setsuna_98ed47f3

    n "Wait, are you even supposed to be at this school?"

    show setsuna glare

    s "I meant the gym, moron. It's off-limits to students without a teacher present." id introduction_setsuna_4fefe81e

    n "I knew that!"

    show setsuna impatient

    s "Sure you did." id introduction_setsuna_dfaa5d87

    show setsuna relaxed

    s "Welp, I got more important stuff to do. If you ever decide to do anything entertaining, by all means, find me." id introduction_setsuna_363d019c

    hide setsuna

    "I chase after her, but by the time I get outside, she's nowhere to be found."

    return

label introduction_kietsu:

    "I follow a dirt path that branches off to the right of the school's entrance."
    "It wraps around to a brick storage shed. Inside is a café lined with wall to wall bookshelves."
    "Looks like any furniture that doesn't have a complete set gets stored here."
    "A heavenly aroma of breakfast wafts through the air."
    "At one of the tables, a kid in trashed clothes is sitting with his head in his arms, muttering something to himself."

    show kietsu sad

    n "...Um... You okay, dude?"

    "I nudge the leg of his chair with my foot and he jumps up with a start."

    show kietsu confused

    ki "Hunh!? Oh, sorry, didja want to sit here or somethin'?" id introduction_kietsu_68e4049a

    "There's a whole room of empty chairs. Why would I want to take the one he was sitting in?"

    n "I was just making sure you're okay."

    show kietsu sympathetic

    ki "Thanks man. I've been better, but y'know, who hasn't?" id introduction_kietsu_904a7913

    show kietsu

    ki "At least this place has cheese curds, y'want a cheese curd?" id introduction_kietsu_15d9f788

    "I can't resist the call of free food. I join him at his table."
    "It seems like the first thing he did when he got here was figure out where to eat."
    "A big plate of fried appetizers is set between us."

    show kietsu dontworry

    ki "You can tell a lot about a place by the food they serve their people." id introduction_kietsu_da9d77ff

    show kietsu upset1

    ki "Crap food means you'll get treated like crap." id introduction_kietsu_27f7965d

    n "You've been to a school like this before?"

    show kietsu dontworry

    ki "Like this? Nah. I've been in n' out of a couple... ah, what do they call 'em?" id introduction_kietsu_84052b18
    ki "'Guided Learning Programs'. I've been to a bunch of those." id introduction_kietsu_857b4776

    "Camps designed to stop kids from developing 'unnatural' abilities that could label them as a Vision major."
    "Some of those places could be downright criminal, and none of them worked. I didn't know they were still around."

    n "I can't believe your parents would do that to you."

    show kietsu mischievious

    ki "My parents...? Nah, I signed myself up." id introduction_kietsu_2a36a73d

    n "You can do that? Why would you do that?"

    show kietsu sympathetic

    ki "Thought it'd work better than choking on sage and makin' my mom cry. I even tried bootcamp." id introduction_kietsu_e71e086f
    ki "It was actually really cool, but..." id introduction_kietsu_539ede58

    show kietsu cringe

    "He trails off. With his sunglasses, it's hard to tell if he's looking at me or totally zoning out."
    "I check behind me, just to be sure, but we're the only people in the lobby."
    "I wave at him to get his attention."

    show kietsu confused

    ki "Sorry, what was I talkin' about?" id introduction_kietsu_203efd31

    hide kietsu

    menu:
        "What's wrong with you?":

            $ kiRep -= 1

            show kietsu serious

            ki "That's a loaded question." id introduction_kietsu_e36b3265

            "He drums on the table with his knuckles."

            show kietsu concerned

            ki "See, we just met, so I don't know what you think 'right' is." id introduction_kietsu_d2a4a31a
            ki "Conversations like this are just for you to figure out how similar I am to you when you've already decided we're nothin' alike." id introduction_kietsu_ad299552

            "He rubs his temples."

            show kietsu surprised

            ki "Why. Why would you ask that? Did I do something upsettin' if y'think..." id introduction_kietsu_156a78de
            ki "You a Vision major, or do you hate 'em?" id introduction_kietsu_c2d70ed9

            n "You just kept trailing off and forgetting what you were saying."

            show kietsu upset2

            ki "That's normal." id introduction_kietsu_3741e200

            n "No dude, it's not."

            show kietsu upset1 surprised

            ki "It's normal for me. Are you one of those people who like irritatin' people?" id introduction_kietsu_d068106d

            n "I-Uh."

            show kietsu serious

            ki "'Cause that was hella rude. What's wrong with you?" id introduction_kietsu_d2279c48

            n "I didn't mean it like that."

        "Your old school":

            $ kiRep += 1

            show kietsu sad talk

            ki "Right, well they said being a Vision major, I'm a Vision major, they said it made my case too complex." id introduction_kietsu_c16c76ce

            n "What does that mean?"

            show kietsu serious

            ki "I know, right? I was so pumped to have a goal other than 'stay out of trouble' too." id introduction_kietsu_7bc45814
            
            show kietsu sympathetic

            ki "Everythin' was super structured, it was kinda nice. I don't know what to do with myself now." id introduction_kietsu_05481597

            show kietsu sad

            "He's zoning out again, but I can tell he's still somewhat present."

            n "At least we have decent food."

            show kietsu

            ki "Oh yeah, and real plates too. They said we might be able to get music pumped in here after classes." id introduction_kietsu_21c7ce67

            "He seems genuinely happy to be here, and the food is good."

            show kietsu sympathetic

            ki "Thanks for sittin' with me by the way." id introduction_kietsu_6c8f2631

            n "Hunh? Oh, yeah, no problem."

            show kietsu upset1

            ki "It feels like everyone here already knows each other." id introduction_kietsu_9352c24b

            show kietsu sympathetic

            ki "It's hella uncomfortable, so it's cool to have someone who wants to talk to me." id introduction_kietsu_8d46d7b6

        "Eating sage?":

            $ Vision += 1

            show kietsu cringe

            ki "I mean, you can, but I don't see why you'd want to eat that stuff plain." id introduction_kietsu_8b83b948

            n "You said you choked on sage?"

            show kietsu laugh

            ki "Sage smoke, man, not a plate of it. You burn sage to ward off evil spirits." id introduction_kietsu_98f74a78
            ki "Not the nicest way to wake up in the mornin'." id introduction_kietsu_24c1c4f5

            "He laughs."

            n "How does that work? Do they not like the smell of it or something? Can spirits even smell?"

            show kietsu mischievious

            ki "Hunh... Never thought about it like that before, I guess they don't." id introduction_kietsu_78bb588c

            show kietsu sad talk

            ki "You'd hate the smell of it too if someone shoved ten smudge sticks in your face." id introduction_kietsu_119fcc2c

            show kietsu laugh

            ki "Never had to eat it though." id introduction_kietsu_986a57c4

            n "I guess that makes more sense."

            show kietsu

            ki "Makes more sense than half the stuff you find online. At least it's harmless." id introduction_kietsu_e10859ec

    show kietsu surprised

    ki "Have you seen how big this place is?" id introduction_kietsu_e54687df

    show kietsu tease
    
    ki "When I heard only twenty-some kids would be here, I thought it was going to be super small." id introduction_kietsu_28cf60a9
    ki "No wonder the waitlist is so long." id introduction_kietsu_3955935c

    n "There's a waitlist to get in? Already?"

    show kietsu talk

    ki "Well, yeah, any place that takes teens gets packed right away." id introduction_kietsu_6ea4bb97
    ki "But the requirements here are really specific. I was lucky to get in." id introduction_kietsu_05c905c3

    "I wonder..."

    n "Did you get questioned by a red-headed lady in a bad pantsuit?"

    show kietsu cringe

    ki "Ahh... no. It was, umm... she had a scarf and really big earrings." id introduction_kietsu_12b4f023

    show kietsu

    ki "I ended up writing everything I could fit in the comment section of the application and it earned me a scholarship." id introduction_kietsu_93da5a9f

    show kietsu sad talk

    ki "The interview was hard, but I managed to get through it. Sounds like you got a mean one." id introduction_kietsu_79378098

    n "Yeah, a real piece of work."

    "Could it be? Did Vivaldi really meet this guy in person? Why?"

    n "But it's not like she's part of the faculty here, so I don't think we'll be seeing her."

    show kietsu

    ki "That's good. And hey, we get a huge place all to ourselves. No upperclassmen either." id introduction_kietsu_b4ff009d
    ki "We should make the most of this year." id introduction_kietsu_181ecc08

    n "Yeah, I guess so."

    show kietsu talk

    ki "I'm gonna go stretch my legs. Don't worry about the bill, my meal plan will cover it." id introduction_kietsu_152c7dab

    "There are only three cheese curds left. I barely had any. Where did they all go?"

    show kietsu dontworry

    ki "Oh, and thanks for checking on me. You'd be surprised how many people would have just walked away." id introduction_kietsu_54eb257a

    hide kietsu

    "He shoots a couple finger guns at me before walking away..."
    "The food's all gone. I should keep moving forward."

    return

label introduction_momoko:

    "As I make my way to the third floor, I hear a huge crash at the end of the hall."
    "The door to the school lab is slightly ajar. I rush in to see a girl with multicolored hair standing in the middle of the room"
    "Or, at least, standing as well as she can with rollerskates on. Are those even allowed?"

    n "What happened? Are you okay?"

    show momoko puzzled

    mh "Is one free outlet without a jenga tower in the way too much to ask for?" id introduction_momoko_7c1d2213

    "She's trying her best to close one of the cabinets."

    n "I guess not... but that noise-"

    mh "Noise? I didn't hear anything. Maybe you're hearing things, Nagen." id introduction_momoko_3533d61f

    "A foreboding clunk comes from behind the small wooden door as she backs away."

    show momoko surprised

    mh "Don't open that cabinet." id introduction_momoko_5bfe1b31

    n "How did you know my name? None of us have been here that long."

    "She starts laughing."

    show momoko worry

    mh "Decisions, decisions." id introduction_momoko_dd86e350
    mh "Do I pretend to be someone else and see how long it takes you to figure it out? Or do I tell you?" id introduction_momoko_edf87bf8

    "I honestly can't place her face to a name. Her voice is sort of familiar, but..."
    "She's still laughing at me."

    n "Is it really that funny?"

    show momoko happy

    mh "You took it so personally when I kept forgetting your name." id introduction_momoko_d81d5640
    mh "I had it written on my hand for at least a year before I got it down." id introduction_momoko_bd42deda
    
    show momoko puzzled
    
    mh "Maybe my forgetfulness is contagious?" id introduction_momoko_0eb77797

    "I still got nothing, but there's no way I'd forget someone's name."
    "She'd have to have gone to Estella. Was she in my class or the Intel course?"

    n "I'm so sorry, could you please just tell me your name?"
    
    show momoko talk1

    mh "Momoko Yoshino. My Proficiency is in Chemistry." id introduction_momoko_d95082db
    mh "We were in the same special classes and homeroom in Estella for four years. Ring any bells?" id introduction_momoko_925e58ed

    n "Momoko!?"

    hide momoko

    scene backgroundP4

    #[CG: Momoko as a younger kid]
    "She used to be the only one in class I was taller than."
    "She was this mousey wisp of a person who barely had the energy to present a school project."
    "It was like being in class with an asthmatic chihuahua."
    "There's no way I'd have recognized her without any help."
    #[Hide CG]

    scene backgroundlab

    menu:

        "What happened to you?":

            $ mhRep -= 1

            show momoko sad

            mh "Oh, well, I was messing around with some new hair dye formulas and it kinda nuked my eyebrows..." id introduction_momoko_897d16f6
            mh "And my lashes..." id introduction_momoko_bb0c6d32
            mh "And my bangs..." id introduction_momoko_c4d1731c
            mh "It exploded." id introduction_momoko_4e75cd10

            n "That isn't too surprising."
            n "But I meant all of this; the clothes, the bigness. You're so different."

            show momoko talk2

            mh "So? No one wanted me around before. At least now I think I'm fun, the rest should follow after." id introduction_momoko_4d3edc04

            n "The rest of what?"

            show momoko talk1

            mh "Rebellion!" id introduction_momoko_7cd3e4c3
            mh "After spending months in boardrooms talking with boring grown-ups, I got so frustrated trying to make those jerks happy that I decided to stop caring what anyone thinks." id introduction_momoko_b9282e8f

            mh "They can do whatever they want with my old invention." id introduction_momoko_59e827b6
            mh "But while I'm here, everything I make is going to be for me." id introduction_momoko_36be7c64

            "So this is her idea of what teenage rebellion looks like?"

            show momoko angry

            mh "Now I'm all feisty. Begone, frown wrinkles, begone!" id introduction_momoko_e51bc48a
            
            show momoko

            mh "Today is supposed to be a good day, for we have science. Unsupervised science." id introduction_momoko_dc0335b3

            n "...We always have science."

        "You look happy":

            $ mhRep += 1

            show momoko

            mh "For the first time in a long time, I feel like things are going to get better." id introduction_momoko_4889dcf5
            mh "I got that vibe, y'know. Don't you?" id introduction_momoko_f8706590

            n "I think you're one of the few."

            show momoko angry

            mh "Aww, don't go bummering all over my parade because you're jealous I'm thriving." id introduction_momoko_f61427c2

            n "I'm not jealous. You're jealous."

            show momoko happy

            mh "D'aw, cheer up Nagen, it'll be okay. I mean, you're still an Intel major, yeah?" id introduction_momoko_c87ea72d

            n "Well, yeah..."

            show momoko talk1

            mh "Then that's one more reason to smile." id introduction_momoko_51a676f2
            mh "We'll get to be in the same classes again! Come on dude, get on this level." id introduction_momoko_59eabddc

            n "Yeah, I suppose that's true."

            "She gives me a huge, cheesy grin and I can't help smiling too."

        "Mad scientist":

            $ Intel += 1

            show momoko manic

            mh "Now don't go saying that, you'll make people think I'm irresponsible or something." id introduction_momoko_b7fddcce

            n "You're on wheels near a tower of glass."

            show momoko talk1

            mh "It's not like I'm zipping around in Jams." id introduction_momoko_cd322034
            mh "They're quads, baby skates, I'm safer in these than on solid ground; trust me." id introduction_momoko_9be6cada
            
            show momoko puzzled
            
            mh "Do I really give off crazy vibes?" id introduction_momoko_d570b30f

            n "No... but you have been known to be a bit of a pyromaniac."

            show momoko sad talk

            mh "Fire likes me, not the other way around. Besides, I've been trying to break up with combustibles." id introduction_momoko_629fd271
            mh "Even contained explosions are too much stress right now." id introduction_momoko_f07d2d7c

            "That's a surprise. She was always so enchanted with fireworks and the like."
            "I can't imagine her doing anything else."
    
    show momoko talk1

    mh "I think we all can use a break from everything going on outside." id introduction_momoko_369d290b
    mh "It's best to think of this as a free vacation." id introduction_momoko_b50ebd58

    n "It's hard for me to see how school and vacation fit in the same circle."

    show momoko sad talk

    mh "Really? I thought you loved school." id introduction_momoko_481b7653
    mh "You were always so competitive about grades and you ran all those clubs. You practically lived there." id introduction_momoko_940e5e5e

    "She shakes her head."

    show momoko talk2

    mh "Eh, who am I to judge? I didn't have much of a life before either." id introduction_momoko_062f8cc0

    n "Why are you here so early anyways? It's not like we have class yet or anything."

    mh "I'm looking for a place to put a stereo. If this is going to be my workshop, I'm going to need music." id introduction_momoko_078added

    n "Workshop? You're going to start making stuff here?"

    show momoko puzzled

    mh "See, that look of panic is not what I'm going for." id introduction_momoko_78c897cd
    mh "I know I've got a bit of a destructive streak to make up for, but I swear I've changed." id introduction_momoko_37202708
    mh "I want to make nice things, the kinds of stuff that makes people happy." id introduction_momoko_ce87fb65

    n "You don't mean-"

    show momoko happy

    mh "Cosmetics!" id introduction_momoko_dd84552f

    n "Umm..."

    show momoko talk2

    mh "I've already started trying to make my own hair dye with... mixed results." id introduction_momoko_48a25585
    mh "But there's still more things to try. It'll be like putting a spa in a bottle, doesn't that sound like fun?" id introduction_momoko_2133ed79

    n "I'm sure someone will like it."

    show momoko

    mh "I still gotta assert my dominance and claim this lab as my own, but once I do, you'll know." id introduction_momoko_b1e03f8a

    "I'm concerned."
    "Despite her good intentions, Momoko hasn't had the best track record with hazardous chemicals and staying on task."
    "I've turned in more than my fair share of charred paperwork as her lab partner."

    mh "You should come by some time and try my stuff!" id introduction_momoko_751ecec8
    
    n "I don't know..."

    show momoko talk1

    mh "Why not? There's nothing more manly than taking care of yourself." id introduction_momoko_8c53c8fd

    n "That's not the issue."

    mh "Do you have any weird allergies or something?" id introduction_momoko_8f5b0fd7

    n "Eggs."
    
    "And explosions."

    show momoko happy
    
    mh "Then it shouldn't be a problem, right? Oh, and if there's anything specific you want, just let me know." id introduction_momoko_1fa76a6c

    n "Yeah, just, don't spend all your time cooped up in here."
    n "I mean, what's the point of making people happy if you never see it?"

    "Just please, for everyone's safety, fixate on something else."
    
    hide momoko

    return

label introduction_rei:

    "The classrooms are filled with wall to wall shelves of books."
    "The main floor has been tidied up to make room for the rows of antique tables."
    "At the back of the room is a hologram projection of a blackboard with a welcome message hastily scribbled on it."
    "This place feels less like a classroom and more like a lecture hall. In the center row, a girl sits quietly crying."

    n "Hey, are you okay?"

    show rei disappointed

    re "Oh Nagen, it's just awful, they took everything away! I totally forgot I had them with me until the alarms went off." id introduction_rei_533bfa6c
    re "I told them I wasn't going to stab anyone. I swear, I wasn't going to stab anyone!" id introduction_rei_785bf24c
    re "But they took them all anyway: Rainbow Bright, Hog Cleaver, even Obsidian Snowflake!" id introduction_rei_c275e2c7

    n "Woah, woah, slow down. What are you talking about?"

    show rei sad talk

    re "The swords! All of my sister's swords, what did you think I was talking about?" id introduction_rei_2ee91b9d

    "Her sister's swords? I only know one person whose family heirlooms are weapons."

    n "I don't know, Rei, maybe you were listing Warrior Pony OCs."

    show rei disappointed

    re "I'm such an idiot. I got so used to carrying them around in the riots." id introduction_rei_9251059e

    "She's always had issues with time."
    "Her poor grades were the only reason she ended up in the 'At Risk' class. It's a shame, really."
    "Her skills as a dancer and color guard member would have made her somewhat popular if she hadn't been lumped in with us."
    "I respect that she never blamed her classmates for the crummy treatment she received."
    "It would have been really easy to throw us under the bus to save her reputation."

    hide rei

    menu:

        "Your sister's gonna kill you":

            $ reRep += 1

            show rei irate

            re "I know... Ugh, I should have gotten a storage locker or something. My poor babies." id introduction_rei_97470f80

            n "It's okay, I'm sure they just locked them up. There aren't too many safe places to dispose of swords right now."

            show rei optimistic

            re "Right, you're right! I'll get them back eventually." id introduction_rei_c4765718
            re "For now, I'll just settle for plastic props. They're a shame compared to her craftsmanship." id introduction_rei_deb643fa
            
            n "I'd like to see them sometime."

            show rei talk1

            re "I'm more of an artillery gal myself, but even I could see the beauty in her armory." id introduction_rei_96c868ac
            re "You'll definitely have to come by this summer and see 'em." id introduction_rei_6c5ab826

        "Aren't they heavy?":

            $ reRep -= 1

            show rei disappointed

            n "How could you forget you were carrying those things?"

            re "Nagen, honey, use critical thinking. I have endless endurance." id introduction_rei_958eb52e
            re "Just because they were heavy doesn't mean it bothered me to carry them." id introduction_rei_c62f0be1
            re "I just got used to having them on me. I don't know how else to explain it." id introduction_rei_4c1242b0

            n "How many were there?"

            show rei talk2

            re "About eight. Any more than that and I wouldn't be able to move." id introduction_rei_257b03b0

            n "You forgot you were carrying eight swords?"

            show rei talk1

            re "Yeah, and my fifteen knives, and my keys." id introduction_rei_d569eee4

            n "Your keys?"

            show rei brag

            re "The key chain was a brass knuckle kitty." id introduction_rei_3a0d1700
            re "I couldn't get the keys off because they were welded to the head like whiskers." id introduction_rei_0fae8233

            n "Unbelievable."

            show rei depressed

            re "I already got three weeks probation, I don't need a lecture from you too." id introduction_rei_f8aa5d14

            "This girl walks into school with the iron throne strapped to her back and I'm the one on probation?"

        "You haven't changed":

            $ Vigor += 1

            show rei surprised

            re "In a good way, I hope." id introduction_rei_d0e9a9ee

            n "Why wouldn't it be in a good way?"

            show rei irate
            
            re "Well, I never was sure if you actually liked me." id introduction_rei_3729d1d9
            re "No one in our class wanted to be there. It always felt like everyone was just waiting to get out." id introduction_rei_6ba3dd73

            n "I mean, you're not wrong, but that doesn't mean I disliked you. I just had other things going on."

            show rei talk1

            re "That's good to hear." id introduction_rei_423e5a36

            n "Now that you've been caught bearing arms, you've really earned your title as a 'problem' child."

            re "You're the only ones who thought constantly forgetting homework wasn't a problem." id introduction_rei_9afa464d

    show rei smile talk

    re "I'm really glad you're here, Nagen." id introduction_rei_23c3ed3f
    re "I was starting to think that I'd have to go to this big ol' scary place by myself." id introduction_rei_1d0ae3a2

    n "I'm surprised you recognized me."

    show rei talk1

    re "So you finally got to pick your own clothes, big deal. You still sound the same as always." id introduction_rei_bbf0f1c4
    re "We were really worried about you when you disappeared during the riots." id introduction_rei_2ab495ca

    n "We?"

    show rei pout 

    re "...Our classmates." id introduction_rei_77a5acf6
    re "And the girls from the squad. We were doing a headcount at the refugee center and couldn't find you." id introduction_rei_60829a93

    "I honestly didn't think they'd notice I was gone."

    re "Promise you won't run off on your own like that again?" id introduction_rei_7a57d2e9

    n "Okay, mom."

    show rei irate

    re "I'm serious. We've got to look out for each other now more than ever." id introduction_rei_201dc5d7

    "Even though she has no idea what I'm going through, she's still trying to look out for me."

    n "Thanks Rei, I'll try my best."

    show rei surprised

    re "O-oh, there's no need to thank me..." id introduction_rei_a356d4a9

    n "The same goes for you though, you can't let your guard down here. It's not safe."

    show rei disappointed

    re "Nagen, I'm the one who accidentally brought weapons to the school." id introduction_rei_113ac048
    re "This place is supposed to protect us from the aftermath of the riots. They want to help us." id introduction_rei_98229b67

    "So that's what they've been telling everybody else."
    "It's a shame. As sweet as Rei is, she's too trusting."

    show rei talk1

    re "This is going to be a fresh start for us, you'll see." id introduction_rei_6497dd3f

    hide rei
    
    return

label introduction_rise:

    play music "music/TriumphantReturn.mp3"

    "There's only a few rooms open on the top floor."
    "This appears to be a meeting place of some sort, but it's glaringly apparent that everything in the room has never been used."
    "Every piece of furniture clashes despite the effort to match colors."
    "By the large bay window sits a poised girl with a tea set."
    "Rise Kisaki, her Proficiency is Allure, which I never fully understood."
    "According to Uitto, it means she's a people magnet, like a lot of Charisma majors."
    "With me being in the “bad kids” class, I never really talked to her."
    "Her far off stare reminds me of a china doll. Across from her is an empty cup and chair."

    n "I'm sorry, were you waiting for someone?"

    "She perks up at the sound of my voice with slow, deliberate blinks."

    show rise smile

    r "Yes, though high tea is an activity that can be enjoyed by anyone. Please, have a seat." id introduction_rise_6486e804

    hide rise

    menu:
        "Sit":

            $ rRep += 1

            show rise

            n "Are you sure?"

            r "I can always make another cup." id introduction_rise_7ad174a6
            r "Besides, meeting others on neutral ground is the best way to make new friends." id introduction_rise_2136341c

            "She says this, yet there's no denying who's in control as she pours me a cup."

            n "This just looks like water..."

            show rise talk

            r "It is for now. I would not want to accidentally poison a stranger through social convention by serving the wrong tea." id introduction_rise_84d9330d
            r "Now let us see if I have anything you would like." id introduction_rise_fe32bf83

            "She pulls out a handful of packages and arranges them neatly on a dish, studying me with care."

            r "Choose whatever you would like." id introduction_rise_fa871d43

            hide rise

            menu:
                "Golden Tip":

                    $ Charm += 1

                    show rise smug

                    r "It tastes best without milk, I should know." id introduction_rise_20f5ed90

                    "She takes a sip from her own cup. That must be what she's drinking right now"

                    n "You have multiple bags of $200 tea?"

                    show rise flirt

                    r "Is that why you chose it? And here I thought you were aiming for the health benefits." id introduction_rise_5d08be09
                    r "It is supposed to help with anxiety." id introduction_rise_e409f36d

                    n "Not going to argue it's 'not that expensive'?"

                    show rise frown

                    r "I would not know, I did not buy them." id introduction_rise_e1691c7c

                    "She gently caresses the gold rim of her teacup. It looks pretty old."

                    n "It might be a while until you can get more. Are you sure I can have this?"

                    show rise

                    r "By all means; you are curious and I already offered it to you, regardless of its worth." id introduction_rise_676a60ff
                    r "It will be ready in about five minutes." id introduction_rise_12ff8218

                    n "If you drink this a bunch, does that mean you're an anxious person?"

                    show rise frown

                    r "...I have been favoring it recently. But everyone has been seeking comfort more as of late, correct?" id introduction_rise_25e4bef8

                    n "I guess."

                "Spark Matcha":

                    $ Vigor += 1

                    show rise smile

                    r "Are you feeling tired?" id introduction_rise_9c69b1e7

                    n "Like you wouldn't believe. It's been a long couple of months and the drive over here sucked."

                    r "You would not rather go rest?" id introduction_rise_bfdfd938

                    n "I can't, I still have things I need to do today."

                    show rise frown

                    r "Before school begins? That must be stressful." id introduction_rise_5c6ca19c

                    n "Yeah. The school's so big and all the construction is making it hard to get around."

                    show rise flirt

                    r "Your motivation is admirable." id introduction_rise_9099ac9b
                    r "Merely setting foot on campus felt like a chore to me, even though this is an area I should thrive in." id introduction_rise_ad9ad4f1
                    r "Where do you find the drive?" id introduction_rise_8ff15b16

                    n "I've spent the last few months with no internet and barely two people to talk to."

                    show rise smug

                    r "So the facility itself is the obstacle?" id introduction_rise_2c63c660
                    r "Well, that certainly explains a lot, but you should not put too much pressure on yourself." id introduction_rise_37f37735
                    r "I am sure they will take roll tomorrow and you will have your answer then regardless." id introduction_rise_7b280cd3
                    r "It certainly would be more efficient." id introduction_rise_ad2dd6b3

                    n "No good. If I don't try my hardest, it will just keep me up all night."

                "Earl Gray":

                    $ Intel += 1

                    show rise talk

                    n "You'll have to forgive me if I'm a little shaky on the proper etiquette, but that's the one I can put milk in, right?"

                    r "I suppose if you would like to practice for afternoon tea then yes, milk and sugar are reserved for black teas." id introduction_rise_be8056e0
                    r "But I am well aware my definition of polite behavior differs greatly from those here, so please do not be afraid to act as you normally would." id introduction_rise_08dac3d5

                    n "Thanks."

                    "She says that, but I feel like she's watching my every move. Too bad there's no food."

                    show rise flirt

                    r "You must be new at this if you have to think so much about drinking tea." id introduction_rise_7fcad997
                    r "A true blue blood has such notions drilled into them since birth." id introduction_rise_b0fa0ac0

                    n "The lessons I took this year weren't my idea. This will probably be the only time I'll use them."

                    r "What makes you so sure?" id introduction_rise_ff7e98a2

                    n "I don't think the people who taught me plan on keeping me around after graduation."

                    show rise smug

                    r "It is a shame when you do not feel like you belong." id introduction_rise_eaf7b800
                    
        "Decline":

            $ rRep -= 1

            show rise frown

            n "Sorry, not a big tea fan."

            r "How unfortunate." id introduction_rise_265be803
            r "In that case, this room is reserved. I trust you do not need me to show you the way out." id introduction_rise_ffabbdb5

            "There's no reason for me to stay here. I turn and leave."
    
    show rise talk
    
    r "Perhaps I could help you find who you have been looking for?" id introduction_rise_3381271c

    n "I never said I was looking for anyone specific."

    r "My apologies, I made an assumption based on your behavior earlier. Was I mistaken?" id introduction_rise_0aebe957

    "There's a glimmer in her eye as she speaks."

    n "Not exactly. I'm looking for some old friends of mine."
    n "I appreciate your offer to help, but there'd be no way to contact each other. Someone like you wouldn't want my number."

    show rise disappointed

    r "What gave you that idea?" id introduction_rise_da5678c5
    r "Nagen, this may be overstepping my bounds, but I do not think your group is worth this much of your time." id introduction_rise_f3718cee
    r "All they ever did was get you into trouble." id introduction_rise_619e6486
    r "There are plenty of people here who would make more supportive friends." id introduction_rise_978d9e5d

    "She's acting like she's helping me, but that's clearly an insult towards my friends."

    n "You don't know what you're talking about."

    show rise frown

    r "I have been mistaken before." id introduction_rise_117bc451
    r "I just worry that you have been exploited by individuals that do not value your personal achievements." id introduction_rise_f13ce59d

    n "And you do?"

    show rise flirt

    r "I could, though I am not in the best position to impose myself on anyone at the moment." id introduction_rise_99399ed1
    r "Given enough time, I could compose a detailed list of potential matches that would be mutually beneficial." id introduction_rise_10515077

    n "Not interested."

    show rise smug

    r "Suit yourself." id introduction_rise_3af91ee2

    "She smiles pleasantly as if nothing's wrong."
    "Though I suppose for her, there isn't anything wrong with what she said."
    "I can't take the silence."

    n "Thanks for the tea, but I need to go."

    show rise smile

    r "Anytime, Nagen. I do hope our next meeting will be pleasant." id introduction_rise_d694373d

    hide rise

    "I turn and leave."

    return

label introduction_dyre:

    "At the end of the first-floor hallway is a solid metal door with 'Computer Lab' written on it."
    "I can't get it to open, no matter how hard I try."
    "It's not like I need a computer that bad, but I had hoped maybe they had access to the internet."

    show dyre

    d "Tesuta, is that really you? What are the odds I'd find you here? I thought you were too smart for computers." id introduction_dyre_d42db12c

    "Of all the people to run into, why'd it have to be him?"

    n "Hello, Dyre."

    show dyre concerned

    d "Now, is that any way to treat an old friend?" id introduction_dyre_8cb3c637

    "When we were younger, we hung around each other all the time, until one of his pranks landed us both in deep shit."
    "I got expelled to the 'bad kids' class after that; he got a slap on the wrist."
    "Being the principal's grandson had its perks for him."
    "We stopped talking after that."

    n "I said hello, didn't I? I don't know what you expected, opening with backhanded compliments and shit."

    show dyre smirk

    "He smiles at me like the cat that got the canary."

    d "Would it really kill you to give people the benefit of doubt? I just wanted to talk." id introduction_dyre_3ea6ec2d
    d "After the riots, we didn't exactly get a list of survivors, no one knew where you went." id introduction_dyre_9fc7a615
    
    n "Well considering I ran away from home before the riots, I don't find your 'sympathy' terribly inspiring."
    
    show dyre talk1
    
    d "...We just thought you were out sick. You ran away? Shit, man." id introduction_dyre_bc4f52cc

    hide dyre

    menu:

        "Who told you I was sick?":

            $ dRep += 1

            show dyre sad talk

            d "I mean, you called out sick all the time." id introduction_dyre_cc43c825

            n "Yeah, but do you remember if anyone specifically said I called out?"

            "I ran away right after lunch to avoid my parents."
            "It wouldn't be unheard of for me to get pulled out of school in the middle of the day, but I wonder..."

            show dyre talk1

            d "Now that you mention it, Professor Kataki was the one who told us." id introduction_dyre_2824e767

            "That's weird, why would a homeroom teacher from another class be spreading rumors about someone else's students?"

            d "We were wondering why a whole bunch of kids didn't show up, and he said they got strep." id introduction_dyre_f34ee8a4
            d "Next thing I know, the whole school's getting evacuated, teachers started going MIA, and kids were disappearing left and right." id introduction_dyre_36533ca4
            d "It was like something out of a horror movie." id introduction_dyre_3a0c88f2

            n "I can't believe they lied about what was going on."

            show dyre scowl

            d "Does that mean you're going to tell me the truth instead?" id introduction_dyre_5e0cd0a3

            n "Hunh?"

            d "I keep asking you direct questions about that night, and you keep deflecting. Are you going to tell me what actually happened?" id introduction_dyre_44dbaf48
            
            n "It's like I said, I ran away."

        "Yeah, sorry":
            $ Charm += 1

            show dyre sad talk

            d "What are you apologizing to me for? I don't care where you live, as long as you're okay." id introduction_dyre_4ebe7b01
            d "There's a lot of weirdos out there that'd try to take advantage of a kid like you." id introduction_dyre_f57aedd7

            n "We're the same age!"

            show dyre talk2

            d "Yeah, that's how I know." id introduction_dyre_ae93f3c7
            d "You got talked into all kinds of stuff when we were younger and you still won't let it go." id introduction_dyre_a20d2fe9

            n "I... I let some stuff go."

            show dyre smirk

            d "Oh really?" id introduction_dyre_28c8abc7
            d "Well then, what about when you swore up and down that cow's milk stole calcium from your bones because you read it in some paper." id introduction_dyre_d4882dc9

            n "I did, and it wasn't just 'some paper', it was written by a doctor."

            d "Yeah, with a PhD in Fine Arts." id introduction_dyre_e0680ef1

            n "I was hoping you'd forget that part."

            show dyre smile talk

            d "Hah! No way." id introduction_dyre_596f70bc
            d "But that's totally my point, you get all worked up and you don't take time to see the other side." id introduction_dyre_68ffeb0e
            d "It makes it way too easy to mess with you." id introduction_dyre_30379c8b

            n "You could just, not do that."

            "He was the one who showed me that paper in the first place."

            show dyre smirk

            d "Stop? Where's the fun in that?" id introduction_dyre_34209eac

            "I should have known better than to talk to him."

        "Of course":

            $ dRep -= 1

            show dyre disturbed

            n "My helicopter parents never gave me a moment to myself."
            n "Then you got me thrown in my mom's class and suddenly I was under surveillance 24/7."

            d "How the hell is that my fault?" id introduction_dyre_e5b58c11
            d "I'm not the one that threw a tantrum up in the principal's office. That was all you." id introduction_dyre_39231fb5

            n "It wasn't- For the last time, a panic attack isn't something anyone chooses to have."

            show dyre mad

            d "Do you have any idea how long she waited for you during the evacuation?" id introduction_dyre_f67c98b7
            d "I know Dr. Tesuta wasn't exactly the nicest teacher, but she refused to leave the shelter without you." id introduction_dyre_de41f2af
            d "Some kid's parents never showed up." id introduction_dyre_eec3d0e1

            "Of course he doesn't get it. Even if I agreed with him, he'd just flip sides and argue the opposite."

            n "I couldn't stay there any longer. That place was killing me."

            show dyre talk2

            d "Well, at least everything turned out okay for you." id introduction_dyre_ca70ebb8
    
    show dyre talk1

    d "It's kind of odd this place is locked up, don't you think?" id introduction_dyre_bc2f7901
    d "All the major renovations were finished up to the fourth floor." id introduction_dyre_10e64a33

    n "Computers are expensive. It makes sense a teacher has to be in the room when we use them."

    d "That's the rationalization you're going with? Boring." id introduction_dyre_ea414212

    n "Reality usually is."

    show dyre tease

    d "Come on. In this huge, old building, you don't think there's a bit of history to it?" id introduction_dyre_74d9d722
    d "Something that would make this place more affordable for a school to set up shop in?" id introduction_dyre_b7047fac

    n "I don't like where this is going."

    d "It's totally a murder basement. It's right where the stairs would be if there was a lower level." id introduction_dyre_c1f693f8
    d "I heard the psychic girl's afraid to use her powers here because of all the angry spirits hanging around." id introduction_dyre_dacd3455

    #[Noise cue, hum/wind]

    show dyre smirk

    d "Yeah, it's haunted as fuck. Ten bucks says they never let us in there this year." id introduction_dyre_3b1f3da0

    n "Like you have ten dollars."

    #[Noise cue, distorted computer cry, soft]

    show dyre tease

    d "I will soon." id introduction_dyre_daae27a5

    n "Knock it off, this isn't funny."

    d "I didn't do anything, something inside did. Something they don't want us to see." id introduction_dyre_fb29e857
    d "You got to admit, they aren't being terribly honest with us." id introduction_dyre_dfe624bb

    "I'm not going to fall for this. I know they're lying about the Junior Gladiators, that my friends and I are here."
    "There's probably other stuff about the DVP they're covering up too."
    "He's just... trying to get under my skin and get me to say something I shouldn't."
    "I mean, there's no way this place is actually haunted, right?"

    #[Noise cue, distorted computer cry, loud]

    n "Y-you're an asshole. It's too early in the year for this man."

    show dyre talk2

    d "Fine, don't believe me." id introduction_dyre_9634f7d1

    hide dyre

    "He wanders off, waving goodbye over his shoulder as he goes."
    "I really don't want to stick around, not that I believed a word he said. I should look elsewhere."

    return

label introduction_jona:

    play music "music/SpeedWins.mp3"

    "I follow a paved walkway behind the field to a sparsely wooded area."
    "Hidden behind rows of planters is a small concrete stage."
    "It looks like it hasn't been long since the poppies were watered. The earth smells damp and cool."

    show jona relaxed

    j "....."

    "Someone's staring at me. They aren't coming any closer, but they aren't looking away either."
    "With all the junk covering their face, it's impossible to tell what they're thinking."

    j "....."

    "Creepy."

    j "....."

    n "If you have something to say, spit it out already."

    j "...I knew it." id introduction_jona_d0b8cb38

    n "Uhh... What?"

    j "You're the only one I've seen with that hue of magenta, but I wasn't sure." id introduction_jona_59d8db55
    j "Nothing's more awkward than walking up to someone thinking you know them when you really don't." id introduction_jona_d27843a1

    n "...Right..."

    show jona frustrated

    j "Nagen, it's me, Jona." id introduction_jona_03b5fa7a

    "That makes more sense. Jona was the most withdrawn and awkward member of our gang."
    "Looks like he covered himself head to toe the moment he got a chance. That explains why he's so calm right now."

    n "You certainly got your hands on a lot of... accessories since we last talked."

    show jona relaxed

    j "I made them myself! Well, I can't sew or blow glass, but you get the idea." id introduction_jona_cfcb6083

    n "Does the gas mask work?"

    j "...What do you mean 'does it work'?" id introduction_jona_6f31c8b1

    "Jona has a habit of repurposing things for art without knowing what they are."
    "He had tried inventing things, but always valued aesthetics over functionality."

    j "I haven't passed out yet, so I think it's bearable." id introduction_jona_d94c7834
    j "Why? Do you think it looks weird? Like, you'd cross the street to avoid me kinda weird?" id introduction_jona_9b5a8cbf

    "There's one right answer."

    n "Yeah, kinda."

    show jona happy

    j "Then it's kinda working!" id introduction_jona_f2599125
    j "I'm glad you're here. I was starting to think I'd have to track everyone down myself." id introduction_jona_6645c400

    n "You know we're not supposed to do that, right?"

    j "Since when have we listened to what they say? I mean, you're doing the same thing aren't you?" id introduction_jona_093396f9
    j "Of course, you are! ...but wait, if you didn't recognize me, why'd you walk up to me?" id introduction_jona_300ef636

    hide jona

    menu:

        "Opposites attract":

            $ Vision += 1

            n "Ah, well, I haven't seen anyone who's dressed in full counter-culture around here."
            n "I mean, steampunk is definitely more mainstream, but still..."
            n "Yeah, it's uh, it's neat. The wordless staring you were doing, not so much."

            show jona relaxed

            j "Aw shoot, you're making me blush." id introduction_jona_0d55c412

            n "....."

            j "Please, I didn't mean to interrupt. It's nice not to be the one monologuing for once." id introduction_jona_18c8a3f3

            n "I-I don't know man, don't put me on the spot like that!"

            j "Are you flustered?" id introduction_jona_9af85d90

            n "N-no."

            j "Really? But you're stuttering and your face is changing colors." id introduction_jona_9382612a
            j "Hiro said that happens when you're flustered." id introduction_jona_407517a0

            n "You caught me off guard is all. Hiro doesn't know what he's talking about."

            j "Oh. Well, I shouldn't be too surprised, he's been wrong about a lot of things before." id introduction_jona_3de05203
            j "I'm still upset there are no strawberry milk cows. The chocolate cows must be lonely." id introduction_jona_9f653081

            "Just let it go, Nagen. You don't want to go down that road again."

        "To start a fight":

            $ jRep += 1
            
            show jona frustrated

            j "!!!"
            j "Why!?" id introduction_jona_f7d540bd

            n "You kept staring at me. I figured you were trying to start something."

            j "I'm not big into social clubs, actually." id introduction_jona_16b6d7e5

            n "What? ...no, I meant- Nevermind."
            n "You just can't stare at people non-stop like that. People'll get the wrong idea."

            show jona relaxed

            j "I was just drawing." id introduction_jona_54f55163

            n "Drawing? Like, drawing me, or..."

            j "Not important. Just cause my goggles face somewhere doesn't mean I'm looking there." id introduction_jona_ecc57f51
            j "In fact, I haven't looked at you the whole time we've been talking. They're really handy." id introduction_jona_d70f7cef

            "Somehow, that's more unsettling."

            j "I wish I had the self-confidence to assume people were paying attention to me like other people do." id introduction_jona_2352a86e
            j "Well, actually, that would be more self-conscious than self-confident, wouldn't it?" id introduction_jona_855eec4d

            "I know he's not talking about me when he goes off on tangents like this."

            j "Maybe if you stop acting as if you cared, you'd be more self-confident... or conceited..." id introduction_jona_3d843e06

            show jona frustrated

            j "Or is it conceited to assume people are looking at you at all?" id introduction_jona_131feb6e
            j "I forgot where I was going with this." id introduction_jona_b9fcf224

            n "I'm not sure either."

            j "Oh, right! I was trying to match your 'playful' banter. I've been practicing." id introduction_jona_1cb06bb0

            n "Well you succeeded in confusing both of us."

            j "Sorry. I'll try better next time." id introduction_jona_c36387b5

            n "You really don't have to."

        "Look for an exit":

            $ jRep -= 1

            n "You're the one who walked up to me."

            "I rarely hung out with Jona one on one. For one, this is the kid that carved up desks for fun."
            "The other was, well, he reminds me of my mom for some reason..."

            show jona relaxed

            j "I suppose I did talk to you first. Are the others here?" id introduction_jona_fc3abf15

            n "I don't know, that's why I'm looking around."

            j "We could do it together! I have logs on Uitto and Hiro's daily routines." id introduction_jona_7f225a4b
            j "Oh, but, you've already got those memorized, don't you?" id introduction_jona_501e1777

            n "...Yeah... I totally know those things..."
            n "Haven't ever listed them out in a planner though. Because, uh, that would be kinda weird."

            "He tries to hide the notebooks in his bag."

            show jona frustrated

            j "Bad weird or good weird?" id introduction_jona_2583833c

            n "I didn't mean either. Weird is just an adjective."

            j "People always say that, but they mean 'good' weird or 'bad' weird." id introduction_jona_fe8c9b94

            n "Aahhh... Good weird! I meant good weird."

            show jona happy

            j "...Hunh. Well, you gotta show me your class schedule so I can update your book. My JG logs are pretty dated." id introduction_jona_41bc41b8

            n "We're not in the Junior Gladiators anymore. You don't need to keep logs on everyone."

            j "...But I like knowing everyone's schedule." id introduction_jona_7fd8996e

            "This is just one of those things I have to let go of, I think."

            n "Okay, but don't tell anyone outside of the group that you're doing that."
            n "We might get in trouble for resuming club activities if they know."

            j "Okay!" id introduction_jona_66075dd7

    n "Anyway, I'm getting everyone to meet in room 313 at four."

    show jona happy

    j "Everyone, everyone!?" id introduction_jona_641ef28b

    n "Yeah. But, uh, you can't come with me, we'll stick out too much walking around together." 
    n "It's gotta be a secret meeting."

    j "...I'll be there." id introduction_jona_f7fc0e3d
    
    n "Great, talk to you then."

    j "....."

    hide jona
    
    return

label Meeting:

    play music "music/Unconditionally.mp3"

    scene backgroundstuco

    "I walk into the room to find Hiro and Jona waiting for me. Uitto comes in silently behind me."
    "The last time we were all together, it was to tell everyone that Lethe had passed."

    show jona relaxed at center

    j "So, who's leading the meeting?" id Meeting_49dffaa5

    show hiro judge at left

    h "Whaddya mean?" id Meeting_779e2ad5

    j "Well, usually Odori tells us what to do, but I don't see her here." id Meeting_1f8c8f9d
    j "I haven't seen her since she called for a cease-fire. Hiro, you were supposed to be guarding the base, where-" id Meeting_a402d956

    show hiro sad talk

    h "So Nagen, what's the plan?" id Meeting_aa0b0848

    show jona mad

    j "Why are you avoiding the question?" id Meeting_a6c28f10

    show hiro grumpy

    n "Focus guys, both of you. I never 'said' anything about a plan."

    show hiro mad

    h "So you wanted to hold a meeting and there isn't even a plan?" id Meeting_1dd01f51

    show jona frustrated

    j "I am so confused." id Meeting_e02373fe

    n "Guys, I know you're wondering why I called you here."

    show uitto yell at right

    u "Just spit it out, Nagen. You knew I was here, I'm sure the same went for the others too." id Meeting_3540bba3
    u "So, where the hell's Odori? Did she just not make the cut or did she stop participating in life too?" id Meeting_65f57b05

    h "Uitto!" id Meeting_b7170505

    show jona relaxed

    j "Well, Nagen, do you know what happened to her?" id Meeting_49a17005

    n "She's... still missing. No one's found her."

    "Hiro doesn't look surprised, but he's definitely avoiding Jona's almost accusatory turn towards him."
    "It's hard to tell with the goggles. Uitto keeps glaring at me."

    show uitto sad talk

    u "That's what I thought..." id Meeting_149037a5
    u "So, when are you going to beg for our forgiveness? Or are you going to keep acting like {i}you're{/i} not the one who sold us out?" id Meeting_a67ec8d4

    show uitto sad
    show jona depressed
    show hiro guilty

    n "What are you talking about?"

    show uitto yell

    u "I'm talking about how, despite pleading not-guilty, I ended up in reform school!" id Meeting_79462cb8
    u "You're the one that knew we'd all be here, so you have to be in their pockets!" id Meeting_cb4f5779

    show uitto sad
    show hiro mad

    h "Quit calling him manipulative! Not everyone is good at talking people into believing lies like you." id Meeting_8f3bf317
    
    show hiro guilty

    h "We should just be happy we're together again..." id Meeting_6a5c847c

    show jona mad

    j "Of course you would say that, you coward. If it were up to you, we'd be groveling on our bellies years ago." id Meeting_9449a401

    n "Now hold on..."

    show hiro grumpy

    h "You're one to talk! They were asking me about the doomsday cult we supposedly started." id Meeting_fdce35d4

    show hiro wait

    h "I wonder who's pet project that could have been?" id Meeting_dadf64aa

    show hiro mad

    h "Your stupid stories probably got us into more trouble than we should have been in." id Meeting_bf3bed2c
    h "And you're running around the school looking like a freaking serial killer! Are you trying to get us targeted!?" id Meeting_eda0737a

    show jona frustrated

    j "Steampunk is art! Quit acting like my art is hurting people." id Meeting_40e18be5

    show jona mad
    show hiro sulk

    j "You're the one that left Odori alone with people on our tail!" id Meeting_85b6c596

    n "Guys! Look, I know things aren't ideal right now, but that's why I called you here."
    n "We got separated on purpose, and all of us were forced to do things we didn't want to do to get by."
    n "But we're together now, and we need to figure out what to do next."

    show uitto serious

    u "Oh really, and why should we listen to you? You sold us out to the DVP!" id Meeting_fad6313f

    n "I never-"

    show uitto yell

    u "The agent they sent to get me mentioned you by name!" id Meeting_d2d68b8f
    u "I bet they gave you an offer you couldn't refuse or some cliche that makes you feel {i}better{/i} about leaving us to the wolves..." id Meeting_5161129d

    show uitto sad

    u "What else could you want from us?" id Meeting_ebdb651d

    n "Look, I'm sorry, really I am. But the DVP interrogated us separately for this very reason."
    n "They wanted us to turn on each other and make their boarding school look good."
    n "They're afraid of what we accomplish when we work together."

    show jona depressed

    j "Well, yeah. A faceless organization is ten times scarier than a handful of teens." id Meeting_65315517

    show hiro mad fine

    h "I'd have to disagree. Faceless organizations don't punch you in the junk in the middle of the night." id Meeting_09b7445f

    n "What!?"

    show hiro grumpy

    h "My foster brother's an asshole."

    show uitto serious

    u "...Right. So, you were saying..." id Meeting_b6607f25

    n "If we work together, all of us can get the hell out of here, for good."
    n "It's going to be lame, but if we can play the part for a year and play it well, they've got nothing on us."
    n "We make them think we're model students and we gain support from the students here to prove our innocence."

    j "How's that any different from what they told us to do?" id Meeting_f7634d66

    n "Because the whole student body will be in the palm of our hands and they'll be none the wiser."
    n "I'm going to take control of whatever passes for a student council and... well that's all I got for now."

    show hiro empty

    h "...Cool..." id Meeting_fe13c284

    n "And in the end, we'll get a lighter sentence and still get to be heroes."

    show hiro

    h "Yes! Good! I like this plan!" id Meeting_5e07b6d3

    show jona happy

    j "That isn't exactly a plan, but it doesn't sound like it'll get us in trouble..." id Meeting_84650ae5

    show uitto

    u "So, we get stuck here for a year, make nice and live happily ever after?" id Meeting_b2c5b9ef

    n "Pretty much."

    u "Not interested." id Meeting_885d089a

    show jona frustrated

    j "What are you talking about?" id Meeting_2093e331

    show uitto talk

    u "You all can act like the last few years didn't happen and live in a fantasy world, but I'm not interested in lying to the randos at this school." id Meeting_afe13a4b

    show uitto cringe

    u "I'm a wanted criminal, I ruined people's lives, and no amount of crocodile tears will make that okay." id Meeting_b926e838

    show uitto sad talk

    u "Of course, the people I hurt deserved it, but I'm not a helpless victim anymore. It's not fair to the other kids..." id Meeting_6c97a54b

    n "Then why plead not guilty if you're so honest?"

    show uitto sad

    u "Some of us actually want a normal adult to say we were right instead of begging for probation." id Meeting_bdc7a83d

    show hiro sad talk

    h "Come on, guys, arguing will get us nowhere." id Meeting_f89720a4

    show uitto sad talk

    u "I'll see you later, Hiro... maybe. I shouldn't be here..." id Meeting_6b90333f

    show jona frustrated
    hide uitto

    j "Uitto, wait!" id Meeting_8cbca8b5

    "She leaves without another word."

    hide jona
    hide hiro

    menu:
        "Forget her":

            $ uRep -= 1
            $ jRep -= 1

            show hiro guilty at left_center
            show jona relaxed at right_center

            n "Who needs her anyways? It's not like she ever did anything important."

            h "Come on man, I know you're pissed-" id Meeting_fc657c07

            n "No, she wants to throw her little diva tantrum, that's fine."

            j "Doesn't her ditching throw off your master plan?" id Meeting_9b40fba1

            n "Every experiment has an outlier. As long as the majority of the school believes us, nothing will change."

            hide jona
            hide hiro

        "She'll come around":

            $ jRep += 1
            $ hRep += 1

            n "She just needs some time to get over it. She will get over it, won't she?"

            show hiro guilty at left_center
            show jona depressed at right_center

            h "Ehh... hard to say." id Meeting_780c2a83
            h "She still refuses to watch Avenger League ever since it took the time slot of her favorite show." id Meeting_b46e4eea

            n "Empire of the Lost did not deserve to be canceled and I support her decision."
            n "But this is something entirely different. This is about our lives."
            n "She could end up with a life sentence. She knows that, right?"

            j "I don't know. She didn't look mad at us, not enough to hold a grudge." id Meeting_87d19213
            j "I don't care what her aura looked like to you." id Meeting_1b6dcf5c
            j "Nagen's right, she's not going to hold a grudge over this forever. We just have to wait." id Meeting_bc54b7f4

            hide jona
            hide hiro

        "Go after her":

            play music "music/CoolNights.mp3"

            $ uRep += 1

            n "Uitto, wait!"

            scene backgroundhall1 #Not sure if this is the right one

            "Has she been crying?"

            show uitto sad

            u "What?" id Meeting_ef2f1671

            n "What happened to you?"

            u "Excuse me?" id Meeting_d7ad3a0a

            n "You're angry, I get that, but is this really all about me?"

            u "I... I don't... Seeing everyone again..." id Meeting_b3b658a7
            u "Now isn't a good time, I'll just seem emotional and stupid. I need to clear my head." id Meeting_87696e5b

            n "Okay. If there's anything I can do-"

            show uitto embarrassed

            u "You'll try and fix it, I know." id Meeting_2a9ce046

            show uitto cringe

            u "This is just a little too much right now. I'll see you later." id Meeting_97009cb6

            hide uitto

            "So she isn't actually mad at me. I guess that's good, but I'm still worried."
    
    label meet_main:

        play music "music/Undertow.mp3"
        
        "I managed to get the guys to agree to join me. They may question my methods, but at least they're on board."
        "As for Uitto... I know we're all upset getting shoved into reform school, but it didn't seem like she had a better idea than mine."
        "I can't postpone returning to my dorm any longer."

        scene backgroundroomn
        with Fade(0.5, 1.0, 0.5)

        "Part of my aversion comes from how barren and sterile the rooms are."
        "I'd compare this place to a prison, but at least prisons are fully indoors."
        "I guess public opinion on Proficiency-centered education is dwindling because we're all having to stay in musty portable buildings."
        "I hope it's well-ventilated. I cringe to think of how hot this place could get in the summer."
        "I don't have the energy to unpack yet. I shrug out off my jacket and collapse on the bare mattress."
        "As I drift off to sleep, I desperately try to convince myself everything will work out in the end."

        if Vision >= 4:
            
            scene backgroundclass

            show yaguchi at right

            ya "So, what's the plan?"

            show sato annoyed at left

            sa "Darling, this was the plan."

            show vivaldi

            v "For now, we will proceed as originally intended. This just means we'll have to devote more energy to security."

            hide yaguchi
            show yaguchi frown at right

            ya "With what time?"

            hide sato annoyed
            show sato dissatisfaction at left

            sa "The four of us are burnt out as it is. We need manpower. If you would just let me call a few people..."

            hide ViBase
            show inukai concerned

            ik "Man, hearing you guys bicker like this really reminds me of the old days."
            ik "Still..."

            hide inukai concerned
            hide yaguchi frown
            hide sato dissatisfaction

            #CG note

            g "Dear Fallen Heroes,"
            g "I have reason to believe you are making use of revealing information deemed inaccurate and unfounded in nature."
            g "It is required that you cease and desist the following; holding registered Proficiency Users against their will, utilizing Proficiency-based education for personal benefit."
            g "If you fail to comply within fourteen days, I will have no choice but to pursue the matter personally."
            g "Sincerely, Estella O'Laurel."

            #CG teachers

            show inukai concerned

            ik "This is a little too eloquent for a student to be responsible, don't you think Viv?"

            show VFrown at left

            v "We can't exclude any possibility at this point."

            show yaguchi frown at right

            ya "For your sake, I hope it's some dumb kid."

            hide inukai concerned
            hide yaguchi frown
            hide VFrown

            return
        else:
            return