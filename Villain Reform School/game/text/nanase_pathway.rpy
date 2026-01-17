label NanaseVisit:

    if uTurn == 0:
        jump Nanase1
    elif uTurn == 1:
        jump Nanase2
    elif uTurn == 2:
        jump Nanase3
    elif uTurn == 3:
        jump Nanase4
    else:
        jump NanaseF

label Nanase1:  
    scene backgroundstuco

    nk "Hunh? Oh… I mean not really, why?" 

    n "Wanna’ hang out." 

    nk "S-sure!" 

    "She stared at me expectantly, and a little lost. To be fair, I might have looked the same way. I should probably say something."

    menu:
        "What are your hobbies?":
            $ Vision += 1
	
            nk "Hunh?" 

            n "What do you like to do in your free time?" 

            nk "Umm… I guess cleaning?" 
            nk "I do that a lot. I’ve never really thought about it though."

            n "Never thought about having fun?" 

            "She faltered and tried to back track."

            nk "That’s not what I meant!" 
            nk "I mean I’ve always spent my time trying to better my chances at getting into a good career…"

            "Her energy deflated before she finished her sentence."
        
            nk "So, I guess I don’t usually think about having fun." 
            nk "I mean, there’ll be time for that when I’m an adult right?" 
            nk "I should just focus on my goals now. The rest will sort itself out eventually."

            n "If you can’t figure out how to balance that stuff now, what makes you think you’ll have time to do it when you have a job?" 

            nk "W-well… I really don’t know where to start." 

            n "What do you like?" 

            nk "I don’t know. Pandas are kinda cute." 

            n "There you go, find something to do with pandas." 

            nk "Okay! Yeah. I can do that." 

        "What's with the sweater vest?":

            $ nkRep -= 1

            "She stares at me blankly."

            n "I mean, you’re already wearing a sweater. Isn’t it kinda redundant?" 

            nk "I get cold easily, okay. Besides, what goes better with a sweater than a sweater vest?" 

            n "Sweatpants. If you’re cold, try wearing pants." 

            nk "I just picked it because it was soft. Why do you care?" 

            n "Easy now. I was just making conversation." 

            nk "Yeah, well this was… uhh… interesting, but I should get back to work." 

        "What do you want to do?":
            $ nkRep += 1

            nk "I don’t know." 

            n "Well, what do you usually do with your friends?" 

            nk "Umm…" 

            "She stalled for time as long as she could."

            nk "Usually I’d watch them play games or something while I worked." 

            n "What about when you weren’t working?" 

            nk "Sleep." 

            "She picked up on my confusion."

            nk "I used to be a teacher’s aide." 
            nk "I’d grade papers, audit attendance records, revise lesson plans and all that." 
            nk "I didn’t have time to just hangout, especially with them bugging me for assignment answers." 

            n "If you loved being an aide so much, why aren’t you one now?" 

            "She bit her lip and avoided my eyes."

            nk "Well, the uh, the school and I agreed it would be for the best if I wasn’t a TA anymore…" 

            "Her shoulders slumped as she spoke."

            nk "I don’t really talk to them anymore. My childhood friends that is." 

            "I want to ask her why, but it seems personal."

            n "Why don’t we watch a movie or something?" 

            nk "O-okay." 

            "We hooked up my laptop to the classroom projector and watched Shanghai Bouncer. Lots of B-grade action scenes and pandas."
        
    nk "Umm… I don’t know if this is the best time for this, but you pursuing this anonymous threat letter has me concerned." 

    n "What else am I supposed to do?" 

    nk "Just let the teachers handle it." 
    nk "If you acknowledge their threat and go after them yourself, you’re going to make things worse." 
    nk "What if this jeopardizes your position on the student council?"

    n "I can’t just sit around and do nothing." 
    n "Just because they told me they’ll do something doesn’t mean I have to mindlessly obey their commands." 
    n "It’s called using your brain." 

    "She doesn't understand. The people who’d be coming for me wouldn’t be your average bullies. The person doing this could very well be a threat to everyone." 

    nk "I’m just trying to help." 

    "She glared at me, almost about to cry. I don’t think I’ve ever seen her this mad before. I mean, yeah I was kinda rude, but nothing deserving of such a steely glare. She stormed off without anothing word."

    return

