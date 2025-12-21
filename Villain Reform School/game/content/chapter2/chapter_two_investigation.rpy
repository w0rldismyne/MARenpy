label chapter2_investigation_ichita:

    scene backgroundpond

    "Ichita has been scoping out areas for the party."
    "I don't think the teachers will let us do anything near the water, unfortunately."
    "He's digging around the plants with a puzzled expression."

    n "Did you lose something?"

    "Ichita bolts up and stumbles out of the brush."

    i "Naw, I was just looking for something."

    "Hey, you're books smart, do you know where lilies grow?" 
    "I can see why he'd think to look here, but the only thing growing in the pond is algae."
    
    n "Sorry man, flower stuff wasn't one of the things I studied."
    n "I'm sure there's flowers growing somewhere around here, but I bet they're going to be pretty small."
    
    i "Damn, I can't just get any old weeds. Everyone will be doing that." 
    
    "He sighs and shakes his head."

label chapter2_investigation_ichita_loop:

    menu:
        "Help with the Party":
            #+Characters helping
            n "Please tell me you have some ideas on how to make this whole party thing achievable."
            n "You're one of the people who kept raising the scale of what we're doing."
            
            i "I mean, I don't think my ideas were that involved. Nanase can handle most of it." 
            
            "He must've heard how that sounds."
            
            i "Tell you what, I'll come in two hours early. Anything you need set up, I can handle."
            i "Decorations, lights, all of it. If I turn it into a little competition, I'm sure I can get a bunch of other people to help out too." 
            
            n "What would they win?"
            
            i "Bragging rights." 
            
            n "Yeah, that'll work."

            jump chapter2_investigation_ichita_loop

        "Show Evidence":
            menu:
                "Red Hair":
                    "It looks like a match"
                    
                    i "That's weird. Did they drop it on the ground?" 
                    
                    n "We found it behind one of the letters. I don't think dropping it would put it there."
                    n "It must have fallen when the letter was being glued down."
                    
                    i "Then maybe they picked it up off the ground or maybe someone's clothes?" 
                    
                    n "Someone?"
                    
                    i "Hey man, I'm not the only one with red hair. Mu, Dyre..." 
                    
                    "He trails off, thinking really hard."
                    
                    i "Momoko, sometimes. Or heck, it might even be brown, and it just looks red because you only got the one."
                    
                    "He's making a lot of excuses for someone claiming to be innocent."
                    
                    jump chapter2_investigation_ichita_loop

                "Magazine Clippings":

                    i "Kietsu wanted us to come up with ideas for something that people would like."
                    i "I didn't want to come up with boring stuff, so I asked to borrow a few magazines to look at fancier types of parties." 
                    
                    n "Did any of them have green letters in them?"
                    
                    i "I don't know, probably. Chisei was the one who was able to find them for me. She knows where everything is in the library."
                    
                    jump chapter2_investigation_ichita_loop

                "Location of Note":
                    
                    n "Jona found it on his desk. You share homeroom with him; did you see anyone put it there?"
                    
                    i "All Vision Majors share homeroom with him. As class rep, it's my job to make sure the classroom is clean before everyone goes home."
                    i "I didn't see anything out of the ordinary before I left. If someone put it there, it had to be before the teacher got to see it."
                    i "They've been on the lookout for suspicious behavior lately."
                    
                    jump chapter2_investigation_ichita_loop
                
                "Nail Polish":

                    i "Don't wear any. Try asking one of the girls." 
                    
                    jump chapter2_investigation_ichita_loop
        "Motive":
            
            i "Creepy note, but as you remember, I was with you that morning."
            
            n "Yeah, but I'm not sure when it was made."
            
            i "So? Look man, I'm a Vision Major too. We get enough of a hard time without doing petty shit like writing mean notes."
            i "If I wanted to challenge him, I'd fight him in the hall." 
            
            "He did ask us if we wanted to get beat up now or later when Mariko first attacked. Would this be 'later'?"
            
            jump chapter2_investigation_ichita_loop

        "Leave":
            pass

    i "Hey, I know. Maybe I could get Shoma to make flowers out of cloth?" (16)
    
    "Somewhere in the distance, I hear the cries of an overworked designer."
    
    n "Maybe just have him show you how to make them. I'm sure he's busy with everything else." 
    
    i "I'm not the most crafty guy. What about Jona?" (17)
    
    "I think about objecting, but given enough creative freedom, that's exactly in his wheelhouse."
    
    n "If what you want is something unique, I'm sure he could make it for you. Though if your heart's set on lilies, you'll need to find a reference."
    
    i "That would involve looking at books. Too suspicious. Guess I'll just have to hope for the best. Thanks, Nagen!" (18)
    
    "Maybe he should wait and see what Jona comes up with before thanking either of us."
    
    return

label chapter2_investigation_shoma:

    scene backgroundsew
    
    "I hate bugging Shoma when he's already so busy. The claustrophobic room is a mess of pins, fabrics, and paper."
    "The machine whines as he fights with a ream of glittery fabric folded multiple times over."
    "Spiderweb thin threads are looped around corners and fraying from what looks like a bedsheet in his hands."
    
    "Somehow, the room smells like a wet dog rolled all over the floor."
    
    sh "Don't you do it." 
    
    "The machine groans a sharp protest and grinds to a halt. He threatens the half finished piece with a pair of scissors."
    
    sh "For the love of God, why must you betray me in my hour of need?" 
    
    "He pops all the pieces open and gives a sharp tug. A tangled mess of thread fights to keep it tied to the machine."
    
    sh "I'm never touching organza again." 
    
    n "Maybe you could use a break?"
    
    "The look he gives me as he cuts the thread is absolutely feral. He relaxes a bit when he realizes it's me."
    
    sh "Yes, a break." 
    
    "He leaves the sewing machine, but not before giving it a warning glare. He reaches under the cooler and tosses me a water bottle."
    
    sh "What's on your mind?" 

label chapter2_investigation_shoma_loop:

    menu:
        "Help with the Party":
            #+Characters helping
            "He gives me a long, hard look."
            
            n "I-I mean, I know you're already doing a lot for the people going, but is there anything you need to get stuff done on time?"
            
            sh "Oh... Now that you mention it, I could use a few things to make the garments more finished."
            sh "I'm having a problem with things fraying. If I could get a lighter and some clear nail polish, that would be a great help."
            
            n "I know Mu has a lighter, and Uitto probably knows who'd have clear nail polish. You sure you don't want an extra set of hands though?"
            
            sh "As much as I'd like to have other people sweat it out with me, I'm afraid teaching amateurs how to sew would take more time than it would save."
            sh "Besides, I have a vision for how things are supposed to go. You know how it is." 
            
            "I do know. Hopefully he can get everything done on time."
            
            jump chapter2_investigation_shoma_loop

        "Show Evidence":
            menu:
                "Nailpolish":
                    
                    n "Do you know which of the girls wears nail polish?"
                    
                    sh "No, but I know Dyre and Kazz will on occasion. I haven't seen them wear pink yet."
                    
                    "He snaps his fingers."
                    
                    sh "Some of the girls wear fake nails made of plastic or resin."
                    sh "You can tell if they're wearing some by the raised edges near the nail beds."
                    
                    jump chapter2_investigation_shoma_loop
                
                "Magazine Clippings":
                    
                    "His eyes widen, mouth agape."
                    
                    sh "Who would do this to an innocent issue of Vogue?!" 
                    
                    n "So it's a fashion magazine?"
                    
                    sh "I'd know that font anywhere. Ugh, most of the stuff in the library is dated, so it has to be something someone brought with them."
                    sh "I imagine the longer we stay here, the more stuff from the outside will become valuable. How could they do this?"
                    
                    "He's more upset then Jona was when he got threatened. Though both of them are more concerned with what was used to make the note than the note itself."
                    "No wonder they get along so well."
                    
                    jump chapter2_investigation_shoma_loop

                "Stolen Sketchbook":
                    
                    sh "I wish I knew where it was. I've offered for Jona some of my drafting paper to use in the meantime but-" 
                    
                    n "It's the wrong kind of paper."
                    
                    sh "Jona draws with such a heavy hand. It's impossible to erase on thin paper without tearing." (16)
                    
                    "Maybe there are imprints left in the sketchbook?"
                    "All the drawings could have been ripped out of if by now, but not many people would think to check the blank pages."
                    "It's a good thing to keep in mind."
                    
                    jump chapter2_investigation_shoma_loop             
        "Motive":
            
            sh "I've personally never had any issues with Jona. I wouldn't let him in the shop if I did."
            
            n "That's fair. Do you know anyone who does?"
            
            sh "If there is anyone, it's probably someone from the upper class rings. Those people have such strange rules for what an 'undesirable' person is."
            
            n "I don't think anyone in our old class was that well-off."
            
            sh "No. If memory serves correct, the rich kids favored colors you'd find in nature."
            sh "Neutrals, golds, pretty much anything you'd find on an apple. We all brought our things from home."
            sh "I'd try asking someone who looks the part."
            
            n "I'll keep that in mind."
            
            jump chapter2_investigation_shoma_loop

        "Leave":
            pass
    
    sh "I should get back to fighting with that thing if I don't want to fall behind."
    
    "It looks mostly finished to me. He drags himself back to his seat and as he sits down, he shrieks."
    
    sh "You rat bastard, you broke my needle!" 
    
    "I should get out of here."
    
    return

