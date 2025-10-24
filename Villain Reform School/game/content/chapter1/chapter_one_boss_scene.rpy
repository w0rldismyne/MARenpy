label chapter1_boss_scene:

    scene backgroundB1
    
    "I run to the practice field with all my might while keeping my phone close, hoping that at any moment, Hiro will answer my calls."
    "As the grass caves under my boots, I see three girls arguing amongst themselves. For a brief second, I thought I had made it in time."
    "After all, it isn't uncommon for the cheerleaders to monopolize the field. However..."

    s "Answer the question." #(Irritated)
    
    m "....."

    re "Making me pick sides like this again… I can't." #(Sad/desperate)
    
    m "If you're not going to help me, just leave."

    re "We're trying, but revenge isn't going to help anyone. Please, let this go."

    "Mariko looks up at me with a brow raised."

    m "I don't see Hiro with you, though it looks like you're bringing everyone else instead."

    "The other cheerleaders look up as Uitto and Jona join me at my side."

    n "I think you already know why Hiro isn't with us."

    m "Is that so? Then were you planning on bringing him to me as well?"

    scene backgroundmariko

    show uitto serious at left

    u "You backstabbing little-"

    show rei disappointed

    re "It's not like that! I noticed Hiro wasn't in class and…"

    show setsuna cringe at right 

    s "We had the same suspicions. Well, most of us did."

    hide uitto serious
    show mariko glare at left

    m "This has nothing to do with you, Setsuna; it's between me and them."

    hide mariko glare
    show mariko judge at left

    m "Even though Hiro's not with you, I'll still forgive you, if you were planning on giving him to me."
    m "After all, it's not your fault someone else beat you to the punch."

    n "We'd never do something like that!"

    hide setsuna cringe
    show jona mad at right

    j "...Where is he?"

    hide mariko judge
    show mariko mad talk at left

    m "How disappointing. I really wanted to avoid hurting other people."
    m "But if you're going to continue to defend him, then you're just as guilty."

    hide uitto serious
    hide rei disappointed
    show rei sad 

    re "Mariko, this is enough! You're scaring me."

    hide mariko mad talk
    show mariko cry at left

    m "...I'm sorry."

    hide rei sad
    hide jona mad

    "She snaps her fingers and with solemn expressions, the other girls turn to us. Uitto and Jona end up pinned before I know it."

    hide mariko cry
    show mariko glare

    m "This wouldn't have happened if you just listened to me in the first place."

    u "Nagen, don't just stand there, do something!"

    hide mariko glare
    show mariko mad talk

    m "This is your chance to wash your hands of this whole mess, Nagen. Turn tail and run. Run as far away as you can from this place."
    m "Show me how far you can really make it on your own."

    if mRep < 5:
        show backgroundblack
        with dissolve

    "What else is there to say?"

    hide mariko mad talk

    if mRep >= 5: 

        show mariko upset talk

        m "Please, I don't want to fight you."

        n "If you don't want to fight me, then let them go."

        m "Sorry, but I don't exactly trust your ‘friends' right now."

        show jona depressed at left

        j "That's fair."

        show uitto serious at right

        u "Do not agree with the psycho head cheerleader!"

        hide mariko upset talk
        show mariko cry

        m "I think that might be why I was chosen. I don't have anyone to rely on other than Rei and they still found us."

        n "...Who's they?"

        hide mariko cry
        show mariko upset talk

        m "I'm not sure, but they seem to know a lot about you. I think it's the people you used to work for."

        "Could it be Lethe's old allies? But then why target us?"

        hide mariko upset talk
        show mariko cry

        m "Nagen, when you turned yourselves in, they wanted me to- I'm supposed to be Hiro's replacement."
        m "What do you think they'll do to me if I refuse to go through with this?"

        "His... replacement?"

        m "Nagen, please. Run."

        hide mariko cry
        hide uitto serious
        hide jona depressed

        g "It seems your opponent doesn't want to fight you. This is your chance to convince them to join your side. One wrong move and combat will begin."

        show mariko cry

        n "I'm not going to fight anyone."

        hide mariko cry

        menu:
            "Where's Hiro":
                jump chapter1_boss_intro
            "I'm no coward":
                jump chapter1_boss_intro
            "You're hurt":
                pass

        show mariko cringe

        n "We both know you're in no position to fight right now. If you keep pushing yourself like this, you're going to pass out again. Wait, is this why you've been freaking out about not having enough time? Do you think something's going to happen to you?"

        m "They found this place and where I live, they even know where my friends are. I have every right to be scared. I'm not being paranoid."

        hide mariko cringe

        menu:
            "I can help":
                jump chapter1_boss_intro
            "Let's find the teachers":
                jump chapter1_boss_intro
            "It's not your responsibility":
                pass
        show mariko cry

        n "You don't have to take on everything yourself. No one's blaming you for what happened, but trying to fix things by yourself, it just makes things worse."

        #[If Vision > ?] For later ...
        #
        #n "Believe me, I've tried to get this right so many times."

        m "Don't you think I know that!? My original squad is gone, and even though I know they made their own choices, that doesn't help either. Nothing I do is working, but I can't stop trying. What else am I supposed to do?"

        n "Let us help you. You've been fighting alone for too long. Tell us where Hiro is so we can get you out of this mess."

        hide mariko cry
        show mariko judge

        m "...Okay…"

        "She snaps her fingers again, signaling to Rei and Setsuna to go to the scoreboard."

        show uitto cringe at left

        u "About time. What's their damage anyway?"

        hide mariko judge
        show mariko upset talk

        m "I'm not allowed to say. Honestly, if Hiro hadn't cooperated, I would have been in more trouble than I already am."

        show jona frustrated at right

        j "He turned himself in?"

        hide mariko upset talk
        show mariko cry

        m "...Yeah. He didn't want you guys getting in trouble because of him. I guess that's the one thing we can agree on... Once the teachers find out about what happened, I might not see you for a while."

        hide mariko cry

        "She turns and walks off the field, not wanting to face Hiro after what she's done. Both cheerleaders are having to support his weight as they bring him to us."

        hide jona frustrated
        show jona mad at right

        j "Is he awake? What the hell happened?"

        show hiro guilty

        h "I'm awake, it's just hard to move with all this crap they put on me."

        hide jona mad
        hide uitto cringe

        show rei depressed at right
        show setsuna at left

        re "I'm so sorry, Hiro. I honestly don't know what to think anymore."

        s "We should go talk to Principal Thani. I'm sure these guys can handle taking care of Hiro."

        "Rei hesitates a moment before letting him go and following in Mariko's footsteps."

        hide setsuna
        hide rei depressed

        show uitto talk at left

        u "Can we really trust them?"

        hide hiro guilty
        show hiro beans

        h "Are you kidding? I thought they'd never leave."

        "Uitto and Jona fuss with the overlapping belts as he speaks."

        hide hiro beans
        show hiro serious

        h "I never thought Mariko would resort to something so underhanded. Guess all that self righteous talk was just that, talk."

        n "I could have told you that. I can't believe after all we went through, you'd just turn yourself in like that."

        hide hiro serious
        show hiro sad talk

        h "Because it's my fault we all got stuck here. If I hadn't convinced people to put on those helmets, things wouldn't have gotten so bad."

        hide hiro sad talk

        if Villain >= Hero:

            show hiro insulted

            n "That doesn't mean you should throw yourself to the wolves. What if you'd actually gotten hurt?"

            h "....."

            show jona mad at left

            j "You could have told us what you were doing instead of running off on your own again."

            h "....."

            show Uittosadtalk

            u "Guys, quit ganging up on him. What matters is nothing serious happened, at least not yet. We should check out that tape before the teachers find out about it."

            hide hiro insulted
            hide jona mad
            hide Uittosadtalk

            jump chapter1_boss_player_choice

        show jona mad at left
        show hiro mad
        show uitto sigh

        n "It's not like putting them on was your idea to begin with. Besides we- I wasn't completely honest about what they did."

        j "Nagen!"

        n "But it's true. I thought if you knew how… complete the brainwashing was, you wouldn't go through with it, so we lied. All of us did."

        h "But I did know. I'm not stupid, Nagen, I could see what was happening out there. I just convinced myself it would all be worth it in the end. I wanted to believe we're the good guys."

        u "We are the good guys! Don't let all this mess with your head. Good guys make mistakes too."

        n "And right now, we gotta figure out who's behind this. Hopefully, that tape will give us some answers."

        hide jona mad
        hide hiro mad
        hide uitto sigh

        jump chapter1_boss_player_choice

    if mRep >= 10:

        show mariko cry

        m "I promised, didn't I? ‘No matter what happens, I'll protect you.'"
        m "This is the only thing I can do right now."

        hide mariko cry

        jump mariko_bonus_scene

