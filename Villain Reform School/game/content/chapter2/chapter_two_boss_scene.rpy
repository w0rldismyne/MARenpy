label chapter2_boss_scene:
    #"Ch 2 Boss Battle"

    #BG: Gym Dark

    scene backgroundCh2_RiseArena:
        yalign 1.0 xalign 0.0
        linear 4.0 yalign 0.0 zoom 0.75

    pause

    "The main lights in the gym are off, but it's not completely dark. The pool is open. Instead of water, there's... furniture?"
    "Large, ornate antiques that would look more at home in a mansion than a gym are haphazardly stored in the empty pool."

    r "Your cries for attention have fallen on deaf ears, Jona. Quit drawing this out and come out of hiding."
    r "It is depressing to watch, especially when no one is bothering to look for you."

    "I see a flash of blond hair between the furniture. Jona must be in there somewhere too."
    "It hasn't been that long since the sketchbook incident; what if he shut down again?"

    n "You don't speak for us. Of course we're looking for him."

    r "Nagen?"

    "She effortlessly hops onto a dresser with a far off look in her eyes."

    r "I see. Well, this is rather disappointing. I had hoped someone else would be baited here instead. Serves me right for aiming for two birds with one stone."

    scene backgroundCh2_RiseReveal

    "She snaps her fingers and the doors behind me lock. I can feel her watching me even though her eyes aren't focused."
    "The sudden sound of an engine startles me. Not as much as watching Rise fly up into the air, a jet pack strapped to her back."

    n "How did you...?"

    r "Impressive, no? It seems this gym was being fitted for simulations of some kind before the funding ran dry."
    r "I stumbled across it when they were putting my things in storage."

    "I text Uitto and Hiro to get help."

    n "Let us go."

    r "Us; that I cannot do, but perhaps an arrangement of some kind can be made?"
    r "I dispose of the two-faced snake hiding in the grass and in return, you can help me reclaim my father's business. Everyone wins!"

    n "Everyone except Jona. I'm not selling him out just to get out of here."

    r "You are so afraid of change that you keep clinging to these selfish people."
    r "Nagen, they are taking advantage of your desire to be needed and giving you nothing in return."
    r "I know how painful cutting ties with such people can feel, but once you experience that freedom, you can live for yourself."
    r "I promised to help you; let me keep that promise."

    #Insert negotiation here

    n "You're only trying to help yourself."

    scene backgroundCh2_RiseCloseup

    r "I am sure it seems that way, but I assure you, this is what's best for everyone."
    r "You saw the things he drew; it is the same twisted imagery that inspired that cult."
    r "Nothing has changed. I wish you would listen to reason, but it seems we're at an impasse."

    "She reaches behind her and pulls out a crystal perfume bottle."

    j "Nagen! Run!"

    "She immediately turns toward the sound of Jona's voice and throws the bottle."

    #SFX: Explosion

    "A GRENADE?!"

    r "Quit hiding behind my things you little- Ah well."

    "She pulls out two more and looks back at me."

    r "I apologize, but this will hurt a bit."

    show backgroundCh2_RiseCloseup with dissolve:
        zoom 1.0
        linear 0.5 zoom 2.0

    "I dive into the maze of furniture for cover. The walls of the pool glow as I run to get out of sight."

    window hide
    show backgroundblack with dissolve

    hide backgroundCh2_RiseCloseup

    show lfr1 with Dissolve(4.0):
        subpixel True
        xanchor 0.5 yanchor 0.5
        xalign 0.5 yalign 0.5
        zoom 1.2
        pause 2.0
        linear 1.0 zoom 1.0

    show backgroundblack zorder -1

    show mazerose zorder -1 with Dissolve(0.2)

    hide backgroundblack

    jump chapter2_boss_battle_initial

#------

