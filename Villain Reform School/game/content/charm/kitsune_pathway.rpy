label KitsuneVisit:

    if kTurn == 0:
        jump Kitsune1
    elif kTurn == 1:
        jump Kitsune2
    elif kTurn == 2:
        jump Kitsune3
    elif kTurn == 3:
        jump Kitsune4
    else:
        jump Kitsune5

label Kitsune1:
    scene backgroundstage
    with Fade(0.5, 1.0, 0.5)
    "I hear the trill of a bird throughout the halls. It's going up and down the octaves in rapid succession."
    "Following the sound has led me here. Standing center stage is Kitsune, going through scales as lovingly as a ballad."
    "I should have figured someone was singing."
    "Not wanting to interrupt, I go for the exit."
    show kitsune shocked
    k "Nagen! You surprised me!" 
    "She hops down to the ground floor."
    show kitsune cry talk2
    k "Don't tell me you're wanting the stage for something as well."
    k "I've already had to tell Chisei that she can have the space when she has something worth blocking and not a second sooner."
    n "Can't you practice somewhere else?"
    show kitsune mad
    k "I could in theory, were the school not full of music haters! Outside, inside, even my own room is off limits apparently."
    k "I managed to get one run through in before someone started banging on the wall for me to be quiet."
    k "I'm lucky to have a place like this, but I can only use it for a few hours after classes before the teachers want to lock up for the night."
    n "I didn't mean to cut in to your time. I thought I heard a bird."
    show kitsune smug
    k "A bird? Me? You're too kind." 
    "Am I?"
    k "Nagen, I know you're busy with other things, but I could use some help."
    show kitsune talk
    k "I think Kazz is patronizing me, and I'm not sure what to do."
    n "What do you mean?"
    show kitsune shocked
    k "Everytime I come up with an idea or a new song, he just says it's great and then gives no other feedback."
    k "Of course, I like my ideas, but after a while it sorta feels like I'm being ignored."
    n "Knowing Kazz, he probably just wants you to be friends with him."
    show kitsune mad
    k "That's worse. I don't want a friend right now, I want a coworker. Someone to bounce ideas off of."
    k "Without critique my creative drive is withering to mush. You've always been a brutally honest person."
    show kitsune sulk
    k "Would you be able to sit in on my run through and tell me what you think?"
    n "I don't know much about music, but sure."
    "Hopefully it doesn't take too long."
    scene backgroundblack
    with Fade(0.5, 1.0, 0.5)
    scene backgroundstage
    with Fade(0.5, 1.0, 0.5)
    "I stand corrected."
    k "So, what do you think?"
    "It's like looking into the eyes of a starving child. She clearly wants me to like it, but I don't."
    "I was held hostage by social convention long after I had enough."
    menu:
        "It's too long":
            $krep +=1
            k "By how much?"
            n "By fourteen songs."
            show kitsune teary
            k "But that's most of them!"
            n "Exactly. You should only have one or two to start."
            n "Making all this production for over an album's worth of songs, you'll never get anything finished."
            show kitsune sulk
            k "Okay, less songs, that's... reasonable, as much as I hate it."
            n "Welp, I think that's a decent jumping off point. Now if you'll excuse me-"
        "It's great":
            $krep -=1
            show kitsune mad
            k "Not you too." 
            n "Hey, I'm trying not to be mean here."
            k "Why? Do you think I can't take a little critique?"
            "It's not little, that's part of the problem."
            n "It's not the sort of thing I'd usually watch."
        "I have to go":
            show kitsune teary
            k "Wait!"
            "Anything's better than saying to her face that I hated the whole damn thing. She runs ahead and blocks the door."
            k "You promised!"
            n "I promised nothing. Don't make me be mean to you."
    show kitsune talk2
    k "Nagen, please, I'm not going to get any better if I don't hear what specific things I can change."
    n "Less costume changes."
    show kitsune mad
    k "Never!"
    n "But you just said-"
    show kitsune apathetic
    k "You just haven't seen it yet. Once it's in front of you, you'll get it."
    k "It takes up the stage and helps compensate for my shaky choreo. Never underestimate the power of misdirection."
    n "If you're distracting people, doesn't that mean they won't pay attention to your singing?"
    k "I guess it would be difficult to maintain the right breath support if I plan it wrong..."
    k "Fine, one less costume change, but I'm not killing the idea entirely. I just need more practice."
    "She looks at the ground, her feet unsteady in her heels."
    "That's another thing I was going to suggest, that she looks like she's about to topple over, but she might know that already."
    show kitsune talk2
    k "Thank you for listening to me sing. No one's wanted to since the riots calmed down, so I'm really out of practice."
    k "It was nice having an audience for once."
    "She reaches out, then hesitates. I'm not sure if she wanted to hug me or shake my hand. Instead, she fidgets with the end of her glove."
    show kitsune apathetic
    k "If those things are what come to mind, then my singing isn't as rusty as I thought it was. That's good to know." 
    n "Were you serious about not needing a friend? That seems kind of lonely."
    k "Well, I- I'm sort of busy."
    n "If you ever change your mind, feel free to hit me up."
    show kitsune teary
    k "Oh."
    "I know Uitto doesn't like her, but she might not spend all her time picking fights with her if she had someone to talk to."
    k "I'll definitely think about it."
    hide kitsune
    return
