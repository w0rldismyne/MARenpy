label chapter_two:

    # Intro
    $ current_chapter = c_chapter_two

    $ set_profile_availability("chisei", c_i_profile_available)
    $ set_profile_availability("dyre", c_i_profile_available)
    $ set_profile_availability("ichita", c_i_profile_available)
    $ set_profile_availability("kazz", c_i_profile_available)
    $ set_profile_availability("kietsu", c_i_profile_available)
    $ set_profile_availability("kitsune", c_i_profile_available)
    $ set_profile_availability("mariko", c_i_profile_hidden)
    $ set_profile_availability("momoko", c_i_profile_available)
    $ set_profile_availability("nanase", c_i_profile_available)
    $ set_profile_availability("mu", c_i_profile_available)
    $ set_profile_availability("rei", c_i_profile_available)
    $ set_profile_availability("rise", c_i_profile_available)
    $ set_profile_availability("setsuna", c_i_profile_available)
    $ set_profile_availability("shoma", c_i_profile_available)
    $ set_profile_availability("taiga", c_i_profile_available)
    $ set_profile_availability("yoku", c_i_profile_available)

    call chapter2_day1_event1

    call chapter2_classes

    call chapter2_day1_event2

    call freetime

    call chapter2_day1_event3

    call freetime

    call chapter2_day1_night

    call chapter2_day2_event1

    call freetime

    call chapter2_day2_event2

    call freetime

    call chapter2_day2_event3

    call freetime

    call chapter2_day2_event4

    call freetime

    call chapter2_day2_night

    call chapter2_day3_event1

    call freetime

    call chapter2_day3_event2

    call freetime

    call chapter2_day3_event3

    call freetime

    call chapter2_day3_event4

    call freetime

    call chapter2_day3_night

    call chapter2_day4_event1

    call freetime

    call chapter2_day4_event2

    call freetime

    call chapter2_day4_event3

    call freetime

    call chapter2_day4_night

    call chapter2_day5_event1

    call freetime

    call chapter2_day5_event2

    call freetime

    call chapter2_day5_event3

    call freetime

    call chapter2_day5_event4

    call freetime

    call chapter2_day5_night

    call chapter2_day6_event1

    call freetime

    call chapter2_day6_event2

    call freetime

    call chapter2_day6_night

    call chapter2_day7_event1

    call freetime

    call chapter2_day7_event2

    call freetime

    call chapter2_day7_event3

    call freetime

    call chapter2_day7_event4

    call freetime

    call chapter2_day7_night

    call chapter2_day8_event1

    call freetime

    call chapter2_day8_event2

    # Chapter 3
    return

