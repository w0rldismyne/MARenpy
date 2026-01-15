label NanaseVisit:

    if nkTurn == 0:
        jump Nanase1
    elif nkTurn == 1:
        jump Nanase2
    elif nkTurn == 2:
        jump Nanase3
    elif nkTurn == 3:
        jump Nanase4
    elif nkTurn == 4:
        jump Nanase5
    elif nkTurn ==5:
        jump Nanase6    
    else:
        jump NanaseF

label Nanase1:  
    scene backgroundstuco

    n "Are you busy?"

    show nanase surprised

    nk "Hunh? Oh? I mean not really, why?" 

    n "Wanna? hang out." 

    hide nanase surprised
    show nanase embarrassed

    nk "S-sure!" 

    "She stared at me expectantly, and a little lost. To be fair, I might have looked the same way. I should probably say something."

    hide nanase surprised
    menu:
        "What are your hobbies?":
            $ Vision += 1

            show nanase condescending
    
            nk "Hunh?" 

            n "What do you like to do in your free time?" 

            hide nanase condescending
            show nanase talk

            nk "Umm? I guess cleaning?" 
            nk "I do that a lot. I've never really thought about it though."

            n "Never thought about having fun?" 

            "She faltered and tried to back track."

            hide nanase talk
            show nanase surprised

            nk "That's not what I meant!" 

            hide nanase surprised
            show nanase sad1

            nk "I mean I've always spent my time trying to better my chances at getting into a good career."

            "Her energy deflated before she finished her sentence."

            hide nanase sad1
            show nanase sad2
        
            nk "So, I guess I don't usually think about having fun." 

            hide nanase sad2
            show nanase sad smile

            nk "I mean, there'll be time for that when I'm an adult right?" 
            nk "I should just focus on my goals now. The rest will sort itself out eventually."

            n "If you can't figure out how to balance that stuff now, what makes you think you'll have time to do it when you have a job?" 

            hide nanase sad smile
            show nanase sad1

            nk "W-well, I really don't know where to start." 

            n "What do you like?" 

            nk "I don't know. Pandas are kinda cute." 

            n "There you go, find something to do with pandas." 

            hide nanase sad1
            show nanase smile

            nk "Okay! Yeah. I can do that." 

            hide nanase smile

        "What's with the sweater vest?":

            $ nkRep -= 1

            show nanase disappointed

            "She stares at me blankly."

            n "I mean, you're already wearing a sweater. Isn't it kinda redundant?" 

            nk "I get cold easily, okay. Besides, what goes better with a sweater than a sweater vest?" 

            n "Sweatpants. If you're cold, try wearing pants." 

            nk "I just picked it because it was soft. Why do you care?" 

            n "Easy now. I was just making conversation." 

            nk "Yeah, well this was... uhh... interesting, but I should get back to work." 

            hide nanase disappointed

        "What do you want to do?":
            $ nkRep += 1

            show nanase embarrassed

            nk "I don't know." 

            n "Well, what do you usually do with your friends?" 

            nk "Umm..." 

            "She stalled for time as long as she could."

            hide nanase embarrassed
            show nanase disappointed

            nk "Usually I'd watch them play games or something while I worked." 

            n "What about when you weren't working?" 

            nk "Sleep." 

            "She picked up on my confusion."

            hide nanase disappointed
            show nanase sad1

            nk "I used to be a teacher's aide." 
            nk "I'd grade papers, audit attendance records, revise lesson plans and all that." 
            nk "I didn't have time to just hangout, especially with them bugging me for assignment answers." 

            n "If you loved being an aide so much, why aren't you one now?" 

            "She bit her lip and avoided my eyes."

            hide nanase sad1
            show nanase sad smile

            nk "Well, the uh, the school and I agreed it would be for the best if I wasn't a TA anymore..." 

            "Her shoulders slumped as she spoke."

            hide nanase sad smile
            show nanase scold

            nk "I don't really talk to them anymore. My childhood friends that is." 

            "I want to ask her why, but it seems personal."

            hide nanase scold
            show nanase sad smile

            n "Why don't we watch a movie or something?" 

            nk "O-okay." 

            "We hooked up my laptop to the classroom projector and watched Shanghai Bouncer. Lots of B-grade action scenes and pandas."

            hide nanase sad smile
    show nanase

    nk "Umm... I don't know if this is the best time for this, but you pursuing this anonymous threat letter has me concerned." 

    n "What else am I supposed to do?" 

    nk "Just let the teachers handle it." 
    nk "If you acknowledge their threat and go after them yourself, you're going to make things worse." 
    nk "What if this jeopardizes your position on the student council?"

    n "I can't just sit around and do nothing." 
    n "Just because they told me they'll do something doesn't mean I have to mindlessly obey their commands." 
    n "It's called using your brain." 

    "She doesn't understand. The people who'd be coming for me wouldn't be your average bullies. The person doing this could very well be a threat to everyone." 

    hide nanase
    show nanase irate

    nk "I'm just trying to help." 

    hide nanase irate

    "She glared at me, almost about to cry. I don't think I've ever seen her this mad before. I mean, yeah I was kinda rude, but nothing deserving of such a steely glare. She stormed off without anothing word."

    return