label Nanase2:
    scene backgroundstuco
    nk "Yeah. Things to file, documents to shred."

    "Ouch, looks like she’s still mad about earlier. She turned her back on me and continued shredding documents. ...Wait a minute, shredding documents?" 

    "I picked up a form from the pile."

    nk "Hey!"

    "It was one of those student request forms. Whoever filled it out requested that I jump off the roof of the school."

    n "Are these all threat letters?"

    nk "Th-they’re just empty threats."
    nk "It seems the anonymity of the request form makes it easy to target people."
    nk "I find it best not to give a reaction."

    "She struggled to change the subject."

    nk "We’re really only interested in nominations for student council."
    nk "There’s actually quite a few-"

    n "Why are you doing this?"

    nk "Well I’m aiming to be class historian, so I figured volunteering to work on the election would-."

    n "I mean why are you shredding these?"
    n "Why are you going out of your way to get rid of these?"

    nk "Is it so hard to believe that someone just wants to help you?"

    n "Yes."
    n "I find it very hard to believe that someone would repeatedly go out of their way to help someone with my reputation."
    n "Especially when that someone has done nothing in return. It seems very fake."

    nk "Fake?"

    n "Sorry, probably not the best choice of words."
    n "Perfunctory would be more appropriate."
    n "I just don’t get this whole...whatever it is you think you’re doing."

    nk "I feel bad for you!"
    nk "I understand what it’s like to have a reputation."
    nk "My Proficiency is only as good as the person I’m assisting, so I only help the best of the best!"
    nk "I am doing everything I can, but I can’t even begin to help you unless you tell me what to do! So don’t you dare tell me that doing what you’re told is mindless, because it’s the only thing I’m good at!"
    nk "So… that genuine enough for you?"

    "In a flash, her confidence evaporated."

    n "Wait, that’s why you’re mad at me?"

    nk "My Proficiency is… Obedience. I need people to tell me what to do, or I fail."
    nk "I truly want to help you. I just don’t know how. I’m sorry."
    
    menu:
        "I didn’t ask for your help.":
            $ nkRep -= 1 

	        nk "Why are you making this so difficult?"

            n "You don’t have to be here."

            nk "You’re the one who came looking for me."
            nk "If you don’t want my help, then why are you here?"

            n "I’m just trying to blow off some steam, okay?"

            nk "Yeah? Well you have a funny way of doing it."
            nk "I… I just want to make people happy."
            nk "It’s one of the few good things that comes from having such a lame ability, and no one wants me to use it the way I want to."

            n "How is that my problem?"

            nk "It’s not. So don’t treat me like I’m a problem and let me do my job."

        "Reputation?":
            $ nkRep += 1

	        n "You have a reputation?"

            nk "I… Uhh… Oh jeez; me and my big mouth. I don’t know if I told you this already or not, but I used to be a teacher’s aide…"
            nk "…and I, uh, really liked my teacher."

            n "That’s it? That doesn’t sound so bad."

            nk "His wife didn’t seem to think so."

            n "Oh… Oh, wait, what? When did this happen? You’re like fifteen at the oldest."

            nk "It’s not what you think!"
            nk "Everyone else seems to think that too…"
            nk "I wanted them to think that, in the past that is."
            nk "As if having a teacher as my boyfriend made me better than them somehow. Now I’m that girl."

            n "I think that’s a little different from what I’m going through."

            nk "And what would that be?"

            "Wait a minute… does she not know?"

        "You shouldn’t get involved.":
            $ Intel += 1
 
            n "I know you mean well, but this isn’t something you should get involved in."
            n "It’s too dangerous."

            nk "Aren’t you the one making it dangerous?"

            n "I literally can’t help being a target at this point."
            n "All I can control is how I react to it."
            n "You’ll just get roped in with me if you keep interfering like this."
            n "You’ll ruin your chances at Class Historian at this point."

            nk "W-well you’ll ruin your chances at Student Council President."

            n "My chances are slim enough as it is."
            n "For all you know, this could make me go up in the polls. If not, then I’ll do something else."

            nk "No! You absolutely have to be Class President! If not then…"

            n "Then?"

            nk "Then Kaju would be the only candidate."

            "She shuddered, rejecting the idea with every fiber of her being."

            nk "I can’t let that happen. You’re by far the best choice we’ve got."

    n "Do you have any idea- Haven’t you heard about the Guwon Riots?"

    nk "Well, yeah, but what’s that have to do with anything?"
    nk "Unless… Oh. Were you one of the survivors?"
    nk "I’ve heard a few of them came here."

    n "You don’t recognize me?"

    nk "Is this some kind of trick question? Of course I recognize you…"
    nk "We’re friends, aren’t we?"

    n "No, you know what? Nevermind, it’s nothing."

    "I’m not going to botch a chance at being perceived as normal over winning an argument… yet."

    n "Look, I’m sorry, it’s just hard for me not to question people’s motivation."

    nk "I get it."
    nk "I do the same thing all the time. It’s hard to let people in."
    nk "But that doesn’t mean you have to shut people out entirely."
    nk "I’m here for you, if you need me."
    nk "You know where to find me."
    
    return

