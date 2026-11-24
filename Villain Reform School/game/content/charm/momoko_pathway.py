label MomokoVisit:

    if mhTurn == 0:
        jump Momoko1
    elif mhTurn == 1:
        jump Momoko2
    elif mhTurn == 2:
        jump Momoko3
    elif mhTurn == 3:
        jump Momoko4
    elif mhTurn == 4:
        jump Momoko5
    else:
        jump MomokoF

label Momoko1:

    scene backgroundlab
    "Momoko makes use of the chem lab from when classes let out to curfew."
    "Music blasting out of the door and into the hallway is a guarantee that she's in."
    "I do better when I'm working alongside someone, so I've brought stuff to work on while she stares intently at her experiments."
    "Only today, it seems the thing she's staring intently at is me."
    show momoko confused
    mh "Nagen, are you going grey?"
    "How could she tell? I made sure to touch up my roots before school started. Hair doesn't grow that fast, does it?"
    mh "Nothing to be ashamed of, I'm just trying to figure out which part is dyed and which part is natural."
    mh "You, uh, sort of missed a chunk by your ear." 
    n "Damn."
    "And Uitto didn't even bother to tell me."
    show momoko happy
    mh "Were you trying to go for midlife crisis black?"
    n "Haha, very funny."
    "She takes my pencil away from me. "
    show momoko talk
    mh "I'm trying to figure out what dye to make you, dork. Isn't that why you're sitting in here?"
    n "No, I just wanted to hang out."
    show momoko surprise
    mh "Really? Wouldn't you rather hang out with your other friends?"
    n "Uitto doesn't like when I work on other things around her, Hiro's too distracting, and Jona says I'm too much of a distraction when he's trying to work." 
    "Somehow, all of them are already behind." 
    n "I knew if I came here, you wouldn't be mad that I was working on stuff."
    show momoko sad talk
    mh "Of course not. I'm just, I don't know, surprised? I'm not used to people thinking about me honestly."
    mh "Anytime we worked together in class, I just assumed you got stuck with me. I didn't think you actually chose to work with me."
    "I guess some changes are only superficial. When we were kids she was the quietest person in the room."
    "She speaks her mind a lot more now, but maybe she's still insecure on the inside."
    hide momoko
    menu:
        "Of course I did.":
            $ mhRep += 1
            show momoko confused
            n "You actually did the work, and early."
            n "I knew working with you wouldn't be a month long anxiety attack where I had to do everything last minute."
            show momoko worry
            mh "Oh my God, that's the worst. Love Rei, but no matter how many times I'd remind her, she'd never turn anything in."
            mh "I always felt like such an asshole just asking people in my group to do their job."
            n "Yeah, I'd rather get things done now and not have to worry about it."
            mh "I get that, but we're not working on an assignment together. We're just doing our own things."
            n "That's what makes it fun."
            show momoko puzzled
            mh "Fun?"
            "She shuffles her feet back and forth, the wheels of her skates making it seem like she's bobbing in the sea."
            mh "I mean, it is fun. It's just cool to hear someone else call it fun instead of being a weirdo, y'know?"
        "It wasn't bad.":
            show momoko surprised
            n "Back then, there were the five of us, so someone always got left out."
            n "It was nice to have someone to partner with when that happened."
            "Hiro and I always fought over who partnered with Odori, only to lose to Uitto."
            "The three of us would then be left to vote on who had to wander outside of our comfortable social circle."
            n "Jona and I always knew we were safe if you were our partner."
            mh "Jona too? Man, and this whole time I thought I was some booger people got stuck with."
            mh "You ever want to go back in time and like, shake the stupid out of yourself?" 
            n "All the time. I remember everything from when I was six years old onward."
            show momoko puzzled
            mh "I guess we both have things we wish we could forget."
        "I didn't.":
            $ mhRep -= 1:
            show momoko sad
            n "To be fair, I would've been stuck working with anyone."
            n "No one really liked working with me, they just wanted me to do the work for them"
            "It pisses me off just thinking about it."
            mh "Same. I just... didn't know how to complain about it at the time."
            mh "I was so scared of getting bad grades, I'd just do the work anyway."
            n "That's not something to be ashamed of."
            show momoko sad talk
            mh "But it didn't make me happy. I mean, look at us now. Our parents, those teachers; none of them are around to care anymore."
            mh "It was pointless people pleasing." 
            "I know she's talking about herself, but it still stings."
    show momoko sad talk
    mh "I spent my whole life trying to be invisible."
    show momoko sad
    mh "I even tried straightening my hair so it was one less thing people could point at me over."
    mh "Y'know, cause if no one notices you, they can't have anything bad to say. You're like wallpaper or a desk lamp then."
    mh "You're just there. It's nice to know that I was wrong, even if we didn't talk much."
    n "Are you okay?"
    "I can't put my finger on it, but something about the way she's talking concerns me."
    "I don't remember anyone bullying her in school or anything, but she talks like everyone used to hate her. It's odd."
    show momoko surprise
    mh "Oh yeah. Compared to before, I am much more... me. I feel like me as opposed to nothing, which is better."
    show momoko base
    mh "It's just a lil' surprising hearing about how other people felt about me."
    mh "It doesn't seem real. 'Cause like, I'd get why you'd think about me now, but then? Wild. You're such a nerd."
    n "Hey, if I wanted to be called a nerd for working on homework, I'd study with Uitto."
    "She laughs."
    show momoko happy
    mh "Tell you what: even though you didn't come here to get your hair fixed, I'll still do it as a group project of sorts."
    mh "We're far out from any store that would sell dye, so I can help keep your roots from showing. It'll be our little secret."
    n "Really?
    show momoko worry
    mh "Yeah, but I want to do it right. What color were you actually going for?"
    "I pull out a ballpoint pen and scribble on the corner of my homework. She looks at it, then up at my hair and frowns."
    show momoko talk
    mh "I see, so you put in the base color with no highlight. It would be easier to dye all your head one color."
    mh "Do you want to keep the streaks?"
    n "Only if you can find a dye that's my natural color."
    mh "Blue's a tricky one to do permanently. I'll look into both. That is, unless you want to do something more fun?"
    n "If I change it too much, Jona'll wig out."
    show momoko
    mh "Got it. God, I hope I didn't distract you too much. I know you were working on something and I just started gabbing."
    n "It's fine. I like talking to you."
    "It's the perfect balance really. I'd rather be here than alone in my room."
    "She fidgets in place again and looks away while playing with her extensions."
    "I wonder if there's anything I could do to help her in return..."
    "At the end of the night I packed up my stuff, having made a good dent in everything that had been assigned for the week."
    hide momoko
    return

