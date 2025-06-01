    # Opening video goes here.

label prologue:

    scene backgroundDisc1

    g "Click to continue."

    scene backgroundDisc2

    g "Click to continue."

    play music "music/Undertow.mp3"
    scene backgroundpolice

    "My whole life, I feel like I've been dragged around by my collar."
    "I guess when most adults see a kid act out of line, they want to control the situation."
    "Funny, seeing as that's the very thing I've been fighting for: a chance to be in control of my life."

    show cop

    cop "Please state your name and registered Proficiency." id prologue_b121c771

    n "My name is Nagen Tesuta."
    n "I have an Intelligence Proficiency."
    n "Anything I see, hear, or experience is recorded in perfect detail."

    hide cop

    "I tap the side of my head."
    "Having a great memory doesn't really make me smarter than anyone else, but the ability falls under the Intelligence major."
    "People want to classify things so they can feel important, they stop asking whether it's worth the effort in the first place."
    "I mean, some people can go their whole lives without realizing they have a Proficiency."
    "It's nothing special. The only reason I know about mine is because I was conditioned to have it."

    show cop

    cop "Look, you and I both know it's not looking good for you." id prologue_3787084e
    cop "I mean, you've heard the charges: premeditated murder, inciting a riot, mayhem, and menticide." id prologue_c616cfd6
    cop "These are all with a registered Proficiency which will add twenty-five more years to your sentence." id prologue_279523b4
    cop "Don't even get me started on the use of deadly weapons." id prologue_559297ff

    hide cop
    show koe

    ka "There's more than enough evidence to try you and your cohorts as adults." id prologue_2f132815
    ka "In the case of The Supreme Court vs. Lethe, vigilantism was determined to be a Class One felony." id prologue_2d7a1977

    show koe smirk

    ka "Some of her sympathizers seem to think they are above the law, like you." id prologue_4f631a84
    ka "If we were able to find her remaining supporters, it would be an excellent demonstration of goodwill." id prologue_0de140c0
    ka "We all remember-" id prologue_0a97bf0a

    hide koe

    play music "music/WhereS.mp3"

    "Remember? No one is truly capable of remembering."
    "Well, if you want to get technical, remembering is just being aware of something."
    "But people seem to think that it means they can recall the past in perfect clarity, ignorant of how time and their own perception taints everything that enters their mind."

    n "I know you. Koe Amagi, you were the prosecutor during Lethe's trial."
    n "Trying to extort information out of a child for your old department? That's surprisingly underhanded of you."

    show koe

    ka "Then you understand what you're up against." id prologue_648b8c83
    ka "Choosing to represent yourself in court only gave you a fool for a client." id prologue_4321cc62

    "She's the prosecutor for my case!?"

    show koe eh

    ka "I'm just doing my job, Mr. Tesuta and ensuring I have all the information I need for my case." id prologue_84fe7ab3
    
    hide koe
    show cop

    cop "Just make this easier on yourself and fold. It'll be better than what your friends are going through." id prologue_08dcde7d
    
    hide cop