label Nanase3:
    scene backgroundstuco
    nk "No, but aren’t you?" 

    n "Uhh…" 

    nk "In the entire time I’ve known you, you haven’t made one move toward advancing your campaign." 

    n "I’ve been kinda preoccupied." 

    nk "If you can’t even be bothered to campaign properly, how do you expect the students to have faith in your commitment to the position?" 

    n "Well, it’s not like I’m doing nothing. I’m doing something right now." 

    nk "And that would be?" 

    n "Surveying?" 

    "She doesn’t seem even remotely impressed."

    menu:
        "Want to help?":
            $ nkRep += 1

	        "Her eyes lit up."
	
            nk "Well, since you asked." 
            nk "We need to get posters up; flashy, with a 6th grade reading level." 
            nk "A good election speech, short, lot’s of 3 word catch phrases. It really helps nail down your key message."
            nk "Oh, a few club endorsements wouldn’t hurt, and a faculty advisor… for starters."

            "She was talking at a mile a minute, but I’m guessing my eyes started to glaze over or something, because she’s slowed down."

            n "6th grade, really?" 

            nk "Average literacy levels are low sir, don’t underestimate the power of knowing your audience."

            n "But whatever shall I do without my superfluous adjectives?" 

            nk "I think you’ll live. Now, come on! Let’s go!" 

            scene backgroundMPath

            "I set up in the library with butcher paper and a handful of ‘borrowed’ markers from the council room."

            nk "They don’t allow food in the library, so it’s a good thing this stuff isn’t really food." 
            nk "Coffee isn’t even in a food group." 

            n "Due to its lack of inherit nutritional value, coffee is considered part of the other or oil group." 
            n "Though it is a leading antioxidant." 

            nk "Right, well I guess we can add detail oriented to your list of qualifications for presidency."

            n "Sorry, I know a lot of useless information." 

            nk "I don’t think it’s useless, you just have to find a way to put it to practical use." 

            n "That was almost convincing." 

            nk "Well you shouldn’t be so hard on yourself. You have an amazing ability. It’s way cooler than mine." 

            n "I get ice pick headaches if I remember stuff for too long and I get lost in thought for hours if I’m left alone."

            nk "I can’t cook, do laundry or do anything correctly unless someone else tells me to." 

            n "Isn’t that a little bit of an exaggeration?" 

            nk "Ever burned water?" 
            nk "No, I’m serious, I tried making tea once and it started smoking. I ruined the kettle." 

            n "Point made." 

            nk "It’s just lame, but if I work for an amazing person, maybe it’ll be less lame." 

            n "You’re working with one." 

            nk "D-don’t get cocky. You still have the potential to suck." 

            n "Wow." 

            nk "Sh-shut up and draw your stupid poster." \
        "What about you?":
            $ Intel += 1
	
	        nk "Hunh?" 

            n "What about your campaign for Historian? I haven’t seen you campaigning." 

            nk "That’s different, I’m running unopposed." 
            nk "Not a lot of kids are rushing to be a secretary." 

            n "I mean, that’s fair, but that doesn’t mean you shouldn’t try. Live by example and all that." 

            nk "Does that mean you’ll try harder, if I try harder?" 

            n "No, it means I’ll start trying if you start." 

            nk "Ugh, point made. I’ll run a proper campaign and so will you. Let’s do this!" 
        "Stand by your statement.":
            $ nkRep -= 1
	
            n "Yes surveying, hearing from the people, learning their problems and coming up with solutions." 

            nk "Okay then, I have a problem for you sir." 

            n "G-go on." 

            nk "I have a friend who claims to want responsibility, but does none of the things to earn it." 
            nk "How do I get my lazy running mate’s butt in gear." 

            n "Coffee." 

            nk "Wha~at?" 

            n "Buy him some coffee." 

            nk "Are you seriously asking me to bribe you into doing something you said you wanted to do?" 

            n "It’s worth a shot." 

            nk "Ugh, you’re no better than those idiots." 
            nk "If I wanted to be someone’s mommy I’d hang out with Kaz or Dyre again." 

            n "Hey! I’m a presidential nominee, not an advice columnist… I don’t know who you’re talking about." 

            nk "Two of the most immature dorks I’ve ever met." 

            "Harsh, and she’s the one who started it. Nagging me out of the blue like that, what gives?"

    "Even if we don’t always get along, the past few days I’ve spent with Nanase have felt surprisingly normal."
    "After everything that happened, I hadn’t expected to be able to just hang out with someone and work on school stuff again."
    "Still, I haven’t exactly been up front about why I’m here. I can’t keep pretending it’s because I don’t know how to start."

    n "Are you familiar with Estella Prep?" 

    nk "Yeah, I went there in middle school." 

    "Oh, so she does know."

    n "Cool… cool. Then, you were there, weren’t you?" 

    nk "Yeah… Nagen, what’s this about?" 

    n "I just had to check, y’know? You just seem so unaffected by it." 

    nk "I don’t remember much about what happened." 
    nk "The riots, it just feels like a giant blur to me." 
    nk "It just seems so surreal, I can’t help but feel disconnected." 
    nk "I know what happened, and it’s not that I don’t care, it just doesn’t feel real to me y’know." 
    nk "It just feels different remembering an experience as opposed to someone telling it to you." 
    nk "I try not to think about it." 

    n "Honestly, me too." 

    nk "It must be harder for you. You can remember everything." 

    n "I’m still trying to pull myself out of that way of thinking too." 

    "I’m still trying to figure out where to go from here, but it’s moments like these that are nice."

    return