label chapter2_investigation_chisei:

    scene backgroundlibrary

    "I find Chisei flipping through old notebooks with a reference book beside her."
    "She sighs, seemingly stumped on what to put on the page. I try not to startle her when I approach the table."
    
    n "You doing okay?"
    
    ch "Hm? Oh, yes, I am fine."
    ch "I figured being this far away from civilization would make it easier for me to write, but I forgot I also have to work on my hand strength."
    ch "The process has been slower than what I am used to. It is quite frustrating."
    
    n "Mind if I ask you some questions?"
    
    ch "By all means."

label chapter2_investigation_chisei_loop:
    menu:
        "Will you go to the dance with me?":
            if chRep >= 2:
                
                ch "Me? Really?" 
                
                n "I mean, that's what these things are for, aren't they? I'm not really sure."
                n "I've never gone to one."
                
                ch "Neither have I." 
                
                "She smiles."
                
                ch "I would love to find out together." 
                
                "YES!"
                
                n "I, er, humbly accept your acceptance."
                
                ch "Naturally."

            else:
                
                ch "As shallow as this may sound, I was hoping someone else would ask me. I might have to do the asking myself." 
                
                n "I see."
                
                "Bummer."
                
                ch "I do appreciate the invitation though." 
                
                n "Yeah, no, I get it."
                
                "It was worth a shot anyway."
                
            jump chapter2_investigation_chisei_loop

        "Help with the Party":
            #+Characters helping
            
            ch "I'm not sure what I could do."
            
            n "We could always use a hand cleaning up."
            
            ch "I'll do my best."
            
            jump chapter2_investigation_chisei_loop
        "Show Evidence":
            menu: 
                "Letters":
                    
                    "She wrinkles her nose."
                    
                    ch "I do not understand how people can overlook such flagrant spelling errors."
                    ch "Perhaps it was easier to miss since it was not handwritten?"
                    
                    "Hiro had trouble noticing too."
                    
                    n "Know anyone that misspells things?"
                    
                    ch "I have not had the pleasure of proofreading for many students."
                    ch "I know Kietsu's mind gets away from him sometimes, and Rei is not much better. Not everyone is a writer, so I try not to judge." 
                    
                    "She perks up a little."
                    
                    ch "Ichita and Setsuna are the only people with a higher grade than me in English."
                    ch "I can't imagine one of them would misspell something by accident."
                    
                    jump chapter2_investigation_chisei_loop

                "Sketchbook Paper":
                    
                    ch "It had fallen off his desk while we were getting ready for class. I pointed it out to him thinking it was something he had dropped."
                    ch "It looked like the paper in his sketchbooks." 
                    
                    n "That's because it was."
                    
                    ch "How unfortunate. There is no place to readily get another. After the riots, I doubt they are sold anymore, unless they get imported." 
                    
                    "I didn't even think of that. There's a good chance he'll spend his entire winter break groping different sketchbooks until he finds an adequate replacement."
                    
                    jump chapter2_investigation_chisei_loop
        "Motive":
            
            ch "This pains me to admit, but in the past I did find Jona's presence... uncomfortable."
            ch "I am all for storytelling, but he seemed to blur the lines between fiction and reality when he rambled on."
            ch "One time, he had written a story about turning into a pterodactyl and putting me in a nest to be eaten." 
            
            "I have a feeling I already know why he did that."
            
            n "When was this?"
            
            ch "Fifth grade."
            
            n "Yeah, he was just fucking with you to talk to someone."
            
            "His life was incredibly dull before we became friends. Making stuff up was one of the few ways he kept himself entertained."
            
            ch "I am more familiar with him now that we share the same class."
            ch "I understand better how isolating it is to try and adjust to unpleasant changes. He has shown an interest in what I am working on these days."
            ch "It is refreshing to share works in progress with someone that thinks there are no bad ideas."
            
            "Right, she wasn't a Vision Major back then. I wonder if other vision majors share the same comradery."
            
            jump chapter2_investigation_chisei_loop

        "Leave":
            pass

    n "What are you writing?"
    
    ch "I do not have the stamina to write anything these days. I am simply editing an old work of mine to get my strength back."
    ch "Usually I would read them out loud to Ichita, but he has been avoiding me lately." 
    
    n "Really?"
    
    ch "Quite a few people have. Are there rumors going around by any chance?" 
    
    n "Not that I can tell. Then again, Uitto doesn't think I'm good at keeping secrets. She might know more than me."
    
    "She bites her lip."
    
    n "She's not talking to you either?"
    
    ch "It is no different from before. I am just noticing it more now."
    
    "I wish there was a way I could help, but I can't get people to like me that much either."
    
    n "I'll see you around."
    
    return

label chapter2_investigation_rei:

    scene backgroundfield
    
    "Things have been a little awkward with Rei since the fight. She still has the earrings Mariko made for her."
    "At least we're at a place where we can agree to disagree."
    
    re "Hey."
    
    "She stops practicing her routine, a little apprehensive about what I want to ask her."
    
    re "I heard about the dance. It's a pretty good idea. A lot of people are looking forward to it."
    
    n "Thanks. Listen, I know you didn't have a lot to do with what Mariko planned, but it's happened again. Someone sent a threat letter to Jona."
    
    re "Are you kidding?!"
    
    "She shakes her head."
    
    re "Listen, I can't say a lot, but I'll try to help if I can."
    
    "Her piercing glimmers as she pulls her hair behind her ear."
    
    re "Other people could get hurt."

label chapter2_investigation_rei_loop:
    menu:
        "Help with the Party":
            #(+Characters helping)
            re "You know, a lot of the girls brought their own stuff from home?"
            re "If we pooled all of our makeup together, I'm sure I could do some really cool stuff with it." 
            
            n "Isn't sharing makeup bad? Like, isn't that a health hazard or something?"
            
            re "Nagen, n there's a safe way to do anything." 
            
            "She thinks a moment longer."
            
            re "Okay, so it's unlikely anyone's brought unused stuff. But it's just one time! I'll be sure to wash the brushes well and maybe Momoko has a way to sterilize stuff."
            re "If there's a pink-eye outbreak, don't look at me." 
            
            n "I think getting stuff up to the roof would be more helpful."
            
            re "I can do both!"
            
            jump chapter2_investigation_rei_loop
        "Show Evidence":
            menu:
                "Nail Polish":
                    
                    re "Ooo, that's such a cute color." 
                    
                    "It looks like the same color Rei is wearing."
                    
                    re "Before I left, my cousin offloaded her entire nail polish collection on me."
                    re "It's been quite handy as a bartering chip now that we're in here."
                    
                    n "Do you remember who borrowed this one?"
                    
                    re "Hmm... I didn't pay the closest attention. Nanase, Rise, and Chisei all took an interest in it. Momoko can never settle on a color too long."
                    re "She's one of the few that has nail polish remover, so she can switch colors whenever she wants."
                    
                    jump chapter2_investigation_rei_loop

                "Red Hair":
                    
                    re "I can't tell if someone was trying to pick it out of the glue or place it there."
                    re "Either could be possible. Someone might have put the polish there on purpose when they couldn't get the hair out." 
                    
                    n "You think one of the guys might have done this?"
                    
                    re "Anything's possible, unfortunately."
                    
                    jump chapter2_investigation_rei_loop

                "Magazine Clippings":
                    
                    re "I saw a lot of people looking through magazines once word about the dance got out."
                    re "I have no idea who this could belong to."
                    re "Sorry, Nagen."
                    
                    jump chapter2_investigation_rei_loop
        "Motive":
            
            n "I know we hid a lot of stuff from you, and Jona said some... tactless things in the hall."
            
            re "We were in the same class for years, I know he didn't mean anything cruel by it."
            re "Honestly, out of all of you, he seems the most set on trying to change." 
            
            "I'm sorry, but what?! Hiro literally turned himself in to prove how sorry he was."
            
            re "Like, all he's done since being here is go to class and draw quietly."
            re "He's pretty much accepted that people hating him is the consequence of doing a shitty thing to his classmates."
            re "I mean, an apology would be nice, but I can tell he's not going to do something that stupid again."
            
            "I guess I'm not in that category."
            
            re "Sorry, I know you're trying too. After Mariko, I'm just a little suspicious of anyone advertising how okay and better they are."

#            if $Ch1IntelEnding 
                #(+Rei, +Mariko)
#               n "I have something for you."
#              "I hand her a note. Mariko wasn't allowed to have anything sharp in her room, so we had to settle for crayons."
#                "I figured she wouldn't believe me if the note was in my handwriting."
#                re "Is she... is this real?" (9)
#                n "Yeah. She made me promise not to tell anyone why she can't come back to class right away, but she's okay."
#                n "She just needs more time before she can get back to things as usual."
#                "I didn't actually read the note."
#                n "What's in it?"
#                re "...if you see her again, tell her she didn't need to ask me out. I already thought we were dating."
#                n "Oh!"
#                re "Honestly, she's so stupid sometimes."
#                n "Yeah, can I get that in writing? There's no way she'll believe me otherwise."
                #[Gained Rei note]