label Kitsune2:
    #[Must happen in chapter 1]
    scene backgroundstage
    "Kitsune is offstage for once, standing amongst the seats in deep contemplation."
    "She tilts her head left, then right, up, then behind her."
    "I do the same to see what she's looking at, but the place looks the same as last time."
    show kitsune talk
    k "Nagen, do you like movies?"
    n "Depends on the movie, but yeah."
    show kitsune smug
    k "Excellent."
    "She grins in a grinch-like fashion, chuckling darkly to herself. I'm a bit concerned."
    k "That's what everyone's been saying, which means I now have a way to get everyone in here."
    n "You lost me."
    show kitsune mad
    k "No one wants to gamble on a no-name act. That's why smaller artists open for bigger artists all the time."
    k "The fear of wasting time on something they don't like is gone."
    n "So you're going to trick people into watching you sing?"
    show kitsune smug
    k "Exactly. I mean, it worked with you."
    n "Hey!"
    show kitsune catty
    k "Besides, we'll be providing a much needed service."
    k "Other than the three clubs and the café, there's nothing to do other than read."
    k "Which, don't get me wrong, love reading, it's just not exactly a social activity."
    k "However, going to the theata' can be done with friends. Outfitting this place to play movies is the perfect way you can help me."

    menu:
        "Why would I help you?":
            $krep -= 1
            show kitsune apathetic
            k "Hmm, let me think. That's right, it's your fault all of us are stuck here."
            k "Supposedly you're trying to be a better person, but other than Rei, I don't seem to recall you doing anything to help anyone other than yourself."
            k "Forgive me for assuming that was what you came here to do."
            n "Would it kill you to at least ask first?"
            k "Will you help our fellow students and me by trying to make a screening setup?"
            k "Keeping in mind, if you don't, it will color how I vote in the future."
            menu:
                "No":
                #pathwaylock
                    show kitsune mad
                    k  "Then, as we say in show biz, that is all."
                    "She turns away from me to resume staring at her surroundings."
                    n  "I just came here to talk, not to build some elaborate thing."
                    "She ignores me."
                    return
                "Yes":
                    show kitsune catty
                    k  "As expected of our student council president."
        "Why me?":
            $krep +=1
            show kitsune talk
            k "Weren't you like, the tech guy?"
            k "You and Jona used to tear shit up and put it back together during lunch, but only the ones you messed with ever worked again."
            k "His just sort of looked neat."
            n "Well, yeah, but Mr. Yaguichi-"
            "She rolls her eyes."
            show kitsune mad
            k "Yaguchi wants people to leave him alone."
            k "If it's not school related, he won't give me the time of day."
            show kitsune catty
            k "Besides, even if we fail, it'll make both of us look good for trying."
            n "I guess that's true."
            k "Excellent." 
        "Sounds complicated":
            show kitsune talk2
            k "Yeah, that's what's been stumping me too."
            k "I know a projector can work on a plain old bed sheet, but that doesn't help us with sound or y'know, projecting."
            show kitsune talk
            k "I'm sure there's old stuff around here that can be fixed up."
            k "That's where you come in. Tech is the unsung hero of the entertainment world after all."
            n "I mean, it's worth a shot."
            show kitsune smug
            k "Exactly."
            k "When the students find out you're trying to get a theater running out of the goodness of your heart, it's sure to win you some brownie points and me some fans."
    n "Are you sure this is going to work?"
    show kitsune talk2
    k "Oh yes, I've done a thorough survey of half the students. This movie thing will be a sure-fire hit."
    n "Yeah, people will be jazzed about getting to watch something resembling TV, but if you want people to watch you, why not throw a concert?"
    k "I hate singing alone, even during rehearsals. It's just so draining performing for empty seats."
    "She looks down at the ground."
    show kitsune cry talk2
    k "I never got to have my big break, so that's all I can picture. If my first live performance doesn't have an audience... it would be soul crushing."
    "She slaps her cheeks to snap herself out of it, flashing a picture perfect smile my way."
    show kitsune
    k "So, even if they don't actually come to see me, it would be a dream come true to sing in front of a live audience for the first time."
    k "As a solo artist, of course. I did earn my stripes in choir already."
    "So she's not used to being in the spotlight by herself. I sort of get the feeling."
    n "I kinda got used to other people taking credit for things I did. The first time people really paid attention to me, it came with a warrant. Not my grandest moment, but I've been digging myself out. Sorta. My point is, I don't think your first performance is going to be a sign for how well you'll do."
    show kitsune sulk
    k "You think they're going to hate it."
    n "No, I just think you're putting a lot of pressure on yourself. This is supposed to be a fun thing, right?"
    k "You're right. First things first, we need to see if this dusty old library even has movies to play."
    show kitsune talk2
    k "It's a huge place. I'll search the first floor and you take the second. Between the two of us, we should find something."
    k "I'll even take books on tape if it comes down to it."
    "With a plan in place, we part ways. I'll have something to show her next time I talk to her."
    hide kitsune
    return
