    # Opening video goes here.

label prologue:

    scene backgroundDisc1

    g "Click to continue."

    scene backgroundDisc2

    g "Click to continue."

    play music "music/Undertow.mp3"
    scene backgroundpolice

    "My whole life, I feel like I've been dragged around by my collar."
    "I guess when most adults see a kid act out of line, they're overwhelmed with a need to control the situation."
    "Funny, seeing as that's the very thing I've been fighting for: a chance to be in control of my life."

    show CopBase

    voice "audio/cop/prologue_b121c771.ogg"

    cop "Please state your name and registered Proficiency."

    n "My name is Nagen Tesuta."
    n "I possess an Intelligence Proficiency."
    n "Anything I see, hear, or experience is recorded in perfect detail."

    hide CopBase

    "I tap the side of my head."
    "Having a great memory doesn't really make me smarter than anyone else, but the ability falls under the Intelligence major."
    "People are just so determined to classify things so they can feel important, they stop asking whether it's worth the effort."
    "I mean, some people can go their whole lives without realizing they have a Proficiency."
    "It's nothing special. The only reason I know about mine is because I was groomed to have it."

    show CopBase

    voice "audio/cop/prologue_3787084e.ogg"

    cop "Look, you and I both know it's not looking good for you."

    voice "audio/cop/prologue_c616cfd6.ogg"

    cop "I mean, you've heard the charges: premeditated murder, inciting a riot, mayhem, and menticide."

    voice "audio/cop/prologue_279523b4.ogg"

    cop "These are all with a registered Proficiency which will add twenty-five more years to your sentence."

    voice "audio/cop/prologue_559297ff.ogg"

    cop "Don't even get me started on the use of deadly weapons."

    show KoeBase

    ka "There's more than enough evidence to try you and your cohorts as adults."
    ka "In the case of The Supreme Court vs. Lethe, vigilantism was determined to be a Class One felony."
    ka "Some of her sympathizers, like you, seem to think they are above the law."
    ka "If we were able to find her remaining supporters, it would be an excellent demonstration of goodwill."
    ka "We all remember-"

    hide KoeBase

    scene backgroundblack

    # Change soundtrack
    play music "music/WhereS.mp3"

    "Remember? No one is truly capable of remembering."
    "Well, if you want to get technical, remembering is just being aware of something."
    "But people seem to think that it means they can recall the past in perfect clarity, ignorant of how time and their own perception taints everything that enters their mind."
    "These hypocritical drones are spitting on the name of the very woman they worshiped six months ago."
    "People treat her like she was some kind of psychopath, incapable of feeling anything for anyone."
    "Sure she had a Messiah Complex toward the end, but it's not like she didn't care about other people entirely."
    "I mean, she was the leader of the Karmic Gladiators; she devoted her life to helping people that everyone thought couldn't be helped."
    "She was everyone's hero, especially mine..."

    #(Flashback)

    #[CG: Young Odori with Lethe]

    play music "music/Sappheiros.mp3"
    scene backgroundP1 with fade:
        size (1920, 1080) crop (300, 400, 640, 360)

    voice "audio/Apex/prologue_2bfa7b67.ogg"

    o "Gladiators! You'll never believe the guest speaker I found for today's meeting!"

    #[Pan out, Lethe is standing behind her, smiling]

    scene backgroundP1 with fade:
        size (1920, 1080) crop (300, 500, 640, 360)
        linear 2 crop (600, 0, 960, 540)

    l "Hello, little ones! It's so inspiring to see young people take an interest in our initiative."
    l "Even if my colleagues disagree, I think it's important to foster the growth of the industry."
    l "After all, it's rare to see young people so devoted to liberating the justice system."
    l "Not many have what it takes."

    n "O-of course! I mean, who wouldn't want to become a real live hero?"
    scene backgroundP1 with fade:
        size (1920, 1080) crop (600, 0, 960, 540)
        linear 2 crop (0, 0, 1920, 1080)
    n "I can't believe you're actually here! We've mostly been planning. I mean, what else can we do?"
    n "But we've been working day and night on what we'll do as real heroes!"
    n "Not like a hobby… or anything… We meet everyday after school, and even longer on weekends."
    n "We can't use the classrooms, so we meet in the park!"

    "I started gathering the draft papers, but when I looked up at her face, she seemed so sad."
    "She took a seat at the table in silence."

    l "I ask this of all my fans, just as a formality..." 

    stop music

    l "Do you feel safe at home?"

    scene backgroundP2 with fade:
        size (1920, 1080) crop (700, 200, 640, 360)
        linear 4 crop (0, 0, 1920, 1080)


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
    "We worked with what we had, in the time we had…"

    scene backgroundpolice

    play music "music/Undertow.mp3"

    "But that was the me of two years ago, the kid who grew up in a glass box waiting for my veins to stop burning."
    "The unwilling test subject of the very people who stand before me claiming I'm the monster."
    "Back before the Department of Villain Prevention was a governing body under Estella's control."

    n "I know you. You were the prosecutor during Lethe's trial."
    n "Trying to extort information out of a child for your old department? That's surprisingly underhanded of you."

    show KoeBase

    ka "Then you understand what you're up against."
    ka "Choosing to represent yourself in court only gave you a fool for a client."

    "She's the prosecutor for my case!?"

    ka "I'm just doing my job, Mr. Tesuta, in ensuring I have all the information I need for my case."
    
    hide KoeBase
    show CopBase

    cop "Just make this easier on yourself and fold. It'll be better than what your friends are going through."
    hide CopBase

    #[Player Choice]

    menu:
        "Confess everything": #(-Hiro)
            $ hRep -= 1
            n "Yeah, I did it, everything you said is true."
            n "I helped start the riots to take down Estella and her talent mills."
            n "You want the names of all the adults that worked with her, right?"
            n "Fine. Just don't throw the book at me."
            n "We both know this is shady as hell."
            n "I'll parrot any garbage you want me to say after I get my sentence."

            jump interrogation_end

        "Refuse": #(Fast forwards past all choices, all points put in Intelligence)
            $ Intel += 4
            jump interrogation_1

    label interrogation_1:

    n "Good cop, bad cop? Really?"
    n "I'm sorry, it's going to take more than a movie cliché to get me to tell anyone anything."
    n "Also, I was never read my rights, so unless you want a mistrial, I suggest you start treating me like an adult before trying me like one."

    show CopBase
    cop "That's not how the system works, kid."

    hide CopBase
    show KoeBase

    ka "No, he has a valid point. You want to be talked to like an adult? Fine."
    ka "Mr. Tesuta, if you don't give us the information we need, there will be no 'deal'."
    ka "The first step is pleading guilty in court. There is no workaround."

    "So it's her way or no way, hunh? Fine, whatever, she has her reasons; I have mine."

    hide KoeBase

    #[Player Choice]

    menu:
        "I have to protect my teammates": #(+Hero, +Vis)
            $ Hero += 1
            $ Vision += 1
            n "I'll plead guilty in court, but I and I alone am guilty of these charges."
            n "I cannot say the same of my friends; they genuinely believed in what Lethe told them..."

            "If I lie, I could be held in contempt of the court, but if I play the 'scapegoat', maybe they can get out of here unscathed."
            "Either way, someone has to answer for what we did."

            jump interrogation_2

        "I don't have a choice": #(+Villian, +Vig)
            $ Villain += 1
            $ Vigor += 1
            n "Under the advice of my legal counsel, I will."

            "Maimai would be heartbroken if I got locked away. She's been through this before."
            "I practically have a walkthrough written on my sleeve."

            show CopBase

            cop "Do you believe you are guilty of these crimes?"

            n "....."

            "I've talked too much already. Isn't the confession enough?"

            hide CopBase

            jump interrogation_2

        "It's all part of the plan": #(+Int)
            $ Intel += 1
            n "I'll cooperate."

            "It's too dangerous to make a move now. Best to play along for now."

            jump interrogation_2

        "I need to lighten my sentence": #(+Chr)
            $ Charm += 1
            n "...okay..."

            "I hang my head at a 30-degree angle and feign the slightest tremor in my shoulders."
            "The more sympathy I can gain, the better."
            "No one will want to hear my side of the story if I act like the violent criminal they think I am."

            jump interrogation_2

    #[Return to Main Branch]
    label interrogation_2:

    n "I fully understood the ramifications of my actions and stand at the mercy of the court."
    n "I aided in the brainwashing of my classmates and tried to conquer the Guwon Province for my own benefit."

    show CopBase

    cop "That's all we need to hear."

    show KoeBase

    ka "Not quite. I still have a few questions for Mr. Tesuta."
    ka "The Junior Gladiators started as a club at your school, later to fall down a path of destruction."
    ka "And yet, no one can tell us whose fault this was."
    ka "In your estimation, who was the leader during the attack?"

    hide KoeBase

    #[Player Choice]

    menu:
        "The one who told us to kill": #(+Chr)
            $ Charm += 1
            n "Lethe was. She wanted to create a group of youth vigilantes to gain back public support."
            n "It wasn't until after she died that we realized she was the one who started the chaos."

            "Chaos is putting it lightly."
            "She tried to get people to lynch anyone who was above average at... well... anything."
            "It nearly destroyed the nation."
            "Of course, if you really look at it, she wasn't wrong."
            "Proficiencies were dangerous to the general public, but so is a pen if you use it correctly."
            "These people, however, just want to confirm what they already believe, so I'll just tell them what they want to hear."

            jump interrogation_3

        "The one who gathered the army": #(+Hero, +Vig)
            $ Hero += 1
            $ Vigor += 1
            n "Hiro Morine was our leader. He insisted on it constantly."
            n "If it wasn't for him, we wouldn't have gathered nearly as much support."

            "He wasn't a very good leader after that..."
            "Actually, I was the one who did all the real work, but he meant well."
            "He was the first one of us to get captured by these hypocrites."
            "Even after getting dragged down, he insisted on taking credit for what happened. I hope he's okay."

            jump interrogation_3

        "The one who planned the attack": #(+Int)
            $ Intel += 1
            n "I was. I deliberately withheld information from my peers, knowing it would sway their decision to stay."
            n "In the end, I was the only one standing."

            "Well, not exactly standing. Let's just say, I don't handle failure very well."
            "I was lucky Maimai was crazy enough to spare my life."
            "If I manage to get out of this, I should thank her properly."

            jump interrogation_3

        "The club president": #(+Vis)
            $ Vision += 1
            n "Odori Hato was our leader. She's the one who brought Lethe's attention to our club."
            n "Odori just wanted to help us and a cheesy superhero club was her answer."

            "After Lethe died, she insisted we continue with our plans so that everyone would be happy again."
            "It's amazing how far out of hand things got."

            show CopBase

            cop "Do you know where Ms. Hato is?"

            n "No, she's not with us anymore."

            "I want to believe she's still out there, but…"

            hide CopBase

            jump interrogation_3

    #[Return to Main Branch]
    label interrogation_3:

    show KoeBase

    ka "You were apprehended by Vivaldi Thani before you were able to carry out your plan to completion, correct?"

    n "Yes."

    ka "What did you intend to do once you took over the city?"

    hide KoeBase

    #[Player Choice]

    menu:
        "Fortify the city against my enemies": #(+Villain, +Vig)
            $ Villain += 1
            $ Vigor += 1
            n "I just wanted a place where I could feel safe. Anyone there was free to leave, but they chose to stay."
            n "They took up arms, and I had to defend myself."

            show KoeBase

            ka "According to eyewitness testimonies, you sought out innocent civilians who were in hiding and killed them on sight."
            ka "We found seventeen assault rifles in your room. Were these also for your defense?"

            n "Yes."

            "It's not like I bought the guns online or anything. Guwon was already a dangerous place to live."
            "If you were alone on the street for over twelve hours, you could get killed or worse."
            "Wandering around the city with a gun was safer than going back home anyway."
            "I had all kinds of other machines I was playing with that I got from the junkyard, but that's not what they care about."

            ka "Did you use any of these guns against another person?"

            n "Yes."

            hide KoeBase

            jump interrogation_4

        "Rebuild the city": #(+Hero, +Int)
            $ Hero += 1
            $ Intel += 1
            n "Before making any plans, I would have had to reverse the damage that had been done."
            n "I was in command of over five hundred people; they needed a place to live once the dust settled."

            show KoeBase

            ka "That's all?"

            n "Well, we would have needed a hospital next as well as to secure some kind of agricultural production to feed everyone."
            n "That alone would have taken months, and who knows what other problems may have arisen."

            "What can I say, I read way too many doomsday zombie comics as a kid."
            "If I wanted to be a good leader, I had to make sure my people were provided for."

            ka "This would be the same city you planned to bomb, correct?"

            n "I wouldn't say that bombing the entire city was the plan, but I would say that arming every soldier with TNT definitely reduced the number of casualties on our end."

            "I tried my best to keep everyone safe, even if it meant lying. I can't let them down now."

            hide KoeBase

            jump interrogation_4

        "Rebuild society in my vision": #(+Villain, +Vis)
            $ Villain += 1
            $ Vision += 1
            n "Guwon was an experiment to see if we truly were capable of reshaping society."
            n "It was supposed to show the might of our nation's youth, that we were something bigger than everyone else said we were."
            n "The experiment failed."

            "I would have loved to see it spread past Guwon, but the opportunity never presented itself."

            show KoeBase

            ka "Lethe had similar ideals. She thought that turning citizens against each other would weed out the weak."

            n "No. Lethe thought society was beyond saving and proved that one spark could bring it crumbling down, which is why you have a job today."
            n "I believe that people can coexist, we just need to modify a few rules."

            "Lethe was right, the system had become too polluted, but destroying the world isn't the answer."
            "If you try to kill a virus, it will come back stronger and nothing will change."
            "In order to take it down, you have to integrate into its life cycle and prevent it from reproducing."
            "I just tried to do so from the wrong angle. Next time, I won't be so sloppy."

            hide KoeBase

            jump interrogation_4

        "I don't know": #(+Hero, +Chr)
            $ Hero += 1
            $ Charm += 1
            n "....."

            show CopBase

            cop "Mr. Tesuta, please answer the question."

            n "...I didn't. I mean, part of me thought it would never work... I just... did what I always did..."
            n "I never questioned why or what came next."

            hide CopBase
            show KoeBase

            ka "And what would that be?"

            n "Hunh? Oh… nothing. Nothing was planned after that… I just did what I was told."

            "I just wanted to make everyone happy."
            "I thought if we took down the city together, we'd get some kind of happily ever after."
            "That's just not how the world works. There is no 'after'."
            "Just now and everything that has since passed. I have to do what I can so that 'now' doesn't get me killed."

            hide KoeBase

            jump interrogation_4

    #[Return to Main Branch]
    label interrogation_4:

    show KoeBase

    ka "And what exactly was your end goal in all of this?"

    n "Excuse me?"

    ka "Why did you attack Guwon in the first place? Such extreme actions had to come from somewhere."
    ka "It's not every day a middle school student attempts to destroy a city."

    n "Guwon had to be brought down!"

    ka "Why?"

    hide KoeBase

    #[Player Choice]

    menu:
        "It was corrupt": #(+Hero)
            $ Hero += 1
            n "Guwon's entire economy was based around the manufacturing and propagation of Proficiencies."
            n "They treated us like livestock! We were paraded about as status symbols and meal tickets."
            n "No one cared what happened to us."

            show KoeBase

            ka "There is no need for dramatics, Mr. Tesuta."

            n "Dramatics? Are you even listening to what I'm saying?"
            n "The Estella school system picked kids out and did whatever it took to show that their school improved the abilities of 'gifted' children."
            n "We were their guinea pigs to flaunt to the media and nothing was below them as long as it produced results."
            n "Someone had to stop it."

            ka "I find it hard to believe that Estella would do anything that would harm their students, Mr. Tesuta."
            ka "If there was truly such a problem, you should have gone to the police."

            n "They didn't listen, no one does! I'm not making this up, my parents worked there."
            n "I knew better than anyone what was going on and you did nothing! Eight anonymous tips and zero investigations."
            n "No one even looked. I had to do something, anything!"

            ka "So you were angry at the Estella faculty and those who ignored you."
            ka "Most children in that situation would simply run away; you stayed and killed anyone who opposed you."

            n "I did run away. Lethe was the one who came after me."

            "She was the one who told us to stand up and fight for what we believed in."
            "That when the dust settled, the strongest would be left standing. Even if I lost, I'm still here."

            hide KoeBase

            jump interrogation_end

        "It was convenient": #(+Villain)
            $ Villain += 1
            n "Where else was I supposed to start? Guwon was my home."
            n "I had never been outside of my hometown and it was as good a place as any."

            show KoeBase

            ka "For what?"

            n "A blank slate. An area untouched by the stigmas of adults."
            n "Where governing bodies are chosen based on who is the most capable, not the most likable."
            n "We need to exhume these archaic standards and start from scratch."

            ka "There is no such thing as a blank slate, Mr. Tesuta. An ageist cleanse of the area is not a plan to be taken lightly."

            n "Don't put words in my mouth. Anyone who wanted to could leave; I merely claimed the area as my own."

            ka "Your peers weren't allowed to leave."
            ka "We have rescued hundreds of children from those delightful obedience collars."

            n "Education collars, actually, though I do take issue with your tone."
            n "You act like I was the one who made them."
            n "Quite the opposite, as it was your technology we were using."
            n "So before questioning how I used it, shouldn't you be asking why it was made in the first place?"

            hide KoeBase

            jump interrogation_end

        "It was safest": #(+Villain)
            $ Villain += 1
            n "Guwon is water locked, it would be the easiest to fortify."
            n "With what Odori had planned, we couldn't just set up shop anywhere. It had to be someplace secure."

            show KoeBase

            ka "What exactly did she have planned?"

            n "We were going to finish what Lethe started."

            "I can't exactly tell them that they were specifically our target."
            "They were the ones who called for Lethe's head."
            "They're probably asking these questions to see if everyone keeps the same story. That's fine, I can play along."
            "As long as even one of us makes it out of here, these people are going down."

            n "I wasn't exactly sure, but Odori assured me that the end justifies the means."

            ka "You expect us to believe that you were blindly following orders?"

            n "I'm just the tactician. You asked me why I picked Guwon, I told you."
            n "It was the most pragmatic decision."
            n "I believed Lethe had our best interests in mind, same as you believe she was a monster."

            hide KoeBase

            jump interrogation_end

        "To end the war": #(+Hero)
            $ Hero += 1
            n "Everyone was fighting each other, not just us."
            n "This is just an isolated incident among many that happened during the battle between Lethe and the Karmic Gladiators."
            n "Even after she was gone, people were still fighting each other."
            n "I believe it's the entire reason your department exists, madam Vice President."

            show KoeBase

            ka "Our department exists to regain peace, not to insight riots in the streets."

            n "Then why did it take our riots for you to turn your attention to Guwon?"
            n "It was home to a well-known weapons manufacturer at the time."
            n "Once we cut off their exports, suddenly you guys were able to regain control of the populace."

            ka "We needed to restore order. Doing so takes time and hard work."
            ka "We turned our attention to Guwon next due to the number of casualties, not because of any vigilante interference."

            "She spits out the words as if they're acid." 
            "It's clear I'm getting nowhere with this woman."

            n "Casualties were bound to happen, you're assuming our activities caused more."

            hide KoeBase

    #[Return to Main Branch]

    # Error, if we run out of story, it leads us back here?
    label interrogation_end:

    show KoeBase

    ka "I rest my case. It is clear that Nagen Tesuta is guilty of all crimes, and shows no remorse for what he has done."

    "Wait a minute, that's it!"

    # Add SFX

    n "Objection!"

    hide KoeBase
    show CopBase

    cop "That's not how an interrogation works, Mr. Tesuta."

    n "S-sorry. It's just, wasn't the purpose of this case to determine whether or not the Junior Gladiators lead to people dying?"
    n "None of the prosecution's questions have been relevant to the charges at hand; they've been about my character."
    n "In fact, all of Ms. Amagi's questions were about proving that my group was malicious and dangerous to society."

    hide CopBase
    show KoeBase

    ka "This is outrageous and highly unprofessional."

    n "If this is indeed a trial to prove that my group committed atrocities in Guwon Province, then there is more than enough evidence to support the charges."
    n "However, it seems the prosecution wants to prove that my friends and I are, to put it plainly, evil."
    n "And for that, there is not enough evidence."

    "I already made a deal with the DVP to pardon my crimes in exchange for information on the location of the remaining Karmic Gladiators."
    "There's something else she's been trying to fish out of me, but I can't figure out what it could be."

    n "I want to change the terms of the deal."

    ka "You mean the plea bargain?"

    n "Right, that. I know that my friends and I, we're good people deep down."
    n "We just got caught up in something bigger and scarier than us and we did what we could to stay alive."
    n "The same can be said of any criminal of war. If you need someone to blame, then blame the adults."
    n "Just drop the charges against my team members."

    ka "I'm listening."

    n "I am fully aware that someone has to atone for what happened in Guwon." 
    n "No amount of apologizing can erase that."
    n "The people you want to put behind bars are the adults that helped Lethe."
    n "The ones who destroyed everything, not just Guwon. I can tell you where they are."
    n "Just let me and my friends go."

    ka "And how do you expect us to believe your group is so blameless?"

    n "....."

    "Shit, I thought I had her!"

    ka "The DVP has a program for troubled teens."
    ka "So far, we have been unable to gather any evidence that proves the program is effective."
    ka "We would like to use the Junior Gladiators as our focus group."

    "Wait a minute, what?"

    ka "If your members cooperate and complete the program, we will drop the charges."
    ka "Of course, the Junior Gladiators are officially disbanded and will not be allowed to continue any further activities."
    ka "You will be under constant surveillance as a part of the observational study and to prevent skewed data, they will not know about the experiment."

    "Woah, woah, woah. A; that is highly unethical and B; why's the cop gone silent?"
    "Did I just play into this lady's hand? No way."
    "I mean, yeah I wanted to get my friends out of this, but I didn't want to make them into guinea pigs like me."
    "There's no telling what these people might do for the sake of 'science'."


    hide KoeBase
    show CopBase

    cop "The terms have been set."
    cop "If the Junior Gladiators complete the DVP's Villain Prevention Program and can prove they can integrate back into society, they will be issued a full pardon."
    cop "If they are unable to do so, they will be tried as adults for their crimes in Guwon."
    cop "Do you agree to these terms?"

    n "Yes."

    "It's not like I really have a choice anyway."

    cop "Then it's settled. A follow-up hearing will be scheduled in one year to document your progress."
    cop "In the meantime, you will be appointed a guardian from the DVP to take care of you during your time in the program."

    "Unbelievable. Fucking unbelievable."
    "I thought for once I could outsmart these assholes and get out of all this. No, this is not over."
    "A year is a long time. I'm sure I will be able to think of something."

    cop "Your guardian is waiting."

    hide CopBase

    #Life at the House (scene 2)

    #[BG: Car Exterior]

    scene backgroundcar

    play music "music/leaf.mp3"

    "A black limo is waiting for me out back."
    "What's the point of sneaking me out with the trash if they're going to send a nice car?"
    "It feels like stepping into this car might be the last thing I get to do."
    "Regardless of my hesitation, I'm ushered into the back seat by the bailiffs and greeted by none other than the Medusa Killer."

    #[BG: Car interior]

    scene backgroundcarin

    n "Maimai?"

    #[Sprite: Maimai]

    show MMBase

    mm "The one and only."

    n "You're my appointed guardian? This has to be a mistake, you're a registered villain."

    mm "The Medusa Killer is a registered villain who's gone MIA. I'm Maimai."
    mm "See, I've got glasses and everything, no one can tell the difference."
    mm "Either way, I haven't seen you since pulling you out of a war zone and this is the hello I get?"

    "I ended up in a dark room with two vultures circling me thanks to her 'help'."
    "She promised she wouldn't leave my side until I was safe."

    mm "Don't give me that look, you're fine."

    n "You still haven't told me why they sent you."

    mm "They thought a friendly face would keep you from bolting out of the car."

    n "And the stupid glasses?"

    mm "A sign of my sincerity. My hypnotic stare only works when you can see my eyes."
    mm "If I was planning to force you to cooperate, you'd be drooling on the floor by now."

    "Her hypnosis was terrifying to experience first hand, especially knowing for five other victims, it was the last thing they experienced."
    "In my attempt to seize control of Guwon, I had put myself in the crosshairs of a dark-web serial killer when I endangered her next target."
    "I thought she'd be out for my blood, but she felt bad for me, I guess."
    "I'd like to believe she cares for me deep down, but maybe she's completely delusional. I wouldn't rule out both."

    n "This is the most normal I've seen you look... ever."

    mm "After those DVP schmucks found out my methodology, I had to retire from stuffing orchids down criminals' windpipes and ditch the costume."
    mm "Besides, it wasn't suitable for my new role."

    hide MMBase

    #[Player Choice]

    menu:
        "New role?": #(+Chr)
            $ Charm += 1
            show MMBase

            mm "Pantsuit, short hair, dorky accessories; I'm one minivan away from perfection."

            "This is her idea of what a mom looks like?"

            n "I'm flattered, but I need a couch to crash on, not a parent."

            mm "That's not what the state says."
            mm "You want to get out of this mess unscathed, then we gotta go full nuclear. Nuke the situation beyond recognition."

            n "You do realize a nuclear family has two parents, right?"
            n "Please tell me this isn't going to be one of those 'Weekend at Bernies' things where you dress up a dead body to be my dad or something."

            mm "I didn't even think of that!"
            mm "It could work... but no, I found a living option and on my honor, he will remain a living option."

            n "A friend of yours from your dark web days?"

            mm "Yeah, we go way back."

            n "I think the dead body would be safer."

            hide MMBase

            jump life_1

        "Where are we going?": #(+Int)
            $ Intel += 1
            show MMBase

            mm "Someplace safe."
            mm "The DVP would like you to believe the best place for you is with them; they're only half right."

            n "So we're running from the DVP again."

            mm "This is a little different than huddling around a flaming oil drum in an abandoned alleyway."
            mm "Going off-grid isn't going to help us now. We need to leach from the immunity capitalism offers."
            mm "Money may not buy happiness, but it sure as hell can buy you protection."

            "Well that kinda explains the car."

            n "Whose limo is this?"

            mm "...an old target's decided to be quite hospitable."

            n "What the- Oh my god, you're blackmailing the poor man."

            mm "I'm not a monster! It's more complicated than that. You just gotta trust me."

            hide MMBase

            jump life_1

    #[Return to Main Branch]
    label life_1:

    show MMBase
    
    mm "I had to cash in an old favor to get us out of this mess."
    mm "I was hoping to leave his debt dangling over his head for a few more years, but this is more important."
    mm "You need a proper guardian and as much as I'd love to take care of you myself..."
    mm "I don't have a legal job, or house, or any of the tools that would let the state give me guardianship."

    n "I'm not a child."
    n "I appreciate everything you've done for me, but you'll have to forgive me for not fully trusting you or this other person."

    mm "I just want what's best for you. Please, just give this guy a chance."
    mm "I will be with you the whole time. He's... he's a bit of a potato, but he'll treat us well."

    n "...Potato?"

    mm "Boring, acidic, lives somewhere dark and hard to find. A potato."

    n "...Right..."
    n "Has anyone heard from Odori?"

    mm "No, I'm sorry."

    n "You sure it's not classified or something?"

    mm "If it was classified, I would have told you it's classified."

    # Needs new song queue, something sad?
    play music "music/Still.mp3"

    "A month. She's been missing for over a month."
    "At this point, they're not looking for {i}her{/i} anymore, they're looking for a body."
    "My mouth's gone dry. I don't want to be here."
    "She should be in a limo on her way to a new home, not me."

    mm "Nagen honey, remember to breathe. We're not going to get out of the car until you're ready."

    #[BG: Manor Exterior]

    scene backgroundnhouse
    play music "music/LateNights.mp3"
    
    "As we step out of the car, I can smell the faint, eerie scent of velvet kiss growing up by the walkway."
    "The dreary gray estate looms in front of me. Utterly unwelcoming."

    mm "Now we just gotta find a way in!"

    "Maimai's exuberance clashes with the apathetic surroundings."
    "Her violently pink attire is giving me a migraine."

    n "He is expecting us, right?"
    n "You didn't just stalk the man... did you?"

    mm "No... kind of."

    "Of course. Why would I expect any different?"
    "I stumble after her through the leaves."
    "With her bottom lip clenched between her teeth, she fishes a metal chain out of the overgrowth of trees and pulls."
    "The building groans as a sizable bell rings from a tower above the gate."
    "When the door opens, I begin to understand why Maimai described my appointed guardian as a potato."

    show MMBase

    mm "Surprise!"

    hide MMBase
    show KenzoBase

    kan "What part of this arrangement involved you coming here?"

    n "I knew it! He wasn't expecting us at all!"

    hide KenzoBase
    show MMBase

    mm "Well, he was expecting you."

    hide MMBase
    show KenzoBase

    kan "...That's the kid?"

    hide KenzoBase
    show MMBase

    mm "He claims otherwise, but yes, this is him."
    mm "Don't worry, in this big ol' house, you'll hardly notice us."

    hide MMBase
    show KenzoBase

    kan "Us?"
    kan "You're the one who insisted on abandoning your old identity and with it, any connection to me."
    kan "You made that very clear."

    hide KenzoBase
    show MMBase

    mm "I'm not going to leave my kid in some strange place all by himself."

    n "I'm not you kid! And you're not a mom."

    mm "Of course I'm a mom."
    mm "We'll work out the details later."
    mm "I have a full day ahead of me dropping off the rest of the rugrat felons, but I'll be back before you know it."

    hide MMBase
    show KenzoBase

    kan "I agreed to claim to be taking care of the child."
    kan "You said nothing about living here."

    hide KenzoBase
    show MMBase

    mm "I feel like you're hearing me, but you're not understanding."
    mm "I am a new mom and we will talk about this later."
    mm "I'll see you soon, Nagen."

    hide MMBase

    "What happened to not leaving me alone in a strange place?"
    "The man sighs and lets me in anyway."
    "Everything I own now fits inside my backpack, but I’m not sure where to put it."
    "He just stares at the closed door, potentially regretting his decision to let me in."

    #BG Interior

    menu:

        "Where am I staying?":

            show KenzoBase

            kan "Here, apparently."

            n "...In the hallway?"

            kan "Second floor, east wing, third room on the left side."
            kan "It should have nothing terribly breakable in it."
            kan "Just don't touch anything outside of that room."

            n "...Okay."

            "I go to leave, but he stops me."

            kan "She didn't mention there were... others."

            n "That's... kind of a long story."

            kan "Follow me, we need to talk."

            jump prologue2

        "Who are you?":

            show KenzoBase

            kan "I'm a software engineer."

            n "That's it?"
            n "I find it really hard to believe Maimai would obsessively pursue some software engineer."
        
            kan "...that was my own doing."
            kan "I made the mistake of confusing a dark-web serial killer with an ARG and tried to set a trap for her so to speak."

            n "You asked Maimai to target you on purpose!?"

            kan "In a way, yes. Though it's usually incredibly difficult to get her to show herself."
            kan "The question is, why is she risking that for you and your friends?"

            jump prologue2

        "Why are you doing this?":

            show KenzoBase

            n "Are they paying you to babysit me?"
            n "Or is it just because Maimai's blackmailing you?"

            kan "That woman couldn't blackmail me if she tried."
            kan "No one would listen to her."

            n "Then why are you doing it?"

            "He looks me over in disgust."

            kan "Occasionally her ramblings have merit."

            n "She mentioned you owing her a favor."

            kan "She got me off Lethe's radar, I made the mistake of thanking her; now you're here."

            "Lethe was after him too?"

            kan "You seem confused."
            kan "Follow me, we have a lot to talk about."

            jump prologue2

