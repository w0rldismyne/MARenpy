label chapter1_interrogation:

    #[Boss Accusation]
    #[IF Intel > ? This option will be available to the player]
    #(If from Mariko Interrogation)
    #(AN: All pieces of evidence will be on screen. There will be breaks in the dialogue where the player will be encouraged to present evidence. [ = the option needed to continue the scene. Letters will denote which path the player's going down if there is more than one right answer.)
    
    "I know who did this."
    "The person responsible was someone close to Kazz."
    "They would have known the stuff that he smuggled in from day one since he was bragging so much."
    "When they had an opportunity to take his phone, that’s when they put their plan in action."
    "They made sure they were the last person in the PA booth and set up his alexa to play a command right as everyone was out of class."
    "In order to keep from getting caught, they hid his phone somewhere that would incriminate a different classmate."
    "I’m sure they thought they’d have plenty of time to run back to the main halls so it would look like they had an alibi when the announcement went off."
    "But, even without feeling pain, I’m sure running on an injured leg is difficult."

    n "Isn’t that right Mariko?"
    
    show mariko judge

    "Between what everyone's been seeing, and how she's been acting, I'm sure she's behind the PA Incident."
    "However, it's too soon to get her to admit it, especially with how defensive she's been lately."
    "If I want her to talk, I should ask her about something innocuous; something that would connect her to the recording booth without sounding like an accusation."

    n "I know you're busy with the cheer squad, but don't you talk to people outside of cheer?"

    m "....."
    m "Yeah, I'm talking to you, aren't I?"

    n "Well- yeah, but aren't there other people you're close to?"

    m "I've been talking to Shoma about uniform assignments a lot lately, if that's what you're getting at."

    "No good. I'll have to work backwards then and show proof someone thinks they're close to her."
    # Choose clue goes here

    #[1: Friends List]

    show mariko talk

    n "You're friends with Kazz and his group too."

    m "He's a nice guy and all, but 'friends' is a little strong of a term."
    m "We were in the same homeroom class at Estella, so talking to him came a little more naturally."
    m "'What have you been up to?' That kind of stuff. Why does it matter that I talk to other people?"

    "She's trying to downplay their connection, but it explains some things."
    "If they knew each other before, it's make sense that he'd want to impress her."

    hide mariko

    menu:
        "Brag":
            pass
        "Prank":
            jump chapter1_interrogation_unsuccessful
        "PA Access":
            jump chapter1_interrogation_unsuccessful
        "Club Ad":
            jump chapter1_interrogation_unsuccessful

    # Choose clue goes here
    #[2: Brag]

    show mariko talk
    
    n "It doesn't really. It's just that Kazz can be pretty naive sometimes."
    n "I heard his first day here, he told everyone who would listen about all the junk he smuggled in."
    n "That includes what was found in the PA booth. I'm sure you're one of the first people he went to."

    show mariko mad talk

    m "So what if I was? He told a lot of people about that stuff. I mean, even you know about it."
    m "Besides, that has nothing to do with me. There isn't any proof the stuff that was in there belonged to Kazz in the first place."

    "I'm positive the recording device was Kazz's."

    hide mariko

    menu:
        "PA Access":
            jump chapter1_interrogation_unsuccessful
        "ID Account":
            jump chapter1_interrogation_b
        "Prank":
            jump chapter1_interrogation_a
        "Missing Phone":
            jump chapter1_interrogation_unsuccessful

    # Choose clue goes here