label Kitsune3:
    scene backgroundstage
    "We combine our hordes together like dragons. The DVDs are our safest bet. Momoko has a game system and Kazz has a laptop."
    "At least one of them has to be able to hook up to a projector."
    show kitsune
    k "I grabbed anything that looked movie-like."
    "She tosses aside an internet safety video."
    show kitsune talk
    k "Guess I shouldn't be too surprised there's a lot of reference stuff here."
    n "I found a couple of things."
    "There's a few random episodes of TV shows. They must have been pulled out of box sets to make it easier to lend out."
    "There's a handful of movies by indie studios that were probably cheap and the piece de la resistance: a musical."
    n "Check it. It's not everyone's cup of tea, but it'll attract anyone that likes singing."
    "Her eyes light up until she sees the title."
    show kitsune cry talk2
    k "I don't know."
    n "What, is it inappropriate or something?"
    "That would be more of a draw."
    k "No, it's just a little too close to home for me. If we watch that, I will ugly cry."
    n "Isn't it about shoes?"
    "I didn't bother reading the back."
    show kitsune cry talk
    k "Well, yeah, but it's more the dad character in it."
    k "My dad used to just throw away things he didn't want me to have: books, shoes, clothes."
    k "I don't really want to watch a movie where a guy like that just gets away with it.."
    menu:
        "That's fucked up":
            $krep +=1
            n "Does he still do that?"
            show kitsune mad
            k "No, he doesn't do anything now."
            "Oh."
            show kitsune sad talk2
            k "It's fine. I mean it's not fine, but I don't miss him, that's for sure."
            k "He wouldn't have let me come here if he was alive."
            "She smiles a bitter smile."
            show kitsune talk2
            k "It would have been the same for you too, right?"
            n "Probably, if he couldn't figure a way to be on the staff."
            n "I don't know. The more I think about it, the more it seems exactly like a place he would run, minus the drug testing."
            "Remote, isolated, a small group of people he could charm into having power over. Seems like his kind of jam."
            k "So this is like, normal for you too. I, uh, kinda got used to being by myself, so a place this big and empty isn't that scary."       
        "The dad's the villain though":
            $krep -=1
            n "How does he get away with what he does?"
            show kitsune sulk
            k "I mean, no one stops him when he's acting like a shithead."
            k "He doesn't get punished in the end, he just sort of keeps on living off stage unchanged."
            k "Fairly realistic, but I'm not interested in realism right now."
            n "I can tell."
            "She glares at me."
        "Why?":
            show kitsune apathetic
            k "I don't know. He had this very clear idea of who I was supposed to be and didn't like the fact that I wasn't anything like that."
            k "When he found out I was a Vigor Major, he was so excited I could have a 'real' career instead of singing." 
            n "What did he think you were going to do?"
            k "Be a Karmic Gladiator, I guess. I can shatter glass with my voice, so he'd take me into this sound proof room and have me practice over and over again."
            k "He also wanted me to reach lower registers. A bass note deep enough can change how fast a heart beats, but it's nothing more than parlor tricks."
            k "People would get bored of it."
            n "Sounds pretty cool to me, but I get why you'd want to do something more with it." 
            "The more things you can do with your Proficiency, the better off you are."
    show kitsune cry talk2
    k "I wouldn't have been able to come here if he was still alive. I know I shouldn't be happy about it, but I guess a better word is relieved?"
    k "Like, I spent my whole life having to look over my shoulder and now I just... don't."
    n "How do you do it?"
    k "Do what?" 
    n "Stop being anxious about it?" 
    "My dad's been gone for over a year, but I still flinch anytime a door closes behind me."
    show kitsune talk
    k "Well, I had this list of everything I was going to do once I was on my own." 
    "She clicks her heels together."
    show kitsune
    k "Doing all of it is sort of like armor. All I gotta do is look at my nails and it reminds me he can't tell me what to do anymore."
    n "And that works?"
    k "Totally." 
    "She gasps."
    show kitsune smug
    k "I could totally do it for you too. I think you could pull off black, real OG rock star vibes." 
    n "What about the movies?"
    k "We can have everyone vote on which of the good ones to start with. If I get out-voted on the musical thing, then so be it."
    k "Gosh, do I even have black polish? Momoko might. Even if she doesn't, someone has to have a sharpie."
    "We pack up our things as she starts talking about other stuff I could do, like gathering a bunch of safety pins or paint to decorate with."
    "I've never seen her so excited to talk about someone else before. It's nice."
    hide kitsune
    return