label prologue2:

    "I follow him into a cluttered study."
    "He takes a long drink of coffee before he sits down."
    "He prompts me to find a seat with a casual wave of his hand."

    kan "Liberation Army, hunh?"

    n "Liberation Front."

    kan "Same difference."

    n "No, it's the Liberation Front, get it right."

    "The computer next to him roars to life."
    "He has no keyboard or mouse, yet it seems to be working just fine."
    "He stares me down across his empty desk."

    kan "You seem pretty proud of that."

    n "Five kids bringing down an entire province is pretty impressive in my book."
    n "I was our lead strategist, so their success is my success."

    kan "Hmm..."

    n "Odori was our leader."
    n "She was the one that saw potential in all of us."
    n "We trusted her with our lives and we let her down."
    n "She never wanted to be our leader, but Hiro and I basically made her be."
    n "Now she’s gone."

    "I hate saying it like that."
    "I hate thinking about it like that, but after everything we lost, what we did had to mean something."

    n "I know she’s out there somewhere, she has to be."
    n "She physically couldn’t have run away, and no one can tell me where she is."
    n "So the least you could do is not treat me like some dumb kid while I’m waiting to hear if my friend is dead."
    n "For god’s sake, we took over a whole damn province together!"

    kan "Are you finished?"

    n "Uhh..."

    kan "Maimai's assumption is correct in one regard."
    kan "You are a child if you think anything you did in Guwon is worth celebrating."
    kan "Violence like that may be effective in the short term, but the damage always radiates far beyond your intended target."

    n "What else was I supposed to do, just accept my life as a lab rat?"

    kan "You need to divorce your attack on Guwon with your anger at Estella."
    kan "The two are not connected."

    n "Guwon profited off of Estella's caste system for generations."

    kan "Then you intended to harm countless innocents in your reenactment of Children of the Corn?"

    n "No! It isn't that simple."

    kan "Then I suggest you think long and hard about what it was you were trying to accomplish before you defend your actions."
    kan "Your methods clearly haven't taken you to where you wanted to go."

    "I just got here and he's already lecturing me about how disappointed he is in me."
    "At least we're on the same page about how much I want to be here."

    n "Is that all you want me to do?"

    kan "Keep a low profile for a month until school starts."
    kan "You'll be staying at the dorms where they'll be able to keep a closer eye on you."

    n "Boarding school? Really!?"
    n "Guwon's government and supply chain is in shambles but hey, at least we still have boarding school."

    kan "McCarthy Academy is overseen by an old friend of mine."
    kan "It promises to be a safe place for survivors like yourself."

    n "I thought you were supposed to be doing that."

    "Great, I'm going to spend the next year getting shuffled around like old luggage."

    kan "I have to rebuild my company from the ground up since someone managed to break through our security system."

    "Oh shit, don't tell me..."

    n "By company, you wouldn't happen to mean Ando Electronics... would you?"

    kan "Seeing as I'm the founder, yes. I was told you can be quite intelligent when you want to be."
    kan "For your sake, I hope that's true. I don't enjoy gambling."

    "Gambling on what? What's this guy's deal?"
    "Maimai, why on Earth did you think this was going to be a good idea?"

    kan "It's been a long day. Go unpack your things, Maimai will handle the rest."

    "He proceeds to ignore me, opting to focus on his computer screen instead."

    n "Umm... where-"

    "He groans, rubbing his temples."

    kan "Second floor, east wing, third door on the left side."

    n "Right."

    "I high-tail it out of his office, eager to escape the oppressive air."
    "The room I’ve been given shares a striking resemblance to the one I grew up in as a kid."
    "It’s not quite the same shade of blue and the books are too new to be mine."
    "It’s equally eerie and comforting."

    scene backgroundnhouse
    play music "music/TheLoyalist.mp3"

    "The lingering winter nips at my cheeks as I watch the last of my things get packed into the cab."
    "A familiar feeling of helplessness washes over me."
    "There’s nothing else I can do."

    show MMBase

    mm "Hey, it’s going to be okay. Boarding school isn’t that bad."

    n "You don’t know that."

    mm "Excuse me mister, but I have been to my fair share of reform schools."

    n "Clearly they worked wonders."

    hide MMBase
    show KenzoBase

    kan "All the more reason not to be scared."
    kan "This is only to show the courts you can behave for a long period of time."

    n "...Can’t I just stay here with you guys instead?"

    kan "I thought you hated being cooped up here."

    hide KenzoBase
    show MMBase

    "I do."
    "I do hate it, but at least I know what to expect when I’m here."

    mm "You can come back during the break and I’ll be going with you the first day to make sure the place is on the up and up."

    hide MMBase
    show KenzoBase

    kan "I assure you, it’s a legitimate establishment."
    kan "I wouldn’t send him off if I wasn’t familiar with the staff."

    "That’s supposed to make me feel better?"

    scene backgroundcar

    n "I hate this."

    mm "I know. Come on, the year will be over before you know it."

    hide MMBase

    "She herds me into the car with a forced smile on her face."

    scene backgroundcarin

    "We drive a few hours to get to the school."
    "It’s one of the few buildings that survived the riots."

    scene backgroundschool
    play music "music/TheySay.mp3"

    "I heard it was a library donated to the DVP for renovation and now it’s become this."
    "I would have preferred the library."
    "It’s no surprise, really, that this is where they planned to test their stupid program."
    "What confuses me is that I’m expected to act like an ordinary student."
    "I mean, our names were never released to the public, so it could work."
    "Something just seems... off."

    scene backgroundhall1

    "Each classroom has a transparent door with an electronic display built-in."
    "It feels more like an observation tank than a classroom."

    show MMBase

    mm "The building had been a library since the 1600's."
    mm "I never got to see the inside, because the previous owner was such a nut job."

    n "Why should I care?"

    mm "No, but do you think these bowties proofread every book in the building before bringing you in here?"
    mm "Who knows what you could find!"

    "I appreciate she’s trying to make this sound like an adventure, but it doesn’t change how... empty the school feels."
    "The second floor is for more specialized classes."
    "Along the west corridor are rooms for the fine arts and along the east is a giant computer lab."
    "Large bay windows look out to the central courtyard."
    "We finally arrive at a large mahogany office door."

    mm "This is it."
    mm "Promise you’ll be on your best behavior?"

    n "...Why are you asking me that now?"

    "She searches for the right words to say."

    mm "I didn’t want you to spend your time at the mansion worrying about school."
    mm "This is the safest place for you to be right now, even if it’s upsetting at times."
    mm "Until they grant me full guardianship, my hands are tied."

    n "...I promise I’ll try."

    "Maimai escorts me into the office."

    hide MMBase
    play music "music/Still.mp3"

    scene backgroundprincipal

    # Principal office
    "A woman gestures for us to sit down. She takes her place behind a massive desk with a stack of forms for us to review."
    "The nameplate in front of her reads in gold letters 'Principal Vivaldi Thani'."

    n "....."

    "Vivaldi Thani, the chief officer sent to hunt down Lethe and her conspirators."
    "She was at the scene when Lethe... when she died."
    "I wouldn't have come if I knew she'd be here."
    "She's the last person I want to talk to."

    show VBase

    v "Is something wrong?"

    "It's like she doesn't even care."

    hide VBase
    show MMBase

    mm "He’s just nervous because it’s a new school."
    mm "You know teenagers, all salty about change and stuff."

    "The principal is cold and composed, much like a statue."
    "I can’t help glaring at her. The DVP had handed me over to the woman who set up Lethe and sabotaged our siege of Guwon."
    "How could she be so indifferent? Doesn’t she recognize me at all?!"

    mm "So you’re the principal?"
    mm "That’s uh, quite a shift from being a police officer."

    hide MMBase

    "I've never seen Maimai so nervous before."
    "Is she scared of this woman? Or just psychics in general?"
    "She hands us papers to sign, with Maimai trying to stay as far away from the woman's hands as possible."
    "My phone is confiscated and replaced with a cheap knock-off to use while on campus."

    show VBase

    v "Detective. I grew tired of locating criminals after they committed crimes."

    hide VBase

    "Locating? Is that what she calls what she did? Locating criminals?"
    "Lethe was- She watched them kill her with that indifferent stare on live television."
    "We get up to leave. I can’t hold my tongue any longer."

    scene backgroundP3 with fade:
        size (1920, 1080) crop (0, 0, 1920, 1080)

    n "You ruined my life."

    mm "Nagen, please."

    scene backgroundP3:
        size (1920, 1080) crop (0, 0, 1920, 1080)
        linear 1.5 size (1920, 1080) crop (0, 0, 2400, 1525)


    n "No, because of her stupid feud, I lost both my mentor and my best friend in one night."
    n "Just because I have to be here doesn’t mean I have to play along with her revenge fantasy."

    v "This isn’t supposed to be a punishment, Mr. Tesuta. Your school life will be what you make of it."
    v "I trust you will do everything in your power to avoid ending up in my office again. Good day to you both."

    scene backgroundhall2

    "I practically get pushed out of the room by Maimai."
    "The wooden doors slam shut, but her hands never leave my shoulders."

    show MMBase

    mm "I know you’re a smart kid, so please... please don’t go starting fights you can’t finish."

    n "You can’t leave me here with her- You knew she’d be here!"

    mm "It's part of your plea bargain, I can't pull you out even if I wanted to."
    mm "I'm not your legal guardian yet."

    n "She’s going to set me up to fail."
    n "You can’t expect me to believe she’s okay with helping someone who trashed their hometown."

    mm "I don’t. That’s why you need to be careful."
    mm "These people stand more to gain from your success than your failure, but I can’t guarantee their motives are good-intentioned."
    mm "We have to meet them halfway."

    n "You know I don’t like being alone."

    mm "I’m sorry."
    mm "I’m sure there are a lot of troubled kids who could benefit from a school like this."

    "Each word is slow and deliberate."

    mm "I’m sure you’ll find some good friends here."

    "She finishes with a wink and finally I understand."
    "My old teammates could be here too."

    n "Are they really-"

    "Still, to cut me off like that, it must mean I was right."
    "They’re here. Somewhere in this god-forsaken reform school, I’ll find my friends."

    mm "You got this."

    # New Background showing around the outside here
    scene backgrounddorm

    "We go back to the car to get the last of my things."
    "She wraps me in a huge hug and I become very aware of the car coming up to the roundabout."

    n "Maimai, please-"

    mm "Be safe. Call me if anything happens."
    mm "I want to hear from you at least once a week, mister."
    mm "I mean it. Don’t go forgetting about me, okay?"

    n "Okay, okay, people are staring."

    "I brush her off and collect my bags."

    n "I’ll miss you too."

    hide MMBase

    "I really don’t want to go, but I can’t keep putting it off."
    "We say our final goodbyes and I watch as the car drives off. Tomorrow will be my first day of school."
    "I can see other kids unloading their luggage and milling about the grounds. Now would be a good chance to find my friends."

    #insert nanase intro here
    scene backgroundschool

    play music "music/CryingOverYou.mp3"

    show NBase

    nk "Good morning!"

    n "AH!"

    nk "I'm sorry, I didn't mean to startle you."
    nk "My name's Nanase Keisan. I'm helping with orientation during move in week."
    nk "Will you be staying on campus this year?"

    n "....."

    "Good god man, have you forgotten how to talk to people like a normal human being?"
    "Don't just stand there, say something!"

    menu:
        "Say something witty":
            $ Charm += 1

            n "Well, all my stuff is here already, so I might as well."

            "I motion to my garishly decorated luggage; my guardians said I needed more than my usual duffle bag of necessities."
            "Pretty sure I have more bags than clothes. They would have been a nice way to carry my rifles... had they let me keep them."

            nk "R-right, of course."

            "She sighs."

            nk "You'll want to head to Classroom E-103."
            nk "Let me know if you need any help."

            n "Thanks, I got it."

            jump nk_intro
        
        "Just answer the question":
            $ Vigor += 1

            n "Yeees..."

            "Did that sound weird? I feel like it sounded super weird."
            "I'm drawing a blank. Why did I only get four hours of sleep last night? This is a nightmare."

            nk "Alright, then head over to Classroom E-103."

            n "She points to a towering building a few yards west."

            "103, that'll probably be on the ground floor. I grab my many bags, fumbling a little."

            nk "Do you need any help?"

            "Have I taken too long? I really can handle it, it'll just be a little awkward balancing five bags."
            "Though now that I think of it, I most certainly don't own enough junk to warrant this much luggage."

            jump nk_intro

        "Introduce yourself":
            $ Intel += 1

            n "My name's Nagen Tesuta. Orientation is in E-103, right?"

            "I memorized today's schedule well in advance."
            "If I get there early, I'll have five hours to try and finish Dracula."

            nk "Yep. Do you need any help?"

            menu:
                "No":
                    n "I'm fine, really. Thanks anyways."

                    nk "O-okay then."

                    "She doesn't seem convinced, but I'm in a bit of a hurry."

                    jump nk_intro

                "Yes":
                    $ nkRep += 1
                    n "Actually, yeah, I could use an extra pair of hands."

                    nk "Great, I'll walk with you! What do you need me to carry?"

                    "She insists on taking three of the five bags, which is more than I actually need."
                    "But she seems happy to have someone to talk to."
                    "I notice other students helping with orientation are in red volunteer shirts, but she doesn't have one."
                    "Is she actually helping with orientation?"

                    n "You seem pretty new here yourself. How'd you get to be a volunteer?"

                    nk "Hunh? Oh, no, I;m not with them."
                    nk "I got here yesterday night, but I figured helping out was better than just standing around waiting for the meeting."
                    nk "Not much to do around here other than unpacking and wandering around the school."

                    n "To each their own, I guess."

                    hide NBase

                    jump nk_intro

