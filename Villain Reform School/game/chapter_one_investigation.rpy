label investigation:
    #INVESTIGATION SCENES 
    #[These scenes can be played during freetime by selecting the character from the investigation menu.]
    #Clues from Ch1... 
        #CDs, Computer, Microphone, Announcement List
    #Clues to find in Investigation... 
        #Mysterious Noise, Prank, Brag, PA Access, ID Account, Second locker, Missing Phone, Alexa Commands (might replace with more ID Account), Baton Pass
    scene NagensRoom
    menu:
        "Ask For Help":
            call Ask_For_Help
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
        "Kietsu":
            call KietsuInv1
        "Next":
            call investigation2

label investigation2:

    menu:
        "Back":
            call investigation
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
        "Setsuna":
            call SetsunaInv1
        "Next":
            call investigation3

label investigation3:

    menu:
        "Back":
            call investigation2
        "Kitsune":
            call KitsuneInv1
        # Temporary "Pass"es added so it could run
        "Mu":
            call MuInv1
        "Kazz":
            pass
        "Mariko":
            pass

label Ask_For_Help:

    menu:
        "Back":
            call investigation
        "Uitto":
            call UittoInv1
        "Jona":
            call JonaInv1
        "Hiro":
            call HiroInv1


label YokuInv1:
    #Yoku Interrogation
    scene backgroundstage

    show sprite YBase

    y "Careful wh-where you step!"

    "I freeze, foot in the air, with the door to the stage half open."
    "The floor is littered from end to end with carefully overlapped pieces of sheet music."
    "I slowly open the door and find a safe place to stand."
    "Yoku is in the center of it, a little more disheveled than usual."

    n "Are you... okay?"

    y "I- Well, I guess it does look per-ertuburbing to an outsider."
    y "Th-there is a method to the madness, I assure you."

    n "I hope so. Is this all from the library?"

    y "It holds a sur-rprising wealth of reference material."

    n "Does the staff know you pulled out all these pages?"
    n "I'm pretty sure the collections are supposed to be 'intact' while we're here."

    y "....."
    y "They fell out."

    "I’m trying so hard to keep a straight face, but I think he can hear me stifling a laugh."

    y "Clearly you can see I'm preoccupied at the mo-oment. What did you want?"
label YokuChoice1:

    menu:
        "Alibi":
            y "That morning, I had to report to the classroom early to perform my duties as class representative."
            y "It ssseems I'm the only one that wants to come into class twenty minutes early."

            n "You got that right."

            y "Re-reguardless, that morning there was an alarm coming from one of the lockers on the second floor."
            y "It was from one of those dubstep/crunk songs that were everywhere befor-re the riots."
            y "Very irritating."
            y "I asked the council to take care of it. I haven't heard it since."

            "A ringtone maybe?"

            n "What are you doing exactly?"

            "He looks up unamused."

            y "Name on-ne person outside of this room that would have a use for sheet music."

            n "What about Kazz?"

            y "Ha! That wannabe disc jockey couldn't tell B major from G shhharp minor."

            n "...what's the difference?"

            y "There is none, he wouldn't know tha-at either. His idea of writing music is dragging and dr-ropping sound clips. Which is... fffine. I just doubt he'd use these over his machines."

            n "I suppose that's fair." #(+Mysterious noise)

            call YokuChoice1
        "Show Evidence":
                "I show Yoku a photo I took of the CDs"

                n "This is going to sound silly, but would you be able to look at this picture and tell me if there's anything special about how these CDs are organized?"

                y "No."

                n "I was afraid that was the case."

                y "There's no or-rder to them at all."
                y "Either that or they were arranged with person-nal taste in mind. Where did you take this picture?"

                n "The AV room."

                y "That's why. Kazz let his friends pick ou-ut what they wanted to hear before he star-rted accepting requests."
                y "One of the perks of bein-ng a DJ."
                y "It'll be June before I hear any cl-lassical music on the air."

                call YokuChoice1
        "Leave":
            call YokuOutro
label YokuOutro:

    n "Well, thank you for taking time out of... whatever this is to talk to me."

    y "....."

    n "Uh, bye, I guess."

    "I quickly close the door and hear the flutter of papers getting flung into the air."

    y "NOOOOO!"

    n "Sorry, I-"

    hide sprite YBase

    "Shit, I better get out of here."

    pass # Should call Ch1 equivilent of Freeday from the sandbox

label ReiInv1:
    scene backgroundamp

    #Rei Investigation
    #[BG: Amphitheater]

    "Rei might not want to talk to me, but if I want a clear picture, I need to talk to everyone."
    "I find Rei practicing her old floor routine on the outdoor stage."
    "She juggles her plastic sword mechanically, focusing on throwing it as high as she can."
    "Normally she moves with more grace and joy."

    n "Hey, can we talk?"

    "She catches her blade one last time, but refuses to look at me."

    show sprite ReBase

    re "Say whatever you want."

    "I think that's as close as I'll get to a yes."

    #-Negotiation-
    g "There will come times when people won't want to talk to you."
    g "You'll have one chance to convince them you're worth their time, though Charisma Majors may have more luck."
    
    #[Player Choice]
    #A. What's wrong?
label ReiChoice1:
    menu:
        "What's wrong?":
            n "You only practice like this when you're upset."

            re "Am I not allowed to be angry?"

            n "That's not what I said. I'm just concerned is all."

            re "Well, I'm glad when you see me face to face, I'm worthy of your concern."
            re "For a second there, I thought you'd become a total sociopath."

            n "Rei-"

            re "I don't even know how to fully process this, okay?"
            re "Just- I'm trying to be mature and not mean, but it's hard."
            re "I don't know if I should trust you again."
            re "I'll- I'll see you later."

            #(Fail, Rei’s scene is now locked)
            pass
        "I didn't know...":
    
            n "I never meant to hurt you or any of the other kids at school."
            n "I'm sorry things turned out like this."

            re "I just feel so stupid."
            re "We were all in the same class together for four years."
            re "It was like having a second family to me."
            re "I constantly worried about how we were going to stay together when we got older only to find you don't think about me at all."

            n "Rei, it's not like that-"

            re "It's not just you. No one here-"
            re "I think I'm the only one that thought we were all friends."

            "There are definitely people here I could have gone my whole life without seeing again."
            "I don't think there's anything I can say to make this right, but..."

            n "I wanted to keep everyone safe too."
            n "That's why I couldn't leave you behind."
            n "I really was relieved to see you again, even if you don't want to talk to me again."

            re "I don't want to be mad at you. I really don't."
            re "If we're going to stay friends, you can't hide stuff from me."
            re "You gotta show me the same trust I showed you."

            "I didn't realize how close Rei felt to everyone."
            "Maybe it wouldn't be so bad to have someone this loyal on my side."

            n "The truth is, I'm trying to find who spread the message over the PA system."
            n "If you have any ideas, it'd help me a lot."

            call ReiChoice2
label ReiChoice2:  
    menu:
        "Alibi":
    
            re "I've been mostly helping Mariko revive the cheer squad."
            re "We've been making posters, working on banners; we even got a spot on the announcements!"

            n "What about flag line? That's why you brought all your armaments, isn't it?"
            n "There isn't a lot of opportunity for you to dance if you’re a cheerleader."

            re "Most of my stuff's been confiscated."
            re "It'll take weeks to make decent prop replacements."
            re "Besides, cheer is more accessible to rookies than twirling."

            n "That sounds like Mariko talking, not you."

            re "She needs this more than I need flag line."
            re "Anything to make this place feel like a normal school, a place to make new friends, will help her."
            re "She's really starting to worry me."

            n "She doesn't seem that different to me."

            re "Ever since we got here, even before we found out there could only be three clubs, she's been pushing herself without rest to form the squad."
            re "I've never seen her fumble during a performance like she did during the opening ceremony."
            re "I'm pretty sure a fall like that shouldn't break your ankle, but it's still purple."
            re "She refused to suspend practice until she's recovered."
            re "It's like all the joy has been sucked out of her."
            re "Helping her with the squad feels like the only way I can help."

            "Rei would know best if Mariko's acting odd. Still, there's a high chance this is all coincidence."

            n "I'm sure she appreciates it."

            re "It's such a hopeless feeling watching her like this when I know something's wrong."
            re "I keep hoping she'll tell me what's really bothering her, but I'm not sure she knows how to."

            n "Don't forget to take care of yourself too."
            n "Coming here has been hard for everyone."
            #+ Cheer Ad

            call ReiChoice2
        "Show Evidence":
            menu:
                "Computer":
                    re "Kazz had one of those Echo thingies."
                    re "Wouldn't he be the one to look it up? They were both in his booth after all."

                    n "Kazz could have just logged into his account through the computer and programmed new commands through that, but this page is talking about how to use the app."
                    n "Plus, his phone was missing during that time. It's the only other way to program the thing."

                    re "Maybe someone was borrowing it from him."

                    n "Then they would have asked him first and he'd tell them how to use it..."

                    "Why is she acting so defensive?"

                    n "Rei, did someone tell you they were borrowing his stuff?"

                    re "They didn't have to. He made it perfectly clear that anyone could use his stuff whenever they wanted."

                    "But not without permission. Whoever it was, they must be close to Kazz and Rei." #(+Brag)
                    call ReiChoice2
                "Missing Phone":
                    re "Yeah, I've seen it."
                    re "But why? Kazz should have gotten it back by now."

                    n "Where did you find it?"

                    re "Kitsune brought it to practice looking for the owner."
                    re "Mariko recognized it right away and said she'd take it back to him."
                    re "Maybe she hasn't been able to track him down yet; he's been literally all over the place lately..."

                    "Still, it wouldn't be hard to leave a note on his dorm or something."

                    n "So you didn't see her give it to him?"

                    re "No. But I don't see why she'd lie to me."
                    re "Besides, the two of them are friends, sort of..."

                    "Even she doesn't seem totally convinced by that explanation." #(+Baton Pass)
                    call ReiChoice2
                "CDs":
    
                    re "Between everyone here, that's not a bad collection."
                    re "Too bad he's not accepting MP3s. I might have some old music on a thumb drive somewhere."

                    n "I didn't realize it was a community effort."

                    re "Oh yeah. Next semester, I'll be sure to bring a whole bunch of stuff."

                    call ReiChoice2
                "Announcement List":
    
                    re "We're dead last on the list? That doesn't seem right."

                    n "Spots were first come, first serve. Was Mariko in there before the other girls?"

                    re "Dyre had pulled her aside wanting to sneak something into the booth."
                    re "I had assumed that she dropped off the ad when she helped Dyre."
                    re "Maybe something came up?"
                    
                    n "At least you got in on time."

                    re "....."
                    re "Yeah."
                    
                    "She's really not happy about it though."
                    call ReiChoice2
        "Leave":
            call ReiOutro
label ReiOutro:      
    re "After all this drama, I don't think I'll sleep well tonight."

    n "Sleep? What's sleep?"

    re "Nothing too important, I'm sure."

    "To a Vigor Major like her, maybe it's not."

    re "But I should at least try and rest."

    "She hesitates and fumbles with her baton."

    re "You know, some of us like to hang out in the cafe at night."
    re "If you came alone, I don't think people would chase you away."

    n "Quite the compelling pitch you got there."

    re "I'm just saying, if you have the energy, maybe you should drop by."
    re "It could be a good way to make new friends."

    n "You're asking me to ignore curfew and participate in a ritual B and E? You really are a troublemaker, aren't you?"

    re "Greatest memory in the world and you always seem to forget that."
    re "Besides, there's no rule against going in at night, so technically, it's okay."
    re "It beats lying awake in the dorms, that's for sure."

    # Currently this portion of the game is now a stretch goal.
    #[IF Vigor < ?]
    #n "I guess that's true. I'll think about it."

    #[Else] 
    n "I'd like to, but I like to sleep more."

    "Vigor Majors can be almost inhuman sometimes."

    re "I'll see you around, Nagen."

    hide sprite ReBase
    pass #connect to loop here