label Momoko2:
    scene backgroundlab
    "Any hopes I had of working on homework have been dashed by the noxious fumes filling the lab."
    show momoko
    "Momoko's music is on full blast, the same CD from the day before. There's a couple of plastic bowls on the counter."
    "Her gloves are stained various shades of blue." 
    n "Momoko, did you open a window?"
    "She can't hear me, bobbing as she titrates liquid into a bowl of white powder."
    "There are various things on fire and tubes dripping into other things. I crack open the window, which catches her attention."
    show momoko happy
    mh "Nagen, you made it! Check it out."
    "She points to cloth hanging over a bunsen burner, each one darker than the rest."
    mh "They have raspberry drank mix. I have no idea how many washes it'll hold up to, but it should get your roots to the color you want."
    "A light splotch blooms on the fabric where she touched it."
    show momoko sad talk
    mh "It'll look better if we lighten the parts you botched first and then put the new color on."
    n "Is that safe? It kinda smells like ammonia in here." 
    "Now that I think about it, isn't that the stuff in pee?" 
    n "Momoko, where did you get ammonia?"
    show momoko
    mh "Relax, with enough firepower, you can squeeze all kinds of elements out of the air. But it's not ammonia you're smelling, it's bleach."
    "She holds up one of the plastic bowls." 
    mh "All they got is the cleaning kind, which is too acidic to bleach hair with. I've been trying to bully it into being basic." 
    "I eye the stinky bowl with suspicion. She did not answer my question about how safe it is."
    show momoko sad talk
    mh "We'll test a small section here in the back, and if it's ass, we can just cut it and pretend nothing happened."
    n "If you say so."
    mh "Really? Just like that, you trust me? You're crazy, man."
    "She paints the test strip in my hair."
    hide momoko
    menu:
        "I don't have a choice.":
            show momoko sad
            n "It's this or Jona's markers."
            "I hate the white in my hair. People already said I looked like my dad."
            "The last thing I need is his hair color haunting me first thing in the morning."
            mh "I mean, you could go all dark. It might look more natural then."
            "She must have taken her glove off. It's weird having someone's bare hand combing through my hair. Not bad, just weird."
            show momoko happy
            mh "That's the cool thing with hair; you can do whatever you want with it and it'll grow back."
            mh "Speaking of it growing, how long do you want this part before you shave it again?"
            n "As long as it doesn't stick up in the back, it's fine."
            show momoko sad talk
            mh "So free real estate then. Your hair is so light, we could put a pattern in pretty easily."
            n "I'm good."
            "As it is, I'm a little nervous about trusting her around flammable chemicals."
        "Of course I do.":
            $ mhRep += 1
            show momoko manic
            n "This is something you like to do, right?" 
            mh "Well, yeah, but practicing on a live human is different than the mannequin head."
            mh "Especially right now. Not a lot of people willing to part with their hair for newbs like me at the moment."
            n "You have done this before, right?"
            show momoko puzzled
            mh "On myself, but no offense Nagen, our hair is very different. There is a slight chance I fry it before I get the timing right."
            mh "It is already pretty brittle."
            n "Matches the rest of me." 
            show momoko manic
            mh "OMG, that's right, you were sick like all the time. You're doing okay now?"
            "I'm not sure how to answer that."
            show momoko talk
            mh "It's fine if you're not. Pretty sure everyone here feels like shit and is just too scared to talk about it."
            mh "I know it's hard to tell who's safe to talk to, but I'm here if you need someone to talk to."
            n "Thanks."
            "She doesn't press further, and leaves my side to check on the open flames."
            "Is it really okay to have all this stuff out and open at the same time?"
        "I don't trust anyone.":
            $ mhRep -= 1
            show momoko surprised
            mh "Really?"
            n "I mean, do you blame me?"
            show momoko sad talk
            mh "No, but I figured you at least trusted Hiro and the others. They care about you a lot."
            n "Well, yeah, I care about them too. I just meant in general, I try to keep my expectations low."
            show momoko talk
            mh "Okay edgelord, see how far that kind of thinking gets you."
            mh "Meanwhile, the rest of us will be honest about having standards and holding people to them."
            mh "Haven't you ever heard of fake it til' you make it?"
            n "Like, affirmations? I don't think those work."
            show momoko sad talk
            mh "Well, something's got to and doing something is better than doing nothing."
            mh "Case and point, these sad little hand laid streaks. Hmm, maybe I should've wrapped this."
            mh "It's drying out a little too much."
            "I feel like I've made a mistake."
    show momoko surprised
    mh "Shit."
    n "What's shit? What did you do?!"
    mh "Nothing!"
    "She goes to rinse my hair out with her bare hands. The back of my head feels lighter for some reason."
    n "Momoko? What. Happened."
    mh "I think the dye you used had metal in it. I didn't think a dark dye would use metal, I'm so sorry."
    n "Metal?! How can you tell?"
    mh "It melted."
    n "What did?"
    mh "Your hair."
    "I can't see it myself, but it sounds bad. She gives up on the bleach and reaches for the boiling blue beaker instead."
    show momoko worry
    mh "I can at least mask the roots for a week or so with this stuff."
    mh "It won't be perfect, but it'll look better than having your roots showing."
    n "But how did you know metal made it melt? You're using a bunch of harsh chemicals, couldn't that do it?"
    show momoko talk
    mh "Naw, when chemicals burn hair it splits like a banana and gets all crinkly."
    "She shows me the end of one of my lost hairs."
    mh "Here you can see how it's wider and thinner than the untreated hair."
    "I can't, it just looks like hair to me. That is, until she squishes it between her fingers and it spreads like ink."
    mh "If I had a nickel for every time I made something that melts metal, I'd have two nickels."
    show momoko sad
    mh "It'll take me a bit longer to make a bleach that won't interact with the deposits on your hair though."
    mh "Not quite ready to give up yet, but the lack of supplies here will seriously limit what we can do."
    "That's pretty much where we're all at. Still, it's cool that she's at least trying to make up for it."
    "It could be a while before commercial stuff like hair dye is on shelves."
    "Everyone's more focused on regular rebuilding efforts, which is important, but stuff like this makes things feel a little more normal."
    "After she's done, she tells me to wait a few hours before rinsing it out."
    "I have a bad feeling it'll all wash out, but I appreciate the effort."
    hide momoko
    return