#                jump ReiInterrogation2
#            else:
            
            jump chapter2_investigation_rei_loop

        "Leave":
            pass

    re "I can't believe someone would be stupid enough to go through all of this again. There are so few of us that got to get away from the shelters."
    re "Why would they go and ruin it for everyone else?"
    
    n "What do you mean?"
    
    "It's only Hiro and Jona that have been messed with, to my knowledge."
    re "No one enjoys being around conflict, Nagen. Even if they aren't directly affected, it's still stressful to be around."
    
    re "If people keep acting out, all of us could get sent back. I figured that was like, common sense, but I guess not."
    
    n "I never thought about it that way."
    
    re "I really hope this will go away quietly."
    
    "After what Mariko did, I highly doubt it."
    
    return

label chapter2_investigation_kietsu:

    scene backgroundstuco

    "Papers are strewn about Kietsu's desk. It looks messy, but he clearly has a system."
    "Students have been trying to anonymously sneak in their own suggestions for the dance into the piles."
    "I'm against taking on more than we can handle, but Kietsu's been trying to accommodate as much as he can."
    
    ki "Oh hey, Nagen. You wouldn't happen to know how to make dry ice, would you?"
    
    "Lord have mercy."
    
    n "That's something you'd have to buy. Not sure that's the wisest use of the budget Setsuna gave us."
    
    "Our budget is zero, and so far we've been making it work."

label chapter2_investigation_kietsu_loop:
    menu:
        "Help with the Party":
            #(+Character help)
            ki "What all do you need?"
            
            n "With all the decorations people are bringing, I'm going to need help getting them set up in time."
            n "Would you be able to handle the lighting?"
            
            ki "Yeah, I could string up some lights."
            
            jump chapter2_investigation_kietsu_loop

        "Show Evidence":
            menu: 
                "Note":
                    
                    ki "Man, this is kinda embarrassing' to admit... It's a little hard for me to read this."
                    
                    n "Really?"
                    
                    ki "I think all the different fonts and sizes are throwin' me off."
                    ki "They actually make a special font that's easier for me to read, it's all slanted with wide spacing."
                    ki "Easier to keep track of when the words start and end that way."
                    
                    "Interesting. Hiro might want to look into that."
                    
                    n "It says 'I will strike during the dance'."
                    
                    ki "Spooky. They would've had to make it fairly quick. We didn't want to announce anythin' until all the class reps were on board with the party idea." 
                    
                    jump chapter2_investigation_kietsu_loop

                "Sketchbook Paper":
                    
                    ki "I haven't seen anyone drawin' stuff. I guess that's not the only thing it could be used for."
                    ki "I just don't really pay attention to what other people are doin'." 
                    
                    n "You got enough on your plate anyway."
                    
                    ki "We both do. Have you tried talkin' with the teachers about this?" 
                    
                    "I really don't want to go back to Vivaldi's office. I barely dodged getting in trouble the last time."
                    
                    n "What could they do?"
                    
                    ki "They could do room searches. It's what we did at my old school." 
                    
                    n "I think that would just get everyone mad at me."
                    
                    ki "Suit yourself." 
                    
                    jump chapter2_investigation_kietsu_loop

                "Red Hair":
                    
                    ki "Maybe it's animal hair? Those things get everywhere. Taiga brought a bunch of critters."
                    
                    "I haven't seen what his other rabbits look like."
                    
                    n "If so, it could be from anyone that's gone in his dorm."
                    
                    "I'll have to confirm for myself before I jump to conclusions."
                    
                    jump chapter2_investigation_kietsu_loop
        "Motive":
            
            ki "Everyone here has so much history with each other. I've never been so thankful to not know anyone."
            
            n "The classes in Estella were really insular, so it was easy for people to have an us versus them mentality."
            
            ki "I can tell."
            
            n "Have you heard anyone saying bad things about Jona?"
            
            ki "Vision Majors try to get along, even if we don't 'like' each other. The most I've heard is people bein' irritated that he shows up late to class."
            ki "Though if somethin' of his was stolen, that explains why he was buggin' out."
            
            n "We think it was taken when Mariko attacked Hiro."
            
            ki "If he left it somewhere, anyone could've taken it." 
            
            jump chapter2_investigation_kietsu_loop

        "Leave":
            pass

    
    ki "There has to be some way to put fog on the dancefloor. Or maybe bubbles?"
    
    n "Anything with soap could make someone fall."
    
    ki "I guess so. Can't have anyone slidin' off the roof now, can we? I'll have to sit on that one a bit longer before throwin' in the towel."
    ki "It's a good thing to keep in mind for next year."
    
    "Anything we want to buy, we'll have to use more than once or Setsuna will kill us. Guess I should try somewhere else."

label chapter2_investigation_yoku:

    scene backgroundcafe
    
    "I've never seen someone stare so intently at a menu before. He's scanning the coffee offerings like a man deciphering hieroglyphics."
    
    y "I don't suppose you could explain what the difference between a mocha latte and a latte with mocha sauce is, could you?" 
    
    "I look and sure enough, it's on the menu twice for some reason."
    
    n "I mean, if what you want is something full of sugar, I'd go with the mocha latte. If it's more expensive, it's gotta have more of something in it."
    
    y "That's a fair point. Perhaps the number of pumps is the difference. If you get the other one, we could compare." 
    
    "Why do I have to buy one too? ...damn it, now I'm curious."
    
    n "Fine."
    
    "It'll be easier to ask him questions if we're both waiting for our drinks to cool anyway."

label chapter2_investigation_yoku_loop:

    menu:
        "Will you go to the dance with me?":
            if YokuRep >= 2:
                
                "He has no readable expression. I snap my fingers a bit to see if I can pull him out of his head."
                
                n "It's an easy question to answer. It's either yes or no."
                
                y "I'm just a little shocked is all. Are you sure that's what you want? People have been desperate for something to talk about."
                
                n "I don't care. It's just a dance, it'll be fun."
                
                y "Yes, fun." 
                
                "He takes a sip of coffee."
                
                y "Might as well."

            else:
                
                y "You must be joking." 
                
                n "No, I was just asking-"
                
                y "I would never lower myself to be seen arm in arm with the likes of you."
                
                "Ow. A simple no would have been fine."
                
            jump chapter2_investigation_yoku_loop

        "Help with the Party":
            # +Characters helping
            y "You want my help?" 
            
            n "You're the music guy, aren't you?"
            
            y "I figured for a party type setting, you'd prefer Kazz and his little drum machines."
            
            n "Kazz can DJ all he wants, but I'd feel more comfortable with a concrete set list. That way we could know when things were wrapping up."
            
            y "I would be more than happy to throw my hat in the ring then."
        
            jump chapter2_investigation_yoku_loop

        "Show Evidence":
            menu:
                "Magazine Clippings":
                    
                    y "Well, someone fancies themselves intimidating. Though a ransom note typically works best when you have something to ransom."
                    
                    n "Like a stolen book?"
                    
                    y "Ah, maybe that's it. I know you've been drawn out to a school yard brawl in the past, but this seems to have nothing to do with you."
                    y "It may just be in Jona's best interest not to go to the dance. There could be a bucket of trash waiting to get dunked on his head."
                    
                    n "I just want to be cautious."
                    
                    "After last time, I don't trust the 'it's just bullying' defense."
                    
                    jump chapter2_investigation_yoku_loop

                "Location of Note":
                    
                    y "Interesting they should mention the dance specifically."
                    
                    n "What do you mean?"
                    
                    y "Well, this was found after we had our meeting. Surely news doesn't cycle around that quickly."
                    y "All of us were sworn to secrecy until we could confirm that the idea had been greenlit."
                    y "I doubt anyone could have heard about it, made this, and snuck it into the Vision classroom in the short amount of time between the meeting and class."
                    
                    "So either they were in the Vision class, or they knew beforehand."
                    
                    n "Who all knew about the dance?"
                    
                    y "Use your head, Nagen. You were at the meeting just as I was."
                    
                    jump chapter2_investigation_yoku_loop

        "Motive":
            
            y "Jona's family was part of the upper echelon before my family arrived."
            y "My guess is that we were their replacements, though we did enter at the bottom of the food chain."
            
            n "So you benefit from him being where he is?"
            
            y "It's more that I don't have to think about him at all. After school, our lives will never cross paths again."
            
            jump chapter2_investigation_yoku_loop

        "Leave":
            pass

    y "Let me try your coffee."
    
    "He seems to debate which part of the cup to drink from before making a decision and taking a sip."
    
    y "...I can't tell the difference." 
    
    "He pushes his cup my way. I try it. I'm no gourmand, but it tastes exactly the same."
    
    n "I think you paid extra for no reason."
    
    y "I should have trusted my instincts. It's serviceable at least." 
    
    "I leave a little poorer and wiser."
    
    return

