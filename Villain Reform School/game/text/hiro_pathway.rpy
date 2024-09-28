label HiroVisit:

    if hTurn == 0:
        jump Hiro1
    elif hTurn == 1:
        jump Hiro2
    elif hTurn == 2:
        jump Hiro3
    elif hTurn == 3:
        jump Hiro4
    else:
        jump HiroF

label Hiro1:
    scene backgroundhall1

    show HHappy

    h "Hey dude, long time no see."

    n "You just saw me not too long ago."

    hide HHappy
    show HBase

    h "Yeah, but that was like, in passing."
    h "I haven’t actually talked to you in forever."

    n "We never really talked much before."
    n "It was mostly you daring yourself to do stupid stuff and then doing said stupid stuff."

    hide HBase
    show HGrump

    h "Hey! Quit judging 10 years old me’s life decisions."
    h "One of them was being your friend."

    n "Alright, alright; but I mean running down the entrance handrail was a pretty stupid idea."

    hide HGrump
    show HHappy

    h "For a normal kid maybe, but I’m a Vigor Major, we’re built of stranger stuff."

    hide HHappy
    show HHeadempty

    h "Or a least I am."

    n "I’ve been meaning to ask you, how are Vigor Proficiencies, well, Proficiencies?"

    hide HHeadempty
    show HTALK2

    h "How do you mean?"

    n "Well your Proficiency is Durability, but that’s not a skill, you can’t improve how dense your bones are."
    n "It’s just a part of you, it’s how you were born."

    h "Well yeah, but like, there are things I can do that others can’t"
    h "It’s an advantageous."

    n "Don’t you mean an advantage?"

    hide HTALK2
    show HTALK1

    h "Whatever, but you get what I mean right?"
    h "There was a guy in my class with microscope eyes, but like he’s able to make all this tiny stuff without extra tools. Does that make sense?"
    h "Why the sudden interest?"

    hide HTALK1

    menu: 
        "I'm worried about you.":
            $ Vigor += 1

            show HSuppress
            
            h "Run that by me again?"

            n "I have no idea what will happen to you once we get out of school."
            n "I mean when we were kids, you wanted to be the leader of the Power Rangers."
            n "And it’s not like your Proficiency…"

            hide HSuppress
            show HShame

            h "Yeah, I get it… Ha ha…"

            hide HShame
            show HSass

            h "Dude, I have no idea what I’m going to do."
            h "I, uh, I didn’t think I’d make it this far."

            n "When we got caught or…"
            
            hide HSass
            show HSadtalk

            h "I mean in general."
            h "When Guwon went to shit, I was kind of relieved."
            h "Like the apocalypse was here, nothing mattered anymore, all we had to do was survive."
            h "That I was good at, surviving that is."

            n "Yeah, as much as I ripped on you for being irresponsible, you were really cool on the field."

            "He was our self proclaimed leader, a real ass about it, but he did a good job of keeping us safe when things went south. It also helped that he knew how to cook."

            hide HSadtalk
            show HHappy

            h "Right!? I was freaking awesome."
            h "Now we’re back to square one and I don’t know man."
            h "It’s not like the old days where I can just copy over your shoulder."
            h "We’re not in any of the same classes anymore."

            n "Yeah, I know what you- Wait. You copied off me?"

            hide HHappy
            show HSadSmile

            h "Or compared answers, whatever makes you sleep better at night."

            n "Dude!"

            hide HSadSmile
            show HMad

            h "They wouldn’t keep me in the program if I got bad grades, I couldn’t risk getting kicked out."

            n "You can’t keep slacking off like that."

            hide HMad
            show HJudge

            h "Slacking off!?"
            h "It takes me ten, scratch that, twenty times longer than you to learn something from a stupid book; and that’s all they gave us."

            "He does have a point. I only have to read something once to learn it. The only time I have to drill stuff is if I learned it incorrectly the first time."

            n "The ability to master a multiple choice test becomes obsolete after collage."
            n "You should figure out what your working toward first."
            n "That’s what’s going to motivate you when you have to study."

            hide HJudge
            show HHeadempty

            h "All I know is I don’t want to be stuck waiting tables the rest of my life. I’m so boned."

            n "You’re not boned dude."
            n "Come on, let’s do something to take your mind off it. I feel bad digging up all this anxiety."

            "I’m really worried about him. If he can’t figure out what he wants to do, it won’t matter whether or not he gets out of this mess."

            h "Yeah…"

            hide HHeadempty

        "I want to switch majors.":
            $ hRep += 1

            show HGuilt

            h "What!? Why?"

            n "I’m painfully aware of how mundane any ability is."
            n "I need to think of ways to utilize it outside of exams."

            hide HGuilt
            show HGrump

            h "...right...And you jumped from that to me because…"

            n "Other than being the only Vigor major I know."
            n "I need help brainstorming some ideas."
            n "You’ve always had the most off the wall plans, I figured you’d be a good place to start."

            hide HGrump
            show HTALK2

            h "Woah- Woah, wait. You’re asking me for help?"

            n "Kind of. I retain the right to reject anything that could get me killed."

            hide HTALK2
            show HSmug

            h "Say it."

            n "Say what?"

            h "Say ‘Hiro I need your help’."

            hide HSmug
            show HHappy

            h "Oh! And you’re not allowed to say any of my ideas are dumb."

            "This was a mistake."

            hide HHappy
            show HSmug

            h "Say it. Say it. Say it."

            n "It."

            hide HSmug
            show HSulk

            h "Not that smart ass."

            n "Fine~ Hiro, I need your help."

            "He pressed a button on his phone with a wicked grin."

            n "Hiro, I need your help."
            n "What was that?"

            hide HSulk
            show HSmug

            h "My new ringtone."

            n "What!? No! Hand it over!"

            "He’s going to be guarding that stupid thing like his life depended on it."

            hide HSmug

        "No reason":
            $ hRep -= 1

            show HSulk
            
            h "...Bullshit."

            n "Hey!"

            hide HSulk
            show HJudge

            h "You’re up to something, spill."

            n "I told you, it’s nothing."

            h "It’s not nothing. You never ask something just ‘cause. What is it?"

            n "I already told you."

            hide HJudge
            show HInsulted

            h "Do you not trust me or something, is that it?"

            n "Dude just drop it, it’s nothing."

            hide HInsulted
            show HGrump

            "He glared at me."

            h "You’re a really shitty liar, you know that?"

            n "Why does it matter?"

            h "Because you’re hiding something and I don’t know what it is."
            h "Ever since we got here you’ve been super jumpy and writing it off as nothing."

            n "I swear, there’s nothing to worry about."

            hide HGrump
            show HGuilt

            h "Dude, the last time you did shit like this, you had a breakdown."

            n "Don’t remind me."

            "I’m not historically the best in high pressure situations."
            "Though to be fair, at the time I was twelve, my teammates were missing and I was lost in a war zone."
            "So I’d appreciate if he gave me a little more credit."

            h "I have a right to be worried. You do this all the time. I don’t want you to get stuck, y’know."

            "Easy for him to say. And again, more credit would be appreciated."

            n "I swear everything is fine."

            hide HGuilt
            show HHeadempty

            h "Right, sure it is."

            hide HHeadempty
    $ Vigor += 1
    $ hTurn += 1

    show HBase

    h "Hey, I saw a vending machine on the third floor. Bet you I can get us some free candy."

    n "Please don’t."

    hide HBase

    "I had to help him pull his arm out of the bottom of a vending machine before any staff found us. It’s strange, even years later, I still end up being his handler."
    "If he expects me to do this out of school, he needs to start paying me."
    return