label chapter1_interrogation_a:
    #[3A: Prank]
    
    show mariko mad talk

    n "Dyre's been telling people he handed Kazz's Echo directly to you so you could hide it in the booth."
    n "It seemed funny to him before stuff actually went missing."
    n "There was only one Echo there, so it should be his."

    m "You don't know that."

    n "Are you saying he lied? I wouldn't be surprised, but if he hears you've been telling people otherwise-"

    m "Don't! He told a few people about doing that, but we couldn't go through with it."

    n "Then do you still have it?"

    show mariko glare

    m "N-no. I hid it somewhere else. Like I said, none of us could get in."

    "Now that's just a bold-faced lie."

    hide mariko

    menu: 
        "Club Ad": 
            jump chapter1_interrogation_unsuccessful
        "ID Account":
            jump chapter1_interrogation_unsuccessful
        "PA Access":
            pass
        "Kazz's Bragfest":
            jump chapter1_interrogation_unsuccessful
            
    # Choose Clue Menu goes here
    #[4A: PA Access]

    show mariko glare
    
    n "You're one of the few people who could get in at all."
    n "Even Setsuna couldn't get in. That made you the perfect pawn for Dyre's prank."
    n "Not only that, it gave you a pretty good alibi too. No one would question why you had his stuff if Dyre was talking up a prank you were helping with."

    show mariko judge

    m "So? Nagen, are you seriously accusing me of manipulating my classmates?"

    n "No, I think you just saw an opportunity and took it. I'm sure I'm not the only one who suspects as much."
    n "They're just too nice to confront you about it."

    m "An opportunity to do what? Quit dancing around the subject and spit it out."

    n "You're the one who called out a challenge to Hiro on the PA system."
    n "You borrowed the keys from Kietsu and returned them after the message played."
    n "You're the only one who could have done it."

    m "All of this is just gossip, Nagen. Even if Kietsu kept track of when the club leaders had the key, none of that proves I was ever in the booth."
    
    hide mariko
    
    # Choose Clue Menu goes here

    menu:
        "Cheer Ad":
            pass
        "Alexa Commands":
            jump chapter1_interrogation_unsuccessful
        "Found Phone":
            jump chapter1_interrogation_unsuccessful
        "Locker Number":
            jump chapter1_interrogation_unsuccessful

    #[5A: Cheer Ad]

    show mariko glare
    
    n "This is your ad, right here, and it was turned in after the other club leaders."
    n "You were the last person in the booth before the announcement went off."
    
    hide mariko
    
    jump chapter1_interrogation_success

label chapter1_interrogation_b:
    #[3B: ID Account] 

    show mariko
    
    n "All you have to do is ask it who's logged into it."
    n "It should tell you right away if it belongs to him."
    n "If nothing else, you could ask it to play his music or any number of things he programmed that thing to say."

    show mariko talk

    m "Alright, I get it. It doesn't matter anyway. The teachers have it, remember? There's no way to check it."

    n "Right, but I could check the Echo that hasn't been confiscated and see if he's logged into that one."

    show mariko cringe

    m "You wouldn't."

    n "It'd be a quick walk to Shoma's workshop is all."
    n "You had access to Kazz's whole setup and he gave you just enough information that you could use it."

    show mariko judge

    m "Use it for what? Nagen, do I look like I'm someone who needs a digital assistant?"

    n "More like a digital accomplice."

    "Without it, there'd be no way for her to have used the PA mic without getting caught."
    
    hide mariko

    # Choose Clue Menu goes here
    menu:
        "Alexa Commands":
            pass
        "Found Phone":
            jump chapter1_interrogation_unsuccessful
        "Missing Phone":
            jump chapter1_interrogation_unsuccessful
        "Mystery Noise":
            jump chapter1_interrogation_unsuccessful

    #[4B: Alexa Commands]

    show mariko talk
    
    n "You used it to play your message without you having to stay in the booth to do it."
    n "You even looked up the instructions on how to get the machine to play a custom sound bite."

    m "Nagen, I'm a star athlete, but even I can't trigger a voice command and make it out without anyone seeing me."
    m "Besides, I was in class, like everyone was supposed to be."

    "Seems like she's counting on that to be her alibi, however..."

    n "It could be remotely activated with anything Kazz was logged into, like his phone for instance. It has been missing for quite a while."

    show mariko judge

    m "I did not steal his phone! Kitsune's the one who was wandering around school with something that didn't belong to her." 
    m "Ask Ichita, he was with her this morning."

    "Interesting she brought her up, since their stories contradict each other."
    
    hide mariko

    # Choose Clue Menu goes here
    menu:
        "Mystery Noise":
            jump chapter1_interrogation_unsuccessful
        "Found Phone":
            pass
        "Missing Phone":
            jump chapter1_interrogation_unsuccessful
        "Kazzz's Bragfest":
            jump chapter1_interrogation_unsuccessful

    #[5B: Baton Pass]

    show mariko judge

    n "She's been telling everyone she gave it to you."

    m "So you're just going to believe her over me, just like that? How is that remotely just?"

    n "Well, it helps that Rei saw it happen."

    show mariko cry

    m "...Rei?"

    n "Are you going to accuse your best friend of lying too?"
    n "She has no reason to say something that would make you look like a thief. Or maybe she does, I don't know."

    m "No. Rei's not- she doesn't lie. But that doesn't mean I have it. You can search my stuff, but you won't find it."
    m "It's probably with the teachers, who knows what they do with contraband?"
    m "I took it there after I talked with Kitsune, which was before the announcement went off. So, yeah, you can't prove a thing."

    "She's just going to keep denying stuff until I spell it out for her. I know for a fact it didn't go 'straight to the teachers'."
    "Multiple people have said as much."

    hide mariko

    # Choose Clue Menu goes here

    menu:
        "Missing Phone":
            jump chapter1_interrogation_unsuccessful
        "Found Phone":
            jump chapter1_interrogation_unsuccessful
        "Mystery Noise":
            jump chapter1_interrogation_ba
        "Second Locker":
            jump chapter1_interrogation_bb