label chapter2_investigation_setsuna:
    
    scene backgroundcourtyard
    
    s "How's it going?"
    
    n "You know how it's going."
    
    s "Aww, don't be such a little baby. This is like, your one chance to prove you're competent."
    s "I've been dying to see how you do."
    
    n "I'm sure you are."
    
    "Last time, she was directly involved with what was going on."
    
    n "If someone was trying to screw us over, you'd tell me right?"
    
    s "Depends on what you expect me to tell."

label chapter2_investigation_setsuna_loop:

    menu:
        "Help with the Party":
            # + Characters helping
            s "I already am."
            
            n "But-"
            
            s "Nagen, do you want this thing to balloon even more out of control?"
            
            "Definitely not."
            
            s "Then my job is to keep everyone's 'great' ideas off of Kietsu's desk."
            s "I swear to God, all of you are trying so hard to be liked that you're overworking yourselves."
            s "It's only been a few weeks."
            
            jump chapter2_investigation_setsuna_loop

        "Show Evidence":
            menu:
                "Red Hair":
                    
                    s "The only people I can think of with red hair are guys and maybe Rei, but it's too short to be her hair."
                    s "Then again, maybe someone close to them framed the red head. You remember how hard someone tried to make Kazz and Mu look bad."
                    
                    n "Yeah, but who'd be able to get a hair without noticing?"
                    
                    "She looked down at her sweatshirt and pulled one of her own blond hairs that got shoved through the fibers."
                    
                    s "Usually happens in the wash. I'm sure everyone's washed their clothes by now."
                    
                    "So they may not have felt it taken off them. A lot of people wear sweatshirts, though."
                    
                    jump chapter2_investigation_setsuna_loop

                "Nail Polish":
                    
                    s "I can't stand the stuff. It's nice for like, one day and then it gets all messed up."
                    s "Even if you try to patch it up, there'll be a dent."
                    
                    n "So if this happened to someone's nails, you'd be able to tell?"
                    
                    s "Maybe. It'll either be patched up or redone entirely." 
                    
                    jump chapter2_investigation_setsuna_loop

                "Magazine Cippings":
                    
                    s "Ichita's a dead man if these are what I think they are."
                    
                    n "You know what magazines they are?"
                    
                    s "I recognize the O. He was borrowing them from someone, that's all I know."
                    
                    jump chapter2_investigation_setsuna_loop

        "Motive":
            
            s "If some big dramatic confrontation happens during the dance, that is going to be a ton of paperwork for Nanase and a pain in my ass."
            s "Why would anyone in the student council gamble what little good will we gained from the student body over some guy we don't know?" 
            
            n "Right, you and Kietsu never went to Estella."
            
            s "And Nanase barely remembers you were one of the guys responsible for the riots. Or at the very least, she doesn't care."
            
            n "Have you heard anyone say they don't like him?"
            
            "She thinks a bit."
            
            s "A lot of people in the Charm course know of him. I'm not sure if they've made the connection they were told not to like him."
            
            n "What do you mean?"
            
            s "He pushes people away and he doesn't compromise. You might not have seen it since he's your friend, but trust me, it's a huge issue."
            
            "So Charm Majors might not like him. Good to know."
            
            jump chapter2_investigation_setsuna_loop

        "Leave":
            pass

    s "I'm disappointed, I thought you were going to ask about something else." 
    
    n "Like what?"
    
    s "Like the fact that anyone pierced by Mariko isn't allowed to take them out."
    
    n "Wait a minute, what do you mean?"
    
    s "With new piercings, you can't take them out or the wound will heal. You're supposed to rotate them though and mine haven't been."
    s "The nurse told me to have Mr. Yaguchi take a look at them."
    
    n "Isn't he, like, a tech guy?"
    
    s "Yeah. Something was in them. He told me he 'turned them off' but not to take them out."
    s "I've done some digging, but no one else has gotten new piercings, so I don't think it'll happen again."
    s "It is curious. If Mariko had something that could control someone's nervous system, why'd she give it to us and not you guys?"
    s "It would have been easier to capture you then."
    
    n "Were you being controlled during the fight?"
    
    s "Yeah. I get why everyone's freaked out about it. Poor Rei can't catch a break. It happened to her twice, and from a friend each time."
    
    n "I didn't know an education device could be that small."
    
    "The hardware needed for ours required full helmets and other types of equipment. I can't imagine how any of that could fit into a stud."
    
    s "You're not the only one who makes stuff. Well, later, Nagen. Unlike you, I'm busy with other things."
    
    return

label chapter2_investigation_nanase:

    scene backgroundroof
    
    "Nanase is busy getting the dimensions for the roof. In her little notebook is a list of all the outlets and a map of the walkable areas."
    
    nk "Goodness, you startled me!"
    
    
    n "Sorry, I just had to ask you a couple of questions."

label chapter2_investigation_nanase_loop:
    
    menu:
        "Will you go to the dance with me?":
            if nkRep >= 2:
                
                nk "Yes!"
                
                "She's so excited."
                
                nk "Oh my goodness, we're going to have so much fun. Are any of your other friends bringing dates?"
                
                n "I think it's just us."
                
                "Hiro has no problem going stag. Finding a date is probably the last thing on Jona or Uitto's minds."
                
                nk "Oh well. It'll be just us."
                
            else:
                
                nk "I'd love to, but I'm on door duty, remember?"
                
                "Right, she volunteered to take tickets. We already don't have enough people to manage what we have planned."
                
                nk "You should ask someone who has time to enjoy the whole dance with you."
                
                "She looks disappointed. That makes both of us."

            jump chapter2_investigation_nanase_loop

        "Help with the Party":
            # +Characters Helping
            nk "Oh dear, what are we forgetting?"
            
            n "A chaperone."
            
            nk "Goodness, you're right. We may have gotten permission to be on campus after hours, but we haven't asked any of the teachers to lend a hand."
            
            n "Would you be able to ask Ms. Sato to do it?"
            
            nk "Wouldn't Professor Inukai be more lax?"
            
            n "At the first school event? I think he'd try too hard to follow the rules."
            n "I imagine that late at night, Ms. Sato would be happy to sit in her chair while we all do our thing."
            
            nk "Excellent point. I'll draft a proposal once I'm done here." 
            
            jump chapter2_investigation_nanase_loop

        "Show Evidence":
            menu:
                "Nail Polish":
                    
                    nk "I almost used that one. It's the most popular color from Rei's collection."
                    nk "I wanted to see what Shoma did with my mom's old dress before picking a color."
                    
                    n "You're not having him make something new?"
                    
                    nk "He's already overworked as it is."
                    
                    n "That's fair. Do you know who's used it?"
                    
                    nk "No, sorry."
                    
                    jump chapter2_investigation_nanase_loop

                "Magazine Clippings":
                    
                    nk "Scrapbooking glue."
                    
                    "She narrows her eyes."
                    
                    n "Not a fan of the hobby?"
                    
                    nk "I guess not? It's so strange. As soon as I smelled it, it felt like the room was crowded."
                    nk "I can only imagine how much of a mess that would cause, all the little bits of paper and useless stuff sitting in piles."
                    
                    "She does seem to like to keep things neat and tidy."
                    
                    nk "Then again, I'm not a fan of clutter in general."
                    
                    jump chapter2_investigation_nanase_loop

                "Sketchbook Paper":
                    
                    nk "So it belongs to Jona."
                    
                    n "You've seen it before?"
                    
                    nk "Kind of. Would you hold on a second?"
                    
                    "She left to go riffle through her backpack."
                    
                    nk "This is made by the same company."
                    
                    "She hands me a hardcover book with blank pages." 
                    
                    #(+New Sketchbook)
                    
                    nk "I thought it was going to be like a journal. I don't like writing in things without lines."
                    
                    "There are a few attempts with slanted handwriting so small that I could barely read it."
                    
                    nk "He can have it if it'll work as a replacement."
                    
                    n "Are you serious?" 
                    
                    "I know the guy hates hardbound sketchbooks, but it's better than nothing."
                    
                    nk "It would feel wrong throwing away something I barely used. I'd rather it go to someone who needs it."
                    
                    n "Thank you so much."

                    jump chapter2_investigation_nanase_loop
        "Motive":
            
            nk "I've heard a few people say he deserves this. It's so despicable. I don't see how this kind of retribution helps anyone."
            
            n "Who's been saying that?"
            
            nk "Dyre mostly."
            
            "No surprises there."
            
            nk "Even Rise and Yoku agree. They mentioned some kind of cult."
            
            n "This isn't the first time Jona has had his art stolen."
            n "Last time it was for this doomsday cult that hated Vision Majors. Seeing how he is one, that was clearly not what he intended with it."
            
            nk "That's terrible."
            
            jump chapter2_investigation_nanase_loop

        "Leave":
            pass

    n "So, do we have enough space?"
    
    nk "It'll be a little tight. If we can find some more extension cords, we can move the DJ booth over here and then the snacks could go there."
    
    "Her plans sounds more confusing than a football play, but I'll take her word for it."
    
    return

