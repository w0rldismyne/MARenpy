#[Rise is available during mornings after class]
label RiseVisit:

    if rTurn == 0:
        jump Rise1
    elif rTurn == 1:
        jump Rise2
    elif rTurn == 2:
        jump Rise3
    elif rTurn == 3:
        jump Rise4
    else:
        jump Rise5

label Rise1:
    scene backgroundpond
    "Birds are singing in the trees. The rickety dock that looks out over the electrical wire infested waters looks significantly more elegant with a table setting on it."
    "A plastic foldable table has been decorated with a hand embroidered tablecloth and fresh flowers, flanked by iron deck chairs."
    "Rise wipes the sweat from her brow as she admires her handy work."
    show rise smile
    r "Nagen! To what do I owe the pleasure?" 
    n "I was looking for you, actually."
    show rise smug
    r "For business or pleasure? I understand school has been a bit bothersome for you as of late, but I had hoped to enjoy the last bits of morning."
    r "Look at this place; you can almost forget we are at a school." 
    n "Uhh, I was going to see if you wanted to hang out."
    r "Splendid! As long as I have a view of the water, I will be content." 
    "She had spent the first day of school shrewdly watching people from the window. Now that there's students using the student council room, she's lost her perch."
    "Perhaps it was the grounds she'd actually been watching, but even now it seems like she's observing me."
    show rise scheme
    r "There are so many things I would like to ask you, but I fear coming off as crass. Would you mind humoring me for a bit?" 
    "I guess I shouldn't be surprised people at school would want to know just as much as the lawyers of my case."
    "That said, I can't risk saying the wrong thing. Who knows what she'll tell people?"
    n "I'll answer to the best of my ability."
    show rise smile
    r "How funny. There is no need to look so serious. I was simply curious as to why this is the first time we have crossed paths."
    r "Your father was quite accomplished in making pharmaceuticals and my father funded his research. Yet, I never saw you at any of the upper ring's gatherings."
    hide rise
    menu:
        "I was sick":
            $rRep -= 1
            show rise mad
            "Usually when I missed out on stuff, I was busy being my dad's lab rat. I went with the same excuse I always did."
            r "For all of them?" 
            n "Probably."
            r "You have an iron clad memory. Were I to give you the exact dates, could you tell me what you were sick with?"
            r "Or would that be too many lies to keep track of?"
            n "I'm not-"
            show rise disappointed
            r "I told you, my father funded the research you were involved with. I know the difference between 'sick' and 'preoccupied'. If you would rather not discuss it, just tell me. I despise lying." (8)
            "I might as well have been a rat sitting at the table."
            hide rise
        "My mom wouldn't let me.":
            $rRep += 1
            show rise frown
            r "Your mother? Her family was the only reason you had an invitation. Whyever would she turn it down?" 
            n "I don't know, she never really talked to me. She probably didn't think I'd be a good fit or that I would be an embarrassment."
            n "I did just transfer to the 'problem kids' class when I would have been old enough."
            show rise frown
            r "Is that what they told you? I had been attending since I was five. They must have deliberately been keeping you out of sight."
            r "It is not like you would have needed them to be there in order to go." 
            n "I still don't know how to drive. There'd be no way it would cross my mind to go anywhere without them."
            show rise mad
            r "Yes, and making friends more powerful than them could be seen as a problem in their eyes."
            "Her words hit like an icepick to the gut. I've always felt this way, but I've never had someone put it into words so plainly."
            "Not since Lethe. She takes my silence as confirmation."
            r "I imagine that was the case, as it is the exact opposite of my father's advice to me. The opposite of independent being, well, dependent."
            r "They isolated you on purpose." 
            hide rise
        "I don't know what you're talking about.":
            show rise talk
            r "Which part?" 
            n "The gatherings. What the hell are those?"
            show rise smug
            r "Hmm, how do I put it tactfully while still being clear?"
            show rise flirt
            r "When two rich families love each other's status very much, they will strongly encourage their children to get closer."
            r "The upper and lower rings would gather annually, and often in smaller groups often as well. I would know; I attended all of them."
            n "Sounds exhausting."
            show rise
            r "It was, but I made my own fun. I am rather fond of the grey hairs I gave my father talking to anyone that seemed interesting."
            r "Your name came up, of course, as someone who was always absent."
            n "Well, now that I know what they are, I wouldn't want to go."
            hide rise
    show rise frown
    r "How unfortunate. See, being at the top of the social ladder, there was nowhere but down for me to go."
    r "My parents were so terrified I would tarnish their reputation by marrying the wrong person, and yet here we are."
    n "You don't like your parents?"
    show rise surprised
    r "I-"
    "She thinks for a moment."
    show rise frown
    r "The love I hold for them is complicated, and I am sure there are some that think I should despise them."
    r "That is something I cannot force myself to do, despite all evidence."
    r "I find it funny that the world sees me as being at the bottom of the social ladder, watching my fortune get squandered by vultures."
    show rise mad
    r "After all, what would I do with money? I am just a child." 
    n "Your parents didn't have any rich friends you could go to?"
    r "The only thing my parents had were competitors and me. So, I have decided to throw caution to the wind, and go with my second choice for independence." 
    n "And what would that be?"
    show rise hearts
    r "You shall be my fiance." 
    "HA! What year is it? Wait, she's not laughing. She can't be serious, no one seriously gets engaged in highschool. We aren't even dating. I barely know her!"
    n "I shall not."
    show rise talk
    r "Odd. Usually that works." 
    "What does that mean?!"
    show rise smug
    r "It seems you need time to get used to the idea. Sew wild oats and what not."
    r "Whenever you are ready, feel free to find me and we shall try this again." 
    "Umm, excuse me?! The wind picks up, and all Rise cares about is rescuing her tea set from getting swept up with the table. My objections fall on deaf ears."
    hide rise
    pass