label chapter1_interrogation_ba:
    #[6B: Mystery Noise]

    show mariko mad talk
    
    n "Leading up to the event, people kept hearing a siren in the hallway."
    n "It really freaked people out, especially the student council who was meeting that morning."
    n "Of course, I'm sure it would have freaked them out less if they knew what Kazz's ringtone sounded like."

    "She's ringing her hands quite a bit. Doesn't seem like she has anything to say to that."

    n "Kazz has been having people call it for days."
    n "Funnily enough, no one could hear it anymore after the announcements, no matter how many times it was called."
    n "It might have been given to the teachers then, but not before it could be used."

    m "Knock it off with the smug act. I don't care how many coincidences or testimonies you found, none of that proves I did it."
    
    hide mariko
    
    #Choose Clue Menu goes here

    menu: 
        "Locker Number":
            jump chapter1_interrogation_b2
        "Found Phone":
            jump chapter1_interrogation_unsuccessful
        "Dyre's Prank":
            jump chapter1_interrogation_unsuccessful
        "Brag":
            jump chapter1_interrogation_unsuccessful

label chapter1_interrogation_bb:
    #[6C: Second Locker]

    show mariko cringe
    
    n "I can search anywhere you say? Even the locker you're borrowing for uniform storage?"

    m "How- that has nothing to do with this."

    n "But you do have a second locker, the one that was originally assigned to Mu?"

    m "Yeah, you're welcome to wade through the pompoms, but you're repacking it if you do."

    n "No need. I just wanted to make sure we agree that's your locker now."

    show mariko glare

    m "So what if it is? It's like you said, I'm using it to hold club supplies."
    m "Even if you told the teachers, I wouldn't get in trouble over that."
    
    hide mariko

    menu: 
        "Locker Number":
            jump chapter1_interrogation_b2
        "Found Phone":
            jump chapter1_interrogation_unsuccessful
        "Dyre's Prank":
            jump chapter1_interrogation_unsuccessful
        "Kazz's Bragfest":
            jump chapter1_interrogation_unsuccessful

label chapter1_interrogation_b2:
    #[7B+C: Locker #] 

    show mariko glare
    
    n "Multiple people heard the siren coming from your cheer locker."
    n "It got so bad, Setsuna had to bust into it to get the noise to stop."
    n "Only she couldn't just mute the phone because it was password locked."
    n "If it wasn't, she might not have given it to the teachers at all."
    n "Both of them thought the locker still belonged to Mu, which I'm sure you were counting on."
    n "Also it's weird it was locked considering Kazz doesn't lock his phone."
    
    hide mariko

    jump chapter1_interrogation_success