label MomokoInv1:
    scene backgroundlab
    
    "Momoko's music is so loud I can hear it down the hall."
    "I peer in through the window to make sure she isn't handling any chemicals before opening the door."

    n "Momo?"

    "No good, she can't hear me."
    "I flick one of the light switches on and off."
    "She jumps, but the minute she sees me a huge smile spreads across her face."
    "I can see her lips moving, but all I hear is the music."

    n "Where's the stereo!? THE STEREO?"

    "Click."

    show sprite MhBase

    mh "-keep telling them it's not my fault; the sinks smelled when I got here."

    n "Glad to see you're not trying to avoid me."

    mh "Eh, what's the point when you could find me anyway?"
    mh "We're stuck in this fish bowl together for the next four years, why make enemies now?"

    n "...thanks."

    mh "You're welcome! Did you need something?"
label MomokoChoice1:
    menu:
        "Alibi":
            mh "The first day of school... I was here."
            mh "Every lab has a system for where things go."
            mh "Now it's my system and I plan to keep it that way."
            mh "All my time is in my log book."

            n "Anybody come by the lab?"

            mh "Kazz helped me set up the stereo. That was nice."
            mh "Especially since I could just give him my club ad in person."
            mh "The more I can avoid the stairs, the better."

            "Right, the skates. It's probably a pain to take them off every time she wants to go to a different floor."

            n "I take it you haven't gone to the third floor then."

            mh "There's nothing for me there."
            call MomokoChoice1
        "Show Evidence":
            "I show Momoko the computer."

            mh "Well, they certainly weren't shopping for an Alexa, no one's willing to drive this far for small deliveries."
            mh "Trust me, the next shipment of lighter fluid won't be here for two months."

            n "Then someone must have snuck one in from the outside."
            n "But how? I thought the teachers confiscated all tech when we got here."

            mh "It's a speaker with bluetooth. It's not that hard to cut it off from the internet."
            mh "Setsuna and Kazz have tried to get me to connect them to the internet multiple times."

            n "Really?"

            mh "Yeah, I'm like; hello, chemistry and technology are two different zones."
            mh "'Oh Momo, you're smart, you must know–' No! I only know chemicals."

            n "You think anyone else has one?"

            mh "Not likely. Or if they do, they're smart enough to actually hide it."
            mh "After this, we'll be lucky to keep our school phones."
            mh "It should show who's logged into it if you ask."#+ID Account

            call MomokoChoice1
        "Leave":
            call MomokoOutro
    #-Else-
    
    #mh "That doesn't sound out of place, Nagen. Sounds like you're over thinking things again."

    #n "There has to be something. I refuse to believe this is a 'perfect crime'."

    #-Outro-
label MomokoOutro: 
    n "...is that beaker supposed to be smoking?"

    mh "Spinach-laced-ridilin, turn off the lights!"

    "She grabs the beaker with a set of tongs and moves it toward the fume hood."

    mh "Not another one- Nagen, the lights!"

    "I plunge the room into darkness and the fire dissipates."

    mh "Now I have to start from scratch! ...maybe that's why the lashes were melting instead of gluing..."

    hide sprite MhBase

    "I should probably go."
    pass #connect to loop

label RiseInv1:
    scene backgroundcourtyard
    "I find Rise enjoying a cup of tea in the courtyard."

    show sprite RBase

    n "I hope I'm not interrupting."

    r "Perish the thought."
    r "Please, have a seat."
    r "There is something I would like to discuss with you."

    "How does she manage to flip the script so quickly?"

    r "If it is not too much trouble, could you do something about your little friend?"
    r "Ever since I became class representative, they have been disrupting class with their... jokes."

    "Uitto could care less about who was cleaning erasers and checking attendance logs."
    "However, she's not too keen on people telling her what to do."

    r "It is one thing to whine about my popularity giving me 'unfair' advantages, but it is another to bring my bust size into the conversation."
    r "That, and when we were voting for class president, she submitted a rather vulgar drawing of a... phallic-looking thing and asked me to 'suck it'."

    n "Just ignore her."

    r "This kind of behavior is unacceptable."
    r "Her actions reflect on you as well, seeing as you are still friends with her."

    n "I know, and I can apologize for her if that's what you want, but talking to her will just make it worse."
    n "Either go completely stone faced or get a teacher involved."
    n "I can't reign her in like I can with Hiro."

    r "I see... That is disappointing."
    r "Well then, I suppose that addresses my concerns, but I believe there was something you wished to discuss?"
label RiseChoice1:
    menu:
        "Alibi": 
            r "I overheard what happened during the announcement."
            r "How utterly mortifying it must have been to be thrust into the spotlight like that."

            n "I didn't ask how you felt about it, I asked if you had anything to do with it."

            r "Forgive me, I do not have an alibi."

            n "Ahah!"

            "She raises a solitary hand and waits for me to close my mouth."

            r "I cannot offer an alibi for a vague period of time when I am not even sure how it was done in the first place."
            r "Everyone was accounted for in my class up until the bell rang."
            r "I am certain that remains true for the other classes."

            n "Oh."

            r "I am sorry I cannot be of more help."
            r "If there is something more specific you would like to ask me about, I would love to help if possible."
        "Show Evidence":
            menu:
                "Announcement List":
                    r "I am not a club leader, so I do not have access to the recording booth."
                    r "I am only a class representitve, not a council member."

                    n "Know of anyone who'd have access in your class?"

                    r "Someone on the council might, but that is only speculation."
                    r "You may try asking Nanase or Setsuna if they have access."
                    r "No one in the Charm Department is a club leader, oddly enough."
                    r "Everyone seems content to wait until there are more students."

                    n "I see, thank you." #(+PA Access)
                    call RiseChoice1

                "Missing Phone":
                    r "We have hardly been here a week and people have already started stealing? How distasteful."

                    n "You haven't seen anything suspicious, have you?"

                    r "That odd girl Kitsune asked if I knew how to get into a phone that had been locked."
                    r "I assumed she just forgot her password, but none of my tricks seemed to work."
                    r "I did not know it was possible to have an alternate model, otherwise I would have demanded an upgrade myself."

                    n "You're positive it wasn't the school model she was running around with?"

                    r "Definitely, though she was unable to use it, so I doubt it did her much good."
                    r "I would be surprised if she held onto it."
                    call RiseChoice1
        "Leave":
            call RiseOutro
label RiseOutro:
    r "I am sorry I was not more helpful."
    r "I have not been around long enough to get a feel for how everyone gets along nowadays."
    r "We may have grown up with each other, but a lot can change in two years."

    n "You could help me talk to other people."

    r "And risk my position as neutral observer? I think not."
    r "There are too many unknown factors for me to go choosing sides just yet."
    r "Quite frankly, your reputation puts you at a disadvantage."
    r "Find me after the dust settles and ask who I would invest my time in and you might be pleased with the answer."

    "Is she... rooting for me?"
    "If so, she has a strange way of showing it."
    "She packs up her set into an old cigar box with a sigh."

    r "Do not be too disheartened, Nagen."
    r "I know you are smart enough to figure this out."

    hide sprite RBase

    "With that, she leaves."
    pass #connect to loop

label NanaseInv1:
    scene backgroundcafe
    "Nanase was more than happy to meet with me, but she told me she was working on something at the cafe."
    "I arrive to find various ingredients out, with tinny music playing from a burner phone."
    "Nanase is running around from table to book to fridge covered in what smells like cocoa powder."

    n "Wow, I didn't know we were allowed to use the kitchen."

    show sprite NBase

    nk "Eep! Gah, I mean, hi."
    nk "Yeah, you can use the cafe during off hours with instructor supervision."

    n "I don't see anyone here."

    "She points to a mounted security camera."

    nk "Mr. Yaguchi's watching from his office, so I don't 'burn the place down'."

    "Creepy. She’s about to dust herself off when she looks up."

    nk "Umm... You don't have any allergies, do you?"
    nk "I didn't think about that before inviting you over."

    n "Eggs and, uhh, maybe marshmallows."
    n "Although that might be because I tried to eat a whole bag in under a minute once."

    nk "Eggs?"

    "She looks over at a decimated carton on the far left table with obvious disappointment."

    n "I'll be fine as long as I don't eat them."

    nk "Right... Anyways, what did you want to talk about?"
label NanaseChoice1:
    menu:
        "Alibi":
            n "I don't remember seeing you during the broadcast. What were you doing?"

            nk "In the morning, before classes, we had our first council meeting."
            nk "That's when we heard sirens in the hallways."
            nk "It was so scary! The school was still empty at the time and all the teachers were preparing for first period, so it was just this ominous screeching in the dark hallways."
            nk "Eventually, we found it was coming from one of the lockers."

            n "I don't remember hearing anything during class."

            nk "Setsuna snuck out during first period after she got the locker combinations from Professor Inukai."
            nk "She thought it was odd for Mu to have such a noisy ringtone and turned it into the lost and found."
            nk "Though if it's from the outside, it might have been confiscated."

            n "Did you see her turn it in?"

            nk "Well... no. I stayed in class to cover for her."

            n "Does she have everyone's locker combinations or just Mu's?"

            nk "Everyone's... we couldn't tell who's locker it was from the outside, it wasn't decorated or anything." #(+Locker Combo)
            call NanaseChoice1
        "Show Evidence":
            "I showed her the announcement list"

            nk "Kietsu's the one who's been handling club requests."
            nk "Though it seems like he's approving anyone who applies."
            nk "I'm not even sure there's enough interest to maintain four clubs at this school."
            nk "We barely have enough for a functioning student council."

            n "You wouldn't happen to know who the club leaders are, would you?"

            nk "No, sorry."
            call NanaseChoice1
        "Leave":
            call NanaseOutro
    #-Other-
    
    #nk "Well, it isn't odd that those things would be in the PA room. I don't see anything... incriminating about it."

    #"She probably thinks I'm being paranoid."
label NanaseOutro:
    nk "Umm... are you doing okay? "

    n "Hunh?"

    nk "I mean, that message over the PA was really scary."
    nk "I can't imagine what it would feel like to get bullied the first day of school."

    n "It's... I've got things under control. It's fine. I'm surprised that you, you know, care?"

    nk "I'm not heartless. Besides, starting rumors anonymously over the air like that is so irresponsible."
    nk "I just want you to know not everyone here buys into that witch-hunt mentality."

    n "Uhh... thanks."

    nk "If there's anything else I can do to help you, just let me know."

    n "Sure."

    hide sprite NBase

    "It's so weird to think the announcement pissed off people who weren't even involved."
    "I wonder if there are others who felt threatened by it."
    pass #connect to loop

