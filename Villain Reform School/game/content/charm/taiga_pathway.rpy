label TaigaVisit:

    if tTurn == 0:
        jump Taiga1
    elif tTurn == 1:
        jump Taiga2
    elif tTurn == 2:
        jump Taiga3
    elif tTurn == 3:
        jump Taiga4
    elif tTurn == 4:
        jump Taiga5
    else:
        jump TaigaF

label Taiga1:
    scene backgroundroof
    "The city looks so small yet so close from this high up."
    "Now that everyone's here, I don't even hear cars anymore, just the hush of trees pulled about by the wind."
    "At night, it's easier to pretend it's because everyone's asleep and not because we're miles from anyone else."
    show taiga gasp
    t "Hello? Yes, I'm looking for the Sakurai Company. Do you know anyone that works there?" 
    "Taiga's curled up on the roof. He nods."
    show taiga grimace
    t "Thank you." 
    "Then he looks at his burner phone and punches in a number."
    show taiga gasp
    t "Hello? Yes, I'm looking for the Sakurai Company. Do you know anyone-"
    "They hung up on him. Houdini, his bunny, tugs impatiently at his sleeve."
    show taiga sad talk1
    t "I know, I know. Just three more numbers and we can get you food." 
    n "He, uh, might be warning you about me."
    "I guess his bunny hates even looking at gloves. I put them in my pocket, and instantly all is forgiven."
    n "What are you doing up here?"
    show taiga grumpy
    t "Gets the best cell reception."
    "He frowns at his phone."
    show taiga gasp
    t "You wouldn't happen to remember the number for the Sakurai Company, would you?"
    t "There were a bunch of commercials for it a few years ago."
    "I never paid attention to the ads for the circus."
    "I don't imagine they'd come this far out either, but I'm guessing it's more important than that."
    "I sit down next to him and lay back on the concrete."
    n "I might have seen it, but it would take combing back through a lot of stuff to find it."
    show taiga smile talk
    t "REALLY? That's so cool. I didn't even think- Dude, if you can dig up that number, you'd be a lifesaver!"
    n "Really? I mean, I appreciate the compliment, but how-"
    show taiga sad talk2
    t "My whole family works there, my real one, not whatever lady they're trying to track down that's supposedly my 'real' mom."
    t "I have no way of contacting them, and with the riots they might- I want them to know I'm not dead."
    hide taiga
    menu:
        "Aren't you curious about your 'real' mom?":
            $ tRep -= 1
            play sound "752275__ienba__magic-reveal.ogg"
            show taiga mad talk
            t "I know all I need to. I've been at the same place she left me for eleven years."
            t "Not once did she try coming to get me or even see me."
            "He curses and looks away. Guess the other benefit of the roof is no one sees you cry."
            show taiga grumpy
            t "I know exactly where she is. She's in another country. I'm already far from home as it is."
            n "If you know where she is, then why-"
            show taiga annoyed
            t "I lied. Told the stupid government workers I didn't know a thing about her. This is about as far as playing dumb got me."
        "They know you're alive":
            show taiga sad talk2
            n "A huge memorial's been planned for all the kids that didn't make it. Since you're here, your name won't be on it."
            t "You seriously think someone would read that whole thing?"
            "I think of the many nights I combed through obituaries and missing persons lists looking for Odori's name."
            n "Yeah, I do. I'm sure they're looking for you all over, but if you're here that means you aren't listed dead or 'missing'."
            "A lot of hope can be held in not seeing someone's name."
            show taiga sad talk1
            t "It's not the same as them hearing I'm okay."
            "He sighs. It's not the perfect solution, but it's the only thing we can hold onto."
        "I'm in the same boat":
            $tRep += 1
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            show taiga
            n "I can contact my foster, but technically, she can't legally take care of me yet."
            n "She's basically using this place to bide time."
            t "Aren't you from a rich family though?" 
            n "Maybe, but I don't know them. Maimai's the one that took care of me during the riots-"
            "I remember seeing papers on her desk."
            n "Wait a minute. These people, they took care of you for more than six months, right?"
            show taiga grimace
            t "Yeah, eleven years is longer than six months." 
            n "They could be considered next of kin!"
            "It was a bunch of legalese, but I remember Maimai kept highlighting it as one of the main reasons she had more of a say than my grandparents about who I stayed with."
            n "It's usually for nannies, but if they can prove you were left in their care, they'd get put above strangers for adoption purposes."
            n "If they were in the middle of a bunch of legal stuff, that could be why you're not allowed to talk to them."
            "It really just depends on what his 'real' mom's reaction will be to finding out about him."
            show taiga mad talk
            t "I hope so, but you didn't see how they treated everyone."
            show taiga sad talk1
            t "When I asked to go back to them, the case worker tried to say they 'lied' about being my family and I was just some stupid kid for believing them."
            t "It was like arguing with a robot." 
    show taiga sad talk1
    n "Wait a minute, were you trying to guess the number earlier?"
    t "What else am I supposed to do? They took away my phone."
    "Guess he never memorized anyone's number."
    n "I can't make any promises."
    n "The only time I was able to watch TV was when I was hospitalized, and sometimes I saw billboard ads, but they never stuck out to me."
    n "Kinda like when you skim through a magazine; I might have seen it without seeing it. I'll try though."
    show taiga smile talk
    t "I think... I think this is the closest I've gotten to finding them."
    "Okay, no pressure then."
    t "Seriously, even the fact you're willing to help..."
    n "It's what I do. At least, what I try to do."
    show taiga
    t "Do you have to concentrate while you flip through your head?"
    n "Sort of?"
    "Can't say I'm the greatest multitasker, but I've also never tried to do something like this outside of exams."
    show taiga grimace
    t "Why don't we get something to eat? If I'm keeping you up late, the least I can do is help you help me." (21)
    "It doesn't really work that way, but I can only imagine how useless I'd feel watching someone try to help me."
    n "Sure, why not?"
    "Turns out I can't flip through visual memories and walk at the same time, and I'm a piss poor conversationalist to boot."
    "Still, it was nice to be able to do something for someone. I hope he'll be able to sleep better tonight."
    hide taiga