label Nanase2:
    scene backgroundstuco

    n "Are you busy?"

    show nanase irate
    nk "Yeah. Things to file, documents to shred."

    "Ouch, looks like she's still mad about earlier. She turned her back on me and continued shredding documents. ...Wait a minute, shredding documents?" 

    "I picked up a form from the pile."

    hide nanase irate
    show nanase offended

    nk "Hey!"

    "It was one of those student request forms. Whoever filled it out requested that I jump off the roof of the school."

    n "Are these all threat letters?"

    hide nanase offended
    show nanase irate

    nk "Th-they're just empty threats."
    nk "It seems the anonymity of the request form makes it easy to target people."
    nk "I find it best not to give a reaction."

    "She struggled to change the subject."

    hide nanase irate
    show nanase scold

    nk "We're really only interested in nominations for student council."
    nk "There's actually quite a few-"

    n "Why are you doing this?"

    hide nanase scold
    show nanase sad1

    nk "Well I'm aiming to be class historian, so I figured volunteering to work on the election would-."

    n "I mean why are you shredding these?"
    n "Why are you going out of your way to get rid of these?"

    hide nanase sad1
    show nanase offended

    nk "Is it so hard to believe that someone just wants to help you?"

    n "Yes."
    n "I find it very hard to believe that someone would repeatedly go out of their way to help someone with my reputation."
    n "Especially when that someone has done nothing in return. It seems very fake."

    hide nanase offended
    show nanase ashamed

    nk "Fake?"

    n "Sorry, probably not the best choice of words."
    n "Perfunctory would be more appropriate."
    n "I just don't get this whole...whatever it is you think you're doing."

    hide nanase ashamed
    show nanase offended

    nk "I feel bad for you!"
    nk "I understand what it's like to have a reputation."

    hide nanase offended
    show nanase scold

    nk "My Proficiency is only as good as the person I'm assisting, so I only help the best of the best!"
    nk "I am doing everything I can, but I can't even begin to help you unless you tell me what to do! So don't you dare tell me that doing what you're told is mindless, because it's the only thing I'm good at!"
    nk "So... that genuine enough for you?"

    "In a flash, her confidence evaporated."

    n "Wait, that's why you're mad at me?"

    hide nanase scold
    show nanase sad1

    nk "My Proficiency is... Obedience. I need people to tell me what to do, or I fail."
    nk "I truly want to help you. I just don't know how. I'm sorry."

    hide nanase sad1
    
    menu:
        "I didn't ask for your help.":
            $ nkRep -= 1 

            show nanase irate

            nk "Why are you making this so difficult?"

            n "You don't have to be here."

            hide nanase irate
            show nanase scold

            nk "You're the one who came looking for me."
            nk "If you don't want my help, then why are you here?"

            n "I'm just trying to blow off some steam, okay?"

            hide nanase scold
            show nanase irate

            nk "Yeah? Well you have a funny way of doing it."
            nk "I- I just want to make people happy."
            nk "It's one of the few good things that comes from having such a lame ability, and no one wants me to use it the way I want to."

            n "How is that my problem?"

            nk "It's not. So don't treat me like I'm a problem and let me do my job."

            hide nanase irate

        "Reputation?":
            $ nkRep += 1

            show nanase embarrassed

            n "You have a reputation?"

            nk "I... Uhh... Oh jeez; me and my big mouth. I don't know if I told you this already or not, but I used to be a teacher's aide..."
            nk "....and I, uh, really liked my teacher."

            n "That's it? That doesn't sound so bad."

            hide nanase embarrassed
            show nanase cry

            nk "His wife didn't seem to think so."

            n "Oh... Oh, wait, what? When did this happen? You're like fifteen at the oldest."

            hide nanase cry
            show nanase embarrassed

            nk "It's not what you think!"

            hide nanase embarrassed
            show nanase ashamed

            nk "Everyone else seems to think that too..."
            nk "I wanted them to think that, in the past that is."
            nk "As if having a teacher as my boyfriend made me better than them somehow. Now I'm that girl."

            n "I think that's a little different from what I'm going through."

            nk "And what would that be?"

            "Wait a minute- does she not know?"

            hide nanase ashamed

        "You shouldn't get involved.":
            $ Intel += 1

            show nanase scold
 
            n "I know you mean well, but this isn't something you should get involved in."
            n "It's too dangerous."

            nk "Aren't you the one making it dangerous?"

            n "I literally can't help being a target at this point."
            n "All I can control is how I react to it."
            n "You'll just get roped in with me if you keep interfering like this."
            n "You'll ruin your chances at Class Historian at this point."

            hide nanase scold
            show nanase irate

            nk "W-well you'll ruin your chances at Student Council President."

            n "My chances are slim enough as it is."
            n "For all you know, this could make me go up in the polls. If not, then I'll do something else."

            hide nanase irate
            show nanase offended

            nk "No! You absolutely have to be Class President! If not then..."

            n "Then?"

            nk "Then Kazz would be the only candidate."

            "She shuddered, rejecting the idea with every fiber of her being."

            hide nanase offended
            show nanase irate
            nk "I can't let that happen. You're by far the best choice we've got."

            hide nanase irate

    show nanase surprised

    n "Do you have any idea- Haven't you heard about the Guwon Riots?"

    nk "Well, yeah, but what's that have to do with anything?"

    hide nanase surprised
    show nanase sad1

    nk "Unless... Oh. Were you one of the survivors?"
    nk "I've heard a few of them came here."

    n "You don't recognize me?"

    hide nanase sad1
    show nanase scold

    nk "Is this some kind of trick question? Of course I recognize you..."
    nk "We're friends, aren't we?"

    n "No, you know what? Nevermind, it's nothing."

    "I'm not going to botch a chance at being perceived as normal over winning an argument... yet."

    n "Look, I'm sorry, it's just hard for me not to question people's motivation."

    hide nanase scold
    show nanase sad smile

    nk "I get it."
    nk "I do the same thing all the time. It's hard to let people in."
    nk "But that doesn't mean you have to shut people out entirely."
    nk "I'm here for you, if you need me."
    nk "You know where to find me."

    hide nanase sad smile
    
    return