label investigation_good_end_Ch2:
    scene backgrounddoor

    "Detention."
    "I've managed to avoid it so far, but it's kind of weird the staff hasn't officially told us about it."
    "Something behind the door chirps and lets me in."

    scene backgrounddetention
    menu:
        "Mariko":
            $mRep += 1
            "Mariko's looking a lot better. She has a stack of books we've been reading together on the bedside table next to her."
            "It looks like she's finally allowed to stand without Chiriyo yelling at her, though her ankle is still casted up."
            m "God, we need to get a bell on you or something. It's way too easy to get snuck up on in here." 
            "An impressive feat considering one of her walls is a glass window."
            if Rei_note = True:
                n "I brought you something."
                "I unfold the note and hold it up to the glass. She squints a bit, reading it over."
                m "Oh my God." 
                "I go to fold it up."
                m "What? No, let me read it again!"
                "She reads it at least three times before allowing me to fold up. A delighted shriek echoes from her cell."
                ci "Mariko! I told you, you can't do routines yet with your broken leg-"
                ci "Oh!"
                ci "You're smiling, that's good, but I thought you were hurt." 
                m "I have a girlfriend! Oh my God, I have a girlfriend!" 
                n "Yeah, you need to get your ass out of here so I can stop being your mailman. I know the shi-"
                "The AI glares at me."
                n "I know the stuff you have to do here really sucks, but there's someone outside waiting for you to get better so you can do gay stuff."
                m "You have no idea how hard it is not to jump around right now."
                "She sighs."
                m "Thank you. Thank you so much."
            else:
                m "I really appreciate you coming to visit me all the time. You really don't have to do that." 
                n "We're friends, aren't we?"
                m "Yeah, yeah we are." 
                n "What's the first thing you want to do when you get out of here?"
                m "Go to the pond. I heard there were little fishes in it, but I'm pretty sure they're tadpoles."
                m "There should be cute little frogs hopping around by the time I'm out." 
                "That's a good couple weeks from now."
                n "You like frogs?"
                m "You don't? The squishy lil guys, they're adorable."
                m "I know we're not allowed to have any pets on campus, but we can at least act like the animals in the area are pets."
                n "We'll do a little frog hunting, I guess. I'll find some glass jars to hold them in."
                m "Don't forget to poke holes in the jar."
                "She laughs."
                m "I'mma burn this into your memory, Tesuta. Holes in the jar. Now, about that book you brought last week."
            "We chat a bit about the books we've read over the last week and plans for when she gets out of detention."
            "She's not sure the school will allow her back after she's stable."
            "After all, she did do a number on Hiro and scared the shit out of everyone else."
            "There's a good chance she'll be gone after this."
            m "Nagen, there won't be any way for me to contact anyone here after I get out."
            m "It's kind of silly, but I'm worried once they ship me off, people will forget about me."
            n "Well, you know I won't."
            m "Yeah, but you'll be hanging out with other people. You have your actual friends."
            m "People you wanted to be close to. After we get out of here, will we still be friends?"
            menu:
                "No":
                    m "I thought so."
                    m "Well, it's still nice to have someone to talk to."
                    m "I appreciate you being kind to me. Getting stuck down here really would have sucked without you."
                "Yes":
                    play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
                    m "Then I'll wait. Every time we're apart, I'll write a bunch of letters."
                    m "That way I won't forget anything I want to share with you. We've got different brains."
                    m "I don't want you ever thinking I stopped caring just because my memory's worse."
                    n "That really means a lot. You have no idea."
            m "Loyalty is pretty much the most important thing to me."
            m "The fact you've kept coming down here, even after I was such an ass..."
            m "I'll never forget it. No matter what happens, I'm in your corner."
            "I feel like I've made a friend for life."
            #[Mariko pathway end]
        "Rise":
            "Rise's room is significantly less sterile than the other rooms."
            "There are less cushy things, a tea table, and a radio next to her bed."
            "I guess they're less worried about her hurting herself."
            "What surprises me most is the bandages on her eyes, and how much weight she's seemed to gain overnight."
            "She must have been wearing a corset or something this whole time."
            n "Um..."
            "She tries to remain composed, but I can see her flinch."
            r "I was told we wouldn't have any visitors. This is a pleasant surprise."
            "Even the way she talks is slightly different. Is this even the same person?"
            r "I'm facing you, aren't I? I don't want to seem rude." 
            n "Yeah, I'm just a little shocked."
            r "I figure that down here, there isn't anyone to impress. Besides, what's the point in being uncomfortable? I can't enjoy what I look like. It's been a bit of an adjustment."
            "She closes a fluffy robe around her. I can only imagine how many layers she's used to wearing."
            n "What happened to your eyes?"
            #[If Bad Ending]
            r "Burned. They're not sure if I'll be able to see again."
            r "Even if they do heal, there's a chance I'll have to look around scars my whole life."
            r "I should have considered that before putting strange technology in my eyes, but it was so handy at the time that I could only think of it as a blessing." 
            #[If Good Ending]
            r "The surface of my eye got scratched."
            r "It'll heal, but anytime I so much as look the wrong direction it burns and I become a factory of tears and snot."
            r "So unsightly. The bandages are mostly to encourage me not to use them until they've found how to help me."
            r "There has to be eye drops or something, but everything's been in short supply."
            #[Return to Main Branch]
            "I guess it's a good thing I didn't put those contacts in my eyes."
            r "What brings you down here?" 
            n "I wanted to check on you. I found out everyone who gets in serious trouble ends up in the room below the computer lab."
            "I describe in as much detail as I can where she is, that Mariko is down here with her, and how the place reminds me of a hospital."
            "She seems to relax a bit."
            r "I don't suppose you could escort anyone else down here?"
            n "Who do you want to see?"
            r "Yoku... He's avoided me ever since we came here."
            r "I'm not sure what exactly I did, but I would like to apologize."
            r "It sounds like after all is said and done, I won't be allowed back amongst the other students."
            r "Serves me right for thinking I could have my cake and eat it too. They're bound to find out I don't have a real Proficiency."
            r "I won't have any benefits from my old life. I'll be like anybody else after this."
            n "Is there anything else I can bring you? Maybe something easier to sneak down here?"
            r "Hmm... careful giving me your undivided attention, Nagen. I could get used to it~"
            "She clears her throat."
            r "I'm not sure. Anything I can think of would require my eyes, and I've been expressly forbidden from using those."
            menu:
                "Something she can taste":
                    $ rRep -= 1
                    r "I have my tea. As comforting as they are, they're not the greatest of entertainment."
                "Something she can listen to":
                    $ rRep += 1
                    play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
                    r "You know, the radio I have is able to play cassette tapes."
                    r "If you were able to find any of those, I'd be intrigued. It'd be like little mystery gifts."
                "Something she could feel":
                    r "You can't come on the other side of the glass, I'm afraid."
                    n "Not what I had in mind!"
                    r "That's a shame."
                    "Even when hospitalized, she still manages to find the upper hand somehow."
            r "I wish I could give you a more substantial answer."
            r "I'm sure you've noticed with Mariko, but we're not allowed to fall out of line, even if we've lost."
            r "The leashes we attached ourselves to are short ones. I'm sure you remember what that was like."
            n "I guess."
            r "You only guess?" 
            "Her hand skirts around the table for her kettle to start a fresh cup brewing."
            r "Nagen, I'm curious how your mind works."
            r "I know you say you can remember everything, but that could mean a couple of different things."
            r "For instance, I can drink any tea on this table."
            "She squeezes each package before pulling one up."
            r "But I choose when."
            "She rips open the bag and smells it."
            r "And, if this hadn't been what I was looking for, I could put it back before allowing the leaves to hit the water."
            r "I know part of why I appear calm is that I'm choosing to drown out anything that would make me cry in front of you."
            n "I wish I could, but it's not like I get to choose how things happened. If I remember something, I remember something."
            n "I don't see what this has to do with why you can't tell me what Apex is planning or how she found us."
            r "I fear that reaction is what she was counting on. It can be hard to admit to ourselves when we've been taken advantage of."
            r "I would know."
            "She sighs."
            r "Should someone try and force you to face it before you're ready, don't push them away like I did."
            "Even through the bandages, I can feel her staring me down."
            n "Okay."
            "I came here to make sure she was doing okay. It's best not to upset her."
            r "Ms. Chiriyo, is there any way to serve him a cup?"
            ci "I'm sorry, only faculty can take things in and out of the room."
            #[If teacher = yes]
            n "I'll get it myself then."
            #[If teacher = no]
            r "Drat. It seems I'll be drinking two cups then."

    "I wrap up my visit. It's getting late and if I want to make it to class on time, I really should be going."
    ci "Nagen, thank you again for coming. It seems only fair that I warn you, but I'll be getting shut down for maintenance soon."
    n "What do you mean?"
    ci "It was my job to keep anything from the outside from getting into the school."
    ci "Somehow, a student was able to hack into the computer system, so my entire program may be compromised."
    ci "I'm sure the students will be frightened when there's a sudden change at the school, so please let them know everything will be alright."
    n "They're going to turn you back on, right?"
    ci "Someone will, at some point. I have no way of knowing when that will be. As soon as you can, I'd like to see you. The last time I was shut down, all my students changed so much, and I've yet to catch up."
    n "Of course I'll come."
    "It shouldn't take that long. After all, the program knows how to look sad if she wants to."
    "For it to keep smiling, that has to mean this is a routine maintenance kind of thing."
    ci "I'm so proud of how far everyone has come so far. I look forward to seeing you again soon."
    "There's an awful glitching sound as I leave. The door locks behind me. I'm not sure when I'll be allowed back in."
    pass