label Taiga2:
    scene backgroundamp
    #[BG: Ampetheater Night]
    "I came outside to clear my head."
    "Taiga's quest to remember an obscure telephone number is easy on paper, but when locked in my room, I get distracted by everything else that's been going on."
    "At least outside is cool, and I can feel like I'm doing more than sitting in my room for hours."
    show taiga smile talk
    t "Hey!"
    "Anytime I see him, I feel guilty. I don't have an answer yet. At least he's not glued to his phone trailing random numbers."
    t "Taking a break?"
    n "Yeah. The portables get stuffy after a while. What were you doing?"
    show taiga scheme
    t "Practicing."
    "He flips onto his hands and walks towards a basketball."
    "It's a little low on air, but that doesn't stop Taiga from balancing on it. I didn't even know we had a basketball."
    n "Wait, you performed in the circus with your family?"
    show taiga annoyed
    t "No, I feasted on grapes lying on a bed of gold."
    "He flips over onto his feet, propping the ball on his hip."
    show taiga gasp 
    t "Of course I performed! The longer I'm here, the more I stiffen up."
    show taiga suspicious
    t "I can't believe they expect everyone to sit around for hours and not turn into shrimp people."
    "I did not know a leg could bend in that direction."
    show taiga grumpy
    t "I was this close to graduating from tumbling too."
    t "Hard to stand out when you're performing with four other pip-squeaks, but I got nothing to practice my new act here."
    "I wonder what his act was supposed to be..."
    hide taiga
    menu:
        "Trappez":
            show taiga grimace
            t "That only works with a strong duo and well... Let's just say there aren't too many kids my age around the camp."
            t "They're either adults or really little. Besides, I wanted my own act for once, not to share the stage."
            n "I guess, but you could always find someone else to practice with. You don't have to only perform with your family."
            show taiga gasp
            t "With who?"
            t "I don't know if you noticed, Nagen, but even the Vigor Majors here are locked in on the whole school thing instead of what they can do after graduation."
            show taiga scheme
            t "Unless you're volunteering."
            "Would it be fun to swing around in the air? Maybe."
            "The only problem is I'm not a fan of falling. Doubly so since there's nothing to catch us around here, let alone swing on."
            show taiga gasp
            t "You're seriously thinking about it?"
            "He ropes an arm around my shoulder."
            t "Well, trapeze and ropes are out of the question, but maybe we can figure out something else you could do."
        "Animal training":
            $ tRep -= 1
            play sound "752275__ienba__magic-reveal.ogg"
            show taiga annoyed
            t "Yeah, my folks thought that'd be a good idea too."
            "I mean, he's the animal guy. If anyone would be the best at it, it'd be him."
            t "The only problem is that most of the classic tricks, the things that really 'wow' people, are painful to the animals."
            "He demonstrates balancing on the ball again."
            show taiga mad talk
            t "Their bones weren't made to do those sorts of things."
            t "Neither were ours, but we can at least tell people when enough's enough for the day. The animals can't."
            "He hops off and glares back at the school."
            t "I think I get why the bigger animals hate being a part of the circus."
            show taiga grumpy
            t "You can't convince someone they aren't trapped when they clearly are."
            n "What about the bunnies?"
            show taiga smile talk
            t "Oh, we have a few pallor tricks up our sleeves, but the run time isn't long enough for a whole act."
            t "Hou's great at fetching things, Angel likes popping out of hiding spots, and Blaine... Blaine just likes the treats."
        "Aerial hoops":
            $tRep += 1
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            show taiga smile talk
            t "It's so cool!"
            t "You basically get to fly without worrying who's going to catch you, and you don't have to worry about people going 'I can do that'."
            t "Well, not as much as other stuff anyway. I'd been working on my act for almost two years and now– poof!"
            "He shakes his head."
            show taiga grimace
            t "The best I can hope for is to keep up the strength and flexibility training and hope my skills don't atrophy."
            "His arms hang at his sides, defeated for the time being."
            show taiga grin
            t "What made you think I'm an aerialist though? Those guys are jacked."
            n "I don't know!" 
            "I look away. I don't know where under all the robes and junk I'd see anything, but I don't want him assuming I had been looking at all."
            n "A lot of people would guess that. It's a circus thing. Be happy I didn't guess clown!"
            show taiga grimace
            t "I am a clown." 
            "He cartwheels my way. I flinch just as he lands an inch away from my face."
            show taiga grin
            t "If you think that's something to be ashamed of, you just haven't met the right clown."
            "He winks and backs off before I can push him or think of a witty retort. Not sure which I wanted to do. He just laughs at me."
    show taiga gasp
    "I look up at the trees with their wide branches."
    n "You know, Shoma has a bunch of fabric. Couldn't you use that to make an act with?"
    t "What, like aerial silks? I don't know if anyone would have something long enough to do that with."
    t "If he made something by stitching a bunch of stuff together, it could rip at the seams."
    show taiga suspcious
    t "Not exactly the thing you want to have happen while in the air." 
    n "Bummer."
    "It never hurts to ask. If nothing else, it could get added to the pile of stuff to order."
    show taiga annoyed
    t "Ain't that the headline of the month. I don't suppose you've had any luck digging up that number, have you?"
    n "Sorry, there's a lot of garbage to sift through."
    n "I was hoping to find it somewhere in my memories of the city during the riots, like on a billboard or something, but I got nothing."
    show taiga
    t "Well, yeah. I figured if it was anywhere, it'd be in a memory from when things were normal." 
    "Well when he puts it like that, what I was doing sounds stupid."
    show taiga suspicous
    t "You'd rather remember the riots then what happened before them?"
    "I know the answer, but I also know how insane it'd sound to someone from outside of Guwon."
    "It doesn't help that he looks worried by the prospect."
    "Because yeah, with everyone else romanticizing the past I would look like a freak for wanting to avoid it, but there's so much in there that I don't-"
    show taiga gasp
    t "Are you okay?"
    "No. I don't think I am, but I can't tell him that. I panic. I run. I hope the next time I see him he won't bring it up again."
    hide taiga