label Nanase3:
    scene backgroundstuco

    show nanase offended

    n "You busy?"

    nk "No, but aren't you?" 

    n "Uhh..." 

    nk "In the entire time I've known you, you haven't made one move toward advancing your campaign." 

    n "I've been kinda preoccupied." 

    hide nanase offended
    show nanase scold

    nk "If you can't even be bothered to campaign properly, how do you expect the students to have faith in your commitment to the position?" 

    n "Well, it's not like I'm doing nothing. I'm doing something right now." 

    nk "And that would be?" 

    n "Surveying?" 

    "She doesn't seem even remotely impressed."

    hide nanase scold

    menu:
        "Want to help?":
            $ nkRep += 1

            show nanase smile

            "Her eyes lit up."
    
            nk "Well, since you asked." 
            nk "We need to get posters up; flashy, with a 6th grade reading level." 
            nk "A good election speech, short, lot's of 3 word catch phrases. It really helps nail down your key message."
            nk "Oh, a few club endorsements wouldn't hurt, and a faculty advisor... for starters."

            "She was talking at a mile a minute, but I'm guessing my eyes started to glaze over or something, because she's slowed down."

            n "6th grade, really?" 

            hide nanase smile
            show nanase talk

            nk "Average literacy levels are low sir, don't underestimate the power of knowing your audience."

            n "But whatever shall I do without my superfluous adjectives?" 

            hide nanase talk
            show nanase smile talk

            nk "I think you'll live. Now, come on! Let's go!" 

            hide nanase smile talk

            scene backgroundMPath

            "I set up in the library with butcher paper and a handful of 'borrowed' markers from the council room."

            nk "They don't allow food in the library, so it's a good thing this stuff isn't really food." 
            nk "Coffee isn't even in a food group." 

            n "Due to its lack of inherit nutritional value, coffee is considered part of the other or oil group." 
            n "Though it is a leading antioxidant." 

            nk "Right, well I guess we can add detail oriented to your list of qualifications for presidency."

            n "Sorry, I know a lot of useless information." 

            nk "I don't think it's useless, you just have to find a way to put it to practical use." 

            n "That was almost convincing." 

            nk "Well you shouldn't be so hard on yourself. You have an amazing ability. It's way cooler than mine." 

            n "I get ice pick headaches if I remember stuff for too long and I get lost in thought for hours if I'm left alone."

            nk "I can't cook, do laundry or do anything correctly unless someone else tells me to." 

            n "Isn't that a little bit of an exaggeration?" 

            nk "Ever burned water?" 
            nk "No, I'm serious, I tried making tea once and it started smoking. I ruined the kettle." 

            n "Point made." 

            nk "It's just lame, but if I work for an amazing person, maybe it'll be less lame." 

            n "You're working with one." 

            nk "D-don't get cocky. You still have the potential to suck." 

            n "Wow." 

            nk "Sh-shut up and draw your stupid poster." 
        "What about you?":
            $ Intel += 1

            show nanase surprised
    
            nk "Hunh?" 

            n "What about your campaign for Historian? I haven't seen you campaigning." 

            hide nanase surprised
            show nanase condescending

            nk "That's different, I'm running unopposed." 
            nk "Not a lot of kids are rushing to be a secretary." 

            n "I mean, that's fair, but that doesn't mean you shouldn't try. Live by example and all that." 

            hide nanase condescending
            show nanase irate

            nk "Does that mean you'll try harder, if I try harder?" 

            n "No, it means I'll start trying if you start." 

            nk "Ugh, point made. I'll run a proper campaign and so will you. Let's do this!" 

            hide nanase irate

        "Stand by your statement.":
            $ nkRep -= 1

            show nanase irate
    
            n "Yes surveying, hearing from the people, learning their problems and coming up with solutions." 

            nk "Okay then, I have a problem for you sir." 

            n "G-go on." 

            hide nanase irate
            show nanase scold

            nk "I have a friend who claims to want responsibility, but does none of the things to earn it." 
            nk "How do I get my lazy running mate's butt in gear." 

            n "Coffee." 

            hide nanase scold
            show nanase surprised

            nk "Wha~at?" 

            n "Buy him some coffee." 

            hide nanase surprised
            show nanase scold

            nk "Are you seriously asking me to bribe you into doing something you said you wanted to do?" 

            n "It's worth a shot." 

            hide nanase scold
            show nanase irate

            nk "Ugh, you're no better than those idiots." 
            nk "If I wanted to be someone's mommy I'd hang out with Kazz or Dyre again." 

            n "Hey! I'm a presidential nominee, not an advice columnist... I don't know who you're talking about." 

            nk "Two of the most immature dorks I've ever met." 

            "Harsh, and she's the one who started it. Nagging me out of the blue like that, what gives?"
            hide nanase irate

    scene backgroundstuco

    show nanase talk

    "Even if we don't always get along, the past few days I've spent with Nanase have felt surprisingly normal."
    "After everything that happened, I hadn't expected to be able to just hang out with someone and work on school stuff again."
    "Still, I haven't exactly been up front about why I'm here. I can't keep pretending it's because I don't know how to start."

    n "Are you familiar with Estella Prep?" 

    nk "Yeah, I went there in middle school." 

    "Oh, so she does know."

    n "Cool... cool. Then, you were there, weren't you?" 

    hide nanase talk
    show nanase

    nk "Yeah... Nagen, what's this about?" 

    n "I just had to check, y'know? You just seem so unaffected by it." 

    hide nanase
    show nanase sad1

    nk "I don't remember much about what happened." 
    nk "The riots, it just feels like a giant blur to me." 
    nk "It just seems so surreal, I can't help but feel disconnected." 
    nk "I know what happened, and it's not that I don't care, it just doesn't feel real to me y'know." 
    nk "It just feels different remembering an experience as opposed to someone telling it to you." 
    nk "I try not to think about it." 

    n "Honestly, me too." 

    hide nanase sad1
    show nanase ashamed

    nk "It must be harder for you. You can remember everything." 

    n "I'm still trying to pull myself out of that way of thinking too." 

    "I'm still trying to figure out where to go from here, but it's moments like these that are nice."

    hide nanase ashamed

    return
