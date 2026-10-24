label chapter2_interrogation:
    $ chapter2_interrogation_chance = False

    scene backgroundroof

    "The person responsible for this had to have close enough connections to the event to know my every move."
    "They planted Jona's drawings around the school and tried to keep me busy by raising the students expectations of the dance through the power of rumors."
    "They even tried to make sure I'd be distracted by other things during the event."
    "Thanks to Mariko, I think they were trying to be more careful about doing things in secret, but their note was sloppy."
    "I have everything I need to prove who did it."

    show rise disappointed

    "I show Rise the note, but she has no reaction to it, she just looks at me."
    
    r "What do you want, Nagen? It is not like you to be so indirect."
    
    n "I want you to admit that you did this."
    
    r "I see, and why would I do that?"
    
    n "Because, if you agree to work with me, I can keep you out of trouble."
    n "You'll be exposed either way, at least this way it'll be on your terms."
    
    show rise mad
    
    r "'My terms' sounds an awful lot like your terms. Besides, you have no proof it was me."
    r "Any number of people could have left that note on Jona's desk."
    
    "That may be true, but there's a good reason to suspect her."
    
    hide rise
    
    menu:
        "Location of note":
            jump chapter2_interrogation_a

        "Magazine":
            jump chapter2_interrogation_b

        "Red hair":

            show rise stare
            
            n "I know you planted a hair on that note to frame someone else."
            
            r "You saw who did it?"
            
            n "Well no."
            
            r "So then how do you know the hair was planted in first place?"
            r "If someone's going to bother framing another person, who's to say I'm not the one being framed."
            
            jump chapter2_interrogation_unsuccessful