label nk_intro:
    
    scene backgroundroom

    "I get to the room and set down my things."
    "I'm not sure what I can expect from this school, but I do know one thing."
    "By the end of the year, the student body will be in the palm of my hand."
    "I mean, why else does someone become student body president, resume material? I think not."
    "I may not be able to clear my name through the DVP, but if I make enough of an impression, they can't just lock me away and pretend nothing happened."
    "After I've gotten settled, I'll take a look around the school."

    g "You will be given the opportunity to explore the school and look for your friends."
    g "This is a good chance to meet your future classmates as well."

    # New Game +

    g "Of course, you can always skip ahead to the next scene."
    g "But this will give you a baseline affinity of 0 with all students."

    # Else

label prologue_meet_students:

    $ config.menu_include_disabled = True

    scene backgroundschool
    play music "music/CosimoFogg.mp3"
    if prologueFriendsFound is 3:
        "Well, I found all my friends, should I go start the meeting?"

        menu:
            extend ""
            "Keep Looking Around" if prologueSearches is not 18:
                pass
            "Start the Meeting":
                $ config.menu_include_disabled = False
                jump Meeting

    if prologueSearches is 0:
        "Okay, where should I start looking?"
    else:
        "Where should I look now?"

    jump prologue_locations_test

    #if prologueLocationsPage is 2:
    #    jump prologue_locations_2
    #elif prologueLocationsPage is 3:
    #    jump prologue_locations_3


label prologue_locations_test:
    $ choice_many_choices = True

    menu:
        extend ""
        "Lecture Hall" if prologueHiroMet is False:
            $ choice_many_choices = False
            jump prologue_lecture_hall
        "Field" if prologueMarikoMet is False:
            $ choice_many_choices = False
            jump prologue_field
        "Hallway" if prologueYokuMet is False:
            $ choice_many_choices = False
            jump prologue_hallway
        "Courtyard" if prologueUittoMet is False:
            $ choice_many_choices = False
            jump prologue_courtyard
        "Stage" if prologueKitsuneMet is False:
            $ choice_many_choices = False
            jump prologue_stage
        "Audio Visual Room" if prologueKazzMet is False:
            $ choice_many_choices = False
            jump prologue_av
        "Nurse's Office" if prologueOshinMet is False:
            $ choice_many_choices = False
            jump prologue_nurse_office
        "Pond" if prologueIchitaMet is False:
            $ choice_many_choices = False
            jump prologue_pond
        "Roof" if prologueTaigaMet is False:
            $ choice_many_choices = False
            jump prologue_roof
        "Library" if prologueChiseiMet is False:
            $ choice_many_choices = False
            jump prologue_library
        "Sewing Room" if prologueShomaMet is False:
            $ choice_many_choices = False
            jump prologue_sewing_room
        "Gymnasium" if prologueSetsunaMet is False:
            $ choice_many_choices = False
            jump prologue_gym
        "Cafe" if prologueKietsuMet is False:
            $ choice_many_choices = False
            jump prologue_cafe
        "Lab" if prologueMomokoMet is False:
            $ choice_many_choices = False
            jump prologue_lab
        "Classroom" if prologueReiMet is False:
            $ choice_many_choices = False
            jump prologue_classroom
        "Student Council Room" if prologueRiseMet is False:
            $ choice_many_choices = False
            jump prologue_student_council_room
        "Forbidden Door" if prologueDyreMet is False:
            $ choice_many_choices = False
            jump prologue_forbidden_door
        "Ampitheater" if prologueJonaMet is False:
            $ choice_many_choices = False
            jump prologue_ampitheater

label prologue_locations_1:

    $ prologueLocationsPage = 1

    menu:
        extend ""
        "Lecture Hall" if prologueHiroMet is False:
            jump prologue_lecture_hall
        "Field" if prologueMarikoMet is False:
            jump prologue_field
        "Hallway" if prologueYokuMet is False:
            jump prologue_hallway
        "Courtyard" if prologueUittoMet is False:
            jump prologue_courtyard
        "Stage" if prologueKitsuneMet is False:
            jump prologue_stage
        "Audio Visual Room" if prologueKazzMet is False:
            jump prologue_av
        "Other Locations":
            jump prologue_locations_2

label prologue_locations_2:

    $ prologueLocationsPage = 2

    menu:
        extend ""
        "Nurse's Office" if prologueOshinMet is False:
            jump prologue_nurse_office
        "Pond" if prologueIchitaMet is False:
            jump prologue_pond
        "Roof" if prologueTaigaMet is False:
            jump prologue_roof
        "Library" if prologueChiseiMet is False:
            jump prologue_library
        "Sewing Room" if prologueShomaMet is False:
            jump prologue_sewing_room
        "Gymnasium" if prologueSetsunaMet is False:
            jump prologue_gym
        "Other Locations":
            jump prologue_locations_3


label prologue_locations_3:

    $ prologueLocationsPage = 3

    menu:
        extend ""
        "Cafe" if prologueKietsuMet is False:
            jump prologue_cafe
        "Lab" if prologueMomokoMet is False:
            jump prologue_lab
        "Classroom" if prologueReiMet is False:
            jump prologue_classroom
        "Student Council Room" if prologueRiseMet is False:
            jump prologue_student_council_room
        "Forbidden Door" if prologueDyreMet is False:
            jump prologue_forbidden_door
        "Ampitheater" if prologueJonaMet is False:
            jump prologue_ampitheater
        "Other Locations":
            jump prologue_locations_1

label prologue_lecture_hall:
    
    $ prologueSearches += 1
    
    scene backgroundcharm

    if prologueHiroMet is False:
        
        $ prologueFriendsFound += 1
        $ prologueHiroMet = True
        
        call prologue_hiro

    else:
        "Hiro isn't here anymore."

    jump prologue_meet_students

label prologue_field:

    $ prologueSearches += 1

    scene backgroundfield

    if prologueMarikoMet is False:
        
        $ prologueMarikoMet = True

        call prologue_mariko
    else:
        "There seems to be nobody here anymore."
    
    jump prologue_meet_students

label prologue_hallway:

    $ prologueSearches += 1

    scene backgroundhall1

    if prologueYokuMet is False:

        $ prologueYokuMet = True

        call prologue_yoku
    else:
        "There seems to be nobody here anymore."
    
    jump prologue_meet_students

label prologue_courtyard:

    $ prologueSearches += 1

    scene backgroundcourtyard

    if prologueUittoMet is False:

        $ prologueFriendsFound += 1
        $ prologueUittoMet = True

        call prologue_uitto
    else:
        "Uitto isn't here anymore."
    
    jump prologue_meet_students

label prologue_stage:

    $ prologueSearches += 1

    scene backgroundstage

    if prologueKitsuneMet is False:

        $ prologueKitsuneMet = True

        call prologue_kitsune
    else:
        "There seems to be nobody here anymore."
    
    jump prologue_meet_students

label prologue_av:

    $ prologueSearches += 1

    scene backgroundavroom

    if prologueKazzMet is False:

        $ prologueKazzMet = True

        call prologue_kazz
    else:
        "There seems to be nobody here anymore."
    
    jump prologue_meet_students

label prologue_nurse_office:

    $ prologueSearches += 1

    scene backgroundnurse

    if prologueOshinMet is False:
        
        $ prologueOshinMet = True

        call prologue_oshin
    else:
        "There seems to be nobody here anymore."
    
    jump prologue_meet_students

label prologue_pond:
    
    $ prologueSearches += 1

    scene backgroundpond

    if prologueIchitaMet is False:
        
        $ prologueIchitaMet = True

        call prologue_ichita
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_roof:
    
    $ prologueSearches += 1

    scene backgroundroof

    if prologueTaigaMet is False:
        
        $ prologueTaigaMet = True

        call prologue_taiga
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_library:
    
    $ prologueSearches += 1

    scene backgroundlibrary

    if prologueChiseiMet is False:
        
        $ prologueChiseiMet = True

        call prologue_chisei
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_sewing_room:
    
    $ prologueSearches += 1

    scene backgroundsew

    if prologueShomaMet is False:
        
        $ prologueShomaMet = True

        call prologue_shoma
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_gym:
    
    $ prologueSearches += 1

    # BG:Gym

    if prologueSetsunaMet is False:

        $ prologueSetsunaMet = True

        call prologue_setsuna
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_cafe:
    
    $ prologueSearches += 1

    scene backgroundcafe

    if prologueKietsuMet is False:
        
        $ prologueKietsuMet = True

        call prologue_kietsu
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_lab:
    
    $ prologueSearches += 1

    scene backgroundlab

    if prologueMomokoMet is False:
        
        $ prologueMomokoMet = True

        call prologue_momoko
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_classroom:
    
    $ prologueSearches += 1

    scene backgroundclass

    if prologueReiMet is False:
        
        $ prologueReiMet = True

        call prologue_rei
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_student_council_room:
    
    $ prologueSearches += 1

    scene backgroundstuco

    if prologueRiseMet is False:
        
        $ prologueRiseMet = True
        
        call prologue_rise
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_forbidden_door:
    
    $ prologueSearches += 1

    scene backgrounddoor

    if prologueDyreMet is False:
        
        $ prologueDyreMet = True

        call prologue_dyre
    else:
        "There seems to be nobody here anymore."

    jump prologue_meet_students

label prologue_ampitheater:
    
    $ prologueSearches += 1

    scene backgroundamp

    if prologueJonaMet is False:
        
        $ prologueFriendsFound += 1
        $ prologueJonaMet = True
        
        call prologue_jona
    else:
        "Jona isn't here anymore."

    jump prologue_meet_students

label prologue_hiro:

    play music "music/WeAre.mp3"
        
    "I arrive at the room where the student council meets."
    "Everything looks too new, too clean, like no one has set foot in here since the school opened."
    "I stand for a while, admiring the leather office chair at the end of the table possibly meant for the student council president."
    "I would give anything to be in charge and shape the future of this school."
    "It may take a while, but I'm sure I can get there."

    show HBase

    h "Nagen? Nagen, is that you?"

    "I turn and see one of the last people I expected to see. My former teammate and rival, Hiro Morine."
    "I mean, I say rival, but it was purely for Odori's attention."
    "He cheated off all my tests while leaving me in the dust when it came to sports or fighting."
    "Any way you slice it, it was never a fair competition. One of us would always have an advantage over the other."
    "But I'd be lying if I said I wasn't bitter that everyone liked hanging out with him at recess."
    "I'm getting off track."

    n "It's good to see you, I uh, haven't seen you since before..."

    "I trail off. There's no way of knowing how much he knows about the deal that was cut with the DVP."
    "If I say the wrong thing, I could jeopardize his chance at getting pardoned."

    hide HBase
    show HHappy

    h "Yeah, I'm surprised they're letting us go to school together."
    h "My lawyer said they were going to separate us and we weren't allowed to see each other again. I wonder what changed?"

    hide HHappy
    menu:

        "Pretend to speculate":

            $ Intel += 1

            show HHappy

            n "I don't know, maybe Uitto worked her magic and cried us into a lighter sentence."

            show HTALK2

            h "We could do that? Shoot, if I'da known that, I woulda taken a lemon into the courtroom or something."

            hide HTALK2
            show HSmug
            h "I mean, yeah I was kinda scared, but I totally coulda cried my way to freedom."

            "He's as determined as ever."

            n "I was thinking more along the lines of using her Proficiency. It was Diplomacy, remember?"

            hide HSmug
            show HHeadempty

            "He stares at me blankly."

            n "She could talk people into doing things for her."

            hide HHeadempty
            show HSass

            h "Right, she was a Charisma major at the time."

            hide HSass
            show HBase
            h "Oh! That reminds me."
            hide HBase
            show HTALK1
            h "There's been a rumor going around that you can change your major, have you heard anything about that?"

            n "No, I haven't."

            hide HTALK1
            show HTalk

            h "Oh, that sucks. I was hoping you could explain it to me."
            h "Something to do with how Proficiencies can apply to different majors depending on how they're used."

            hide HTalk
            show HSuppress
            h "But I just don't get injured easily. I don't see how that would make me smarter or more likable."

            "That is odd, I'll have to look into that."
            
            hide HSuppress

        "Ask how he's doing":

            $ Charm += 1
            $ hRep += 1

            show HHappy

            n "Crazy, right? But it's good to see you. How have you been?"

            hide HHappy
            show HSadtalk

            h "I'm living in a group home right now. It's not too bad, a little cramped, but they were willing to take me."

            n "That's kinda surprising."

            show HSadSmile

            h "Well, I mean, it's like a rehab center for troubled kids."
            h "We have to go to classes, and therapy sessions, and they;ve got this little reward system and junk."

            hide HSadSmile
            show HSadtalk
            h "I had to work really hard just to be able to leave the building on my own."

            n "Oh, well, I mean that's good to hear. Is it nice?"

            hide HSadSmile
            show HSass
            h "I only have the bottom half of a bedroom door, and one of the other kids punched a hole in the wall last week."

            hide HSass
            show HSadSmile
            h "But the grown-ups are nice, they give me plenty of space... But it's like a respect thing, not 'cause they're scared."

            "Well that's good. He has a bad habit of lashing out if people get too close too suddenly."
            "That thing about the kid punching the wall kinda concerns me though."

            n "I'm glad that's working out for you."
            n "My foster family's a little... strange. They live in this huge house, but they don't really take care of it."
            n "It's like living in a museum. Lots of dusty old expensive things I'm not allowed to touch."

            hide HSadSmile

        "Lawyers are dumb":

            show HHappy

            n "Why would they tell you that?"
            n "It wasn't a standard case, it's not like he could flip through a handbook and find the standard punishment on taking over a city."
            
            hide HHappy
            show HSuppress

            h "Well, no, I guess not."

            n "He was probably trying to scare you or something. That's so unethical..."
            n "I think."
            n "I'm not sure to be honest. See, this is why I chose to represent myself."

            hide HSuppress
            show HTALK2

            h "You shoulda been my lawyer instead, I'm sure you were awesome."

            n "I hope so."
            h "What do you mean? You're here, aren't you? That means you won, right?"
            n "Something like that; I'm on probation. Do you think the others are here?"
            h "I mean, it's possible. They had Proficiencies too... Maybe we could start our club back up!?"

            hide HTALK2
            menu:
                "Yes":

                    $ Villain += 1

                    show HSmirk

                    n "Shh, keep your voice down. We can't have the DVP finding out about this."

                    h "I gotcha. Well, let me know if anything changes. I got your back, man."
                    
                    n "Oh, and Hiro?"

                    h "Hmm?"

                    n "This time we're doing things my way."

                    hide HSmirk

                "Maybe":

                    $ Hero += 1

                    n "As tempting as that sounds, it'd be best if we lay low for a while. At least wait and see how things pan out for us here."

                    show HHeadempty

                    h "What's bread got to do with this?"

                    hide HHeadempty
                    show HSmirk

                    "I must look like I'm about to clock him or something because he starts laughing like a mad man."

                    hide HSmirk
                    show HSmug

                    h "Dude, I;m just kidding, cool your jets."

                    n "You know how I feel about puns."

                    h "Yeah, yeah; look I can't make any promises, but I'll try."

                    n "To knock it off with the puns, or to keep out of trouble?"

                    h "Both."
                    
                    hide HSmug

                "No":

                    show HThisisfine

                    n "I don't know. I mean, we can't use the same group name, and it wouldn't feel right without Odori anyway."

                    h "Yeah, that's true."

                    "Odori was the one who brought us all together in the first place."
                    "The Liberation Front was her dream, and a part of it died with her."

                    hide HThisisfine
                    show HTalk

                    h "Hey man, are you okay?"

                    hide HTalk

    show HThisisfine

    n "We’ll be meeting later."

    hide HThisisfine
    show HTALK2

    h "We?"

    hide HTALK2
    show HHappy

    h "Wait, no way, are the other’s here too?"

    # Has Nagen found someone?
    if prologueFriendsFound is 2:
        n "I don’t know for sure, but I’m looking for them. Until then, play it cool."
    else:

        # Change this thanks

        n "Yup."

    hide HHappy
    
    "I've spent way too long listening to what other people tell me to do."
    "Once I've finished scoping out the school, I'm breaking out the strategy board."
    "I should get going. There's still more of the school to see."

    return

