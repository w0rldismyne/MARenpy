label MarikoVisit:

    if mTurn == 0:
        jump MarikoP1
    elif mTurn == 1:
        jump MarikoP2
    elif mTurn == 2:
        jump MarikoP3
    elif mTurn == 3:
        jump MarikoP4
    else:
        jump MarikoPF

define food = False

label MarikoP1:
    scene backgroundfield

    "I know Mariko said she didn't want any trouble from me, but I wonder if she's doing alright."
    "It wouldn't hurt to drop by and say hi, would it? During lunch break, I found her on the practice field with a gaggle of other girls."
    "It seems like she was able to gather enough participants to start the Cheer Squad."

    show mariko judge

    m "What do you think you're doing?"

    n "I think we got off on the wrong foot. You're the Cheer Captain aren't you?"
    n "As a club leader, we might be working together more in the future."

    m "What makes you so sure of that?"

    n "I'm running for Student Council president."

    m "Oh, that's rich. Listen, no offence, but we're kinda in the middle of practice right now."
    m "Other teams have years to come up with routines, and I've gotta start from the bottom with a bunch of rookies."
    m "These girls need my full attention if they ever want to be competition ready."

    n "Okay, I can come back when you're not as busy."

    hide mariko judge
    show mariko

    m "We go on break in twenty, before lunch ends."

    hide mariko

    "I needed to get food anyways. I came back later, when practice was over."

    show mariko sheepish

    m "Good job girls! Next practice, be sure to bring extra water! Oh! You, uh, actually came back."

    n "Twenty minutes before lunch ends, right?"

    m "Right... So, what's up?"

    hide mariko

    menu:
        "What are you forcing them to practice?":
            $ mRep -= 1

            show mariko mad talk

            m "I didn't force them to do anything!"
            m "We all agreed that we needed more practice before our first game!"

            "I think I hit a nerve."

            m "If you want to worry about how someone's leading, I'd suggest you talk to your future council members."

            n "I didn't mean to insult your leadership style, I just found it odd."

            hide mariko mad talk
            show mariko judge

            m "These girls are almost as soft as you are."

            "S-soft!?"

            m "We practice twice a day, every day. It's the only way to toughen them up."

            "That really doesn't sound healthy. I don't think I'm going to convince her otherwise."
            "The rest of the period she lectured me about how tired she was of people assuming Cheerleaders didn't have to work hard; including her squad members."

            hide mariko judge

        "Aren't you going to eat something?":
            $ mRep += 1

            show mariko

            m "Hunh? Oh yeah, I almost forgot. Thanks for reminding me."

            "How do you forget to eat? It looks like she brought something though. It's just a thing of plain spaghetti."

            m "I gotta remember to carb load between practices! Did you grab something?"

            n "Yeah, I got something while I was waiting."

            hide mariko
            show mariko sad talk

            m "Sorry about earlier, it's just, they're starting the season so early."
            m "Normally a new squad gets at least three months to prepare. We have two weeks."

            "So that's why they're practicing so hard."

            n "You really should be eating more than that if you're practicing this much."

            m "Yeah, but I don't really have a lot of time to cook and the lines are so long right after the bell rings."
            m "I can't show up late to practice when I'm the one who scheduled it."

            "She sounds so defeated. It probably doesn't help that the cafeteria closes up at the end of lunch. How long does she expect to keep going like this?"

            n "You have a meal plan, right?"

            hide mariko sad talk
            show mariko talk

            m "Yeah, why?"

            n "Next time you need food, I can just grab you some during practice."

            hide mariko talk
            show mariko smile talk

            m "Really!?"

            n "As long as you have a card, it won't cost me anything. Why not?"

            m "Oh the girls will be so happy when I tell them tomorrow!"
            m "This is such a huge help, thank you so much Tesuta!"

            "Somehow, I got roped into being a gopher for the Cheer Squad."

            hide mariko smile talk

            $ food = true
        "If you could change one thing, what would it be?":
            $ Vigor += 1

            show mariko

            "She looked at me with a blank stare. I don't know why; I expected a slightly positive reaction."

            m "...I need more time."

            "She seemed, defeated in a way. Maybe it was because she just finished practice that she looked so exhausted."

            n "You've got an event coming up or something?"

            hide mariko
            show mariko upset talk

            m "Something like that. I don't think I'll be ready for it, no matter how much I practice."

            "She half laughed, not meeting my eyes."

            n "Are you okay? You're shaking!"

            m "I- ugh- low blood sugar maybe? I haven't eaten anything yet."

            n "You need to take better care of yourself. You could end up getting hurt."

            m "I-I know. To be lectured by you of all people."

            hide mariko upset talk
    $ Vigor += 1
    $ mTurn += 1

    show mariko judge

    m "Why did you do it?"

    n "Do what?"

    m "Start the riots... Why? What made you think that was okay?"
    m "What possess somebody to do something like that?"

    n "I was just trying to protect my friends."
    n "I tried everything else. That was the only idea I had left."

    "She closed her eyes and took slow, shallow breaths. I waited patiently for her to respond."

    hide mariko judge
    show mariko talk

    m "What... what were you protecting them from?"

    n "It's not really my place to tell you, you'd have to ask them yourself."
    n "To be vague, I guess I'd say bad people. Or rather, people who were trying to hurt them."

    "She mulled that over as well."
    "Granted, it was a gross exaggeration of the problem, but ten minutes is not enough time to tell anyone's life story."

    hide mariko talk
    show mariko judge

    m "Then you understand why I don't like you?"

    n "Yeah, sort of."
    n "I didn't do anything to you directly, but I contributed to the state of Guwon."

    m "Then why'd you come to see me."

    n "It looked like something was bothering you, I wanted to make sure you were okay."

    hide mariko judge
    show mariko cry

    m "I... thanks. Really. It's been... Adjusting's been hard."
    m "I'm fine. It's fine. Everything's going to be okay."

    hide mariko cry

    return