label chapter2_interrogation_a:

    show rise stare
    
    n "I never told you where the note was found."
    
    r "Are you sure?"
    
    n "I have superhuman memory, so yes, I'm sure."
    n "Besides, you're one of the few people who could have gotten into the classroom before class."
    
    show rise disappointed
    
    r "You may have perfect memory, but I do not. I... think it is reasonable to assume it was at his desk."
    r "However, whoever did this used materials available to several other people who could have entered the room."
    r "When people lack information, they often fill in the gaps with their own conclusions instead of the truth."
    r "Are you immune to that as well?"
    
    "She's pretty good at making it sound like she's in the right, but she's refusing to outright lie."
    "I might be able to use that to my advantage. The threat letter lines up with something else that happened."
    "If I use that, I can get her."

    menu: 
        "Magazine Clippings":

            show rise surprised

            n "You're the only one I know who makes collages out of magazine clipings."
            
            r "I am not the only who can though."
            r "After all the libray has a fair share of magazines, just ask Chisei."
            
            show rise scheme
            
            r "Not to mention how many of us still share our things."
            r "All it takes is one person asking to borrow something to get their hands on the needed supplies."
            r "Are you also suggesting I am the only one who knows where to find a pair of scissors?"
            
            "Shit, I thought I had her!"
            
            jump chapter2_interrogation_unsuccessful
        
        "Jona's Sketchbook":
            #Branch A. Q2. Answer: Sketchbook Paper or Jona's Sketchbook
            
            pass
        
        "Nail Polish":
            
            show rise mad
            
            n "Anyone with the supplies could, but does just anyone have pink nail polish."
            
            r "No."
            r "That shade of pink is a popular color at the moment."
            
            show rise frown
            
            r "Have you seriously not considered the culprit had an accomplice?"
            r "Someone to make the note, another to get it into the classroom."
            r "There are quite a few people that find your friends' presence here unsettling, and Jona makes for a weak link."
            
            "An accomplice would completely ruin my theory. I don't think there is one, but I'm not sure how to prove there isn't."
            
            jump chapter2_interrogation_unsuccessful

    show rise surprised
    
    n "No, you're right."
    n "Except, I wonder where they got this paper from?"
    n "Jona's sketchbook went missing for a while."
    n "It's be nice if we could get him a backup."
    
    show rise disappointed
    
    r "They probably just used a page from the book when they stole it."
    
    n "I never said it was stolen, but it's interesting you assume the same person did both as well."
    
    r "...Great minds think alike."
    
    "Again, she won't outright deny it. Though all of this is circumstantial, none of it provides a motive."
    "However, what she did with it gave away her intentions."
    
    menu:
        "Popularity":
            
            show rise flirt
            
            n "I've seen movies, you're just trying to make yourself look cool by bullying someone other people don't like."
            
            r "Nagen."
            r "I have a collective networth larger than the school itself."
            r "Models were chosen for magazines based on my appearance."
            r "I do not need any help 'looking cool'."
            
            n "Yeah, but-"
            
            show rise disappointed
            
            r "Not to mention, I do not see anyone envying Mariko's position."
            r "There is no social benefit in this tiny hierachy to causing conflict."
            r "Though, if Jona were to leave, maybe that would finally end the tension once and for all."
            
            "She's seriously blaming Jona for this? He's gone out of his way to do nothing!"
            
            jump chapter2_interrogation_unsuccessful
        
        "Humiliating Uitto":
            
            $ rRep -= 1
            
            show rise disappointed
            
            n "You're jealous of Uitto!"
            
            r "The poor thing being stalked by someone she thought was a friend?"
            
            show rise mad
            
            r "No, not jealous in the slightest."
            r "In fact, I find it troubling the teachers saw no issue with those drawings."
            r "We may not get along personally, but I despise the fact several people wanted to keep those drawings a secret from her."
            r "I mean, how would you feel if someone close to you lied about their intentions?"
            
            n "They're just drawings. He drew all of us. She didn't want people to think of her like that."
            
            show rise surprised
            
            r "Exactly, and someone close to her does."
            r "Are you saying you would keep something like that from her, just because it didn't make you uncomfortable?"
            
            n "N-no, but putting it out there for everyone to see-"
            
            show rise mad
            
            r "Exactly, everyone believes Uitto was the victim in this, and not someone causing drama."
            r "I sincerely am disappointed you continue to keep Jona in your company after that."
            r "I thought you were smarter than that."
            
            jump chapter2_interrogation_unsuccessful

        "Bullying Jona":
            #Branch A. Q3. Answer: Jona's Sketches

            pass
            
    show rise disappointed
    
    n "Very peculiar they chose to share some of his drawings all over the school."
    n "They must have really wanted us to see how much Jona LOVED Uitto."
    
    r "A little too much, I would say."
    
    n "Yeah, too bad he didn't draw any of us."
    
    "She purses her lips."
    
    n "I would have loved to see what I'd look like."
    
    "Her eyebrow twitches."
    
    n "He rarely draws people unless he really likes them."
    
    show rise talk
    
    r "Quite a charitable reading."
    r "Neither I nor Uitto found the drawings of her flattering, and we rarely agree."
    r "IF there were drawings of you, I do not think you would want anyone seeing them."
    
    show rise scheme
    
    r "In fact, I think you would pocket it so fast no one else would have a chance to see it."
    r "Your right pocket, probably."
    
    show rise disappointed
    
    r "So before acting so coy, consider that other people may have a clearer understanding of what is going on than you."
    
    "How the hell did she know which pocket I put it in?"
    "I can't let her get into my head. She's clearly backed into a corner."
    "She may be good at dressing things up, but she gave herself away the minute she made the note."
    
    jump chapter2_interrogation_2

