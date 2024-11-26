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

show YEyeroll

"Oh, it’s that guy. Yoku sat playing a beat up violin."
"I’m begrudgingly amazed he can make it sound so incredible."
"He paused."
"He seemed hopeful for a moment, but then saw me."

n "Why did you stop playing?"

hide YEyeroll
show YIrate

y "Your footsteps were so o-obnoxious, I could hardly hear myself play."
y "For an Ex-Sniper, you sure love to breathe through your m-mouth."

n "Most people don’t notice those things, let alone comment on them."

y "I can’t help but n-notice, having div-v-visive hearing will do that."

"He put away his instrument with a sullen expression his face"

hide YIrate
show YIrate2

y "This place is so far rem-moved from most refugee sites, I had hoped to finally practice in peace."
y "Even with such sm.mall numbers, this place manages to feel crowded."

"I’m getting the feeling he’d be just as angry at anyone else who wandered by."

n "It’s not too late to become a hermit and live in the Andes."

hide YIrate2
show YBummed

y "A nice sentim-ment, but logistically impractical. As a m-musician, I need to be relatively app-proachable."

"How relative are we talking?"

n "You’re pretty good, I think this is the first time I’ve heard you play."

hide YBummed
show YIrate

y "P-p-pretty good? Ugh, I have to tr-ry harder."

hide YIrate

menu:
    "Your playing is fine":
        $ yRep += 1

        show YIrate2

        y "Fine isn’t good e-enough, I need to master every instrument if I’m ever to rise above pedestrian talent."
        y "‘Fine’ doesn’t earn co-ontracts or benefactors."

        n "I thought you were a composer."
        n "I get that you don’t like people, but I’m pretty sure directing musicians is part of the job description."

        hide YIrate2
        show YEyeroll

        y "I can’t use other m-musicians, it’s part of the rules."

        n "Rules?"

        hide YEyeroll
        show YBlush

        y "I must write and perform a sere-serenade using every instrument, a-alone."
        y "Only then can I prove my m-mastery of the art."

        n "Sounds like a fool’s errand to me. Whoever told you that just wanted to keep you busy."

        hide YBlush
        show YBashful

        y "You’re probably right. No m-matter, I am a man of my word."
        y "Besides, once I achieve the impossible, people will be b-breaking down my door with job offers. I should invest in a business address."

        "More power to him I guess."

        hide YBashful
    "Does it matter?":
        $ Intel += 1

        show YTalk

        n "As long as you enjoy playing, that’s all that should matter, right?"

        y "I suppose, were I playing recreationally. I don’t p-practice seven hours a day to sound p-pretty good."

        n "You have to be exaggerating, when do you sleep."

        hide YTalk
        show YEyeroll

        y "Including weekends the nu-umbers added up. I’m not so careless as to negl-l-lect needs, unlike some people."

        n "Still, that seems a little excessive."

        y "It’s a necessity if you want to survive. Talent and joy doesn’t breed success, persi-si-stence does."

        "I get what he’s saying. I mean, I wouldn’t be here if it wasn’t for the hours I put into studying. Even still…"

        n "The most successful are the ones who possess both. Otherwise you end up suffering and loose whatever interest you had."

        hide YEyeroll
        show YThink

        y "Are you under the impr-r-ression I ha-ate what I do?"
        y "This isn’t a hobby for m-me, it’s a car-reer. I’m serious about what I do, that’s all."
        y "Since when did d-dedication and elevated sta-a-andards equal disco-ontent."

        "Nevermind, I don’t get this guy. I’ve never spent every waking hour focused on one thing, not by choice at least."

        n "My bad, it just didn’t seem like any of it was making you happy."

        hide YThink
        show YIrate2

        y "Is that so? Hmm… You’ve giv-ven me so-omething to think about."

        hide YIrate2

    "I'm not easily impressed":
        $ yRep -= 1

        show YIrate2

        y "I’m not trying to imp-press you!"

        n "Ooh, do I know him?"

        y "I’m not trying to imp-press a g-g-guy!"

        n "Your haircut says otherwise."

        "No witty comeback to that one I see."

        hide YIrate2
        show YThink

        y "She isn’t h-here right now, but I had hoped she would be."

        "That’s why he was so excited when I first showed up."

        y "Her proficiency was medio-ocre at best when we were children. It wouldn’t surprise me if she wasn’t a-allowed in."

        n "Do you have anyway of getting in touch with this girl?"

        y "Not since we were fitted with your obedience collars. Even if I c.could, she wouldn’t want to ta.alk to me. Not yet."

        "There might not be anyone to talk to if she was in the army."

        n "Uh, yeah, good luck with that."

        hide YThink