label chapter1_boss_intro:
    
    m "I gave you a chance to run. It's not my fault you didn't listen to me."

    show backgroundwhite
    with dissolve

    hide backgroundblack

    hide backgroundwhite
    with dissolve

    "The stadium lights turn on without warning and once my eyes adjust to the blinding lights…"

    show screen boss_mariko_s1
    with dissolve

    m "Call me over ambitious, but if I'm taking over as leader, the whole team is going to need a massive overhaul."

    "She's covered in glittering mesh from the neck down, perched atop thin stiletto boots."

    n "Have you actually lost your mind? What do you mean taking over?"

    m "Isn't it obvious? I'm the new leader of the Junior Gladiators and you've been kicked off the team."

    "Long, thin blades pop out of her gauntlets, poised to strike."

    n "How the hell?"

    m "It's all plastic. I've been told it'll hurt just as much as real blades. Why don't we test that out?"

    n "I don't want to fight you."

    m "I'm afraid you don't have a choice."

    jump chapter1_boss_battle_initial

label chapter1_boss_battle_midfight_scene:

    "Wait, does she... want me to hit her?"
    
    n "This isn't going anywhere. Just give up already."

    m "Oh? But I've come too far to give up now. It's not like you're my target anyway. I just need you to teach him a very important lesson."

    window hide
    hide screen boss_mariko_s1
    with dissolve

    scene backgroundB5

    "The scoreboard that overlooks the field lights up, revealing where Hiro had been bound and gagged."

    m "How does it feel, Morine? Watching your friends get injured while you're helpless to do anything about it?"

    "I attempt to knock her out while she's distracted, but when I hit her..."

    h "Mpmph!"

    scene backgroundB2

    m "Pretty neat, hunh?"
    m "Anytime I get hit, he feels it instead."
    m "Finally, my Proficiency will let me do something other than shield myself from reality."
    m "I can make him feel what they felt."
    m "What it was like to be one of your mindless minions."

    n "This isn't the same thing."

    scene backgroundmariko

    show screen boss_mariko_s1

    m "But it feels the same."
    m "We were awake inside those voiceless meat shields you turned us into."
    m "My squad felt every wound they took for you only to lie nameless in the streets."
    m "The world treats them like a footnote in your casefile!"
    m "I will not let their deaths be treated like a cautionary tale while the people at fault get to move on with their lives."
    m "They should have been here! Don't you understand that?!"
    m "Hiro sent them off to die because he was too scared to fight for himself and I will NEVER forgive him for that."

    n "He didn't know."

    hide screen boss_mariko_s1

    if Hero > Villain:

        #[CG of Hiro's Injury]
        scene backgroundfb11

        "Hiro never wanted anyone to get hurt. He would sooner get himself killed than let others fight for him. No matter how awful people were, he'd always make excuses for them. He wanted everyone to be happy."

        #[CG of Odori and Nagen flanking young Hiro, offering a gun.]
        scene backgroundfb5

        "So we lied to him about Lethe's predictions. We told him no one would get hurt as long as he did exactly what we told him. As crazy as our plan was, he never could figure out how to tell us no."

        #[CG of Hiro blocking out the world with headphones]
        scene backgroundfb2

        "After people started to die, he shut everyone out. Despite our best efforts to hide the truth, I could see him counting how many people made it back every night. He blamed himself for everything going to shit."

        #[CG of Hiro surrounded by monitors of the destroyed city]

        scene backgroundB4

        "When the Proficiency Management Committee demanded for our leader to surrender, Lethe met them in his stead."

        #[Same CG in full color, with scribbled out scenes]
        scene backgroundB3

        "HIe bdloanmtewd hainmtsteolsf feoer htehr diesa!t!h."

        #[Return to previous CG]

        scene backgroundB4

        "He tried to face the people responsible head on... and lost. I thought I'd never see him again."

        # Back to Boss Arena
        scene backgroundmariko

        show screen boss_mariko_s1

        n "The only reason Hiro came to you was to stop anyone else from getting hurt, including you. He already felt guilty for what happened. What more do you want?"

        m "I want to guarantee my friends' safety. Your pretty words aren't enough to save anyone."
        return
    else:
        #[CG of Hiro's Injury]
        scene backgroundfb11
    
        "Hiro wanted to see the good in anyone, even when they hurt him. It made him easy to manipulate. If I so much as looked disappointed, he'd immediately cave. It's why he made such a wonderful puppet."

        #[CG of Odori and Nagen flanking young Hiro, offering a gun.]
        scene backgroundfb5
    
        "We'd feed him our ideas and Hiro would blindly spread them to anyone who'd listen. As long as he thought he was in charge, it didn't matter what we said, he'd still do it. After all, it's a leader's job to make the hard decisions."

        #[CG of Hiro blocking out the world with headphones]
        scene backgroundfb2
    
        "After his father was out of the picture and Lethe passed, we were all he had left. It was kind of pathetic watching him talk to the brainwashed soldiers like they would answer him."

        #[CG of Hiro surrounded by monitors of the destroyed city]

        scene backgroundB4
    
        "When the time came, he served his purpose as our figurehead. Everyone associates his face as the mastermind behind the attacks. Even now, he's taking the blame in our place, all of his own volition. He's too useful of a pawn to throw out like this."

        #[Return to Boss Battle arena]
        scene backgroundmariko

        show screen boss_mariko_s1
    
        n "It's not Hiro's fault people trusted him more than you, Mariko. You're only making things worse by picking a fight you will lose."

        m "As long as I breathe, I'm not done fighting. I'll leave you with scars that will outlive me."
        return