label prologue_mariko:
            
    "A few years ago, I probably wouldn't be anywhere near here. Maybe this year will be different."
    "In the corner of my eye, I see a girl in black spandex bound over, a pile of papers in her hands."

    show MBase

    m "Hold on a second!"
    m "Hey, the name's Mariko Genki, I'm gathering signatures to start up a Cheer Squad!"
    m "Some may say it's a little early, but it's never too early to start practic-"

    "Her chipper demeanor falters once she looks up. It's as if the life has been sucked right out of her."
    "She shifts, using her papers as a physical barrier between us."
    "Floundering for a proper social response, she goes with the first thing I imagine comes to mind."
    
    m "You wouldn't happen to be interested in being a cheerleader, would you?"

    "Her tone is tight, her smile forced. I'd judge, but I have always been awkward around people myself."
    "Being an ex-villain just makes things that more difficult, I guess."

    menu:

        "Try to calm her down":
            
            $ mRep += 1

            n "I'm not against the idea, but do you actually want me on your team?"

            "Her defensiveness eases, but it's clear she's still wary."
            "Not that I blame her, she was once a member of my army. One of the more resistant."
            "I don't know if it was her Proficiency or pure determination, but she had fought the brainwashing harder than anyone else."
            "With an ability like being unable to feel pain, it can be tricky figuring out if she should be a Vigor or Intelligence major."
            "Well I say my army, but Hiro was the one that gathered and directed everyone."
            "I kinda just watched from rooftops and corrected his orders through radio and the like."
            "If it had actually been my army, things might have gone smoother."

            m "I mean, anyone's allowed to join. I just never took you for the 'cheery' type. You've always been so..."

            menu:

                "Dreary":

                    $ Charm += 1
                    
                    "She smiles that polite, forced smile one receives out of pity."
                    "To be fair, I wasn't exactly the most outgoing kid in the world and I didn't have the best lasting impression on her."

                    m "Hey, uh, rhyming is a key ingredient to cheer."

                    "That was the roughest shift in a conversation I've heard since my dad."
                    "A lot of examples come to mind, but I have to focus on the task at hand."

                    n "Good luck with the cheer thing. I'm... really sorry about what happened."

                    "Her face hardens."

                    m "Sorry isn't going to fix anything."

                    "She takes a deep breath."

                    m "But it helps... I just- I'm not going to let my girls down this time. And guys. Really, uh, really should recruit more-"

                    "Her eyes drift to me, then shaking her head."

                    m "I've got to go."

                    "She hurries off. Not that I blame her."

                "Hostile":

                    $ Vigor += 1

                    m "I should have seen it coming."

                    "She shakes her head, regret evident on her face."
                    "When Hiro had gone around recruiting our first members, Mariko declined."
                    "She was the only cheerleader who declined, and her position as the captain didn't matter to anyone when Guwon was already in chaos."

                    n "I was just trying to protect everyone."

                    m "No, I was trying to protect everyone; you wanted to fight back!"

                    n "Fighting is what kept us alive. It's what kept you alive."
                    n "You fought longer and harder than any of us, it was quite impressive."
                    n "You'd have made an excellent general."

                    m "A general hunh?"

                    "She laughs bitterly."

                    m "They don't give medals of honor to villains, Tesuta."

                    n "You're only the villain once you lose."

                    "She may be done fighting, but I'm not. I'll keep pushing forward until there's nothing of me left."

                    n "It was good to see you again. You know, to know that you're okay."
                    
                    "Though I'm surprised she's here considering what I was sent here to do. I'm sure she had hoped to never see me again."
                    "Does that mean there are other kids from the Liberation Front at this school?"
                    
                "Uninterested":

                    $ Intel += 1

                    n "I never really had a lot of free time back then."

                    "Between Odori's hero club and my dad's endless examinations, I didn't have a lot of time for anything."
                    "I was constantly underslept to the point that anything involving standing seemed taxing."

                    m "Right, I don't suppose your mind has changed all of a sudden either?"

                    n "Not especially, no."

                    "She breathes a huge sigh of relief. Still a little anxious, but no longer petrified."

                    m "Then I'll be on my way. Byeee!"

                    "She immediately turns around and leaves. I doubt she'll be coming my way anytime soon."

        "Say anything to make her go away":

            n "Not interested."

            "She clearly recognizes me from the Guwon Riots."
            "Mariko had been a member of my army, and not of her own volition. She was one of the last who fell under our control."
            "I doubt she'd want anything to do with me, and I'm not going to pretend I like the idea of seeing her anyway."
            "What were they thinking, sending both of us to the same school?" 
            "The whole point of witness protection is to maintain a normal life, and she is an obvious threat."

            m "Good, then you'll have no business being around my girls."

            n "Excuse me? I was minding my own business, you were the one who came running up to me."
            n "I'm not out here to get anyone, I'm trying to live a normal school life."

            "She sputters in outrage. There are a million things I'm sure she wants to say to me, but it wouldn't change anything."
            "I don't have time for her to collect her thoughts."
            "As I begin to walk away, she shouts after me."

            m "I don't want any trouble from you, Tesuta."
            m "Anyone wearing this emblem is under my protection, you understand?"

            "She gestures to her earrings like I'm going to look at every girls' ears before talking to them."
            
            m "If you try anything-"

            n "The only thing I'm trying to do is start over."
            n "I don't have the time nor desire to mess around with a handful of powder puffs." 
            n "I've got my own problems to deal with."

            m "Just don't drag my squad into it."

            "It's almost admirable how fervently she defends this so-called 'squad' when she hasn't even gotten permission to lead one in the first place."
            "Old habits die hard, I suppose."
            "Though she wasn't a terribly good leader. All bark and no bite."

    hide MBase

    "I should look around some more."

    return

label prologue_yoku:

    "The grounds of this school are a lot larger than I anticipated."
    "I'll need at least an hour before classes start in order to figure out where I'm going."
    "I wander into a back hallway on the second floor."
    "I assume all of the art classes will be taking place here based on the glass display cases."
    "With all the classrooms locked, there isn't much to see right now."
    "Though I don't seem to be the only person wandering around campus right now."
    "He has a beaten-up piece of paper in his hand and seems lost."
    "When he looks up at me, I feel a chill run down my spine."

    show YBase

    y "Oh, it's you..."

    n "What's that supposed to mean?"

    "A few things come to mind, most tracing back to the last two years."
    "In the course of a year, Odori and I had raised an army of three hundred with the education collars."
    "They essentially hijacked a person's body through their central nervous system."
    "With it, we could train our troops in a matter of hours."
    "However, not everyone was as keen on this idea. Most of the soldiers had been students at our school."
    "Granted, I never came in contact with a lot of recruits, so the question is, how does this kid know me?"
    "I recognize him from the posters at Estella back when we were kids, a real wiz-kid with a piano."
    "We never crossed paths since I spent most of my time studying in my room."
    "My room, of course, being an anti-social hotspot."

    y "What are you doing here?"

    menu:

        "None of your business":

            $ yRep += 1

            n "Just looking for where my new classes are going to be. And talking to you, I guess."

            y "...You can't be serious."

            n "What?"

            y "I thought this was supposed to be a school for the e-e-elite, not a co-common murderer."

            n "First of all; common!? I know having a good memory isn't the most exciting Proficiency, but it's better than you Mr. Music Man."

            n "Secondly, being involved in the Guwon Riots has nothing to do with how capable I am as a student."
            n "The definition of 'elite' here is slightly above average, don't delude yourself."

            y "So defensive over your Pr-proficiency, yet you're going to g-gloss over the murderer comment?"

            n "....."

            "Okay, so I'm a little self-conscious about my so-called 'powers'."
            "But it isn't like I think being able to remember everything is pointless or lame, it's served me fairly well."
            "The thing is, my Proficiency is artificial."
            "Unlike child prodigies like Yoku, my father had to spend every waking moment forcing my brain to process memories the way it does."

            y "Hh-ow long are you going to keep staring into space?"

            n "Sorry, that happens sometimes."

            y "As much as I'd like to continue this ffffascinating discussion, I have business eh-elsewhere."
            y "Until next time."

        "I'm lost":

            $ yRep += 1

            y "...Obviously."

            n "Hey! You're wandering around here too! You're probably more lost than I am."

            "He freezes."

            y "You... you don't know that."

            n "Really, then where are we?"

            "His face pinches up, as if his lower lip is trying to retreat up his nose."

            y "First-"

            "I shake my head as he speaks."

            y "Lower-"

            n "Getting colder. We're on the second floor."

            y "If you kn-know that, how a-re you lost?"

            n "I'm trying to find the dorms. These are not dorms."

            "I'll be fine once I map out the entire school, but my cheapo emergency phone is almost dead and Maimai will flip if she calls and I don't answer."

            n "Also I have to ask..."

            menu:
                "How do you know me?":

                    $ Charisma += 1

                    y "You really don't know?"
                    y "W-well, whe-ere do I start..."

                    "That's never a good phrase to hear."

                    y "Professor Tesuta co-constantly talked about you at galla sssocials, and everyone was dying to kn-know what you'd been up to desp..des..de-"

                    "He sighs."

                    y "Despite never being invited."
                    y "You got in detention mu-m-multiple times for fighting, and you t-took o-over the city."

                    n "Well, yeah, but... how did you know that was me?"

                    y "You didn't even do something as simple as wear a mask. What p-possibly made you think no one would recognize you?"

                    n "I was really good at hiding."

                    y "Y-you were good at camping, that isn't the same thing."
                    y "Honestly, I can't believe you were capable of a-anything on that large a scale."
                    y "I assume you had additional help."

                    n "HEY!"

                    "Granted, I shouldn't be proud of the things I did, but it's okay to feel a little insulted by this, right?"
                    "I'm just mad he's calling me stupid."

                "What are you doing here?":

                    $ Intel += 1

                    y "I was looking for the auditorium, I he-heard that this school was going to provide a Wurlitzer."
                    y "As the future's leading co-com-composer, I'd like to find it."

                    n "A Wurlitzer?"

                    y "Like a giant music box, an orchestra without... people."

                    "I've never seen someone so disgusted at the mention of other human beings. And I thought I was antisocial, dang."

                    n "What do you need a Wurlitzer for?"
                    
                    y "I've composed for a number of high scale events, but it's been a while since I've had a steady stream of clientele."
                    y "Making everything on my own will expedite the progress."

                "Is your hair naturally green?":

                    $ Vision += 1

                    y "....."

                    n "I've seen a couple of people at this school with crazy hair colors. I just had to ask."
                    n "Mine isn't. In case you were curious."

                    y "....."

                    n "So is it? I feel like it'd be a pain to dye it and do the little buzz thing."
                    n "Not that it looks bad, it just sends a certain message y'know."

                    y "I'm going."

                    n "Was it something I said?"

                    "He just walks off, shaking his head."
                    "I don't think I said anything that weird. People ask me about my hair all the time... I think."
                    "It's been a while since I've talked to people on relatively friendly terms. Maybe crazy is the new normal."
                    "If that's true, my friends might actually have a shot at freedom."

    hide YBase

    "He didn't seem to have that much to say to me. That's fine, I'm not here to make new friends."
    "The sooner I can find a way out of here, the better."

    return

label prologue_uitto:

    play music "music/CoolNights.mp3"

    "I decide to check the back of the school."
    "Sun pours down into the center of the courtyard. It should feel warm and inviting."
    "Devoid of any activity, it's unsettling. I feel like I shouldn't be here."
    "I'm not alone, though. In the corner of my eye, I see a girl with a brilliant stream of scarlet hair."
    "She's looking out towards the sky with a forlorn grimace."

    n "Hey... uh, come here often?"

    show Uittosmile

    u "No way, Nagen!?"

    "Her voice is definitely familiar. She turns on me with a wicked grin."
    
    hide Uittosmile
    show Uittosmirk

    u "Did you seriously just hit on me? Good god, man, keep it together. You've been here, what, one day?"

    "Oh no."

    n "Uitto, I didn't realize it was you!"

    hide Uittosmirk
    show Uittogurl

    u "That's supposed to make me feel better?"

    n "No. I mean kinda. I wasn't even flirting, I just-"

    hide Uittogurl
    show Uittotalk

    u "Stop, stop. You're just digging yourself deeper, short stack."

    n "I'm not that short!"

    hide Uittotalk
    show Uittotongue

    u "Still shorter than me."

    n "You're in heels!"

    u "I'm 5' 7” without them."

    n "....."

    hide Uittotongue
    show Uittosmirk

    u "That's what I thought."

    n "You're evil."

    hide Uittosmirk
    show UBase

    u "Only when I want to be."

    "I'll be honest, out of everyone, I'm not surprised she made it."
    "When we were kids, they used to call her 'The Closer'."
    "She could talk her way into and out of any situation and was a headliner in the pageant circuit."
    "It's not surprising she's taller than me either, just disappointing."
    "I had hoped to be taller than at least one of my friends."

    hide UBase
    show Uittosmirk

    u "Oh quit pouting. Size isn't everything, y'know."

    n "Knock it off, wench."

    u "Oooh, 'wench', going old English on me are we? What's next, 'harlot' or hauling myself to a nunnery?"

    n "Don't tempt me."

    hide Uittosmirk
    show Uittotalk

    u "With a sharp tongue like that, I'm surprised you're here."
    
    n "Really? You were worried about me?"

    hide Uittotalk
    show UBase

    u "I'm serious, between the three of you, you're the last person I expected to see on the outside."
    u "Jona's an idiot and Hiro's basically harmless, but you?"
    u "You're smart and you're really bad about pretending to be nice."

    n "Yeah, well, so are you."

    hide UBase
    show Uittosadtalk

    u "Yes, but I'm a poor defenseless girly that was bossed around by a scary guy with piercings and torn up pants."

    n "You're hideously manipulative. Is that really the story you went with?"

    hide Uittosadtalk
    show UBase
    u "Story? It's the truth."
    u "You're the one that pitched a fit over not being leader, you should be flattered I gave you credit."
    hide UBase
    show Uittoyell
    u "Unless you told them something else..."
    hide Uittoyell

    menu:

        "I missed you":

            $ uRep += 1

            show Uittoembarrassed

            u "Ugh, don't be gross."
            n "I'm serious! I thought I'd never see you again."

            u "Yeah, me too..."

            hide Uittoembarrassed
            show Uittosad

            u "Listen, if anything I said got you in trouble, I'm sorry."
            u "I was just trying to think of what you guys would probably say and stick with the most common stuff."
            hide Uittosad
            show UBase
            u "Well, you and Hiro. I figured you both would probably lie to protect the other."

            n "So you lied to protect us?"

            u "And Jona would just lie to lie. All of us were doomed, it was just a matter of damage control."

            n "Well that's a defeatist attitude."
            hide UBase
            show Uittosad
            u "Yeah, being defeated tends to do that to a person."
            hide Uittosad

        "It doesn't matter":

            $ uRep -= 1

            show UBase

            n "We're all here now, so why does it matter?"

            hide UBase
            show Uittoyell

            u "All of us?"

            n "Yeah; you, me, Hiro, and Jona."

            hide Uittoyell
            show Uittocringe

            u "That's not... How do you know they're here?"

            n "Didn't they tell you?"

            u "They? Please tell me this is one of your paranoid delusions."

            n "No, the DVP's Secretary of BS told me during her dumb monologue."
            
            hide Uittocringe
            show Uittogurl

            u "....."

            n "Didn't she talk to you?"

            u "....."

            hide Uittogurl

        "Of course I did":

            $ Charm += 1

            show UBase

            n "You were not a defenseless girly that was bossed around by a scary dude with awesome piercings."
            n "And these are my favorite jeans!"

            hide UBase
            show Uittotongue

            u "You're right! Who'd believe you?"

            n "Nah, I went with the silent, brooding approach. The less you say, the better."

            hide Uittotongue
            show Uittosmirk

            u "You're joking, right? Brooding definitely, but silent?"

            n "Hey, I'm hella stoic."

            hide Uittosmirk
            show Uittogurl

            u "Nagen, your oversharing's one evil laugh away from a cartoon monologue. I mean, seriously, you need help. No offense."

            n "You wound me. My fragile ego can not handle an ounce of criticism."
            n "End your vicious slander or I shall end you. Muahahaha."

            hide Uittogurl
            show Uittosmile

            u "I wilt not be-est tamed or commanded, foul villain. I wilt doeth what I wanteth."

            hide Uittosmile

    show UBase
    n "We'll be meeting in the office room on the third floor."

    hide UBase
    show Uittocringe

    u "We?"

    n "I'm looking for the others right now. We're going to talk about our next move."

    hide Uittocringe
    show Uittoyell

    u "Nagen, what are you talking about? We shouldn't be doing anything right now."
    u "You know what's on the line."

    n "Uitto, you gotta trust me on this, I know what I'm doing."

    if Vision >= 10:
        n "Well, yeah... Uitto, is something wrong?"

        hide Uittoyell
        show Uittocringe

        u "How did you know where to find me?"

        n "Well, I didn't know you were here. I've just been kinda wandering around." 
        n "We're meeting in 313 by four at the latest. Make sure you're there."
        hide Uittocringe
        show Uittosadtalk
        u "...Yeah... whatever you say."

        hide Uittosadtalk

    hide Uittoyell

    "There are still other places to look at. I should go."

    return

label prologue_kitsune:

    scene backgroundstage

    "I'm honestly surprised they bothered to build this when there was a functional amphitheater on the grounds."
    "There's only enough seating for twenty to thirty people, but the walls are decorated to create the illusion of a vast balcony."
    "At least they didn't fill the fake seats with human silhouettes."
    "The stage itself is polished and well lit. It has more than enough space for rehearsals."

    show KBase

    k "Isn't it beautiful?"
    k "I was so worried when they picked this place that they'd shove us into a dingy room and call it 'rehearsal' space."

    n "It's a little small, don't you think?"

    k "Compared to the pathetic platform most bars offer, this is an opera house."
    k "There's even changing stalls! We'll be able to do great things with it."

    n "We?"

    k "Aren't you a fellow performer? You're all dressed up and studying the stage."
    k "What else am I supposed to think; that you're just some Intelligence major?"

    n "I {i}am{/i} an Intelligence major."

    k "Oh..."

    n "Nagen Tesuta, proficient in memorization, can't get more common than that."

    k "N-nagen!? I- Oh my goodness, I didn't know it was you."
    k "I'm so sorry, you must think I'm a monster."

    "No harm was done, but it would be fun to mess with her a bit."

    n "It's okay. Since we're going with blind assumptions, I'm guessing Charisma major?"

    k "You mean you don't recognize me?"

    n "No, why would I? Have we met or something?"

    "I never forget a face, but she's wearing so much makeup it's hard to tell where her face starts and the contouring ends."

    k "W-well, I'm a rising star, everyone at this school should recognize me."
    k "Like a phoenix from the ashes, I will guide our nation's culture with my brilliant light!"
    k "You are looking at living, breathing art; the face and voice of the future."

    "Good god did I hit the nail on the head with this one."
    "I'd bet money she rehearsed that speech in the mirror while brushing her hair."

    n "Right... and what is it you do exactly?"

    k "I am Kitsune."

    "This girl is full of nothing answers, isn't she?"

    menu:

        "That's not a talent":

            $ kRep -= 1

            k "Excuse me? Do you know how many years it took to perfect this?"
            k "I woke up at 4AM to get ready and your only takeaway is 'she has no talent'!?"

            n "They don't hand out Proficiency scholarships for being yourself." 
            n "Not that you're even doing that."

            k "I have enough class and good taste to pick out shoes brighter than your future."
            k "You keep insulting people like that and someone's going to punch you so hard your piercings will get drilled into your gums."

            "What the ever-loving fuck did I do to her?"

            k "But my dainty hands belong wrapped around a mic, so you're safe. For now."
            k "I dazzle audiences with my angelic voice and you..."
            k "Well, I suppose most people would be impressed by an 'iron clad' memory for a few minutes."
            k "Even without my Proficiency, people would rather be me."

            "She seems to have calmed down now, but what was that? Does she want to fight me or not?"

        "Like the fox spirit?":

            $ kRep += 1

            "I only know Uitto by her stage name; maybe this girl picked out her own?"

            k "Exactly! It embodies everything I am; enchanting, elusive and practically unkillable."

            n "Why not go by Tenko then? Aren't they more powerful or something?"

            k "They're old and wise; neither of which has ever been used to describe me, let alone powerful."

            n "You'll get there eventually... in a thousand years."

            k "Hey! I am a star right now. Just ask anyone who's gone to my show."

            n "I thought you were a fox?"

            k "Not literally! It's a metaphor. You know, to invoke imagery and imagination."

            n "I imagine wise old men when people talk about fox spirits."

            k "Maybe it does suit you. You already have the white hair."
            k "Mom always said my white hair made me look elegant."

            "Shoot, I didn't mean to upset her. Gotta backtrack."

            n "You saying old people aren't elegant? That's ageist."

            k "...Is that your backwards way of complimenting me?"

            n "I can forwards compliment you too if you want. You're just so fun to mess with, it's hard not to."

            k "Fun? After you've seen one of my performances, you may compliment me."
            k "O-otherwise it would just feel like empty pandering."

            "Says the person who was fishing for compliments five minutes ago."

        "And your Proficiency is...":

            $ Vigor += 1

            k "I specialize in vocal manipulation. My range is A0 to C8 in relation to a piano."
            k "No other singer can compare to me without the use of technology."

            n "That doesn't sound like a Charm Proficiency."

            k "Because it's not."
            k "Not every Vigor major you meet is going to be some meathead jock."
            k "Still, I'm trying to see if they'll let me switch courses."
            k "I feel like Ms. Sato would help me become a more successful idol."

            n "I don't think this is that kind of school. You should focus on vocal training."
            
            k "I'm almost too old to start making my debut."
            k "If I want to get anywhere, I have to start building my fan base now."
            k "Vocal training and dance lessons can happen while I'm on tour."

            n "That sounds backwards and exhausting."

            k "It's part and parcel with being in the industry."

            n "But why even bother?"

            k "I like the attention."

            "At least she's honest. Seems like a lot of work for little reward."
            "There's no guarantee she'll ever get any fans."
    
    k "I can tell you still have your doubts, but you'll be pleased to know I've already started working on my first album."
    k "Make good use of this insider info, because people are going to eat it up!"

    n "With what? I thought all file sharing electronics were banned."

    k "With CDs of course!"

    n "I don't own anything that plays CDs."

    k "Y-you don't? The school issued laptops, didn't they?"

    n "Yeah, but they don't have CD drives."

    k "Then how do you listen to music?"

    n "Normally I'd use my phone and listen to stuff for free online."
    n "Now I'm stuck with whatever came on the burner phone."

    k "Free!? Oh no, that's no good."

    n "It's pretty standard nowadays."
    
    k "Well I'll just need to find a way to get music into the school."
    k "Maybe they'll allow older models of MP3 players and I could have the album on that?"

    n "That's not a horrible idea."

    k "Great! I'll put you down for a preorder then."

    n "I didn't mean-"

    k "I'm sending your confirmation number through the school messenger aaaand, you're all set."
    k "The release date will be next spring."

    hide KBase

    "She blows me a kiss and runs off before I can finish objecting."

    return