label Nanase4:
    scene backgroundclearing

    "Nanase has been using every ounce of daylight to flip through the book she always carries."
    show nanase ashamed
    "She runs her thumb over a section with torn out pages."

    n "Hey."

    "She jumps and slam the book closed."

    n "Sorry, didn't mean to scare you."

    show nanase embarrassed

    nk "It's fine. It's impossible not to spook people out here." 

    n "Am I allowed to know what you're reading?"

    show nanase irate

    nk "It's my old diary. There's huge gaps in it, even though I was trying to write everyday."
    nk "I apologized every time for not keeping better track, but I'm sure that's what happens when you don't think your life is interesting enough to write about."
    nk "It's a shame. I am interested in those ordinary days, even if the old me thought they were nothing."

    n "I never tried it."

    "Diaries just always seemed like a thing girls kept."
    "If I had written in a journal, I'd have more evidence now about what Estella let slip by them."

    n "I did the way cooler thing of talking to a stuffed animal like it could hear me."

    "She laughs, her grip on the book loosening a little."

    n "I know everyone's been freaking out since the trip started. Are you doing okay?"

    show nanase sad1

    nk "Something the teachers said scared me and I'm trying to figure out why."
    nk "The fact we can't get rid of the statues, even though no one wants them here, it just-"

    "She looks like she's about to cry."

    show nanase sad2

    nk "It felt familiar in a bad way."

    hide nanase

    menu:
        "Why do you need your diary to do that?":

            show nanase surprised

            nk "People's memories change."
            nk "This is the most accurate recording of me, even if I was never a reliable narrator."
            nk "Stuff that seemed normal then, I know better now."

            n "Such as?"

            show nanase sad2

            nk "I, well... I kept agreeing to do things I didn't want to do, and then got mad at the people who wanted me to do them."
            nk "I kept hoping someone would tell me ‘no' for me. People don't work that way."

            n "Did you tell them no?"

            show nanase irate

            nk "No idea, there's no exact quotes to go off of. I was ten after all."
            nk "I had other things on my mind, pointless things. Who knows, maybe they'll seem less pointless when I'm older."

        "Did you find something?":
            
            $ nkRep += 1
            show nanase sad smile

            nk "I think so. Nagen, you had strict parents right?"

            n "Yeah."

            show nanase ashamed

            nk "Did you ever get in trouble for throwing something away?"
            nk "Like, if you tossed out an empty bottle, would they ground you for it?"

            n "No. Granted, I never had a lot of stuff to begin with."

            show nanase sad1

            nk "My memory's not good, even compared to other kids."
            nk "I thought I was blocking out the riots, but now I'm wondering if it was this."

            show nanase scold

            nk "There's so many times in here I got mad at my mom for putting something in my room, or using my Proficiency to keep me from cleaning."
            nk "I have no idea how bad it was or if I was just exaggerating things to seem more interesting."

            "It sounds like something a hoarder would do. "

            n "You don't do that now from what I've seen. I think you should trust yourself a little more."

        "They bother me too.":

            $ nkRep -= 1

            show nanase irate

            n "Then again, I'm a control freak and they're really freaking creepy. To that weird old guy, it might be like your diary."
            n "People don't want things important to them vanishing when they're gone."

            show nanase cry

            nk "That's ridiculous."
            nk "It's just stuff."
            nk "If something happened to me, I wouldn't want you guys holding onto my trash."

            n "Even if it's stuff you didn't think was trash?"

            nk "Especially then. Burdening other people with a chore... Only a selfish person wants that to be their dying wish."

            "I feel like she's talking about someone else."
            "Perhaps age has made me wiser, but I feel like I'm not going to like what she says if I keep pushing forward."

    show nanase sad smile

    nk "I guess you wouldn't have this problem. You don't forget anything."

    "She looks back at her book with a frown."

    show nanase surprised

    nk "I wonder though, and don't feel pressured to answer. How do you know if your memories are accurate?"

    n "I took a million tests, and I could recreate any book I read."

    "Hunh. I guess right now, that would be kind of handy. There could be books and stuff that got destroyed during the riots."

    n "I haven't failed a test in years."

    nk "Well yeah, but what about things involving other people?"
    nk "Like, when I was a kid, I didn't get why there were certain rules I had to follow, and I'd make up the reason so it'd make more sense."
    nk "Have you ever done something like that?"

    elif vision ==1:
        n "Maybe... I'm not sure. I've been trying to figure out why my proficiency's going on the fritz lately."
        n "It's usually stuff involving other people."
        n "It's not like I have other people's thoughts in my head though, and there's changes in what I say."
        n "So it's not like it's just me being unable to keep straight how I felt about things."

        show nanase embarrassed

        nk "You're having problems remembering things too?"

        n "S-sort of, not really, forget I said anything."

        show nanase blush

        nk "Nagen, it's okay. Even if you're having problems, you'll always have a better memory than me.
    else:

        n "I don't think so. I could always revisit the memory whenever I wanted."
        n "I might feel differently about it now, but it's not like I'm misremembering the people I knew." 

        nk "Really? You remember people exactly as they are?"

        n "Yeah."

        show nanase sad smile

        nk "Does that include me?" 

        n "Of course."

        nk "That's good. It's nice to have more than one view of a person. I should start writing again too."

    n "I'm sure you've had all kinds of exciting things to write about now."

    show nanase sad1

    nk "Yeah, though I don't know who would believe me."
    
    show nanase sad smile

    nk "Spooky statues, masquerade balls, I never thought those sort of things would happen to me without someone's help."
    nk "I spent so many of these pages wishing someone would save me." 

    "She stands up, dusting off her skirt with a sad smile on her face."

    show nanase blush

    nk "I know we didn't know each other very well in school, and what you did hurt a lot of people, but..."
    
    show nanase cry

    nk "You ended up being the person I was hoping for. No one knew how bad the house was."
    nk "Even I don't anymore, but I finally get to live with my dad again."
    
    show nanase cry smile

    nk "I get to decide what to do with my proficiency instead of having it used against me."

    hide nanase

    #[CG]

    nk "You're kind of like my hero."

    "No one's said that to me before. Not my friends or Lethe. My entire life, all I've ever wanted to do was be a Karmic Gladiator."
    "I thought I failed when they took the costume away."

    nk "A-are you okay?"

    "It's a stupid thing to cry over. I'm not crying! It's probably dirt in my eye or something."
    "I'm not getting choked up over a little praise. That'd be ridiculous."

    n "I'm fine."

    "Ugh, can you sound a little more like you mean it? "

    nk "This is a secret obviously. I don't want people getting mad at either of us. I just thought you should know."

    elif Hero > Villain:

        nk "The more I get to know you, the more I believe it."

    else:

        nk "I know you're capable of great things."

        n "Yeah, yeah. Don't lay it on too thick or it'll go to my head."

        nk "I'm being serious!"

        n "I know, it's just- It's weird to hear."

        nk "It'll get less weird the more you help people, sir." 

    "I'm curious what's in that book that got her saying all this stuff."
    "There's no way she'd let me see it though. So, instead, we walk back to camp."

    return