label Kitsune4:
    scene backgroundstage
    "We have all the equipment we think we'll need to rig up the screening."
    "Kitsune's running around in flats so she can help out, but she refuses to lift anything heavier than fifteen pounds."
    "I thought working out was how people stay 'dainty', but she staunchly disagrees with me."
    show kitsune smug
    k "It's all about balance. If you do one thing too much, it throws your whole vibe out of whack."
    k "A proper idol knows to be mindful of how they appear, down to what kind of water they drink."
    n "About that, why are you trying so hard now? I don't remember seeing you trying to debut anywhere, no offense."
    n "I figure someone like you would jump at the chance to be in a Rosette pageant at least."
    show kitsune cry talk2
    k "I, uh, didn't make the cut for those. They've got really old, really strict rules, so if you don't know someone on the inside, it's easy to bump into them."
    k "Thank you though. It's good to know someone thinks I'm memorable."
    "I remember everything regardless, but it seems to make her feel a little better."
    "Uitto or I would remember someone like her trying to make it before the riots for sure. It's like she appeared out of nowhere."
    show kitsune mad
    k "I did try to get an agent."
    k "My mom was super supportive. She said I had that 'it' factor, but it turned out to be a scam."
    k "They were just taking her money, they weren't actually trying to find jobs for me at all."
    n "So you've always had to do this kind of thing yourself?"
    show kitsune
    k "Yep." 
    "We each tie a bed sheet to either side of a bar. With a few pulls, it's hanging as straight as it can."
    show kitsune smug
    k "My own music, my own costumes, everything. That's why I'm so glad to be here. This is the first time I've had people who are willing to actually help me."
    k "It's amazing. You, Shoma, and Kazz have brought me so much closer to my dream than I ever could by myself."
    k "Believe it or not, I'm actually not that great at a lot of things."
    n "I believe it."
    show kitsune apathetic
    k "Rude."
    show kitsune
    "She laughs anyway."
    menu:
        "What are you the worst at?":
            $krep +=1
            show kitsune talk
            k "Ooo, that's a hard one. Dancing I guess, since I lack any choreography to learn? Or maybe hair styling?"
            k "I figured out how to do a pigtail and then got too scared to keep going."
            n "Okay, but you're good at those."
            show kitsune shocked
            k "Really? Well, that's reassuring. Compared to other people in the industry I am decidedly bad. I'd get read for my lashes alone."
            "Uitto did say people were cut throat in show biz."
            show kitsune talk
            k "What about you?"
            n "Writing. It's really easy for me to accidentally repeat stuff I've already heard. I couldn't do the sort of stuff Chisei does."
            show kitsune mad
            k "Not with that attitude. If it's something you want to do, you should do it anyway. Eventually you'll stop being bad at it."
            show kitsune smug
            k "I guess my style is living proof."
        "About that scam...":
            $krep -=1
            show kitsune mad
            k "Ugh, it was awful. Like two hundred for a head shot awful."
            k "I kept wondering why I wasn't getting any auditions. She spent so much money believing in me when no one else would."
            k "My parents fought about it a lot." 
            k "Estella was the closest I ever got to getting recognized, until now."
            n "Estella was awful."
            show kitsune apathetic
            k "Yeah, but at least no one was paid to say I was worth something."
            k "I have concrete proof I am the most capable singer of our generation. It's also the reason I got to come here."
            k "We were clearly the only kids who had notable Proficiencies."
            "That's not why I'm here. I was forced to come here. My Proficiency certainly isn't that noteworthy."
            "Who cares about test scores when they're rebuilding hospitals?"
            n "You're getting scammed all over again. This isn't some ritzy private school. If it were, they'd actually have money." 
            show kitsune cry talk2
            k "They can say whatever they want, as long as I reap the benefits before everyone else finds out."
            "She's so determined to go somewhere, even when we're all stuck."
        "When did you get started?":
            show kitsune talk2
            k "What, like singing? Since I was first able to. I was always front row in the church choir."
            "That just means you were shorter than everyone else."
            k "As for when I started training to be an idol... I guess nine? Ten?"
            show kitsune
            k "We were at a restaurant and they had music videos playing on the wall."
            k "I remember hearing them sing and realized I sounded just like the girls on TV."
            k "I'd sing to myself all the time to get the tone just right."
            show kitsune apathetic
            k "I used to post videos of me singing to the internet hoping to get discovered." 
            "She frowns."
            show kitsune mad
            k "But then people told me I sounded like every other kid singing and that really got me going. I had to prove them wrong."
            k "I'm not like any kid, I'm like any idol."
            n "So you got started out of spite?"
            show kitsune talk2
            k "No, and you're not becoming stuco president out of spite, are you? Never forget, Nagen; I got your number."
    "I sort through the collection of unidentified wires. Somewhere in the black spaghetti are the right power cords and adapters."
    "The projector we found won't work with Kazz's computer, but the Gamestation might if I jerry rig it right."
    show kitsune
    k "Thanks for helping me."
    n "Don't thank me yet. I haven't gotten anything to work yet."
    k "I know, it doesn't matter. I appreciate you helping in the first place. You could have bailed on me, but you didn't."
    n "Yeah, well, I said I'd help, didn't I?"
    show kitsune sulk
    k "Yeah... I, uh, I also appreciated you offering to let me sit with you guys on the first day."
    k "I know we all used to go to the same school and whatnot, but it's been a while, things changed."
    k "I thought no one would want to talk to me." 
    "Uitto was right, she's super insecure. If she just said that instead of picking fights with Uitto, things would have gone so much easier."
    show kitsune cry
    k "You're sort of the only person who talks to me outside of working on stuff. It means a lot."
    n "I uh, I mean, you know..." 
    "Words, why do you fail me when I need them the most? Someone is actually complimenting me and I barely did squat." 
    n "Th-thanks."
    hide kitsune
    #CG
    "A bright blue light covers the sheet."
    k "It's working? OMG! Nagen, it's working! You did it! We can watch movies here now!"
    "She hugs me and I nearly explode inside. The moment is fleeting and she abandons me to twirl in the light, white hair dyed in blue."
    "It can't find the Gamestation; what she's celebrating over is an error message. Somehow, she makes it beautiful."
    return