label chapter2_boss_battle_midfight_scene:

    scene backgroundCh2_RiseReveal2
    "Rise's jet pack stutters. Maybe it started to overheat? She descends to the pool's edge."
    scene backgroundCh2_RiseReveal2_Zoom
    "Jona crawls out from his hiding place and tries to signal for me to run."

    "But Rise's still armed and guarding the stairs out of the pool. It's too risky to climb out now. Where are the others?"

    j "If this is about your parents, I don't know who they are."

    "Jona, what are you doing?!"

    r "Liar! His last name is Oshima, as in Oshima cosmetics. My dad funded the company and my mother modeled for them."
    r "Then he has the gall to stir simpletons into a frenzied mob with his art and have them target my family! My home!"
    r "You villainized your own kind and dare to act as if it wasn't your fault people got hurt."

    "Jona's pieces may have lashed out against the upper class, but they made plenty of enemies before him."

    #IF Villain

    if Villain > Hero:

        scene backgroundmazemidfight

        show jona mad at left
        show rise boss guard sad at right

        j "You're still okay, aren't you? If I hated your family so much, do you honestly think I would've let you live?"
        j "It's not my fault your parents funded Estella's experiments or stole businesses or made bad laws to protect themselves."

        r "They weren't trying to protect themselves, they were protecting me!"

        n "They... they funded my dad's research?"

        "There's no way..."

        n "You're a Charm Major... but, what's your Proficiency?"

        show rise boss guard sad tears at left

        r "I... I don't have one."

        "It was for her?! That painful medicine... They treated me like a guinea pig to make drugs for rich people?"

        show rise boss guard smile at left

        r "I could have before, when my family still had its influence. This furniture is all I have left."
        r "Everything else was stolen because of him."

        n "He didn't do anything to you."

        show rise boss guard glare at left

        r "I'm living my parent's worst nightmare because of his propaganda, even though I did nothing to deserve it."
        r "If I'm going to be punished regardless, I might as well get what I want. Isn't that what you did?"

        hide rise
        hide jona
        #Jona's CGs shown in reverse order, one image per sentence

        scene background_JFBMeet2

        "We just wanted to be the heroes for once. To finally be the ones in control of our own life, our own happiness."
        
        scene background_JFBUniform
        
        "All playing by the rules got us was more suffering. We would have been happy to stay with Lethe for the rest of our lives."
        
        scene background_Jfb9

        "But they took her from us. So much has already been taken from us by these privileged assholes. What more could they possibly want?"

        scene backgroundCh2_RiseCloseup

        j "All I want is to make sure my friends have happy lives. If you can't accept that, then it's too much of a risk to keep you around."

        r "S-see Nagen! See what happens when that innocent mask starts to crack?"

        n "Of course; who do you think taught him how to 'play nice'?"

    #IF Hero
    else:
        scene mazeeyes

        show rise boss attack smile at left
        show jona mad at right

        n "They were corrupt people, Rise. They hurt more people maintaining their power than Jona ever could have."
        n "You're smart enough to know that."

        r "Yes, but they were corrupt people I had control over. Now my father's companies are in the hands of strangers."
        r "Strangers who saw your fathers research and put more money into it instead of shutting it down."

        n "That's impossible. I destroyed the lab, I know I did."

        show rise boss guard talk at left

        r "It won't be long before they rebuild elsewhere under a different name. Only now, I have no way to stop it."
        r "There are going to be more children like us while I'm stuck waiting to come of age. We can stop it, if Jona fails out of the program."

        "So she was trying to get him to drop out!"

        j "You'll say anything to get him on your side, but it's not going to work."

        n "Who told you to target Jona?"

        show rise boss guard growl at left

        r "The same person who contacted Mariko. I imagine there are others as well; hired help to do her dirty work."
        r "The reward was too much to ignore. It's a simple trolley problem: the unhappiness of one for the safety of many."

        hide rise
        hide jona
        #Jona's CGs shown in reverse order, one image per sentence

        scene background_JFBSleebover3
        "I promised Jona that I'd keep him safe."
        scene background_JFBMourn
        "He doesn't have anyone else to rely on. If I turn my back on him, he'll have no one."
        scene background_Jfb10
        "Everything he's done, it was for someone else's happiness. If she asked, he may have left on his own just to protect us."
        scene background_Jfb5
        "Instead, she tried using his art to drive a wedge between us."
        scene background_Jfb3
        "No matter her end goal, she's needlessly making someone suffer for her own gain."

        #riseCG

        scene backgroundCh2_RiseReveal2_Zoom

        r "It seems you've made up your mind."

        n "I trust him more than I trust you."

    return

label chapter2_boss_battle_tile_event1:

    r "I tried to end things civilly, but you've left me with no choice."

    n "I'm not going to let you lay a finger on him. We both know you wouldn't risk ruining your precious stuff."

    r "Of course not. I don't have to hurt him, he'll do it himself. A little birdy told me this might trigger something."

    "She holds up an old paint-covered flip phone. It looks like the one Jona had when he ran away from home."

    phone "First unheard message: I have told you a thousand times you are not allowed to leave this house without permission. Are you trying to make me look like a bad mother?!"

    "No, there's no way- but Jona's already shaking."

    r "She was so worried about you and you ghosted her in the middle of a city wide riot. All of us thought you were dead."

    "The walls, did they always have those eyes? Everywhere I look, they're staring at me as if she's watching us."
    "She takes to the sky once more to stay out of reach."

    r "It would have been easier if you were."

    return

label chapter2_boss_battle_tile_event2:

    phone "Second unheard message: Just tell me where you are, I'll come get you. It's dangerous out there, you could get hurt."

    return

label chapter2_boss_battle_tile_event3:

    phone "Third unheard message: Where the hell are you? Do you think this is funny? I don't care about what your stupid little friends talked you into doing. Call me back."

    return

label chapter2_boss_battle_tile_event4:

    phone "Fourth unheard message: ...I hope you're happy. After all I've done for you, this is how you thank me?"

    return