label chapter2_interrogation_b:

    show rise surprised
    
    n "You said yourself these could have come from your magazines. Lending them out would make for the perfect cover."
    n "Especially since it would have been after this note was made. No one else knew about the dance until later that day."
    
    show rise mad
    
    r "I also said there could be issues from the library here. There are thousands of books and magazines here."
    r "You have no way to prove those clippings could not have come from there."
    
    n "But damaging the collection is against the rules!"
    
    show rise flirt
    
    r "...So is threatening a student."
    
    "Right. I can't prove she owned the magazines, but that doesn't mean she didn't do it. The method of making the note matches something else."
            
    menu:
        "Event Planning Book":
            #Branch B. Q2. Answer: Clippings
            
            pass

        "Fashion Magazines":
            
            show rise mad
            
            r "Shoma has them as well, have you lobbied the same accusations at him?"

            n "No-"

            r "Jona looked through them as well, as far as you know the culprit stole magazines along with his sketch book."
            r "It would not be out of the ordinary for a thief to steal other things."
            
            jump chapter2_interrogation_unsuccessful

        "Dacne":

            show rise surprised
            
            r "What does that have to do with me?"
            r "I have good grades in English."
            r "The only one I know who would misspell something like that is Hiro."

            n "Getting a little defensive over a spelling error, aren't we?"

            show rise mad
            
            r "You would do the same if someone implied a spelling error meant you were responsible for something."

            "I guess she's right about that."

            jump chapter2_interrogation_unsuccessful
    
    show rise disappointed
    
    n "You're also the only one I've seen cutting up magazines at all. Those little party books of yours are mostly magazine collages."
    
    r "Those 'party books' were made before the riots. Just because you saw me make one, does not implicate me as some sort of bully."
    
    "But she left something behind that proves she made it."

    menu:
        "Location of the note":

            show rise disappointed

            r "Any class representivitve could have left it there, as could any vision major."

            n "Ichita didn't see anything before he locked up for the night."

            r "Sounds to me like you found your answer and it has nothing to do with me."

            "Man she is not letting up on framing him."

            jump chapter2_interrogation_unsuccessful

        "Nail Polish":
            pass

        "Color of Magazine Clippings":
            
            show rise frown

            r "Are you saying I am the only one who likes the color green?"

            n "Well, no."

            r "Then what does the color of the clippings have to do with me?"

            "She's worse than a lawyer."

            jump chapter2_interrogation_unsuccessful

    show rise stare 
    
    n "No, what implicates you is the nail polish you left behind. The smudges on the page match the color you're wearing."
    
    r "As you can see, my manicure is intact. I have been more than willing to share my cosmetics with anyone."
    
    "She must have redone them to cover her tracks?"
    
    r "If we are talking about hard evidence, you would be better off checking who that hair belongs to. I am a natural blonde so it is not mine."
    
    n "That would be convenient for you, which is probably why you planted it there."
    
    show rise disappointed
    
    r "Honestly Nagen, none of our classmates have gone around saying I pulled hairs out of their head, have they?"
    r "We all lock our doors when we leave."
    r "How could I get someone else's hair to put there in the first place?"

    menu:
        "Location of Note":
            #Branch B. Q4. Answer: Location of the Note
            pass

        "Stuco Meeting":

            show rise frown

            r "You were there, did you see me touch anyone during the meeting?"

            n "No."

            r "Did you see me pick anything off the floor or a table?"

            n "No."

            show rise mad

            r "Then how could I have gotten a hair without you noticing?"

            "It had to be from somewhere else I guess."

            jump chapter2_interrogation_unsuccessful

        "Hair brush":

            show rise scheme

            r "Why would someone give me their hairbrush?"

            "I guess she does look like the kind of person who'd have a bunch of her own."

            show rise frown

            r "Something like that would be odd enough to come up in your investigation."
            r "Saying I got my hands on someone else's personal care items without anyone knowing is a stretch to say the least."
            r "Circumstantial evidence is not proof."
            r "I believe that is why you are able to wander the school grounds as we speak."
            
            jump chapter2_interrogation_unsuccessful
    
    show rise mad
    
    n "Ichita shares the same homeroom as Jona. I haven't seen any janitors around here, have you?"
    n "It's entirely possible that you found one while dropping off the note."
    n "In fact, I bet you got the idea from your own hair flailing on the page and messed up your nails trying to get it out."
    
    r "So you proved it is not Ichita. That does not excuse the fact that someone else with the same nail color did what you said I did."
    
    "True, but when you look at the note closely, there's one last thing that points to her."
    
    jump chapter2_interrogation_2