label prologue_kazz:

    "I stumble across a dingy room tucked in the back of the second floor."
    "The furniture here is considerably older than the classrooms and in worse condition."
    "If it wasn't for a small, glass-paneled recording booth, I would have assumed this room was for storage."
    "Through the windows, I can see purple egg crate walls lined with foam."
    "A mic dangles from the booth's ceiling, hooked up to three different computers."
    "I try to go inside, but the door is locked."

    show KkBase

    kk "What are you doing here? No one's supposed to be here, bromigo."

    n "You're here, aren't you?"

    kk "I asked if I could check out the recording booth before I finished setting up in my room."
    kk "I guess there are rules against soundproofing the dorms."
    kk "I'll be so bummed if the quality of my content worsens 'cause of cheap equipment."

    n "What does that have to do with me being here?"

    kk "If something breaks or goes missing, I'll be the first person they blame."
    kk "I didn't mean to offend you, but my faith in humanity took a bummer turn by at least 46%% this year."
    kk "As long as I can record my show and no one leaves a mess for me to clean up, I'll make due."

    n "You plan on making videos?"

    kk "Hell no, editing's boring and I look weird on camera. I'm trying to do an independent radio show."
    kk "It's half audience engagement, half whatever the hell I feel like."
    kk "I only have six listeners right now, but hopefully I'll be able to double that by this fall."
    kk "If you're interested, I could always use another editor."

    n "Radio isn't really my thing, but I'll, uhh, let you know later."

    kk "Right on! The name's Kazz by the way, Kataki, if that matters."

    "It very much does matter if he is who I think he is."
    "Professor Kataki worked as an administrator at Estella alongside my father."
    "His research in neuroscience perpetuated the illusion that Estella Prep was helping people."
    "If this kid's his son, he could be one of the students that made competing for top marks a living hell."
    "Especially since he was proficient in math."

    kk "You look hella familiar."

    n "I used to go to Estella."

    kk "That's right! You're the kid that bailed on the nerd ward to hang out with all the criminals."
    kk "I heard someone threw a desk at you the first day."

    n "...Yeah."

    "I had gotten into a fight with Hiro on my first day and I flipped a desk over in the process."
    "It's a wonder we ever became friends."

    kk "That's so cool! We never had anything interesting happen in our class."
    kk "I kept hoping I'd get to join you guys, but my dad wouldn't let them transfer me."

    menu:

        "What did you do?":

            $ kkRep += 1

            kk "The correct question is, what didn't I do?"

            n "....."

            kk "My homework. I didn't do my homework, any of it."
            kk "They never reported me, so I turned myself in, but they kept trying to sweep the whole thing under the rug."
            
            n "You stopped doing your homework to move to Special Ed?"

            kk "Oh, I never did it to begin with."
            kk "Busy work like that is just fluff that diversifies the grade points so one bad exam doesn't force you to repeat a grade."
            kk "I did fine on exams, the assignments were a waste of everyone's time."
            kk "I gave my homework to a willing volunteer and just copied their work in my handwriting."
            kk "But apparently, that wasn't a 'real' problem."

            n "To be fair, that doesn't seem like a transferable occurrence."
            n "Not everyone in my class cheated on tests or had bad grades."

            kk "I guess that's true, but it seemed logical at the time."
            kk "Dyre was an argumentative shit-head, all the teachers hated him, but they couldn't get rid of him because of his grades."
            kk "Still, I hope this place won't be boring. The least they could do after bussing us here is to make it interesting."
            
        "I didn't bail":

            $ kkRep -= 1

            n "They didn't give me a choice when they moved me. I would have gladly stayed in Regular Ed."

            "Granted, I wasn't terribly close with anyone in my old class."
            "It was more the embarrassment of being removed I hoped to avoid."

            n "Most of the kids were brought in for causing trouble at other schools."
            n "I was friends with the few normal kids in my class, the rest of it was a gigantic headache."
            n "It wasn't 'so cool'."

            kk "Woah there, Edgar Allen Bro, no need to be a downer. That was forever ago."

            n "It's barely been two years."

            kk "Exactly, it's all in the past."
            kk "If talking about this is going to bring up an ocean of salt, then forget I said anything."

            n "My point was just that-"

            kk "No, I get it, middle school sucked donkey nards, sorry."

            "I can't argue with that."

        "Why not?":

            $ Intel += 1

            kk "I'm not sure."
            kk "Even after they knew I was plagiarizing all my work, they still kept giving me full points."
            kk "I turned in a paper that was the same page twelve times and I got an A."

            n "That's some dedicated nepotism right there."

            "Why couldn't I reap the benefits of being a teacher's kid?"

            kk "Anything bad I did ended up making my dad look bad."
            kk "My only guess is that he donated his time to the school in exchange for their silence."
            kk "The more boring answer would be that they didn't care enough to do anything."
            
            n "No, the school cared way too much about their image to let a loose nail go unhammered."

            kk "I don't enjoy getting hammered. If I'm gonna party, I want to remember it."

            n "That's not even remotely related to what we were talking about."

            kk "Yeah, but it was funny."

            n "....."

            kk "You know, like a play on words."

            n "....."

            kk "I'm sure you're a blast at parties."
    
    kk "It's so trippy though, 91%% of the people I've met here used to go to Estella."
    kk "Most high schools pull in students from four to fifteen different primary schools."
    kk "I should have found more people from different places by now."

    "No, no way. There can't be that many people from Estella here."
    "These people didn't just seek us out based on where we came from, did they?"

    n "This is basically like a private school, right? Maybe it just appeals to similar types of families."
    n "I'm sure there are plenty of kids here from other places."
    n "Or maybe it's so remote, the average commuter student can't go. Or... or-"

    "We're being collected here on purpose."
    "Why do they want us all in one place? What are they planning?"
    "There has to be a reason."

    n "I'm fine. I just need some fresh air."

    "I gotta move. I have to breathe."
    "Focus on walking. Kazz looks scared."
    "I need to calm down."
    "Shit!"

    kk "Do you need to go to the nurse?"

    n "NO! I mean, no, I'm fine. I promise."
    n "I won't mess with your shit in the recording booth."
    n "I'm sorry, I'm fine, really."
    
    hide KKBase

    "He still looks worried, but I'm already out the door."

    return

label prologue_oshin:
    
    "The nurse's office is small, to say the least."
    "It can barely fit two pennies in between all the filing cabinets and office supplies."
    "There's no needles out, which is good, sharps freak me out."
    "In fact, even the smell of latex and hand sanitiser can sometimes set me off, but this place reeks of something else."
    "Like bitter, musty salad that rotted in a pool of Ax body spray." 
    "Do people still even use that stuff?"

    mu "For the love of- Where on Earth did that lighter go?"

    "That doesn't sound like a nurse." 
    "I see rustling behind the curtain of the back cot. It couldn't be..."

    n "Are you seriously smoking in here? Who's dumb enough to try and smoke in the nurse's office?"

    "The curtain flies back and I have to say, I am severely disappointed."

    show MuBase

    "If you're going to break the rules, at least look cool doing it."
    "Or shower first."
    "He used to take so much pride in 'knowing' more than me in biology and anatomy; I wonder if he still has that competitive streak."

    mu "Some nurse's office. I can't find a single compression wrap or ice pack, let alone an O2 tank."
    mu "Granted, that means the building isn't at risk for exploding right now, but I feel bad for anyone with asthma."
    mu "They're screwed."

    n "You're going to give someone asthma smelling like that. Besides, we both know that's not why you're here."

    mu "As the nurse's assistant, it's my job to take inventory. So yeah, that's why I'm here."
    mu "What I do on my fifteen-minute break is another matter."

    n "You're the nurse's aid?"

    mu "For part of the day."
    mu "They don't have a sports medicine program, so shadowing the school nurse was the only way I could use my Proficiency in biology here."
    mu "Well, it was that or be a TA for the Intel Professor during science lectures but... blegh, I hate theory."
    mu "I came here to learn, not to grade papers."

    "That's something I can sympathize with as a fellow Intelligence major. When they ran out of things to teach you, they'd give you busy work."
    "So this is the limit to having a Medicine Proficiency."
    "When he'd go off in class about internal organs, I thought he'd grow up to be a serial killer, not a stoner."
    "Still, he isn't the first person I'd choose to patch my wounds."

    n "Let me guess, you get paid in 'experience'."

    mu "And college credit."

    menu:

        "You should have TA'd":

            $ muRep -= 1

            n "Sure you'd have to grade papers and junk, but it's less work for the same grade."
            
            mu "Didn't you hear me? I hate theory, and explaining the theory to the uneducated- Ugh!"
            mu "Every part of the human body is connected, you can't understand one of them without knowing the others."
            mu "Unless someone knows the basics, I can't begin to help them and no one knows the basics."

            n "Your idea of basic is above average. It can't be that bad."

            mu "I was in class with someone who asked if you could get pregnant through your stomach."
            mu "I couldn't help it. I laughed at the poor girl, but she was serious."

            n "...Why'd a girl ask you that?"

            mu "I. Don't. Know."
            mu "People hear my Proficiency and think it's permission to ask and show me all the gross things they're too scared to talk to an actual doctor about."

            n "Oh."

            mu "People will ask me weird stuff no matter what I do."
            mu "At least this way it's less people and I won't have to read essays."

        "Are you going to use it?":

            $ Intel += 1

            mu "Maybe. I mean, I guess it'd cover A and P, but..."
            mu "I don't know if it's worth the money or effort."
            mu "If I'm taking on heaps of debt, I need to be certain it's for something I actually want to do."
            mu "Med school doesn't look kindly on the uncertain."

            n "What else would you do?"

            mu "Homeopathy, pharmacology, farming; whatever's easiest."

            n "Farming?"

            mu "Yeah."

            "He blows out a cloud of smoke."

            mu "Agricultural farming."

            n "Must be nice to have so many options."

            mu "Yeah, if only those options didn't cost the same as a new house."
        
        "Need any help?":

            $ MuRep += 1

            mu "What do you know about medicine?"

            "Ironically, I know quite a bit about medicine."
            "My father was particularly enchanted with using me as a test subject for all his patent drugs."
            "Most of what he made were stimulants or Proficiency enhancers, neither of which would be applicable here."
            "However..."

            n "I meant with finding your lighter."
            n "I didn't hear anything fall, so it's probably on the bed somewhere."

            mu "Oh dang, yeah. It's not mine though. It's the nurse's."

            n "What would they need a lighter for?"

            mu "You really think I'd be smoking in here without permission?"

            n "Well, no, but I assumed you didn't care. I didn't think you'd ask-"

            mu "Of course I'd tell the nurse if I was smoking; she's the one I'd have to go to if I overdo it."
            mu "Found it!"

            "He holds aloft a small lighter with a skeleton on it."

    mu "Why did you come here anyway? Have any allergies or scripts the nurse needs?"

    n "No. Just figuring out where everything is."
    n "If they make us participate in P.E., I'll end up here eventually."
    n "I have a strange knack for getting hit in the face with sports equipment."

    mu "Wait, no way. Were you the kid that got a bloody nose from a sprout ball?"

    n "They're harder than they look."

    mu "They're made of yarn, man, it doesn't get cushier than that."
    mu "I thought Dyre was exaggerating all those times. That's too rich."

    "I don't think he's going to stop laughing any time soon."

    n "Well, now I know where the nurse is supposed to be. I'll be going now."

    mu "Hey, hey; watch out for flying pompoms. Wouldn't want you to have to check in on your first day."

    n "Hilarious."

    "Unfortunately, I've been injured by less threatening objects."
    "What he said in jest could very well happen if I run into the wrong cheerleader."

    hide MuBase

    return

label prologue_ichita:

    "When I think of high school, I imagine a gray cement building with crowded halls and an oppressive air about the place."
    "The kind that's earned from decades of kids grinding gum into the pavement."
    "Maybe it's because this place hasn't been a school for very long, but the entryway doesn't feel haunted."
    "It makes it all the more jarring to see someone declaring how happy he is to be here."

    show IBase

    i "I finally fuckin' made it!!!"

    "Waaay too happy for the first day of school."
    "I'm spotted and held socially hostage before I can escape the predatory grip of an excited, one-legged extrovert."

    i "My. Dude. Do you know where we are?"

    n "...outside?"

    i "Exactly!"
    i "No stupid bleach smell or 'round the clock nannies or time-eating fluorescent lights."
    i "Just actual dirt and the actual G.D. sun!"
    i "I'm sure you could care less about the sun, but I missed it."
    
    "He's almost shaking me as he speaks. Or maybe he's struggling to stand."
    "I'm not entirely sure which, I just wish he'd stop touching me."

    n "Have we met before? You're being really... friendly with someone you just met."

    "Just as I'm contemplating peeling his hands off my jacket, he lets me go and laughs."

    i "I don't think anyone's ever called me that before. Ichita, maybe you've heard of me."

    "I have."
    "A competitive martial artist that chased after championship titles and treated his opponents like rag dolls."
    "Hiro was the only one who could withstand his brutal strength Proficiency in a match."

    n "Yeah, though nothing flattering comes to mind."

    i "That figures; can't say I'm surprised."
    i "Don't listen to anything those sore losers told you. They got left behind for a reason."

    "Wasn't he the one that always came in second place? If anyone was a sore loser, it was him."

    i "No need to look so scared. I don't bite."

    menu:

        "I wasn't scared!":

            $ Vision += 1

            i "You were making a little scared face." 
            i "Your eyes got all wide and you kept looking at my teeth. You're like an open book."

            n "I wasn't making a face. This is how my face always looks."

            i "....."

            n "I'm serious; I don't know what you're talking about."

            i "Oh you poor cinnamon roll, you're going to be eaten alive."

            n "I don't need your pity... and quit laughing."

        "Hiro said you do":

            $ iRep -= 1

            i "Hiro?"

            "His whole demeanor changes. I regret bringing him up."

            i "That shit storm loved to run his mouth in front of a willing audience."
            i "Too bad most people didn't have the sense to ignore him."

            "I know better than anyone that Hiro had a tendency to exaggerate."
            "I still believe this guy was willing to jump him in the parking lot after he lost a match."

            i "So you're that stray's plaything? How funny."

            "Neither of us are laughing."

            n "I think you got the wrong idea. I'm not-"

            i "Relax. I know you have nothing to do with what he says."

            "He seems happy with whatever decision he's made about me, but his smile doesn't put me at ease."

        "Neither do I":

            $ iRep += 1

            i "Hah, look at you."

            "I feel like he's treating me like a little kid."

            n "You don't know my rep sheet. I could be a dangerous drug dealer or something."

            i "I don't buy it. You're giving off more aggressive social outcast vibes."

            "This conceited-"

            i "Maybe with our combined forces, we'll be able to change how people see us."

            "Hunh? Wait, that wasn't even remotely sarcastic."
            "He's looking at me with so much hope..."

            n "Yeah, sure."

            i "I can work with that!"

            "At least his expectations are low."
    
    i "Sorry for coming on super intense. It's been a while since I've talked with another person my own age."
    i "Oh shit, I didn't even ask you what your name is."

    n "It's Nagen. But yeah, I wanted to ask you why you're so jazzed to be here."
    n "You're acting like you just got out of jail instead of walking towards one."

    i "Compared to a hospital, this place is a theme park!"
    i "Okay, maybe closer to a themed restaurant or summer camp, but you get the idea."

    n "How long were you in the hospital?"

    i "Almost a year and a half in and out. I was really sick when they found me."
    i "Who knew a scraped knee could take your whole leg?"
    i "Agh, too dark, sorry. Still working on 'positive thinking' or whatever they call it."

    n "You don't have to force yourself to act happy for my sake."
    n "Half of what I talk about with my friends is stuff that pisses us off."

    i "Thanks, but if I stop now, it won't be pretty."
    i "Besides, I promised I'd try to 'perk up' and- ugh- yeah. It'd suck if I threw in the towel on the first day."

    n "Suit yourself."

    i "I gotta check out what kind of gym they threw together."

    n "That's all you. I'll see you around."

    hide IBase

    "There are still some other places I haven't checked yet. I'll keep looking."

    return

label prologue_taiga:

    "I make my way to the uppermost floor of the main building."
    "The entryway to the stairs is blocked off with piles of wood and neglected supplies strewn about."
    "I wonder if they put a hold on renovations; I don't see any tools laying around."
    "I slip through a gap in the tarp and get blinded by sunlight."
    "Anything that couldn't be salvaged has been left to rot in the elements."
    "However, the palettes and busted shelves are too carefully arranged to say they were abandoned."
    "Looking out over the expansive grounds is a kid in loose-fitting festival robes."
    "He gives me a passing glance and resumes glaring at the horizon."
    "There's an obligatory fence, but nothing to stop students from sitting on the edge."

    show TBase

    t "Looking for a way out too?"
    t "If you were thinking of running off into that there forest, you best forget about it."

    n "Did you read about that in the brochure?"

    "He shudders."

    t "If there was a way to escape this place, I would have found it."
    t "It's not fair!"
    t "I didn't do anything to get stuck in a place full of criminals; nothing criminal about wanting freedom."
    t "So, what'd ya do to end up here?"

    n "What makes you think I did something?"

    t "If your folks could trust you, you'd be getting schooled in some refugee camp, but you're not, you're here."
    t "So either you kept running away from where they put ya or ya did something."

    "His attention is more focused on something in his lap."

    n "It's kind of a long story, I really don't want to get into it."

    t "That's cool."

    "A small furry face pops out from under his sleeve."

    n "What the-"

    t "Shh. You'll spook him."

    "It's a gray lop-eared bunny with a blue-collar."
    "His coat is broken up with a handful of scars, but overall, he seems healthy."
    "I've never seen a rabbit so calm before."

    menu:

        "Can I pet him?":

            $ tRep += 1

            "Perhaps I was too eager with the way I asked."
            "He stares, shell shocked, before nodding."

            t "Just don't move too fast, he's been a little skittish since the move."

            "I sit down next to him and hold out my hand to the rabbit."
            "It cautiously sniffs my hand before sinking its teeth into the leather of my glove."

            n "Hey!"

            "I try to pull back, but the rabbit won't let go, all while his owner laughs."

            t "Okay, okay; I get it. I'll make him take the glove off, but you have to let go first."

            "Freedom!"
            "I make sure there are no holes before looking back at the offended rabbit."

            t "Sorry about that, he just really hates gloved hands. One too many V.E.T. visits."
            t "I promise he won't bite. Isn't that right?"

            "I've never seen an animal look so personally attacked before."
            "He keeps licking his owner's hand as I pocket my glove."

            t "Deep breath, keep a steady hand and go for the cheeks."

            "I follow his instructions and get immediately rewarded. The bunny practically melts in his lap."

        "Pets are forbidden":

            $ tRep -= 1

            t "Houdini isn't a pet."

            n "Oh, don't tell me he's an emotional support animal or something."

            "His cheeks light up bright red and his eyes narrow."

            t "This stupid faculty thought I wouldn't cooperate, so they used my assistants as bait to get me to stay."
            t "The others are still being held hostage somewhere."

            "Does that mean there are more rabbits hiding in the school?"

            n "And what exactly does this little guy do to help you?"

            t "Anything within reason. For example..."
            t "Hou, don't you think it'd be funny to piss on the little rich boy's boots?"

            "Rich is an overstatement, but before I can form a response, there's a rabbit on my foot."

            n "Nonono-"

            t "Good boy, Hou."

            "The little gray monster scampers into his sleeve to hide."

        "Aren't you scared?":

            $ Charm += 1

            t "Scared? Scared of what, the school?"
            t "The teachers are just people diving into a collective midlife crisis. I'm more annoyed than anything."

            n "I meant about having an animal this close to the edge of the roof. He could fall."

            "He stares off into space, retracing the conversation in his mind."

            t "No. I told him to stay away from the edge."

            n "O-okay?"

            "There's nothing keeping that animal in his lap other than sheer willpower."

            t "Just, don't tell the teachers you saw him out here."
            t "He's supposed to be in his stupid cage in my dorm."
            t "But bunnies are social creatures. They aren't supposed to be alone."

            n "If you say so..."

            t "....."

            n "....."

            t "He's not going to jump out of my lap to become an angel. It's okay."

            "I can't help but be concerned when he doesn't even have a hand on him."
    
    t "His full name is Houdini; Angel and Blaine are still somewhere under lock and key."
    t "We're already trapped in the facility, additional cages are just over the top."

    n "I assume Angel and Blaine are also bunnies?"

    t "Yeah."

    n "And your name would be..."

    t "Oh, Taiga."

    "The longer the silence goes on, the more puzzled he looks."

    n "I'm Nagen Tesuta, my Proficiency is Memory."

    t "Oh, well then. I'm Taiga... Sakurai, I guess. My family wasn't big on formalities."
    t "I can talk to animals, but I don't understand what they say back if that makes any sense."

    "Did he make up the last name?"
    "It does sound familiar, but I don't remember anyone with that name going to Estella Academy."

    t "Just Taiga is fine. I hope the teachers remember that."
    t "Having someone call me Mr. Sakurai would be weird."

    n "They'd do that?"

    t "If you get in trouble, probably."

    "I really hope not. It was weird enough getting called that by the principal."
    "Both of my parents were teachers, so any time I hear 'Mr. Tesuta', I think of my dad."

    t "It's going to be a long couple of years."

    hide TBase

    "I couldn't agree more, but this conversation's kind of bumming me out. Not that I blame him, but I should go."

    return