label Kitsune5:
    scene backgroundstage
    "Kitsune's plan worked. Word has gone around that on Fridays, we can use the stage to play one movie."
    "Votes were cast for what would play each week for the month. Kitsune walks out on stage."
    "It looks like she took my suggestion to ditch the costumes after all."
    show kitsune
    k "Alright everybody, movie starts in fifteen minutes. We'll knock out the lights in ten."
    "A chorus of 'oooos' go around the theater. Not that there's much to worry about."
    "I'm still a little nervous that something's going to break down on us. Kitsune hops off the stage and sits down next to me."
    n "Wait a minute-"
    show kitsune teary
    k "Don't tell me this seat's taken already."
    n "I thought you were going to perform."
    show kitsune apathetic
    k "I mean, I was, but I wanted to watch the movie too."
    k "When I thought about spending hours in a flashy costume just to sit in the dark, I knew I was setting myself up to be uncomfortable."
    show kitsune
    k "Besides, you're the only one who came to see me. I want to give you a proper show, not just a teaser. That'll take more time." 
    n "So you'd rather hang out with me instead?"
    k "Yeah. Is that so weird?"
    menu:
        "Confess":
            show kitsune shocked
            n "It's not weird, unless you wouldn't do this for your other friends. Then it would be, y'know, important."
            n "Which is fine, by the way, if this is supposed to be a thing."
            k "I mean, it is a thing. We've been working on this for days now."
            n "No, I mean like us watching together instead of you doing your thing."
            n "The whole reason you wanted me to help was to perform. At least, I thought that was the case."
            n "Like I said, it's fine if it's not."
            show kitsune apathetic
            k "Nagen, what are you talking about?"
            n "Like a date. Is this a date? It doesn't have to be. I just- yeah, I'll stop talking now." 
            "I probably made an idiot of myself. She seems scared."
            k "Why would going on a date with me make you nervous?"
            n "Cause I like you." 
            if krep >= 3:
                show kitsune shocked
                k "Really?" 
                "She shakes her head."
                show kitsune mad 
                k "Then no, definitely not a date, I didn't even get ready. These are my comfy clothes and-"
                "Bracing myself, I go to hold her hand. She stops talking. A dark blush fights against her foundation."
                show kitsune 
                "I'm too nervous to do anything else, and she seems to be the same, inching slightly closer but never looking away from the screen."
                "I gave myself a cramp not wanting to move, but it was totally worth it."
                hide kitsune
                return
            else:
                show kitsune cry
                k "I'm sorry, Nagen, but I like someone else. I sort of have a crush on Hiro."
                n "Oh. Hiro, really?" 
                "Am I forever cursed for every girl I like to like him more?" 
                k "Does this mean we can't be friends?"
                n "What? No, I just made a dingus of myself, nothing new. Better to find out now."
                k "Yeah..."
                hide kitsune
                return
        "You're a good friend":
            $ krep += 1
            show kitsune shocked
            k "Who, me?" 
            n "I would have been fine spending fifteen minutes by myself, or however long it took you to change out of your costume."
            n "I'm glad you're taking it easy for a change."
            show kitsune
            k "Aww, well I had to admire your handiwork for myself. I wouldn't have been able to do this without you."
            "She fidgets with the end of her skirt."
            k "You really mean it? We're friends?"
            n "Yeah."
            "Uitto may have some objections, but we don't all have to hang out at the same time."
            show kitsune smug
            k "Then, can I tell you a secret? Promise not to laugh!"
            n "Okay..."
            "She leans in and whispers."
            k "I kind of have a crush on Hiro."
            "Oh, oh no, I don't know how to tell her this, but she's not his type. I definitely won't laugh."
            "Nothing funny about never getting noticed by your crush, I would know."
            show kitsune
            k "Super embarrassing, I know, but-"
            "She pulls down the edge of her collar and shows me a chemical burn scar."
            k "He saved my life. My helmet broke and the stuff we were getting fed started going into my neck. He was the only one that noticed."
            hide kitsune
            scene flashback_ch1_2
            "Was that what he was doing?"
            scene backgroundstage
            show kitsune talk
            k "I haven't had anyone to talk to about it, so I've been sort of sitting with it. I don't know what to do about it though."
            k "Do you think he'd like to go to something like this?"
            n "One hundred percent, but as friends. He's uh, mostly worried about having friends right now."
            show kitsune 
            k "Same. It's a good thing we have each other."
            hide kitsune
            "The movie starts playing and everyone quiets down. It's one I've already seen, but I'm mostly here to be a part of something."
            "Even if it's smaller than I first thought."    
        "Yes": 
            show kitsune mad
            n "You've been scheming for the spotlight for so long. I didn't expect you to give it up."
            k "Who said anything about giving up? I'm allowed to take breaks, Nagen. And here I thought you liked my company..."
            "She shakes her head."
            k "I should have known what this was. Now that the collaboration is over, it's back to being strangers. I get it."
            n "I didn't say that."
            show kitsune apathetic
            k "I said I get it. See you in class."
            "She gets up and looks for a different place to sit. Kazz flinches away from her and Shoma's pretending to not know her."
            "I guess this is the sort of friendship she's used to. Well, it's not like I told her to go away."
            "She decided to leave on her own. At least the movie is good."
            return