label prologue_interrogation:

    menu:
        "Confess everything":

            $ hRep -= 1
            #$ Villain += 3
            #$ Vigor += 1

            jump prologue_confession

        "Refuse":

            $ hRep += 1

    n "Good cop, bad cop? Really?"
    n "I'm sorry, it's going to take more than a movie cliché to get me to tell anyone anything."
    n "Also, I was never read my rights, so unless you want a mistrial, I suggest you start treating me like an adult before trying me like one."

    show cop

    cop "That's not how the system works, kid." id interrogation_1_22b00617

    hide cop
    show koe

    ka "No, he has a valid point. You want to be talked to like an adult? Fine." id interrogation_1_9eadb7b7
    ka "Mr. Tesuta, if you don't give us the information we need, there will be no 'deal'." id interrogation_1_5e97f977
    ka "The first step is pleading guilty in court. There is no workaround." id interrogation_1_51729dfa

    "So it's her way or no way, hunh? Fine, whatever, she has her reasons; I have mine."

    hide koe

    #Question 1/4
    menu:
        "I have to protect my teammates": #(+Hero, +Vis)

            $ Hero += 1

            n "I'll plead guilty in court, but I and I alone am guilty of these charges."
            n "I cannot say the same of my friends; they genuinely believed in what Lethe told them..."

            "If I lie, I could be held in contempt of the court, but if I play the 'scapegoat', maybe they can get out of here unscathed."
            "Either way, someone has to answer for what we did."

        "I don't have a choice": #(+Villian, +Vig)

            $ Villain += 1

            n "Under the advice of my legal counsel, I will."

            "Maimai would be heartbroken if I got locked away. She's been through this before."
            "I practically have a walkthrough written on my sleeve."

            show cop

            cop "Do you believe you are guilty of these crimes?" id interrogation_1_591261de

            n "....."

            "I've talked too much already. Isn't the confession enough?"

            hide cop

        "It's all part of the plan": #(+Int)

            n "I'll cooperate."

            "It's too dangerous to make a move now. Best to play along for now."

        "I need to lighten my sentence": #(+Chr)

            n "...Okay..."

            "I hang my head at a 30-degree angle and feign the slightest tremor in my shoulders."
            "The more sympathy I can gain, the better."
            "No one will want to hear my side of the story if I act like the violent criminal they think I am."

    n "I fully understood the ramifications of my actions and stand at the mercy of the court."
    n "I aided in the brainwashing of my classmates and tried to conquer the Guwon Province for my own benefit."

    show cop

    cop "That's all we need to hear." id interrogation_2_4434ad43

    hide cop
    show koe

    ka "Not quite. I still have a few questions for Mr. Tesuta." id interrogation_2_49a741aa
    ka "The Junior Gladiators started as a club at your school, later to fall down a path of destruction." id interrogation_2_2a180a1f
    ka "And yet, no one can tell us whose fault this was." id interrogation_2_37c49d0b
    ka "In your estimation, who was the leader during the attack?" id interrogation_2_3817e59d

    hide koe

    #Question 2/4
    menu:
        "The one who told us to kill": #(+Chr)

            $ jRep += 1

            n "Lethe was. She wanted to create a group of youth vigilantes to gain back public support."
            n "It wasn't until after she died that we realized she was the one who started the chaos."

            "Chaos is putting it lightly."
            "She tried to get people to lynch anyone who was above average at... well... anything."
            "It nearly destroyed the nation."
            "Of course, if you really look at it, she wasn't wrong."
            "Proficiencies were dangerous to the general public, but so is a pen if you use it correctly."
            "These people, however, just want to confirm what they already believe, so I'll just tell them what they want to hear."

        "The one who gathered the army": #(+Vig)

            $ hRep += 1
            $ Hero += 1

            n "Hiro Morine was our leader. He insisted on it constantly."
            n "If it wasn't for him, we wouldn't have gathered nearly as much support."

            "He wasn't a very good leader after that..."
            "Actually, I was the one who did all the real work, but he meant well."
            "He was the first one of us to get captured by these hypocrites."
            "Even after getting dragged down, he insisted on taking credit for what happened. I hope he's okay."

        "The one who planned the attack": #(+Int)

            $ uRep += 1

            n "I was. I deliberately withheld information from my peers, knowing it would sway their decision to stay."
            n "In the end, I was the only one standing."

            "Well, not exactly standing. Let's just say, I don't handle failure very well."
            "I was lucky Maimai was crazy enough to spare my life."
            "If I manage to get out of this, I should thank her properly."

        "The club president": #(+Vis)

            n "Odori Hato was our leader. She's the one who brought Lethe's attention to our club."
            n "Odori just wanted to help us and a cheesy superhero club was her answer."

            "After Lethe died, she insisted we continue with our plans so that everyone would be happy again."
            "It's amazing how far out of hand things got."

            show cop

            cop "Do you know where Ms. Hato is?" id interrogation_2_c5e5c3a7

            n "No, she's not with us anymore."

            "I want to believe she's still out there, but..."

            hide cop

    show koe

    ka "You were apprehended by Vivaldi Thani before you were able to carry out your plan to completion, correct?" id interrogation_3_d4e85fff

    n "Yes."

    ka "What did you intend to do once you took over the city?" id interrogation_3_4754af2c

    hide koe

    #Question 3/4
    menu:
        "Fortify the city against my enemies": #(+Villain, +Vig)

            $ Villain += 1

            n "I just wanted a place where I could feel safe. Anyone there was free to leave, but they chose to stay."
            n "They took up arms, and I had to defend myself."

            show koe

            ka "According to eyewitness testimonies, you sought out innocent civilians who were in hiding and killed them on sight." id interrogation_3_40a08180
            ka "We found seventeen assault rifles in your room. Were these also for your defense?" id interrogation_3_a6f1d42a

            n "Yes."

            "It's not like I bought the guns online or anything. Guwon was already a dangerous place to live."
            "If you were alone on the street for over twelve hours, you could get killed or worse."
            "Wandering around the city with a gun was safer than going back home anyway."
            "I had all kinds of other machines I was playing with that I got from the junkyard, but that's not what they care about."

        "Rebuild the city": #(+Hero, +Int)

            $ Hero += 1

            n "Before making any plans, I would have had to reverse the damage that had been done."
            n "I was in command of over five hundred people; they needed a place to live once the dust settled."

            show koe

            ka "That's all?" id interrogation_3_3737d842

            n "Well, we would have needed a hospital next as well as to secure some kind of agricultural production to feed everyone."
            n "That alone would have taken months, and who knows what other problems may have arisen."

            "What can I say, I read way too many doomsday zombie comics as a kid."
            "If I wanted to be a good leader, I had to make sure my people were provided for."

            ka "This would be the same city you planned to bomb, correct?" id interrogation_3_5369cc0c

            n "What!? No, what good would that do?"

            "I tried my best to keep everyone safe, even if it meant lying. I can't let them down now."

        "Rebuild society in my vision":

            $ Villain += 1
            #$ Vision += 1

            n "Guwon was an experiment to see if we truly were capable of reshaping society."
            n "It was supposed to show the might of our nation's youth, that we were something bigger than everyone else said we were."
            n "The experiment failed."

            "I would have loved to see it spread past Guwon, but the opportunity never presented itself."

            show koe

            ka "Lethe had similar ideals. She thought that turning citizens against each other would weed out the weak." id interrogation_3_f9238aee

            n "No. Lethe thought society was beyond saving and proved that one spark could bring it crumbling down, which is why you have a job today."
            n "I believe that people can coexist, we just need to modify a few rules."

            "Lethe was right, the system had become too polluted, but destroying the world isn't the answer."
            "If you try to kill a virus, it will come back stronger and nothing will change."
            "In order to take it down, you have to integrate into its life cycle and prevent it from reproducing."
            "I just tried to do so from the wrong angle. Next time, I won't be so sloppy."

        "I don't know": #(+Hero, +Chr)

            $ Hero += 1
            #$ Charm += 1

            n "....."

            show cop

            cop "Mr. Tesuta, please answer the question." id interrogation_3_d18d8ff9

            n "...I didn't. I mean, part of me thought it would never work... I just... did what I always did..."
            n "I never questioned why or what came next."

            hide cop
            show koe

            ka "And what would that be?" id interrogation_3_cb0a83f2

            n "Hunh? Oh... nothing. Nothing was planned after that... I just did what I was told."

            "I just wanted to make everyone happy."
            "I thought if we took down the city together, we'd get some kind of happily ever after."
            "That's just not how the world works. There is no 'after'."
            "Just now and everything that has since passed. I have to do what I can so that 'now' doesn't get me killed."

    jump prologue_last_question

label prologue_confession:

    n "Yeah, I did it, everything you said is true."
    n "I helped start the riots to take down Estella and her talent mills."
    n "You want the names of all the adults that worked with her, right?"
    n "Fine. Just don't throw the book at me."
    n "We both know this is shady as hell."
    n "I'll parrot any garbage you want me to say after I get my sentence."