label chapter2_investigation_momoko:
    
    scene backgroundlab
    
    "The lab is covered in hair. Different colored wefts are drip drying on the counter top. The smell is atrocious."
    "Somewhere between vinegar and rotten chicken."
    
    n "Momoko?"
    
    "She's wearing one of Jona's spare masks. At least she's not breathing in the stuff. My eyes water as I motion for her to come into the hall."
    "She follows me out and rips off the mask. Red angry marks line where it had been strapped down. She must've been working in there for a while."
    
    scene backgroundhall1
    
    n "Sorry, I just needed to talk to you real quick."
    
    mh "You're good, the drying stage is the most boring part.  How can I help you?"

label chapter2_investigation_momoko_loop:
    menu:
        "Will you go to the dance with me?":
            if mhRep <= 2:
                
                mh "I wasn't planning on staying that long. My outfit's kinda complicated and I haven't had a chance to give it a test spin."
                mh "If one seam breaks, I'm booking it. I can't have a date slowing me down."
                
                n "Oh, okay."
            else:
                
                mh "Wait, are you for real?"
                
                n "Yeah. Is that a problem?"
                
                mh "What? No. I just- wow. Not a lot of girls are going to have dates to this thing. Does that make me popular now? The world is such a weird place."
                
                "She squints at nothing in particular. It's a good question, though. Our class is so small that we're the ones who get to decide what makes someone cool."
                "Though, I'm not sure if having a date would matter all that much."
                
                mh "But, yeah... Yeah! This is going to be so much fun."
                
            jump chapter2_investigation_momoko_loop

        "Help with the Party":
            
            mh "What do you need?"
            
            n "Stuco has set up covered, but we could use help cleaning it up once everyone's done."
            n "A lot of people are lending us stuff, and I don't want it to get lost or ruined."
            
            mh "Sure, we can keep it in the lab. That way we can lock the door and head to bed. People can come get their things in the morning."
            
            "Everything will stink, but it's better than nothing."
            
            n "Awesome, thank you so much."
            
            jump chapter2_investigation_momoko_loop
        "Show Evidence":
            menu:
                "Nail Polish":
                    
                    mh "Looks cheap."
                    mh "Not to be rude or anything, it's just that good stuff wouldn't crack or goo up like this unless the person was stupid enough to use glue right after doing their nails."
                    mh "It takes a good couple hours for that third coat to dry. It's why I never use the stuff."
                    mh "As soon as the surface dries, I feel comfortable to start doing things and then BAM there's a crease I can't buff out."
                    
                    n "If someone was in a hurry, they might have thought the same thing."
                    
                    "There wasn't a lot of time between the announcement of the dance and the note showing up."
                    
                    jump chapter2_investigation_momoko_loop

                "Red Hair":
                    
                    n "You've been doing a lot of wigs and stuff. Has anyone asked for red hair?"
                    
                    mh "Haha! I can see why you'd think to ask me, but nope. Reds are super easy to make."
                    mh "If you get the right mud, you can tint hair red. I've been playing with blues and purples."
                    mh "It's really hard to get those richer cool colors to stick."
                    
                    n "Do we have mud like that here?"
                    
                    mh "You know what, there are microscopes in the lab. I could pop it on a slide and see if it's dyed."
                    
                    n "Really?!"
                    
                    mh "Synthetic dye damages the layers of the hair, and natural dyes don't penetrate down to the hair shaft."
                    mh "And of course, you can see the natural roots better on a microscopic level. If it's natural, it'll be nice and scaly looking."
                    
                    "She takes the hair and enters the lab. After a bit, she comes back out."
                    
                    mh "Yep, it's natural."
                    
                    n "You really should've put your mask back on before going in there."
                    
                    jump chapter2_investigation_momoko_loop

                "Magazine Clippings":
                    
                    mh "Question for you, Nagen. Did anyone know this was going to happen before your student council meeting?"
                    
                    n "No, why?"
                    
                    mh "It's just- maybe this is the procrastinator in me, but these letters look too well cut."
                    mh "If I was throwing something together in a hurry, I wouldn't be stressed about making perfect squares."
                    
                    "That's a good point. Maybe some of these letters were cut out in advance."
                    
                    jump chapter2_investigation_momoko_loop
        "Motive":
            
            "Momoko's borrowing stuff from Jona, but that didn't stop people from turning on Kazz."
            
            n "What's your relationship with Jona?"
            
            mh "We're friends, I guess. Not close friends like you guys are but..."
            mh "I think he can tell when people are sad. He used to sit next to me a lot when I was going through a rough time."
            mh "He used to talk a lot about becoming a Karmic Gladiator one day, then just sort of stopped. He hasn't checked in on me as much now that I'm better."
            
            n "Better from what?"
            
            "She bites her lip. Maybe that was too invasive of a question."
            
            mh "Sometimes people feel better about themselves when picking on a weak target. I hate that thinking like that has followed us here."

            jump chapter2_investigation_momoko_loop

        "Leave":
            pass
    
    n "Did you leave a light on?"
    
    "Something's flickering in the window."
    
    mh "Crap!"
    
    "She opens the door. Smoke rolls out of the office. She grabs a flaming bit of hair and douses it in the sink."
    "Not quickly enough to avoid setting off the fire alarm."
    "The sprinklers drench everything; dye is bleeding into one another, painting bright streaks along the counter and floor."
    
    mh "Crap!"
    
    n "I'll get Mr. Yaguichi."
    
    "After the mess is cleaned up, we're given a stern lecture about not turning our backs on active chemicals."
    
    return


label chapter2_investigation_kazz:

    scene backgroundavroom

    "Ever since the incident, Kazz has guarded the PA booth like a hawk. The key never leaves his belt loop. He's like a very dorkily dressed janitor."
    "He's letting me in for the moment, but I can tell I'm being watched."
    
    kk "So someone else has had their stuff stolen now. That's so twisted. It wasn't like he made a big deal about drawing in class, he was being quiet." (1)
    
    n "Yeah. That paired with the threat letter he got afterwards falls into the pattern of what happened last week."
    
    kk "Bummers all around. And I was so hyped for the party too." (2)
    
    "He's the only person who still thinks of it as just a party. It's a small distinction, but I'm happy some people are keeping their expectations low."
    
    kk "I've had my nose to the grindstone with other things, so I'm not sure how much help I can be." (3)

label chapter2_investigation_kazz_loop:

    menu:
        "Help with the Party":
            # + Characters helping
            
            n "We need a DJ."
            
            "His eyes light up."
            
            kk "You want me to spin for the party?"
            
            n "That's your thing, right? The thing you want to do?"
            
            kk "Well, yeah, but I've never mixed live before."
            
            "How hard is it to pick a bunch of songs and make sure it plays? Even if he has no experience, I can't see him messing up. "
            
            kk "Hell yeah I'll help out! This is going to be so much fun."
            
            jump chapter2_investigation_kazz_loop

        "Show Evidence":
            menu:
                "Red Hair":
                    
                    kk "Ew. You've been toting that around all day, bro?" 
                    
                    n "It's just hair."
                    
                    kk "It's still a piece of a person."
                    
                    "He wrinkles his nose."
                    
                    kk "Still, if it was left there, it's probably for a reason. You can pick something like that out with enough determination."
                    kk "The paint, not so much."
                    
                    jump chapter2_investigation_kazz_loop

                "Location of Note":
                    
                    kk "I've been keeping a closer eye on who can go where now, for obvious reasons."
                    kk "Anyone student council or student council adjacent can enter the classrooms whenever they want. At least, whenever Mr. Yaguichi's on campus."
                    
                    n "You think he saw something?"
                    
                    kk "Maybe, but you've seen how often that guy looks up from his work. If he had solid evidence, someone would be in trouble by now."
                    
                    "He has a point. I've seen him soldering more than I've seen him watching students."
                    
                    kk "It's a panopticon. The idea that someone might be watching is enough to deter most people from acting out."
                    kk "I wonder if the person that did this had a way of knowing when he was watching."
                    
                    n "How could they do that?"
                    
                    kk "I don't know. It's either that or they have brass balls and don't care about getting caught."
                    
                    jump chapter2_investigation_kazz_loop

                "Magazine Clippings":
                    
                    kk "That's one dedicated stalker. Not that Mariko wasn't hauling ass, but this kind of thing takes time to put together."
                    kk "They must really hate the guy."
                    
                    n "Yeah, but so far, I haven't had too many people admit to not liking him."
                    
                    kk "Well, you're his friend. I'm sure Uitto hasn't heard any of the rumors floating around the Charm department either."
                    
                    n "What rumors?"
                    
                    kk "That he's faking his proficiency."
                    kk "Some people have been wondering if he's actually proficient in something like lying or manipulation and is covering it up with spooky stuff to seem cool."
                    
                    n "Where'd you hear that from?"
                    
                    kk "Dyre." 
                    
                    jump chapter2_investigation_kazz_loop
        "Motive":
            
            kk "I've been trying to keep things as chill as possible on my end. The first week of school sucked. Real bummer it's happening again.A"
            kk "nd Mariko's off who knows where, so it has to be somebody else, right?"
            
            n "That's what it seems like."
            
            kk "Major buzzkill. I can't say I've ever gone out of my way to interact with Jona; he always avoided me. I have zero clue what would make someone do this."
            
            "That might be my fault. I wasn't exactly subtle about why I was transferred to the at risk class, or the people who failed to follow me there."
            
            jump chapter2_investigation_kazz_loop

        "Leave":
            pass

    kk "Is there anything else I can help with?" (20)
    
    n "Nothing comes to mind."
    
    "Wait, why is he so eager to help? "
    
    n "What are you procrastinating on?"
    
    kk "Ugh, busted. Kitsune wants me to redo the entire album we made since my stuff got confiscated. The first time we did it, she was just hyped to finally record. Now she's got standards, and I'm afraid neither of us is skilled enough to meet them. I've retooled the same bridge three times, and she's still not happy with it." (21)
    
    n "Try telling her you're going for authenticity."
    
    kk "Dude, that's genius." (22)
    
    n "Also, no one else is making new stuff at the school right now. It could be a six out of ten, and people would still like it."
    
    kk "I'm not sure about that. This beast isn't for everyone." (23)
    
    "He looks back at all the editing he has to do."
    
    kk "Alright, I gotta kick you out or I'll keep dragging my feet on this last round of edits." (24)
    
    n "You got this."
    
    return