label chapter1_boss_spare:
    
    "I know she wrecked havoc, but I really can't kick a person while they're down."

    n "Rei, Setsuna; let my friends go. I'm- We aren't going to hurt her."

    j "Are you joking!?"

    u "Look at her, she's a mess. Nagen can handle her, we need to worry about Hiro."

    "It seems like they aren't going to move at first, but soon Rei releases Uitto in tears."

    re "Uitto, I'm so sorry! I- Setsuna, are you still...?"

    "Setsuna slowly releases Jona, her hands shaking."

    s "How could I let this happen?"

    re "Go get help. I'll stay here."

    "Uitto and Jona run to free Hiro while I stare down my opponent."

    n "There's no way you prepared all of this by yourself in five days. Who told you we were coming here?"

    m "I- I can't tell you. If I say something I shouldn't, they'll come after Rei."

    re "Mariko, I'm more than capable of fighting for myself. You shouldn't have gone behind our backs like this, this isn't helping anyone."

    m "...I left a tape in Hiro's locker like I was told, that's the only thing I can say. Even if you hate me, don't let them get my friends."

    n "No one's ‘getting' anyone. Though it looks like you're in serious trouble with the school."

    m "Nagen, school is the least of our worries."

    "The teachers quickly detain Mariko and her friends for questioning."

    jump chapter1_tape_scene