label prologue_last_question:

    show koe

    ka "And what exactly was your end goal in all of this?" id interrogation_4_1533fb2d

    n "Excuse me?"

    ka "Why did you attack Guwon in the first place? Such extreme actions had to come from somewhere." id interrogation_4_dbbb4cac
    ka "It's not every day a middle school student attempts to destroy a city." id interrogation_4_01eab4f6

    n "Guwon had to be brought down!"

    ka "Why?" id interrogation_4_0531dbce

    hide koe

    #Question 4/4
    menu:
        "It was corrupt":

            $ Hero += 1

            n "Guwon's entire economy was based around the manufacturing and propagation of Proficiencies."
            n "They treated us like livestock! We were paraded about as status symbols and meal tickets."
            n "No one cared what happened to us."

            show koe

            ka "There is no need for dramatics, Mr. Tesuta." id interrogation_4_6ac902f6

            n "Dramatics? Are you even listening to what I'm saying?"
            n "The Estella school system picked kids out and did whatever it took to show that their school improved the abilities of 'gifted' children."
            n "We were their guinea pigs to flaunt to the media and nothing was below them as long as it produced results."
            n "Someone had to stop it."

            ka "I find it hard to believe that Estella would do anything that would harm their students, Mr. Tesuta." id interrogation_4_71c541f5
            ka "If there was truly such a problem, you should have gone to the police." id interrogation_4_31158169

            n "They didn't listen, no one does! I'm not making this up, my parents worked there."
            n "I knew better than anyone what was going on and you did nothing! Eight anonymous tips and zero investigations."
            n "No one even looked. I had to do something, anything!"

            ka "So you were angry at the Estella and those who ignored you." id interrogation_4_fe3bd10c
            ka "Most children in that situation would simply run away; you stayed and killed anyone who opposed you." id interrogation_4_4cb5b66c

            n "I did run away. Lethe was the one who came after me."

            "She was the one who told us to stand up and fight for what we believed in."
            "That when the dust settled, the strongest would be left standing. Even if I lost, I'm still here."

        "It was convenient":

            $ Villain += 1

            n "Where else was I supposed to start? Guwon was my home."
            n "I had never been outside of my hometown and it was as good a place as any."

            show koe

            ka "For what?" id interrogation_4_ac425b37

            n "A blank slate. An area untouched by the stigmas of adults."
            n "Where governing bodies are chosen based on who is the most capable, not the most likable."
            n "We need to exhume these archaic standards and start from scratch."

            ka "There is no such thing as a blank slate, Mr. Tesuta. An ageist cleanse of the area is not a plan to be taken lightly." id interrogation_4_dd68f301

            n "Don't put words in my mouth. Anyone who wanted to could leave; I merely claimed the area as my own."

            ka "Your peers weren't allowed to leave." id interrogation_4_d83f7b5c
            ka "We have rescued hundreds of children from those delightful obedience collars." id interrogation_4_c7ba2e40

            n "Education collars, actually, though I do take issue with your tone."
            n "You act like I was the one who made them."

            "Shouldn't she be asking why it was made in the first place?"

        "It was safest":

            $ Villain += 1

            n "Guwon is water locked, it would be the easiest to fortify."
            n "With what Odori had planned, we couldn't just set up shop anywhere. It had to be someplace secure."

            show koe

            ka "What exactly did she have planned?" id interrogation_4_355015b4

            n "We were going to finish what Lethe started."

            "I can't exactly tell them that they were specifically our target."
            "They were the ones who called for Lethe's head."
            "They're probably asking these questions to see if everyone keeps the same story. That's fine, I can play along."
            "As long as even one of us makes it out of here, these people are going down."

            n "I wasn't exactly sure, but Odori assured me that the end justifies the means."

            ka "You expect us to believe that you were blindly following orders?" id interrogation_4_0b5a23fa

            n "I'm just the tactician. You asked me why I picked Guwon, I told you."
            n "It was the most pragmatic decision."
            n "I believed Lethe had our best interests in mind, same as you believe she was a monster."

        "To end the war":

            $ Hero += 1

            n "Everyone was fighting each other, not just us."
            n "This is just an isolated incident among many that happened during the battle between Lethe and the Karmic Gladiators."
            n "Even after she was gone, people were still fighting each other."
            n "I believe it's the entire reason your department exists, madam Vice President."

            show koe

            ka "Our department exists to regain peace, not to insight riots in the streets." id interrogation_4_d5e7a729

            n "Then why did it take our riots for you to turn your attention to Guwon?"
            n "It was home to a well-known weapons manufacturer at the time."
            n "Once we cut off their exports, suddenly you guys were able to regain control of the populace."

            ka "We needed to restore order. Doing so takes time and hard work." id interrogation_4_b94cebfb
            ka "We turned our attention to Guwon next due to the number of casualties, not because of any vigilante interference." id interrogation_4_a503ec13

            "She spits out the words as if they're acid." 
            "It's clear I'm getting nowhere with this woman."

            n "Casualties were bound to happen, you're assuming our activities caused more."

    show koe eh

    ka "I rest my case. It is clear that Nagen Tesuta is guilty of all crimes, and shows no remorse for what he has done." id interrogation_end_1b0b1285

    "Wait a minute, that's it!"

    # Add SFX

    n "Objection!"

    hide koe
    show cop

    cop "That's not how an interrogation works, Mr. Tesuta." id interrogation_end_1f5b1e73

    n "S-sorry. It's just, wasn't the purpose of this case to determine whether or not the Junior Gladiators lead to people dying?"
    n "None of the prosecution's questions have been relevant to the charges at hand; they've been about my character."
    n "In fact, all of Ms. Amagi's questions were about proving that my group was malicious and dangerous to society."

    hide cop
    show koe hmm

    ka "This is outrageous and highly unprofessional." id interrogation_end_0b62d016

    n "If this is indeed a trial to prove that my group committed atrocities in Guwon Province, then there is more than enough evidence to support the charges."
    n "However, it seems the prosecution wants to prove that my friends and I are, to put it plainly, evil."
    n "And for that, there is not enough evidence."

    "I already made a deal with the DVP to pardon my crimes in exchange for information on the location of the remaining Karmic Gladiators."
    "There's something else she's been trying to fish out of me, but I can't figure out what it could be."

    n "I want to change the terms of the deal."

    show koe smirk

    ka "You mean the plea bargain?" id interrogation_end_1204df22

    n "Right, that. I know that my friends and I, we're good people deep down."
    n "We just got caught up in something bigger and scarier than us and we did what we could to stay alive."
    n "The same can be said of any criminal of war. If you need someone to blame, then blame the adults."
    n "Just drop the charges against my team members."

    ka "I'm listening." id interrogation_end_017dffbc

    n "I am fully aware that someone has to atone for what happened in Guwon." 
    n "No amount of apologizing can erase that."
    n "The people you want to put behind bars are the adults that helped Lethe."
    n "The ones who destroyed everything, not just Guwon. I can tell you where they are."
    n "Just let me and my friends go."

    show koe

    ka "And how do you expect us to believe your group is so blameless?" id interrogation_end_5187cbb7

    n "....."

    "Shit, I thought I had her!"

    ka "The DVP has a program for troubled teens." id interrogation_end_0d81cd23
    ka "So far, we have been unable to gather any evidence that proves the program is effective." id interrogation_end_be81a2af
    ka "We would like to use the Junior Gladiators as our focus group." id interrogation_end_6882d4e6

    "Wait a minute, what?"

    show koe smirk

    ka "If your members cooperate and complete the program, we will drop the charges." id interrogation_end_16ce5e4a
    ka "Of course, the Junior Gladiators are officially disbanded and will not be allowed to continue any further activities." id interrogation_end_8e278142
    ka "You will be under constant surveillance as a part of the observational study and to prevent skewed data, they will not know about the experiment." id interrogation_end_894a80d2

    "Woah, woah, woah. A; that is highly unethical and B; why's the cop gone silent?"
    "Did I just play into this lady's hand? No way."
    "I mean, yeah I wanted to get my friends out of this, but I didn't want to make them into guinea pigs like me."
    "There's no telling what these people might do for the sake of 'science'."

    hide koe
    show cop

    cop "The terms have been set." id interrogation_end_c2900460
    cop "If the Junior Gladiators complete the DVP's Villain Prevention Program and can prove they can integrate back into society, they will be issued a full pardon." id interrogation_end_91a2a7d9
    cop "If they are unable to do so, they will be tried as adults for their crimes in Guwon." id interrogation_end_a20f350c
    cop "Do you agree to these terms?" id interrogation_end_a0fa5fb0

    n "Yes."

    "It's not like I really have a choice anyway."

    cop "Then it's settled. A follow-up hearing will be scheduled in one year to document your progress." id interrogation_end_1ac62a6d
    cop "In the meantime, you will be appointed a guardian from the DVP to take care of you during your time in the program." id interrogation_end_bf51e3a0

    "Unbelievable. Fucking unbelievable."
    "I thought for once I could outsmart these assholes and get out of all this. No, this is not over."
    "A year is a long time. I'm sure I will be able to think of something."

    cop "Your guardian is waiting." id interrogation_end_efac05da

