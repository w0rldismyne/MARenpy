
label UittoVisit:

    if uTurn == 0:
        jump Uitto1
    elif uTurn == 1:
        jump Uitto2
    elif uTurn == 2:
        jump Uitto3
    elif uTurn == 3:
        jump Uitto4
    elif uTurn == 4:
        jump Uitto5
    else:
        jump UittoF

label Uitto1:

    scene backgroundcourtyard

    "I can't keep not talking to Uitto about how she stopped wanting to have anything to do with me. I mean, theoretically I could, but not knowing will drive me bananas."
    "Now, how do I approach her without pissing her off?"

    show uitto serious

    n "Umm... hey. How's it going?"

    u "Are you ready to talk about it?"

    n "Hunh?"

    hide uitto serious
    show uitto sigh

    u "That's what you're going to ask me, isn't it?"
    u "Of course, you know the answer is no because I haven't told you, so you're trying to see if I'm in a good enough mood to pester me about it."

    n "That's not-"

    hide uitto sigh
    show uitto serious

    u "....."

    n "Okay, you got me."
    n "God forbid I want to know why my childhood friend and comrade turned her viper fangs on me."

    u "We were never friends, Nagen."

    n "That's not true."

    u "And what part of our riveting childhood terrorism made us friends?"

    n "You used to be nice to me. A little intimidating at times, but not bitter."

    hide uitto serious
    show uitto yell

    u "You don't know anything about me."

    hide uitto yell

    menu:
        "List everything":
            $ uRep += 1

            show uitto serious

            n "Oh reallly?"
            n "So I guess that means I don't know you defended your DDR title for four years or that you had the weakest constitution in your dance class."

            hide uitto serious
            show uitto cringe

            u "Okay, so you know stupid stuff about me."

            n "It wasn't stupid to you. Not at the time."

            hide uitto cringe
            show Uittosadtalk

            u "You remember everything about everyone."
            u "That hardly makes me different than anyone else."

            n "I wanted to know those things. You hardly told us anything about yourself, that's all I have to go on."

            hide Uittosadtalk
            show uitto sad

            u "There's a reason I filtered myself. I had an image to uphold. Bitter and jaded doesn't look good in any audition."

            n "What are you talking about?"

            hide uitto sad
            show uitto

            u "Always so damn literal. I was putting on an act, you dumbass." 

            hide uitto           

        "You're right":
            $ uRep -= 1

            show uitto serious

            n "I don't know who you are anymore. You're like a completely different person."

            u "Oh really, and who exactly was this glorious person you knew?"

            n "An impressionable pageant girl that got her kicks from hanging out with the bad kids."
            n "You followed us around like a lost puppy and suddenly you're too cool for us?"

            hide uitto serious
            show uitto yell

            u "Is that all you think this is?"

            n "What else am I supposed to think? You won't talk to me."

            u "Forgive me for not wanting to showboat with you around the school so soon after defeat.'
            u 'My idea of laying low doesn't involve giving the middle finger to the people who spared us."

            n "See, that's what I don't get. Are you trying to work with the DVP or outsmart them?"
            n "Are you mad at me cause you think I sold you out or cause I stole your idea?"

            hide uitto yell
            show Uittosadtalk

            u "I'm just trying to survive, Nagen."
            u "I... You screwing me over makes the most sense. Less holes to fill in."

            n "Compared to what?"
            n "Some crooked cop shaking me down for info? You're right, me spontaneously being an asshole makes way more sense."

            u "You're being one right now. Makes plenty of sense to me."

            hide Uittosadtalk

        "You don't know you either":
            $ Charm += 1

            show uitto sigh

            u "What kind of fake-deep nonsense-"

            n "Sixth grade, August 19th, Jona slipped a pill bug into your sandwich to see if it tasted like anything."
            n "You ate it."

            hide uitto sigh
            show uitto cringe

            u "Eww! Why would you do that? Why didn't you tell me?!"

            n "Like I said, Jona did it. I didn't tell you at the time because you would have made a scene."
            n "Then everyone would have known. You didn't need to have people laughing at you on top of all that."

            hide uitto cringe
            show uitto yell

            u "Why didn't you stop him?"

            n "I thought it'd be funny."
            n "It was."

            u "Ugh. Shut up, you jerk."

            n "My point is, if I haven't told you something, it isn't to be cruel. I'm sure you're the same way."
            n "Whatever it is, I can handle it."

            hide uitto yell

    $ uTurn += 1
    $ Charm += 1
    
    show uitto sad

    u "I'm over trying to impress you or anyone else for that matter."
    u "It's... exhausting and frankly, I'm too tired to keep trying. I'm sorry I'm not the person you thought I was."

    n "You're making this way more complicated than it has to be. Did I do something to piss you off?"

    u "I think so."

    n "Something I could fix?"

    hide uitto sad
    show Uittosadtalk

    u "Probably not."

    n "What do you think I did?"

    u "I don't think you're being honest with anyone about what happened with the DVP."
    u "Intentional or not, you did something to get the better deal. Being a plant is part of it."

    n "I'm not a plant."

    hide Uittosadtalk
    show uitto serious

    u "Oh come off of it, Nagen. You're the only one who knows what's really going on."
    u "The DVP hasn't said a word to the rest of us. I don't know if that was your intention or not, but it feels shitty."

    n "MOTHER FU-"

    "I'm not a big fan of being used. It's times like this I wish I was more eloquent when upset."

    hide uitto serious
    show uitto yell

    u "Nagen, it's fine. You just need to be more careful."
    u "Did they give you any tech? Anything they could sneak a bug or tracker in?"

    n "A laptop and a phone. That's about it."

    u "Then keep them away from us. I can't trust you like I used to, no offense."

    n "No, I get it."

    hide uitto yell
    show uitto sad

    u "Watch what you say to people. Your words hold more power than you think."

    n "Thanks, I'll keep that in mind."

    hide uitto sad

    "Even if she's just being paranoid, she has a point."
    "I'll make sure to cover anything that looks remotely like a camera lens tonight."
    return