label Rise2:
    scene backgroundcafex
    "A lot of the girls have been giggling at me. It seems word of Rise's unasked for engagement has already traveled through the school."
    "If I thought it was because she actually liked me, it'd be another story, but I get the feeling I'm being used."
    show rise hearts talk
    r "Darling!"
    "And bribed."
    r "Have you had breakfast yet?"
    "She has a not so conspicuous basket behind her. It's sort of eerie how quickly she's identified when I get up in the morning."
    show rise flirt
    r "I can eat by myself if I am being a bother, but I thought it would be nice to chat over a meal."
    n "Sure."
    "Maybe I'll finally be able to clear this mess up. She sets up her picnic basket on one of the outdoor tables, where everyone can see."
    show rise talk
    r "I realize in hindsight that I was never clear about what I had to offer."
    r "Forgive me for my brazenness earlier. I forgot that despite all my parents' marketing, you were never there to see it."
    r "Asking you to take me at my word was presumptuous of me. I apologize."
    "Oh?"
    "Oh! Sweet, I don't have to do anything."
    "Someone else probably made fun of her and she's just been taking things in stride. Well, I'll accept an apology breakfast."
    n "What do you mean marketing?"
    show rise frown
    r "You never found it odd that green eyed models became popular once my mother took over the cosmetics industry?"
    r "What about the hair dye commercials? The beauty standards of Guwon were being sculpted after my appearance for a reason."
    show rise smug
    r "I'm the only one to come by it naturally." 
    "I doubt that will be the case moving forward. She seems to think the same thing too, a defeated sigh making its way out before she can cover it."
    show rise
    r "I have been rather diligent in Ms. Sato's class if I do say so myself. I have no doubt I can regain my previous status if I talk to the right people."
    r "The quicker I reestablish myself, the better. There are some, dare I say, bastards that will not take me seriously regardless of how old I am."
    r "That is why I need someone like you."
    n "So you admit it doesn't have to be me. You have plenty of time to, y'know, actually date people like a normal person."
    show rise smug
    r "Yes, well, I had a feeling you would be the easiest to negotiate with. Though, I guess it depends on what it is you want after leaving this fish bowl."
    hide rise
    menu:
        "Power":
            show rise mad
            "My goals haven't changed since coming here. I first need to get a foothold within the student body."
            "Rise could help with that in some ways, but at what cost?"
            n "I'm more interested in doing things on my own. If I can just get people to listen to me, then I can do whatever I want."
            n "I have to be too powerful to mess with."
            r "Well there is your first mistake; no one is self made. Look behind your heroes and you will find generational wealth and friends in the right places." 
            r "If it is the approval of the masses you are after, then I can teach you the rules of upper society no one bothered to."
            hide rise
        "Money":
            $ rRep -= 1
            show rise disappointed
            n "Maimai got me an in with some rich software engineer. If I don't piss him off, I'll be set for life."
            r "Is that all?" 
            n "What do you mean?"
            show rise talk
            r "You have no way of knowing how long 'for life' is. If money is all you are after, there will never be a sum large enough to make you feel secure."
            r "It is an arbitrary, endless goal. A means to an end. Do you have no further aspirations?"
            "None that I want to share with you."
            n "Not at the moment."
            show rise disappointed
            r "Well, I assure you, wealth is in my future if that is all you want."
            hide rise
        "Family":
            $ rRep += 1
            show rise talk
            r "Forgive me, but I was under the impression your parents passed away."
            n "Oh, yeah, I didn't mean them. Uitto, Jona and Hiro; they were the ones I was thinking of."
            n "None of us had that great of a place to go back to, so we promised to stick together."
            n "Even getting me to be student council president. I can tell they don't really get it, but they've been trying to help me anyway."
            "Maimai too, but being away from her for so long, it's hard to tell what she's really thinking."
            "I've been trying not to think about what I'll be coming back to too much."
            show rise surprised
            r "I see. Perhaps that is what I am drawn to. I also value family dearly, but mine is well..."
            show rise disappointed
            r "I never tried to make one of my own before, and it terrifies me how lost I have felt since coming here."
            r "What I can say is, I desperately want a place to belong to as well."
            hide rise
    show rise frown
    r "What do you think about the food?"
    n "It's fine."
    show rise hearts
    r "Excellent, then we can add that to the list of things you get to look forward to as my husband."
    "This wasn't apology food; it was a bribe, I should have gone with my gut."
    n "It's not that I don't like you-"
    show rise hearts talk
    r "Of course. I also do not dislike you. That is why it would be a good match."
    n "We don't really know each other."
    show rise 
    r "Naturally, that happens with time."
    n "Which is why I, again, don't want to be engaged to you."
    show rise frown
    r "I see. Is this because I went about it the wrong way?"
    n "Exactly! I mean, how many other girls have been running around looking for husbands?"
    "Though, now that I think about it, that might be good to know."
    show rise talk
    r "No one. I just thought I was being a go-getter. It makes sense applying upper ring rules to ordinary people would not work."
    r "It never occurred to me that I was doing something wrong."
    n "I mean, wrong is a strong word. Insensitive maybe? Like, I didn't get a say in anything before you decided we were engaged."
    show rise disappointed
    r "Well, I have egg on my face then."
    n "Yes. I mean, yeah it's a little embarrassing, but you also literally have egg on your face."
    "I point on my chin and she quickly brushes it off. Red as a beet, she buries her head in her arms. All things considered, I think that went pretty well."
    hide rise
    pass