label prologue_chisei:

    "Out of all the rooms in the whole school, this is the only one that hasn't been remodeled."
    "The bookshelves are molded into the walls, floor to ceiling."
    "A walkway splits the shelves in half, allowing access to the topmost shelves."
    "To think that the whole building once looked like this."
    "Hidden amongst the shelves is a girl with dark hair."

    show ChBase

    ch "Am I in your way?"

    "She stands fixed in place in front of one of the shelves, refusing to look at me."

    n "No, you're good, didn't mean to scare you. I'm just surprised someone else wanted to come here."
    n "Y'know, since there are books all over the place."
    n "Having another room dedicated to them when they won't fit is a little odd."

    "At least this part seems organized as opposed to books crammed randomly anywhere they fit."
    "She looks down at the floor."

    ch "I will admit, I was hoping to postpone meeting new peers until the last possible moment."
    ch "I supposed it would be better to introduce myself to one individual at a time then to the whole class..."
    ch "I am going to turn around."

    n "Okay..."

    ch "I just do not mean to startle you. My appearance is substantially damaged."
    ch "It was from an accident. No, it does not still hurt and please do not touch me."

    "I summon all my willpower not to yelp in surprise."
    "Despite my best efforts, I can feel my eyes wander back to her torn-up arm."
    "I'm no expert, but I'm pretty sure she's missing some muscles in her arm and... is that a robot hand?"
    "I've been staring too long, I've got to say something."
    
    ch "....."

    menu:

        "I'm so sorry":

            $ chRep -= 1

            ch "All you have done is stare."
            ch "Unless you have thought something uncouth, there is no need to apologize."

            n "What? No!"

            ch "No laughter. Perhaps my delivery was not whimsical enough?"

            n "O-oh."

            ch "It is human nature to stare. We will both just have to wait until it gets boring for you."

            "She talks with barely any emotion at all."
            "It's hard to tell if she's trying to make another joke or if she's being sincere."

            n "....."

            ch "Another botched attempt."

            "She sighs."

            ch "This is going to be a long year."

        "Sick robot hand":

            $ chRep += 1

            ch "It is not humanoid, but it serves me well. You are the second person to compliment it."

            "She hides her gaping smile behind her other hand."

            ch "I guess you could say, its appeal has had a mass effect on people?"

            "She giggles as I realize with dawning horror she's one of those people who loves puns."

            n "Oh, that one hurt. Why?"

            ch "I have been waiting for someone to set me up for that all day!"

            n "Why'd you have to inflict your bad joke on me?"

            ch "The best person to share a pun with is someone who hates them. That is just common knowledge."

            "I can practically feel her adding me to a list of victims."

        "What's your major?":

            $ Vision += 1

            "It's basic small talk, so why does she look so down?"

            ch "I am a playwright."

            n "I thought you were an Intelligence major?"

            ch "I should be." 
            ch "I should be in classes that help me improve my skills as a writer and collaborate with other creatives."
            ch "But Guwon does not recognize 'dual' proficiencies so it does not matter how good my writing skills are anymore."
            ch "Because something strange sometimes happens to me, I had to change majors."

            n "...You're a Vision major?"

            ch "Not by choice. Until I can gain full control of my other hand, I am stuck there."

            "Having a prosthetic shouldn't affect your major. Maybe she can't write as well with her left hand?"
    
    ch "We likely will not be in any of the same classes this year. I hope to be able to change that soon."
    ch "Until then, if you happen upon any unsettling rumors, please feel free to address them with me directly."

    n "Unsettling how?"

    ch "I have become a channel for the unseen; well, my hand has anyway."
    ch "People could claim any number of things about my writing; about me."
    ch "I figured the best plan is to handle it with complete transparency."

    n "So you're a medium of some kind?"

    ch "No. That is not something I have ever wanted to be."
    ch "However, there is something at this school that is trying to take advantage of my hand's weakness and write messages with it."

    n "Has this 'thing' told you anything about me?"

    #[If Hero > Villian]
    if Hero >= Villain:
        ch "...Yes."
        ch "It does not want me to believe what others may say about you; that you are a good friend and an honest person."
        "Not exactly the creepy mentalist stuff I was expecting."
    else:
    #[If Villian > Hero]
        ch "....."
        ch "Sometimes I think my mind is playing tricks on me." 
        ch "Maybe the teachers will see that and put me back with the normal Intelligence majors."
    #[Return to Main Branch]

    ch "I do not like the idea of invading someone's privacy."

    n "You really believe you're being contacted by some unseen entity?"

    ch "It is hard for me to deny at this point. I just hold onto the prospect that one day I can get it to stop."

    n "Good luck with that."

    ch "Thank you."
    ch "Well then, I must be off. Good day, Nagen. I hope you are able to find what you are looking for."

    "She shuffles away, carrying with her a heavy black book... I never told her my name."

    hide ChBase

    return

label prologue_shoma:

    "As I exit the third floor, I see light trickling through the bottom of an unmarked door."
    "Curiosity gets the better of me and I take a step inside. The air is thick and humid."
    "A small swamp cooler rattles in the back window, struggling to cool the room by a degree."
    "A boy is setting up a retro sewing machine that looks like it's been fetched out of a dump."
    "He looks up with a smirk, eyeing me up and down."

    show ShBase
    
    sh "Ah, I see we've dressed ourselves today."
    
    n "Hey, just because you know how to plug in a sewing machine doesn't mean you can judge me for what I'm wearing."

    sh "Okay, okay; just an observation. I never took you for the punk type."
    sh "Having no uniform restrictions has really opened my eyes to what our classmates are comfortable wearing."

    "Eyes... Oh, this is that kid from the Vigor program that Hiro always told me about."
    "All the Vigor majors he'd met before gravitated towards sports, but not him."
    "The guy's got eyes able zoom in and out like a camera."
    "He used to sit in the back of the class, a bit of a loner type."

    sh "Shoma Nishimoto, but you probably remember that, hunh?"

    n "Yeah, though this is probably the longest we've ever talked."

    "...Probably shouldn't have led with that."

    n "But it's good to see you. The more kids I find from our old homeroom, the better I feel."

    sh "Yeah, I know what you mean. I'm kinda glad there's more crossover classes than just homeroom."
    sh "Hopefully, it will help all the majors get along better. It's gotten so competitive lately."

    n "So what are you doing here?"

    sh "Well, the school couldn't supply a proper costume shop of any kind, but they said I could use this room."
    sh "So... I'm trying to make due."

    "This place has multiple theaters but no place to make the costumes? That doesn't make sense."

    menu:

        "What's with the machine?":

            $ shRep += 1

            n "I know they're low on funds, but the least they could do is get you a modern sewing machine." 
            n "That thing looks ancient."

            sh "Well, actually, this is mine from home. I know it's pretty old, but at least it works."
            sh "Besides, this way it doesn't fall under the tech restrictions."

            n "I suppose that's true."

            sh "More modern machines try to take the human element out of fashion."
            sh "A pair of pants is far more impressive if you know a person made it without the aid of factory machines."

            n "Do you make your clothes on this thing?"

            sh "Most of them! I'm not good with knitwear, but other than that, it's all me!"

            n "Honestly, I wouldn't have been able to tell."
            n "I attempted a wallet stitch in grade school and found it wasn't for me."

            sh "That's quite the compliment considering your taste."

        "Your stuff's going to melt":

            $ Vigor += 1

            sh "I'm not sure that's possible."

            n "It is stupidly hot in here considering it's still spring. What are you going to do in the summer?"

            sh "Well, we won't be here during the summer."
            sh "The room may be warm now, but it'll get cooler as the year goes... I hope."

            n "They're not going to fix it?"

            sh "Technically this was a storage closet, so air conditioning is really low on the list of things the school needs."

            n "Then ask for a different room. There has to be someplace more comfortable for you to set up shop."

            sh "Oh no, I could never."
            sh "They've already been generous enough to lend me this space, as long as I don't throw out anything they store here."

            "He doesn't seem the least bit annoyed by that."
            "If that had been me, I would have already marched down the hall demanding a room change."
            "Well, if it really doesn't bother him, there's nothing I can do."

        "This is boring":

            $ shRep -= 1

            sh "Ah, yes. Unpacking generally isn't fun. You could offer to help instead of complaining."

            n "I could. I could also rip on you for wearing fall clothes in an unairconditioned sweatshop."
            n "But I'm not going to do either."

            sh "You're not a very creative person, are you?"

            "I can tell he's not trying to be rude, which makes it worse."

            n "....."

            sh "If you come back after I'm done setting up, I'll try harder to be an entertaining host."

            "So not helping."

    sh "I'm sorry, it seems my mind is all over the place."
    sh "I honestly wasn't expecting to talk to another human being until class started."

    n "Really? Then why did you come onto campus the day before?"

    sh "Well... This place... I need a place to create that isn't where I sleep."
    sh "Then I'd be spending way too much time in my room and I... I'm trying to break myself of that habit."

    n "I see... what exactly do you plan to do here?"

    sh "Mostly alterations, unless I can get my hands on some larger materials."
    sh "I could buy some, but it would mean taking commissions."

    n "What's wrong with that?"

    sh "I'm not really... comfortable with women's wear, and I have a feeling that would be in the highest demand here."
    sh "There are only so many vague gown requests I can handle. I'd much rather do something new."

    n "You might have to adjust those biases if you want any clients."

    sh "I know, I know. I just need to find a way to get motivated to sew a circle skirt."

    "It's as if he's peering into a dark void off into the horizon. I'm not sure what he's seeing."
    "He shudders a bit and then smiles at me."

    sh "But if you or your friends ever need something, I'm always up for a challenge."
    sh "I could make some really cool 'punk' stuff out of some strange materials if you find stuff for me."

    n "Are you sure?"

    "Even though we were in the same homeroom, we weren't friends exactly."
    "He's just someone I kind of grew up with. That's not exactly the relationship that gets you free stuff."

    sh "Of course! Just... I'll need money, or the materials, upfront if I want to make anything new."
    sh "I hope coming here will be worth my time."
    sh "Beats sheltering at my uncle's place and rotting in front of a TV, that's for sure."
    sh "At least here, I can sew without people bugging me."

    n "I'm sure it will be fine. Granted, it'll suck being cut off from... everything."
    n "But there's other things to do too. You just got to get creative is all."

    sh "Y-yeah... thanks, Nagen, but I think I'm going to wrap up here for now."
    sh "Maybe I'll see you around."

    hide ShBase

    "With that, he ushers me out of the room. He wanders off with a heavy step."
    "I should get going too."

    return

label prologue_setsuna:

    "My footsteps squeak as the smell of floor polish and vinyl hits me in the face."
    "It must have been built recently for the place to be so clean."
    "I had heard there was supposed to be a pool here, but this is clearly a basketball court."

    n "Well, this is disappointing."

    show SBase

    s "The gym or being at school?"

    "What the- where did that come from?"

    s "...You weren't talking to me, were you?"

    n "I didn't realize you were here, sorry."

    s "It happens all the time, don't sweat it."

    "She smiles with such ease. I can't help but feel a little jealous."

    s "The name's Setsuna Hori. I won't be offended if you forget it."

    n "That's highly unlikely. I can't forget anything, eidetic memory."

    s "Is that what you go by?"

    n "No, I'm Nagen."

    "She hums, deep in thought as she messes with the face of her watch."

    s "I guess it's only fair to tell you my Proficiency."
    s "I'm told I'm basically invisible; people don't notice me or remember me as much as other people."
    s "I prefer the term Social Chameleon, but the bow-ties in charge of labels don't want to change my status without a retest."

    "A Charisma major that specializes in being unnoticed, how odd."

    s "Having the wrong label has its perks though."
    s "As long as I act like I belong, I can go pretty much anywhere I want."
    s "Which is good, since I never get invited anyway."

    "She laughs at her own joke."

    s "I don't know what you expected to find here that's got you so down. It's just a gym."

    menu:

        "My friends":

            $ sRep += 1

            s "You know other people that go here?"
            s "Lucky you, I feel like a fish out of water. It's like everyone here grew up together or something."

            n "If they're from Estella, they may have."
            n "It depends on what class they were in. Some of the courses were highly insulated."

            s "Shoot, that'll make things extra hard."

            n "Make what extra hard?"

            s "Meeting everyone. Ever try introducing yourself while people are talking to their friends?"
            s "It's like shoving your leg in a closing elevator."
            s "People just stare and you have, like, half a second to make a good impression before they hit close again."
            s "It's going to be a lot of that or go back to my corner being ignored."

            "She shudders."

            n "Well you've already met me, so if you run into someone, you can always open with that."

            s "Thanks. I'll keep that in mind, but I'm really trying to stand on my own."

        "The pool":

            $ Charm += 1

            "She pounds on the gym floor, it sounds... hollow?"

            s "I don't think there'll be any free swim days for a while. Huge bummer, I miss having an indoor pool."

            n "So the pool's under the court?"

            s "There's a concrete bucket below the gym, but I doubt it has any water in it."
            s "This place is trying so hard to look competent, but in the end, it's not much better than outside."

            n "It's better at being impractical."
            
            "That got her to laugh."

            s "I guess that's true, but there's potential at least."
            s "You'd be surprised how many people can't even manage that."

        "Something interesting":

            $ sRep -= 1

            s "Sorry to disappoint you then."

            "I wasn't talking about her, so why's she taking it personally?"
            "There are a million other things I could have said that would be worse."
            "Ugh, but the way she keeps glaring at me..."

            s "By all means, feel free to object at any time."

            n "You're the one that chose to self-deprecate. It's not my job to boost your self-esteem."

            s "I can see why you've been wandering around by yourself all this time."

            n "Hey, I have friends, they're just not here right now."

            s "Hmm..."

            "I can't tell if she doesn't believe me or just doesn't care. Either way, it pisses me off."

    "A high pitched alarm rings from her wristwatch."

    s "Well, that was painful."

    "She immediately turns to leave."

    n "Wait, what's going on?"

    s "I've met my bare minimum for giving a shit and this conversation is clearly going nowhere."
    s "You're not nearly as interesting as I hoped, so I'm leaving."
    s "Honestly, I don't understand why everyone's so worried that you're here."
    s "Outshining you will be a cakewalk."

    "Does this person crave attention so much she sees rumors as competition or... she couldn't be a copycat, could she?"

    n "What do you mean? Who have you been talking to?"

    s "Of course that's what you'd say. It doesn't matter and I didn't sneak in here to walk you through my thoughts."

    n "Wait, are you even supposed to be at this school?"

    s "I meant the gym, moron. It's off-limits to students without a teacher present."

    n "I knew that!"

    s "Sure you did."
    s "Welp, I got more important stuff to do. If you ever decide to do anything entertaining, by all means, find me."

    hide SBase

    "I chase after her, but by the time I get outside, she's nowhere to be found."

    return

label prologue_kietsu:

    "I follow a dirt path that branches off to the right of the school's entrance."
    "It wraps around to a brick storage shed. Inside is a café lined with wall to wall bookshelves."
    "Looks like any furniture that doesn't have a complete set gets stored here."
    "A heavenly aroma of breakfast wafts through the air."
    "At one of the tables, a kid in trashed clothes is sitting with his head in his arms, muttering something to himself."

    show Kisad

    n "...Um... You okay, dude?"

    "I nudge the leg of his chair with my foot and he jumps up with a start."

    hide Kisad
    show Kihunh

    ki "Hunh!? Oh, sorry, didja want to sit here or somethin'?"

    "There's a whole room of empty chairs. Why would I want to take the one he was sitting in?"

    n "I was just making sure you're okay."

    hide Kihunh
    show Kisympathy

    ki "Thanks man. I've been better, but y'know, who hasn't?"

    hide Kisympathy
    show KiBase

    ki "At least this place has cheese curds, y'want a cheese curd?"

    "I can't resist the call of free food. I join him at his table."
    "It seems like the first thing he did when he got here was figure out where to eat."
    "A big plate of fried appetizers is set between us."

    hide KiBase
    show Kidontworry

    ki "You can tell a lot about a place by the food they serve their people." 

    hide Kidontworry
    show Kimildlyupset

    ki "Crap food means you'll get treated like crap."

    n "You've been to a school like this before?"

    hide Kimildlyupset
    show Kidontworry

    ki "Like this? Nah. I've been in n' out of a couple... ah, what do they call 'em?"
    ki "'Guided Learning Programs'. I've been to a bunch of those."

    "Camps designed to stop kids from developing 'unnatural' abilities that could label them as a Vision major."
    "Some of those places could be downright criminal, and none of them worked. I didn't know they were still around."

    n "I can't believe your parents would do that to you."

    hide Kidontworry
    show Kimischeif

    ki "My parents...? Nah, I signed myself up."

    n "You can do that? Why would you do that?"

    hide Kimischeif
    show Kisympathy

    ki "Thought it'd work better than choking on sage and makin' my mom cry. I even tried bootcamp."
    ki "It was actually really cool, but..."

    hide Kisympathy
    show Kicringe

    "He trails off. With his sunglasses, it's hard to tell if he's looking at me or totally zoning out."
    "I check behind me, just to be sure, but we're the only people in the lobby."
    "I wave at him to get his attention."

    hide Kicringe
    show Kihunh

    ki "Sorry, what was I talkin' about?"

    hide Kihunh

    menu:
        "What's wrong with you?":

            $ kiRep -= 1

            show Kihey

            ki "That's a loaded question."

            "He drums on the table with his knuckles."

            hide Kihey
            show Kiveryconcerned

            ki "See, we just met, so I don't know what you think 'right' is."
            ki "Conversations like this are just for you to figure out how similar I am to you when you've already decided we're nothin' alike."

            "He rubs his temples."

            hide Kiveryconcerned
            show Kidude

            ki "Why. Why would you ask that? Did I do something upsettin' if y'think..."
            ki "You a Vision major, or do you hate 'em?"

            n "You just kept trailing off and forgetting what you were saying."

            hide Kidude
            show Kireallyupset

            ki "That's normal."

            n "No dude, it's not."

            hide Kireallyupset
            show Kiunpleasentsurpise

            ki "It's normal for me. Are you one of those people who like irritatin' people?"

            n "I-Uh."

            hide Kiunpleasentsurpise
            show Kihey

            ki "'Cause that was hella rude. What's wrong with you?"

            n "I didn't mean it like that."
            hide Kihey

        "Your old school":

            $ kiRep += 1

            show Kisadtalk

            ki "Right, well they said being a Vision major, I'm a Vision major, they said it made my case too complex."

            n "What does that mean?"

            hide Kisadtalk
            show Kihey

            ki "I know, right? I was so pumped to have a goal other than 'stay out of trouble' too."
            
            hide Kihey
            show Kisympathy

            ki "Everythin' was super structured, it was kinda nice. I don't know what to do with myself now."

            hide Kisympathy
            show Kisad

            "He's zoning out again, but I can tell he's still somewhat present."

            n "At least we have decent food."

            hide Kisad
            show KiBase

            ki "Oh yeah, and real plates too. They said we might be able to get music pumped in here after classes."

            "He seems genuinely happy to be here, and the food is good."

            hide KiBase
            show Kisympathy

            ki "Thanks for sittin' with me by the way."

            n "Hunh? Oh, yeah, no problem."

            hide Kisympathy
            show Kimildlyupset

            ki "It feels like everyone here already knows each other."

            hide Kimildlyupset
            show Kisympathy

            ki "It's hella uncomfortable, so it's cool to have someone who wants to talk to me."

            hide Kisympathy

        "Eating sage?":

            $ Vision += 1

            show Kicringe

            ki "I mean, you can, but I don't see why you'd want to eat that stuff plain."

            n "You said you choked on sage?"

            hide Kicringe
            show Kibwahaha

            ki "Sage smoke, man, not a plate of it. You burn sage to ward off evil spirits."
            ki "Not the nicest way to wake up in the mornin'."

            "He laughs."

            n "How does that work? Do they not like the smell of it or something? Can spirits even smell?"

            hide Kibwahaha
            show Kimischeif

            ki "Hunh... Never thought about it like that before, I guess they don't."

            hide Kimischeif
            show Kisadtalk

            ki "You'd hate the smell of it too if someone shoved ten smudge sticks in your face."

            hide Kisadtalk
            show Kibwahaha

            ki "Never had to eat it though."

            n "I guess that makes more sense."

            hide Kibwahaha
            show KiBase

            ki "Makes more sense than half the stuff you find online. At least it's harmless."

            hide KiBase

    show Kidude

    ki "Have you seen how big this place is?"

    hide Kidude
    show Kiteasing
    
    ki "When I heard only twenty-some kids would be here, I thought it was going to be super small."
    ki "No wonder the waitlist is so long."

    n "There's a waitlist to get in? Already?"

    hide Kiteasing
    show Kitalk

    ki "Well, yeah, any place that takes teens gets packed right away."
    ki "But the requirements here are really specific. I was lucky to get in."

    "I wonder..."

    n "Did you get questioned by a red-headed lady in a bad pantsuit?"

    hide Kitalk
    show Kicringe

    ki "Ahh... no. It was, umm... she had a scarf and really big earrings."

    hide Kicringe
    show KiBase

    ki "I ended up writing everything I could fit in the comment section of the application and it earned me a scholarship."

    hide KiBase
    show Kisadtalk

    ki "The interview was hard, but I managed to get through it. Sounds like you got a mean one."

    n "Yeah, a real piece of work."

    "Could it be? Did Vivaldi really meet this guy in person? Why?"

    n "But it's not like she's part of the faculty here, so I don't think we'll be seeing her."

    hide Kisadtalk
    show KiBase

    ki "That's good. And hey, we get a huge place all to ourselves. No upperclassmen either."
    ki "We should make the most of this year."

    n "Yeah, I guess so."

    hide KiBase
    show Kitalk

    ki "I'm gonna go stretch my legs. Don't worry about the bill, my meal plan will cover it."

    "There are only three cheese curds left. I barely had any. Where did they all go?"

    hide Kitalk
    show Kidontworry

    ki "Oh, and thanks for checking on me. You'd be surprised how many people would have just walked away."

    hide Kidontworry

    "He shoots a couple finger guns at me before walking away..."
    "The food's all gone. I should keep moving forward."

    return