label Uitto2:

    scene backgroundclass

    "Ever since I've talked to Uitto, I've been more careful about what I say and who I say it to."
    "Things seem to have gone back to normal with us."

    show uitto cringe

    u "I'm telling you Nagen, it's torture sitting through Proficiency Management."
    u "It's one thing to yell at me for an hour about how I shouldn't use my ability, it's another to cage me in with a bunch of Charisma Majors."

    n "But you are a Charm Maj-"

    hide uitto cringe
    show uitto serious

    u "Charisma Major."

    n "Whatever. Why hate your cohorts?"

    hide uitto serious
    show uitto

    u "See, you're an intelligence major, so you don't get it."
    u "Getting labeled a Charisma Major is nothing but trouble. Like Kitsune, classic example of the vapid peacocks I get lumped in with. The people who advertise them only make it worse."
    u "You're either preened for objectification or labeled manipulative. It doesn't matter how smart you are or how hard you work, all your accomplishments are considered handouts."
   
    hide uitto
    show uitto cringe
   
    u "There's only a few types who can survive that lifestyle; I can't stand any of them."

    hide uitto cringe

    menu:
        "Which type are you?":
            $ uRep += 1

            show uitto sigh

            u "A little bit of both. I prefer people think I'm the manipulative type."
            u "Saves me from false pity."

            n "What do you mean?"

            hide uitto sigh
            show Uittosadtalk

            u "You know, those shallow social responses you get when people don't have anything nice to say."
            u "Sure, they'll tell you ‘I'm sorry to hear that', but that just means you're making them uncomfortable."

            n "I heard rumors that Rosette wasn't the most wholesome venture."

            hide Uittosadtalk
            show uitto smirk

            u "A lot of it was BS from parents who were pissed their daughters didn't make the cut."
            u "They didn't know that in order to make it in pageants, you have to eat, live, and breathe everyone's shallowness."
            u "It gets really ugly."

            "Despite all that, she still holds onto the title as her superhero alias."
            "Maybe years of living that lifestyle makes it hard to quit."

            n "Do you ever miss it?"

            hide uitto smirk
            show uitto sad

            u "Sometimes."

            hide uitto sad
            show uitto serious

            u "The days right after I was crowned, when there were still three of us... I can never go back to that life."

            "She says so with icy conviction. I knew they were the reason she joined us, but I never asked her about it."
            
            hide uitto serious

        "It's not that bad":
            $ uRep -= 1

            show uitto cringe

            n "There's a lot worse things in life than putting up with a room full of extroverts for an hour."

            u "That doesn't make it suck any less. Besides, this isn't just about the class."
            u "My whole life, I've been the poster child for those idiots. I hated every minute of it."
            u "I'd sooner take suppressors than live the rest of my life as a ‘Charm' Major."

            n "Don't joke about that kind of stuff. Suppressors are evil as hell."

            "The stuff I was forced to take growing up wrecked me."
            "There's barely any research, let alone guidelines, for making Proficiency-based drugs."
            "I wouldn't trust anyone who was trying to take peoples' powers away."

            hide uitto cringe
            show uitto yell

            u "I'm not joking. I would give anything to just be normal."

            n "This is normal."

            u "No Nagen, this is a bunch of people trying to replicate normal."
            u "As long as I'm a Charisma Major, I will be lumped in with the rest of them."

            hide uitto yell

        "There has to be someone":
            $ Charm += 1

            show uitto talk

            n "Not every Charisma Major is a showpony. I mean, you're not."

            u "Shows what you know."

            n "Still, there has to be Charisma Majors you can stand."

            hide uitto talk
            show uitto sad

            u "There was one. Renge, she was the first girl to win the Roselia pageant. Her Proficiency was empathy."
            u "She gave everything she had to make Rosette something everyone should care about."

            n "What happened to her?"

            hide uitto sad
            show Uittosadtalk

            u "She... They decided she was too old."
            u "I was supposed to be her replacement. When she told me to quit Rosette, I thought it was just because she was jealous... It was just her way of looking out for me."

            n "Empathy, hunh? I could see how her abilities would compliment yours."

            hide Uittosadtalk
            show uitto sad

            u "I didn't like her because of her Proficiency. You can understand how someone feels and still be a dick."
            u "I liked her because she was the only one looking out for me before you guys. If it wasn't for her, I could have ended up like Siren, or worse."
            
            hide uitto sad
    
    show uitto cringe

    u "You remember Siren, right?"

    n "The original leader of the Karmic Gladiators, formed for recruiting the entire team, and renowned Charisma Major?"
    n "Nope, no idea. Completely clueless."

    u "I could do without the sarcasm, Nagen. A simple yes would've worked."

    n "My Proficiency is Memory, the yes is implied."

    hide uitto cringe
    show uitto sigh

    u "Ugh, anyways, people don't remember her for her career. I guarantee you ask anyone at this school and the only thing they'll talk about is the scandal."
    u "After all, what good is a public servant who lets herself get attacked? If only she turned off her wicked charm then she'd be safe."
    u "Shame on her for making the wrong people like her."

    n "You're joking."

    hide uitto sigh
    show uitto serious

    u "That was today's lecture. I mean, not those exact words, but you get the idea. All I know is if I'm going to be remembered for one thing, I don't want it to be Rosette."
    u "Heaven forbid I become the subject of someone's cautionary guilt speech."

    n "What do you want to do?"

    hide uitto serious
    show uitto

    u "I mean, what else is there? I've been training for Proficiency pageants my whole life. It's all I know."

    n "Well one of the benefits of all of this is the freedom to make our own decisions."
    n "No one's going to force you back into those pageants and you don't have to go around advertising your Major."

    hide uitto
    show uitto smile

    u "Hey, you're right! I could do whatever I want!"

    n "Within reason."

    hide uitto smile
    show uitto smirk

    u "Forget what those stupid teachers say, I'll make my own path to glory."

    n "Within reason."

    u "Everyone will be blinded by the trail I blaze to the point of speechlessness."

    n "That doesn't make any sense."

    hide uitto smirk
    show uitto smile

    u "It doesn't have to! My life, my rules."

    "She has stopped listening to reason. She's downright unreasonable."

    hide uitto smile
    show uitto smirk

    u "Mwahaha."
    u "Look out world, you're going to forget Uitto Hanatabe ever existed!"

    hide uitto smirk

    "I've created a monster."


    $ uTurn += 1
    $ Charm += 1
    return