label chapter1_boss_punish:
    
    n "Of course I'll forgive you, you provided valuable entertainment for everyone."

    m "What are you talking about?"

    n "When you tell people what you plan to do, they can make other arrangements. Like, say, borrowing a few burner phones for a special school-wide stream. Of course, there's no audio, but that kind of works in my favor. Especially when I've been super calm about everything and you're bawling your eyes out after attacking me with knives. It's not a good look for you."

    m "So? Everyone knows what kind of person you are."

    n "True, but you're the psycho stalker that broadcasted a threat letter to everyone and lashed out at me and your own friends. At best, you'll be ridiculed, at worst, expelled. Either way, no one's going to believe you."

    m "No one believed me before. I know who you really are and I know I made the right decision."

    m "All I can do is hope my friends don't fall for your bullshit a second time."

    "Mariko snaps her fingers and in an instant, my friends are let go. I can see Setsuna running as far from the field as possible out of the corner of my eye. Uitto and Jona run to help Hiro while Rei lingers behind."

    re "After everything that's happened, I can't believe you'd put us through this again... You..."

    re "You both really need help."

    "She turns her back on us and runs to meet the teachers that are coming."

    m "This was the best I could do."

    "The teachers quickly detain Mariko and her friends for questioning."

    "Vivaldi lingers behind, emotionless and ever watchful."

    v "You all have to come too."

    n "What!? I'm the victim here!"

    v "That's what everyone thinks when they're in a fight."

    v "I'll talk with the others later. For now, you'll have to come into my office."

    n "But-"

    v "Do you want someone to listen to your side or not?"

    n "...Fine."

    "I spend over three hours in her office explaining everything in detail. In the end, she says nothing and sends me away."

    "I don't think I'm in trouble, at least not directly, but I'm definitely worried she'll call my fosters and tell them what happened."

    jump chapter1_tape_scene 