label life_1:

    window hide
    with Dissolve(1.0)

    hide cop
    with dissolve

    show backgroundPT
    with Fade(0.5, 1.0, 0.5)
    
    play music "music/leaf.mp3"

    pause

    scene backgroundcar
    with Fade(0.5, 0.5, 0.5)

    "A black limo is waiting for me out back."
    "What's the point of sneaking me out with the trash if they're going to send a nice car?"
    "It feels like stepping into this car might be the last thing I get to do."
    "Regardless of my hesitation, I'm ushered into the back seat by the bailiffs and greeted by none other than the Medusa Killer."

    scene backgroundcarin

    play audio "car sedan door open 1.ogg"

    n "Maimai?"

    show maimai

    mm "The one and only." id interrogation_end_665582e8

    play audio "car sedan door shut 1.ogg"
    play sound "car_inside.ogg" loop

    n "You're my appointed guardian? This has to be a mistake, you're a registered villain."

    mm "The Medusa Killer is a registered villain who's gone MIA. I'm Maimai." id interrogation_end_6805706d
    mm "See, I've got glasses and everything, no one can tell the difference." id interrogation_end_ba51f0f6
    mm "Either way, I haven't seen you since pulling you out of a war zone and this is the hello I get?" id interrogation_end_bdd73484

    "I ended up in a dark room with two vultures circling me thanks to her 'help'."
    "She promised she wouldn't leave my side until I was safe."

    mm "Don't give me that look, you'll be fine." id interrogation_end_4ba27adc

    n "You still haven't told me why they sent you."

    mm "They thought a friendly face would keep you from bolting out of the car." id interrogation_end_695c698d

    n "And the stupid glasses?"

    mm "A sign of my sincerity. My hypnotic gaze only works when you can see my eyes." id interrogation_end_8f7c5908
    mm "If I was planning to force you to cooperate, you'd be drooling on the floor by now." id interrogation_end_ecbaf125

    "Her hypnosis was terrifying to experience first hand, especially knowing for five other victims, it was the last thing they experienced."
    "In my attempt to seize control of Guwon, I had put myself in the crosshairs of a dark-web serial killer when I endangered her next target."
    "I thought she'd be out for my blood, but she felt bad for me, I guess."
    "I'd like to believe she cares for me deep down, but maybe she's completely delusional. I wouldn't rule out both."

    n "This is the most normal I've seen you look... ever."

    mm "After those DVP schmucks found out my methodology, I had to retire from stuffing orchids down criminals' windpipes and ditch the costume." id interrogation_end_d8e6c5ef
    mm "Besides, it wasn't suitable for my new role." id interrogation_end_4adf67e2

    hide maimai

    menu:
        "New role?":

            #$ Charm += 1

            show maimai

            mm "Pantsuit, short hair, dorky accessories; I'm one minivan away from perfection." id interrogation_end_678aca50

            "This is her idea of what a mom looks like?"

            n "I'm flattered, but I need a couch to crash on, not a parent."

            mm "That's not what the state says." id interrogation_end_073a4d47
            mm "You want to get out of this mess, then we gotta go full nuclear. Nuke the situation beyond recognition." id interrogation_end_935c89a1

            n "You do realize a nuclear family has two parents, right?"
            n "Please tell me this isn't going to be one of those 'Weekend at Bernies' things where you dress up a dead body to be my dad or something."

            mm "I didn't even think of that!" id interrogation_end_a7993254
            mm "It could work... but no, I found a living option and on my honor, he will remain a living option." id interrogation_end_639a0a53

            n "A friend of yours from your dark web days?"

            mm "Yeah, we go way back." id interrogation_end_acab57b9

            n "I think the dead body would be safer."

        "Where are we going?":

            #$ Intel += 1

            show maimai

            mm "Someplace safe." id interrogation_end_3108d53c
            mm "The DVP would like you to believe the best place for you is with them; they're only half right." id interrogation_end_b27fbd5b

            n "So we're running from the DVP again."

            mm "This is a little different than huddling around a flaming oil drum in an abandoned alleyway." id interrogation_end_f293281e
            mm "Going off-grid isn't going to help us now. We need to leech from the immunity capitalism offers." id interrogation_end_a1436a27
            mm "Money may not buy happiness, but it sure as hell can buy you protection." id interrogation_end_25c0ea6c

            "Well that kinda explains the car."

            n "Whose limo is this?"

            mm "...An old target's decided to be quite hospitable." id interrogation_end_336d4d64

            n "What the- Oh my god, you're blackmailing the poor man."

            mm "I'm not a monster! It's more complicated than that. You just gotta trust me." id interrogation_end_a89226d3

    mm "I had to cash in an old favor to get us out of this mess." id life_1_f5c87301
    mm "I was hoping to leave his debt dangling over his head for a few more years, but this is more important." id life_1_054db603
    mm "You need a proper guardian and as much as I'd love to take care of you myself..." id life_1_2328d997
    mm "I don't have a legal job, or house, or any of the tools that would let the state give me guardianship." id life_1_33f8eb0d

    n "I'm not a child."
    n "I appreciate everything you've done for me, but you'll have to forgive me for not fully trusting you or this other person."

    mm "I just want what's best for you. Please, just give this guy a chance." id life_1_159e00ec
    mm "I will be with you the whole time. He's... he's a bit of a potato, but he'll treat us well." id life_1_2f5b06dd

    n "...Potato?"

    mm "Boring, lives somewhere dark and hard to find. A potato." id life_1_9befeacf

    n "...Right..."
    n "Has anyone heard from Odori?"

    mm "No, I'm sorry." id life_1_5771cc36

    n "You sure it's not classified or something?"

    mm "If it was classified, I would have told you it's classified." id life_1_73b4e738

    stop sound 
    stop music 

    "A month. She's been missing for over a month."

    play music "music/Still.mp3"

    "At this point, they're not looking for {i}her{/i} anymore, they're looking for a body."
    "My mouth's gone dry. I don't want to be here."
    "She should be in a limo on her way to a new home, not me."

    mm "Nagen honey, remember to breathe. We're not going to get out of the car until you're ready." id life_1_92a5184d

    scene backgroundnhouse

    play music "music/LateNights.mp3"

    play audio "car sedan door open 1.ogg"
    
    "As we step out of the car, I can smell the faint, eerie scent of velvet kiss growing up by the walkway."
    "The dreary gray estate looms in front of me. Utterly unwelcoming."

    show maimai smile

    mm "Now we just gotta find a way in!" id life_1_c69ebb73

    "Maimai's exuberance clashes with the apathetic surroundings."
    "Her violently pink attire is giving me a migraine."

    n "He is expecting us, right?"
    n "You didn't just stalk the man... did you?"

    show maimai oh

    mm "No... kind of." id life_1_e78bf0d3

    hide maimai

    "Of course. Why would I expect any different?"
    "I stumble after her through the leaves."
    "With her bottom lip clenched between her teeth, she fishes a metal chain out of the overgrowth of trees and pulls."
    "The building groans as a sizable bell rings from a tower above the gate."
    "When the door opens, I begin to understand why Maimai described my appointed guardian as a potato."

    show maimai smile at left_center

    mm "Surprise!" id life_1_bd60fe00

    show ken at right_center

    kan "What part of this arrangement involved you coming here?" id life_1_8e960e52

    n "I knew it! He wasn't expecting us at all!"

    mm "Well, he was expecting you." id life_1_29062182
 
    kan "...That's the kid?" id life_1_07ea0577

    mm "He claims otherwise, but yes, this is him." id life_1_de196b8d
    mm "Don't worry, in this big ol' house, you'll hardly notice us." id life_1_b207f309

    show ken damn

    kan "Us?" id life_1_3d8dc490
    kan "You're the one who insisted on abandoning your old identity and with it, any connection to me." id life_1_da75a0e9
    kan "You made that very clear." id life_1_9ed54c34

    mm "I'm not going to leave my kid in some strange place all by himself." id life_1_e239c06a

    n "I'm not your kid! And you're not a mom."

    show maimai oh

    mm "Of course I'm a mom." id life_1_1d2bdfd4
    mm "We'll work out the details later." id life_1_ab2d89f0
    mm "I have a full day ahead of me dropping off the rest of the rugrat felons, but I'll be back before you know it." id life_1_532b7ab4

    show ken

    kan "I agreed to claim to be taking care of the child." id life_1_3c010f27
    kan "You said nothing about living here." id life_1_be4471b7

    show maimai frown

    mm "I feel like you're hearing me, but you're not understanding." id life_1_ad3539d3
    mm "I am a new mom and we will talk about this later." id life_1_73a1b8b4

    show maimai smile

    mm "I'll see you soon, Nagen." id life_1_4255763e

    hide maimai
    hide ken

    "What happened to not leaving me alone in a strange place?"
    "The man sighs and lets me in anyway."

    scene backgroundMansion

    "Everything I own now fits inside my backpack, but I'm not sure where to put it."
    "He just stares at the closed door, potentially regretting his decision to let me in."

    menu:

        "Where am I staying?":

            show ken

            kan "Here, apparently." id life_1_b1edb688

            n "...In the hallway?"

            kan "Second floor, east wing, third room on the left side." id life_1_56bfd45d
            kan "It should have nothing terribly breakable in it." id life_1_580f73d3
            kan "Just don't touch anything outside of that room." id life_1_127c4077

            n "...Okay."

            "I go to leave, but he stops me."

            show ken talk

            kan "She didn't mention there were... others." id life_1_dc743400

            n "That's... kind of a long story."

            kan "Follow me, we need to talk." id life_1_14117ada

        "Who are you?":

            show ken

            kan "I'm a software engineer." id life_1_6f0efdf9

            n "That's it?"
            n "I find it really hard to believe Maimai would obsessively pursue some software engineer."
        
            kan "...That was my own doing." id life_1_82598262
            kan "I made the mistake of confusing a dark-web serial killer with an ARG and tried to set a trap for her so to speak." id life_1_e4561678

            n "You asked Maimai to target you on purpose!?"

            kan "In a way, yes. Though it's usually incredibly difficult to get her to show herself." id life_1_a035a97c
            kan "The question is, why is she risking that for you and your friends?" id life_1_e7146c08

        "Why are you doing this?":

            show ken

            n "Are they paying you to babysit me?"
            n "Or is it just because Maimai's blackmailing you?"

            kan "That woman couldn't blackmail me if she tried." id life_1_3f98975f
            kan "No one would listen to her." id life_1_163c7fd4

            n "Then why are you doing it?"

            show ken damn

            "He looks me over in disgust."

            kan "Occasionally her ramblings have merit." id life_1_735120ad

            n "She mentioned you owing her a favor."

            kan "She got me off Lethe's radar, I made the mistake of thanking her; now you're here." id life_1_5628757c

            "Lethe was after him too?"

            kan "You seem confused." id life_1_9005b9d3
            kan "Follow me, we have a lot to talk about." id life_1_c6fea334

    "I follow him into a cluttered study."
    "He takes a long drink of coffee before he sits down."
    "He prompts me to find a seat with a casual wave of his hand."

    kan "Liberation Army, hunh?" id prologue2_bbb5b131

    n "Junior Gladiators."

    kan "Same difference." id prologue2_1847cff7

    n "No, it's the Junior Gladiators, get it right."

    "The computer next to him roars to life."
    "He has no keyboard or mouse, yet it seems to be working just fine."
    "He stares me down across his empty desk."

    kan "You seem pretty proud of that." id prologue2_58e50c79

    n "Five kids bringing down an entire province is pretty impressive in my book."
    n "I was our lead strategist, so their success is my success."

    kan "Hmm..." id prologue2_38ab7775

    n "Odori was our leader."
    n "She was the one that saw potential in all of us."
    n "We trusted her with our lives and we let her down."
    n "She never wanted to be our leader, but Hiro and I basically made her be."
    n "Now she's gone."

    "I hate saying it like that."
    "I hate thinking about it like that, but after everything we lost, what we did had to mean something."

    n "I know she's out there somewhere. She has to be."
    n "She physically couldn't have run away, and no one can tell me where she is."
    n "So the least you could do is not treat me like some dumb kid while I'm waiting to hear if my friend is dead."
    n "For god's sake, we took over a whole damn province together!"

    kan "Are you finished?" id prologue2_00cdb1e9

    n "Uhh..."

    kan "Maimai's assumption is correct in one regard." id prologue2_fa102437
    kan "You are a child if you think anything you did in Guwon is worth celebrating." id prologue2_ee2438b2
    kan "Violence like that may be effective in the short term, but the damage always radiates far beyond your intended target." id prologue2_47c15d5c

    n "What else was I supposed to do, just accept my life as a lab rat?"

    kan "You need to divorce your attack on Guwon with your anger at Estella." id prologue2_5dec20ff
    kan "The two are not connected." id prologue2_a7fe3826

    n "Guwon profited off of Estella's caste system for generations."

    kan "Then you intended to harm countless innocents in your reenactment of Children of the Corn?" id prologue2_7e456b44

    n "No! It isn't that simple."

    kan "Then I suggest you think long and hard about what it was you were trying to accomplish before you defend your actions." id prologue2_f95572f9
    kan "Your methods clearly haven't taken you to where you wanted to go." id prologue2_222ca451

    "I just got here and he's already lecturing me about how disappointed he is in me."
    "At least we're on the same page about how much I want to be here."

    n "Is that all you want me to do?"

    kan "Keep a low profile for a month until school starts." id prologue2_1b29f6b0
    kan "You'll be staying at the dorms where they'll be able to keep a closer eye on you." id prologue2_9598c9ac

    n "Boarding school? Really!?"
    n "Guwon's government and supply chain is in shambles but hey, at least we still have boarding school."

    kan "McCarthy Academy is overseen by an old friend of mine." id prologue2_2760c3c1
    kan "It promises to be a safe place for survivors like yourself." id prologue2_d9f313cb

    n "I thought you were supposed to be doing that."

    "Great, I'm going to spend the next year getting shuffled around like old luggage."

    kan "I have to rebuild my company from the ground up since someone managed to break through our security system." id prologue2_04a5f0ab

    "Oh shit, don't tell me..."

    n "By company, you wouldn't happen to mean Ando Electronics... would you?"

    kan "Seeing as I'm the founder, yes. I was told you can be quite intelligent when you want to be." id prologue2_cfef000f
    kan "For your sake, I hope that's true. I don't enjoy gambling." id prologue2_380616d4

    "Gambling on what? What's this guy's deal?"
    "Maimai, why on Earth did you think this was going to be a good idea?"

    kan "It's been a long day. Go unpack your things, Maimai will handle the rest." id prologue2_da03f5b8

    "He proceeds to ignore me, opting to focus on his computer screen instead."

    n "Umm... where-"

    "He groans, rubbing his temples."

    kan "Second floor, east wing, third door on the left side." id prologue2_2193645d

    n "Right."

    "I high-tail it out of his office, eager to escape the oppressive air."
    "The room I've been given shares a striking resemblance to the one I grew up in as a kid."
    "It's not quite the same shade of blue and the books are too new to be mine."
    "It's equally eerie and comforting."

    hide ken

    scene backgroundblack

    play music "music/WhereS.mp3"

    "These hypocritical drones are spitting Lethe's memory when they worshiped her six months ago."
    "People treat her like she was some kind of psychopath, incapable of feeling anything for anyone."
    "Sure she had a Messiah Complex toward the end, but it's not like she didn't care about other people entirely."
    "I mean, she was the leader of the Karmic Gladiators; she devoted her life to helping people that everyone thought couldn't be helped."
    "She was everyone's hero, especially mine..."

    play music "music/Sappheiros.mp3"

    window hide
    scene backgroundP1 with fade:
        size (1920, 1080) crop (300, 400, 640, 360)

    o "Gladiators! You'll never believe the guest speaker I found for today's meeting!" id prologue2_2bfa7b67

    #[Pan out, Lethe is standing behind her, smiling]

    scene backgroundP1:
        size (1920, 1080) crop (300, 400, 640, 360)
        linear 2 crop (600, 0, 960, 540)

    l "Hello, little ones! It's so inspiring to see young people take an interest in our initiative." id prologue2_9a7f5aa7
    l "Even if my colleagues disagree, I think it's important to foster the growth of the industry." id prologue2_fa05e057
    l "After all, it's rare to see young people so devoted to liberating the justice system." id prologue2_d874f507
    l "Not many have what it takes." id prologue2_ed304292

    n "O-of course! I mean, who wouldn't want to become a real live hero?"

    scene backgroundP1:
        size (1920, 1080) crop (600, 0, 960, 540)
        linear 2 crop (0, 0, 1920, 1080)
    
    n "I can't believe you're actually here! We've mostly been planning. I mean, what else can we do?"
    n "But we've been working day and night on what we'll do as real heroes!"
    n "Not like a hobby... or anything... We meet everyday after school, and even longer on weekends."
    n "We can't use the classrooms, so we meet in the park!"

    "I started gathering the draft papers, but when I looked up at her face, she seemed so sad."
    "She took a seat at the table in silence."

    l "I ask this of all my fans, just as a formality..." id prologue2_96ceab93

    stop music

    l "Do you feel safe at home?" id prologue2_e12ba218

    scene backgroundP2 with fade:
        size (1920, 1080) crop (1100, 320, 528, 297)
        ease 20 crop (0, 0, 1920, 1080)

    play music "music/Nostalgia.mp3"

    "I became painfully aware of the IV that hid under my sleeve."
    "Had she noticed it? Was she going to tell anyone?"
    "If anyone found out, I could be taken away, or worse. What if she had already told someone?"
    "We all choked out an empty yes, but she wasn't satisfied."
    "She wanted to make sure I was safe when she left that room and somehow, she knew I had been lying."
    "All of us had, and it wouldn't surprise me if she had taken the others aside as well."
    "In her name, we fought for sanctuary from Estella Academy and the people who abused us."
    "The brainwashing of our peers was a little excessive, I'll admit, but how else would you be able to safely train middle schoolers for a civil war?"
    "We didn't have the luxury to make a boot camp with the city up in flames."
    "We worked with what we had, in the time we had..."

    play music "music/Undertow.mp3"

    "But that was the me of two years ago, the kid who grew up in a glass box waiting for my veins to stop burning."
    "The unwilling test subject of the very people who stand before me claiming I'm the monster."

    window hide
    scene backgroundblack
    with Dissolve(2.0)

    "A month goes by in a flash."

    window hide
    scene backgroundnhouse
    with Dissolve(3.0)
    
    play music "music/TheLoyalist.mp3"

    "The lingering winter nips at my cheeks as I watch the last of my things get packed into the cab."
    "A familiar feeling of helplessness washes over me."
    "There's nothing else I can do."

    show maimai at left_center

    show ken talk at right_center

    mm "Hey, it's going to be okay. Boarding school isn't that bad." id prologue2_5c5f6de6

    n "You don't know that."

    mm "Excuse me mister, but I have been to my fair share of reform schools." id prologue2_eea239ed

    n "Clearly they worked wonders."

    kan "All the more reason not to be scared." id prologue2_07c0cd54
    kan "This is only to show the courts you can behave for a long period of time." id prologue2_ab741f20

    n "...Can't I just stay here with you guys instead?"

    kan "I thought you hated being cooped up here." id prologue2_8433f1ae

    "I do."
    "I do hate it, but at least I know what to expect when I'm here."

    show maimai smile

    mm "You can come back during the break and I'll be going with you the first day to make sure the place is on the up and up." id prologue2_f889154e

    show ken

    kan "I assure you, it's a legitimate establishment." id prologue2_ef40a804
    kan "I wouldn't send him off if I wasn't familiar with the staff." id prologue2_275e155d

    "That's supposed to make me feel better?"

    scene backgroundcar

    play audio "car sedan door open 1.ogg"

    n "I hate this."
    
    show maimai frown

    mm "I know. Come on, the year will be over before you know it." id prologue2_aa7e1a52

    hide maimai
    hide ken

    "She herds me into the car with a forced smile on her face."

    scene backgroundcarin

    play audio "car sedan door shut 1.ogg"
    play sound "car_inside.ogg" loop

    "We drive a few hours to get to the school."

    scene backgroundtown
    with dissolve

    "Out my window were the decimated towns and scorched wastelands leading into the outskirts of Guwon."
    "Far from anyone else sat an old brick building."
    "It's one of the few buildings that survived the riots."

    stop sound 
    play audio "car sedan door open 1.ogg"

    scene backgroundschool
    with dissolve

    play music "music/TheySay.mp3"

    "I heard it was a library donated to the DVP for renovation and now it's become this."
    "I would have preferred the library."
    "It's no surprise, really, that this is where they planned to test their stupid program."
    "What confuses me is that I'm expected to act like an ordinary student."
    "I mean, our names were never released to the public, so it could work."
    "Something just seems... off."

    scene backgroundhall1

    "Each classroom has a transparent door with an electronic display built-in."
    "It feels more like an observation tank than a classroom."

    show maimai

    mm "The building had been a library since the 1600's." id prologue2_a712716c
    mm "I never got to see the inside, because the previous owner was such a nut job." id prologue2_5d2d2df2

    n "Why should I care?"

    show maimai smile

    mm "No, but do you think these bowties proofread every book in the building before bringing you in here?" id prologue2_3cccc1f3
    mm "Who knows what you could find!" id prologue2_61ff597f

    "I appreciate she's trying to make this sound like an adventure, but it doesn't change how... empty the school feels."
    "The second floor is for more specialized classes."
    "Along the west corridor are rooms for the fine arts and along the east corridor is a giant computer lab."
    "Large bay windows look out to the central courtyard."
    "We finally arrive at a large mahogany office door."

    show maimai frown

    mm "This is it." id prologue2_7dce6920
    mm "Promise you'll be on your best behavior?" id prologue2_82b2c62c

    n "...Why are you asking me that now?"

    "She searches for the right words to say."

    mm "I didn't want you to spend your time at the mansion worrying about school." id prologue2_b5f635a7
    mm "This place is the safest place for you to be right now, even if it's upsetting at times." id prologue2_73d1447e
    mm "Until they grant me full guardianship, my hands are tied." id prologue2_8d2073db

    n "...I promise I'll try."

    "Maimai escorts me into the office."

    hide maimai
    play music "music/Still.mp3"

    scene backgroundprincipal

    "A woman gestures for us to sit down. She takes her place behind a massive desk with a stack of forms for us to review."
    "The nameplate in front of her reads in gold letters 'Principal Vivaldi Thani'."

    n "....."

    "Vivaldi Thani, the chief officer sent to hunt down Lethe and her conspirators."
    "She was at the scene when Lethe... when she died."
    "I wouldn't have come if I knew she'd be here."
    "She's the last person I want to talk to."

    show vivaldi
    show maimai frown at left

    v "Is something wrong?" id prologue2_8f0b8338

    "It's like she doesn't even care."

    show maimai smile

    mm "He's just nervous because it's a new school." id prologue2_015bb72e
    mm "You know teenagers, all salty about change and stuff." id prologue2_95052a68

    "The principal is cold and composed, much like a statue."
    "I can't help glaring at her. The DVP had handed me over to the woman who set up Lethe and sabotaged our siege of Guwon."
    "How could she be so indifferent? Doesn't she recognize me at all?!"

    mm "So you're the principal?" id prologue2_d4d634e7
    mm "That's uh, quite a shift from being a police officer." id prologue2_58e34f2d

    "I've never seen Maimai so nervous before."
    "Is she scared of this woman? Or just psychics in general?"
    "She hands us papers to sign, with Maimai trying to stay as far away from the woman's hands as possible."
    "My phone is confiscated and replaced with a cheap knock-off to use while on campus."

    v "Detective. I grew tired of locating criminals after they committed crimes." id prologue2_8b233c3e

    "Locating? Is that what she calls what she did? Locating criminals?"
    "Lethe was- She watched them kill her with that indifferent stare on live television."
    "We get up to leave. I can't hold my tongue any longer."

    scene backgroundP3 with dissolve:
        size (1920, 1080) crop (320, 204, 1280, 816)

    n "You ruined my life."

    mm "Nagen, please." id prologue2_28f173df

    scene backgroundP3:
        size (1920, 1080) crop (320, 204, 1280, 816)
        linear 1.5 size (1920, 1080) crop (0, 0, 2400, 1525)


    n "No, because of her stupid feud, I lost both my mentor and my best friend in one night."
    n "Just because I have to be here doesn't mean I have to play along with her revenge fantasy."

    v "This isn't supposed to be a punishment, Mr. Tesuta. Your school life will be what you make of it." id prologue2_97d59531
    v "I trust you will do everything in your power to avoid ending up in my office again. Good day to you both." id prologue2_c5ece82f

    hide vivaldi
    hide maimai

    scene backgroundhall2

    "I practically get pushed out of the room by Maimai."
    "The wooden doors slam shut, but her hands never leave my shoulders."

    show maimai

    mm "I know you're a smart kid, so please... please don't go starting fights you can't finish." id prologue2_911151a6

    n "You can't leave me here with her- You knew she'd be here!"

    mm "It's part of your plea bargain, I can't pull you out even if I wanted to." id prologue2_293acdcf
    mm "I'm not your legal guardian yet." id prologue2_5af6c118

    n "She's going to set me up to fail."
    n "You can't expect me to believe she's okay with helping someone who trashed their hometown."

    show maimai frown

    mm "I don't. That's why you need to be careful." id prologue2_f009dcdf
    mm "These people stand more to gain from your success than your failure, but I can't guarantee their motives are good-intentioned." id prologue2_0235a97e
    mm "We have to meet them halfway." id prologue2_df94b175

    n "You know I don't like being alone."

    mm "I'm sorry." id prologue2_10cc5cff
    mm "I'm sure there are a lot of troubled kids who could benefit from a school like this." id prologue2_d3a502d4

    "Each word is slow and deliberate."

    show maimai smile

    mm "I'm sure you'll find some good friends here." id prologue2_98d7c2ba

    "She finishes with a wink and finally I understand."
    "My old teammates could be here too."

    n "Are they really-"

    "Still, to cut me off like that, it must mean I was right."
    "They're here. Somewhere in this god-forsaken reform school, I'll find my friends."

    mm "You got this." id prologue2_16262522

    hide maimai

    scene backgroundschool
    with dissolve

    "We go back to the car to get the last of my things."
    "She wraps me in a huge hug and I become very aware of the car coming up to the roundabout."

    scene backgroundcar

    n "Maimai, please-"

    show maimai smile

    mm "Be safe. Call me if anything happens." id prologue2_366609f1
    mm "I want to hear from you at least once a week, mister." id prologue2_368d150e

    show maimai frown

    mm "I mean it. Don't go forgetting about me, okay?" id prologue2_17e8ac34

    n "Okay, okay, people are staring."

    "I brush her off and collect my bags."

    n "I'll miss you too."

    hide maimai

    scene backgroundschool

    "I really don't want to go, but I can't keep putting it off."
    "We say our final goodbyes and I watch as the car drives off. Tomorrow will be my first day of school."
    "I can see other kids unloading their luggage and milling about the grounds. Now would be a good chance to find my friends."

    stop music

    jump chapter_one