label Nanase4:
    scene backgroundstuco
    "Nanase and I worked on our posters for a good couple hours, preparing for speeches and public speaking in general."
    "Nanase’s had a border of panda stickers and some crudely drawn books on her adverts. I tried my best to keep my letters the same size on the stupid thing."

    nk "-and then in episode 145, Pandeku crashed this underground speakeasy run by flamingos." 
    nk "There was this killer dance battle-" 

    "She’s been talking about Shanghai Bouncer non-stop since she got here. Unless I want a five paragraph essay on Pandeku’s season three character arch I need to change the subject."

    n "Uh, thanks again for helping out with the campaign and everything." 

    nk "Hunh? Oh, no problem, really. It’s nice to finally be working with someone, not for them." 
    nk "Really nice…" 
    nk "Do you think we would have been friends if we’d gone to the same school when we were kids?" 

    n "Don’t you mean the same class?" 

    nk "Hunh?" 

    n "We both went to Estella Prep, remember?" 

    nk "O-oh, right. Do you think we’d be friends if we were in the same class?"   
    
    menu:
        "Yes":
            nk "Y-yeah, me too. Maybe things would have turned out differently."
            $ nkRep += 1
        "No":
            nk "You’re probably right… but we’re friends now. That’s all that really matters."

    n "There’s actually something I’ve been meaning to ask you…"

    menu:
        "Why do you keep trying to help me?":
            $ nkRep -= 1
		    nk "Haven’t we gone through this already? I like helping you."

            n "Yeah you said that. You also said you could only do something right if you were told to…" 

            nk "Y-yeah… So?" 

            n "Did you want to help me? Or did someone tell you to." 

            nk "O-oh, you meant like that." 
            nk "Obedience is my Proficiency and you asked me to help, that’s why I’m so good at it." 
            nk "No need to be paranoid." 

            n "Yeah, after you insisted. You were the one who first came to me." 
            n "Why?" 

            nk "I mean, there a lot of reasons." 

            n "But was one of them being told to?" 

            nk "Does it matter?" 

            n "Yes. There is someone, isn’t there?" 
            n "Who?" 

            nk "I don’t know." 

        "Why do you keep calling me sir?":
            $ nkRep +=1 

            n "I’m not your boss or anything, you could just call me by my name." 

            nk "Uhh… Umm…" 

		    n "It’s not that weird." 

            nk "O-okay, I’ll try… Mr. Tesuta." 

            n "N-no. No, that’s not what I meant." 

            nk "I know! But, like, you’re going to be my boss if you win. It’s a respect thing." 

            n "Come on, we’re friends aren’t we?" 

            nk "Okay then, N-nagen." 

            n "See? That wasn’t hard at all." 

            nk "Easy for you to say!" 
            nk "I haven’t called anybody by their first name since elementary school!" 
            nk "It makes things easier." 
            nk "But if I’m going to be in this for the long haul, I need to commit." 
            nk "This is the ultimate sign of trust y’know, you’re not allowed to disappoint me now… Nagen."

            "I guess it’s a step in the right direction, but something about what she said seemed off."
        
        "Do you want to go out?":

            nk "Do you need some fresh air or something?" 

            n "I meant do you want to go out, on a date?" 

            nk "O-oh! Oh my goodness. Are you serious?" 

            n "Yeah." 

            if nkRep > 3:

                "In all the scenarios I had run through my head of how she’d react, I never imagined her crying."

                n "Hey, woah, are you okay?"

                nk "Y-yeah I’m okay." 
                nk "I’m okay… You really mean it?" 
                nk "You want to go out with me?" 

                n "Yeah, I’m not messing with you or anything." 
                n "Is that… That’s not a bad thing is it?" 

                nk "No, no." 
                nk "I’m sorry."  
                nk "I’m really, really happy." 
                nk "I didn’t think… I’m sorry I can’t stop crying." 
                nk "It’s like, I was hoping you liked me but I don’t feel like I deserve it." 
                nk "It’s stupid." 

                n "It’s not stupid at all." 

                "I really didn’t know what else to say at that point. I just kinda stood there, feeling useless while she calmed down."

                nk "You want to go out with me." 

                "She repeated it softly, reaffirming what I feel like I’ve repeated a few times now."

                n "Yeah. I’m, uhh, not sure where yet." 

                nk "That’s okay. I’m not terribly picky." 

                n "So that’s a yes then?" 

                nk "Ah! Yes, of course." 

            else:

                nk "That... wouldn’t be a good idea." 

                n "What do you mean? We make a great team. It wasn’t something I said, was it?" 
                n "I don’t want to pressure you into doing something you don’t want to do." 

                nk "No it’s not that I don’t like you…" 
                nk "I mean, I think I do. I just want…" 
                nk "I don’t want to hurt you…" 

                n "What makes you think you’d be hurting me?" 

    nk "I’m sorry, I just keep making things difficult by getting involved." 
    nk "I don’t know what I’m supposed to do anymore." 
    nk "I want to do everything I can to help you, but I’m not even sure what that means." 

    n "Nanase what’s going on?" 

    nk "Something just doesn’t feel right about this." 
    nk "I feel like I’ve kinda forced myself on you, and I feel really bad about it." 
    nk "I mean, I love that you started coming to see me." 
    nk "It made me feel needed, but what if that’s a bad thing?" 
    nk "What if I’m repeating the same mistakes over and over again and now I’m dragging you down with me?!" 
    nk "Or… maybe I’m just being paranoid." 

    "Nanase’s always been a little codependent around me."
    "I had just written it off as a side effect of having a limited number of friends."
    "I hadn’t considered it was something she was self conscious about."

    n "It’s okay, I’d tell you if you were bothering me." 
    n "I like hanging out with you." 
    n "If there’s anything I could do to help you, let me know." 

    "I watched as all emotion drained from her face. She stared at me blankly, maybe thinking something over, I’m not sure."
    
    #nk no emotion
    nk "I’m sorry, that request conflicts with 17 previous commands." 
    nk "Would you like to continue or override existing commands?" 

    n "Nanase, is this some kind of joke? What are you doing?" 

    #nk no emotion
    nk "Resuming. Please wait."

    #nk "normal"
    nk "I’m sorry for worrying you." 
    nk "I’m fine really, I just have a lot on my mind lately." 
    nk "It’s kinda hard to explain." 

    n "...right. Does it having anything to do with… whatever the hell that was?" 

    nk "I’m sorry, once I have a better idea of what’s going on, I’ll tell you." 

    "I mean, that’s good I guess, but what the hell was all that?"

    nk "I'm sorry sir, now's not a very good time." 

    return

label NanaseF:
    scene backgroundstuco
    "Nagase must be busy right now."
    return