label mariko_bonus_scene:

    #(Chapter 1, prior to the tape scene? If Mariko = MAX)
    #[BG: Grey watercolor. POV Mariko.]
    scene background_Mfb1
    
    m "I always used to think I was invincible, but my parents treated me like I was made of glass."
    m "I couldn't go anywhere without them shadowing me. That meant no sports, no clubs, and no school with friends for six whole years."

    scene background_Mfb2
    #[Mariko on the couch in front of a TV. Tall shadows stretch behind her and over her head. As Estella talks, the background shifts to a lighter grey and the shadows shrink.]
    e "So you think your child has exceptional abilities? At Estella Academy, we tailor our curriculum around your child's... special attributes."

    M"Finally released from my bubble, I leapt at the chance to talk to kids my own age."

    scene background_Mfb3
    #[Mariko surrounded by silhouettes of the cheer squad]
    M"Most of the girls in my class were in cheer, so I joined too. Even without auditioning, I was named captain of the squad."

    Hiyoko "We can test out the moves to make sure it's safe before you try."

    Ty "I'll be your spotter!"

    Kiki "Everything will come naturally if you practice right."

    re "I can tell you when you've hurt yourself if you tell me when I should take a break; deal?"

    m "But when the riots started…"
    
    scene background_Mfb4

    #[Same formation, but Mariko's blocking the exit to a building. There's fire outside.]
    
    m "If you walk out this door, you're off the team!"

    Kanon "Who cares!? The only reason you were made captain was because your parents didn't want you doing any routines!"

    re "Everyone's scared. If Hiro found some place safer to hide, then I think we should believe him."

    m "Fine, don't listen to me! I don't want a bunch of liars on my team anyway!"

    scene background_Mfb5

    #[Scene fades; Mariko's running through the city.]

    m "I can't physically feel pain."
    
    m "But when I found Kanon, it felt like a shotgun to the chest."
    m "With each breath I took, the shrapnel dug into my lungs and my resolve shattered."
    m "My mind became like a broken record."

    m "Move."

    m "Survive."

    m "Find them."

    m "As each of my friends became a name on a list, I struggled to form rational thought."

    m "Move."

    m "Survive."

    scene background_Mfb6

    #[Mariko at the school, still running]
    
    m "We were rescued, those of us left, and I was asked to find a 'new normal'."
    m "The shattered feeling dulled, but it never left."
    m "I combed through my old phone looking for their voices, for evidence they were there."
    m "Anything as long as I kept moving."

    scene background_Mfb7

    m "Except I didn't know what I was moving toward anymore."
    m "When did the enemy I had to fight become my own body?"
    m "When did my will to fight gain a will of its own?"
    m "How do I make the pieces of my life fall back into place?"

    scene background_Mfb8

    #[CG of Mariko in a hospital looking room, mirroring the CG of her on the couch.]
    
    m "How long have I been running in circles?"

    jump chapter1_boss_player_choice