label Taiga3:
    scene backgroundcafe
    #[BG: Cafe Night]
    show taiga 
    "Taiga insists food tastes better under a full moon and outdoors."
    "I can't say I agree. I worry my stuff will go flying every time the wind blows, but Taiga closes his eyes and lets the world bobble him around instead of fighting against it."
    "For him, this is lunchtime."
    t "I've just never seen another human being want to function at six am."
    t "If everyone hates it, the teachers could just move class time instead of suffering with us."
    show taiga grimace
    n "I think the point is to prove we can tolerate suffering."
    t "Gross." 
    "Spoken like someone who refuses to stay awake for first period."
    show taiga grin
    t "Then why do you play along with it? Do you enjoy suffering?"
    n "No."
    "More like I'm used to it at this point. Houdini nibbles at a plate of greens."
    "The little guy has no idea what's going on other than the food in front of him. I'm kinda jealous."
    show taiga
    t "Then do you miss it? The weird hierarchy Guwon kept selling, you were primed to be at the top of it."
    hide taiga
    menu:
        "I miss my home":
            show taiga
            n "Don't get me wrong, I hate being under constant surveillance, but at least the walls were more sound proof back then."
            t "We're not under constant surveillance."
            "Taiga puts a fork in the center of the table."
            show taiga grimace
            t "There's only four of them. At any point, that fancy control room of theirs is either empty or barely being watched."
            "He turns the fork to an empty chair."
            show taiga annoyed
            t "They just want it to feel like we're being watched so we'll stay in line, but look how well that turned out."
            t "They can't even keep kids from breaking curfew."
            n "Are we breaking curfew?"
            show taiga grin
            t "Does it matter?"
            "I don't know what all will count toward finalizing my sentence. I got careless."
        "I miss knowing what to do":	
            $tRep += 1
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            show taiga grimace
            n "It sounds stupid to you I'm sure, but back then I knew what I was doing because the school required it and what I was doing for myself."
            n "Now it's more complicated."
            t "I wouldn't say that sounds stupid... I just don't really get it."
            show taiga
            t "My folks wanted to help me find an act that I'd be good at and wouldn't be hell on my body later down the road, but they never forced me to do something for no reason like this place does."
            n "There's a reason. I don't like it, but there's a reason for it."
            show taiga suspicous
            t "You know something."
            "I wish I could tell someone about the deal."
            "Unfortunately, if a word of it gets back to any of my friends, that could ruin it for all of us."
            "I don't even know if I can fully trust Taiga."
            n "I just wish other people weren't dragged into it."
            show taiga annoyed
            t "You should have thought of that before forming an army."
            "He laughs."
            show taiga grin
            t "Kidding, sort of."
            show taiga gasp
            t "Unless... Is that part of it?"
            show taiga
            t "You don't know if you learned your lesson for you, or because that's what you're supposed to do."
            "How the hell does he do that?"
            show taiga grimace
            t "I guess, if that's the case, what matters is if you're happy with the choice you made."
            t "Who cares who asked you to make it?"
            "I wish I knew the answer to that."
        "I miss Lethe":
            $tRep -= 1
            play sound "752275__ienba__magic-reveal.ogg"
            show taiga grimace
            n "I hate how everyone's used her death to pretend like she was someone she wasn't."
            n "I know there's a lot of things she did that were questionable, but she did it to save all of us."
            n "The riots were inevitable."
            "She could see into the future, which means if there was a way to prevent people dying, she would have guided us in that direction."
            "Instead, the goal had been to find as many kids as possible and save them."
            "At least, that's what the helmets were supposed to do."
            show taiga sad talk1
            t "What kind of person was she?"
            n "Kind, like to a fault."
            n "She felt guilty if she made someone even a little bit uncomfortable."
            n "When we told her we wanted to be heroes, she didn't laugh, she actually listened and told us what we'd need to do to get there."
            n "I thought I was going to have to wait years to do anything good, but she said..."
            n "I mean she could see into the future, so when she said what I was doing mattered, I knew she meant it."
            show taiga sad talk2
            t "That's the lady that wanted to tear everything down?"
            n "Yeah, but because of what you said. People were suffering."
            "Only now we're falling back to what's familiar."
    show taiga annoyed
    t "I've had a bunch of people who don't know my family try to tell me we did things 'wrong'."
    t "All I can find is that the way we live just doesn't fit in Guwon's weird proficiency-based boxes."
    t "I thought I'd be surrounded by the same garbage here, but it doesn't look like they took the fight out of anyone." (16)
    n "Definitely not. More of a restructuring period."
    n "Odori and Hiro were more of the solve-every-problem-with-hammers type. I'm far more strategic."
    t "Riiight. So what's the strategy now?"
    n "Become student council president..."
    show taiga grimace
    t "....."
    n "That's all I got so far."
    "I can't blame him for laughing because I sure as hell want to."
    show taiga grumpy
    t "Why anyone here's scared of you, I'll never know. You fit into whatever jello mold people put in front of you."
    n "No I don't!"
    t "Then why are you helping me find that number?"
    n "Because I don't want you to be sad!"
    show taiga gasp
    #[Taiga blush sprite]
    n "I don't want anyone to be sad, but this is one of the few things I can actually do something about."
    n "I just wish I was able to do it faster."
    show taiga
    t "Really, that's it? There's not something you want from me?"
    n "L-like what?"
    t "I don't know. Something?"
    hide taiga
    menu:
        "Your vote":
            show taiga suspcious
            t "You're that certain you can find it that you'd gamble away a vote on it?" 
            n "Not necessarily gamble."
            n "More like mutual reciprocity, show that I'm willing to help and listen? Be a friend?"
        "A date":
            $tRep += 2
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            show taiga grin
            n "Flowers are so cliche, right?"
            t "Really?" 
            n "I-I thought you were going to laugh. It was a joke."
            "He's not buying it." 
    show taiga grimace
    t "I see, I see. Then how do I know you're not lying?"
    n "Hunh?"
    show taig
    t "How do I know you're actually trying to help and not saying you will because it's convenient for you?"
    t "After all, it's not like I can see for myself if you're actually digging through your memories instead of saying you are." (25)
    n "I mean, that'd be kind of boring to watch."
    "More importantly, I'd be so distracted, it'd be open season for anyone that would want to hurt me."
    "Not that he necessarily would, but it's not like I had much warning about Mariko."
    show taiga mad talk
    t "Try me."
    n "I- I'll think about it."
    hide taiga