label Rise3:
    scene backgroundhall1
    show rise talk
    r "Nagen, do you have a moment?" 
    "I am painfully available, so I agree to follow her somewhere a little more private to talk."
    hide rise
    scene backgroundcourtyard
    show rise disappointed
    r "I wanted to properly apologize for my behavior from before."
    r "I severely underestimated how universal the manners I grew up with were and I put you in an uncomfortable position."
    n "It's fine."
    "Certainly not the worst thing to have happened since coming to school."
    show rise surprised
    r "I had talked with several of the girls here, and they informed me as kindly as they could that I fumbled courtship from the very first step."
    show rise frown
    r "I will not do so a second time."
    "Wait a minute, why is she telling me this?"
    show rise hearts
    r "You have my permission to ask me on a date."
    "Damn it, what did they tell her? She seems so proud of herself too. How the hell do I get her to let this idea go?"
    hide rise
    menu:
        "I knew that.":
            $rRep += 1
            show rise surprised
            n "The problem isn't that you didn't let me ask you out, it's that you assumed I wanted to in the first place."
            r "But you kept talking to me."
            n "Yeah, so I could be your friend, but you're making it impossible to be even that."
            show rise talk
            r "Friends are such temporary things, Nagen. Once we leave this place, do you seriously think anyone here will stay in touch?"
            r "Marriage is the only relationship enforced by a contract. It takes so much more trust, why-"
            "Maybe if I put it in a way she understands."
            n "I have no idea how long it would take for me to trust someone enough to put myself in that position to begin with."
            n "I'm still kinda working on how to have friends."
            show rise hearts talk
            r "I thought I could be the exception."
            hide rise
        "I'm dating someone else.":
            $rRep -= 1
            show rise mad
            r "Then why are you talking to me?"
            n "I just want to be friends."
            r "Nagen, I have been nothing but forthcoming about how I was courting you for marriage."
            r "How could you approach me while someone else's heart is in your hands? That is cruel not only to them, but to me as well."
            r "Have you no sense of loyalty?"
            n "I've turned you down every time! I'm turning you down right now. I want to be able to talk to you like a normal human being."
            hide rise
        "I've already said no.":
            show rise hearts
            r "Yes, but-" 
            n "No, no buts. I said no. I don't want to be engaged, or pre-engaged, or whatever the girls told you."
            n "You keep making these decisions without asking me what I think."
            show rise frown
            r "How do I do that? You have not told me what you think, you have just been telling me no. I have been guessing at the reason-" 
            n "Alright, instead of guessing, try asking what I want to do."
            show rise surprised
            r "Oh, um... Do you want to get married?" 
            n "In highschool? Hell no."
            hide rise
    show rise surprised
    r "I'm bad at this, aren't I?" 
    "I've been trying to be nice, but maybe a blunt dose of reality would do her some good."
    n "Yeah, you can't just force someone to like you like that."
    show rise frown
    r "I'm supposed to be able to. That was my Proficiency."
    "Well, crap, I'm definitely not immune to Charm abilities. Uitto manages to talk me into all kinds of things I don't want to do."
    "If Rise can't use her power like she used to- She's like, really crying now."
    show rise mad
    r "Nagen, this was what I was raised to do, and I'm bad at it! Not even average, bad."
    "I help her sit down. She tries to breathe, but can't. Then, reaching around her side, unzips her corset to free herself from the shape she forced her body to take."
    "I know back in Guwon you'd get kicked out of the program if you lost your Proficiency."
    n "I won't tell anyone."
    "Her tears make large, dark spots on her skirt."
    n "You can tell people you changed your mind, or that you didn't actually want me and that's why your ability didn't work. Nothing bad is going to happen."
    show rise surprised
    r "I don't know what I'm going to do."
    n "Well, that's kinda where we're all at right now." 
    "Honestly, I think Mr. Yaguichi would be able to help her more than I can."
    "I probably wait a little too long to leave, but it's hard to tell when the least awkward time to leave someone crying after getting rejected is."
    "I hope she's okay."
    hide rise
    pass