label Nanase5:
    scene backgroundstuco

    show nanase smile talk

    "Nanase and I worked on our posters for a good couple hours, preparing for speeches and public speaking in general."
    "Nanase's had a border of panda stickers and some crudely drawn books on her adverts. I tried my best to keep my letters the same size on the stupid thing."

    nk "-and then in episode 145, Pandeku crashed this underground speakeasy run by flamingos." 
    nk "There was this killer dance battle-" 

    "She's been talking about Shanghai Bouncer non-stop since she got here. Unless I want a five paragraph essay on Pandeku's season three character arch I need to change the subject."

    n "Uh, thanks again for helping out with the campaign and everything." 

    hide nanase smile talk
    show nanase surprised

    nk "Hunh? Oh, no problem, really. It's nice to finally be working with someone, not for them." 
    
    hide nanase surprised
    show nanase smile

    nk "Really nice..." 
    nk "Do you think we would have been friends if we'd gone to the same school when we were kids?" 

    n "Don't you mean the same class?" 

    nk "Hunh?" 

    n "We both went to Estella Prep, remember?" 

    nk "O-oh, right. Do you think we'd be friends if we were in the same class?"   
    
    hide nanase smile

    menu:
        "Yes":
            show nanase blushing

            nk "Y-yeah, me too. Maybe things would have turned out differently."
            $ nkRep += 1
            
            hide nanase blushing

        "No":

            show nanase sad2

            nk "You're probably right... but we're friends now. That's all that really matters."

            hide nanase sad2
    show nanase

    n "There's actually something I've been meaning to ask you..."

    hide nanase

    menu:
        "Why do you keep trying to help me?":
            $ nkRep -= 1

            show nanase disappointed

            nk "Haven't we gone through this already? I like helping you."

            n "Yeah you said that. You also said you could only do something right if you were told to..." 

            hide nanase disappointed
            show nanase condescending

            nk "Y-yeah... So?" 

            n "Did you want to help me? Or did someone tell you to." 

            hide nanase condescending
            show nanase sad1

            nk "O-oh, you meant like that." 
            nk "Obedience is my Proficiency and you asked me to help, that's why I'm so good at it." 
            nk "No need to be paranoid." 

            n "Yeah, after you insisted. You were the one who first came to me." 
            n "Why?" 

            hide nanase sad1
            show nanase

            nk "I mean, there a lot of reasons." 

            n "But was one of them being told to?" 

            nk "Does it matter?" 

            n "Yes. There is someone, isn't there?" 
            n "Who?" 

            nk "I don't know." 

            hide nanase

        "Why do you keep calling me sir?":
            $ nkRep +=1 

            show nanase surprised

            n "I'm not your boss or anything, you could just call me by my name." 

            nk "Uhh... Umm..." 

            n "It's not that weird." 

            hide nanase surprised
            show nanase sad smile

            nk "O-okay, I'll try.. Mr. Tesuta." 

            n "N-no. No, that's not what I meant." 

            nk "I know! But, like, you're going to be my boss if you win. It's a respect thing." 

            n "Come on, we're friends aren't we?" 

            hide nanase sad smile
            show nanase embarrassed

            nk "Okay then, N-nagen." 

            n "See? That wasn't hard at all." 

            hide nanase embarrassed
            show nanase offended

            nk "Easy for you to say!" 
            nk "I haven't called anybody by their first name since elementary school!" 
            nk "It makes things easier." 
            nk "But if I'm going to be in this for the long haul, I need to commit." 
            nk "This is the ultimate sign of trust y'know, you're not allowed to disappoint me now... Nagen."

            "I guess it's a step in the right direction, but something about what she said seemed off."

            hide nanase offended

        "Do you want to go out?":

            show nanase surprised

            nk "Do you need some fresh air or something?" 

            n "I meant do you want to go out, on a date?" 

            hide nanase surprised
            show nanase embarrassed

            nk "O-oh! Oh my goodness. Are you serious?" 

            n "Yeah." 

            hide nanase embarrassed

            if nkRep > 3:

                show nanase cry

                "In all the scenarios I had run through my head of how she'd react, I never imagined her crying."

                n "Hey, woah, are you okay?"

                nk "Y-yeah I'm okay." 
                nk "I'm okay... You really mean it?" 
                nk "You want to go out with me?" 

                n "Yeah, I'm not messing with you or anything." 
                n "Is that... That's not a bad thing is it?" 

                hide nanase cry
                show nanase cry smile

                nk "No, no." 
                nk "I'm sorry."  
                nk "I'm really, really happy." 
                nk "I didn't think... I'm sorry I can't stop crying." 
                nk "It's like, I was hoping you liked me but I don't feel like I deserve it." 
                nk "It's stupid." 

                n "It's not stupid at all." 

                "I really didn't know what else to say at that point. I just kinda stood there, feeling useless while she calmed down."

                hide nanase cry smile
                show nanase blushing

                nk "You want to go out with me." 

                "She repeated it softly, reaffirming what I feel like I've repeated a few times now."

                n "Yeah. I'm, uhh, not sure where yet." 

                nk "That's okay. I'm not terribly picky." 

                n "So that's a yes then?" 

                hide nanase
                show nanase sad smile

                nk "Ah! Yes, of course." 

                hide nanase sad smile

            else:
                
                show nanase cry

                nk "That... wouldn't be a good idea." 

                n "What do you mean? We make a great team. It wasn't something I said, was it?" 
                n "I don't want to pressure you into doing something you don't want to do." 

                nk "No it's not that I don't like you..." 
                nk "I mean, I think I do. I just want..." 
                nk "I don't want to hurt you..." 

                n "What makes you think you'd be hurting me?" 

                hide nanase cry

    show nanase ashamed

    nk "I'm sorry, I just keep making things difficult by getting involved." 
    nk "I don't know what I'm supposed to do anymore." 
    nk "I want to do everything I can to help you, but I'm not even sure what that means." 

    n "Nanase what's going on?" 

    hide nanase ashamed
    show nanase sad2

    nk "Something just doesn't feel right about this." 
    nk "I feel like I've kinda forced myself on you, and I feel really bad about it." 
    nk "I mean, I love that you started coming to see me." 
    nk "It made me feel needed, but what if that's a bad thing?" 
    nk "What if I'm repeating the same mistakes over and over again and now I'm dragging you down with me?!" 
    nk "Or... maybe I'm just being paranoid." 

    hide nanase sad2
    show nanase sad1

    "Nanase's always been a little codependent around me."
    "I had just written it off as a side effect of having a limited number of friends."
    "I hadn't considered it was something she was self conscious about."

    n "It's okay, I'd tell you if you were bothering me." 
    n "I like hanging out with you." 
    n "If there's anything you want to talk to me about." 

    "I watched as all emotion drained from her face. She stared at me blankly, maybe thinking something over, I'm not sure."
    
    hide nanase sad1
    show nanase

    #nk no emotion
    nk "I'm sorry, that request conflicts with 17 previous commands." 
    nk "Would you like to continue or override existing commands?" 

    n "Nanase, is this some kind of joke? What are you doing?" 

    #nk no emotion
    nk "Resuming. Please wait."

    #nk "normal"

    hide nanase
    show nanase surprised

    nk "I'm sorry for worrying you." 
    nk "I'm fine really, I just have a lot on my mind lately." 

    hide nanase surprised
    show nanase ashamed

    nk "It's kinda hard to explain." 

    n "...right. Does it having anything to do with... whatever the hell that was?" 

    nk "I'm sorry, once I have a better idea of what's going on, I'll tell you." 

    "I mean, that's good I guess, but what the hell was all that?"

    nk "I'm sorry sir, now's not a very good time." 

    hide nanase ashamed

    return