label Taiga4:
    scene backgroundlake
    "Taiga had issues sleeping back when we were at the school and everything was fine."
    "Now he's got a whole new batch of bunnies to worry about on top of the ones he brought with him."
    show taiga sad talk1
    n "You doing okay?"
    "He makes a noise that's far from encouraging. Not everyone gets what he's so worried about, but it sounds like the babies are at a fragile stage. Out here, there's not much he can do other than wonder."
    n "Did you eat at least?"
    t "Yeah."
    n "Cool, cool."
    "Why am I so bad at this?"
    n "In that case, why don't we do something to take our minds off things?"
    show taiga suspcious
    t "Like what?"
    "Owls call out into the night."
    "It's lights out for the camp."
    "If we're caught starting a new fire, we'll be in trouble."
    "That really only leaves-"
    n "We could go for a swim?"
    "The water's probably cold as hell. I'll stand by it if he goes along with it."
    show taiga sad talk2
    t "Fine."
    hide taiga
    #[CG: Taiga's scar]
    n "Woah. What the hell did that?"
    "Along his back are thick, raised scars."
    "He looks back at me confused for a minute, then realizes what I'm looking at."
    t "A tiger."
    menu:
        "What happened?":
            $ tRep -= 1
            play sound "752275__ienba__magic-reveal.ogg"
   
            t "I told you, a tiger happened."
            n "But-"
            t "What more do you need to know?"
            t "My folks had one they trained for shows. She first figured out she was bigger than me, then that I wasn't a tiger around the time there was blood everywhere."
            t "The only reason I'm alive is because she listened to me begging for her to let go." (6)
            n "Really?"
            t "Yeah, and they killed her anyway."
            n "Cause she only listened to you?"
            t "Yeah."
        "Is that why you favor bunnies?":
            $tRep += 1
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            "A bunny is about as far from a tiger as you could get."
            "I don't think he's ever mentioned being interested in taking care of cats, let alone anything bigger than a lunch box."
            t "I guess."
            n "I never heard you talk about any of the animals at your parents' circus the way you talk about your bunnies."
            "He seems genuinely surprised."
            t "Never thought of it like that. I guess because they aren't really mine, I just grew up working with them."
            t "After I got hurt, and a bunch of protests, they sort of phased out the animal acts."
            t "I've thought about working with birds, but they're either too fragile or they live so long I'd worry about leaving them behind."
            "Then the tiger probably isn't alive anymore."
            n "What about dogs? I've seen a few acts on talent shows that use rescue animals in their shows."
            t "I'd need help raising that many dogs. If I'm going to a shelter, they're all coming with me."
            "He hangs his head."
            t "Man, what am I going to do with so many little ones?"
        "Did you fight in the riots?":
            #Unlocks bonus interaction with Shoma)
            t "Yeah. It didn't matter that I didn't go to school with you guys, I got scooped up with everyone else. I didn't get this from it, though." (13)
            #[If talked to Shoma first]
            if $shoma_quest = True:
                "This was the kid that saved Shoma's life."
                t "What's so funny?"
                n "Well, Cinderella, someone's been desperate to find you. You're a hero."
                t "What?! Who? Since when?"
                n "Shoma said he got rescued by someone with a scar on his back once the mind control wore off."
                n "He's been sitting on a confession this entire time."
                n "Dude seriously thinks you're like He-Man or something."
                if shRep > 4:
                    t "Really?" 
                    n "Yeah, the only reason he agreed to help with the dance was to try and find you."
                    n "But you brought a costume from home, didn't you?"
                    t "Forget that part, what do you mean he's been sitting on a confession?"
                    "Sorry, Shoma. It's for the greater good."
                    n "Taiga, come on. He's in love with you.
                    n "If you go up to him and say who you are, he'll be over the moon, instant boyfriend."
                    n "I guarantee it."
                    t "He doesn't even know me!"
                    n "But he wants to."
                    t "You're crazy."
                    "Hopefully that means he'll think about it."
                else:
                t "Aw man. Not that I'm not flattered, but I don't know him." 
                n "Sure you do."
                t "I mean, he's never wanted to hang out or anything."
                t "I think the only time I talked to him was when he was preparing for the dance, and even then..."
                t "It sounds like he's in love with an idea."
                n "I guess, but don't all relationships start out that way? You don't really know someone, and then you do?"
                t "Yeah. You and I have been getting to know each other pretty well. You don't have to worry about some rival."
                n "I didn't mean it like that!"
                t "Sure you didn't." 
            else:
            n "Why didn't you say something sooner?"
            t "I mean, didn't everyone get caught up in it? I wasn't special."
            n "I don't know, everyone else got a chance to yell at me for dabbling in mind control."
            "When he said he wasn't from here, I assumed that meant he wasn't involved."
            t "Nagen, I wasn't mind controlled."
            n "Hunh?"
            t "I noticed that kids with the helmets weren't attacking each other, so I put on a dud and pretended I was one of you guys until I could figure out what the hell was going on."
            t "I still don't get it, but hey, I'm alive aren't I?"
    "He shrugs and disappears into the water. A few seconds later, his head pops up."
    show taiga sad talk1
    t "Wh-what are you w-waiting f-f-for?" 
    "This was my idea."
    "I repeat it in my head over and over, right until I'm ankle deep in the lake."
    "I'm frozen by pins and needles. I bite back a yelp so we don't get caught."
    show taiga mad talk
    t "C-come o-on. Wh-what are you w-waiting for?" 
    "If I take too long, this asshole's going to pull me in."
    "As it is, I have to sort of run away from him while he follows like a crocodile."
    "If the water is freezing, coming out of it must be worse."
    "I run until I'm waist deep. Again I'm struck by how cold the water is and how I could have suggested literally anything else."
    t "Don't look at me like that, this was your idea!" 
    "I wave for him to keep it down. After all, if we get caught before I even get to try and swim, I'll have suffered for nothing. I bite the bullet and plunge off the sand shelf into the deep end. On the upside, my fingers have gone numb."
    #[No sprite]
    ik "What's going on out there?" 
    show taiga gasp
    "A lamp ghosts over the camp site. Taiga pulls me under while we wait for the light to pass. We pop up for air as quietly as possible. The swim to the far side of camp is slow, but eventually we make it to shore without being spotted."
    n "Our clothes..."
    "We're going to have to run through camp soaking wet and hope Professor Inukai doesn't find them."
    ik "What do you think you're doing?"
    "We both scream, waking up the nearest tent."
    "Turning off the lamp while he searched the camp was a dirty trick, but at least he brought us our clothes."
    ik "It's not safe to go in the water without someone on lifeguard duty. Drowning happens faster than you think."
    "We get lectured the rest of the way back to camp."
    hide taiga