label Mariko2P:

    scene backgroundfield

    show mariko smile talk

    m "Well, well, well; look who came back girls?"

    if food == True:
        m "Alright everybody, break time!"
            
        "After she finished barking her orders I got swarmed."
        
    else:
        m "So, what is it this time?"

        n "What do you mean?"

    m "You honestly expect me to believe you're hanging around here just for the fun of it?"

    n "No. Doesn't mean it's not true though."

    hide mariko smile talk
    show mariko talk

    m "You're  a lot different then what I expected, more sarcastic."

    n "I'm not being sarcastic!"

    "She grimaced."

    hide mariko talk
    show mariko cry

    m "Really? What exactly about this is fun for you?"
    m "Is it a fetish? Do you have a thing for pom poms?"

    hide mariko cry

    menu:
        "Hell yeah it's about the pom poms.":
            $ mRep -= 1

            show mariko cry

            m "I didn't actually mean... good god."

            "She looked so disturbed."

            n "You asked. Why, what's your type?"

            hide mariko cry
            show mariko talk

            m "Double-Ds."

            n "...Like fat dudes or...?"
            n "No way."
            n "Where do you get off judging me?"
            n "At least my ideal is realistic."

            hide mariko talk
            show mariko glare

            m "Hey, I'm better then some pom-pom chaser. I don't go cruising around-"
            m "This isn't about me okay!"

            n "Let this be a lesson, don't ask questions you don't want to know the answer to."

            hide mariko glare
            show mariko talk

            m "You could try and show a little shame y'know."
            m "Geez, I don't know if I should be relieved your intentions are relatively normal or more on guard."

            hide mariko talk
        "I want to know more about you.":
            $ mRep += 1

            show mariko upset talk

            n "I never really talked to anyone from the front lines."
            n "All I really know was you were the last to join."
            n "It was almost legendary the way people talked about it."

            m "Legendary huh?"

            n "I wanted to see first hand what kind of person could do the impossible."

            hide mariko upset talk
            show mariko talk

            m "It's not nearly as incredible as you make it sound."
            m "I was on the run for two days, and then they put the helmet on."
            m "Others may have given up at that point, only I knew I couldn't stop resisting, not for a moment."

            n "I mean, I guess running away isn't as cool as fighting off a brainwashed army."

            hide mariko talk
            show mariko cry

            m "Running away? Never, I kept running forward...."
            m "That sounded less cheesy in my head."
            m "The point is I kept going until I found everyone from my squad and brought them home, dead or alive."
            m "It was the least I could do."

            "There wasn't exactly a home to go back to either."
            "It's hard to imagine running around that long looking for the deceased to return to rubble. Like a morbid Captain Ahab."

            hide mariko cry
            show mariko talk

            m "I promised I would keep everyone safe, but it's kinda hard to help people who won't listen to you."
            m "I will never let something like that happen again."   

            hide mariko talk
        "I like watching people.":
            $ Vigor += 1

            show mariko

            n "You know, like anthropology, seeing people in their natural habitat and how they behave."

            m "So you're studying me? Why?"

            "She was tense, defensive, and likely picked up on what I had in mind."
            "Genki by nature was stubborn as hellfire, my life could be easier down the road if she was on my side."

            n "Do you think you're not worthy of observation?"

            hide mariko
            show mariko cringe

            m "N-no. I mean, not like that. It's just kind of a weird thing to tell someone."

            "She tugged at her earring as she faltered."

            n "I'm only telling the truth. Don't ask questions you don't want to know the answer to."

            hide mariko cringe
            show mariko judge

            m "...Is it with ill intent?"

            n "Huh?"

            m "You watching me, is it... You're not trying to start anything again, are you?"

            n "No."

            hide mariko judge
            show mariko talk

            "She breathed a long, reserved sigh of relief."

            m "You could stand to work on your people skills, y'know."

            hide mariko talk

    $ Vigor += 1
    $ mTurn += 1

    show mariko talk

    m "I take what I do very seriously. By the time I'm done, these girls will be an elite unit."
    m "Hopefully, by then, they won't need me anymore. Until then-"

    n "Yeah, yeah; don't lay a finger on them, I know."

    hide mariko talk
    show mariko judge

    m "This is no laughing matter. I don't need them getting distracted by some wandering Cyber Goth."
    m "If you come back again, be prepared to work."

    n "What's that supposed to mean?"

    hide mariko judge
    show mariko smile talk

    m "Fufu, I bet you don't even own a pair of sweats."

    n "Hey, I work out... periodically."

    m "Uh huh, prove it."   

    n "Maybe I will."

    m "Maybe?"

    n "Just not right now."

    hide mariko smile talk

    "My exit out of that conversation was as graceful as my leave off the field."

    return

