label HiroVisit:

    if hTurn = 0:
        jump Hiro1
    elif hTurn = 1:
        jump Hiro2
    elif hTurn = 2:
        jump Hiro3
    elif hTurn = 3:
        jump Hiro4
    elif hTurn = 4:
        jump Hiro5
    else:
        jump HiroF

label Hiro1:
    scene backgroundhall1

    h "Hey dude, long time no see."

    n "You just saw me not too long ago."

    h "Yeah, but that was like, in passing."
    h "I haven’t actually talked to you in forever."

    n "We never really talked much before."
    n "It was mostly you daring yourself to do stupid stuff and then doing said stupid stuff."

    h "Hey! Quit judging 10 years old me’s life decisions."
    h "One of them was being your friend."

    n "Alright, alright; but I mean running down the entrance handrail was a pretty stupid idea."

    h "For a normal kid maybe, but I’m a Vigor Major, we’re built of stranger stuff."
    h "Or a least I am."

    n "I’ve been meaning to ask you, how are Vigor Proficiencies, well, Proficiencies?"

    h "How do you mean?"

    n "Well your Proficiency is Durability, but that’s not a skill, you can’t improve how dense your bones are."
    n "It’s just a part of you, it’s how you were born."

    h "Well yeah, but like, there are things I can do that others can’t"
    h "It’s an advantageous."

    n "Don’t you mean an advantage?"

    h "Whatever, but you get what I mean right?"
    h "There was a guy in my class with microscope eyes, but like he’s able to make all this tiny stuff without extra tools. Does that make sense?"
    h "Why the sudden interest?"

    menu: 
        "I'm worried about you.":
            $ Vigor + 1
            
            h "Run that by me again?"

            n "I have no idea what will happen to you once we get out of school."
            n "I mean when we were kids, you wanted to be the leader of the Power Rangers."
            n "And it’s not like your Proficiency…"

            h "Yeah, I get it… Ha ha…"
            h "Dude, I have no idea what I’m going to do."
            h "I, uh, I didn’t think I’d make it this far."

            n "When we got caught or…"

            h "I mean in general."
            h "When Guwon went to shit, I was kind of relieved."
            h "Like the apocalypse was here, nothing mattered anymore, all we had to do was survive."
            h "That I was good at, surviving that is."

            n "Yeah, as much as I ripped on you for being irresponsible, you were really cool on the field."

            "He was our self proclaimed leader, a real ass about it, but he did a good job of keeping us safe when things went south. It also helped that he knew how to cook."

            h "Right!? I was freaking awesome."
            h "Now we’re back to square one and I don’t know man."
            h "It’s not like the old days where I can just copy over your shoulder."
            h "We’re not in any of the same classes anymore."

            n "Yeah, I know what you- Wait. You copied off me?"

            h "Or compared answers, whatever makes you sleep better at night."

            n "Dude!"

            h "They wouldn’t keep me in the program if I got bad grades, I couldn’t risk getting kicked out."

            n "You can’t keep slacking off like that."

            h "Slacking off!?"
            h "It takes me ten, scratch that, twenty times longer than you to learn something from a stupid book; and that’s all they gave us."

            "He does have a point. I only have to read something once to learn it. The only time I have to drill stuff is if I learned it incorrectly the first time."

            n "The ability to master a multiple choice test becomes obsolete after collage."
            n "You should figure out what your working toward first."
            n "That’s what’s going to motivate you when you have to study."

            h "All I know is I don’t want to be stuck waiting tables the rest of my life. I’m so boned."

            n "You’re not boned dude."
            n "Come on, let’s do something to take your mind off it. I feel bad digging up all this anxiety."

            "I’m really worried about him. If he can’t figure out what he wants to do, it won’t matter whether or not he gets out of this mess."

            h "Yeah…"
        "I want to switch majors.":
            $ hRep + 1

            h "What!? Why?"

            n "I’m painfully aware of how mundane any ability is."
            n "I need to think of ways to utilize it outside of exams."

            h "...right...And you jumped from that to me because…"

            n "Other than being the only Vigor major I know."
            n "I need help brainstorming some ideas."
            n "You’ve always had the most off the wall plans, I figured you’d be a good place to start."

            h "Woah- Woah, wait. You’re asking me for help?"

            n "Kind of. I retain the right to reject anything that could get me killed."

            h "Say it."

            n "Say what?"

            h "Say ‘Hiro I need your help’."
            h "Oh! And you’re not allowed to say any of my ideas are dumb."

            "This was a mistake."

            h "Say it. Say it. Say it."

            n "It."

            h "Not that smart ass."

            n "Fine~ Hiro, I need your help."

            "He pressed a button on his phone with a wicked grin."

            n "Hiro, I need your help."
            n "What was that?"

            h "My new ringtone."

            n "What!? No! Hand it over!"

            "He ran off before I could catch him. He’s going to be guarding that stupid thing like his life depended on it."
        "No reason":
            $ hRep - 1
            
            h "...Bullshit."

            n "Hey!"

            h "You’re up to something, spill."

            n "I told you, it’s nothing."

            h "It’s not nothing. You never ask something just ‘cause. What is it?"

            n "I already told you."

            h "Do you not trust me or something, is that it?"

            n "Dude just drop it, it’s nothing."

            "He glared at me."

            h "You’re a really shitty liar, you know that?"

            n "Why does it matter?"

            h "Because you’re hiding something and I don’t know what it is."
            h "Ever since we got here you’ve been super jumpy and writing it off as nothing."

            n "I swear, there’s nothing to worry about."

            h "Dude, the last time you did shit like this, you had a breakdown."

            n "Don’t remind me."

            "I’m not historically the best in high pressure situations."
            "Though to be fair, at the time I was twelve, my teammates were missing and I was lost in a war zone."
            "So I’d appreciate if he gave me a little more credit."

            h "I have a right to be worried. You do this all the time. I don’t want you to get stuck, y’know."

            "Easy for him to say. And again, more credit would be appreciated."

            n "I swear everything is fine."

            h "Right, sure it is."
    $ Vigor + 1
    $ hTurn + 1

    h "Hey, I saw a vending machine on the third floor. Bet you I can get us some free candy."

    n "Please don’t."

    "I had to help him pull his arm out of the bottom of a vending machine before any staff found us. It’s strange, even years later, I still end up being his handler."
    "If he expects me to do this out of school, he needs to start paying me."
    return