label Momoko3:
    scene backgroundlab
    "I am of two minds."
    "On one hand, the fact that Momoko is so dedicated to figuring out how to bleach my hair relatively safely means a lot, especially since she's doing it as a favor."
    "On the other hand, I now know someone that has collected clippings of my hair for personal use."
    "If anyone finds out, I will be mortified. It's for testing purposes, but still."
    show momoko puzzled
    n "How goes the science?"
    mh "Maddening. It would be one thing if I had clean chemicals to work with instead of commercial compounds."
    mh "Anything I make either fries the hair or has a reaction to the metal."
    n "You know, it's cool if you can't do it. I can always get it redone at home. It's not that big of a deal." 
    "I'm pretty sure everyone can figure out I dye my hair just by looking at it."
    show momoko talk
    mh "Too late, it's a point of pride now. I've made more complicated stuff with less before."
    mh "If I can only make one thing on purpose, what kind of genius would I be?"
    n "Yeah, I've been meaning to ask about that. You mentioned melting metal before. Was that on purpose, or was it an accident?"
    show momoko
    mh "It was on purpose."
    mh "The Education Collars were rigged to explode if the hinge around the neck opened, so I made something that would melt through it and not people."
    "She invented something that melts through metal?!"
    n "That's amazing. How did you do that?"
    show momoko sad talk
    mh "Honestly, I just got desperate. Things were going to shit, and I realized we might starve before people figured out how to get them off safely."
    n "You made that in less than three days?"
    mh "Sort of. I had a lot of time to think with that silly thing on."
    hide momoko
    menu:
        "You say that like it's a good thing.":
            show momoko confused
            mh "I never really had time to think before. It was always go, go, go, y'know. 'Harvard waits for no one'."
            n "That sounds familiar."
            show momoko surprised
            mh "Shit, you too? And they seriously wondered why we were sick all the time."
            "She pulls away from the samples."
            mh "I'll figure something out eventually. I'm just bummed I couldn't get it done sooner."
            show momoko worry
            mh "It's kinda like baking."
            mh "Anytime you make a substitution, things could go sideways, and there's only so much hair you can give me before people start to notice."
        "You should patent it.":
            $ mhRep -= 1
            show momoko worry
            mh "I can't. I don't want people hounding me over something I made trying to save my own skin."
            mh "It doesn't feel right to charge people for that. More good'll come from anyone that needs it getting to use it."
            n "But with something like that, you could be free to do whatever you want. You could be like the guy who invented glue."
           show momoko manic 
            mh "I also don't want to make money off of something people are going to turn into a weapon."
        "You'll make other stuff.":
            $mhRep += 1
            show momoko
            n "You made something amazing at fifteen. That gives you eighty-five years to make a second thing."
            n "That's a shit load of time to get the right supplies."
            show momoko happy
            mh "You're right."
            show momoko confused
            mh "Ugh, making stuff is just so hard right now, and it's the one thing that distracts me from the fact we're at school."
            mh "I want to have something new to play with this year."
            n "Hey, I'm not your barbie doll."
            mh "Without bleach you can't be."
    show momoko sad
    mh "It wouldn't bum me out so much if I was trying to invent something new or improve upon something that exists, but this?"
    mh "It's bleach, it's hair bleach, it's been around since the 1600s. If I'm really some great chemist, I should be able to make it easily." 
    n "Really? People have been bleaching their hair that long?"
    show momoko sad talk
    mh "Well, yeah. Vikings would use lye to lighten their hair and before that people would put lemon juice in their hair..."
    mh "Oh my god, that's it!" 
    "She skates out of the room. I have no idea where she's going, but the door to the stairs slams open and shut."
    "If what she needed was down there, I wish she had asked me to go, or at least took her skates off first."
    show momoko happy
    mh "Found it!"
    "In her hands she has a bunch of lemons and some dandruff shampoo."
    show momoko 
    mh "We don't need to completely bleach your hair, we need to get the dye out of it, duh!"
    mh "This stuff always made my dye jobs bleed, which means it'll lighten it!"
    mh "Then when I put the new color over it, it'll blend into an ombre instead of looking like an accident."
    mh "At least, in theory. We should test it first. Worst case scenario, nothing happens." 
    "She closes the curtains to make the room as dark as possible and soaks my hair in pure lemon juice, misting occasionally to keep it from drying out into a sticky mess."
    "When the timer goes off, I'm attacked with the shampoo. Even in the dim light, I can see the white shampoo tinge blue."
    show momoko sad talk
    mh "Not as dramatic a change as I was hoping for, but if you do this every night, we'll start getting places. Deal?"
    n "Deal."
    "I'm glad her solution ended up not involving harsh chemicals. For a second there, I thought she was going to try to make her own lye."
    "That would probably result in another explosion."
    hide momoko
    return