label KietsuInv1:
    scene backgroundstuco
    #Kietsu Investigation
    #[BG: Office]
    
    "I find Kietsu buried under a pile of paperwork."
    "Everything is sorted into color-coded piles, but chaotically so."
    "Every few seconds, he pauses to write something on a stray sticky note."

    show sprite KiBase

    n "Hey, do you have a minute?"

    "No response. He must really be in the zone."
    "I turn to leave, but opening the door catches his attention."

    ki "Sorry man, didn't mean to ignore you."
    ki "Have a seat."
    Ki "I need a break from this mess anyway."

    n "What is all this?"

    ki "...I'm not exactly sure."
    ki "Some of it's stuff to help the teachers, some of it's fundraisin’ ideas, some of it's random stuff we could do."
    ki "Nanase's the one who organized them for me, but then the piles hit the floor..."
    ki "It's gonna take a fortnight to sift through."
    ki "Anyway, what can I do for you?"
label KietsuChoice:
        menu:
            "Show Evidence":
                menu:
                    "Announcement List":
                        n "You were in charge of approving the club ads, weren't you?"

                        ki "Hmm... yeah, I guess I was."
                        ki "I didn't read any of them though."
                        ki "I figured if there was anything y'know, bad, Kazz would catch it before readin’ it."
                        ki "Anyone who wanted to run a club I let borrow the AV room key so they could drop off their ad."
                        ki "At least this way, everyone gets a fair shot at gatherin’ members to get their club approved by the teachers."

                        n "Wait, you just let anyone go in the AV room?"

                        ki "Only people who really wanted to get a club ad in before the first mornin’ announcements. Seriously, some kids are really intense when it comes to after school activities."

                        n "Who all did you give the key to?"

                        ki "Chisei, at like, 6AM. And then Mariko twenty minutes later. After that, Kazz took the key so he could go straight to the AV room after first period."

                        n "Was anyone else with them when they asked for the key?"

                        ki "Not that I could see."

                        "Kazz doesn't seem like the type to let people in."
                        "It might be a good idea to check with the others." #PAAccess = True

                        call KietsuChoice

                    "CDs":
                    #-Other-   
                        ki "It'd be weirder if that wasn't there, wouldn't it?"

                        n "I guess..."

                        ki "Kazz knows that booth better than me. If something went missin’, then he'd know."
                        call KietsuChoice
            "Alibi":
                n "What were you doing before the broadcast?"

                ki "Broadcast?"

                n "....."

                n "The broadcast; creepy robot voice saying the school is dangerous and my friends should get expelled. It went off after first period."

                ki "Is that what people are talkin’ about? I could barely hear it at the time. That really blows, man. No wonder you're freakin’ out."

                n "I- Umm... I wouldn't say I'm 'freaking out'. I'm just, really curious what people were up to before that happened."

                "There's really no way to question people about this without sounding paranoid as all get out. Doesn't seem to bother him much though."

                ki "I was in class... before that was the council meeting... nothing seemed out of the ordinary."

                n "What happened during the meeting?"

                ki "Setsuna rejected all my proposals and stormed off. Nanase went to follow her in a panic. It seems like that's normal for both of them though."

                n "I see."

                call KietsuChoice

            "Leave":

                call KietsuOutro
label KietsuOutro:
    #-Outro-
    ki "Sorry I can't help you out more, but if I want to be able to host any school events."
    ki "I need to have a fool-proof plan of attack against the penny-pinchin’ treasurer."
    ki "If anything’ about what happened makes it through the student council, I'll let you know."

    n "Thanks."

    ki "And Nagen?"

    n "Yeah?"

    ki "Don't let this whole thing dominate your head space."
    ki "If people find out one message is enough to send you in a tailspin, more people will try to use it to mess with you."
    ki "It can be really easy to let fear cloud your judgment."

    "For a second there, he sounded so grown up."
    "But just as quickly, his gaze wanders and he starts fretting over the disorganized piles on his desk."

    ki "Things will get easier once we get everythin’ under control."

    n "...we?"

    ki "Hnh? Oh yeah. You're the one who sent in a council application form, right?"
    ki "That means we could be workin’ together for the rest of the year."

    n "Yeah. That's true."

    "I guess they really do need all the help they can get."
    "Still, it's nice to know not everyone thinks I'm a monster on sight."

    n "I'll talk to you later."

    hide sprite KiBase

    "There's still more people I have to see."
    pass # Should call Ch1 equivilent of Freeday from the sandbox

label TaigaInv1:
    #Taiga Investigation
    #[BG: Courtyard]
    #-Intro-
    scene backgroundcourtyard
    "I find Taiga doing stretches in the courtyard."
    "Next to him is a wide pen for his rabbits to enjoy the fresh air."
    "It's strange to see him this awake."

    show sprite Tbase

    t "....."
    t "How long have you been watching me?"

    n "I wasn't- What are you doing anyway?"

    t "I'm not used to sitting for hours at a time. I thought they might kick me out if I slept in that egotist's class, but you shot that theory dead in the water."

    n "I haven't done anything though."

    t "No, but you're here. And nobody's gotten detention for that announcement stunt either. I'd hate to see what you'd have to do to get suspended."

    n "That's fair..."

    t "You gonna tell me why you came looking for me or did you come to see my assistants again?"
label TaigaChoice:
    menu:
        "Alibi": 
            t "I've never had to wake up before ten until I came here."
            t "I would have stayed in my dorm, but the red headed nurse's assistant dragged my ass to homeroom."

            n "You mean Mu?"

            t "Yeah, him. I was practically a zombie all morning."
            t "He wouldn't even let me sleep while he was getting his stuff."

            n "What, you tried to lay down in the hallway?"

            t "What? No, man, he keeps his stuff in the nurse's office."
            t "There's a perfectly good bed there too and he wouldn't let me crash there."

            n "What's wrong with his locker?"

            t "Nothing really."
            t "I guess he's making some extra scratch renting it to Mariko for all her club stuff."

            "Isn't that extortion? Surely the school would have given her space to store club stuff if she asked."
            "Why go so far to rent someone else's locker?" #(+Genki's Second Locker)
    
            n "Anyone else know about this?"

            t "Probably the cheerleaders. I didn't ask though; didn't think it mattered."
            call TaigaChoice
        "Show Evidence":
            "I showed him the CDs"
 
            t "Man, Kazz has the worst taste in music."
            t "This is why no one listens to his radio shows."

            n "My alarm's stuck on it. Every morning I have to fight with it."

            t "Hunh, then I wonder why they used the PA system?"
            t "Kazz's stuff is automatically set to the radio."
            t "If they want to send a threat to you, it'd be easier to reach you there."

            n "To embarrass us. Well, not embarrass, that's not it. Expose. That's the word."

            t "Seems like a lot of risk and effort for little reward."

            "He has a point though. It's odd someone would make a move like that in front of the faculty."
            "Why wouldn't they try to be more secretive about it?"
            call TaigaChoice
        "Leave":
            call TaigaOutro
label TaigaOutro:
    t "You really care what all those kids think, don't you?"

    n "Well, yeah, don't you?"

    t "Not particularly. They've all tangled their roots in city living, so I won't see any of them after graduation."
    t "Plus, most of them are too busy tending to their own yards to look over the fence."
    t "Not that it makes them bad people, but why bother to perform for an audience that's not watching, y'know?"

    n "You don't know that for sure."

    t "How many times have you thought about someone else that wasn't related to how they saw you today?"

    n "....."

    t "Exactly. But good luck getting people to like you."
    t "It's a lot less fun liking someone than spreading rumors."

    hide sprite Tbase

    pass #connect to loop

label DyreInv1:
    scene backgroundhide
    "Technically, students aren't supposed to come to areas that are under construction."
    "But since the roof's unlocked, some people have been treating it like free game."
    "Dyre is one of those people. He’s dragging old beat-up furniture around a stack of busted palettes, just out of eye-line from the stairs."

    show sprite DBase

    n "What are you doing?"

    "He jolts, then relaxes a bit when he sees me."

    d "Just trying to make the place a little more homey."

    n "But why here? It's basically outdoors."

    d "It's also one of the few places without security cameras."
    d "None of the teachers have time to come up here, so it's the perfect spot to set up shop. Metaphorically speaking that is."

    "Dyre's a master at throwing me down rabbit holes when I come looking for something else."
    "I gotta stay focused."

    n "Cool. Look, I actually came to talk to you about something else."

    d "Oooh, let me guess, you're playing detective and want to cross examine me as a witness."
    d "Are you going for a Sherlock vibe or Batman?"

    n "This is serious, Dyre."

    d "I'm just trying to figure out how long this is going to take."
    d "No need to take it so personally."
label DyreChoice:
    menu:
        "Alibi":
            d "It was the first day of school; there was a bunch of 'get to know you' lectures and other nonsense."
            d "Huge waste of time, but everyone saw me in class."
            d "There's no way I had the time to set all that up."

            n "You honestly expect me to believe you didn't mess with anyone?"

            d "I didn't say that."

            "He says with a knowing smile, then sighs."

            d "I'm sure you've heard by now, but Kazz brought in a bunch of contraband into the school."
            d "It's a bunch of tech stuff, which I wanted to be able to borrow, but he wouldn't shut up about having it."
            d "So, I got worried it'd get confiscated or stolen."

            n "What did you do?"

            d "I had Genki hide his Echo in the recording booth when she was dropping off her club request form."
            d "I thought it'd be funny to have him freak out for a bit just to have it be right under his nose."
            d "Y'know, teach him a lesson before he got his stuff taken away."
            d "Turns out I was a little late for that."

            n "So Mariko's the last one to touch his echo?"

            d "We don't know that. Any other club leader could have found it in there." #(+Prank)
            call DyreChoice
        "Show Evidence":
            menu:
                "Computer":
                    n "Someone was having trouble getting the echo to do what they wanted."
                    n "The history is full of searches on how to leave a recorded message."

                    d "...that idiot."

                    n "So you know who it is?"

                    d "I was making a general statement."
                    d "Whoever left without clearing their internet history is an idiot."

                    "What a liar!"
                    "But, if he's willing to cover for them, it might be someone he's close to."
                    "At the very least, I know it's not him."
                    call DyreChoice
                "Announcment List": 
                    d "That many people want to start a club, hunh?"
                    d  "No wonder Mariko's been so competitive with recruiting."

                    n "What do you mean?"

                    d "Well, there's only four teachers, right?"
                    d "That means unless they have time, they'll only be able to supervise one club each."
                    d "The first four to get enough members will probably be the only legitimate clubs this year."
                    call DyreChoice
                "CDs":
                    d "Kazz already gave me a tour of the booth. I don't need a second."

                    n "Nothing looks different to you?"

                    d "Nope. That's what it's supposed to look like."
                    call DyreChoice
        "Leave":
            call DyreOutro
label DyreOutro:
    "By this point, Dyre has completely abandoned his attempt to rearrange the roof."
    "He regards me with the same amount of intrigue and confusion one might have toward a foreign commercial."

    d "You really had a hand in the riots, didn't you?"

    n "Yeah. I think everyone has made that abundantly clear."

    d "Forgive me for doubting, I just didn't want to believe it, even though the truth was so obvious."
    d "It's just so disappointing to see how low you've sunk."

    "Honestly, I don't know what to say. He doesn't even look that mad."

    d "You need to figure out real quick what you stand for or you're not going to like the results."
    d "No one's going to wait around for you to make up your mind."

    n "What are you talking about?"
    n "I know what happened wasn't ideal, but it was the only way to protect my friends."

    d "If you really believed that, you wouldn't be here."

    hide sprite DBase

    "He brushes past me, leaving me alone on the roof."
    "Just who does he think he is anyway? I can't let him get to me."
    "I should leave before I get caught."
    pass #connect to loop