label prologue_momoko:

    "As I make my way to the third floor, I hear a huge crash at the end of the hall."
    "The door to the school lab is slightly ajar. I rush in to see a girl with multicolored hair standing in the middle of theroom"
    "Or, at least, standing as well as she can with rollerskates on. Are those even allowed?"

    n "What happened? Are you okay?"

    show MhBase

    mh "Is one free outlet without a jenga tower in the way too much to ask for?"

    "She's trying her best to close one of the cabinets."

    n "I guess not... but that noise-"

    mh "Noise? I didn't hear anything. Maybe you're hearing things, Nagen."

    "A foreboding clunk comes from behind the small wooden door as she backs away."

    mh "Don't open that cabinet."

    n "How did you know my name? None of us have been here that long."

    "She starts laughing."

    mh "Decisions, decisions."
    mh "Do I pretend to be someone else and see how long it takes you to figure it out? Or do I tell you?"

    "I honestly can't place her face to a name. Her voice is sort of familiar, but..."
    "She's still laughing at me."

    n "Is it really that funny?"

    mh "You took it so personally when I kept forgetting your name."
    mh "I had it written on my hand for at least a year before I got it down."
    mh "Maybe my forgetfulness is contagious?"

    "I still got nothing, but there's no way I'd forget someone's name."
    "She'd have to have gone to Estella. Was she in my class or the Intel course?"

    n "I'm so sorry, could you please just tell me your name?"
    
    mh "Momoko Yoshino. My Proficiency is in Chemistry."
    mh "We were in the same special classes and homeroom in Estella for four years. Ring any bells?"

    n "Momoko!?"

    hide MhBase

    scene backgroundP4

    #[CG: Momoko as a younger kid]
    "She used to be the only one in class I was taller than."
    "She was this mousey wisp of a person who barely had the energy to present a school project."
    "It was like being in class with an asthmatic chihuahua."
    "There's no way I'd have recognized her without any help."
    #[Hide CG]

    scene backgroundlab

    show MhBase

    menu:

        "What happened to you?":

            $ mhRep -= 1

            mh "Oh, well, I was messing around with some new hair dye formulas and it kinda nuked my eyebrows..."
            mh "And my lashes..."
            mh "And my bangs..."
            mh "It exploded."

            n "That isn't too surprising."
            n "But I meant all of this; the clothes, the bigness. You're so different."

            mh "So? No one wanted me around before. At least now I think I'm fun, the rest should follow after."

            n "The rest of what?"

            mh "Rebellion!"
            mh "After spending months in boardrooms talking with boring grown-ups, I got so frustrated trying to make those jerks happy that I decided to stop caring what anyone thinks."

            mh "They can do whatever they want with my old invention."
            mh "But while I'm here, everything I make is going to be for me."

            "So this is her idea of what teenage rebellion looks like?"

            mh "Now I'm all feisty. Begone, frown wrinkles, begone!"
            mh "Today is supposed to be a good day, for we have science. Unsupervised science."

            n "...We always have science."

        "You look happy":

            $ mhRep += 1

            mh "For the first time in a long time, I feel like things are going to get better."
            mh "I got that vibe, y'know. Don't you?"

            n "I think you're one of the few."

            mh "Aww, don't go bummering all over my parade because you're jealous I'm thriving."

            n "I'm not jealous. You're jealous."

            mh "D'aw, cheer up Nagen, it'll be okay. I mean, you're still an Intel major, yeah?"

            n "Well, yeah..."

            mh "Then that's one more reason to smile."
            mh "We'll get to be in the same classes again! Come on dude, get on this level."

            n "Yeah, I suppose that's true."

            "She gives me a huge, cheesy grin and I can't help smiling too."

        "Mad scientist":

            $ Intel += 1

            mh "Now don't go saying that, you'll make people think I'm irresponsible or something."

            n "You're on wheels near a tower of glass."

            mh "It's not like I'm zipping around in Jams."
            mh "They're quads, baby skates, I'm safer in these than on solid ground; trust me."
            mh "Do I really give off crazy vibes?"

            n "No... but you have been known to be a bit of a pyromaniac."

            mh "Fire likes me, not the other way around. Besides, I've been trying to break up with combustibles."
            mh "Even contained explosions are too much stress right now."

            "That's a surprise. She was always so enchanted with fireworks and the like."
            "I can't imagine her doing anything else."

    mh "I think we all can use a break from everything going on outside."
    mh "It's best to think of this as a free vacation."

    n "It's hard for me to see how school and vacation fit in the same circle."

    mh "Really? I thought you loved school."
    mh "You were always so competitive about grades and you ran all those clubs. You practically lived there."

    "She shakes her head."

    mh "Eh, who am I to judge? I didn't have much of a life before either."

    n "Why are you here so early anyways? It's not like we have class yet or anything."

    mh "I'm looking for a place to put a stereo. If this is going to be my workshop, I'm going to need music."

    n "Workshop? You're going to start making stuff here?"

    mh "See, that look of panic is not what I'm going for."
    mh "I know I've got a bit of a destructive streak to make up for, but I swear I've changed."
    mh "I want to make nice things, the kinds of stuff that makes people happy."

    n "You don't mean-"

    mh "Cosmetics!"

    n "Umm..."

    mh "I've already started trying to make my own hair dye with... mixed results."
    mh "But there's still more things to try. It'll be like putting a spa in a bottle, doesn't that sound like fun?"

    n "I'm sure someone will like it."

    mh "I still gotta assert my dominance and claim this lab as my own, but once I do, you'll know."

    "I'm concerned."
    "Despite her good intentions, Momoko hasn't had the best track record with hazardous chemicals and staying on task."
    "I've turned in more than my fair share of charred paperwork as her lab partner."

    mh "You should come by some time and try my stuff!"
    
    n "I don't know..."

    mh "Why not? There's nothing more manly than taking care of yourself."

    n "That's not the issue."

    mh "Do you have any weird allergies or something?"

    n "Eggs."
    
    "And explosions."
    
    mh "Then it shouldn't be a problem, right? Oh, and if there's anything specific you want, just let me know."

    n "Yeah, just, don't spend all your time cooped up in here."
    n "I mean, what's the point of making people happy if you never see it?"

    "Just please, for everyone's safety, fixate on something else."

    hide MhBase

    return

label prologue_rei:

    "The classrooms are filled with wall to wall shelves of books."
    "The main floor has been tidied up to make room for the rows of antique tables."
    "At the back of the room is a hologram projection of a blackboard with a welcome message hastily scribbled on it."
    "This place feels less like a classroom and more like a lecture hall. In the center row, a girl sits quietly crying."

    n "Hey, are you okay?"

    show ReBase

    re "Oh Nagen, it's just awful, they took everything away! I totally forgot I had them with me until the alarms went off."
    re "I told them I wasn't going to stab anyone. I swear, I wasn't going to stab anyone!"
    re "But they took them all anyway: Rainbow Bright, Hog Cleaver, even Obsidian Snowflake!"

    n "Woah, woah, slow down. What are you talking about?"

    re "The swords! All of my sister's swords, what did you think I was talking about?"

    "Her sister's swords? I only know one person whose family heirlooms are weapons."

    n "I don't know, Rei, maybe you were listing Warrior Pony OCs."

    re "I'm such an idiot. I got so used to carrying them around in the riots."

    "She's always had issues with time."
    "Her poor grades were the only reason she ended up in the 'At Risk' class. It's a shame, really."
    "Her skills as a dancer and color guard member would have made her somewhat popular if she hadn't been lumped in with us."
    "I respect that she never blamed her classmates for the crummy treatment she received."
    "It would have been really easy to throw us under the bus to save her reputation."

    menu:

        "Your sister's gonna kill you":

            $ reRep += 1

            re "I know... Ugh, I should have gotten a storage locker or something. My poor babies."

            n "It's okay, I'm sure they just locked them up. There aren't too many safe places to dispose of swords right now."

            re "Right, you're right! I'll get them back eventually."
            re "For now, I'll just settle for plastic props. They're a shame compared to her craftsmanship."
            
            n "I'd like to see them sometime."

            re "I'm more of an artillery gal myself, but even I could see the beauty in her armory."
            re "You'll definitely have to come by this summer and see 'em."

        "Aren't they heavy?":

            $ reRep -= 1

            n "How could you forget you were carrying those things?"

            re "Nagen, honey, use critical thinking. I have endless endurance."
            re "Just because they were heavy doesn't mean it bothered me to carry them."
            re "I just got used to having them on me. I don't know how else to explain it."

            n "How many were there?"

            re "About eight. Any more than that and I wouldn't be able to move."

            n "You forgot you were carrying eight swords?"

            re "Yeah, and my fifteen knives, and my keys."

            n "Your keys?"

            re "The key chain was a brass knuckle kitty."
            re "I couldn't get the keys off because they were welded to the head like whiskers."

            n "Unbelievable."

            re "I already got three weeks probation, I don't need a lecture from you too."

            "This girl walks into school with the iron throne strapped to her back and I'm the one on probation?"

        "You haven't changed":

            $ Vigor += 1

            re "In a good way, I hope."

            n "Why wouldn't it be in a good way?"
            
            re "Well, I never was sure if you actually liked me."
            re "No one in our class wanted to be there. It always felt like everyone was just waiting to get out."

            n "I mean, you're not wrong, but that doesn't mean I disliked you. I just had other things going on."

            re "That's good to hear."

            n "Now that you've been caught bearing arms, you've really earned your title as a 'problem' child."

            re "You're the only ones who thought constantly forgetting homework wasn't a problem."

    re "I'm really glad you're here, Nagen."
    re "I was starting to think that I'd have to go to this big ol' scary place by myself."

    n "I'm surprised you recognized me."

    re "So you finally got to pick your own clothes, big deal. You still sound the same as always."
    re "We were really worried about you when you disappeared during the riots."

    n "We?"

    re "...Our classmates."
    re "And the girls from the squad. We were doing a headcount at the refugee center and couldn't find you."

    "I honestly didn't think they'd notice I was gone."

    re "Promise you won't run off on your own like that again?"

    n "Okay, mom."

    re "I'm serious. We've got to look out for each other now more than ever."

    "Even though she has no idea what I'm going through, she's still trying to look out for me."

    n "Thanks Rei, I'll try my best."

    re "O-oh, there's no need to thank me..."

    n "The same goes for you though, you can't let your guard down here. It's not safe."

    re "Nagen, I'm the one who accidentally brought weapons to the school."
    re "This place is supposed to protect us from the aftermath of the riots. They want to help us."

    "So that's what they've been telling everybody else."
    "It's a shame. As sweet as Rei is, she's too trusting."

    re "This is going to be a fresh start for us, you'll see."

    hide ReBase
    
    return

label prologue_rise:

    play music "music/TriumphantReturn.mp3"

    "There's only a few rooms open on the top floor."
    "This appears to be a meeting place of some sort, but it's glaringly apparent that everything in the room has never been used."
    "Every piece of furniture clashes despite the effort to match colors."
    "By the large bay window sits a poised girl with a tea set."
    "Rise Kisaki, her Proficiency is Allure, which I never fully understood."
    "According to Uitto, it means she;s a people magnet, like a lot of Charisma majors."
    "With me being in the “bad kids” class, I never really talked to her."
    "Her far off stare reminds me of a china doll. Across from her is an empty cup and chair."

    n "I'm sorry, were you waiting for someone?"

    "She perks up at the sound of my voice with slow, deliberate blinks."

    show RBase

    r "Yes, though high tea is an activity that can be enjoyed by anyone. Please, have a seat."

    menu:

        "Decline":

            $ rRep -= 1

            n "Sorry, not a big tea fan."

            r "How unfortunate."
            r "In that case, this room is reserved. I trust you do not need me to show you the way out."

            "There's no reason for me to stay here. I turn and leave."

        "Sit":

            $ rRep += 1

            n "Are you sure?"

            r "I can always make another cup."
            r "Besides, meeting others on neutral ground is the best way to make new friends."

            "She says this, yet there's no denying who's in control as she pours me a cup."

            n "This just looks like water..."

            r "It is for now. I would not want to accidentally poison a stranger through social convention by serving the wrong tea."
            r "Now let us see if I have anything you would like."

            "She pulls out a handful of packages and arranges them neatly on a dish, studying me with care."

            r "Choose whatever you would like."

            menu:
                "Golden Tip":

                    $ Charm += 1

                    r "It tastes best without milk, I should know."

                    "She takes a sip from her own cup. That must be what she's drinking right now"

                    n "You have multiple bags of $200 tea?"

                    r "Is that why you chose it? And here I thought you were aiming for the health benefits." 
                    r "It is supposed to help with anxiety."

                    n "Not going to argue it's 'not that expensive'?"

                    r "I would not know, I did not buy them."

                    "She gently caresses the gold rim of her teacup. It looks pretty old."

                    n "It might be a while until you can get more. Are you sure I can have this?"

                    r "By all means; you are curious and I already offered it to you, regardless of its worth."
                    r "It will be ready in about five minutes."

                    n "If you drink this a bunch, does that mean you're an anxious person?"

                    r "...I have been favoring it recently. But everyone has been seeking comfort more as of late, correct?"

                    n "I guess."

                "Spark Matcha":

                    $ Vigor += 1

                    r "Are you feeling tired?"

                    n "Like you wouldn't believe. It's been a long couple of months and the drive over here sucked."

                    r "You would not rather go rest?"

                    n "I can't, I still have things I need to do today."

                    r "Before school begins? That must be stressful."

                    n "Yeah. The school's so big and all the construction is making it hard to get around."

                    r "Your motivation is admirable."
                    r "Merely setting foot on campus felt like a chore to me, even though this is an area I should thrive in."
                    r "Where do you find the drive?"

                    n "I've spent the last few months with no internet and barely two people to talk to."

                    r "So the facility itself is the obstacle?"
                    r "Well, that certainly explains a lot, but you should not put too much pressure on yourself."
                    r "I am sure they will take roll tomorrow and you will have your answer then regardless."
                    r "It certainly would be more efficient."

                    n "No good. If I don't try my hardest, it will just keep me up all night."

                "Earl Gray":

                    $ Intel += 1

                    n "You'll have to forgive me if I'm a little shaky on the proper etiquette, but that's the one I can put milk in, right?"

                    r "I suppose if you would like to practice for afternoon tea then yes, milk and sugar are reserved for black teas."
                    r "But I am well aware my definition of polite behavior differs greatly from those here, so please do not be afraid to act as you normally would."

                    n "Thanks."

                    "She says that, but I feel like she's watching my every move. Too bad there's no food."

                    r "You must be new at this if you have to think so much about drinking tea."
                    r "A true blue blood has such notions drilled into them since birth."

                    n "The lessons I took this year weren't my idea. This will probably be the only time I'll use them."

                    r "What makes you so sure?"

                    n "I don't think the people who taught me plan on keeping me around after graduation."

                    r "It is a shame when you do not feel like you belong."

    r "Perhaps I could help you find who you have been looking for?"

    n "I never said I was looking for anyone specific."

    r "My apologies, I made an assumption based on your behavior earlier. Was I mistaken?"

    "There's a glimmer in her eye as she speaks."

    n "Not exactly. I'm looking for some old friends of mine."
    n "I appreciate your offer to help, but there'd be no way to contact each other. Someone like you wouldn't want my number."

    r "What gave you that idea?"
    r "Nagen, this may be overstepping my bounds, but I do not think your group is worth this much of your time."
    r "All they ever did was get you into trouble."
    r "There are plenty of people here who would make more supportive friends."

    "She's acting like she's helping me, but that's clearly an insult towards my friends."

    n "You don't know what you're talking about."

    r "I have been mistaken before."
    r "I just worry that you have been exploited by individuals that do not value your personal achievements."

    n "And you do?"

    r "I could, though I am not in the best position to impose myself on anyone at the moment."
    r "Given enough time, I could compose a detailed list of potential matches that would be mutually beneficial."

    n "Not interested."

    r "Suit yourself."

    "She smiles pleasantly as if nothing's wrong."
    "Though I suppose for her, there isn't anything wrong with what she said."
    "I can't take the silence."

    n "Thanks for the tea, but I need to go."

    r "Anytime, Nagen. I do hope our next meeting will be pleasant."

    hide RBase

    "I turn and leave."

    return