label Hiro2:
    scene backgroundstuco

    show HHappy

    h "Dude, have you seen the dorms? It’s so nice to finally have my own space again!"

    n "Right, you mentioned before the group home they sent you had a couple of kids."

    hide HHappy
    show HInsulted

    h "There’s six of us in the same house and they want us to all get along like a family, but they’re all kids like me, so that doesn’t always work out."

    n "I’m sorry to hear that."

    hide HInsulted
    show HSadSmile

    h "It’s really not that bad. My bunkmate Ryota’s been helping me with my hero training."

    "He hasn’t given up on that?"

    n "What do you mean hero training?"

    hide HSadSmile
    show HSadtalk

    h "Well I kinda messed up being a hero the first time, and I was trying to figure out where I went wrong and then it hit me."
    h "Hercules, King Arthur, Krysta; what did they have in common?"

    n "Those are all from cartoons."

    hide HSadSmile
    show HSuppress

    h "No… Well, yeah, but not what I was going for."

    hide HSuppress
    show HHappy

    h "Mentors man!"
    h "They all had people who taught them how to hero. That’s what I was missing!"
    h "I mean, Lethe was nice and supportive, but she didn’t really teach us what to do."

    "I mean, he’s not wrong, but at the same time, I don’t feel like he’s quite getting the whole picture here."

    hide HHappy
    show HBase

    h "So Ryota’s been helping me out!"
    h "We’ve been doing strength training, lessons and running through scenarios."
    h "Our biggest focus lately is thinking outside the box; how doing things you normally would do isn’t always a good thing."
    h "It’s been really helpful, you should try it."

    n "Okay…"

    hide HBase
    show HTALK1

    h "Scenario: You’re trapped in a room on fire with your best friend; what do you do?"

    menu:
        "Put out the fire.":
            $ Vigor += 1

            show HPout

            h "Well yeah, obviously, but how?"
            h "This room doesn’t have a fire extinguisher."

            n "You never said that."

            hide HPout
            show HJudge

            h "Just look around you, where’s an extinguisher."

            n "Wait, you meant this room?"

            hide HJudge
            show HSass

            h "Duh, it’s a scenario."

            "I forgot how literal he can be."

            n "Then I’d engage the sprinkler system."
            n "There’s also an alarm near the teachers desk, which would call 911 for us."

            hide HSass
            show HMad

            h "Boring!"

            n "Being a hero isn’t always the most exciting choice."
            n "It’s about making the best one."

            hide HMad
            show HTALK1

            h "That’s easy to say when you have warning, but in the heat of the moment, anything could happen."

            n "Please stop with the puns, I beg you."

            hide HTALK1
        "Shield my friend from the fire.":
            $ hRep += 1

            show HEmbarrassed

            h "W-what?"

            n "I’m wearing mostly leather, so it should work long enough for the sprinklers to go off."

            h "B-but you really don’t have to do that. You could try to stop the fire or call for help."

            n "Well yeah, I might do those thing afterward, but that’s not what I’d do first."

            "What’s gotten into him?"

            n "You asked what I’d do, that’s what I’d do."

            hide HEmbarrassed
            show HBlush

            h "I mean, yeah, that… that makes sense. Wait, no! You’re missing the point."

            n "Hunh?"

            hide HBlush

        "Refuse to answer.":
            $ hRep -= 1

            show HMad

            n "I don’t have enough information to answer the question."

            h "What more do you need to know? The room’s on fire."

            n "How did the fire start? Why didn’t the alarms go off?"
            n "Is there smoke involved? What is the substance on fire?"
            n "Are there any explosives involved? How exactly are we trapped in the room?"

            hide HMad
            show HSerious

            h "Dull, dull, dull. Don’t you know anything about heroism? You’ve got to be a man of action!"

            n "All I’m asking for is a little verisimilitude."
            n "Things don’t happen at random, there has to be a reason."

            hide HSerious
            show HSass

            h "And in the time you complained about versachi we both died."

            n "You mean verisimilitude."

            hide HSass
            show HMad

            h "Now the rest of the building’s on fire!"

            n "You don’t know what that word means, do you?"

            h "You gotta do something fast, we’re getting crispy."

            n "You just said we died!"

            hide HMad
    $ Vigor += 1
    $ hTurn += 1

    show HMad

    h "You’re missing the point."
    h "The idea is to do something you usually wouldn't do. It’s the only way to change."

    n "Okay, what would you do then?"

    hide HMad

    "I shouldn’t have asked that. If I had thought about it for even a second, I wouldn’t have."
    "He opened the window, I had enough time to acknowledge we were on the third floor before he picked me up and jumped out."
    
    scene backgroundHPath

    n "aaaaAAAAHHHH!"

    h "It’s cool, if the pool doesn’t break your fall, I will."

    scene backgroundHPath2

    n "AAHHHHH!"

    "We hit the water and everything left my mind except the need for air."
    "When we finally breached the surface, I thrashed blindly around trying to hit him"
    
    scene backgroundpond

    n "WHAT THE FRESH HELL WAS THAT FOR!?"
    n "We could have died!"

    show HHappy

    h "That’s why we jumped out the window!"

    n "I can’t believe you jumped out the window. Don’t you ever picked me up like that again!"

    hide HHappy
    show HSmirk

    h "How do you want me to pick you up?"

    n "That’s not what I meant and you know it! And you ruined my favorite jacket!"

    "I sloshed out of the pool with an embarrassing squelch."

    h "I can always get you a new jacket, I can’t get a new you."

    n "Just think things through next time."

    hide HSmirk

    "I really can’t stay mad at him. He means well, but we can’t keep doing stupid stuff like this."
    "This was a very expensive jacket."

    return