label chapter1_interrogation_success:

    show mariko judge

    m "So?"

    n "That's all you have to say for yourself?"

    m "I didn't use all that junk to hide from you, I did it to give everyone a chance to prepare."
    m "And since I don't see Hiro behind you, I take it you're not here to support me."

    n "Support what exactly?"

    show mariko mad talk

    m "You've seen this place, it's not safe. It's a place to hide us until we're adults no one's responsible for."
    m "Who knows what's going on out there while we're stuck here? The fighting could come back on our doorstep any minute."

    n "You're being paranoid."

    m "And who's fault is that exactly? I know it would be easier to run away, but I can't just leave Rei here by herself like that."
    m "Hiro's my ticket for getting both of us out of here."

    n "Says who?"

    show mariko glare

    m "Like I'd tell you anything. I know I'm taking a gamble, but I'm not going to blow it by saying something I shouldn't."

    n "You're not even going to try and beg for forgiveness?"

    m "From you? What are you going to do, tell on me? Hit me? I don't feel pain and I already knew I wasn't going to graduate."

    "For a moment, her bravado falters."

    m "Hiro took everything I cared about and you just sat by and watched it happen. What else could you possibly do to me?"

    hide mariko

    menu:
        "Blackmail you":

            $ Villain += 1  

            show mariko cringe

            n "You really haven't been talking to other people, have you?"
            n "Sure, there are a few people who are mad that my friends and I are here, but more of them are pissed about what you did."
            n "You saw how Rei blew up at us. She'll barely talk to me now, imagine what she'd do to you."
            n "Did you even tell her what you were planning?"

            m "......"

            n "I can't guarantee you won't get in trouble with the faculty, but if you get expelled over this, it'll be my word against speculation."
            n "If we aren't on good terms by the end of this conversation, Rei won't want anything to do with you. That I can guarantee."

            m "You rat."

            n "Is that a no?"

            m "What do you want?"

            n "Simple. Turn yourself in and I'll help downplay this whole incident."

            "Of course, there's no telling how much mileage I can get out of this afterward."

            show mariko upset talk

            m "....."
            m "Fine." #(-Mariko)
            #(Enemy Neutralized) Add variable to play data so the boss battle will be skipped directly to the tape scene
            
            hide mariko

            $ mRep -= 1

        "Protect you":

            $ Hero += 1   

            show mariko upset talk

            n "Someone put you up to this, didn't they?"
            n "How else could you know we were going to be here?"

            m "....."
            m "I didn't think I'd meet anyone from the riots."
            m "I was going to refuse to come here initially, but then I got this tape..."

            "She shivers, gaunt and ghostly pale."

            show mariko cry

            m "Whoever sent it knew about all of us and they knew where this place was."
            m "We're not safe here. I thought I could use them to get Rei and I out of Guwon entirely."

            "There's no way that's going to happen."
            "Even if she was successful, the DVP wouldn't let unaccompanied minors disappear like that."

            n "And what if you failed?"

            m "I don't know exactly, but whatever it is... it's not pleasant."

            n "I'm not going to let anything happen to you."
            n "We'll take care of who targeted you."

            m "We?"

            n "You may not have faith in Hiro and I, but we'll get to the bottom of this."
            n "You should tell the teachers though, they should know someone from the outside is targeting us."

            m "But if I do that..."

            "She covers her earrings with her pompoms and keeps darting her eyes between me and the paper in front of her..."
            "Is she wearing cameras? I scribble the message down and hold it up. She nods. Who would do something like this?"

            n "Nevermind. I'll let Uitto take care of things." #(+Mariko) 
            
            hide mariko
            
            $ mRep += 1
            #(Enemy Neutralized)

    show mariko upset talk
    
    "Mariko hands me an unmarked VHS tape from her bag."

    $ chapter1_solved = True

    m "On the roof, the guys found an old CRT TV."
    m "You should go there when you get the chance."

    n "I- thanks."

    "I should wait until I'm with everyone to watch this."
    "She collects her stuff with a solemn look on her face."

    m "Don't thank me yet."

    hide mariko
    
    return
    

label chapter1_interrogation_unsuccessful:

    #[If Accusation = Fail]

    show mariko glare
    
    m "It's your word versus mine, Nagen and let's face it, people trust me more than they trust you."
    m "They want me to be here more than you. They need me to protect them."
    m "You're just paranoid and trying to protect yourself. Like always."

    "She gathers up her supplies with a glare."

    m "If I find out you've been harassing the other girls like this, you're a dead man."

    hide mariko

    return #call main game loop

    #(Enemy Agitated) 
    #Investigation Helper Scenes 
    
    #"There's no way I can talk to everyone before the deadline. Maybe one of the guys overheard something in one of their classes. At the very least, it'll give me a place to start."