$ Intel += 1
$ yTurn += 1

show YBase

"He finished packing up his stuff with a sigh."

y "Why are y-you here?"

n "You’ve already asked me that."

y "Yes, and you dodged the question l-l-last time. I want to know."
y "Why would you, a famed villain of sorts, be wa-andering around school like nothing happened? It doesn’t m-make sense."

n "You don’t seem to have a problem talking to me. I mean, yeah I get the stigma, but just because I did bad things doesn’t make me an asshole, or a bad person."

hide YBase
show YIrate

y "So you’re just here b-because you can be?"

n "Is that a crime?"

y "N.no, but it’s certainly disappointing."

"I don’t know what this guy expects of me."

hide YIrate
return

label Yoku2:
    scene backgroundcourtyard

    "I should have known coming here was a mistake."
    "Granted, I wasn’t given a choice, but that’s besides the point. I’m pretty sure the penitentiary wouldn’t be blasting wonky classical music at all hours."

    show YIrate

    n "Three in the morning, doesn’t this guy ever stop?"

    "I storm down to the courtyard to give him a piece of my mind."

    y "Do y-you mind? I’m trying to practice."

    n "At three in the morning?!"

    y "It’s S-saturday."

    n "I don’t care if it’s Mozart’s Birthday! It’s too early for this! Go to bed."

    hide YIrate
    show YEyeroll

    y "Gladly, as soon as they change my room a-assignment. My neighbor apparently has night terrors."
    y "I don’t do well with s-sudden screams in the night, though that’s not why you ca-ame to talk to me."

    n "Night terrors…"

    y "You know, that an-n-noying thing when someone can’t tell the difference between dreams and reality, often involves sc-creaming."

    n "I know what night terrors are, and it’s usually a stress response. Do you know what they were screaming about?"

    hide YEyeroll
    show YBummed
    
    y "Most of it was unintelligible. I’m surp-prised you care."

    n "Yeah, well, it seems like I’ve been surprising you a lot lately. It’s still early in the year, if you give it time, the night terrors might resolve in a few days."
    n "New environments sometimes trigger them."

    y "I hope you’re right. I can’t keep changing r-rooms every other n-night."

    n "Every other night?"

    y "I’m used to certain co-omforts. Adjusting has been d-difficult."

    hide YBummed

    menu:
        "What are you used too?":
            $ yRep += 1

            show YThink
        
            y "I was brought into this world for the sole purpose of crossbreeding my-y abilities with a higher ranking Proficiency User to create the most a-accomplished and influential musician."
            y "As long as I did what I was s-supposed to, my parents left me a-alone."

            "How can he talk about this so casually."

            hide YThink
            show YTired

            y "You seem surprised. Wasn’t it the same for you?"
            y "Professor Tesuta was a product of s-selective breeding as well. They talked so highly of you, I just a-assumed."

            n "No, I was a lab rat for Estella’s research facility. They hovered over me all the time. I felt like I was in a zoo."
            n "Didn’t matter though, they still didn’t get the results they wanted."

            hide YTired
            show YTalk

            y "I see. That’s why you were never present for the ba-anquets, you were being marketed with false a-advertising."

            n "Hey!"

            hide YTalk
            show YBummed

            y "You didn’t miss much. It was a g-glorified auction at best."
            y "Though, if you’d gone, maybe people would have stopped s-suggesting I was ‘lucky’ to attend."
            y "You seem like b-bottom rung material to me."

            n "Are you listening to yourself? It’s talk like this that fueled Estella’s corruption."

            y "True. I sup-p-pose old habits die hard."

            "So Yoku stuck in one of those Proficiency mills. That could have very easily been me."

            hide YBummed

        "Suck it up":
            $ yRep -= 1

            show YIrate

            n "All I ever hear you do is complain, but you never do anything about it. So people rub you the wrong way, who cares? Grow up and stop acting like a spoiled brat."

            y "I’m not the one who la-aunched an entire city into chaos because my parents didn’t love me."
            y "I put up with being livestock just like my p-peers, you’re the one who couldn’t handle it."

            n "You take that back!"

            hide YIrate
            show YIrate2

            y "I’m sorry, did I hurt your feelings? What are you g-going to do, kill me so you’ll feel better about yourself?"
            y "I may not t-tolerate the general public, but at l-least I value their lives."

            n "You don’t know anything about me."

            y "Then stop a-acting like we’re friends and leave me alone. I owe you no courtesy."

            "He pulled out his instrument."

            hide YIrate2
            show YBase

            y "“I suggest you inv-vest in a pair of ear plugs, otherw-wise it will be a long night."

            n "If you don’t give a shit about me, fine, but you’ll be waking everyone else up if you play."

            "He lowered his bow with a glare."

            hide YBase

        "Adjusting is difficult for everyone":
            $ Intel += 1

            show YSad

            n "A lot of people just came out of war torn areas. I know you like to blame me for it, but things wouldn’t be this way if I had a say in things."

            y "You may have seen it, but exp-periencing it was another thing entirely."
            y "Even the DVP doesn’t understand what it’s like to have your f-free will taken from you."

            n "What are you talking about?"

            y "The Eclipse Collar, it r-robbed you of your senses. It used music to drown out the screams. My o-old neighbor can’t stand to hear it now."

            "I never programmed it to do that."

            hide YSad
            show YBummed

            y "More than any haunting m-melody, I fear silence."
            y "Even if no one wants to hear me play a-anymore, I will continue to practice."

            n "If that’s the case, maybe practicing in the middle of the night isn’t the best thing."

            hide YBummed
    $ yTurn += 1
    $ Intel += 1

    show YBase

    y "Were things the way they were sup-p-posed to be, I wouldn’t be staying in the dorms at all. My grandparents’ home was once in the a-area."

    n "This place may not be an estate, but it’s better than it could be."

    "I remembered Hiro's story about living in the shared rooms in the foster home. It still kinda bugs me."

    hide YBase
    show YIrate

    y "It wasn’t an est-tate. It was some townhome. I doubt it’s on the list for renovation."

    "He sighed. "

    y "Now’s not the time to be getting s-sentimental. It’s late, I need to get some s-sleep."

    n "Not worried about the night terrors next door?"

    y "If you start screaming again, I’ll just b-bang on your wall to wake you up."

    hide YIrate

    return