label Hiro3:
    scene backgroundfield

    show HSadtalk

    h "You got a minute? There’s something I want to show you."

    "He lead me to the practice field."
    "Along the back fence was a pile of old timber, likely from when they gutted the interior of the building."
    "It was just tall enough that Hiro was able to pull himself over the top of the fence."

    h "This way."

    "I’m not sure leaving school grounds is the best idea."

    hide HSadtalk

    menu:
        "Stay behind":

            show HPout

            n "Look dude, we just got here. I can’t go running off school grounds like this."

            h "But-"

            n "No, if it’s off campus, it has to wait."

            hide HPout
            show HSadtalk

            h "Suit yourself."

            "He left without me."

            hide HSadtalk

            return
        "Follow":

            show HSadtalk

            n "What’s so important outside?"

            h "You’ll see."

            hide HSadtalk
    #BG city

    scene backgroundtown

    "I stumbled after him for about fifteen minutes through the woods before we finally reached the city surrounding our school."
    "At any other academy, you’d be able to take trips into town to go out to eat or shop. But this place…"

    n "It’s a ghost town."

    show HSerious

    h "Sixty percent of the country is still like this. It’s taking forever to rebuild everything."

    "He sat down amongst the wreckage, I soon followed suit."

    hide HSerious
    show HSadtalk

    h "I used to think I was made for this world."
    h "The fucked up one where all there was, was survival or death."
    h "I’m good at surviving Nagen, damn good. It’s the only thing I’ve known."

    "I used to think Hiro was a clumsy, obnoxious idiot. He’s still obnoxious, but the other things weren’t his fault."
    "He may have forgotten how many times he told us he fell down stairs, but I didn’t."

    hide HSadtalk
    show HSadSmile

    h "But I don’t belong here, no one does, we just had to put up with it."
    h "I’m not proud of what I did to get by, but there’s nothing stopping us from making it better."

    n "Us?"

    hide HSadSmile
    show HConfess

    h "You’re the smartest guy I know, maybe ever."
    h "I want to make better choices now, but I still need a lot of help."
    h "It’s hard for me to think further into the future than a single day."
    h "It’s just not how I was trained. Do you… is it just me?"

    "I looked back at what remained of the town."
    "When the world is collapsing all around you, it’s hard to picture anything else."
    "I’ve been running around trying to pin the blame on someone, but that isn’t going to get me anywhere."
    "I want things to change, but do I have to change myself to do it?"

    hide HConfess

    menu:
        "I'm not the problem.":
            $ hRep -= 1

            show HGuilt

            n "It’s just you."

            h "Oh."

            n "And where’s all this nonsense about needing to change?"
            n "Just because you don’t know what to do anymore doesn’t mean I’m going to make those decisions for you."

            hide HGuilt
            show HSerious

            h "That’s not what I meant."
            h "I mean, like, making the right decision is hard. I don’t want to mess this up."

            n "There is no such thing as ‘the right’ decision, just my decision."
            n "Whether or not people agree with it is not my problem."
            n "You’ll sleep a lot better at night if you accept that."

            hide HSerious
            show HJudge

            h "You don’t seriously think everything we did was okay?"
            h "People got hurt because of us."

            n "It’s a good thing you care, because no one else does"
            n "It’s all about the money and the publicity with these people."
            n "This chaos makes them look good, so they’ll keep watching and doing nothing to change it."

            hide HJudge
            show HMad

            h "That doesn’t mean you have to be the same way."

            hide HMad

        "I don't know.":
            $ hRep += 1

            show HThisisfine

            n "I don’t know man, I struggle to think past the hour. I had to learn the big picture stuff the hard way."
            n "You’ll do fine man. You’re trying, that’s what matters."

            h "Big picture stuff, hunh?"

            n "Yeah, like where you want to see yourself in five years, junk like that. It doesn’t come naturally."
            n "Most people pretend like they know until they actually figure it out. If they figure it out at all."

            hide HThisisfine
            show HSadtalk

            h "I don’t know man…"

            n "Just try it. What do you want to be able to do five years from now?"

            hide HSadtalk
            show HHeadempty

            h "Honestly? Eat as much pizza as I want and play videogames."

            n "Great, reasonable goal, I like it."
            n "Now all you have to do is think backwards until you make it to today." 
            n "As long as you get to do the things you want to do, you’ll have made it."

            hide HHeadempty
            show HSulk

            h "Cool, now all I gotta do is find a job I don’t hate, one that’s cool with ex-convicts and, y’know, graduate."
            h "That’s not stressful at all."

            n "Dude, don’t drop sarcasm during a heartfelt moment."
            n "That’s my job."

            hide HSulk
        
        "I have to change.":
            $ Vigor += 1

            show HSass

            n "The trick is changing without changing."
            n "I know they say fake it til you make it, but faking it is exhausting."

            h "Tell me about it…"
            h "Do you think it’s too late to learn German?"

            hide HSass
            show HTALK1

            h "I’m pretty sure no one knows who we are in Germany."

            n "Germany’s not a third world country, they have international new"

            hide HTALK1
            show HHappy

            h "No, it’s perfect. We just nope out of the country, change our names, and we’ll be set. Full do over!"

            n "...In Germany?"

            h "Yeah!"

            n "Why Germany?"

            hide HHappy
            show HBase

            h "If I’m going to bail, might as well go big."
            h "Would have gone with England, but I can’t stand that much rain and it’s too expensive for me."

            "I’m pretty sure that apocalypse hit everywhere, but it’s a nice thought."

            n "Running away would be easier."

            h "Yeah… but it’s not going to fix anything."

            n "We’ll keep that as a plan ‘B’."
            
            hide HBase
    
    $ Vigor += 1
    $ hTurn += 1

    show HSadtalk

    h "Things were so much easier when this kind of stuff happened on TV."
    h "There wasn’t any of this morally grey bullshit."
    h "You just had bad guys and good guys, and the good guys always won."
    h "That’s the kind of hero I wanted to be."

    "I believed what we did was necessary, righteous even, but I wouldn’t classify it as heroic."
    "Last I checked, leading a city under the martial law of a brain washed horde was not in the hero commandments."
    "Not that there are hero commandments, but if there were, it wouldn’t be one of them. There really should be-"

    hide HSadtalk
    show HThisisfine

    h "Nagen! You’re spacing out again; come back to the present."

    n "Sorry, got a little side tracked, but seriously, the only place those kinds of heroes belong is on TV."
    n "If you want to be like them, become an actor, not a vigilante."

    h "Hey, don’t go counting me out just yet."
    h "I’m going to be a real hero someday, you’ll see."

    "Standing here is depressing."
    "We went back to campus without anyone noticing we left."

    hide HThisisfine

    return