label ChiseiInv1:
    scene backgroundstage
    "Chisei is puttering around the stage with a tape measure and a package of chalk."
    "She has a piece on the ground and is trying to drag it along the ground with the ball of her foot."

    show sprite Chbase

    n "Need some help?"

    ch "I suppose."
    ch "Do I look that silly?"

    n "No... I mean, I don't know what you're trying to do, but it seems purposeful."

    "I pick up the chalk."
    "Before I can hand it to her, she points at the ground."

    ch "A line, please. I need the size of the stage."

    n "Why?"

    ch "If we have enough members, the drama club can put on plays."
    ch "I want to know what space I have to work with."

    n "Can't you get the dimensions from the teachers?"

    ch "The plans are 'around here somewhere'."
    ch "I can measure it all myself before Mr. Inukai can hunt it down..."
    ch "You can laugh. I know I am slow."

    n "Oh. Sorry, I had something on my mind."

    ch "What is it?"
label ChiseiChoice1:
    menu:
        "Alibi":   
            n "What were you doing the day before the first day of class?"

            ch "I wanted to find some potential plays for the drama club before drafting the recruitment announcement."
            ch "So that night, I went to look around the shelves on the first floor."
            ch "However, I got scared and did not find anything in time."

            n "The hallways do get really eerie at night."

            ch "Exactly! The lack of artificial light at night is welcoming to the stars, but it shrouds the interior in shadows."
            ch "Confronting sirens, armed only with a flashlight, I felt my heart stop for a second."

            n "Metaphorical sirens or weird noises?"

            ch "A loud series of noises, around the lockers, I think."
            ch "I did not pursue the matter further."
            ch "Though seeing as I have not gotten in trouble for wandering the grounds at night, I do not think it was something I triggered."
            #(+Mysterious Noise)

            n "Have you heard it since?"

            ch "Thankfully, no. A number of our peers find such noises upsetting."

            "I think most people find loud noises upsetting."
            "Especially when they come out of nowhere in the middle of the night."

            call ChiseiChoice1
        "Show Evidence":
            "I show her the announcement list."
 
            ch "I am glad Ms. Yamamoto is a patron of the arts."
            ch "Without her support, I would not have been granted approval for the drama club."
            ch "Now it is just a matter of gathering members."

            n "Does that mean she submitted your ad for you?"

            ch "No, I had to sign out a key from the student council."
            ch "I managed to get my ad in after Momoko, but before the head cheerleader."

            n "Was Kazz's echo in there the whole time?"

            ch "I did not think to check, I am sorry."

            call ChiseiChoice1
        "Leave":
            call ChiseiOutro
label ChiseiOutro:   
    ch "....."

    "She bites her lip, looking at the string of lines we made on the stage."

    ch "This is your first time coming to this building, right?"
    ch "You and your friends did not come here before it was a school, did you?"

    n "I mean, I didn't. I can't imagine the others coming all the way out here... why?"

    "She holds up her left hand with a frown."

    ch "I thought if I was far enough from civilization, I would stop getting messages."
    ch "They are not as frequent, but today..."
    ch "There is something still trying to use me."
    ch "I was hoping it was not something that followed me here."

    n "What did it say, if you don't mind me asking?"

    ch "....."
    ch "Attack the crowd and be thrown to the lions."

    n "Is that like 'don't bite the hand that feeds you'?"

    ch "I cannot find any record of it anywhere."
    ch "The closest thing that comes up is 'Damnatio ad bestias'; death by beasts."
    ch "It was used as a punishment for instigators of rebellion."

    n "The only thing around here is Taiga's rabbit and pigeons."

    ch "I hope it is nothing. I never know what to do with anonymous messages, especially cryptic ones."
    ch "All it does is bum people out, but then I wonder if I have a moral obligation to share?"

    n "Well, it's not like your hand predicts the future."

    ch "No. I have no clue who these words come from."

    n "Then don't worry too much about it."
    n "You're not a spiritual post office."

    ch "Y-yeah."
    ch "Yeah! I am not everyone's personal fortune cookie, I am a different kind of snack."

    "Her sudden burst of energy catches me off guard and I can’t help myself; I laugh."

    ch "I finally got you to smile!"

    hide sprite Chbase

    "I came here looking for answers, but Chisei ended up cheering me up instead."
    pass #connect to loop

label ShomaInv1:
    scene backgroundsew
    
    "Shoma is in his hovel of a sewing room."
    "The place is a little more organized than before, but strung up lights can't block out the dungeon vibe I get whenever I walk in."

    q "Emerge from oblivion, O' weary traveler."

    "What the- Where did that come from?"

    show sprite ShBase

    sh "Come to check the place out now that all the heavy lifting is done?"

    n "Sort of... Is there anyone else here?"

    sh "Nah, that's a recording. Just one of the many ways I tried to make the place feel normal."

    "This guy's definition of normal and my definition are wildly different."

    sh "Now if only I could find a diffuser that wasn't also a fire hazard, I'd be set."

    n "I know you've been busy getting set up, but I had a few things I wanted to ask you."
label ShomaChoice1:
    menu:
        "Alibi":
            sh "I've been spending most of my freetime unpacking. It's a long way from here to the dorms."
            sh "Rei sort of lent a hand, but she's been getting dragged around to help with the cheer squad so..."

            "He groans."

            sh "I was doing a good job hiding from them, but I still managed to get roped into making their uniforms for free."

            n "Can't you just say no?"

            sh "According to your Treasurer, my refusal would result in the squad putting together uniforms with hot glue and desperation."
            sh "The last thing they need is to be publicly humiliated by a wardrobe malfunction."

            n "You could start a tab. The teachers should be reimbursing you for anything club related, shouldn't they?"

            sh "I suppose I could get a few contracts going."

            "I can practically hear a cash register go off in his mind."

            n "You haven't heard anything out of the ordinary, have you?"

            sh "There's been a bunch of the generator tests and the like going on at night."
            sh "I think Mr. Yaguchi hasn't finished installing the school's security system yet."
            sh "He's been fighting with someone at odd hours."

            "That explains how someone could sneak around at night without getting noticed. I wonder who he's fighting with."
            call ShomaChoice1
        "Show Evidence":

            "I showed Shoma a pictture of the computer."

            sh "Oh shoot, that stuff would have been helpful a few hours ago."
            sh "It would have saved me a bunch of eye rolls from Setsuna."
            sh "Logging into my stuff was a pain. I mean, who wants someone having a record of their activities on someone else's phone? But I figured it out."

            "I thought Kazz was the only one that managed to smuggle stuff in."

            n "How do you know who's logged in if it's not connected to your phone?"

            sh "Watch this."

            "He turned his head toward the door."

            sh "Computer, identify account."
            call ShomaChoice1
        "Who's logged in?":
            Alexa "Setsuna the Bomb Digity is logged in."

            n "....."

            sh "I know right, but what to do with this information?"

            "I'm starting to think Setsuna should be worried about getting spied on and not the other way around."

            sh "Without an account, it's basically a brick, so I have to ask for her help every time I want to add a command."
            sh "It'd be easier if she'd just let me put my own account on it, but she wants to have total control over it, so...."

            "So anyone logged into the same account can give it commands."
            "That's good to know. There was no login page in the computer's history and I doubt that someone would leave behind the search history if they were covering their tracks."
            "They must have some other way to log in."
            #(+ID Account)
        "Leave":
            call ShomaOutro
    #-Other-
    #sh "Kazz takes requests for what plays on the school radio. I've suggested a bunch of stuff, but he hasn't played them yet. I wonder if his friends got top priority."
    #"I should try asking about something else."
label ShomaOutro:
    
    n "Why go through all this trouble just for a glorified door bell?"

    sh "It's acting as a personal assistant. Anything I need gets put on the list of council expenses."

    n "Does that mean the teachers have access to it?"

    sh "I... I hadn't thought of that before, but you're probably right."
    sh "They're definitely aware it's here."
    sh "I mean, Setsuna wouldn't be using things behind the teacher's back, would she?"

    n "If she told them, they may have just forgotten she said anything. That happens a lot."
    n "Do you remember if she said something about the stuff?"

    sh "Uhh... Umm... Hmm... Not really, no. Oh wait!"
    sh "She did mention having to talk to them about something in a student's locker and to keep this thing safe for her."

    n "You think maybe that meant hide it for her?"

    sh "...oh."

    n "Yeah, maybe don't have it set to motion control."

    sh "Motion control? Try remote control, I can tell it when to play with the push of a button."
    sh "Those things don't have cameras or people sensors. It's just a speaker with a microphone."

    n "Still, I don't know how much trouble you'll get into with the teachers for harboring a fugitive, but Setsuna will kill you if they confiscate it."

    sh "Fair point. Good thing it's hidden where no one can find it."

    n "....."

    n "It's in that box of fabric, isn't it?"

    sh "And no one can find it. Trust me, I've already lost two needle cushions in there. Things just have a habit of disappearing around here."

    hide sprite ShBase

    "I think I've gotten everything I can get from him. I best get moving."
    pass #connect to loop

label IchitaInv1:
    #Ichita Investigation
    #[BG: Pond]
    scene backgroundpond
    "I find Ichita by the large pond behind the amphitheater."
    "He’s sitting on the dock and staring into the water intently."
    "It’s so murky, you can’t see the bottom, but every now and then, I swear I see a fish."
    "At least ducks think it’s safe to land on."

    show sprite IBase

    i "How deep do you think the water is? It looks hella deep, right?"
    i "Like it's meant to be swam in."

    n "Dude, you know they don't want us in there. There's some kind of amoeba in it or something."

    i "Those only live in standing water, all this stuff is an offshoot of the river."

    "He lays back on the dock, his legs dangling over the edge."

    i "They just don't want to get a lifeguard for us."
    i "We'd be totally fine with a few floaties or something."

    n "It's really too cold to be doing that kind of stuff anyway."

    i "Why you gotta constantly crush my dreams, man? I know you're not here to fight, so what do you want?"

    n "I wanted to ask you about the intercom incident."

    i "You think I had something to do with it!? If I wanted to hurt you, I woulda punched you in the face when we met."
    i "I'm not stupid enough to bang pots and pans around the teachers announcing a fight."
    i "That's just- I don't know anything about it, okay."

    n "Maybe you saw something then."

    i "Like what?"

    n "I don't know, literally anything noteworthy or out of the ordinary."

    i "I mean, I'll try, but I don't make any promises."
label IchitaChoice1:
    menu:
        "Alibi":              
            i "I spend every chance I get outside. The grounds here are huge; I still haven't seen everything yet."
            i "Besides, the school building's kinda creepy, don't you think?"

            n "What do you mean?"

            i "I don't know, just a bad vibe. Like electronic stuff turns on and off on its own and it's everywhere throughout the school."
            i "People have heard sirens go off in the middle of the night."

            n "People? Who?"

            i "Chisei and Kietsu mentioned it, but maybe it's just a Vision Major thing."
            i "Or a 'don't be in the school unsupervised' thing."

            n "Let's hope for the second."

            i "I guess. But what good is an alarm if there's no one to respond to it?"
            i "Unless... You don't think we're being recorded, do you?"

            n "I didn't... before."

            "Now I'm not going to be able to shake that feeling of being watched."

            n "Thanks for that."

            i "Sorry. I'm used to having a camera in my room, so it seemed like the next logical conclusion."

            n "Not helping."

            "Please god, don't let there be a camera in my room."
            call IchitaChoice1
        "Show Evidence":
            "I asked Nagen about the missing phone."
            
            i "Wait, that was Kazz's. I think I might know where it is?"

            n "Really?"

            i "Yeah, Kitsune n' I found this black thing in the dirt by the dorm."
            i "I thought it was a taser at first because the case was covered in skulls n' junk."
            i "Anyway, Kitsune insisted we take it back to the owner since that stuff's, y'know, banned, but we couldn't get in to see who's it was."
            i "So she went to Setsuna for help."

            n "Did you see her give it to Setsuna?"

            i "Well, no, but the thing was basically a paperweight without a passcode."
            i "I can't imagine it'd be too useful to anyone other than Kazz."
            #(+Found Phone)
            call IchitaChoice1
        "Leave":
            call IchitaOutro
    #-Other-   
    #i "You're guess is probably better than mine. That doesn't seem out of place to me."