label Mariko3P:

    scene backgroundfield

    show mariko smile talk

    m "You really don't know when to quit, do you?"

    n "You said if I came back, to be prepared to work."

    "The exercise clothes I borrowed from Hiro were easily a size too big."
    "The longer I stood there, the more the girls stared at me. Or at least at the stains on this borrowed shirt."
    "Even if they're not my mustard stains, I can't help but feel incredibly uncomfortable."

    hide mariko smile talk
    show mariko judge

    m "Didn't take you for the masochistic type, but then again, you're full of surprises."

    "She turned to face the girls."

    hide mariko judge
    show mariko cackle

    m "Alright everybody, strap on the weights, it's time for lunges. No whining, no complaining, let's move!"

    n "Aren't we going to warm up first?"

    hide mariko cackle
    show mariko smile talk

    m "We already have, you were late."

    "Against my better judgement, I followed Genki's orders."

    hide mariko smile talk
    show mariko cackle

    m "You've gotta ease into it Cyber Dork, if you keep doing that, you'll tear a ligament."

    n "I don't know what you're talking about, I'm in perfect form."

    "She burst out laughing, which was doubly insulting considering she was folded like a pretzel while I contemplated the least embarrassing way I could stand up from this."

    n "You know I'm glad you're finally laughing around me, but why does it have to be at my pain?"

    hide mariko cackle
    show mariko smile talk

    m "I'm sorry, I just never dreamed you'd look so ridiculous."

    n "Key word here is ‘pain'. I can't get up."

    m "Oh geez. Here let me help you."

    "With a surprising amount of strength, she hoisted me onto my knees. I may or may not have fallen on my face when she let me go."

    m "Again with the dramatics."

    "She rolled her eyes, but I seriously need some ice."

    n "Your overwhelming concern fills me with great joy."
    n "Seriously though, this is the happiest I've seen you. What gives?"

    hide mariko smile talk
    show mariko upset talk

    m "Oh... you noticed."

    n "That's not the only thing I've noticed."

    hide mariko upset talk

    menu: 
        "None of the girls talk to Mariko.":
            $ mRep -= 1

            show mariko upset talk

            n "You're the captain, but none of the girls seem to talk to you... Wait, you are the Captain right?"

            m "Of course I am!"
            m "I'm the one who brought everyone together. Who else would be a better Captain then me?"

            n "Then why don't they talk to you?"

            m "Th-they do. They're just busy right now. Right girls?"

            "They reply with zeal like always, but I know what I've seen."

            n "You just seem kinda lonely."
            n "I mean, why else would you be talking to me instead of your friends."

            hide mariko upset talk
            show mariko judge

            m "They aren't- Look, I appreciate your concern, but I'm fine, really."
            m "I'm just trying to figure something out."

            n "Do they not like you or something? I know girl friendships are tricky."

            m "Just drop it, okay."

            "She doesn't look fine. There's a melancholic air about her that she just can't seem to shake. I can't tell if I'm helping or making it worse."

            hide mariko judge

        "You keep looking at that girl.":
            $ Vigor += 1

            hide mariko mad talk

            m "No, I'm not! ...I mean, of course I would be looking at my teammates."
            m "I'm like, super in charge of them and junk."

            n "Subtle."

            m "I really don't need the sarcasm right now."

            "There's always time for sarcasm. I am a seven layer bean dip of sarcasm."

            n "Next you're going to tell me she's your star athlete."

            "She flushed bright red."

            m "But she is!"
            m "Rei used to be captain of the Flag Line. She can juggle sabers while doing back flips."

            n "Really? Cause it looks like she's just doing toe-touches."

            hide mariko mad talk
            show mariko glare

            m "You're impossible!"

            n "You dragged me through the mud for ogling at them, just let me have this."

            "She hung her head in shame looking incredibly guilty."

            m "I wasn't ogling."

            "All I could do is laugh."

            hide mariko glare
            show mariko upset talk

            m "Rei... is... a trusted comrade. I would never do anything to jeopardize that."
            m "Which is why I wasn't ogling!"

            n "I'm not buying any of it."

            hide mariko upset talk
            show mariko cry

            m "Would you just keep it down already! She might hear you!"

            "Her energy's dropped way down. I think I've hit a little too close to home."

            n "I'm sorry, I didn't mean to make you uncomfortable."
            n "I just find it kind of funny that this is your achilles heel."

            hide mariko cry
            show mariko smile talk

            m "Well your achilles heel is your complete lack of strength."

            n "Hey!"

            "At least she's feeling better, but it meant 10 laps around the field." 

            hide mariko smile talk

        "You're not taking care of yourself.":
            $ mRep += 1

            show mariko talk

            m "What do you mean? I'm in my prime!"

            n "Yeah, you put in your all at practice, but you do so until there's nothing else to give."
            n "I can't count how many times I've had to remind you to eat and I fail to see how you can do all this and school without missing sleep."

            m "I have to keep myself busy. I can't risk losing focus now."

            n "But you're hurting yourself to do it."

            "I used to be the same way. I poured myself into my work and shut out the world around me. It isn't a healthy way to deal with your problems."

            n "What are you afraid will happen if you stop?"

            hide mariko talk
            show mariko upset talk

            m "...That I'll wake up and all of this will be over."

            "She watched the girls practice with a combination of longing and mourning."

            hide mariko upset talk
            show mariko cry

            m "Moments like these is what kept me going."
            m "If they go away again, if I stop pushing forward, I don't know if I can start again."

            n "So you become someone else."
            n "You can still do great things, and it won't erase the person you are now, you'll just have to learn how to do things differently."
            n "We'll all be here to help you too."

            "Her laugh sounded empty."

            hide mariko cry
            show mariko smile talk

            m "You're part of the problem y'know."
            m "Being so nice to me, it's making me doubt certain things."
            m "It's been years since I've felt like this. I don't like it."

            n "Would it help if I was meaner?"

            m "A little, but it's a little too late for that I think."

            hide mariko smile talk

    $ Vigor += 1
    $ mTurn += 1

    show mariko judge

    m "Do I need to take you shopping? You're showing your underwear again."

    n "No I'm fine... And what do you mean again?"

    m "I mean it seems like every pair of pants you own are either too tight or obviously not made for you."

    n "Hey I don't need to be lectured by the queen of ‘oh yeah, I forgot it was lunch'."

    hide mariko judge
    show mariko

    m "Shoot, lunch is almost over, isn't it."

    n "Yeah, and you still haven't eaten anything."

    m "I completely forgot. I'll see you around Nagen."

    hide mariko

    "She ran off desperate to grab something from the cafeteria before they closed."

    return