label Yoku3:
    scene backgroundamp

    show YBase

    "Last time I talked to him, Yoku mentioned that his grandparents weren’t well off, but I’m certain he was a part of those uppercrust Proficiency mills. I wonder how he ended up there."

    y "C-can I help you?"

    n "Hunh?"

    y "You came over here and have been st-staring at me for a few good minutes"

    n "Sorry, that happens sometimes."

    y "Did you want something or n-not?"

    n "You’ve mentioned before being a part of the societal banquets, I was wondering what that was like."

    hide YBase
    show YDaydream

    y "I sup-p-posed I could entertain your curiosity for a minute."
    y "To sum-m-marize, it was a bimonthly showcase where up-p-per class folks would go to pat each other on the backs."
   
    hide YDaydream
    show YBummed
   
    y "There was a lot of pressure to schmooze senior members in hopes of m-marrying into a higher ring within the club."
    y "The b-best way being to brag about your accomp-plishments."

    "Gross. No wonder this guy talks about himself all the time."

    y "If they would listen to you at all, the e-easiest way to reach them was through their children. I started going when I was fi-ive for that very reason."

    hide YBummed

    menu:
        "Because you weren't accomplished":
            $ yRep -= 1

            show YIrate
            
            n "You hadn’t done anything, so you had to cozy up to the big-wigs the backway."

            y "What five year old’s done a-anything noteworthy? Don’t go making baseless assumptions."

            n "True, but your parents didn’t think you’d do anything, did they? You’re an intelligence major, aren’t you?"
            n "That means your Proficiency probably didn’t surface until school, around the same time they made you go.”"

            "I started laughing, I couldn’t help it, picturing some snob disappointed that all their kid could do was hear well."

            hide YIrate
            show YBummed

            y "That’s not… status was based on bl-l-loodline more than skill."
            y "I was at a disadvantage! That isn’t the reason at all. You’re twisting my words."

            n "Right, whatever you say."

            "It’s obvious I’ve hit close to the mark. Or at least, he’s afraid I have."

            hide YBummed
        "Because it was traditional":
            $ yRep += 1

            show YBummed

            y "Well, yes and no. My family was c-considered fresh blood."
            y "We didn’t have strong ties in the c-community yet. I was barely considered third g-generation, but the practice was expected."

            "I think my head’s spinning. This is a lot to take in at once."

            n "I can’t believe people would do stuff like this to their kids."

            hide YBummed
            show YEyeroll

            y "A family’s l-legacy can outweigh the individual in many homes. Quite a few of my old ‘friends’ were the children of tycoons or p-politicians."

            n "Do you really think that?"

            hide YEyeroll
            show YTired

            y "...No. It sounds u-utterly ridiculous. For people who clung so d-desperately to the future, they were s-surprisingly short sided."
            y "All they left behind were arbitrary rules."

            "At least he has some sense in him."

            n "I wouldn’t know the difference. My parents were not big on ‘family values’. They didn’t even do enough to rank at mediocre."
            n "This whole dynasty thing is so alien to me, it sounds like a giant pain."

            hide YTired
            show YTalk

            y "I don’t imagine you wo-ould have enjoyed it, n-n-o."

            hide YTalk
        "To find a girl to marry up":
            $ Intel += 1

            show YEyeroll

            y "Excuse me?"

            n "That’s how it worked right? Weren’t you all upper class and junk?"

            hide YEyeroll
            show YIrate

            y "Well technically speaking yes, but in that small of a pond a single d-demerit could ruin your c-comparable value."

            n "Demerit?"

            y "One’s worth as a potential partner was carefully calculated; me-easured by achievements or demerits."

            n "You’re getting a little too technical on me."

            y "Sorry. Let’s just say my per-erceived worth wasn’t ‘good’. I had a lot to prove, so the s-sooner I started, the better."

            n "That’s so messed up. A kid shouldn’t have to prove their worth."
            n "Learning how to take care of yourself is enough without piling other crap on."

            hide YIrate
            show YSad

            y "Quite. Though, I’ll admit it’s nice to hear you assumed differently."

            n "I’ve heard what you can do. If you just figure out how to market your work right, you’ll be leagues ahead of those trust fund babies."
            n "The only one who remembers what those people thought of you, is you."

            y "It’s true. I had hoped school here would be a fre-esh start for me."

            hide YSad
    $ yTurn += 1
    $ Intel += 1

    show YBummed
    
    y "My parents dreamed that the Y-Y-Yoku name would go down in music history under a legendary composer."
    y "They shared with me their love of music and their dreams. On.nly, they didn’t intend for me to be that c-composer."
    y "I was viewed as a stepping stone toward that goal." 

    n "Then why are you bothering with all the instruments and commissions? Isn’t that the golden ticket to do whatever you want?"

    hide YBully
    show YTalk

    y "I wa-ant to do this. Granted, the terms are a little extreme and I’m expected to fail, but that alone doesn’t m-mean I shouldn’t try."

    n "But I mean, what would you get out of it? It just seems like a giant waste of time."

    hide YTalk
    show YDaydream

    y "I get to do what I love. I get to spend ev-veryday bringing something into existence that’s never b-been done before."

    "I’ve never seen him speak with such passion before. Well, about something positive, that is."
    
    hide YDaydream
    show YBase

    y "I came here because it w-would bring me closer to my goal, regardless of the risks…"
    y "Why are you here?"

    "This again."

    n "I already told you, I-"

    "I… I don’t think I’ve actually thought about it. I mean, technically I’m forced to be here, but I can’t tell him that. "
    
    n "I.."

    hide YBase
    show YSad

    y "Still no answer of your o-own."
    y "That kind of lazy thi-inking will get you nowhere."

    n "Hey!"

    y "Whenever you fi-igure out the answer, let me know."

    hide YSad

    return