label chapter2_investigation_dyre:

    scene backgroundlibrary

    "Dyre is sitting at a table, surrounded by piles of books. The covers have pictures of brains on them or bland white textbook covers."
    "Lots of stuff on brain injuries and personality disorders. He seems kind of frustrated, but then he sees me and puts on that smarmy mask of his."
    
    d "To what do I owe the pleasure?"
    
    n "I think you know what. Someone stole Jona's sketchbook and of everyone here, you're the only one that's tried to pull pranks on people."
    
    d "Nagen, I'm no monster. I only jest with people who I know can hang. You haven't been in on the joke in years."
    
    n "I certainly don't find this funny. Last time you had an idea of who was harassing us and you chose to say nothing. I'm guessing you have some ideas again."
    
    d "Alright, I'll bite. What do you want to know?"

label chapter2_investigation_dyre_loop:

    menu:

        "Help with the Party":

            # + Characters helping
            
            d "Sure, I guess. What do you need?"
            
            n "Trash. There's going to be so much trash when we're done. If you could take the bags to the dumpster, that would be great."
            
            d "Hardly a glamorous job."
            
            n "That's why no one wants to do it."
            
            d "Alright. At least it's easy." 
            
            jump chapter2_investigation_dyre_loop

        "Show Evidence":
            menu:
                "Magazine Clippings":
                    
                    d "I've seen a lot of people looking at stuff like that."
                    d "Chisei especially, she likes to have references when writing set descriptions."
                    d "I don't see her cutting one up anytime soon. Whoever did this probably owned them."
                    
                    n "You think?" 
                    
                    d "If it was stolen, we would have heard about it, like with Jona and Kazz's stuff."
                    d "If it was borrowed, the borrower would get caught as soon as the magazines were given back."
                    d "If you can find out who was lending them out, you'll be golden."
                    
                    jump chapter2_investigation_dyre_loop

                "Nail Polish":
                    
                    d "The note is misspelled. Hard to say they caught it when all the nail goop is up by the hair instead."
                    d "Doesn't look like the letters were moved around at all after they were placed."
                    d "I wouldn't be surprised if the person laying them down thought of them more as pictures than letters."
                    
                    n "So someone artistic?"
                    
                    d "Depends on what you consider artistic."
                    d "I know artists usually have bad handwriting, but there are other things they could have used to make this if art was their thing."
                    
                    jump chapter2_investigation_dyre_loop

                "Red Hair":
                    
                    d "It isn't mine. I know it looks like I spend hours in the mirror, but that's to try and straighten my hair, not the other way around."
                    d "Whoever's hair that is, it's naturally straight."
                    d "Rather than focusing on that, it's really weird how vague the note is. Mariko had a set deadline, but this is open ended and can be interpreted several ways."
                    
                    n "Or they didn't know when exactly the dance was happening."
                    
                    d "Also a possibility. I'm guessing they know how you think."
                    
                    jump chapter2_investigation_dyre_loop

        "Motive":
            
            d "People in the Charm department have had an issue with him and his family for years."
            d "I'm sure you remember this, but his mom wasn't the nicest person when it came to him. She made it everyone's problem when the school tried to classify him as a Charm Major at first."
            
            n "That's news to me."
            
            d "Well, Charm Proficiencies can get grandfathered down. Kinda like a peer reviewed ability, but his mom refused to believe he had her ability."
            d "Kept accusing the staff of trying to curse him. They never could prove one way or another which class he should've been in."
            d "Though I'm sure if you ask him, he'll double down on being a vision major."
            
            n "That's 'cause he is."
            
            "He's got the emotional intelligence of a shoe. Most of the time, he's guessing what to do based on auras, but it's not like he has a mood ring guide. "
            
            d "Or he could be lying to himself. You'd be surprised what people can convince themselves of when the alternative is violent rejection."
            
            "He shrugs."
            
            d "It doesn't matter if you think it's true, what matters is that other Charm Majors think it's true."
            
            jump chapter2_investigation_dyre_loop

        "Leave":
            pass

    "That was surprisingly helpful."
    
    n "Thanks."
    
    d "What for?"
    
    n "For actually answering my questions."
    
    d "I have no horse in this race. Forgive me for being a little defensive of my friend when the last time you took issue with someone, they woke up in a war zone."

    if Hero > Villain:

        d "It seems you learned your lesson."

    else:

        d "You haven't exactly been acting like someone who won't do it again."
    
    n "Either way, I appreciate it."
    
    d "Yeah, whatever."
    
    "I leave him to his pile of books."
    
    return

label chapter2_investigation_kitsune:

    scene backgroundstage

    "Kitsune is standing on stage holding a tiny thing up to the stage lights. She tilts and rotates it around with a grim expression."
    
    k "Does this look like a rhinestone to you?"
    
    n "It looks like a gem."
    
    k "We don't have any, so I'm trying to make due with glue and candy wrappers. The glass ended up being too heavy. It's better than nothing at least."
    
    "There are a few other rejected attempts in her pocket. A couple of masks are sitting in the wings."
    "It seems anything she's thinking about wearing at the dance, she's brought to see how it would look on stage." 
    
    n "You're taking this dance really seriously." 
    
    k "Of course! I'd like to keep doing fun things like this, but it only works if everyone's on board. You all have been working so hard, it only makes sense we should too."

label chapter2_investigation_kitsune_loop:
    menu:
        "Will you go to the dance with me?":

            k "Get out of here."
            
            n "I'm sorry?"
            
            k "No! I mean, like, you're serious. Like, for real, for real? You want to go to the dance with me?"
            
            n "Is that a problem?"
            
            k "Are you kidding? Broody bad boys were like, in before the world went to shit."
            k "Being the only femme there with a date would totally show everyone who's actual prom queen material."
            
            "I feel like we're getting off topic."
            
            n "Is that a yes?"
            
            k "Um, yeah. Of course it's a yes. My dress is based on a white peacock, dress accordingly."
            
            # kdate = true, date = true, 
            jump chapter2_investigation_kitsune_loop

        "Help with the Party":
            # + Characters helping
            k "I'll be spending a lot of time getting ready beforehand. Is there anything I could do after?"
            
            "I'm surprised she didn't ask to sing."
            
            n "We'll have a bunch of dishes that'll need to be brought back to the cafe. Think you can manage it?"
            
            k "Of course."

            jump chapter2_investigation_kitsune_loop

        "Show Evidence":
            menu:
                "Sketchbook Paper":
                    
                    k "Who cares about that?"
                    
                    n "Well, Jona does-"
                    
                    k "Hasn't Ichita been acting super weird lately? He's all secretive and scheme-y and he won't tell me anything, called me a blabber mouth."
                    k "Me? A blabber mouth? Can you imagine?!"
                    
                    "Quite easily."
                    
                    k "I think he's up to something. I caught him whispering stuff to Uitto and they stopped talking as soon as they saw me."
                    
                    "Well, if Uitto's involved, they're definitely not going to tell you anything." 
                    
                    jump chapter2_investigation_kitsune_loop

                "Nail Polish":
                    
                    k "This is why all my colors are plastic."
                    
                    "She drills her fake nails against each other."
                    
                    k "That's a pretty popular color right now. Rise, Rei and Chisei all wanted to wear it."
                    k "Speaking of Chisei, have you noticed everyone's been avoiding her lately?"
                    
                    n "What?"
                    
                    k "All the girls have been whispering behind her back. It's absolutely awful to watch. Be extra nice when you see her next."
                    k "She doesn't want to go to any of the teachers about it. After the incident with Mariko, she's worried about 'overstating harm'."
                    k "But I get it, there's not much the teachers can do to make people include her."
                    
                    jump chapter2_investigation_kitsune_loop

                "Magazine Clippings":
                    
                    k "That's interesting."
                    
                    "She reaches into her backpack and pulls out a fashion magazine with a green cover."
                    
                    k "Look familiar?" 
                    
                    n "Where did you get that?"
                    
                    k "All of us with any taste pooled our collection together so everyone could look over references for the dance."
                    k "I didn't include this one, because there were already duplicates. Whoever cut that up knew it wasn't the only copy, I guarantee it."
                    
                    n "Who else was pooling magazines together?"
                    
                    k "Shoma and I, obviously. Momoko had a few, Rise and Rei as well, and Jona actually."
                    
                    n "That's odd."
                    
                    k "Kind of calculated if you ask me. As far as I could tell, it was a fun time seeing what everyone managed to fit in their suitcase."
                    k "It kind of retroactively spoils it if he recognized the pieces like I did."
                    
                    jump chapter2_investigation_kitsune_loop
        "Motive":
            
            k "Ew, why would I go anywhere near that lice factory?"
            
            "I didn't realize that was common knowledge. When we were kids, his mom didn't take any of his concerns seriously."
            "She put him scratching in the same category as crying over shirt tags. That was one of the grosser things Hiro and I had to teach him about."
            
            n "That was when we were ten."
            
            "She went silent."
            
            k "My point is, I don't think about him, period. I've got my own things I'm working on."
            
            jump chapter2_investigation_kitsune_loop

        "Leave":
            pass

    k "I can't wait until we can buy stuff again. My fosters keep sending me allowance and I have nothing to spend it on." (23)
    
    n "You get an allowance?!"
    
    k "Yeah... is that not normal?" (24)
    
    n "For foster parents, no."
    
    k "Well, it's all going to Shoma as soon as we can buy fabric. I should probably keep that to myself, hunh?" (25)
    
    n "I would."
    
    "No one gets to know how much this jacket cost."
    "It's the only birthday present I've gotten, and even that's just because Maimai was overcompensating for the whole getting arrested thing."
    
    return