label IchitaOutro:
    #-Outro-
    i "What exactly are you going to do when you figure out who it is?"

    n "What do you mean?"

    i "Say you find out who it is- then what? You going to shove their head in a toilet?"

    n "What? No! I'll- that isn't any of your business."

    i "Like hell it isn't! That bastard scared the shit out of everybody with that announcement, going off like we're trapped here. It's making people stir crazy."

    "...is that why he's out here?"

    i "We have to be here for at least three years and they start us out with this nightmare-fuel calling card, what an asshole."

    n "Wow, uh, I don't know what to say. I just assumed you weren't on my side."

    i "I'm not and I still plan on kicking your ass as soon as a single hit won't kill you."

    n "...great."

    i "But, I'm also not going to support a hypocrite that wants to drag everyone into their drama. As far as I'm concerned, you're both the same. If I ever find them, I will shove them into a locker."

    "I can barely fit my backpack into my locker, but I don't think it's a good idea to bring that up."

    n "Umm... thanks, I guess."

    i "No problem. Now, if you don't mind, I'm going to take a nap."

    "He still doesn't get up."

    n "Umm..."

    i "Zzzzz"

    "Damn, that was fast. I should go now."

    hide sprite IBase

    pass # connect to main game loop

label SetsunaInv1:
    scene backgroundcafexn
    #Setsuna Investigation
    #[BG: Cafe Exterior]
    
    "Setsuna can really be hard to find when she wants to be. Which I guess in her case, would be all the time."
    "I find her outside the cafe surveying the flora with a wrinkled nose."

    n "What's wrong?"

    show sprite SBase

    s "Just thinking about what all could be living under there."
    s "Bush vipers are common in this region. Wouldn't want something to happen to Taiga's... pets. Too much paperwork."

    n "You're suggesting we take care of it?"

    s "Well, it's that or hire someone who will. And trust me, we do not have the money to pay someone to pull weeds."

    "The overgrowth around her is waist high. I hardly consider them weeds."
    "At this point, they are the grounds. She shakes her head."

    s "Honestly, they have our work cut out for us until graduation. So, what did you want to complain about?"

    n "I wasn't-"

    s "Don't take it so personally."
    s "It's the first week of school and everyone wants the council to fix something for them. What's your's?"

    n "I just wanted to ask you some questions about the PA incident."

    s "Oh. You actually wanted to talk to me... Sure, I'll bite. What did you want to know?"
label SetsunaChoice1:
    menu:
        "Announcement List": 
            s "We thought making clubs first-come first-serve would make things easier."
            s "That way it didn't seem personal when we told people no."

            "She groans into her hands."

            s "I mean, for god's sake, there isn't enough time or mentors for everyone to get what they want."
            s "That isn't the council's fault."

            n "Are people still trying to get their clubs approved?"

            s "More like they're yelling at me because all the spots got taken on the first day."
            s "We got a drama club, gaming club, cheer squad, and the student council. That's it."
            s "And it's not like I'm saying people can't hangout, they just can't get school credit for it."

            n "And how many of those clubs are you in?"

            s "All of them, obviously."

            "And yet she can't understand why people think she's biased."

            s "I may be an opportunist, but I accept all opportunities equally." #(+Club Leader List)
            call SetsunaChoice1
        "Computer":

            s "Well there's two reasons the computer's search history's like that."
            s "Either A: the Echo was new or B: someone was borrowing it."
            s "Regardless, it was new to the user."
            s "Was anyone logged in on the help page or tried to log in on the computer?"

            n "Not on the computer."

            s "Maybe the echo was stolen then."

            n "Hunh?"

            s "Think about it: if you were going to set up commands, why use mobile when the desktop was right there?"
            s "It would have been faster to type up that message on the computer rather than on a tiny screen."
            s "The easiest explanation would be they couldn't log in."

            "People forget their passwords all the time, but if they had access to something that already had access..."

            n "I'll keep that in mind."
            call SetsunaChoice1
    #-Other-
    
    #s "That's supposed to be there, it was donated to the school."
        "Missing Phone":  
            s "I gave that noisy thing to the principal."
            s "I mean, I assume that's the one you're talking about."
            s "It had been going off through the whole council meeting, literally the worst."

            n "Where was it?"

            s "In Mu's locker of all places, and it was the only thing in there."
            s "I had to go through a stack of papers a mile high just to find the locker combination."

            n "Why didn't you just ask him?"

            s "Why do you think? Starting out school with contraband is obviously suspicious."
            s "It's either his or belongs to someone he knows."
            s "I wouldn't put it past him to cover up for someone if he knew we were onto them."

            n "And you're sure it's Kazz's?"

            s "Everything seems to line up, unless someone has an identical phone case and ringtone."
            s "The screen was password locked, so I can't say with a hundred percent certainty."

            "That sure sounds like Kazz's phone alright. I should let him know where it is. "
            #(+Locker, +Phone)
            call SetsunaChoice1
        "Leave":
            call SetsunaOutro
label SetsunaOutro:
    s "You've been surprisingly level headed about this whole thing. I'm starting to see why Nanase wants you on the Council so badly."

    n "Are you actually warming up to the idea of me being Student Council President?"

    s "Barely. But I have to admit, there's only so much the three of us can do at this point."
    s "The school's full of strong personalities and we're seriously outnumbered."
    s "Besides, you respect me enough to listen to what I have to say, which is more than any opponent I could find would do."

    "Hard to believe the bar is that low at this point. I'd sooner believe no one else is interested."

    n "If you didn't sign up for every club, you'd have the time to run the council yourself if it matters that much to you."

    s "A nice sentiment, but I'd run into the same problem only tenfold."
    s "It's one thing to be ignored as an accountant, but as a leader- Not worth the stress."
    s "Our best strategy is to make use of how you scare people to get them to listen to us."
    s "They've already given you a golden opportunity."

    n "You're expecting me to make an example of this?"

    s "I sure hope so. The real question is what kind of example you want to set."

    n "....."

    s "I'll be watching you. We all will."

    "She turns her attention back to the overgrowth."

    s "In the meantime, I'll need a pair of scissors."

    hide sprite SBase
    pass #connect to game loop

label KitsuneInv1:
    scene backgroundlibrary
 
    "I find Kitsune in the library with her head down on one of the desks."
    "She usually seems so put together, or at least, she tries really hard to seem that way. For a moment, I’m seriously worried."

    show sprite KBase

    k "You wouldn't happen to have Tylenol or something, would you?"

    n "No. Shouldn't you go to the nurse's office for something like that?"

    k "Absolutely no, I'd have to walk."

    "She kicks at a pair of abandoned heels."

    k "And I really don't want to deal with all of Mu's nosey questions."

    n "That's fair."

    k "Would you be able to go get me some? Please?"

    "There's no way Mu would hand me meds unless he was there to watch me take it."
    "But Jona usually carries all kinds of stuff in his pockets."

    n "I might know where to get some, but afterward I need to talk to you."

    k "Yes, anything. You're literally a life saver."

    "I return with a ziplock bag and a 'no questions asked' debt to Jona."
    "Kitsune accepts it with abundant appreciation."

    k "I seriously underestimated how much endurance it takes to look this good everyday."

    "Yeah, she's definitely feeling better."

    k "Well, I did say I would owe you, so what exactly were you hoping to talk to me about?"
label KitsuneChoice1:
    menu:
        "Alibi":
            "Why do I get the feeling I'm going to regret asking this?"

            n "What were you doing before classes started on the first day of school?"

            k "Moi? Well, I had planned to make use of our isolation by working on my craft, but alas, I'm not a born seamstress."
            k "Actually, none of the dresses I tried to make looked wearable."
            k "If Uitto saw me held together with safety pins, I'd never be able to live with myself."

            "I don't think she'd care."

            n "You tried making your own clothes?"

            k "I have a very specific image of what I want to look like."
            k "Unfortunately, my skills aren't up to speed with my taste level."
            k "Shoma caught me trying to dispose of the evidence and was kind enough to salvage my mess into this."
            k "Though I wish he'd just teach me instead of forcing me to pay him every time I need a new outfit."
            k "I can't afford to be indebted to someone like that."
            call KitsuneChoice1
        "Show Evidence":
            menu:
                "Microphone":   
                    k "It's a shame, isn't it?"
                    k "There's no recording equipment available to the students."
                    k "But what you heard didn't use any of that."

                    n "How can you tell?"

                    k "When you have a telephone chain of recording devices and speakers, there will always be feedback or artifacts."
                    k "Something was set up to play the clip directly into the mic, live."
                    k "There's no way that was a person speaking either. Every person has a specific rhythm they speak in, but computers are flat."
                    k "Something that unnatural sounding had to be computer generated."

                    n "Why would that matter?"

                    k "Everything seems to have been done using Kazz's stuff, but he has ways of recording audio with the stuff he brought in."
                    k "We were supposed to start working on a few singles this weekend, but now...."
                    k "My point is, it would have been easier for him to record a voice and distort it than generate one. I think someone is trying to frame him."

                    "It wouldn't be hard to tip an anxious person like him over the edge as a distraction."
                    "But I can't ignore that Kitsune has a personal reason for wanting to keep him out of trouble."#(+Alexa Commands)
                "Missing Phone":
                    k "I should have known that was his, he's the only person I know who's snuck in tech they shouldn't have."
                    k "I just didn't take him for a skull kind of guy."

                    n "So you have seen it."

                    k "Ichita and I found it near the dorms."
                    k "I told him I was going to take it to the lost and found, but... I didn't want to get someone in trouble for losing something they cared about."
                    k "So I went to find someone on the council when I ran into Rei and Mariko."

                    "She bites her lip."

                    k "Mariko recognized it, so I gave it to her."
                    k "You know she's got the whole goth thing going on, it seemed like it fit her personality, she even knew the passcode."
                    k "I just didn't think to question it."

                    n "But Kazz still hasn't found it. So she didn't give it back to him."

                    k "Do you think she stole it? They're pretty close, why would she do something like that to him?"
                    k "You don't think she's just pretending to be friends with him so she can take advantage of him?"
                    k "That would be horrible."

                    n "Honestly, I couldn't say."

                    k "He already has a hard time opening up to people. If that's true, he'll be devastated."

                    "Maybe she knows something about him I don't."
                    "As far as I can tell, he's one of the most trusting people here."
                    call KitsuneChoice1
        "Leave":
            call KitsuneOutro