label Hiro2:
    scene backgroundstuco

    h "Dude, have you seen the dorms? It’s so nice to finally have my own space again!"

    n "Right, you mentioned before the group home they sent you had a couple of kids."

    h "There’s six of us in the same house and they want us to all get along like a family, but they’re all kids like me, so that doesn’t always work out."

    n "I’m sorry to hear that."

    h "It’s really not that bad. My bunkmate Ryota’s been helping me with my hero training."

    "He hasn’t given up on that?"

    n "What do you mean hero training?"

    h "Well I kinda messed up being a hero the first time, and I was trying to figure out where I went wrong and then it hit me."
    h "Hercules, King Arthur, Krysta; what did they have in common?"

    n "Those are all from cartoons."

    h "No… Well, yeah, but not what I was going for."
    h "Mentors man!"
    h "They all had people who taught them how to hero. That’s what I was missing!"
    h "I mean, Lethe was nice and supportive, but she didn’t really teach us what to do."

    "I mean, he’s not wrong, but at the same time, I don’t feel like he’s quite getting the whole picture here."

    h "So Ryota’s been helping me out!"
    h "We’ve been doing strength training, lessons and running through scenarios."
    h "Our biggest focus lately is thinking outside the box; how doing things you normally would do isn’t always a good thing."
    h "It’s been really helpful, you should try it."

    n "Okay…"

    h "Scenario: You’re trapped in a room on fire with your best friend; what do you do?"

    menu:
        "Put out the fire.":
            $ Vigor + 1

            h "Well yeah, obviously, but how?"
            h "This room doesn’t have a fire extinguisher."

            n "You never said that."

            h "Just look around you, where’s an extinguisher."

            n "Wait, you meant this room?"

            h "Duh, it’s a scenario."

            "I forgot how literal he can be."

            n "Then I’d engage the sprinkler system."
            n "There’s also an alarm near the teachers desk, which would call 911 for us."

            h "Boring!"

            n "Being a hero isn’t always the most exciting choice."
            n "It’s about making the best one."

            h "That’s easy to say when you have warning, but in the heat of the moment, anything could happen."

            n "Please stop with the puns, I beg you."
        "Shield my friend from the fire.":
            $ hRep + 1
            h "W-what?"

            n "I’m wearing mostly leather, so it should work long enough for the sprinklers to go off."

            h "B-but you really don’t have to do that. You could try to stop the fire or call for help."

            n "Well yeah, I might do those thing afterward, but that’s not what I’d do first."

            "What’s gotten into him?"

            n "You asked what I’d do, that’s what I’d do."

            h "I mean, yeah, that… that makes sense. Wait, no! You’re missing the point."

            n "Hunh?"
        "Refuse to answer.":
            $ hRep - 1

            n "I don’t have enough information to answer the question."

            h "What more do you need to know? The room’s on fire."

            n "How did the fire start? Why didn’t the alarms go off?"
            n "Is there smoke involved? What is the substance on fire?"
            n "Are there any explosives involved? How exactly are we trapped in the room?"

            h "Dull, dull, dull. Don’t you know anything about heroism? You’ve got to be a man of action!"

            n "All I’m asking for is a little verisimilitude."
            n "Things don’t happen at random, there has to be a reason."

            h "And in the time you complained about versachi we both died."

            n "You mean verisimilitude."

            h "Now the rest of the building’s on fire!"

            n "You don’t know what that word means, do you?"

            h "You gotta do something fast, we’re getting crispy."

            n "You just said we died!"
    $ Vigor + 1
    $ hTurn + 1

    h "You’re missing the point."
    h "The idea is to do something you usually wouldn't do. It’s the only way to change."

    n "Okay, what would you do then?"

    "I shouldn’t have asked that. If I had thought about it for even a second, I wouldn’t have."
    "He opened the window, I had enough time to acknowledge we were on the third floor before he picked me up and jumped out."
 
    #Cg

    n "aaaaAAAAHHHH!"

    h "It’s cool, if the pool doesn’t break your fall, I will."

    n "AAHHHHH!"

    "We hit the water and everything left my mind except the need for air."
    "When we finally breached the surface, I thrashed blindly around trying to hit him"
    
    scene backgroundpond

    n "WHAT THE FRESH HELL WAS THAT FOR!?"
    n "We could have died!"

    h "That’s why we jumped out the window!"

    n "I can’t believe you jumped out the window. Don’t you ever picked me up like that again!"

    h "How do you want me to pick you up?"

    n "That’s not what I meant and you know it! And you ruined my favorite jacket!"

    "I sloshed out of the pool with an embarrassing squelch."

    h "I can always get you a new jacket, I can’t get a new you."

    n "Just think things through next time."

    "I really can’t stay mad at him. He means well, but we can’t keep doing stupid stuff like this."
    "This was a very expensive jacket."

    return
label Hiro3:
    return
label Hiro4:
    return
label Hiro5:
    return
label HiroF:
    return