label Uitto3:
    scene backgroundstage

    show uitto serious

    n "So, how's the trail blazing going?"

    "She glares at me with a thin frown."

    n "Your silence speaks volumes."

    hide uitto serious
    show uitto cringe

    u "I have no idea what to do."
    u "Before, I had no options and now I have significantly more. Way too many if you ask me."

    n "Oh no, whatever will you do?"

    hide uitto cringe
    show uitto smile

    u "I've decided to give theater another try."

    "She hands me a script to act as her scene partner."
    "I'm not that great of an actor, but she seems so excited."

    hide uitto smile

    menu:
        "Comedic":
            $ uRep += 1

            show uitto smile

            "I skim through the scene. The dialogue is pretty sappy."
            "I don't see how anyone can take this seriously. Granted, my well known bias against romantic dramas probably affects my decision."

            n "Lay down. Your arms."

            hide uitto smile
            show uitto serious

            u "Nagen, what are you doing?"

            n "I'm being. Dramatic."

            hide uitto serious
            show uitto cringe

            u "Dramatically overacting is more like it."

            n "You think that's overacting?"

            u "Oh no."

            "I take a knee and extend my arm to the sky."
            "In my worst attempt at a British accent, I proclaim..."

            n "If not on this night, then in. Your GRAVE!"

            "Nailed it."

            hide uitto cringe
            show uitto embarrassed

            u "No more, please."

            "She shields her face with her script."

            n "I see I have blinded you with my stage presence."
            n "Maybe I missed my calling?"

            hide uitto embarrassed
            show uitto smile

            u "No, absolutely not."

            "She's trying her hardest not to laugh."

            u "The only reason I'd root for the assassin in this scene would be to spare the audience."

            n "Oooh. And here I thought you were laughing with me, not at me."

            hide uitto smile
            show uitto cringe

            u "Your choices were just so... exaggerated."

            n "What else am I supposed to do? These lines are so corny."

            u "True, but at the same time, an actor has to set aside their bias and perform the role they're given to the best of their ability."

            n "...that was my best."

            hide uitto cringe
            show uitto

            u "That's why the problem was your choices, not your energy. You're just trying to have fun with it."
            u "I respect that. It's not like you're going to be on stage anytime soon."

            hide uitto

        "Improv":
            $ uRep -= 1

            show uitto smile

            n "Why don't you start us off?"

            hide uitto smile
            show uitto

            u "Oh. Okay, let's see..."

            "She flips back a few pages."

            hide uitto
            show uitto sad

            u "I've wandered these halls a thousand different ways. Something is a miss. Who goes there?"

            n "The dog, mostly."

            hide uitto sad
            show uitto talk

            u "What?"

            n "Though if you're referring to that shadowy figure, I think we're about to find out."

            u "Nagen, those aren't your lines."

            n "Nagen? Who's Nagen? Fair princess, you know this foul villain?"

            hide uitto talk
            show uitto yell

            u "If you didn't want to do this, you could have said so."

            n "I would never dream of leaving your side."

            u "Enough messing around, Nagen."

            n "Geez, lighten up a little, will ya?"

            hide uitto yell
            show uitto serious

            u "I get acting isn't the most ‘respectable' of professions, but the least you could do is humor me for a few minutes."
            u "Heaven knows I've done the same for you."

            hide uitto serious

    $ uTurn += 1
    $ Charm += 1

    show uitto talk

    n "You've got a lot of passion for this. The drama club is lucky to have you."

    u "I'm glad you think so. I was starting to think I was the only one."

    n "Did the theater kids recognize you?"

    u "Well, yeah, but it's not like they're scared of me or anything."

    n "A mistake, really."

    hide uitto talk
    show uitto serious

    u "They don't need to know that. No, they had an issue with me giving my fellow actors direction."
    u "Like, excuse me, I didn't spend eight years taking acting lessons to be in a show with amateurs."
    u "I don't care if it's not for an audience, if you're going to practice something, you have to practice it right."

    n "I thought drama club was for fun."

    u "That's exactly what they said."
    u "But that kind of lazy thinking is how bad performance habits form."
    u "There's no point in acting if you won't even bother to learn the basics like projecting or facing the audience! And you know what they told me when I said that?"

    n "What?"

    hide uitto serious
    show uitto cringe

    u "Stop being ‘dramatic'. And I was like, ‘are you trying to be ironic, because it isn't cute'."
    u "And they were serious. I just can't with those people. So I quit."

    n "You quit over that?"

    hide uitto cringe
    show uitto smirk

    u "Why not? It's not like I'm under contract to stay in that sinking ship of a club."
    u "Now I have to find something else to do. I really thought it'd be a good fit too."

    "She sighs."

    hide uitto smirk
    show uitto sad

    u "This sucks."

    "I never took her for the type to quit like that. She's always been so headstrong. This is a little creepy."

    n "What are you going to do now?"

    hide uitto sad
    show uitto talk

    u "I don't know. Maybe dance or something constructive like that. They say exercise is supposed to decrease stress or something like that."

    n "You stressed about something?"

    u "Me? No. I was just saying that because you're a walking ball of anxiety."
    u "I mean, look at you. You're too young to be going gray."

    n "Not gray, but fair. Can't really argue with that."

    hide uitto talk
    show uitto playful

    u "Really? I was just kidding."

    n "I mean, it's been a while since I've had a panic attack, but you never know when one's going to sneak up on you."

    "And now I've made her uncomfortable. Great, fantastic job."

    n "But you're never going to catch me dancing about it or something."

    hide uitto playful
    show uitto smile

    u "It's a shame. People would pay good money to see that."

    n "Hard pass. I'll stick to my videogames."

    hide uitto smile

    return