label Momoko4:
    #[Chapter 2 or 4]
    scene backgroundlab
    "I check back in with Momoko once no more dye can be stripped from my hair."
    "There is a limit to how grey I want to look before people take notice. Despite the pounding music, Momoko seems glum."
    show momoko sad
    n "Uh oh, did we jump the gun?"
    "She shakes her head, having a blue paste all ready to go."
    n "Then what's wrong?"
    mh "I said I was going to help you, but in the end, I just did what anyone here could do."
    mh "You might have figured out what I did by accident if you were here long enough."
    "She motions for me to sit down and starts to section out all the parts I had dyed myself."
    show momoko worry
    mh "I keep telling myself if I had better supplies, I could do so much more, but maybe that's a lie."
    mh "The only time I've made something usable was basically an accident anyway. You don't get lucky twice."
    mh "I shouldn't have used your hair to boost my own ego. I'm sorry."
    n "You are helping me."
    "My hair is literally in her hands."
    show momoko sad talk
    mh "Yeah, but anyone can do this. I just happen to be around."
    n "So? I'm glad you're around and that it's you. Isn't that enough?"
    "Something wet drips on my shoulder."
    n "Momoko?"
    mh "Ditto."
    n "Hunh?"
    show momoko sad
    mh "Can I tell you a secret?"
    n "I don't see why not."
    mh "When you guys were telling everyone to put on the Education Collars, I could tell what they actually were and... I put mine on anyway."
    "She let herself be mind controlled?!"
    mh "I really hated who I was and I knew if something bad happened when the helmet was on, no one would blame me."
    hide momoko
    menu:
        "What were you running from?":
            $ mhRep += 1
            show momoko worry
            n "We wanted to help kids run away from home safely. I didn't know everyone's story, but I could see how miserable kids were at school."
            "She had burst into tears one day because she got a 0.7mm dot of juice on her sleeve once, and she barely had anything in her lunch most days."
            "That's not the kind of shit that just happens."
            mh "My mom said I was our ticket out of Crystal Lane."
            mh "If I got good enough grades and looked the part, I'd get a fancy job and could start paying her back for everything she put into me."
            n "You still hear her, don't you? Not literally, but what she would say?"
            show momoko sad
            mh "Yeah." 
            n "I hear it too. Nothing I did was ever good enough for them."
            show momoko sad talk
            mh "I'm good at shutting it out most days, but today's been pretty bad." 
        "I'd blame me":
            $ mhRep -= 1
            show momoko confused
            mh "Really? You don't seem too choked up about the people who didn't make it." 
            n "A lot of people didn't make it. There's not a lot I can do to bring them back, but it does bother me."
            show momoko angry talk
            mh "Oh yeah? Name one."
            n "Odori, for starters. Then there was Kanon, Jazz, Ty, Kiki, Hiyoko, Kira, Sio-"
            mh "I get it, I get it. You remember everybody."
            "Not that I knew everyone all that well. I still know what they looked like, what class they were in, that kind of stuff."
            show momoko sad
            mh "Odori's really gone?"
            n "They said they're looking for a body at this point."
            mh "Are they actually looking?"
            n "I don't know."
        "Stay silent":
            show momoko sad talk
            mh "It's not like I was going to do anything."
            mh "But when I thought about the what if's, it was like a weight lifted off my shoulders."
            show momoko sad
            mh "It should have scared me, thinking those things, but it didn't."
            mh "I just couldn't picture anything different. It was either every day being the same or letting myself fall into the hive mind."
            mh "Looking back, I could have died before inventing anything. At least now I've done something instead of nothing." 
    show momoko angry talk
    mh "The strangest thing happened though, cause like, the world with that helmet on lost all color."
    mh "I couldn't smell anything other than my own face. My body wasn't in my control."
    mh "I could finally think, and I kept thinking of all the things I wished I could do."
    show momoko talk
    mh "Like having fun hair, walking into one of those bath stores and smelling all bathbombs, holding someone's hand."
    mh "Or for once, just once, getting one of those fancy bakery cakes for my birthday instead of one from the grocery store."
    mh "Without anyone hanging over my shoulder telling me it was stupid, I realized those stupid things are what made me happy."
    mh "So I decided, if I made it, I'd do all those things."
    "There are no fancy bath stores or bakeries right now."
    "There's no telling how long it will take for the city to have stuff like that again, or if we'd be able to afford to do any of it."
    n "I think you love the world a lot more than I do."
    show momoko sad talk
    mh "Well, you like me more than I do."
    mh "I'm working on it, but it's hard to feel like I'm making progress when I wake up every day in one of those dingy trailers."
    mh "I do best when I have proof I made things."
    "She sets aside her bowl, admiring the spaghetti strings of blue dye she's put in my hair."
    n "Is there anything I can do to help?"
    show momoko surprised
    mh "What are you talking about?"
    show momoko
    mh "You are helping. You're here."
    "I wonder if there's a way to do some of the things she talked about."
    "Like with the dye, we don't have a bunch of stuff here, but there might be simpler ways to do it."
    "The easiest thing might be the cake."
    hide momoko
    return