label chapter2_investigation_taiga:
    
    scene backgroundamp
    
    "Taiga is lying on the grass without a care in the world. He looks like he might be asleep."
    "I approach carefully when a furry head pops up and looks at me."
    
    t "What is it?"
    
    "He turns over to look at me."
    
    t "Oh, hey. What are you doing out here? I figured you'd be working your tail off corralling people into volunteering."
    
    n "Well, I am doing that. Though I'm mostly looking into who's responsible for what happened to Jona."
    
    t "Walked into that one. Alright, shoot."

label chapter2_investigation_taiga_loop:
    menu:
        "Will you do to the dance with me?":
            if tRep >= 2:

                "A huge dopey grin spreads across his face."
                
                n "What?"
                
                "He keeps grinning at me."
                
                n "What?"
                
                t "You like me."
                
                "I did not come here to get teased."
                
                n "Is that a yes or a no?"
                
                t "Sure."

            else:
                
                t "No."
                
                "Well, that was crystal clear."
                
                t "Don't take it personally, I just don't plan on sticking around Guwon."
                t "I'll be out of here soon enough."
                
            jump chapter2_investigation_taiga_loop

        "Help with the Party":
            #+ Characters helping
            n "We have a bunch of tickets and things that need to be cut out. Would you be able to help out with that?"
            
            t "Sounds easy enough." (4)
            
            "He's not exactly thrilled, but at least he's helping."
            
            jump chapter2_investigation_taiga_loop

        "Show Evidence":
            menu:
                "Magazine Clippings":
                    
                    t "Hunh, I might've actually seen something."
                    
                    "He sits all the way up."
                    
                    t "Rise was carrying a stack of magazines exactly like this. She said it was for the party, so I didn't think much of it."
                    
                    n "Were any of them cut up?"
                    
                    t "Most of them were. She had a bunch of binders with her too."
                    
                    "I'll have to talk to her more about that."
                    
                    jump chapter2_investigation_taiga_loop

                "Nail Polish":
                    
                    t "I don't wear any. It's not a good idea to have anything that chips when taking care of animals."
                    t "The bunnies are nice, but they like to nibble."
                    
                    n "Do you know anyone who does?"
                    
                    t "I don't know. Girls, I guess."
                    
                    jump chapter2_investigation_taiga_loop

                "Location of Note":
                    
                    t "Why didn't they put it in his locker?"
                    
                    n "Maybe because more people might have seen it."
                    
                    t "Not if they did it at night. Guess that means they did it during the day and no one noticed."
                    
                    "Not a bad theory, but I have no proof to back that up."
                    
                    jump chapter2_investigation_taiga_loop

                "Red Hair":
                    
                    t "Mine's brown."
                    
                    n "Yeah, and?"
                    
                    t "And what? Congratulations, you found a hair."
                    t "Try talking to the people it'd match instead."

                    jump chapter2_investigation_taiga_loop
        "Motive":
            
            t "I don't know anyone here. I'm not even supposed to go here, I just got shuffled in with the rest of you."
            t "Any weird personal beef you guys have going on doesn't involve me."
            
            n "Have you heard anyone say anything odd though?"
            
            t "I sleep in class and I mind my own business. You should do the same."
            
            jump chapter2_investigation_taiga_loop

        "Leave":
            pass
    
    "Taiga seems to want to stay out of things. I should consider myself greatful one person is going out of their way to make being at school less of a nightmare."
    "Still, it sucks to see him all by himself like this."
    
    n "You should try, I don't know, hanging out with us?"
    
    t "Why would I do that?"
    
    n "Most of us are night owls. I think Hiro's the only one actually awake before 11 am."
    n "I'm sure everyone would love to dote on your little friend. You don't have to, but if you're bored, you could always stop by."
    n "It sucks not knowing where to go."
    
    "His expression softens."
    
    t "Thanks. I'll definitely think about it."
    
    "I'm sure in a place where everyone already knows each other, it's hard to find an in."
    "I know Jona and I needed someone to tell us it was okay to be near them. Maybe he's the same way."

    return

label chapter2_investigation_mu:
    
    scene backgroundnurse
    
    "Mu takes independent study way more seriously than I do. I've read my fair share of textbooks, sure, but I wouldn't be caught dead reading one outside of class."
    
    n "I assume I'm not interrupting?"
    
    "He startles and closes the book. It doesn't close all the way."
    
    mu "Not at all."

label chapter2_investigation_mu_loop:
    menu:
        "Will you go to the dance with me?":
            if muRep >= 2:
                
                mu "That seems to be the most popular question of the day."
                
                n "I'm too late, aren't I?"
                
                mu "No, I uh, I kinda turned them down. I think people are just looking for a date because they think they're supposed to have one, not because they like me."
                
                n "I like you."
                
                mu "....."
                
                n "I do, that's why I'm asking."
                
                mu "I mean, when you put it like that... Sure, we can go together."
                
                "I wonder if he was thinking of skipping altogether. I hope I haven't put him on the spot by asking him like this."
            
            else:            
                
                mu "You're the third person who's asked."
                
                n "I knew I should have come here sooner."
                
                mu "Really? There's plenty of other people who'd go with you."
                
                n "Well, yeah, but they're not you."
                
                mu "Nagen, I'm flattered, but I'm the only one here that can take care of you in an emergency. Feels kind of weird to take advantage of that."
                
                "Right, he's probably nice to everyone. At least, his version of nice."
            
            jump chapter2_investigation_mu_loop

        "Help with the Party":
            
            mu "I could help with the food."
            
            n "Really?"
            
            mu "I got a list of everyone's allergies, remember? I can make sure people know which foods are safe for them to eat."
            
            n "That'd be great. We've kinda been scrounging around the kitchen for anything that'll work."
            
            jump chapter2_investigation_mu_loop

        "Show Evidence":
            menu:
                "Location of Note":
                    
                    mu "If the Vision Major class wasn't mostly outsiders, I would have assumed it was one of them."
                    mu "The only people that know Jona from before are Ichita and Chisei. They've both been acting kind of weird now that I think about it."
                    mu "Is there anything on his desk that would indicate he sits there?" 
                    
                    n "Yeah. He's been drawing on pretty much anything he can get his hands on, including his desk."
                    
                    mu "You think the person who stole his sketchbook knew that?" 
                    
                    "It was missing for a few days before all this shit went down. There might be little drawings anywhere Jona hangs out."
                    
                    n "You think they're following him around?"
                    
                    mu "More like planting things in his path. I'd be careful, Nagen. Whoever did this is trying to outsmart you."
                
                    jump chapter2_investigation_mu_loop

                "Nail Polish":
                    
                    mu "Rubber cement."
                    mu "I'm sure it wouldn't be too hard to find some lying around here."
                    mu "This place used to be a library after all. As for the nail polish, anyone smart would either remove their nail polish after making this or switch colors." 
                    
                    n "Shit. You're right."
                    
                    mu "I'd be careful asking people about that one. If you show the culprit you have evidence, they might try to lie after the fact."
                    
                    n "I have an iron clad memory."
                    
                    mu "Yeah, but then it would be your word against theirs."
                
                    jump chapter2_investigation_mu_loop
                
                "Red Hair":
                    
                    mu "Judging by the length, it's probably one of the guys or someone with bangs."
                    
                    n "That's what I was thinking."
                    
                    "I don't see this color in his hair though."
                    
                    n "It might have been planted. Do you know anyone that loses hair a lot?"
                    
                    mu "Ichita picks at himself a lot. He shares homeroom with Jona."
                    mu "Whoever did this could have dropped the note while it was drying on the floor of their classroom to pick up whatever hair was lying around."
                
                    jump chapter2_investigation_mu_loop
                
                "Magazine Clippings":
                    
                    mu "I got a bad feeling whoever's responsible knew about the dance beforehand. Do you remember who pitched it?"
                    
                    n "Kietsu. It sounded like he'd been talking about it with other class heads for a bit before getting permission from the teachers."
                    
                    mu "It would have to be one of the class heads then. I guarantee, if word of this got out sooner, it would be all Kazz talked about on the overhead."
                    
                    "That's a good point. As soon as he found out, he blasted it to the entire school."
                    "He would be the first person to know once it was official. He's still on good terms with the teachers."

                    jump chapter2_investigation_mu_loop

        "Motive":
            
            mu "I'mma be honest, Nagen, I'm with you on this one. That was entirely uncalled for."
            
            n "What do you mean?"
            
            mu "Mariko called all of you out, but you and Uitto are the ones who got into fights with people over it. Jona's mostly stayed in his own lane. I don't get why he's being targeted like this." (11)
            
            n "Neither do I. Even during the riots, all he did was sit around and draw."
            
            mu "It's like they're trying to prove he's dangerous. Though, the longer he does nothing about this, the less I'm convinced they're right."
            
            "I gotta admit, if it weren't for Odori and I, he may have kept doing his own thing."
            
            jump chapter2_investigation_mu_loop

        "Leave":
            pass

    mu "What the hell are we going to do after this?"
    
    n "What do you mean?"
    
    mu "Dude, two different students have made threats of some kind and it hasn't even been a month. You've seen how few teachers there are."
    mu "If they decide the lot of us can't behave well enough to be here... You think they're going to send us back?"
    
    n "I'm not going to let that happen."
    
    "I can't. This experiment is the only way my friends and I can lighten our sentences. If it gets shut down due to outside interference... Does Apex know about the test?"
    
    n "I promise, whatever the hell is going on, you guys aren't going to get punished for it." 
    
    mu "Nagen, I don't think that's something you have any control over."
    
    n "I'll find a way then. I'm the student council president, aren't I? If what you guys are worried about is the school shutting down, then I'll do everything I can to keep that from happening." (+Rep)
    
    mu "Thanks, Nagen. That means a lot. I hope you find whoever did this to Jona."
    
    "I can feel the other kids' opinions about us changing. We're so close to getting them to trust us."
    "I just have to work a little harder. I can't relax now, there's still so much to do."
    
    return