label chapter2_boss_spare:
    #"Rise's End Good (+Rep +Hero)"

    phone "Fifth unheard message:"
    phone "..... Don't come home....."

    scene backgroundstatic

    r "That's strange, this one goes on for twenty minutes."

    "It sounds like the phone got dropped on the floor on the other end of the line."
    play sound "banana hits face 1.ogg"

    scene background_JFBCouch2
    with dissolve
    pause

    "What sounds like a chair moving follows shortly after."
    play sound "848683__al3x-k__sfx_chair_scrape_02.ogg"

    scene background_Jfb10
    with dissolve
    pause

    scene backgroundstatic

    play sound "fall.ogg"

    phone "CRASH!"
    
    play sound "choke.ogg"
    window hide
    show backgroundJonaDraw8
    with dissolve
    pause

    "A sick feeling pools in my stomach."

    n "Rise, turn it off."

    "Someone starts gasping for air."

    n "RISE TURN IT OFF!"

    stop sound

    scene backgroundgym with darker

    show rise boss attack frown at left
    show jona depressed at right

    "She throws the phone down as if it had bit her, all color drained from her face."
    play sound "banana hits face 1.ogg"
    "I run to turn it off as fast as I can."
    "Jona is shuddering with sobs. He had gone back to his house during the riots. We never talked about why."

    show rise boss guard sad at left

    r "Nagen, I didn't know- Why would she give me something like that?"

    n "I'm not the one you should be making excuses at!"

    "The doors finally open and thank God, there are teachers. Hiro runs around to the steps, but Uitto's quicker."

    show uitto yell

    u "Nagen, get away from him."

    "She wraps him in a hug so tight I think she might crush him."

    show jona frustrated at right

    j "I'm sorry! I couldn't stop it. I couldn't-"

    show uitto sad

    u "Hey, I'm not mad, no one here's mad. It'll pass. I'm just glad you're safe."

    "Rise surrenders herself willingly. She still looks sick."

    show rise boss attack frown at left

    r "The walls have eyes, Nagen, and not just these ones. Be careful who you trust."

    "She pulls a drawing out of her blouse and throws it toward me."

    hide rise
    hide uitto
    hide jona 
    "Professor Inukai starts to walk her to the principal's office while Mr. Yaguchi disables the glowing walls with a strange looking key."

    show yaguchi mad

    ya "If you don't want to get closed into the pool, get the hell out of there."

    "As if this is our fault?! Hiro and Uitto help get Jona out of the maze. I linger behind and unfold the picture."

    hide yaguchi
    #CG: Jona's Portrait
    show backgroundJonaDraw4
    pause

    "An eye for an eye? And a locker combination."
    "I'll have to check Rise's locker when no one's around. But this drawing... is this how Jona sees himself?"

    hide backgroundJonaDraw4
    #Hide CG

    #Return to Main Branch

    return

    #"Rise Bad End (+Villian)"

label chapter2_boss_punish:

    scene backgroundCh2_RiseCrash
    "I can't hear anything over the sound of her screaming. Something smells like it's burning."

    # BAD END starts here

    "She keeps rubbing at her eyes only to curl in on herself... No way, are those things really connected to her?"
    "Jona walks over to the phone where she dropped it and crushes it under his boot."

    j "Serves you right for meddling in things you don't understand."

    scene backgroundgym with darker

    show sato annoyed
    show rise boss guard tears at left

    "The doors to the gym finally open. Miss Sato storms in with a look that could kill."
    "She waddles down to where Rise is crumpled on the floor and leans her a hand. Rise has to be led out."
    "I don't think she can see where she's going. Miss Sato glares at us, then whispers something in Rise's ear."

    hide sato
    hide rise
    show uitto sad at left
    show jona depressed
    "Uitto and Hiro motion for Jona and I to climb out of the pool, but something on the floor catches my eye."
    "Rise must have dropped it during the fight."

    hide jona
    hide uitto

    #CG: Lethe's Portrait

    window hide
    show backgroundJonaDraw5
    pause

    "This is it! This is the last picture Jona drew of Lethe before she died."
    "The aura around her, it reminds me of how he described his mom. And those scars on her arms..."

    hide backgroundJonaDraw5

    #CG circles through the burial briefly before disappearing

    show jona mad
    j "Nagen, don't look at that!"

    "He takes the portrait from me. On the back is a locker code."

    j "She..."

    "The picture creases under his grip, but it seems he can't bring himself to destroy it like the other pictures."

    show jona depressed

    j "This isn't how she'd want you to remember her."

    n "I know."

    "But what was Rise doing saving it? Most people wouldn't want her image anywhere near them."

    n "You don't have to keep babying me about it."

    show jona frustrated

    j "Yeah, well, two years isn't enough time."

    h "Isn't enough time for what?"

    show jona depressed

    j "Nothing."

    "He hesitates when he sees Uitto."

    show uitto sad talk at left

    u "Are you okay?"

    j "...No. Are you?"

    u "Not especially, but-"

    show yaguchi mad at right

    ya "Hey! If you don't want to get locked in here, get the hell out!"

    h "Yes sir!"

    hide yaguchi
    hide uitto
    hide jona

    #Return to Main Branch

    return

    #BG: Hallway

    #CONVERGENT ENDING