label Momoko5:
    scene backgroundlab
    "I was wrong about the cake. Turns out, making an entire thing from scratch with no experience results in a blob."
    "It's a tasty blob at the very least, but it's dry and we didn't have anything to make icing."
    "I almost had flowers to decorate it with, but Professor Inukai stopped me and said I was going to poison someone."
    "So with blob cake number three in my possession, I did my best to surprise Momoko."
    show momoko happy
    mh "Check it Nagen! Not only do I have a bleach we can use, I also made this!"
    "She presented me with a blue bottle."
    mh "It's a combination of the dye and a conditioner to keep the style from fading."
    mh "This way, anytime you need a touch up it'll all blend together nicely."
    mh "I think I was putting too much pressure on myself to make wholly unique things instead of just trying to improve what we have here- What's that?"
    show momoko surprised
    "She noticed the cake. Can I even call it a cake if it's just the cake part?"
    n "It's, uh, thank you gift. For helping with my hair."
    show momoko happy
    mh "Whaaaat? But I was doing your hair as a thank you for hanging out with me. You can't thank a thank you. That's like, gratitude inception."
    n "Then for the conditioner stuff then."
    show momoko
    mh "What, this? This is nothing."
    n "I mean, let's be honest, so's this cake. You're right, this was silly, I'll just-"
    mh "Wait!"
    "She must have thought I was going to throw it away. She rushes forward on her skates, bottle in hand and all four things collided in one big mess."
    "Both our gifts were smeared across the lab counter top."
    show momoko sad talk
    mh "Aw man, I'm sorry. I was trying to- I made a mess of things."
    n "It's fine! In hindsight I shouldn't have brought food in here. I wanted to surprise you, but yeah, chemicals."
    hide momoko
    menu:
        "Be honest":
            $ mhRep += 1
            show momoko sad
            n "It's my fault you haven't gotten to do any of the things you wanted to do when you got out."
            n "I thought I could try and make up for it somehow, but-"
            mh "Nagen, I mean this as disrespectfully as possible, I don't expect you to fix anything."
            n "But I-"
            show momoko sad talk
            mh "You alone were not responsible for what happened to us. You didn't fuck up the town with fire bombs and tear gas."
            mh "There was other shit wrong with Guwon, it wasn't just you."
            mh "I appreciate you're trying and that you're my friend. That's all that really matters."
        "Hold her hand":
            $ mhRep += 3
            show momoko surprised
            n "I'll make another one."
            mh "Nagen? What are you-"
            n "I want to make you happy in any way I can. There's not a lot I can do, but I want to try."
            show momoko
            mh  "Happy, or like, romantic happy? 'Cause one of those things I might need meds and therapy for, y'know." 
            n "Both. Is that... Is that okay?"
            mh "Y-yeah. Sorry, my mind's a little blown right now."
            "She glances down at our hands. I haven't let go yet. She turns her hand around so she's holding mine back."
        "Leave"
            $ mhRep -= 1
            show momoko sad
            n "I should go."
            mh "Nagen, I'm so sorry." 
            "I have cake in places there should not be cake. Something on my neck is burning and I just want to get a new set of clothes."
            "I can't even hide my disappointment at this point."
    show momoko sad
    "I help Momoko clean up the mess."
    mh "The truth is, part of why I was freaking out was... The Karmic Gladiators offered me a spot after graduation." 
    "It's my turn to be a walking hazard. I nearly drop all the cleaning supplies I'm holding."
    mh "They were really impressed with the Inorganic Solvent and thought I'd be a great desk agent. Y'know, help make stuff for heroes, but..."
    mh "I just got into my head that it was an accident, that I couldn't make anything else. I got scared."
    n "You could be a Karmic Gladiator?! Have they assigned you a hero identity already? Or do you get to pick one yourself?"
    n "Please tell me you said yes!"
    show momoko surprised
    mh "You really think I could be a professional hero?"
    n "Are you kidding? Of course you could!"
    "Maybe I'm projecting a little. I did always like the desk agent heroes, the sort of people who made cool gear or did detective work."
    "It would definitely give her the free time to play around with chemicals to her heart's content."
    show momoko confused
    mh "I have until graduation to make my decision, but if you think I could hack it, then maybe... I want to prioritize the dyes first."
    mh "Until I can make something that I'm proud of, I won't be able to call myself a hero."
    n "I'm more than happy to lend a hand."
    show momoko
    "She smiles. I really hope I'm not putting too much pressure on her. Getting scouted was always my dream as a Junior Gladiator."
    "Still, there's a part of me that's giddy at the idea that one of my friends, after all this mess, could still make it as a hero."
    "I'll have to work twice as hard so we can be heroes together."
    hide momoko
    return
label Momoko6:
    scene backgroundlab
    "Looks like Momoko's not here."
    return