label Yoku4:

    scene backgroundpond

    "After our last talk I hadn’t expected Yoku to reach out to me of his own volition."
    "He said he wanted to talk to me about something, but he’s just been kinda staring at me intently. I feel like prey."

    show YBase

    y "You’re a person…"

    n "Yes, have been my whole life."

    hide YBase
    show YTalk

    y "So you know what p-people would like…"

    n "I’d like to believe I have a loose understanding of the trends, yes."

    hide YTalk
    show YThink

    y "And girls a-are people…"

    "Oh, I don’t like where this is going."

    n "I’m not going to pretend that I know what every woman in the universe wants."

    hide YThink
    show YBase

    y "But we agree th-that girls are people."

    n "Just get to the point."

    y "......."

    "He handed me a pair of headphones."

    y "Just li-isten."

    hide YBase
    
    scene backgroundYPath

    "He fumbled with the controls and soon followed the sound of a violin accompanied by a piano. It was a strange duet. A little tinny, but good. He was staring me down as I listened."

    y "So…"

    n "Well, it’s definitely a song. Not really my genre of choice."

    y "Then how do I fi.-ix it?"

    n "Fix it? Wait, did you write this?"

    y "I keep trying to add stuff, and it’s not w-working. I just can’t put my finger on what I need to do to fix it."

    menu:
        "I don't know, bass?":
            $ Intel += 1

            n "Everything’s better with a killer bass line."

            y "I’m not doing a launch pad remix, I’m writing a so-onnet. It’s supposed to be moving and emo-otional."

            n "Look dude, I already told you this isn’t my genre of choice. If you want an essay on how awesome Darkwave is, I’m your guy, but I’m not sure what to do with this."

            y "Some h-help you are."

            n "I never claimed to be a music authority or anything. Have you tried talking to the music teacher?"

            y "I guess I could. It’s just frustrating. This is the only thing I kn-now how to do, and I can’t. I c-can’t do it."

            n "I’m telling you, more bass. Everything is better bass boosted."

            y "Really, Beethoven’s 5th is b-better bass boosted?"

            n "I know you’re being sarcastic, but it’s literally the first thing that pops up when I search “bass boosted classical”. Followed by ‘Mozart and Rise of the Valkyries’."

            y "That d-doesn’t make it better."

        "Writing is rewriting":
            $ yRep += 1

            n "If this isn’t working out, then write something else."

            y "So you want me to ju-unk everything."

            n "Not necessarily, but if you start over clean it might give you a fresh perspective."
            n "My friend Jona is a creative type, and that’s what he usually does."
            n "He’ll make the same invention three, four times before he finds out what about the idea appeals to him and perfects it."
            n "If doing that seems like a chore, then it’s probably best to junk the whole thing."

            y "I see… Perhaps I am overth-thinking things."

            n "You keep practicing the violin, but maybe you should try writing with the instrument you’re the most comfortable performing with."
            n "Then compose from there. Or, I don’t know, anything that will make it more sincere."
            n "You want this to stir emotion in someone, right?"

            y "Yes, more than a-anything. This has to be able to speak for me."

        "More cowbell":
            $ yRep -= 1

            y "......?"

            n "I’ve got a fever-"

            y "No."

            n "And the only cure-"

            y "I just w-wanted advice."

            n "Is more cowbell!"

            y "Would you take this s-seriously!?"

            n "I am being serious. Throw in some percussion to spice things up."
            n "Listening to it just makes me all sad and nostalgic. It’s weird."

            y "That’s what it’s su-upposed to do."

            n "Oh… then don’t change anything, it’s fine."

            y "I mean, I was going for more so-omething more saudade with hopeful overtones, but sad and nost-stalgic is a good place to start."

            n "It’s just a song."

            y "It’s not… I mean, it is. Someone like you w-wouldn’t understand."
    $ yTurn += 1
    $ Intel += 1

    scene backgroundpond

    show YTired

    y "I try incredibly ha-ard to come off as el-l-loquent and refined, but I’m still the same stuttering child I was before this all started."
    y "Co-oming here hasn’t changed anything."

    n "Well, no, it’s not going to. No one can make you do anything regardless of how good their intentions are."
    n "There isn’t some great solution or cure all that saves you from being you, but that’s okay."

    hide YTired
    show YIrate

    y "Of course you w-would think that."

    n "Being okay with who you are isn’t a bad thing."
    n "In fact, you’ll never be able to make any progress until you find at least one thing about yourself that’s worth protecting."
    n "Figure out what that is, and then you can work on trying to change the things that you hate."

    hide YIrate
    show YSad

    y "I can’t cha-ange the way I talk, or the way people see me."

    n "Yeah, no, that’s not what I meant. Like… you keep talking about being a great musician and junk, but what is it ultimately for?"
    n "What are you trying to do?"

    y "I just want to sup-p-port myself and the people I care ab-bout while doing the thing I lo.ove to do."

    n "Exactly, that’s what most people want. You’re lucky enough that you know who those people are and what you love doing."
    n "Most people can’t even get that far. You’re getting too caught up on the details."
    n "As long as what you’re doing moves you towards that goal, you’ll be fine."

    hide YSad
    show YBase

    y "Are you one of those p-people; the type that doesn’t know what they wa-ant?"

    n "I mean… yeah. I just want to be happy. Which is bland I know, I just don’t know what to do to get there."
    n "I thought Guwon was the key to that, but that didn’t make things any better, it just made things different."
    n "After the year is over, I don’t know what I’m going to do."

    hide YBase
    show YDaydream

    y "Then you do have a g-goal. Even if it’s small, y-you have a purpose."
    
    n "Yeah… Yeah, you’re right!"

    hide YDaydream
    show YBase

    y "I always thought you were far more… ca-alculating then you seem."

    n "Hey I am calculating, I just don’t have a formula that works for me yet. I’m working on it."

    "He nodded, seemingly in deep thought."

    hide YBase
    show YJoy

    y "It seems I have misju-udged your potential as an ally. I will not do the same a sec-cond time."

    "Hunh?"

    y "You’ve been pushing to become stu-udent council president, have you not? Should you be serious about this endeav-vor, you have my unw-wavering support."
    y "I look fo-orward to speaking with you at ano-other time."

    hide YJoy

    "Wow"
    "Just… I’m not sure how to feel."
    "Having someone like that in my corner would definitely benefit me in the future."
    "Provided he’s able to actually market himself as a musician. I gotta make sure that dork doesn’t get himself into trouble."
    return
label YokuF:
    scene backgroundcourtyard

    show YSad

    y "Sorry Nagen, my next piece isn't finished yet."

    hide YSad
    
    return