label chapter2_interrogation_2:

    menu:
        "Queen of the Dance":
            show rise frown

            r "That was Ichita's idea."
            r "If you recall, I did not agree that anyone in the council should be elligible to win a prize at an event we were hosting."

            "Right, she didn't even imply we should."

            r "If that is your rationale, you have the wrong person Nagen."

            jump chapter2_interrogation_unsuccessful

        "The Dance":
            #Main Branch. Answer: Dance

            pass

        "The date of the dance":

            show rise mad

            n "You were the one who picked the date."
            
            r "I wanted to change the date after I realized it fell on the anniversary of an event I used to go to."
            r "You were the one that said it was set in stone."

            n "Yeah, like reverse psychology thing."

            show rise frown

            r "No, like a regular psychology. I asked you to change the date, and you said there was nothing you could do."
            r "It makes me wonder if you are doing this investigation for attention."

            "Damn it, I don't know what else to do."
            "I know she's not being honest, but she hasn't said anything that's an outright lie."
            
            jump chapter2_interrogation_unsuccessful

    show rise frown
    
    n "The student council originally planned to throw a party. You and Ichita were the ones pushing for a dance."
    n "You're also the only one in that room that wears nail polish."
    
    r "You wear nail polish."
    
    n "Mine's black and I wouldn't do this to my own friend. I'm interrogating you!"
    
    show rise mad
    
    r "You still do not have any solid proof. All of your evidence is purely circumstantial."
    r "If it comes down to a he-said, she-said; I have the upper hand. You are a convicted criminal and I am one of your victims."
    
    n "Yeah, well, that's a risk I'm willing to take."
    
    r "What do you want?"
    
    jump chapter2_interrogation_success

label chapter2_interrogation_success:

    $ chapter2_solved = True

    hide rise

    menu:
        "Surrender":

            $ Hero += 1
            $ Reputation += 1

            show rise disappointed

            r "That is all?"
            
            n "We both suffer if this escalates further. Just leave Jona alone."
            
            r "I gave him plenty of opportunities to leave peacefully. If I fail to fulfill my end of the bargain, I will lose everything I worked for."
            
            n "And what's that?"
            
            show rise mad
            
            r "I need my father's company back."
            
            n "Your father? I thought Jusa Cosmetics belonged to your mom."
            
            r "I do not care about some beauty empire."
            r "I am more concerned about the legion of scientists carrying on our fathers' research while we are stuck here."
            
            hide rise
            
            show background_NagenFB_Testing
            #CG Nagen in the testing center
            #Present
            hide background_NagenFB_Testing
            
            show rise frown
            
            n "Why didn't you say something sooner?!"
            
            r "It would leave me vulnerable to failure. Can you promise me, whe this is all over, I will have control of that horrible place?"
            
            n "....."
            
            hide rise
            
            menu:
                "Yes":
                    
                    $ rRep += 1
                    $ Reputation += 1
                    
                    show rise frown
                    
                    r "...Thank you. I know it is difficult to trust people right now. "
                    
                    "She held out her hand then flinched."
                    
                    show rise surprised
                    
                    "Her eyes are bloodshot. They weren't like that before."
                    
                    #need to have crying sprite
                    
                    n "Rise?"
                    
                    r "I need a mirror."
                    
                    "She kept grabbing the air, and scrunched her eyes closed. A constant stream of tears made her makeup run."
                    
                    n "What the hell's going on?"
                    
                    r "The walls have ears Nagen, please. "
                    
                    "I walked her to the restroom."
                    
                    n "Maybe we should get you to a nurse?"
                    
                    r "I'm fine, they're just sticking."
                    
                    "Contacts shouldn't stick."
                    "I didn't think I should follow her into the bathroom."
                    "Even from the hallway, I can hear she's crying and something wet definitely hit the counter."
                    
                    n "Rise?"
                    
                    r "I'll be okay..."
                    r "I have to be..."
                    
                    "I had to walk her back to her room."

                "No":
                    
                    $ rRep -= 1
                    $ Reputation -= 1
                    
                    show rise mad
                    
                    r "Then we have no deal."
                    
                    "I made good on my threats but so did she."
                    "I'm not sure what she told people, but even though the teachers sided with me, everyone's more wary than before."
                    
        "Money":
            
            $ Villain += 1
            $ rRep -= 1
            $ Reputation += 1
            
            show rise disappointed
            
            r "Nagen, I'm sixteen, what makes you think I have any money?"
            
            n "Your parents were ridiculously wealthy."
            n "Even if you don't have a trust fund, you have to have assets of some kind. That dress alone is a couple hundred dollars."
            
            r "Maybe before the riots, but luxuries are not in high demand right now."
            r "I will be penniless until graduation, that's part of the reason I'm so desperate right now."
            
            n "I want half."
            
            show rise surprised
            
            r "Half of what?"
            
            n "I want half of everything you're worth, or I'll let that cultist group know who and where you are."
            
            "She went pale."
            
            n "They'll also be around after we graduate."
            
            show rise flirt
            
            r "You'd really stoop so low? Those monsters burned people at the stake!"
            
            n "Well I'd rather have the money. I just don't trust you to keep your word without proper motivation."
            
            "She nodded, though she looked like she was going to be sick."
            
            n "Obviously, this stays between us. You wouldn't want to risk the people here hating you."
            
            "She nodded again."
            
            n "Pleasure doing business with you."
            
    hide rise

    return