label Uitto4:

    show backgroundgym

    "It's been really hard to get a chance to hang out with Uitto. Everytime I asked, she was busy."
    "Finally, she texted me to meet her on the tennis court."
    "She's practicing her backhand swing."
    "It reminds me of our days on the battlefield. She wields her racket with the same ferocity she did with an ax."

    n "What happened to taking dance?"

    show uitto serious

    u "I'm garbage at choreography, always have been."
    u "Besides, I figured a bunch of meathead jocks would be more welcoming towards my competitive spirit."

    n "Well, I mean yeah, but you practically lived on the stage. I thought dancing was a part of your job."

    u "Ideally everyone wants a singing, dancing mascot to advertise their product. Rosette wasn't that lucky."
    u "Rinko could dance, Renge could sing, and I could make people think I did both. If you pay attention to the videos, you'll notice I mostly walk and pose."

    n "And the singing?"

    hide uitto serious
    show uitto playful

    u "Lip syncing to an auto tuned recording. I mean, it was still my voice, but it was heavily edited."

    n "I'm so disillusioned."

    hide uitto playful
    show uitto smile

    u "Oh, come off it. There's a reason you didn't know without me telling you. I put in the work to build up that public appearance."

    n "It still feels kinda cheap."

    hide uitto smile
    show uitto talk

    u "It's not cheap, it's a lifestyle, a methodology you eat, sleep, and breathe."
    u "Saying my performance was lacking because I was showcasing different skills is like saying you're stupid because you can't write a short story."

    n "I can too!"

    hide uitto talk
    show uitto playful

    u "How many times did you get in trouble for copying a story you read on accident instead of using your own ideas?"

    n "Forgive me for not knowing the difference. I was seven and the only thing I was trained to do was pass tests."

    hide uitto playful
    show uitto talk

    u "Exactly! Likewise, I was trained to win pageants. I wasn't prepared to defend my reputation after I won."
    u "So, I treated each performance like a challenge. No point in embarrassing yourself unless there's something to win."

    hide uitto talk

    menu:

        "Sounds Stressful":

            $ Charm += 1

            show uitto talk

            u "That's what most people say. I think It's kind of fun. You find what gets the best reaction and rack up brownie points until you get the best outcome."

            n "How do you know what the best outcome is?"

            u "You got to keep playing to find out."

            hide uitto talk
            show uitto sad

            n "I couldn't live like that. I need to have a clear goal, something definitive to reach too."
            n "I can't be on test mode twenty-four seven, it's too draining."

            u "Pfft, ‘test mode', really? You're such a nerd. But, I mean, I can see what you mean. At least with a test, you know when it's over."
            u "It's not the same with performing. There's always an audience, even if it's just you."

            "I can kind of understand that. Growing up, my one goal was to make my father happy. It was a fruitless venture, but that didn't stop me from trying."
            "It got to the point where even if he wasn't watching, I was still acting like he was."

            n "You getting philosophical on me, Hanatabe? Now who's the nerd?"

            hide uitto sad
            show uitto smile

            u "The person who can use ‘philosophical' in casual conversation."

            "She laughs."

            hide uitto smile

        "And if you lost?":
            $ uRep -= 1

            show uitto sad

            "She's quiet for a long time. The ball she was ramming against the wall rolls lifelessly along the ground."

            u "...I guess you're looking at it."

            "She picks up the ball and tosses it in the air, catching it in her hand."

            n "I don't follow."

            u "If you really suck at something, you just keep going until you find something you don't suck at and succeed at that."
            u "Can't sing, then become a great actress. Can't fight, then be intimidating. Got a sucky family, then find a new one."

            n "You make it sound so easy."

            hide uitto sad
            show uitto talk

            u "Nagen, you guys care about me more than my own mom, and she was the one who wanted to keep me. For the pageants."
            u "You can't dwell on your failures. It puts you in a dark place."

            n "Weren't you the one preaching to us about personal responsibility?"

            u "Taking corrective action is taking responsibility."

            "She smacks the ball with her racket."

            hide uitto talk
            show uitto

            u "You just have to not suck at it."

            hide uitto

        "I've always wanted to try":
            $ uRep += 1

            show uitto smile

            "She starts laughing."

            u "Try what?"

            n "Competing in one of those Proficiency pageants."

            "I expect her to keep laughing. Instead, she becomes rather somber."

            hide uitto smile
            show uitto sad

            u "You don't have what it takes. The best you could hope for is eighteenth place."

            n "Excuse me?"

            u "I'm just stating the obvious."
            u "Your Proficiency is dull, your look is generally unappealing, and the whole event is designed to pick the contestants apart. It'd give you an anxiety attack."

            n "If it was really that awful..."

            hide uitto sad
            show uitto talk

            u "It was my job, I wasn't expected to like it."

            n "At least you got paid when you were the best. I'd just get more tests."

            hide uitto talk
            show uitto sad

            u "...right."

            n "What happened to all that prize money?"

            hide uitto sad
            show Uittosadtalk

            u "...I don't know. I never thought of it as my money, so I didn't pay attention. It probably went back into the pageants."
            u "It wouldn't be totally hopeless for you. If we dyed your hair and then-"

            n "No, absolutely not, forget I said anything."

            hide Uittosadtalk
            show uitto playful

            u "t's your loss."

            hide uitto playful
    $ Charm += 1
    $ uRep += 1
    $ uTurn += 1

    show uitto
 
    n "You're pretty good with that racket."

    u "That's just because my target is a wall. I'm a mess on the court."

    n "Wait, really?"

    hide uitto
    show uitto talk

    u "I just feel like everyone's staring at me, waiting for me to mess up."

    n "What about everything you just said about competing and performing?"

    u "I wasn't alone then! Even during competitions, I was always sharing the stage with someone."
    u "Now I can't even get someone to play doubles with."

    "Wait a minute..."

    n "No one wants to partner up with you? That bothers you?"

    hide uitto talk
    show uitto embarrassed

    u "N-no! Of course not, that would be silly and childish."
    u "Besides, we're supposed to be laying low, so it's a good thing people are avoiding me. It's what I wanted..."

    n "You're not completely alone you know. You still have us."

    hide uitto embarrassed
    show uitto talk

    u "Don't start getting sappy on me, I know that. But, I mean, you're not going to want me-"
    u "You can't follow me around all the time, you need to have your own life."

    n "I'm not your babysitter. We're just hanging out. I just meant you have friends and- Oh god, that is sappy."

    u "See?"

    hide uitto talk
    show uitto smile

    "She laughs."

    u "I'll figure something out, you'll see. I just need to find something that's more suited for me."

    hide uitto smile
    return