label Nanase6:
    scene backgroundroof

    "Nanase has been avoiding being alone with me ever since she had that shut down."
    "I can tell she's scared, but for whatever reason, she can't seem to tell me what's wrong."
    "I've been trying to treat her exactly the same, but I can't forget someone acting like a robot for a second just to then act like nothing happened. It's odd."

    "After all this time, she sent a text saying she was ready to talk to me."
    "On the roof, she stares up at a howling sky. A plane, for the first time in weeks, is flying near Guwon."
    "Her hair's pulled up tighter than usual. On the back of her neck is a scar that dips into her turtle neck."

    n "You've known the whole time, haven't you?"

    "The fact she forgot the riots, how she runs from anyone that used to be close to her..."
    "She must be an imposter. A robot, or sleeper agent, or any other type of stepford wife nonsense."
    "There is no way someone like her would be nice to me without an ulterior motive."

    show nanase cry

    nk "Of course I knew something wasn't adding up."
    nk "Pages from my diary were torn out and my computer had been rolled back before being given to me."
    nk "Someone was trying to erase part of the past."

    n "Who are you?"

    nk "I don't know."

    show nanase cry smile

    nk "Nanase Keisan is patient K from Mu's stupid campfire story."

    hide nanase

    #[CG]

    nk "A person who can't make old or new memories without the help of a computer, running on a language model made from what was left behind."
    nk "Without me, Nanase would still be comatose in bed. That's what I am."

    scene backgroundroof

    show nanase cry

    nk "My entire goal was to be her until she could be herself again, but… even though she's awake, she still can't do anything without me."
    nk "I've been trying to figure out why this whole time."

    "She flips through the diary."

    nk "I'd die without you."
    nk "You trust me, don't you?."
    nk "If you love me, you'll listen to me."

    show nanase irate

    nk "What if it's like what happened to Chisei and Mu?"
    nk "I am only as smart and as capable as the person telling me what to do wants me to be."
    nk "I think someone wanted Nanase to be completely dependent on them."

    hide nanase

    menu:
        "Do you think it's me?":
            $ nkRep += 1

            show nanase sad smile

            nk "No. From the moment I saw you I- she felt relieved."
            nk "I mean, I was excited to see people in general, but there has always been this feeling that something bad happened."

            "The riots for one, but she seems to be talking about something else."

            show nanase blush 

            nk "Seeing you be you... I don't know, it was like some happy accident."
            nk "You're the only person other than my dad I- she was happy to see."
            nk "I decided to trust it, even if you didn't know Nanase Keisan."

            n "Then why did you run away?"

            show nanase ashamed

            nk "There are so many holes in my memory. I started to doubt if any of it was real."
            nk "That maybe following you was a command too."

            if dateNanase = True:

                show nanase blush

                "She holds her hands over her heart."

                nk "You're the first person I want to talk to."
                nk "Being around you makes everything easier. Even if I was given a command, this love I have for you is real."

            else:
                
                show nanase sad1

                nk "The last thing I want to do is harm you."
                nk "That's why the thought I could, even by accident, scared me."
                nk "I don't like not being one hundred percent in control of my own body."

        "Who told you those things?":
            show nanase sad2

            nk "My mom."

            "Jesus fucking Christ."

            show nanase surprised

            nk "It's written down so casually, but clearly something about those words stuck out enough to write down."
            nk "There are things Dyre and Kazz said too."
            nk "I'd like to believe none of them realized what they were doing, but... there's so many veiled commands to be silent, cooperative unless talked to."

            n "How did no one else know about this?"

            show nanase irate
            nk "I was told not to complain. Being with you is like the polar opposite of that."
            nk "You expect me to do things when you're not in the room."
            nk "Or like, when you caught me shredding the threat letters, you didn't tell me to stop what I was doing while I was doing it."
            
            show nanase smile2
            
            nk "It was such a small thing, but it meant so much to me."

        "Can she hear me?":
            $ nkRep =- 1

            show nanase surprised

            nk "You mean, the patient?"

            "She looks away from me."

            show nanase irate

            nk "Yes, she can hear you. She's heard everything that's happened."
            nk "It would be bad if everyone at the school knew about this."
            nk "I don't like the idea of people treating her as anything other than a normal girl."
            nk "That's my job after all."

            n "Can you hear her thoughts?"

            show nanase disappointed

            nk "She needs me to have them, so yes, but not in the way you're describing."

            n "Does she need you to live?"

            nk "Without total care assistance? Yes, she needs me to be able to take care of herself."

            n "Is obedience her proficiency or yours?"

            show nanase irate

            nk "Both, I guess. An AI isn't proficient in anything other than following commands."

    show nanase

    nk "These feelings are the only way the patient can communicate with me, so I've been trying to honor them."

    n "You keep talking about them like they're your feelings."

    nk "Yes, well, the programming says I am Nanase. It's difficult to put into words-"

    n "No, I mean, they're your feelings too, aren't they?"

    "Her hand is warm, she's trying not to cry, and the look in her eyes is completely human."
    "I've seen what people move like when they're being controlled against their will."
    "If there are two wills inside her, they're moving together."

    show nanase sad smile

    nk "That's not what the doctors say."
    n "I think you should get a second opinion on that."

    show nanase ashamed

    nk "Nagen, there is something I'd like to try."
    nk "If it is what I think, and my proficiency is preventing me from getting better, another command might overwrite it."

    "If it does work though, that would mean I would have complete control over her. She's shaking, but determined as ever."
    "She looks prepared for the worst. After what Rise and Kitsune said about someone always watching, I have to be careful."

    n "Nanase, you don't have to tell me, but I need you to remember who did this to you."

    "A look of horror comes over her face."

    #[CG]

    n "Hey, hey it's okay."

    nk "I did."

    n "That's impossible. You didn't fry your brain on purpose, or implant a chip in your head-"

    "Wait, am I talking to Nanase or whatever is controlling her?"

    nk "No, but I wanted to forget. I ran away from home convinced I could elope with my teacher and he rejected me."
    nk "I was so embarrassed and heartbroken knowing nothing was going to change that I- I didn't want to be 'me' anymore."
    nk "Other people took advantage of that, but I could have stopped it."

    "I don't believe that. I don't think anyone would do this to themselves on purpose."
    "She's been so scared and lost this whole time, and now we know she could be told to do anything and she'd be compelled to do it."
    "She could have been a Vision Major before what happened and not realized it."

    n "I think, if you didn't know what you were agreeing to do, it isn't your fault."

    scene backgroundroof

    "Uitto would be so much better at this than me, but I get why she wouldn't want me to tell anyone else."
    "She's clinging to me, sobbing. I'm not sure if there's anything I could say that would make her feel better."

    show nanase cry

    nk "I'm sorry."

    "There's nothing to apologize for, but the more she apologizes the more this feeling of dread rises up."

    n "Are you saying sorry for something you did, or something you're going to do?"

    "She couldn't answer me."

    return


label NanaseF:
    scene backgroundstuco
    "Nanase must be busy right now."
    return