label KitsuneOutro:
    "She gently tugs at her hair, threading her thumbs through her pigtails."
    "I think something's still bothering her."

    k "What do you think they're going to do to Hiro?"

    n "I'm not letting anything happen to him. You don't need to worry about that."

    k "I can't help but worry. It's one thing to humiliate someone, but to be so deliberately vague..."
    k "I've seen girls pushed down stairs for not dropping out of choir competitions before."
    k "This could get really ugly. He's too trusting."

    n "Yeah... I'm glad someone else here is taking this seriously. A lot of people have been making me feel like I'm being paranoid."

    k "People generally send threats hoping fear will be enough to get them what they want."
    k "If they really wanted to fight, they wouldn't have warned you guys at all. Instead, all of you stayed."

    n "You think they're trying to get all of us to drop out of the school?"

    k "They said all of your names; I think it's safe to say they want to use Hiro to scare you guys as well."
    k "And if the scare tactics aren't working, how else are they going to guarantee Hiro won't come to class?"

    "A number of things come to mind, none of them good."

    k "If I were you, I wouldn't be investigating on your own like this."
    k "Especially when meeting people in places without witnesses."

    "She carefully puts on her heels and sighs."

    k "I always forget how sheltered you were."

    hide sprite KBase

    "She hobbles out of the room and leaves me behind."
    "I’m the only one left in the library."
    pass #connect to loop

label MuInv1:
    scene backgroundcourtyard
    "It's weird seeing Mu outside of the nurse's office."
    "I mean, I know he's a student here, but I assumed he'd spend his free time hiding in a corner getting high."
    "He’s sitting at the stone table when I find him and looks up from his burner phone at me in surprise."

    show sprite MuBase

    mu "I thought vampires hated the sunlight."

    n "You would know. Pretty sure your whole squad's allergic to sleeping."

    mu "Don't remind me."

    "Hit a little too close to home I see."

    mu "I'm on break right now, but if it's an emergency-"

    n "I'm not here for health reasons."
    n "I just wanted to ask you some questions about what's been going on at the school."

    "He gestures at the seat across from him. I take that as an open invitation."

    mu "Just questions. If you turn this into a cross examination, I'm leaving."

    n "I suppose that's fair."

    "It never ceases to amaze me how small I feel next to this guy, even when he's sitting down."
label MuChoice1:
    menu:
        "Alibi":
            mu "When I haven't been hanging out with Kazz and Dyre, I've been talking to you."

            n "Really?"

            mu "Yeah, funny how that works."
            mu "It's been nice to talk to other people, even if everyone's a little high strung."
            mu "What a way to start the year though. I thought the wrestling team's hazing was bad."

            n "I don't think the goblin on the PA system was hazing us."

            mu "Wasn't thinking about that. Buuut, can you really rule out the possibility?"
            call MuChoice1
        "Show Evidence":
            menu:
                "Missing Phone":  
                    mu "I feel bad for Kazz, I really do, but bringing stuff you aren't supposed to have doesn't make you cool."
                    mu "He kept showing off and trying to impress people with all the stuff he managed to slip by the teachers."
                    mu "There's only so much second hand cringe we could take, so Dyre had the bright idea to give him a scare by swiping his Echo."
                    mu "That was before we realized he lost his phone."

                    n "Does he know you guys took something from him as well?"

                    mu "All they did was sneak it into his PA booth without telling him."
                    mu "Honestly, I'm surprised it took him so long to notice they moved it."
                    mu "Even then, we had to tell him where it was."

                    n "'They' not 'we'?"

                    mu "I'm just an idea man. I didn't have a clue how to get in the booth without raising suspicion."
                    mu "You've seen how guarded he is about it."
                    mu "I thought it'd be better to just hide it in a locker, but Dyre and Mariko were determined to hide it right under his nose."

                    n "When did all this happen?"

                    mu "During move-in day."

                    "So the Echo was already in the booth by the time club submissions were open."
                    "That means anyone who could get in the booth would have access to it."
                    #(+Brag) (+Prank)
                    call MuChoice1
                "Computer":
                    "When I show him the search history, his face darkens."

                    n "Something wrong?"

                    mu "Looks like someone was trying to figure out how to get Kazz's Echo to learn new commands."

                    "He shakes his head."

                    mu "Kazz has his set up to do a bunch of things."
                    mu "They probably just wanted it to spook him when he said something or change what name it responded to."

                    "He's absolutely covering for someone."
                    "I don't think he'll tell me who, but he might be able to confirm something else."

                    n "Is there a way to tell who gave it new commands?"

                    mu "No. It can tell you what account it's logged into and what date it was added, but that's about it." #(+ID Account)
                    call MuChoice1
        "Leave":
            call MuOutro

    #-Other-
    
    #mu "Kazz and I have a deal. I don't touch his junk, he doesn't touch mine."

    #"I'm just going to let that one go."
label MuOutro:
    #-Outro-
    
    "I think it's fair to say that someone he's close with is involved."

    mu "Nagen, I swear, I'll try my best to get to the bottom of this."
    mu "I don't know what I can do about it though."

    "Well, that's more than I was expecting."

    mu "It's just, I don't want to throw someone under the bus without evidence."

    n "You just hope that the conclusion you came to is wrong."
    n "Funny you won't share it with me."

    mu "It's not you I'm worried about."
    mu "It's the little murder hobos that you hang out with that has me worried."
    mu "At the end of the day, my job is to keep people from hurting themselves."
    mu "The last thing we need is a fight."

    "He gets up to leave."

    mu "I'm sorry things ended up like this."
    mu "I thought I could trust my own friends."

    hide sprite MuBase
    pass #connect to loop

label KazzInv1:
    scene backgroundhide
    "It takes a while to track down Kazz."
    "Everyone I‘ve talked to has seen him running all over campus."
    "When I finally find him, he’s lying on the ground with his arms shoved under a broken couch."

    show sprite kkbase

    n "What are you doing down there?"

    "He rolls onto his back and sits up."
    "His hair is a mess and his hat got lost in the folds of his hoodie."

    kk "Dude, I'm so fucking dead. You haven't seen a camera with paint splattered on it, have you?"

    n "No man, I haven't."

    kk "I'm sorry brogati, I know I probably sound like a broken record by now."
    kk "It's just- the longer my stuff's missing, the more I'm freaking out about who could have gone through it."
    kk "I didn't even think to back anything up. What if it's dead!?"
    kk "Shit, I don't know which is worse, broken or stolen?"

    n "Woah there, you need to breathe. It's not the end of the world."

    kk "I'm going to be the idiot that got expelled on the first week of school."
    kk "If they take me, give Dyre the rest of my stuff. He'll know where to find it."

    n "You're not going to get expelled."

    kk "Really? Everything's made out to look like I did it."
    kk "I mean, isn't that why you wanted to talk to me?"

    n "Hunh?"

    kk "Given our previous relationship, it's overwhelmingly likely you came here with an accusation of some kind."
    kk "Circumstances have been tailored to paint me as the villain."
    kk "And this was supposed to be the year everyone finally thought I was cool!"

    "I guess I'm not the only one struggling to rebuild their image."

    n "I'm trying not to jump to conclusions, but I do need to talk to you about everything that's happened."
    n "Especially if you think someone's setting you up."

    kk "I didn't say that..."

    "He's the one who brought up getting framed though."

    n "Whoever hacked the PA system used your equipment to do it."
    n "It'll help us both if we can find who actually did it. They might still have your phone."

    kk "That's- Alright. What'd you need from me?"
label KazzChoice1:
    menu:
        "Missing Phone":
            #[If Phone = -]
    
            n "Do you remember where you last had your phone?"

            kk "I duct taped it to my... leg during move in to smuggle it in."
            kk "But after I got all the boxes into my room, I couldn't find it."

            n "See anyone near the dorms at that time?"

            kk "Kitsune and Ichita were goofing around and Shoma was moving stuff from the dorms to the school."

            "I'll try asking one of them."

            #[If Phone = +]
    
            n "I found it, but..."

            kk "Oh no, what happened? Did it get put in rice in time?"

            n "It's not broken. Setsuna gave it to the principal."

            kk "For the love of Brodin, why!?"

            n "It kept making noise in the lockers and she didn't know who it belonged to."
            n "The teachers probably don't know either, otherwise you'd be in trouble already."

            kk "Awesome! Wait, no, not awesome."
            kk "If I don't claim it, it could end up in the garbage, but then I would get detention."
            kk "Who's locker was it in? I checked all the empty ones three times."

            n "Mu's."

            "Everything's a mess right now, but the bottom line is Kazz's 'friends' were the ones running off with his stuff."

            kk "That traitor is dead to me now. Welp, nothing I can do about it now, I guess."
            kk "I don't have any money, but here, would this be an okay reward?"

            "He hands me a foil card in a plastic sleeve."

            n "Is this a KG card? Where did you get this?"
            n "They stopped making them years ago."

            kk "I used to collect them when I was real little."
            kk "It's a golden age hero, so it might be worth five bucks if you can find a collector that still buys them."

            n "Like hell I'm going to sell it."

            "I had to leave my old collection behind when I ran away from home."
            "Maybe I should try collecting them again."

            kk "Glad you like it!" #(+Memento Mori Card)
            call KazzChoice1
        "Alibi":
            kk "What was I up to during move in?"
            kk "I don't know man, moving in? Meeting new people and trying to make a good impression, you know, normal stuff."

            n "Define 'normal' stuff."

            kk "If I could, I wouldn't be in this mess."
            kk "Once you left our class, I was the nerd everyone tried to cheat off of, and they stopped talking to me when I didn't let them."
            kk "After the disaster in Guwon, I thought here's my chance to be the cool kid for once."
            kk "If I'm friends with everybody, then going to school here will seem less scary."
            kk "All it did was get my stuff stolen."

            n "It's probably the same asshole that threatened Hiro."

            kk "And that's a good thing because???"

            n "Well, then it's one mega-asshole making everyone miserable instead of everyone being two-faced and stealing from people."

            kk "It just sucks because without my phone, I can't log into anything."
            kk "Everything's been on auto login for years, so I don't remember any of my passwords."
            kk "I don't even have a phone lock because it'd been another blob of info I'd forget."

            n "...you seriously don't remember a single one? Why not reset your passwords then?"

            kk "I need my email to do that, which is hooked up to my phone, and uses a password."
            kk "Plus, the school blocks messaging websites, so I couldn't even if I wanted to."

            "That thing's basically a skeleton key for everything he owns."

            kk "I asked the council for help, but they're the ones who let club leaders in the PA booth unsupervised. They didn't even ask me first."

            n "How could they, there was no way to call you?"

            kk "Bro."

            n "Sorry, too soon."

            kk "Anyway, I haven't done much other than that."

            #(+Brag, +PA Access, +Missing Phone)
            call KazzChoice1
        "Show Evidence":
            menu:
                "Announcement List":  
                    kk "Kietsu seriously let everyone and their dog into my sanctuary of music."
                    kk "I came in after lunch and found a stack of unvetted announcement requests."

                    n "A stack? But it's only three people."

                    kk "Apparently, no one put a world limit on the request form. Mariko's was like, 24 words, but Chisei..."
                    kk "She basically wrote a two hour long radio show to advertise for the drama club. The things she writes now are total downers."
                    kk "Momoko just wrote what her club was with instructions to 'adlib'. Still, I'm glad it was only those three."

                    n "You don't think they shared the key with anyone else, do you?"

                    kk "Why would they? Letting anyone else in would risk having their club bumped from the running."
                    kk "It would completely defeat the purpose of their recruitment ad."
                    kk "Besides, Mariko was the last one in there, and she'd have told me if something was out of place." 
                    #(+Cheer Ad, +PA Access)
                    call KazzChoice1
                "CDs":
                    kk "This school had a really crummy selection when we came in."
                    kk "It was all instructional tapes and hot garbage."
                    kk "So I asked around to see if anyone brought stuff from home."
                    kk "Turns out, there's quite a few music lovers that brought their CDs."

                    n "So this isn't your private collection."

                    kk "Some of them are mine. I tried to keep everyone's stuff separated so I could give them back at the end of the year."
                    kk "Mariko had a bunch of 90s grunge rock and Mu collects stuff from pop artists I never heard of."
                    kk "If you have anything, feel free to pitch it in. Just hand it to me directly."
                    kk "Dyre'll just try to slip in his hyperpop remixes of kid's songs into your gel cases if they get to him first."

                    n "Why? Just- why."

                    kk "He thinks it's funny I guess, I don't know. Sometimes his jokes get a little out of hand."
                    kk "I just try my best not to give him the opportunity to screw with me."

                    "Even so, maybe Dyre has done other things to mess with Kazz. I'll have to give it a look." #(+Prank)
                    call KazzChoice1
                "Computer":    
                    n "Your Echo was in there too, but it got confiscated before I could get there."

                    kk "It shouldn't have been in there at all."
                    kk "Maybe it was Setsuna's and she got in to use the computer. She has one too, you know."

                    n "Any way to prove it?"

                    kk "Well, you can ask it to ID the account attached."
                    kk "Plus, mine plays Booty Pirate every morning at 8AM."
                    kk "Whoever was looking at this page was trying to figure out how to customize the alarm."

                    n "That could be anyone, but I'm guessing you and Setsuna would already know how to do that."
                    n "Someone new to the device was trying to get it to play that message automatically."

                    "And that could be anyone." #(+ID Account, +Alexa Commands)
                    call KazzChoice1
                "Microphone":
                    kk "What about Pepper?"

                    n "It can't record anything by any chance, can it?"

                    kk "No, she's set up as a push to talk, only organic live audio for my baby."

                    n "Creepy personification aside, push to talk means someone has to hold the button down for it to turn on."
                    n "Is there a way to keep the button pressed while not in the room? Like tape or a paper weight?"

                    kk "Maybe, but there wasn't any tape on Pepper when I did the morning announcements that day."
                    kk "Unless they went in sometime after I was done. They would have had to have gone straight there from class."

                    "That means anyone I saw in the halls..."

                    #[B/W CG of Rei confronting Nagen]
    
                    "It would have been impossible to make it back in time without being out of breath."

                    #[Rei, Mu, Yoku, Dyre, Taiga, Ichita, and Chisei have been removed from the suspect list]
                    call KazzChoice1
        "Leave":
            call KazzOutro