label MarikoP4:
    scene backgroundfield

    show mariko

    "After the last time we talked, I started dropping by Mariko's cheer practice a couple times a week."
    "It was surprisingly vigorous all things considered. All of us had improved quite a bit since the beginning of the year, but she still wasn't satisfied with the results."

    n "When am I going to learn how to do one of those crazy lifts?"
    n "These muscle bound  broads are starting to make me look bad."

    hide mariko
    show mariko smile talk

    m "Hah! You'd make a better Flyer than a Base."
    m "I'd focus on cleaning up your floor work before you go attempting any stunts."

    "I've been coming here for weeks now, and I'm still only barely able to follow what she says."

    n "I could manage it, just let me give it a try."

    "She rolled her eyes."

    hide mariko smile talk
    show mariko talk

    m "Fine, here we'll start with a basic shoulder sit."

    n "Cool... and that would be."

    hide mariko talk
    show mariko judge

    m "Ugh, I'm too tired for this."
    m "It's in the name Nagen, just, kneel on the ground with one knee out at a 90 degree angle and I'll hop onto your shoulders."
    m "Once I'm on you, stand up. Do you think you can handle that?"

    "I followed her instructions. It was clumsy, but I managed to stand up with the added weight."
    "My back might murder me tomorrow though, she's heavier than she looks."

    hide mariko judge

    n "Hah! See, that wasn't so hard, I can do this crap too."

    "I felt a heavy weight against the back of my head. I could see her arms dangle on either side of my peripheral vision, her chin dug into my skull."

    n "Mariko?"

    "She felt warm... Too warm. Why isn't she moving? What's going on!?"

    show backgroundMPath

    #CG

    n "Mariko? Mariko, say something!"

    "I set her down as gently as I could, she wasn't moving."

    n "You, with the brown hair, go get the nurse!"

    scene backgroundnurse

    "They told me that she was probably dehydrated and under slept"
    "Which, I guess makes sense, but how did she get this bad? Was she forgetting to drink too?"
    "How can someone so outwardly lively just not take care of themselves like this?"
    "My concern only grew when she woke up bawling her eyes out."

    show mariko cry

    m "I'm sorry. I'm sorry I yelled. Please listen to me, don't follow him. NO!"

    "She sat up instantly, eyes wide with fear."

    m "I'm sorry. I'm so sorry."

    n "Mariko?"

    hide mariko cry
    show mariko mad talk

    m "AH!"

    n "It's okay, it's just me."

    "She laughed that horrid, hollow laugh."

    hide mariko mad talk
    show mariko upset talk

    m "Don't look at me like that. Why are you even here. Where... Where am I?"

    n "You're in the nurse's office. You totally passed out on my shoulders."

    "As if that wasn't scary enough, now she's shouting things in her sleep."

    hide mariko upset talk

    menu:
        "It's not your fault.":
            $ mRep += 1

            show mariko talk

            m "Huh?"

            n "I have a hard time forgiving myself for mistakes I made, sometimes it helps to hear someone else say it."

            hide mariko talk
            show mariko cry

            m "I'm sorry for making you worry."

            n "It's okay. You didn't make me do anything, I chose to be worried. No, that doesn't sound right."
            n "But I mean, you get the idea."

            m "Yeah. I just keep making myself look ridiculous. I mean, I jumped down your throat when we first met, and you're not even the one I was really mad at."

            n "You'd be surprised how much I get that."

            hide mariko cry
            show mariko talk

            m "Haha... Hey Nagen, is it normal to... Do you ever have nightmares about your friends dying?"

            n "Sometimes."

            hide mariko talk
            show mariko cry

            m "Then it goes away. The dreams, they'll go away right?"
            m "I can't- I can never save them when I'm asleep. It just keeps happening over and over again."

            "She was crying again, but at least this time she was talking to me and not the wall."

            n "Woah, it's okay."

            m "Nagen, I'm tired of being scared all the time."

            hide mariko cry

        "Why are you doing this to yourself?":
            $ mRept -= 1

            show mariko smile talk

            n "You've got to stop this!"

            m "Nagen, it's not that big of a deal. I just forgot my limits is all."

            n "What, you think this is funny?"

            hide mariko smile talk
            show mariko

            n "Not eating or drinking, and working yourself until you pass out?"
            n "You're going to get yourself killed at this rate."

            m "I... I'm not doing this on purpose."
            m "There are more important things to worry about right now."

            n "What's more important than your own wellbeing?"

            hide mariko
            show mariko glare

            m "Everything. Literally everything. I don't deserve to be a priority right now."

            n "Mariko, you can't keep doing this."

            m "I'm not doing anything to myself!"
            m "Stop acting like I'm the problem here."
            m "If you were so worried about other people's wellbeing, where was it when my friends were out their fighting your war?"

            hide mariko glare

        "What happened?":
            $ Vigor += 1
            
            show mariko talk

            n "You were crying in your sleep about people following someone."

            m "Oh..."

            n "You don't have to tell me if it's too painful."

            hide mariko talk
            show mariko cry

            m "It's... I mean, I can, I just... I don't want to think about it too much."

            "I waited patiently for her to continue."

            m "I was dreaming about when we were in the shelter after Lethe launched her first attack."
            m "The teachers from Estella gathered everyone they could to the gym, told us to wait there for our parents to show up."
            m "Hiro suggested that we should leave..."

            "Wait a minute, Hiro went back to Estella? That doesn't seem right."

            m "I was the only one that stayed behind."

            hide mariko cry
    $ Vigor += 1
    $ mTurn += 1

    if mRep >= 2:

        show mariko cry

        m "What's the most important quality for a person to have?"

        hide mariko cry
        menu:
                "Bravery":
                    $ Intel += 1
                "Insight":
                    $ Vision += 1
                "Empathy":
                    $ Charm += 1
                "Strength":
                    $ Vigor += 1

        show mariko

        m "For me it's loyalty. If you make a promise to someone, you have to keep it, no matter what."
        
        n "That's certainly noble, but why are you telling me this?"

        m "I made a promise to someone that if they helped me, I'd help them in return. I can't break it now, but I'm not sure I can go through with it."

        n "Are you in trouble?"

        hide mariko
        show mariko talk

        m "I'm not sure yet. I have... a lot of thinking to do."

        n "If there's anything I can help with, let me know."

        hide mariko talk
        show mariko smile talk

        m "Thanks. I really do think of you as a friend Nagen. Please don't forget that."

        hide mariko smile talk

        return
    else:
        
        show mariko
        
        m "I don't think you should come around here anymore."

        n "What are you talking about?"

        m "Nothing good will come of this, for either of us. It'll be better if you just leave."

        n "But-"

        hide mariko
        show mariko upset talk

        m "I get it. You like the idea of me. It's sweet, but I can't waste my girl's time talking to you."

        "Excuse me? Where does she get off talking to me like this?"

        m "You know your way out."

        n "Hey, I'm not done talking to you."

        m "Yes, you are. Goodbye Nagen."

        "She dragged herself out of the cot and left me behind."

        hide mariko upset talk

        return
label MarikoPF:
    scene backgroundfield

    show mariko

    m "Nothing's changed Nagen. Go talk to someone else."

    return