label chapter2_interrogation_unsuccessful:

    show rise disappointed

    r "It seems you have no concrete proof of your suspicions."
    r "I hope you leave the rest of our classmates alone about this."
    r "Besides looking paranoid, what happens to Jona has nothing to do with you."
    r "I mean, has he asked you to do this?"

    n "No."

    "In fact, he wanted me to stay out of it."

    show rise talk

    r "Respect his wishes then. He may be trying to protect you as well."

    "She left without another word."

    hide rise

    return

label chapter2_investigation_fail:

    scene backgroundclass

    n "So if we do something now, then there shouldn't be any problems, right?"

    show sato sigh
    sa "Nagen, I appreciate you coming to me with your concerns, but I'm afraid I don't follow."
    sa "While I agree this note was meant to scare your friend, it doesn't fall in line with how that student deals with conflict."

    "Damn it, there has to be something I'm missing."

    show sato annoyed

    sa "Anyone here would know you'd try to look into it, which means they could be framing someone else."
    sa "Not to mention the fact Jona hasn't come to any of us about what's been going on."
    sa "I know you want to protect your friend, but involving innocent people into this would make things worse for both of you."
    sa "Consider someone might have lied to you, even by ommission."
    sa "If you compare multiple accounts, you'll have a stronger arguement for who did it."

    "So if I have more people who agree with me, she'll consider it."
    
    sa "It would be easier to help you if I had something concrete to go off of, like where the supplies used to make the note came from."
    sa "Of course, we could always cancel the dance instead."

    n "No, please don't do that. Everyone's looking forward to it. I don't want to ruin it for everyone else."

    show sato smile talk

    sa "That's very kind of you."
    sa "In the meantime, I'll see if Yaguichi and Inukai will join us."
    sa "It sounds like we'll need all the help we can get. It's your first school event and we all want to see what you've been working on."

    "More teachers means it will be harder for someone to pull something. It's kind of scary how casual she can make beefing up security sound."

    n "Any idea who I should talk to?"

    sa "The note was found in the Vivaldi's class. Try seeing what her students saw before the note was found."

    n "Thank you."

    hide sato
        
    "Guess I have to keep looking."

    return