label Uitto5:
    scene backgroundcourtyard

    show uitto smile
    
    "I believed Uitto when she said she'd figure something out."
    "For as long as I've known her, she's always had something in the works."
    "However, over the last few days, she's been rather quiet. After everything that's happened, I expected her to be more determined than ever to find her own path, but it's almost like she's given up."

    u "I've got it."

    n "Oh thank goodness. Wait, got what?"

    u "I know what I have to do. So, did you mean what you said?"

    n "On principle, I want to say yes, but what exactly are you referring to?"

    hide uitto smile
    show uitto talk

    u "When you said I could rely on you."

    n "Well, yeah."

    hide uitto talk
    show uitto smirk

    u "Then pack a bag. Nothing fancy, just the essentials."

    n "Oh god, who did you kill?"

    hide uitto smirk
    show uitto

    u "No one! Geez, give me a little credit, it's nothing that serious. Just meet me by the back fence when you're done."
    u "I'll explain everything later, just get your things."

    n "O-okay?"

    hide uitto
    
    scene backgroundfield

    "I followed her instructions to the letter. I found her waiting for me, backpack in hand."

    show uitto smile

    u "Good, you're ready."

    "She pulls at the bottom corner of the chain link fence. It was probably loose before she came here, but it's still amazing how easily she rolls up the metal."
    "With a wave of her hand, she ushers me to follow her through the opening."

    u "Come on, let's go."

    hide uitto smile

    #CG

    scene backgroundUPath

    n "Go? Go where?"

    u "....."

    n "Uitto, where are we going?"

    u "Does it matter?"

    "I dig my heels into the soft earth, but she keeps pulling me further away."

    n "Uitto, we can't just leave."

    u "Why not? Who says we have to stay here where no one wants us?"

    n "A lot of important people."

    u "Fuck them. They didn't give a crap about us until we started causing trouble. Who really cares if we disappear?"

    n "I'm not running away again, this is crazy. We don't have anywhere to go."

    scene backgroundlake

    show uitto sad

    u "I don't belong here, Nagen. No matter what I do, I can't break my old habits. There's no prize to be won here."
    u "I'm making an idiot of myself pretending like I could ever live a normal life."

    n "What the hell are you talking about?"

    hide uitto sad
    show Uittosadtalk

    u "No matter what I do or say, that stupid pageant programming comes back."
    u "I don't like it, I can't be that person, I don't want that life. If all I can do is perform in pageants or starve, I pick starve."

    n "Woah, woah. Who said anything about throwing you back into the pageant circuit?"

    u "I don't know anything else. I don't know how to throw away the last ten years of my life. I-I don't know what to do."

    "I am extremely uncomfortable around people when they're crying. It makes me painfully aware of my hands."
    "I don't know what to do with them and I have nothing helpful to say. I end up looking like a confused mime."
    "Uitto also happens to be doing the kind of crying most people reserve for the bathroom. That broken sort of half-choking type of crying that holds you in place."
    "She has a death grip on my wrist, like she'll be swallowed by the ground if she lets go."

    hide Uittosadtalk

    menu:
        "Be helpful":
            $ Charm += 1

            show Uittosadtalk

            "Yes, be helpful. The sensible thing to do."
                
            n "There, there..."

            "Nooo! That's the opposite of helpful, that's patronizing!"

            n "It just seems hopeless right now, cause you've been freaking out about it."

            "Yeah, just keep stating the obvious, dummy."

            n "You're not going to magically change into a different person overnight, it takes time."
            n "Besides, I like you for who you are; Hiro and Jona too."

            "Cool, cool. Going good. Finish strong."

            n "....."

            "Okay, you don't have to finish strong, just say something!"

            n "So stop trying to completely erase who you are. It's obviously stressing you out and it would suck to lose you."

            "Now she's crying even more. Crap!"

            n "Uh... it's okay."

            hide Uittosadtalk
            show uitto sad

            u "You don't have to keep freaking out. I'm fine."

            n "But you're still crying. I'm just trying to help."

            u "No, I get that and it's really sweet of you. But talking about it is making it worse."
            u "Just give me a few minutes to calm down, I'll be fine."

            "There isn't much else to do at this point. With no idea how long it will take, I sit down next to her."
            "We stayed that way for quite a while, her struggling to breathe and me waiting."

            hide uitto sad

        "Do nothing":
            $ uRep += 1

            show Uittosadtalk

            "I've never seen Uitto look so vulnerable before. It kinda freaks me out seeing her break down like this."
            "I can't just bail on her, but I don't really know what else to do."
            "So I just stand there speechless while she clings to my hand."

            hide Uittosadtalk
            show uitto talk

            u "S-sorry."

            "She stands up and dusts herself off."

            u "Didn't mean to just dump that on you. Ugh, you must think I'm pathetic, don't you?"

            n "What, no, not at all. You just gave me the blackmail fuel of the century, which I totally won't hold over your head till the end of time."

            hide uitto talk
            show uitto smirk

            u "Don't you dare, asshole."

            "Bitter as her words are, at least she's laughing."

            u "You may remember every embarrassing thing I've ever done, but I'm the expert in games of social chess, you won't win."

            "She sighs"

            hide uitto smirk
            show uitto sad

            u "At least, that used to be true. Now I'm not so sure."

            n "Ruining my reputation would be shooting fish in a barrel. If you want to flex your powers, target a teacher."

            hide uitto sad
            show uitto smile

            u "You are a horrible influence on me. It's no wonder I keep getting into trouble."

            n "It wasn't my idea to run away this time."

            u "....."

            u "By your logic, that makes this a colossally stupid move."

            hide uitto smile
            show uitto sad

            u "I already told you; I don't know what else to do."

            n "....."

            hide uitto sad
        "Stop crying":
            $ uRep -= 1

            show uitto serious

            u "W-what?"

            n "Stop crying right now."

            hide uitto serious
            show uitto yell

            u "Nagen! What the hell!?"

            n "You can be pissed off at me all you want, but for the love of god, please stop crying."
            n "It's... disconcerting."

            u "....."

            hide uitto yell
            show uitto smirk

            u "You are such a baby. ‘Oh no, I might catch emotion, make it stop'."

            n "That's not-"

            "Stop arguing, you'll only dig yourself in deeper."

            u "No, that is it, it's written all over your face. I made you uncomfortable; sue me."

            n "You need to have a clear head before making huge decisions that uproot your whole life."

            hide uitto smirk
            show uitto sad

            u "I'm never going to ‘clear my head' until I get out of here. That's why I need to leave."

            n "I already told you, that's a bad idea."

            hide uitto sad
            show uitto talk

            u "Who says I have to listen to you? We're not on the front lines anymore. You're not my boss."

            n "You don't have to listen to me, but I'm telling you as a friend, you're making a mistake."
            n "You need to calm down and think things through rationally."

            hide uitto talk
    $ Charm += 1
    $ uTurn += 1

    show uitto sad

    u "....."
    u "Do you think it's too late for me?"

    n "What do you mean?"

    u "This whole rehab program. It was made so adults didn't have to make hard decisions about our punishments."
    u "Truly ‘good' kids like Hiro will have no problems making it through the system, but I... Is it too late for me?"

    n "Woah no, that's..."

    hide uitto sad
    show Uittosadtalk

    u "No one's been able to give me a straight answer. When people talk about the girls from Rosette... they don't understand everything that led up to it."
    u "I hear them referred to as the druggie or the dead one and I remember Renge begging me to drop out before it was ‘too late'..."
    u "I should have listened to her sooner. If I did, maybe then I'd-"

    n "You're not doomed. I know it's exhausting to keep fighting against peoples' perception of you, but you can't give up."
    n "You've got to keep going. If not for yourself, then to give the middle finger to everyone that made you think you should give up."

    hide Uittosadtalk
    show uitto sad

    u "Seems a little petty, don't you think?"

    n "Most people are petty."

    hide uitto sad
    show uitto talk

    u "So what you're saying is stay at the school out of spite?"

    n "Damn straight. Make them regret making you feel shitty by being that much more awesome. Start a cult or read a self help book or something."

    hide uitto talk
    show uitto playful

    u "Start a cult? It's scary how often that's your go-to solution."

    n "Well, I mean, you like telling people what to do. Isn't that why you've been having problems in all these clubs?"
    n "Maybe you should try coaching instead of following."

    hide uitto playful
    show uitto talk

    u "Coaching? Coaching who, in what?"

    n "There has to be people at this school that want to make it in the circuits. You could mentor them and take them over from the inside."

    hide uitto talk
    show uitto smirk

    u "You are truly diabolical, y'know that? Flooding the industry with a bunch of mini-me's would be disastrous."
    u "Still... it would be nice to have someone learn from my mistakes. I wonder if this is how Renge felt."

    "She's calmed down quite a bit."

    n "Cool, so we can forget about the whole running away thing?"

    hide uitto smirk
    show uitto

    u "For now. Come on, let's go back before they've noticed we're gone."

    hide uitto

    return

label UittoF:
    "Uitto must be busy right now."
    return