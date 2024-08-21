label YokuVisit:

    if yTurn == 0:
        jump Yoku1
    elif yTurn == 1:
        jump Yoku2
    elif mTurn == 2:
        jump Yoku3
    elif mTurn == 3:
        jump Yoku4
    else:
        jump YokuF

label Yoku1:

    scene backgroundclass
    
    "I continued to map out the school grounds in my spare time."
    "The fourth floor consisted of vacant offices for the teachers and an archive room left over from when this place was a library."
    "The third floor was split between computer labs and electives classes."
    "The rest of the central building just looked like regular classrooms. Hard to tell with most of the doors still locked."
    "There was one thing that bothered me. The internal layout, it reminded me of Estella…"
    "What am I thinking? Of course it’s familiar, there’s only so many ways to build a school, why reinvent the wheel?"
    "I’m just overthinking things."
    
    n "Music?"
    
    scene backgroundcourtyard
    
    "I followed the sound to the back courtyard."
    "Oh, it’s that guy. Yoku sat playing a beat up violin."
    "I’m begrudgingly amazed he can make it sound so incredible."
    "He paused."
    "He seemed hopeful for a moment, but then saw me."
    
    n "Why did you stop playing?"
    
    y "Your footsteps were so o-obnoxious, I could hardly hear myself play."
    y "For an Ex-Sniper, you sure love to breathe through your m-mouth."
    
    n "Most people don’t notice those things, let alone comment on them."
    
    y "I can’t help but n-notice, having div-v-visive hearing will do that."
    
    "He put away his instrument with a sullen expression his face"
    
    y "This place is so far rem-moved from most refugee sites, I had hoped to finally practice in peace."
    y "Even with such sm.mall numbers, this place manages to feel crowded."
    
    "I’m getting the feeling he’d be just as angry at anyone else who wandered by."
    
    n "It’s not too late to become a hermit and live in the Andes."
    
    y "A nice sentim-ment, but logistically impractical. As a m-musician, I need to be relatively app-proachable."
    
    "How relative are we talking?"
    
    n "You’re pretty good, I think this is the first time I’ve heard you play."
    
    y "P-p-pretty good? Ugh, I have to tr-ry harder."
    
    menu:
        "Your playing is fine":
            $ YRep += 1
    
            y "Fine isn’t good e-enough, I need to master every instrument if I’m ever to rise above pedestrian talent."
            y "‘Fine’ doesn’t earn co-ontracts or benefactors."
    
            n "I thought you were a composer."
            n "I get that you don’t like people, but I’m pretty sure directing musicians is part of the job description."
    
            y "I can’t use other m.musicians, it’s part of the rules."
    
            n "Rules?"
    
            y "I must write and perform a sere-serenade using every instrument, a-alone."
            y "Only then can I prove my m-mastery of the art."
    
            n "Sounds like a fool’s errand to me. Whoever told you that just wanted to keep you busy."
    
            y "You’re probably right. No m-matter, I am a man of my word."
            y "Besides, once I achieve the impossible, people will be b-breaking down my door with job offers. I should invest in a business address."
    
            "More power to him I guess."
        "Does it matter?":
            $ Intel += 1
    
            n "As long as you enjoy playing, that’s all that should matter, right?"
    
            y "I suppose, were I playing recreationally. I don’t p-practice seven hours a day to sound p-pretty good."
    
            n "You have to be exaggerating, when do you sleep."
    
            y "Including weekends the nu-umbers added up. I’m not so careless as to negl.l.lect needs, unlike some people."
    
            n "Still, that seems a little excessive."
    
            y "It’s a necessity if you want to survive. Talent and joy doesn’t breed success, persi-si-stence does."
    
            "I get what he’s saying. I mean, I wouldn’t be here if it wasn’t for the hours I put into studying. Even still…"
    
            n "The most successful are the ones who possess both. Otherwise you end up suffering and loose whatever interest you had."
    
            y "Are you under the impr-r-ression I ha-ate what I do?"
            y "This isn’t a hobby for m-me, it’s a car-reer. I’m serious about what I do, that’s all."
            y "Since when did d-dedication and elevated sta-a-andards equal disco-ontent."
    
            "Nevermind, I don’t get this guy. I’ve never spent every waking hour focused on one thing, not by choice at least."
    
            n "My bad, it just didn’t seem like any of it was making you happy."
    
            y "Is that so? Hmm… You’ve giv-ven me so-omething to think about."
        "I'm not easily impressed":
            $ YRep -= 1
    
            y "I’m not trying to imp-press you!"
    
            n "Ooh, do I know him?"
    
            y "I’m not trying to imp-press a g-g-guy!"
    
            n "Your haircut says otherwise."
    
            "No witty comeback to that one I see."
    
            y "She isn’t h-here right now, but I had hoped she would be."
    
            "That’s why he was so excited when I first showed up."
    
            y "Her proficiency was medio-ocre at best when we were children. It wouldn’t surprise me if she wasn’t a-allowed in."
    
            n "Do you have anyway of getting in touch with this girl?"
    
            y "Not since we were fitted with your obedience collars. Even if I c.could, she wouldn’t want to ta.alk to me. Not yet."
    
            "There might not be anyone to talk to if she was in the army."
    
            n "Uh, yeah, good luck with that."
    $ Intel += 1
    $ yTurn += 1
    
    "He finished packing up his stuff with a sigh."
    
    y "Why are y-you here?"
    
    n "You’ve already asked me that."
    
    y "Yes, and you dodged the question l-l-last time. I want to know."
    y "Why would you, a famed villain of sorts, be wa-andering around school like nothing happened? It doesn’t m-make sense."
    
    n "You don’t seem to have a problem talking to me. I mean, yeah I get the stigma, but just because I did bad things doesn’t make me an asshole, or a bad person."
    
    y "So you’re just here b-because you can be?"
    
    n "Is that a crime?"
    
    y "N.no, but it’s certainly disappointing."
    
    "I don’t know what this guy expects of me."
return

label Yoku2:

label Yoku3:

label Yoku4:

label YokuF:
    scene backgroundfield

    return