label Rise4:
    scene backgroundpond
    show rise frown
    "I find Rise sipping her tea as usual. I can't say I've ever rejected a girl before, but the last few classes with her have been weird."
    "It's like she wants to talk to me, but is afraid to. I want to make sure she's okay."
    n "Um, hey."
    "She sets down her cup and looks at me, a small smile on her face."
    show rise talk
    r "Why, hello."
    r "Is someone forcing you to talk to me? You seem apprehensive."
    n "No, I just wanted to see if you were free."
    show rise frown
    r "That I am, at least for the time being. I did what you said and wept in Mr.Yaguichi's office over how worried I was about the mismanagement of my family's business."
    r "He did not understand why I was so anxious and suggested I join the Intel course."
    r "He suspects I could have a Proficiency in finance or management."
    hide rise
    menu:
        "You don't seem happy.":
            show rise disappointed
            r "I wish I had a memory like yours, because I was always told I was not good at anything else. Now I wonder if I was ever sincerely tested." 
            n "There are so many Intelligence Proficiencies. If you were never given the right test, it's possible they never knew either."
            r "Yes, an honest mistake. That must have been it. No one sees a five year old and thinks of a budding entrepreneur." 
            "There could have been signs. I guess it depends on how involved her parents were."
            hide rise
        "That's great.":
            $rRep += 1
            show rise surprised
            r "You really think so?" 
            n "I mean, that's why you were freaking out, right? Now there's no way you'll get kicked out."
            "As a means of seduction, her methods were terrifying. As sales' tactics, they were perfect."
            n "You must have been miscategorized because you treat everything like a business venture. I'm sure you'd pass an appeal exam with flying colors."
            show rise
            r "You know, I think this is the first time you have encouraged me to do something."
            "She laughs."
            r "I really appreciate it."
            hide rise
        "I doubt that.":
            $rRep -= 1
            show rise mad
            r "Exactly. My parents would have known if I had what it took to be an Intel Major. I mean, how would lying about how smart I was benefit them?"
            "A few ideas come to mind, and I don't like any of them."
            n "No, I mean- I don't think you're that bad at the whole being the prettiest girl in school thing."
            show rise frown
            r "I already told you, my 'beauty' is fake. It just seems I am unable to maintain the ruse on my own."
            "I don't think I'll ever get her to listen to me. She'll just keep hearing what she wants to hear."
            hide rise
    show rise frown
    r "Not many people know this, but when applying for my Proficiency, my parents cited my charms as a reason they stayed together."
    r "In fact, they constantly reminded me of that. I figured my love would be enough to hold us together as well."
    n "You can't love me. We haven't even been in school for a month."
    show rise talk
    r "You are right. The version of you I held onto was a childish fantasy."
    r "I had been aware of your existence from a young age, and you were one of the few candidates both my parents had picked out for me."
    r "The idea that after everything that had happened, we had found each other again was romantic to me."
    n "They already had marriage candidates picked out for you?"
    show rise disappointed
    r "Yes. Each had their own lists of course, but I was torn between making both of them happy by marrying a stranger or ruining them by marrying someone they both disapproved of."
    r "I took too long making that decision."
    n "Did my parents know about this?"
    "I feel like I would have known if they were making plans to auction me off before graduation."
    show rise surprised
    r "You know, now that you mention it, the profile was suspiciously missing a photograph."
    "Oh my god. They didn't know either."
    show rise talk
    r "Your mother was from the upper ring, so it was only natural for you to be a viable candidate. Picture yourself two years ago; what would you have said?"
    "Shit, I probably would have jumped on it. Say what you want about Cinderella, she knew sucking up to rich people was better than being a personal servant."
    show rise mad
    r "Careful how you answer. I would rather not get my hopes up over nothing."
    n "Considering I did start literal riots to get away from my family, I think the answer is obvious."
    show rise talk
    r "Right. I suppose there would be no reason to feel that desperation now. Unless there is something else you are trying to escape?"
    "There it is again, that horrifying feeling of being a bug under a microscope."
    n "School."
    show rise flirt
    r "That you are."
    "I think, finally, I could actually be friends with her. I don't think anyone else can quite understand what it's like to have a Proficiency forced onto them like she can."
    "I may not be ready to open up about that yet, but it's nice to understand someone like this."
    "I spent far too long worrying what would happen once my Proficiency failed me."
    hide rise
    pass