label Taiga5:
    scene backgroundroomn
    "I promised Taiga I'd dig through all my memories, even the unpleasant ones, to see if I could find that circus number. I even tried looking it up during vacation, but I got nothing."
    "Though, it could just be Sakurai is written in something I can't type. So to prove to him I was doing what I said I was, I let him in on one of the nights I went sifting through my own head."
    show taiga gasp
    t "You got a TV in here?"
    n "Uhh..."
    "Technically, I'm not supposed to have one, but we never bothered to take it out after the first ransom tape."
    n "All I've found so far are those magic eye documentaries and a dozen copies of the same black and white movie."
    n "I also have books."
    "Everyone has books; we basically live at a library."
    n "Sorry I don't have much to entertain you with."
    show taiga grimace
    t "Dude, it's fine. Hou and I are used to entertaining ourselves."
    n "It's just gonna be really boring to watch me."
    t "It's fine."
    "I get as comfortable as I can with someone sitting at the other end of the bed. He said it was probably on a TV commercial so..."
    hide taiga
    #[CG: Lab]
    scene background_NagenFB_Testing
    "Someone walks by the viewing window. They're watching a video without their headphones in."
    TV "-Sponsored by Basil mobile-"
    "Nope."
    "Ugh, come on, you know where you watched the most TV."
    #[CG: Nurse with needle]
    scene background_NagenFB_CheckUp
    Nurse "Do you know what show this is?"
    "I do now, it was some sitcom from the 90s."
    "It was the only thing on at 2AM that was remotely kid appropriate."
    "I didn't get any of the jokes, but at the time-"
    n "No!"
    "They couldn't wait one hour, they had to put in another IV right then."
    Nurse "What colored shirts are they wearing?"
    "The needle gets closer."
    Nurse "Hey, Cash, I might need another hand."
    "Come on, where's the commercials already?!"
    scene background_NagenFB_CheckUp_Nurse
    #[CGs, nurse with eyes]
    "Two more nurses come in."
    "They're going to hold me down again."
    "There's a bank ad playing right now, not what I need."
    "The needle goes in and I flinch. The pain is just as real as it was back then."
    "I can't breathe."
    Nurse "It blew."
    Nurse "Come on hun, you need to hold still."
    menu:
        "Give up":
            $ tRep -= 1
            play sound "752275__ienba__magic-reveal.ogg"
            #[CG clears]
            scene backgroundroom
            show taiga grimace
            n "I can't! I'm sorry, I can't!"
            "There's nothing in my hand."
            "It was all in the past."
            "Still, I'm pale as a ghost, and I can feel sticky tears had fallen while I was out of it."
            show taiga sad talk2
            t "You just started..."
            "He's got to know how hard this is for me."
            "I can't exactly fake having a panic attack."
            t "Aren't there memories that aren't traumatizing as hell you could check?"
            n "No, that's what I was trying to tell you."
            n "They're all from when I was in the hospital."
            n "That's the only time I was allowed near cable tv."
            show taiga sad talk1
            t "...then why did you agree to do this?"
            n "Hunh?"
            show taiga mad talk
            t "I don't want you doing this to yourself. If it was going to be this hard, we could have done something else."
            t "Both of us have a burner phone, we could have been trying random numbers together or something."
            t "Do you realize how many weeks we've wasted?"
            n "I'm not- I thought I could handle it, but I can't. I'm not faking."
            t "I know."
        "Hold still":
            "Someone holds my other hand. It didn't happen like that."
            "Someone held me by the shoulder, and another by the forearm while the nurse tried two more times to get a line."
            "I squeeze and feel the warmth under my fingertips."
            "I can't see Taiga and the memory at the same time, but I can feel him."
            Nurse "We got it. Good job."
            scene background_NagenFB_CheckUp
            "That's when I see it out of the corner of my eye."
            "Elephants waving their trunks in front of a pink stage coach."
            "Czeceuraei. Welp, wouldn't have guessed that, but that has to be it."
            n "Eight, four, two-"
            "The hand leaves mine for a moment."
            "I can hear something beep, but it's synchronizing with the monitors from the past."
            "I feel his hand on mine again."
            "He squeezes again. We got it."
            scene backgroundroom
            #[CG clears]
            show taiga
            "I leave the memory as quickly as it came."
            Phone "We're sorry, that number's not in service."
            n "No... No that can't be it."
            n "I'll go back."
            show taiga gasp
            t "Don't!"
            show taiga sad talk2
            t "I shouldn't have asked this of you, man. I had no idea it'd be this bad." 
            n "It's fine."
            t "It's not though." 
        "Reach out for Taiga":
            $tRep += 1
            play sound "823594__happypizzabread__game-ui-sfx-practice-9.ogg"
            "They're going to hold me down. I reach out wildly."
            "There's someone right above me that I can't see."
            scene background_NagenFB_CheckUp_Eyes
            "A face, soft with the smallest bit of bangs and the rest shaved."
            "The hell is he doing so close? I thought I left him at the edge of the bed."
            "I use his shirt collar to pull myself up. It's disorienting to remember being held down while I pull myself up."
            "It's like my arm is in two places."
            "One being treated like a pin cushion and the other wrapped around Taiga's back like he could possibly shield me from a figment of my own imagination."
            scene background_NagenFB_CheckUp
            "That's when I see it out of the corner of my eye. Elephants waving their trunks in front of a pink stage coach."
            "Czeceuraei. Welp, wouldn't have guessed that, but that has to be it."
            n "Eight, four, two-"
            "He doesn't leave."
            n "Aren't you going to write it down?"
            "I can't hear him over the chorus of voices behind me and the memories of my own crying, but I feel a warm hand stroke the back of my neck."
            "I keep going."
            "I then leave the memory as quickly as I can."
            #[CG clears]
            scene backgroundroom
            show taiga sad talk1
            n "Aren't you going to call it?" 
            "I got tears and snot on his front. How embarrassing."
            t "You didn't have to do that for me." 
            "He saves the number in his phone. We don't even know if it'll work yet, but he hugs me again."
            t "You didn't have to do that."
            "We sit in silence for a bit."
            show taiga sad talk2
            t "You, uh, want to talk about it?"
            n "Hell no!"
            "I can feel the raised edges of his scar through his shirt."
            t "Yeah, me neither." 
    show taiga
    t "You were wrong by the way. It wasn't boring."
    t "Your eyes, I could see what was happening in your eyes."
    n "What, really?!"
    show taiga gasp
    t "It was backwards, but yeah. I could see what you were seeing."
    n "It didn't used to be like that. At least, you'd think something like that would have shown up in the progress reports."
    show taiga grin
    t "Next time, you should remember something cool, like a beach or something. Then I could take a picture for you and show you what it looks like." 
    n "Jona would love something like that."
    "Next time he tries to draw me, it'll be with big window eyes."
    hide taiga