label KazzOutro:  
    n "Thanks for talking with me. I think I have a bit more to go on now."

    kk "That's good, I guess. Still, what a crazy first week."
    kk "We have a whole year ahead of us, why stir the pot now?"

    n "No time like the present, I guess."

    kk "Still, whatever their reason, I really hope it was worth it."

    n "You that scared of me already?"

    kk "Not you, man, the teachers."
    kk "You think they're going to take someone picking a fight like this lightly?"
    kk "This place has a zero tolerance policy on 'injurious behavior'."

    n "I don't think schools are supposed to tolerate students hurting people."

    kk "But like, the handbook says breaking that rule results in immediate detention."
    kk "No defined parameters or time limit, the definition is totally blank. There's no getting expelled from here either."

    "All the school rules have clearly defined consequences except that one and the way it's worded is weird."

    n "If it's against the rules to hurt someone, why not just say that?"

    kk "Who cares what their legal team made them write down?"
    kk "All that matters is anyone in a fight gets detention, and that could mean anything."

    "To be honest, I'm not too concerned with what a couple of teachers would do."
    "Especially when they've been acting like nothing happened."

    n "I'll be careful, don't worry."

    kk "......"
    kk "Sorry bro, can't say you're the one I was worried about."

    hide sprite kkbase

    "He shoves his hands in his pockets and leaves without another word."
    "Does he think I'm not going to fight or does he just not care what happens to me? Whatever, I got what I needed anyway."
    pass #connect to game loop

label MarikoInv1:
    scene backgroundclass
    #Mariko Investigation
    #[BG: Classroom]

    show sprite Mbase
    
    "I find Mariko in the art room. She has various pencils and markers scattered about the table."
    "Scraps of paper litter the floor and she seems to be pasting together various concepts for posters."

    n "You really do work without rest."

    "She visibly jumps and looks over at me with wide eyes."

    m "Nagen! For the love of- Why do you always sneak up on me?"

    n "...you're facing the door. I can't help it if you're not paying attention to your surroundings."
    n "Though you seemed pretty preoccupied by all of this."

    "I gesture to the looming piles of art supplies."

    m "Yeah, I'm not exactly the best at art stuff, but I think I made something half decent."

    "She holds up a sticky page, one of the shapes getting slowly pulled down by the weight of gravity."
    "It’s certainly eye-catching, which I guess is the goal so..."

    n "It looks like you put a lot of work into it."

    m "Thanks!"

    n "Maybe you should take a break."

    m "...sure... I take it you want to talk then?"
    m "Well, go ahead, grab a seat. No point in haunting the doorway now."

    "I clear a spot for myself under her watchful eye."
label MarikoChoice1:
    menu:
        "Alabi":
            m "It was a long drive out here, so I didn't have as much time to practice for the assembly as I would have liked."
            m "Trying to remember a three year old routine while everyone stares at you silently- It was a nightmare."
            m "And then to have Mu and Rei drag me off the stage? I've never been so humiliated."

            n "Is your ankle okay?"

            m "It's a little swollen, but it's fine. You people worry too much."
            m "I barely got the cheer ad in time as it is."

            n "Why not get another cheerleader to drop it off for you?"

            m "Only club leaders are allowed in Kazz's precious booth."
            m "At least, that's what I was told. Though I'm sure if he had it his way, no one would be allowed in."
            m "Thank goodness he trusts me in there." #(+Cheer Ad)
            call MarikoChoice1
        "Missing Phone":
            "Mariko falters and looks away."

            m "Yeah, he told me about that. He's really upset about it too..."
            m "Still, it's not like it's gone forever, right? I'm sure it'll turn up somewhere."
            m "You know what they say; 'It's always in the last place you think to look'."

            n "Isn't that because people stop looking once they find what they were looking for?"

            m "I-I don't know. Maybe?"

            n "You sure you haven't seen anyone with it? If someone stole it-"

            m "I mean, I saw Kitsune with something that might be Kazz's, but I couldn't get a good look at it."
            m "I don't want to accuse anyone of stealing, but... It's probably in the lost and found or something."
            m "I'm sure he's just avoiding asking the teachers about it."

            "She refused to look at me the entire time she spoke."
            #-Other-   
            #m "That's Kazz's, I don't know much about it."
            call MarikoChoice1
        "Leave":
            call MarikoCheck
label MarikoCheck:
    if $ Intel >= 3:
        call MarikoInt
    else:
        call MarikoOutro
label MarikoOutro:
    m "Sorry I couldn't be more help."
    m "I've been so busy with my own stuff, I haven't had time to really look around or talk to people."

    n "You seem to know a lot of people here though."

    m "Yeah, but that's just in passing. It's not the same."

    "I guess that's why she's working on posters alone."

    m "I don't get why you're so hung up on this. In a couple of weeks, it won't even matter. People will move on."

    n "Exactly. If I don't do something now, people might forget what they saw."
    n "People who could help. I can't just sit by when someone's threatened my friend."

    m "I see... I hope, for your sake, you don't get hurt over this."
    m "We've all been through enough without adding to the body count."
    m "I can see where you're coming from, though. You're a good friend."

    n "Uhh... thanks, I guess."

    "If I stick around any longer, I'll get roped into making posters for a club I'm not in. I should go."

    hide sprite Mbase
    pass #connect to main game loop
label MarikoInt:
    #[Boss Accusation]
    #[IF Intel > ? This option will be available to the player]
    #(If from Mariko Interrogation)
    #(AN: All pieces of evidence will be on screen. There will be breaks in the dialogue where the player will be encouraged to present evidence. [ = the option needed to continue the scene. Letters will denote which path the player's going down if there is more than one right answer.)
    
    "Between what everyone’s been seeing, and how she's been acting, I'm sure she's behind the PA Incident."
    "However, it’s too soon to get her to admit it, especially with how defensive she’s been lately."
    "If I want her to talk, I should ask her about something innocuous; something that would connect her to the recording booth without sounding like an accusation."

    n "I know you're busy with the cheer squad, but don't you talk to people outside of cheer?"

    m "....."
    m "Yeah, I'm talking to you, aren't I?"

    n "Well- yeah, but aren't there other people you're close to?"

    m "I've been talking to Shoma about uniform assignments a lot lately, if that's what you're getting at."

    "No good. I'll have to work backwards then and show proof someone thinks they're close to her."
    # Choose clue goes here
label Mariko1:
    #[1: Friends List]
    n "You're friends with Kazz and his group too."

    m "He's a nice guy and all, but 'friends' is a little strong of a term."
    m "We were in the same homeroom class at Estella, so talking to him came a little more naturally."
    m "'What have you been up to?' That kind of stuff. Why does it matter that I talk to other people?"

    "She's trying to downplay their connection, but it explains some things."
    "If they knew each other before, it's make sense that he'd want to impress her."
    # Choose clue goes here
label Mariko2:
    #[2: Brag]
    
    n "It doesn't really. It's just that Kazz can be pretty naive sometimes."
    n "I heard his first day here, he told everyone who would listen about all the junk he smuggled in."
    n "That includes what was found in the PA booth. I'm sure you're one of the first people he went to."

    m "So what if I was? He told a lot of people about that stuff. I mean, even you know about it."
    m "Besides, that has nothing to do with me. There isn't any proof the stuff that was in there belonged to Kazz in the first place."

    "I'm positive the recording device was Kazz's."
    # Choose clue goes here
label Mariko3A:
    #[3A: Prank]
    
    n "Dyre's been telling people he handed Kazz's Echo directly to you so you could hide it in the booth."
    n "It seemed funny to him before stuff actually went missing."
    n "There was only one Echo there, so it should be his."

    m "You don't know that."

    n "Are you saying he lied? I wouldn't be surprised, but if he hears you've been telling people otherwise-"

    m "Don't! He told a few people about doing that, but we couldn't go through with it."

    n "Then do you still have it?"

    m "N-no. I hid it somewhere else. Like I said, none of us could get in."

    "Now that's just a bold-faced lie."
    # Choose Clue Menu goes here
label Mariko4A:
    #[4A: PA Access]
    
    n "You're one of the few people who could get in at all."
    n "Even Setsuna couldn't get in. That made you the perfect pawn for Dyre's prank."
    n "Not only that, it gave you a pretty good alibi too. No one would question why you had his stuff if Dyre was talking up a prank you were helping with."

    m "So? Nagen, are you seriously accusing me of manipulating my classmates?"

    n "No, I think you just saw an opportunity and took it. I'm sure I'm not the only one who suspects as much."
    n "They're just too nice to confront you about it."

    m "An opportunity to do what? Quit dancing around the subject and spit it out."

    n "You're the one who called out a challenge to Hiro on the PA system."
    n "You borrowed the keys from Kietsu and returned them after the message played."
    n "You're the only one who could have done it."

    m "All of this is just gossip, Nagen. Even if Kietsu kept track of when the club leaders had the key, none of that proves I was ever in the booth."
    # Choose Clue Menu goes here
label Mariko5A:
    #[5A: Cheer Ad OR Announcement List]
    
    n "This is your ad, right here, and it was turned in after the other club leaders."
    n "You were the last person in the booth before the announcement went off."
    call MarikoSuccess