label chapter1_investigation_fail:

    scene backgroundfield
    
    "I know who did this."
    "The person responsible was someone close to Kazz."
    "They would have known the stuff that he smuggled in from day one since he was bragging so much."
    "When they had an opportunity to take his phone, that’s when they put their plan in action."
    "They made sure they were the last person in the PA booth and set up his alexa to play a command right as everyone was out of class."
    "In order to keep from getting caught, they hid his phone somewhere that would incriminate a different classmate."

    show inukai concerned
    
    ik "Nagen, do you have any proof this person did it?"
    
    n "I mean... not exactly, but it's possible."

    show inukai sad

    ik "I appreciate you wanting to help out a friend Nagen, but I can’t get someone in trouble for being on campus without a teacher present."
    ik "Has anyone else seen this student with Kazz’s things and they had access to the PA room?"

    "Maybe I need to ask around some more."

    return

label JonaInv1:
    scene backgroundamp
    "Jona doesn't really like talking to people alone, so I appreciate he was willing to do this for me."

    show jona frustrated

    j "I wasn't sure what to ask people about, but I think I found some stuff."
    j "Kietsu's been really busy, so he let club leaders go into the PA booth alone."
    j "They're the only ones who could have gone in."
    j "Ichita thought he found Kazz's phone, but someone else went to give it to Setsuna."

    n "Anything else?"

    hide jona frustrated
    show jona relaxed

    j "No one in my class is responsible for the incident."
    j "Or at least, they weren't lying when they were talking to me."

    n "Well that narrows it down a little."

    hide jona relaxed
    show jona happy

    j "Oh good." #(+PA Access)

    $ inventory.AddClue(clue_pa_access)

    hide jona happy
    return #connect to main game loop

label HiroInv1:
    scene backgroundamp
    "I felt a little nervous sending Hiro out on his own. Still, he insisted and when he returned..."

    show hiro

    h "Mariko and Rei wouldn't even talk to me."

    n "Really?"

    "I shouldn't be too surprised, but I thought Hiro was friends with everyone."
    "I guess even he has his limit."

    hide hiro
    show hiro sad smile

    h "They were totally afraid of me. It was such a gross feeling."
    h "Even before I could say anything, they were trying to get away from me."

    n "There's not much we can do about that at the moment."

    hide hiro sad smile
    show hiro sad talk

    h "I know... A-anyway, I was able to talk to Shoma."
    h "He's borrowing one of those Alexa thingies too, so I was able to ask him all about it."
    h "I guess in order to get it to play stuff like it did, it'd have to have some kind of remote like a phone or a laptop."
    h "That way they could set it to go off at a specific time."
    h "He also showed me his to check what account it's using, to see who it belongs to."
    h "I also overheard a few Intel Majors going off about Kazz bringing in a bunch of banned stuff."
    h "You might want to try asking him about what happened. It sounds like he might be a victim in this too."

    n "I'll definitely keep that in mind. Thanks for the info." 
    
    hide hiro sad talk

    $ inventory.ShowClue(clue_account)
    $ inventory.ShowClue(clue_brag)

    return #connect to main game loop

label UittoInv1:
    scene backgroundstuco
    "I ask Uitto if she was able to dig up anything."

    show uitto

    u "I can't believe you wanted me to talk to Kitsune for you."

    n "...Did you?"

    u "I could tell you exactly what she'd say. 'Memememe and also me.'"
    u "There you go, you got the full experience."

    n "Anyone else have anything to say?"

    hide uitto
    show uitto talk

    u "Well, all the student council kids got spooked this morning."
    u "I guess a ghost or something is haunting the lockers."
    u "Setsuna told me which one, but I forgot."
    u "Oh! I do know who's responsible for the Echo in the PA room."
    u "Dyre had a friend of his sneak it in after it was stolen from Kazz."

    n "Isn't that Kazz's booth though?"

    u "Exactly. Who knows how long they were going to be playing musical chairs with his stuff?"
    u "That would drive me bananas."

    n "Thanks, Uitto." #(+Mystery Noise, +Prank)
    $ inventory.ShowClue(clue_mysterious_noise)
    $ inventory.ShowClue(clue_prank)

    hide uitto talk
    return #connect to main game loop