label prologue_dyre:

    "At the end of the first-floor hallway is a solid metal door with 'Computer Lab' written on it."
    "I can't get it to open, no matter how hard I try."
    "It's not like I need a computer that bad, but I had hoped maybe they had access to the internet."

    show DBase

    d "Tesuta, is that really you? What are the odds I'd find you here? I thought you were too smart for computers."

    "Of all the people to run into, why'd it have to be him?"

    n "Hello, Dyre."

    d "Now, is that any way to treat an old friend?"

    "When we were younger, we hung around each other all the time, until one of his pranks landed us both in deep shit."
    "I got expelled to the 'bad kids' class after that; he got a slap on the wrist."
    "Being the principal's grandson had its perks for him."
    "We stopped talking after that."

    n "I said hello, didn't I? I don't know what you expected, opening with backhanded compliments and shit."

    "He smiles at me like the cat that got the canary."

    d "Would it really kill you to give people the benefit of doubt? I just wanted to talk."
    d "After the riots, we didn't exactly get a list of survivors, no one knew where you went."
    n "Well considering I ran away from home before the riots, I don't find your 'sympathy' terribly inspiring."
    d "...We just thought you were out sick. You ran away? Shit, man."

    menu:

        "Who told you I was sick?":

            $ dRep += 1

            d "I mean, you called out sick all the time."

            n "Yeah, but do you remember if anyone specifically said I called out?"

            "I ran away right after lunch to avoid my parents."
            "It wouldn't be unheard of for me to get pulled out of school in the middle of the day, but I wonder..."

            d "Now that you mention it, Professor Kataki was the one who told us."

            "That's weird, why would a homeroom teacher from another class be spreading rumors about someone else's students?"

            d "We were wondering why a whole bunch of kids didn't show up, and he said they got strep."
            d "Next thing I know, the whole school's getting evacuated, teachers started going MIA, and kids were disappearing left and right."
            d "It was like something out of a horror movie."

            n "I can't believe they lied about what was going on."

            d "Does that mean you're going to tell me the truth instead?"

            n "Hunh?"

            d "I keep asking you direct questions about that night, and you keep deflecting. Are you going to tell me what actually happened?"
            
            n "It's like I said, I ran away."

        "Yeah, sorry":
            $ Charm += 1

            d "What are you apologizing to me for? I don't care where you live, as long as you're okay."
            d "There's a lot of weirdos out there that'd try to take advantage of a kid like you."

            n "We're the same age!"

            d "Yeah, that's how I know."
            d "You got talked into all kinds of stuff when we were younger and you still won't let it go."

            n "I... I let some stuff go."

            d "Oh really?"
            d "Well then, what about when you swore up and down that cow's milk stole calcium from your bones because you read it in some paper."

            n "I did, and it wasn't just 'some paper', it was written by a doctor."

            d "Yeah, with a PhD in Fine Arts."

            n "I was hoping you'd forget that part."

            d "Hah! No way."
            d "But that's totally my point, you get all worked up and you don't take time to see the other side."
            d "It makes it way too easy to mess with you."

            n "You could just, not do that."

            "He was the one who showed me that paper in the first place."

            d "Stop? Where's the fun in that?"

            "I should have known better than to talk to him."

        "Of course":

            $ dRep -= 1

            n "My helicopter parents never gave me a moment to myself."
            n "Then you got me thrown in my mom's class and suddenly I was under surveillance 24/7."

            d "How the hell is that my fault?"
            d "I'm not the one that threw a tantrum up in the principal's office. That was all you."

            n "It wasn't- For the last time, a panic attack isn't something anyone chooses to have."

            d "Do you have any idea how long she waited for you during the evacuation?"
            d "I know Dr. Tesuta wasn't exactly the nicest teacher, but she refused to leave the shelter without you."
            d "Some kid's parents never showed up."

            "Of course he doesn't get it. Even if I agreed with him, he'd just flip sides and argue the opposite."

            n "I couldn't stay there any longer. That place was killing me."

            d "Well, at least everything turned out okay for you."

    d "It's kind of odd this place is locked up, don't you think?" 
    d "All the major renovations were finished up to the fourth floor."

    n "Computers are expensive. It makes sense a teacher has to be in the room when we use them."

    d "That's the rationalization you're going with? Boring."

    n "Reality usually is."

    d "Come on. In this huge, old building, you don't think there's a bit of history to it?"
    d "Something that would make this place more affordable for a school to set up shop in?"

    n "I don't like where this is going."

    d "It's totally a murder basement. It's right where the stairs would be if there was a lower level."
    d "I heard the psychic girl's afraid to use her powers here because of all the angry spirits hanging around."

    #[Noise cue, hum/wind]
    d "Yeah, it's haunted as fuck. Ten bucks says they never let us in there this year."

    n "Like you have ten dollars."

    #[Noise cue, distorted computer cry, soft]
    d "I will soon."

    n "Knock it off, this isn't funny."

    d "I didn't do anything, something inside did. Something they don't want us to see."
    d "You got to admit, they aren't being terribly honest with us."

    "I'm not going to fall for this. I know they're lying about the Junior Gladiators, that my friends and I are here."
    "There's probably other stuff about the DVP they're covering up too."
    "He's just... trying to get under my skin and get me to say something I shouldn't."
    "I mean, there's no way this place is actually haunted, right?"

    #[Noise cue, distorted computer cry, loud]
    n "Y-you're an asshole. It's too early in the year for this man."

    d "Fine, don't believe me."

    hide DBase

    "He wanders off, waving goodbye over his shoulder as he goes."
    "I really don't want to stick around, not that I believed a word he said. I should look elsewhere."

    return

label prologue_jona:

    play music "music/SpeedWins.mp3"

    "I follow a paved walkway behind the field to a sparsely wooded area."
    "Hidden behind rows of planters is a small concrete stage"
    "It looks like it hasn't been long since the poppies were watered. The earth smells damp and cool."

    show JRelax

    j "....."

    "Someone's staring at me. They aren't coming any closer, but they aren't looking away either."
    "With all the junk covering their face, it's impossible to tell what they're thinking."

    j "....."

    "Creepy."

    j "....."

    n "If you have something to say, spit it out already."

    j "...I knew it."

    n "Uhh... What?"

    j "You're the only one I've seen with that hue of magenta, but I wasn't sure."
    j "Nothing's more awkward than walking up to someone thinking you know them when you really don't."

    n "...Right..."

    hide JRelax
    show JFrustrated

    j "Nagen, it's me, Jona."

    "That makes more sense. Jona was the most withdrawn and awkward member of our gang."
    "Looks like he covered himself head to toe the moment he got a chance. That explains why he's so calm right now."

    n "You certainly got your hands on a lot of... accessories since we last talked."

    hide JFrustrated
    show JRelax

    j "I made them myself! Well, I can't sew or blow glass, but you get the idea."

    n "Does the gas mask work?"

    j "...What do you mean 'does it work'?"

    "Jona has a habit of repurposing things for art without knowing what they are."
    "He had tried inventing things, but always valued aesthetics over functionality."

    j "I haven't passed out yet, so I think it's breathable."
    j "Why? Do you think it looks weird? Like, you'd cross the street to avoid me kinda weird?"

    "There's one right answer."

    n "Yeah, kinda."

    hide JRelax
    show JHappy

    j "Then it's kinda working!"
    j "I'm glad you're here. I was starting to think I'd have to track everyone down myself."

    n "You know we're not supposed to do that, right?"

    j "Since when have we listened to what they say? I mean, you're doing the same thing aren't you?"
    j "Of course, you are! ...but wait, if you didn't recognize me, why'd you walk up to me?"

    menu:

        "Opposites attract":

            $ Vision += 1

            n "Ah, well, I haven't seen anyone who's dressed in full counter-culture around here."
            n "I mean, steampunk is definitely more mainstream, but still..."
            n "Yeah, it's uh, it's neat. The wordless staring you were doing, not so much."

            j "Aw shoot, you're making me blush."

            n "....."

            j "Please, I didn't mean to interrupt. It's nice not to be the one monologuing for once."

            n "I-I don't know man, don't put me on the spot like that!"

            j "Are you flustered?"

            n "N-no."

            hide JHappy
            show JRelax

            j "Really? But you're stuttering and your face is changing colors."
            j "Hiro said that happens when you're flustered."

            n "You caught me off guard is all. Hiro doesn't know what he's talking about."

            j "Oh. Well, I shouldn't be too surprised, he's been wrong about a lot of things before."
            j "I'm still upset there are no strawberry milk cows. The chocolate cows must be lonely."

            "Just let it go, Nagen. You don't want to go down that road again."

            hide JRelax

        "To start a fight":

            $ jRep += 1
            
            hide JHappy
            show JFrustrated

            j "!!!"
            j "Why!?"

            n "You kept staring at me. I figured you were trying to start something."

            j "I'm not big into social clubs, actually"

            n "What? ...no, I meant- Nevermind."
            n "You just can't stare at people non-stop like that. People'll get the wrong idea."

            hide JFrustrated
            show JRelax

            j "I was just drawing."

            n "Drawing? Like, drawing me, or..."

            j "Not important. Just cause my goggles face somewhere doesn't mean I'm looking there."
            j "In fact, I haven't looked at you the whole time we've been talking. They're really handy."

            "Somehow, that's more unsettling."

            j "I wish I had the self-confidence to assume people were paying attention to me like other people do."
            j "Well, actually, that would be more self-conscious than self-confident, wouldn't it?"

            "I know he's not talking about me when he goes off on tangents like this."

            j "Maybe if you stop acting as if you cared, you'd be more self-confident... or conceited..."

            hide JRelax
            show JFrustrated

            j "Or is it conceited to assume people are looking at you at all?"
            j "I forgot where I was going with this."

            n "I'm not sure either."

            j "Oh, right! I was trying to match your 'playful' banter. I've been practicing."

            n "Well you succeeded in confusing both of us."

            j "Sorry. I'll try better next time."

            n "You really don't have to."

            hide JFrustrated

        "Look for an exit":

            $ jRep -= 1

            n "You're the one who walked up to me."

            "I rarely hung out with Jona one on one. For one, this is the kid that carved up desks for fun."
            "The other was, well, he reminds me of my mom for some reason..."

            hide JHappy
            show JRelax

            j "I suppose I did talk to you first. Are the others here?"

            n "I don't know, that's why I'm looking around."

            j "We could do it together! I have logs on Uitto and Hiro's daily routines."
            j "Oh, but, you've already got those memorized, don't you?"

            n "...yeah... I totally know those things..."
            n "Haven't ever listed them out in a planner though. Because, uh, that would be kinda weird."

            "He tries to hide the notebooks in his bag."

            hide JRelax
            show JFrustrated

            j "Bad weird or good weird?"

            n "I didn't mean either. Weird is just an adjective."

            j "People always say that, but they mean 'good' weird or 'bad' weird. Even I can figure that out."

            n "Aahhh... Good weird! I meant good weird."

            hide JFrustrated
            show JHappy

            j "...Hunh. Well, you gotta show me your class schedule so I can update your book. My JG logs are pretty dated."

            n "We're not in the Liberation Front anymore. You don't need to keep logs on everyone."

            j "...but I like knowing everyone's schedule."

            "This is just one of those things I have to let go of, I think."

            n "Okay, but don't tell anyone outside of the group that you're doing that."
            n "We might get in trouble for resuming club activities if they know."

            j "Okay!"

            hide JHappy

    # Not safe dialogue if someone comes here before finding anyone

    n "Anyway, everyone's going to be meeting in room 313 at four."

    show JHappy

    j "Everyone, everyone!?"

    n "Yeah. But, uh, you can't come with me, we'll stick out too much walking around together." 
    n "It's gotta be a secret meeting."

    j "...I'll be there."
    
    n "Great, talk to you then."

    j "....."

    hide JHappy
    
    return

label Meeting:
    play music "music/Unconditionally.mp3"
    scene backgroundstuco

    "I walk into the room to find Hiro and Jona waiting for me. Uitto comes in silently behind me."
    "The last time we were all together, it was to tell everyone that Lethe had passed."

    show JRelax at center

    j "So, who's leading the meeting?"

    show HJudge at left

    h "Whadya mean?"

    j "Well, usually Odori tells us what to do, but I don't see her here."
    j "I haven't seen her since she called for a cease-fire. Hiro, you were supposed to be guarding the base, where-"

    hide HJudge
    show HSadtalk at left

    h "So Nagen, what's the plan?"

    hide JRelax
    show JMad at center 

    j "Why are you avoiding the question?"

    hide HSadtalk
    show HGrump at left

    n "Focus guys, both of you. I never 'said' anything about a plan."

    hide HGrump
    show HMad at left

    h "So you wanted to hold a meeting and there isn't even a plan?"

    hide JMad
    show JFrustrated at center

    j "I am so confused."

    n "Guys, I know you're wondering why I called you here."

    show Uittoyell at right

    u "Just spit it out, Nagen. You knew I was here, I'm sure the same went for the others too."
    u "So, where the hell's Odori? Did she just not make the cut or did she stop participating in life too?"

    h "Uitto!"

    hide JFrustrated
    show JRelax at center

    j "Well, Nagen, do you know what happened to her?"

    n "She's... still missing. No one's found her."

    "Hiro doesn't look surprised, but he's definitely avoiding Jona's almost accusatory turn towards him."
    "It's hard to tell with the goggles. Uitto keeps glaring at me."

    hide Uittoyell
    show Uittosadtalk at right

    u "That's what I thought..."
    u "So, when are you going to beg for our forgiveness? Or are you going to keep acting like {i}you're{/i} not the one who sold us out?"

    hide Uittosadtalk
    show Uittosad at right
    hide JRelax
    show JDepressed at center
    hide HMad
    show HGuilt at left

    n "What are you talking about?"

    hide Uittosad
    show Uittoyell at right

    u "I'm talking about how, despite pleading not-guilty, I ended up in reform school!"
    u "You're the one that knew we'd all be here, so you have to be in their pockets!"

    hide Uittoyell
    show Uittosad at right
    hide HGuilt
    show HMad at left

    h "Quit calling him manipulative! Not everyone is good at talking people into believing lies like you."
    
    hide HMad
    show HGuilt at left

    h "We should just be happy we're together again..."

    hide JDepressed
    show JMad at center

    j "Of course you would say that, you coward. If it were up to you, we'd be groveling on our bellies years ago."

    n "Now hold on..."

    hide HGuilt
    show HGrump at left

    h "You're one to talk! They were asking me about the doomsday cult we supposedly started."

    hide HGrump
    show HWait at left
    h "I wonder who's pet project that could have been?"
    hide HWait
    show HMad at left
    h "Your stupid stories probably got us into more trouble than we should have been in."
    h "And you're running around the school looking like a freaking serial killer! Are you trying to get us targeted!?"

    hide JMad
    show JFrustrated at center

    j "Steampunk is art! Quit acting like my art is hurting people."

    hide JFrustrated
    show JMad at center
    hide HMad
    show HSulk at left

    j "You're the one that left Odori alone with people on our tail!"

    n "Guys! Look, I know things aren't ideal right now, but that's why I called you here."
    n "We got separated on purpose, and all of us were forced to do things we didn't want to do to get by."
    n "But we're together now, and we need to figure out what to do next."

    hide Uittosad
    show Uittogurl at right

    u "Oh really, and why should we listen to you? You sold us out to the DVP!"

    n "I never-"

    hide Uittogurl
    show Uittoyell at right

    u "The agent they sent to get me mentioned you by name!"
    u "I bet they gave you an offer you couldn't refuse or some cliche that makes you feel {i}better{/i} about leaving us to the wolves..."

    hide Uittoyell
    show Uittosad at right

    u "What else could you want from us?"

    n "Look, I'm sorry, really I am. But the DVP interrogated us separately for this very reason."
    n "They wanted us to turn on each other and make their boarding school look good."
    n "They're afraid of what we accomplish when we work together."

    hide JMad
    show JDepressed at center

    j "Well, yeah. A faceless organization is ten times scarier than a handful of teens."

    hide HSulk
    show HFINE at left

    h "I'd have to disagree. Faceless organizations don't punch you in the junk in the middle of the night."

    n "What!?"

    hide HFINE
    show HGrump at left

    h "My foster brother's an asshole."

    hide Uittosad
    show Uittogurl at right

    u "...Right. So, you were saying..."

    n "If we work together, all of us can get the hell out of here, for good."
    n "It's going to be lame, but if we can play the part for a year and play it well, they've got nothing on us."
    n "We make them think we're model students and we gain support from the students here to prove our innocence."

    j "How's that any different from what they told us to do?"

    n "Because the whole student body will be in the palm of our hands and they'll be none the wiser."
    n "I'm going to take control of whatever passes for a student council and... well that's all I got for now."

    hide HGrump
    show HHeadempty at left

    h "...Cool..."

    n "And in the end, we'll get a lighter sentence and still get to be heroes."

    hide HHeadempty
    show HBase at left

    h "Yes! Good! I like this plan!"

    hide JDepressed
    show JHappy at center

    j "That isn't exactly a plan, but it doesn't sound like it'll get us in trouble..."

    hide Uittogurl
    show UBase at right

    u "So, we get stuck here for a year, make nice and live happily ever after?"

    n "Pretty much."

    u "Not interested."

    hide JHappy
    show JFrustrated at center

    j "What are you talking about?"

    hide UBase
    show Uittotalk at right

    u "You all can act like the last few years didn't happen and live in a fantasy world, but I'm not interested in lying to the randos at this school."

    hide Uittotalk
    show Uittocringe at right
    u "I'm a wanted criminal, I ruined people's lives, and no amount of crocodile tears will make that okay."
    hide Uittocringe
    show Uittosadtalk at right
    u "Of course, the people I hurt deserved it, but I'm not a helpless victim anymore. It's not fair to the other kids..."

    n "Then why plead not guilty if you're so honest?"

    hide Uittosadtalk
    show Uittosad at right

    u "Some of us actually want a normal adult to say we were right instead of begging for probation."

    hide HBase
    show HSadtalk

    h "Come on, guys, arguing will get us nowhere."

    hide Uittosad
    show Uittosadtalk at right

    u "I'll see you later, Hiro... maybe. I shouldn't be here..."

    hide Uittosadtalk
    show JFrustrated

    j "Uitto, wait!"

    "She leaves without another word."

    hide JFrustrated
    hide HSadtalk

    menu:
        "Forget her":
            $ uRep -= 1
            $ jRep -= 1

            n "Who needs her anyways? It's not like she ever did anything important."

            show HGuilt at left
            show JRelax at right

            h "Come on man, I know you're pissed-"

            n "No, she wants to throw her little diva tantrum, that's fine."

            j "Doesn't her ditching throw off your master plan?"

            n "Every experiment has an outlier. As long as the majority of the school believes us, nothing will change."

            hide JRelax
            hide HGuilt

            jump meet_main

        "She'll come around":
            $ jRep += 1
            $ hRep += 1

            n "She just needs some time to get over it. She will get over it, won't she?"

            show HGuilt at left
            show JDepressed at right

            h "Ehh... hard to say."
            h "She still refuses to watch Avenger League ever since it took the time slot of her favorite show."

            n "Empire of the Lost did not deserve to be canceled and I support her decision."
            n "But this is something entirely different. This is about our lives."
            n "She could end up with a life sentence. She knows that, right?"

            j "I don't know. She didn't look mad at us, not enough to hold a grudge."
            j "I don't care what her aura looked like to you."
            j "Nagen's right, she's not going to hold a grudge over this forever. We just have to wait."

            hide JDepressed
            hide HGuilt

            jump meet_main

        "Go after her":
            play music "music/CoolNights.mp3"        
            $ uRep += 1

            n "Uitto, wait!"

            scene backgroundhall1 #Not sure if this is the right one

            "Has she been crying?"

            show Uittosad

            u "What?"

            n "What happened to you?"

            u "Excuse me?"

            n "You're angry, I get that, but is this really all about me?"

            u "I... I don't... Seeing everyone again..."
            u "Now isn't a good time, I'll just seem emotional and stupid. I need to clear my head."

            n "Okay. If there's anything I can do-"

            hide Uittosad
            show Uittoembarrassed
            u "You'll try and fix it, I know."
            hide Uittoembarrassed
            show Uittocringe
            u "This is just a little too much right now. I'll see you later."

            hide Uittocringe

            "So she isn't actually mad at me. I guess that's good, but I'm still worried."
            
            jump meet_main
    
    label meet_main:

        play music "music/Undertow.mp3"
        
        "I managed to get the guys to agree to join me. They may question my methods, but at least they're on board."
        "As for Uitto... I know we're all upset getting shoved into reform school, but it didn't seem like she had a better idea than mine."
        "I can't postpone returning to my dorm any longer."

        scene backgroundroomn

        "Part of my aversion comes from how barren and sterile the rooms are."
        "I'd compare this place to a prison, but at least prisons are fully indoors."
        "I guess public opinion on Proficiency-centered education is dwindling because we're all having to stay in musty portable buildings."
        "I hope it's well-ventilated. I cringe to think of how hot this place could get in the summer."
        "I don't have the energy to unpack yet. I shrug out off my jacket and collapse on the bare mattress."
        "As I drift off to sleep, I desperately try to convince myself everything will work out in the end."

        if Vision >= 4:
            #CG teachers
            ya "So, what's the plan?"

            sa "Darling, this was the plan."

            v "For now, we will proceed as originally intended. This just means we'll have to devote more energy to security."

            ya "With what time?"

            sa "The four of us are burnt out as it is. We need manpower. If you would just let me call a few people..."

            ik "Man, hearing you guys bicker like this really reminds me of the old days."
            ik "Still..."

            #CG note

            g "Dear Fallen Heroes,"
            g "I have reason to believe you are making use of revealing information deemed inaccurate and unfounded in nature."
            g "It is required that you cease and desist the following; holding registered Proficiency Users against their will, utilizing Proficiency-based education for personal benefit."
            g "If you fail to comply within fourteen days, I will have no choice but to pursue the matter personally."
            g "Sincerely, Estella O'Laurel."

            #CG teachers

            ik "This is a little too eloquent for a student to be responsible, don't you think Viv?"

            v "We can't exclude any possibility at this point."

            ya "For your sake, I hope it's some dumb kid."

            call chapter_one
        else:
            call chapter_one