label chapter2_investigation_rise:

    scene background cafe
    
    "Rise is at one for the cafe tables. For once, it isn't for tea. She has a bunch of binders and calligraphy pens out with a huge pile of stuff in the middle."
    
    n "Why does no one ever use the art room?"
    
    "She startles, a long glob of contact cement flying close to her hair."
    
    n "Sorry, didn't mean to surprise you."
    
    r "It is alright."
    
    "She dabs her front with a napkin."
    
    r "I was the one tuning out my surroundings."
    
    n "What is all this stuff?"
    
    "I pick up one of the binders. It's full of fabric swatches and pictures of tables."
    
    r "Planners. An elegant party always has some kind of theme or aesthetic. These were ones I brought from home, but I am afraid they are outside of our means now."
    
    "She flips the drying pages to the front. Cut out pictures of candles in jars and repurposed palettes are carefully organized with little notes next to them."
    
    n "This could work."
    
    r "'Rustic' is a theme I usually try to avoid. At least this way, it will look purposeful."
    
    n "It looks fine. What's your worry?"
    
    r "You only get one chance at a first impression. If..."
    r "If my name is tied to this party, I want it to be one people remember fondly..."
    r "Is something bothering you, Nagen?"
    r "I know your new role has been quite demanding."

label chapter2_investigation_rise_loop:
    menu:
        "Help with the Party":
            # + Characters helping
            n "I know you're helping Uitto organize, but I was wondering if you could find some flowers for us?"
            
            r "Flowers?"
            
            n "Hiro thought it would be a good idea to make those little flower things. We can handle picking and making them, we just don't know what kinds grow here, if any."
            r "I could do that."
            
            "She holds up a small notebook."
            
            r "I could even make pressings of what I find."
            
            n "Awesome, thanks!"
            
            r "Is there anything else?"

            #[Yes, go to menu; no, go to outro]
            menu: 
                "Yes":
                    jump chapter2_investigation_rise_loop
                "No":
                    pass
        
        "Show Evidence":
            menu:
                "Red Hair":
                    
                    r "Red hair, and a short one at that..."
                    r "Ichita or maybe even Mu would fit that description."
                    r "Come to think of it, Ichita is also one of the class representatives. He would have known about the dance before most."
                    
                    n "Are you saying he did it?"
                    
                    r "It would be rude to blame someone based on so little evidence. I am simply stating facts."
                
                    jump chapter2_investigation_rise_loop
                
                "Magazine Clippings":
                    
                    n "Look familiar?"
                    
                    r "Yes, they are from Vogue. It is possible the school has copies."
                    
                    n "I suppose, but you also have magazines right there."
                    
                    r "I have a decent collection. You are welcome to borrow them for costume ideas if you like. Our peers have found them quite useful."
                    
                    n "Like who?"
                    
                    r "Ichita, Shoma, Rei, Chisei, and Kitsune. I would like to believe none of them have cut up the issues I leant to them."
                    r "Though I have yet to have any returned to me..."
                    
                    n "I see." 
                    #+[Magazine]
                    
                    "I should try something else."

                    jump chapter2_investigation_rise_loop

                "Nail Polish":
                    
                    r "Why, that's Rei's favorite color."
                    r "She and Chisei were comparing collections and Rei wanted everyone to try it."
                    r "I prefer a proper french manicure myself."
                    
                    "I should try asking one of them."

                    jump chapter2_investigation_rise_loop

                "Sketchbook paper":
                    
                    r "When I found his pens lying in the cafeteria, I turned them in to the teachers. They seemed important to someone."
                    r "It seems your theif wanted to taunt Jona with their theft with whatever was on hand."
                    r "The crafting of it looks like a rush job too."
                    r "When exactly did it go missing?"
                    
                    n "The night Mariko attacked Hiro."
                    
                    r "That was quite a while ago."
                    r "Have you considered, the book changed hands?"
                    
                    "I didn't, until now."

                    jump chapter2_investigation_rise_loop

                "Location of Note":

                    r "If it was found in the vision class, I'd suggest starting with the students who attend."
                    r "It would not strike people as odd if one of them was there early."
                    
                    jump chapter2_investigation_rise_loop

        "Motive":
            
            n "Someone left a threat note for Jona."
            
            r "What an awful thing to do, and so soon after Mariko lashed out."
            r "Do you think she ended up inspiring someone?"
            
            n "I'm not sure. Jona says it..."
            n "I guess this kind of thing happens to him often, but it doesn't hurt to be careful."
            n "You didn't see anything out of the ordinary this weekend, did you?"
            
            r "I fear not. This is something I am unable to help with, unfortunately."
            
            n "What were you doing before class?"
            
            r "Working on my collages."
            
            n "Anyone else around that saw you?"
            
            r "Ichita and Uitto. Quite the odd pair, if I must say. You may have better luck asking other Vision Majors. They share first period with him after all."
            r "Though I will say, it sounds like he's been more of a liability than a friend to you."
            
            n "You don't know him like I do."
            
            "Anytime I disagree with her, she purses her lips."
            
            r "If you say so."

            jump chapter2_investigation_rise_loop

        "Leave":
            pass
    
    r "You have enough on your plate as it is. This may be out of line for me to say, but have you considered that your friends can handle this without you?"
    
    n "What do you mean?"
    
    r "You have a whole event to plan. It seems unfair that Jona asked for your help and not Hiro's."
    
    n "Jona didn't ask for my help."
    
    r "I see."
    
    n "He shouldn't have to."
    
    r "But are you shown the same courtesy? If they really are your friends, you should be able to rely on them to do that much." 
    r "I have said something that upset you, my apologies." 
    
    n "I need to check on the others. Like you said, I'm kind of busy."
    
    "I leave without another word."
    
    return

# Graveyard?
label askforhelp2:
    menu:
        "Uitto":
            u "I don't get along well with most of the people in my class."
            u "A lot of them have been spreading rumors about Jona. Family stuff."
            u "Rise was busy with whatever you guys were doing before class started, so she showed up late. Guess not everyone knows how to run in heels."
            u "I have heard the nail polish color used was popular. You might want to check with Momoko, she's the beauty guru. She'll know more about it than me." 
        "Hiro":
            h "I like being the first in the door for class."
            h "I am the leader after all."
            h "Shoma said someone slashed up a fashion magazine to make the note we found."
            h "Rei's just as worried as we are; she told me everyone who might've worn that color of nail polish..."
            h "I uh, probably should've written that down. Chisei was one of them."
        "Jona":
            j "No one in class said they wrote a note."
            j "They didn't see anyone entering the room either."
            j "Ichita had the stuco meeting, so he came in a little after everyone else. Not sure if that's much help."
            j "He said there was nothing in the classroom when he locked up for the night."
        "Back":
            #return to menu
            pass