label Rise5:
    scene backgroundpond
    "It's nice to take a break from running around once and a while."
    "Rise's been attacking preparation for the dance almost as much as I have, so it's given us something superficial to talk about."
    "Anytime I broach the subject of her switching classes, she gets sad. I thought she was excited about it, but I guess it is starting over from scratch."
    if dateRise = True:
        "We're going to the dance together, but she may be forcing herself to go since we've put so much time into the event."
    else:
        "I wonder if she has friends she's going to the dance with. Now that I think about it, she's spent a lot of her time planning."
        "I haven't seen her hang out with anyone. I'm the only one that comes to her impromptu tea parties."
    "Her spread for today's tea party is needlessly extravagant. She must have been up all night working on it."
    "Before I would've anticipated her using it as a segway into why she'd be an excellent wife, but she's not even bragging about it. It's just something to do."
    "Instead of tea leaves, she lets dried flowers float in my cup with a strainer on stand by. Between the pond and the tea, all I can smell is wet grass."
    show rise talk
    r "Do you have any ideas for events after the dance?" 
    n "Not really. Holding a dance was Kietsu's idea. This whole thing has been such a headache that I haven't wanted to think about what comes next."
    show rise smile
    r "You should. Not that it will not be less stressful, but people need something to look forward to, even if it's something small."
    r "If you do not have an answer for what comes next, it could kill the momentum you have." 
    n "I don't suppose you have any ideas?"
    show rise talk
    r "Nothing that would go over with this crowd, I fear."
    "Scooping out globs of wet flowers from the cups, she adds a cap full of vanilla to each cup."
    n "Maybe we could do a drink thing. Let people have something during class?" 
    "She stirs in the milk in silence."
    show rise disappointed
    r "I was foolish for thinking I was somehow better than this place. For as much as I despise lies, I managed to tell myself a lot of them."
    n "Aw come on, we're all better than this place. That's why we get to leave it eventually. It's sucked just about as much as I thought it would."
    show rise smile
    r "Then you are far more realistic than I. As embarrassing as this may sound, spending time with you has been one of the highlights."
    r "I may be horrible at making true friends, but I consider myself in much better company now than I was."
    hide rise
    menu:
        "Who was the other guy?":
            #opens ending with Yoku AND Nagen
            show rise frown
            n "You mentioned it being between me and someone your parents hated. Who was the other guy?"
            r "Yoku. Though I am sure you have noticed he has no interest in me now that my family is utterly powerless."
            if $yRep >= 3:
                show rise surprised
                n "That's not true. He's working on some dumb song you asked him to write."
                r "Are you serious?! We were children! Playing a song with 'every instrument' is literally impossible."
                r "Why on Earth- I sincerely thought he had forgotten about that."
                n "It sounds to me like he got it into his head he needed to impress you before you would talk to him again."
                show rise talk
                r "He should hate me for sending him on a fool's errand, not try to complete it."
                n "Or, and here's a wild thought, you talk to him first. Whatever weird bullshit was keeping you from being friends is gone now."
                n "You're the only ones enforcing it now."
                show rise
                r "I will."
                hide rise
            else:
                show rise frown
                n "That guy? Really? He's a stuck up musician. Your parents weren't on board with that?"
                r "His family was considered 'new' blood. As far status goes, that would be the lowest down I could marry without ruining my reputation."
                show rise mad
                r "They did not have faith any of his children would be remotely gifted."
                n "That's supremely fucked up on so many levels."
                show rise disappointed
                r "I know. I guess I always knew, but I kept hearing everyone around me talk about it like it was normal."
                r "I have been trying to break myself of that mentality, but it has been surprisingly difficult."
                n "Well, knowing is half the battle, I guess."
                show rise smile
                r "Yes, I suppose it is."
                hide rise
        "Pick a date":
            #opens ending reuniting Yoku and Rise
            show rise talk
            r "Why?"
            n "Well, finding an excuse to talk to new people without it being awkward is hard."
            n "'A friend of mine thought this was a good idea' is always a good icebreaker. Worked for me all the time."
            show rise mad
            r "Nagen, are you suggesting you could set me up with someone?" 
            n "A someone, a friend, a whatever you want it to be. It'd be something stupid to look forward to."
            r "Like who?" 
            n "Well there's Jona-"
            r "Absolutely not." 
            n "Okay fine, but I guarantee he would listen to you talk about all the teas you brought from home, just saying."
            show rise flirt
            r "If you sincerely want to orchestrate something, I need you to think on it for more than a few seconds." 
            n "So I'm hearing a yes?"
            show rise smug
            r "A maybe, and on the condition you give it your full effort. I have seen what you can do when you put your mind to it."
            hide rise
        "Say we went out...":
            $ rRep += 1
            show rise surprised
            r "Are you serious?"
            n "It's just a hypothetical question. Say we went out, where would you want to go? Doesn't have to be here, could be anywhere."
            r "Where to start... Does it have to be just one place?"
            n "Yeah, just one place."
            show rise
            r "In that case, there was a lodge my family and I used to go to. It had a bunch of water slides, and a lazy river inside the hotel."
            r "As much fun as it would be to go to a regular water park, I liked the option to immediately change into dry clothes afterwards."
            r "It had a lavender berry sorbet that was to die for. Though I think you would prefer something more traditional, like a hot fudge sundae."
            n "Alright, let's do that some time."
            show rise frown
            r "I highly doubt the lodge is still standing. Even if it was, who would be there to run it? Everyone's been focused on rebuilding essential parts of Guwon."
            n "So it'll take a bit. Just means we get to look forward to it."
            show rise hearts
            r "We? Nagen does this mean-"
            n "I'm still not your fiance, okay? That's just way too fast, but if you wanted to actually get to know each other first, then yeah I'd be down to try dating."
            show rise hearts talk
            r "That sounds lovely."
            hide rise
            $ dateRise = True
            $ date = False
            $ dateNanase = False
            $ dateMomoko = False
            $ dateKitsune = False
            $ dateChisei = False
            $ dateHiro = False
            $ dateYoku = False
            $ dateMu = False
            $ dateTaiga = False
    show rise
    "She pushes the cup toward me. Whatever is inside is bright blue."
    r "It made me think of you. I hope you like it. I have matcha with me if you do not."
    "I don't know what she did to it, but it somehow tastes like vanilla custard. For a moment, she seems happy, but then her smile fades."
    show rise frown
    r "I have been wondering lately if knowing something and choosing to say nothing is the same as lying. I pride myself in always being honest, and I have been."
    r "Now it feels like I have only done the bare minimum."
    n "You're hiding something?"
    show rise mad
    r "I did not say that."
    n "Are you allowed to say that?"
    show rise smug
    r "I am allowed to say whatever I want. There is only you, and I, and the flies."
    r "You can trust me when I say I would never do anything that would cause you harm."
    n "Just me?"
    "There's a twinkle in her eyes."
    show rise scheme
    r "Of course not. I am not the sort to bite the hand that feeds me. If there is anything I excel in, it is meeting the expectations of powerful people."
    r "I hope you will remember that if there ever comes a time where you are the strongest person in the room."
    n "When am I not?"
    show rise smile
    r "In my defense, before coming here, I did not know what were rumors and what was the truth. You continue to surprise me. Right now may be one of those times."
    n "If that was true, I don't think you'd be chasing after me like you have been."
    show rise scheme
    r "Shows what you know. I happen to enjoy finding stray cats abandoned in the rain and taking them in."
    "Hey!"
    show rise disappointed
    r "Maybe it is projection, but I simply can not allow a sad little creature with potential being punished by a cruel world."
    r "Right now I may be just some girl, but once I turn eighteen, I will be some heiress instead."
    r "I would rather make my allies now rather than when something could cloud people's judgement of me."
    n "You think this is funny now, wait until I remind you in a decade you said this to me with a straight face." 
    "I have definitely made a powerful ally."
    hide rise
    pass