label chapter1_tape_scene:
    #[BG: Outside the Dorm]
    
    "After all was said and done, Mariko was the one who got in trouble and the rest of us were let go. We still haven't told them about the tape. After all, we don't even know what's on it. I wanted a chance to talk to Hiro before the others come meet up with us to watch it. Hiro doesn't seem so thrilled."

    h "You wanted to yell at me too?"

    n "I mean, I could, but I figured Uitto had that covered. You really worried us."

    h "Believe me, I know."

    h "Mariko's already taken care of, so can you please put away the kid gloves?"

    h "We've been apart for two years, but you all act like you're the only ones who got older."

    if Villain >= Hero:
        n "I figured you'd run your ideas by us before running off and doing something stupid, y'know, like you're supposed to."

        h "And I figured you'd respect the decisions of your old commander instead of undermining me at every turn."

        h "I'm not stupid, Nagen, I know what you've been up to."

        n "What do you mean?"

        "He looks so disappointed, then swallows like he took a bitter pill."

        h "We came here for a fresh start."

        h "I really don't like seeing you act like this when there's no one to impress. It makes it really hard to defend you."

        n "Why are you lecturing me? No one got hurt in the end, not permanently. I just wanted to make sure you were safe."

        h "....."

        n "Hiro, come on, I'd never do something if I thought it would put you in real danger."

        h "I know."

        n "We won. Now's the time to celebrate."

        h "...yeah."

        "He's not back to his usual self yet. Maybe that girl roughed him up more than I realized."

        h "I really hope things change."

        n "Of course they will. Everything just takes a little time."

        return

    #[Return to Main Branch]
    #[If Hero]
    else:
        n "Well, someone's gotta look out for your wellbeing. You're practically addicted to taking the blame for things that have nothing to do with you."
        n "You're not responsible for everyone's happiness, especially if trying to make everyone happy is going to get you hurt."

        h "Says the guy who jumped into a fight that had nothing to do with him."

        "That's different. She said all our names on the intercom and... and I never told you the truth about what the brainwashing would do."
        "I didn't want to scare you away from the plan."

        h "......"
        h "I'm not stupid, Nagen."
        h "I knew what we were doing was bad. I just- I wanted to believe the ends would justify the means."
        h "In the end, it looks like we hurt more people than we helped."

        n "We'll never know that for sure. Nothing would have changed if we didn't do something."
        n "I think we helped people, and we still can, even now. That's why we can't let this shake our resolve."
        n "Wishing you could do better, that's how you know you can do better in the future."

        h "No one cares that we're trying."

        n "You care, don't you? That's all that should matter. Fuck the people too impatient to wait."

        return