label Hiro4:

    scene backgroundcourtyard

    show HTALK2

    n "What did you do?"

    h "Why do you always assume I did something?"

    n "Well, it’s physically impossible to do nothing."
    n "Technically, you’re doing something right now. I was merely asking if there was something you did, past tense."

    hide HTALK2
    show HSass

    h "Okay, okay, I get it. Enough dicktionary talk."

    "I feel insulted; but I have no way to prove he said what I think he said."

    n "What did you do?"

    show HHeadempty

    h "I kinda have detention."

    n "How’d you manage to get detention? We haven’t even been here that long."

    hide HHeadempty
    show HPuppy

    h "You remember how we jumped into the pool. Super awesome, right?"

    n "I don’t remember it being remotely awesome."

    hide HPuppy
    show HSuppress

    h "Yeah… You’re not the only one who thought that."

    n "Bit you in the butt that fast?"

    h "Yeah, something about reckless endangerment, not a good example; blah, blah, blah."

    n "It’s like I’ve been telling you, we’re not little kids fighting to impress Odori anymore, we can’t do shit like that."

    hide HSuppress
    show HJudge

    h "Why would I want to impress Odori?"   

    "Hunh?"

    hide HJudge
    show HHmmm

    n "You’re kidding me right? We were fighting over her all the time."
    n "The prank wars?"
    n "Trying to be leader?"
    n "That thing with the goat?"

    hide HHmmm
    show HHeadempty

    "He stared at me like I was a lunatic."

    n "You’re kidding me, right? Come on, every time I tried to hang out with her, you’d butt in."

    hide HHeadempty
    show HEmbarrassed

    h "Oh, y-you noticed that?"

    n "Hard not to."
    n "You weren’t exactly subtle about it."

    hide HEmbarrassed
    show HConfess

    h "It’s not like I was doing it on purpose or anything."

    n "You just happened to hang out with her all the time?"

    hide HConfess
    show HJudge

    h "Well yeah, but why does that matter now?"

    "I know logically this doesn’t change anything. We were just dumb kids, and she’s gone, but still if I had known…"

    n "I never got the chance to tell her how I felt. I can’t help feeling a little jaded."

    hide HJudge
    show HSerious

    h "Come on man, she knew how you felt… Everyone did."

    "I didn’t mean to make him feel bad."

    h "Even if I hadn’t done anything, would you have?"

    n "What do you mean?"

    h "We were all just friends, the five of us, working for the greater good."
    h "Doing something like that might have messed it up. Would it really have been worth it?"

    hide HSerious

    menu:
        "Yes":
            show HSerious

            n "It couldn’t hurt to try."
            n "I would rather get an honest answer then spend my life speculating on the possibilities."
            n "Besides, we were friends, it would take more than a goofy confession to mess that up."

            hide HSerious
            show HConfess

            h "Yeah… You really mean that?"

            n "Of course."

            "He took a deep breath. After a while, he couldn’t look me in the eye."

            h "It isn’t… wasn’t Odori I was trying to impress."

            "He finally looked at me."

            n "Oh."
            n "Ohhh…"
            n "Wait, what are you saying?"

            hide HConfess
            show HEmbarrassed

            h "Please don’t make this harder, it’s embarrassing enough as it is."

            "This is a joke, right? I mean, there’s no way. I try laughing, but it doesn’t make any of this less awkward."

            hide HEmbarrassed
            show HSadSmile

            h "I’m serious, I would have done anything to make you look at me the way you looked at her."

            hide HSadSmile
            menu:
                "Accept":
                    $ hRep += 5

                    show HShame

                    n "And, uhh… how do you feel now?"

                    h "...The same. Is that… Is that okay?"

                    "I shouldn’t be this surprised. I just never thought about this sort of thing."
                    "Odori was everything I thought I was supposed to want; pretty, intelligent, and demure. We fought endlessly to be in the spotlight of her stage."
                    "I was looked back on those days with fondness, but is it because of her… or him?"

                    n "Yeah… It’s a little more than okay."

                    show HBlush

                    h "Really!?"

                    n "I just need some time to think about things."

                    hide HBlush

                "Reject":

                    show HSadSmile

                    n "But that was a long time ago, right?"

                    hide HSadSmile
                    show HGuilt

                    "Please tell me this isn’t a thing. I really don’t have time to deal with this right now."

                    h "R-right ancient history. No big deal, really."

                    "A wave of relief washed over me, but I could tell he was disappointed."

                    hide HGuilt
                    show HThisisfine

                    h "I didn’t make things weird, did I?"

                    n "No. No man, we’re cool."

                    hide HThisisfine

        "Probably Not":

            $ hRep += 1

            show HWait

            n "You’re right. Stirring up that stuff would have caused nothing but trouble."

            h "Yeah, best to leave things the way they are."

            n "That’s surprisingly level headed coming from you, I’m impressed."

            hide HWait
            show HJudge

            h "Really, that’s what it takes to impress you!? You’re such a nerd."

            n "Hey! You’re the one who’s notorious for bad judgment."
            n "Sue me for trying to be a good influence on you."

            hide HJudge
            show HHappy

            h "Why start now? Honestly, what did I ever see in you."

            "We laughed, unable to keep up the pace."

            h "I think I know what I’m going to do once we get out of here."
            h "I’m going to be a Power Ranger!"

            n "That again? You do realize they aren’t real, right?"

            hide HHappy
            show HBase

            h "No man, like an actor."
            h "I always wanted to be like the heroes on TV, but those kinds of heroes only exist on TV."
            h "If that’s the case, that’s where I’ll go. I’ll be able to do my own stunts, and I won’t get injured nearly as much as a regular stunt double."
            h "I’ll be the best ranger there ever was!"

            n "You’ve really thought this through."

            hide HBase
            show HTALK1

            h "I just need to get the right experience. Maybe I could apply to an amusement park or something."
            h "Y’know practice being around an audience. Start small."

            "It’s not exactly what I expected, but I’m glad he’s found something he wants to do."

            hide HTALK1

        "I won't forgive you":
            $ hRep -= 1

            show HSuppress

            n "If I had confessed, and by some miracle she accepted, I might have been able to spend more time with her."
            n "I could have been with her when Guwon came crashing down around us."

            h "How is… I wasn’t with her either. You chose-"

            n "I got stuck running around the city snipping people from skyscrapers, you made sure of that!"
            n "You put everyone on the front lines and didn’t have the decency to make sure our base was protected!"

            hide HSuppress
            show HSerious

            h "Odori was in charge of protecting the base, she volunteered to do it and I stand by that decision."
            h "I’m sorry that hurt your feelings, but that has nothing to do with us dicking around as kids."
            h "It’s been over a year since then-"

            n "My memories don’t fade like your’s do. I can’t bury my feelings under maturity and time."
            n "I can’t shake how much I cared about her, or how much she didn’t, or what I could have done differently."
            n "Confessing may have only given me closure, but you took that away."

            hide HSerious
            show HFINE
            h "I didn’t stop you from doing anything. This… now’s not a good time for this."

            hide HFINE

    show HSadSmile

    h "Shoot! I’m going to be late!"
    
    n "Take the East stairwell in the back of the building, you can still make it if you book it."

    hide HSadSmile
    show HHappy

    h "Thanks! Sorry we couldn’t talk more, but I gotta go."

    hide HHappy

    return
label HiroF:
    scene backgroundclass

    show HSadSmile

    h "Sorry Nagen, I can't skip out on detention again. I'll talk to you later."

    hide HSadSmile
    return