label Taiga5:
    #(Chapter 5, before going on the mission, with a maxed out rep)
    #(Characters: Nagen, Taiga, Taiga's Mom, Maimai)
    scene backgroundschoolnoon
    "I managed to convince Taiga to show up before noon."
    "It was hard to do so without spoiling the surprise."
    show taiga suspcious
    t "You mind telling me what this is all about?"
    n "Well, I decided to think outside the box a bit."
    n "I got to have one phone call home, so I cashed out a favor."
    t "The hell are you talking about?"
    "Maimai's car pulls up to the roundabout. I hold my breath, worried for a moment that they found the wrong person."
    "Then a woman with slate grey hair steps out of the car."
    show tiaga gasp
    t "MOM!"
    "I have no clue what they're saying to each other."
    "He hugs her."
    "Taiga is blabbing fluently in another language, while who I think is his mom is asking him to slow down."
    "Then, without letting go, he looks at me."
    show taiga annoyed
    t "You did something stupid again, didn't you?"
    n "Only a little."
    "I have no clue if my plan is going to work."
    "If I'm wrong about who's behind all this, my neck will be the first on the chopping block."
    "Still, I was able to use what little leverage I had to actually do something."
    n "I promised I'd help."
    show taiga mad talk
    t "Espèce de beau idiot. Si tu te fais tuer, je ne te pardonnerai jamais!"
    n "What was that?"
    TaigasMom "I love you."
    show taiga annoyed
    t "No it was not! Not exactly. I don't get it, how-"
    n "I appealed to someone's inner Karmic Gladiator."
    show taiga grin
    show maimai smile at left
    mm "Between Babylon and I, we'll be helping your family navigate Guwon's guardianship system."
    mm "Now go, you only get thirty minutes with your mom. You'll have plenty of time to interrogate Nagen later."
    hide taiga
    "Taiga immediately takes his mom by the arm to show her the school."
    "I don't know if half an hour is enough to explain everything that's happened with us, but when she looks back at me, he starts yelling something at her again."
    hide maimai
    show maimai oh
    mm "What does he mean by 'again'?"
    n "Come on, when am I not doing something other people think is stupid?"
    n "Don't worry. It's for a good cause."
    mm "That's what you always say."
    hide maimai
    #[Segue into final scene with Maimai]
    return

label TaigaF:
    pass    