label Mariko3B:
    #[3B: ID Account] 
    
    n "All you have to do is ask it who's logged into it."
    n "It should tell you right away if it belongs to him."
    n "If nothing else, you could ask it to play his music or any number of things he programmed that thing to say."

    m "Alright, I get it. It doesn't matter anyway. The teachers have it, remember? There's no way to check it."

    n "Right, but I could check the Echo that hasn't been confiscated and see if he's logged into that one."

    m "You wouldn't."

    n "It'd be a quick walk to Shoma's workshop is all."
    n "You had access to Kazz's whole setup and he gave you just enough information that you could use it."

    m "Use it for what? Nagen, do I look like I'm someone who needs a digital assistant?"

    n "More like a digital accomplice."

    "Without it, there'd be no way for her to have used the PA mic without getting caught."
    # Choose Clue Menu goes here
label Mariko4B:
    #[4B: Alexa Commands]
    
    n "You used it to play your message without you having to stay in the booth to do it."
    n "You even looked up the instructions on how to get the machine to play a custom sound bite."

    m "Nagen, I'm a star athlete, but even I can't trigger a voice command and make it out without anyone seeing me."
    m "Besides, I was in class, like everyone was supposed to be."

    "Seems like she's counting on that to be her alibi, however..."

    n "It could be remotely activated with anything Kazz was logged into, like his phone for instance. It has been missing for quite a while."

    m "I did not steal his phone! Kitsune's the one who was wandering around school with something that didn't belong to her. Ask Ichita, he was with her this morning."

    "Interesting she brought her up, since their stories contradict each other."
    # Choose Clue Menu goes here
label Mariko5B:
    #[5B: Baton Pass]
    n "She's been telling everyone she gave it to you."

    m "So you're just going to believe her over me, just like that? How is that remotely just?"

    n "Well, it helps that Rei saw it happen."

    m "...Rei?"

    n "Are you going to accuse your best friend of lying too?"
    n "She has no reason to say something that would make you look like a thief. Or maybe she does, I don't know."

    m "No. Rei's not- she doesn't lie. But that doesn't mean I have it. You can search my stuff, but you won't find it."
    m "It's probably with the teachers, who knows what they do with contraband?"
    m "I took it there after I talked with Kitsune, which was before the announcement went off. So, yeah, you can't prove a thing."

    "She's just going to keep denying stuff until I spell it out for her. I know for a fact it didn't go 'straight to the teachers'."
    "Multiple people have said as much."
    # Choose Clue Menu goes here
label Mariko6B:
    #[6B: Mystery Noise]
    
    n "Leading up to the event, people kept hearing a siren in the hallway."
    n "It really freaked people out, especially the student council who was meeting that morning."
    n "Of course, I'm sure it would have freaked them out less if they knew what Kazz's ringtone sounded like."

    "She's ringing her hands quite a bit. Doesn't seem like she has anything to say to that."

    n "Kazz has been having people call it for days."
    n "Funnily enough, no one could hear it anymore after the announcements, no matter how many times it was called."
    n "It might have been given to the teachers then, but not before it could be used."

    m "Knock it off with the smug act. I don't care how many coincidences or testimonies you found, none of that proves I did it."
    #Choose Clue Menu goes here
label Mariko6C:
    #[6C: Second Locker]
    
    n "I can search anywhere you say? Even the locker you're borrowing for uniform storage?"

    m "How- that has nothing to do with this."

    n "But you do have a second locker, the one that was originally assigned to Mu?"

    m "Yeah, you're welcome to wade through the pompoms, but you're repacking it if you do."

    n "No need. I just wanted to make sure we agree that's your locker now."

    m "So what if it is? It's like you said, I'm using it to hold club supplies."
    m "Even if you told the teachers, I wouldn't get in trouble over that."
label Mariko7:
    #[7B+C: Locker #] 
    
    n "Multiple people heard the siren coming from your cheer locker."
    n "It got so bad, Setsuna had to bust into it to get the noise to stop."
    n "Only she couldn't just mute the phone because it was password locked."
    n "If it wasn't, she might not have given it to the teachers at all."
    n "Both of them thought the locker still belonged to Mu, which I'm sure you were counting on."
    n "Also it's weird it was locked considering Kazz doesn't lock his phone."
    call MarikoSuccess

label MarikoSuccess:  
    m "So?"

    n "That's all you have to say for yourself?"

    m "I didn't use all that junk to hide from you, I did it to give everyone a chance to prepare."
    m "And since I don't see Hiro behind you, I take it you're not here to support me."

    n "Support what exactly?"

    m "You've seen this place, it's not safe. It's a place to hide us until we're adults no one's responsible for."
    m "Who knows what's going on out there while we're stuck here? The fighting could come back on our doorstep any minute."

    n "You're being paranoid."

    m "And who's fault is that exactly? I know it would be easier to run away, but I can't just leave Rei here by herself like that."
    m "Hiro's my ticket for getting both of us out of here."

    n "Says who?"

    m "Like I'd tell you anything. I know I'm taking a gamble, but I'm not going to blow it by saying something I shouldn't."

    n "You're not even going to try and beg for forgiveness?"

    m "From you? What are you going to do, tell on me? Hit me? I don't feel pain and I already knew I wasn't going to graduate."

    "For a moment, her bravado falters."

    m "Hiro took everything I cared about and you just sat by and watched it happen. What else could you possibly do to me?"

    menu:
        "Blackmail you":
            $ Villain += 1  
            n "You really haven't been talking to other people, have you?"
            n "Sure, there are a few people who are mad that my friends and I are here, but more of them are pissed about what you did."
            n "You saw how Rei blew up at us. She'll barely talk to me now, imagine what she'd do to you."
            n "Did you even tell her what you were planning?"

            m "......"

            n "I can't guarantee you won't get in trouble with the faculty, but if you get expelled over this, it'll be my word against speculation."
            n "If we aren't on good terms by the end of this conversation, Rei won't want anything to do with you. That I can guarantee."

            m "You rat."

            n "Is that a no?"

            m "What do you want?"

            n "Simple. Turn yourself in and I'll help downplay this whole incident."

            "Of course, there's no telling how much mileage I can get out of this afterward."

            m "....."
            m "Fine." #(-Mariko)
            #(Enemy Neutralized) Add variable to play data so the boss battle will be skipped directly to the tape scene
            $ mRep -= 1
            call MarikoOutro
        "Protect you":
            $ Hero += 1   
            n "Someone put you up to this, didn't they?"
            n "How else could you know we were going to be here?"

            m "....."
            m "I didn't think I'd meet anyone from the riots."
            m "I was going to refuse to come here initially, but then I got this tape..."

            "She shivers, gaunt and ghostly pale."

            m "Whoever sent it knew about all of us and they knew where this place was."
            m "We're not safe here. I thought I could use them to get Rei and I out of Guwon entirely."

            "There's no way that's going to happen."
            "Even if she was successful, the DVP wouldn't let unaccompanied minors disappear like that."

            n "And what if you failed?"

            m "I don't know exactly, but whatever it is... it's not pleasant."

            n "I'm not going to let anything happen to you."
            n "We'll take care of who targeted you."

            m "We?"

            n "You may not have faith in Hiro and I, but we'll get to the bottom of this."
            n "You should tell the teachers though, they should know someone from the outside is targeting us."

            m "But if I do that..."

            "She covers her earrings with her pompoms and keeps darting her eyes between me and the paper in front of her..."
            "Is she wearing cameras? I scribble the message down and hold it up. She nods. Who would do something like this?"

            n "Nevermind. I'll let Uitto take care of things." #(+Mariko) 
            $ mRep += 1
            #(Enemy Neutralized)
    "Mariko hands me an unmarked VHS tape from her bag."

    m "On the roof, the guys found an old CRT TV."
    m "You should go there when you get the chance."

    n "I- thanks."

    "I should wait until I'm with everyone to watch this."
    "She collects her stuff with a solemn look on her face."

    m "Don't thank me yet."

    call MarikoOutro

    #[If Accusation = Fail]
    
    m "It's your word versus mine, Nagen and let's face it, people trust me more than they trust you."
    m "They want me to be here more than you. They need me to protect them."
    m "You're just paranoid and trying to protect yourself. Like always."

    "She gathers up her supplies with a glare."

    m "If I find out you've been harassing the other girls like this, you're a dead man."

    hide sprite Mbase

    pass #call main game loop

    #(Enemy Agitated) 
    #Investigation Helper Scenes 
    
    #"There's no way I can talk to everyone before the deadline. Maybe one of the guys overheard something in one of their classes. At the very least, it'll give me a place to start."



label UittoInv1:
    scene backgroundstuco
    "I ask Uitto if she was able to dig up anything."

    show sprite UBase

    u "I can't believe you wanted me to talk to Kitsune for you."

    n "...did you?"

    u "I could tell you exactly what she'd say. 'Memememe and also me.'"
    u "There you go, you got the full experience."

    n "Anyone else have anything to say?"

    u "Well, all the student council kids got spooked this morning."
    u "I guess a ghost or something is haunting the lockers."
    u "Setsuna told me which one, but I forgot."
    u "Oh! I do know who's responsible for the Echo in the PA room."
    u "Dyre had a friend of his sneak it in after it was stolen from Kazz."

    n "Isn't that Kazz's booth though?"

    u "Exactly. Who knows how long they were going to be playing musical chairs with his stuff?"
    u "That would drive me bananas."

    n "Thanks, Uitto." #(+Mystery Noise, +Prank)

    hide sprite UBase
    pass #connect to main game loop

label JonaInv1:
    scene backgroundamp
    "Jona doesn't really like talking to people alone, so I appreciate he was willing to do this for me."

    show sprite JFrustrated

    j "I wasn't sure what to ask people about, but I think I found some stuff."
    j "Kietsu's been really busy, so he let club leaders go into the PA booth alone."
    j "They're the only ones who could have gone in."
    j "Ichita thought he found Kazz's phone, but someone else went to give it to Setsuna."

    n "Anything else?"

    hide sprite JFrustrated
    show sprite JRelax

    j "No one in my class is responsible for the incident."
    j "Or at least, they weren't lying when they were talking to me."

    n "Well that narrows it down a little."

    hide sprite JRelax
    show sprite JHappy

    j "Oh good." #(+PA Access)

    hide sprite JHappy
    pass #connect to main game loop

label HiroInv1:
    scene backgroundamp
    "I felt a little nervous sending Hiro out on his own. Still, he insisted and when he returned..."

    show sprite HBase

    h "Mariko and Rei wouldn't even talk to me."

    n "Really?"

    "I shouldn't be too surprised, but I thought Hiro was friends with everyone."
    "I guess even he has his limit."

    h "They were totally afraid of me. It was such a gross feeling."
    h "Even before I could say anything, they were trying to get away from me."

    n "There's not much we can do about that at the moment."

    h "I know... A-anyway, I was able to talk to Shoma."
    h "He's borrowing one of those Alexa thingies too, so I was able to ask him all about it."
    h "I guess in order to get it to play stuff like it did, it’d have to have some kind of remote like a phone or a laptop."
    h "That way they could set it to go off at a specific time."
    h "He also showed me his to check what account it's using, to see who it belongs to."
    h "I also overheard a few Intel Majors going off about Kazz bringing in a bunch of banned stuff."
    h "You might want to try asking him about what happened. It sounds like he might be a victim in this too."

    n "I'll definitely keep that in mind. Thanks for the info." #(+ID Account, +Brag) 

    hide sprite HBase
    pass #connect to main game loop
   