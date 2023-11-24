label newgame:
# Player's Stats
    $ Vigor = 0
    $ Vision = 0
    $ Intel = 0
    $ Charm = 0

# Player Data
    $ VigorSP = 0
    $ VigorMax = 3
    $ VisionSP = 0
    $ VisionMax = 3
    $ IntelSP = 0
    $ IntelMax = 3
    $ CharmSP = 0
    $ CharmMax = 3

# Story Reputation Points
    $ Hero = 0
    $ Villain = 4

# Daily Life
    $ FreeActions = 0
    $ DefaultActionCount = 1
    $ ExtraActionCount = 2
    $ Day = 0

# Investigation
    $ Clue1 = False

# Player Relationships
    $ chRep = 0
    $ dRep = 0
    $ hRep = 0
    $ iRep = 0
    $ jRep = 0
    $ kRep = 0
    $ kkRep = 0
    $ kiRep = 0
    $ mRep = 0
    $ mhRep = 0
    $ muRep = 0
    $ nkRep = 0
    $ rRep = 0
    $ reRep = 0
    $ sRep = 0
    $ shRep = 0
    $ tRep = 0
    $ yRep = 0
    $ uRep = 0

# Character Flags
    $ chTurn = 0
    $ dTurn = 0
    $ hTurn = 0
    $ iTurn = 0
    $ jTurn = 0
    $ kTurn = 0
    $ kkTurn = 0
    $ kiTurn = 0
    $ mTurn = 0
    $ mhTurn = 0
    $ muTurn = 0
    $ nkTurn = 0
    $ rTurn = 0
    $ reTurn = 0
    $ sTurn = 0
    $ shTurn = 0
    $ tTurn = 0
    $ yTurn = 0
    $ uTurn = 0

# Prologue Only

    $ friend = 0
return

    # Opening video goes here.

label prologue:
    scene backgroundpolice

    play music "music/LostWithin.mp3"

    "My whole life, I feel like I've been dragged around by my collar."
    "I guess when most adults see a kid act out of line, they're overwhelmed with a need to control the situation."
    "Funny, seeing as that's the very thing I've been fighting for: a chance to be in control of my life."

    show sprite CopBase

    cop "Please state your name and registered Proficiency."

    n "My name is Nagen Tesuta."
    n "I possess an Intelligence Proficiency."
    n "Anything I see, hear, or experience is recorded in perfect detail."

    hide sprite CopBase

    "I tap the side of my head."
    "Having a great memory doesn't really make me smarter than anyone else, but the ability falls under the Intelligence Major."
    "People are just so determined to classify things so they can feel important, they stop asking whether it's worth the effort."
    "I mean, some people can go their whole lives without realizing they have a Proficiency."
    "It's nothing special. The only reason I know about mine is because I was groomed to have it."

    show sprite CopBase

    cop "Look, you and I both know it's not looking good for you."
    cop "I mean, you've heard the charges: premeditated murder, inciting a riot, mayhem, and menticide."
    cop "These are all with a registered Proficiency which will add twenty-five more years to your sentence."
    cop "Don't even get me started on the use of deadly weapons."

    show sprite KoeBase

    ka "There's more than enough evidence to try you and your cohorts as adults."
    ka "In the case of The Supreme Court vs. Lethe, vigilantism was determined to be a Class One felony."
    ka "Some of her sympathizers, like you, seem to think they are above the law."
    ka "If we were able to find her remaining supporters, it would be an excellent demonstration of goodwill."
    ka "We all remember-"

    hide sprite KoeBase
    scene backgroundblack

    #[Screen blacks out]

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

    o "Gladiators! You'll never believe the guest speaker I found for today's meeting!"

    #[Pan out, Lethe is standing behind her, smiling]

    l "Hello, little ones! It's so inspiring to see young people take an interest in our initiative."
    l "Even if my colleagues disagree, I think it's important to foster the growth of the industry."
    l "After all, it's rare to see young people so devoted to liberating the justice system."
    l "Not many have what it takes."

    n "O-of course! I mean, who wouldn't want to become a real live hero?"
    n "I can't believe you're actually here! We've mostly been planning. I mean, what else can we do?"
    n "But we've been working day and night on what we'll do as real heroes!"
    n "Not like a hobby… or anything… We meet everyday after school, and even longer on weekends."
    n "We can't use the classrooms, so we meet in the park!"

    "I started gathering the draft papers, but when I looked up at her face, she seemed so sad."
    "She took a seat at the table in silence."

    l "I ask this of all my fans, just as a formality..." 

    stop music

    l "Do you feel safe at home?"

    play music "music/Voyage.mp3"

    scene backgroundP2

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

    play music "music/LostWithin.mp3"

    "But that was the me of two years ago, the kid who grew up in a glass box waiting for my veins to stop burning."
    "The unwilling test subject of the very people who stand before me claiming I'm the monster."
    "Back before the Department of Villain Prevention was a governing body under Estella's control."

    n "I know you. You were the prosecutor during Lethe's trial."
    n "Trying to extort information out of a child for your old department? That's surprisingly underhanded of you."

    show sprite KoeBase

    ka "Then you understand what you're up against."
    ka "Choosing to represent yourself in court only gave you a fool for a client."

    "She's the prosecutor for my case!?"

    ka "I'm just doing my job, Mr. Tesuta, in ensuring I have all the information I need for my case."
    
    hide sprite KoeBase
    show sprite CopBase

    cop "Just make this easier on yourself and fold. It'll be better than what your friends are going through."
    hide sprite CopBase

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

            call interrogation_end

        "Refuse": #(Fast forwards past all choices, all points put in Intelligence)
            $ Intel += 4
            call interrogation_1

    label interrogation_1:

    n "Good cop, bad cop? Really?"
    n "I'm sorry, it's going to take more than a movie cliché to get me to tell anyone anything."
    n "Also, I was never read my rights, so unless you want a mistrial, I suggest you start treating me like an adult before trying me like one."

    show sprite CopBase
    cop "That's not how the system works, kid."

    hide sprite CopBase
    show sprite KoeBase

    ka "No, he has a valid point. You want to be talked to like an adult? Fine."
    ka "Mr. Tesuta, if you don't give us the information we need, there will be no 'deal'."
    ka "The first step is pleading guilty in court. There is no workaround."

    "So it's her way or no way, hunh? Fine, whatever, she has her reasons; I have mine."

    hide sprite KoeBase

    #[Player Choice]

    menu:
        "I have to protect my teammates": #(+Hero, +Vis)
            $ Hero += 1
            $ Vision += 1
            n "I'll plead guilty in court, but I and I alone am guilty of these charges."
            n "I cannot say the same of my friends; they genuinely believed in what Lethe told them..."

            "If I lie, I could be held in contempt of the court, but if I play the 'scapegoat', maybe they can get out of here unscathed."
            "Either way, someone has to answer for what we did."

            call interrogation_2

        "I don't have a choice": #(+Villian, +Vig)
            $ Villain += 1
            $ Vigor += 1
            n "Under the advice of my legal counsel, I will."

            "Maimai would be heartbroken if I got locked away. She's been through this before."
            "I practically have a walkthrough written on my sleeve."

            show sprite CopBase

            cop "Do you believe you are guilty of these crimes?"

            n "....."

            "I've talked too much already. Isn't the confession enough?"

            hide sprite CopBase

            call interrogation_2

        "It's all part of the plan": #(+Int)
            $ Intel += 1
            n "I'll cooperate."

            "It's too dangerous to make a move now. Best to play along for now."

            call interrogation_2

        "I need to lighten my sentence": #(+Chr)
            $ Charm += 1
            n "...okay..."

            "I hang my head at a 30-degree angle and feign the slightest tremor in my shoulders."
            "The more sympathy I can gain, the better."
            "No one will want to hear my side of the story if I act like the violent criminal they think I am."

            call interrogation_2

    #[Return to Main Branch]
    label interrogation_2:

    n "I fully understood the ramifications of my actions and stand at the mercy of the court."
    n "I aided in the brainwashing of my classmates and tried to conquer the Guwon Province for my own benefit."

    show sprite CopBase

    cop "That's all we need to hear."

    ka "Not quite. I still have a few questions for Mr. Tesuta."
    ka "The Junior Gladiators started as a club at your school, later to fall down a path of destruction."
    ka "And yet, no one can tell us whose fault this was."
    ka "In your estimation, who was the leader during the attack?"

    hide sprite CopBase

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
            "Proficiencies were dangerous to the general public, but so is a pen if you use it right."
            "These people, however, just want to confirm what they already believe, so I'll just tell them what they want to hear."

            call interrogation_3

        "The one who gathered the army": #(+Hero, +Vig)
            $ Hero += 1
            $ Vigor += 1
            n "Hiro Morine was our leader. He insisted on it constantly."
            n "If it wasn't for him, we wouldn't have gathered nearly as much support."

            "He wasn't a very good leader after that..."
            "Actually, I was the one who did all the real work, but he meant well."
            "He was the first one of us to get captured by these hypocrites."
            "Even after getting dragged down, he insisted on taking credit for what happened. I hope he's okay."

            call interrogation_3

        "The one who planned the attack": #(+Int)
            $ Intel += 1
            n "I was. I deliberately withheld information from my peers, knowing it would sway their decision to stay."
            n "In the end, I was the only one standing."

            "Well, not exactly standing. Let's just say, I don't handle failure very well."
            "I was lucky Maimai was crazy enough to spare my life."
            "If I manage to get out of this, I should thank her properly."

            call interrogation_3

        "The club president": #(+Vis)
            $ Vision += 1
            n "Odori Hato was our leader. She's the one who brought Lethe's attention to our club."
            n "Odori just wanted to help us and a cheesy superhero club was her answer."

            "After Lethe died, she insisted we continue with our plans so that everyone would be happy again."
            "It's amazing how far out of hand things got."

            show sprite CopBase

            cop "Do you know where Ms. Hato is?"

            n "No, she's not with us anymore."

            "I want to believe she's still out there, but…"

            hide sprite CopBase

            call interrogation_3

    #[Return to Main Branch]
    label interrogation_3:

    show sprite KoeBase

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

            show sprite KoeBase

            ka "According to eyewitness testimonies, you sought out innocent civilians who were in hiding and killed them on sight."
            ka "We found seventeen assault rifles in your room. Were these also for your defense?"

            n "Yes."

            "It's not like I bought the guns online or anything. Guwon was already a dangerous place to live."
            "If you were alone on the street for over twelve hours, you could get killed or worse."
            "Wandering around the city with a gun was safer than going back home anyway."
            "I had all kinds of other machines I was playing with that I got from the junkyard, but that's not what they care about."

            ka "Did you use any of these guns against another person?"

            n "Yes."

            hide sprite KoeBase

            call interrogation_4

        "Rebuild the city": #(+Hero, +Int)
            $ Hero += 1
            $ Intel += 1
            n "Before making any plans, I would have had to reverse the damage that had been done."
            n "I was in command of over five hundred people; they needed a place to live once the dust settled."

            show sprite KoeBase

            ka "That's all?"

            n "Well, we would have needed a hospital next as well as to secure some kind of agricultural production to feed everyone."
            n "That alone would have taken months, and who knows what other problems may have arisen."

            "What can I say, I read way too many doomsday zombie comics as a kid."
            "If I wanted to be a good leader, I had to make sure my people were provided for."

            ka "This would be the same city you planned to bomb, correct?"

            n "I wouldn't say that bombing the entire city was the plan, but I would say that arming every soldier with TNT definitely reduced the number of casualties on our end."

            "I tried my best to keep everyone safe, even if it meant lying. I can't let them down now."

            hide sprite KoeBase

            call interrogation_4

        "Rebuild society in my vision": #(+Villain, +Vis)
            $ Villain += 1
            $ Vision += 1
            n "Guwon was an experiment to see if we truly were capable of reshaping society."
            n "It was supposed to show the might of our nation's youth, that we were something bigger than everyone else said we were."
            n "The experiment failed."

            "I would have loved to see it spread past Guwon, but the opportunity never presented itself."

            show sprite KoeBase

            ka "Lethe had similar ideals. She thought that turning citizens against each other would weed out the weak."

            n "No. Lethe thought society was beyond saving and proved that one spark could bring it crumbling down, which is why you have a job today."
            n "I believe that people can coexist, we just need to modify a few rules."

            "Lethe was right, the system had become too polluted, but destroying the world isn't the answer."
            "If you try to kill a virus, it will come back stronger and nothing will change."
            "In order to take it down, you have to integrate into its life cycle and prevent it from reproducing."
            "I just tried to do so from the wrong angle. Next time, I won't be so sloppy."

            hide sprite KoeBase

            call interrogation_4

        "I don't know": #(+Hero, +Chr)
            $ Hero += 1
            $ Charm += 1
            n "....."

            show sprite CopBase

            cop "Mr. Tesuta, please answer the question."

            n "...I didn't. I mean, part of me thought it would never work... I just... did what I always did..."
            n "I never questioned why or what came next."

            hide sprite CopBase
            show sprite KoeBase

            ka "And what would that be?"

            n "Hunh? Oh… nothing. Nothing was planned after that… I just did what I was told."

            "I just wanted to make everyone happy."
            "I thought if we took down the city together, we'd get some kind of happily ever after."
            "That's just not how the world works. There is no 'after'."
            "Just now and everything that has since passed. I have to do what I can so that 'now' doesn't get me killed."

            hide sprite KoeBase

            call interrogation_4

    #[Return to Main Branch]
    label interrogation_4:

    show sprite KoeBase


    ka "And what exactly was your end goal in all of this?"

    n "Excuse me?"

    ka "Why did you attack Guwon in the first place? Such extreme actions had to come from somewhere."
    ka "It's not every day a middle school student attempts to destroy a city."

    n "Guwon had to be brought down!"

    ka "Why?"

    hide sprite KoeBase

    #[Player Choice]

    menu:
        "It was corrupt": #(+Hero)
            $ Hero += 1
            n "Guwon's entire economy was based around the manufacturing and propagation of Proficiencies."
            n "They treated us like livestock! We were paraded about as status symbols and meal tickets"
            n "No one cared what happened to us."

            show sprite KoeBase

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

            hide sprite KoeBase

            call interrogation_end

        "It was convenient": #(+Villain)
            $ Villain += 1
            n "Where else was I supposed to start? Guwon was my home."
            n "I had never been outside of my hometown and it was as good a place as any."

            show sprite KoeBase

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

            hide sprite KoeBase

            call interrogation_end

        "It was safest": #(+Villain)
            $ Villain += 1
            n "Guwon is water locked, it would be the easiest to fortify."
            n "With what Odori had planned, we couldn't just set up shop anywhere. It had to be someplace secure."

            show sprite KoeBase

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

            hide sprite KoeBase

            call interrogation_end
        "To end the war": #(+Hero)
            $ Hero += 1
            n "Everyone was fighting each other, not just us."
            n "This is just an isolated incident among many that happened during the battle between Lethe and the Karmic Gladiators."
            n "Even after she was gone, people were still fighting each other."
            n "I believe it's the entire reason your department exists, madam Vice President."

            show sprite KoeBase

            ka "Our department exists to regain peace, not to insight riots in the streets."

            n "Then why did it take our riots for you to turn your attention to Guwon?"
            n "It was home to a well-known weapons manufacturer at the time."
            n "Once we cut off their exports, suddenly you guys were able to regain control of the populace."

            ka "We needed to restore order. Doing so takes time and hard work."
            ka "We turned our attention to Guwon next due to the number of casualties, not because of any vigilante interference."

            "She spits out the words as if they're acid." 
            "It's clear I'm getting nowhere with this woman."

            n "Casualties were bound to happen, you're assuming our activities caused more."

            hide sprite KoeBase

    #[Return to Main Branch]

    # Error, if we run out of story, it leads us back here?
    label interrogation_end:

    show sprite KoeBase

    ka "I rest my case. It is clear that Nagen Tesuta is guilty of all crimes, and shows no remorse for what he has done."

    "Wait a minute, that's it!"

    n "Objection."

    hide sprite KoeBase
    show sprite CopBase

    cop "That's not how an interrogation works, Mr. Tesuta."

    n "S-sorry. It's just, wasn't the purpose of this case to determine whether or not the Junior Gladiators lead to people dying?"
    n "None of the prosecution's questions have been relevant to the charges at hand; they've been about my character."
    n "In fact, all of Ms. Amagi's questions were about proving that my group was malicious and dangerous to society."

    hide sprite CopBase
    show sprite KoeBase

    ka "This is outrageous and highly unprofessional."

    n "If this is indeed a trial to prove that my group committed atrocities in Guwon Province, then there is more than enough evidence to support the charges."
    n "However, it seems the prosecution wants to prove that my friends and I are, to put it plainly, evil."
    n "And for that, there is not enough evidence."

    "I already made a deal with the DVP to pardon my crimes in exchange for information on the location of the remaining Karmic Gladiators."
    "There's something else she's been trying to fish out of me, but I can't figure out what it could be."

    n "I want to change the terms of the deal."

    ka "You mean plea bargain?"

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


    hide sprite KoeBase
    show sprite CopBase

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

    hide sprite CopBase

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

    show sprite MMBase

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

    hide sprite MMBase

    #[Player Choice]

    menu:
        "New role?": #(+Chr)
            $ Charm += 1
            show sprite MMBase

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

            hide sprite MMBase

            call life_1

        "Where are we going?": #(+Int)
            $ Intel += 1
            show sprite MMBase

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

            hide sprite MMBase

            call life_1

    #[Return to Main Branch]
    label life_1:

    show sprite MMBase
    
    mm "I had to cash in an old favor to get us out of this mess."
    mm "I was hoping to leave his debt dangling over his head for a few more years, but this is more important."
    mm "You need a proper guardian and as much as I'd love to take care of you myself..."
    mm " I don't have a legal job, or house, or any of the tools that would let the state give me guardianship."

    n "I'm not a child."
    n "I appreciate everything you've done for me, but you'll have to forgive me for not fully trusting you or this other person."
    #^This line has a slight edit, previously said "your former target", changed to "this other person" to fit with both choices, feel free to change it ofc

    mm "I just want what's best for you. Please, just give this guy a chance."
    mm "I will be with you the whole time. He's... he's a bit of a potato, but he'll treat us well."

    n "...potato?"

    mm "Boring, acidic, lives somewhere dark and hard to find. A potato."

    n "...right..."
    n "Has anyone heard from Odori?"

    mm "No, I'm sorry."

    n "You sure it's not classified or something?"

    mm "If it was classified, I would have told you it's classified."

    "A month. She's been missing for over a month."
    "At this point, they're not looking for {i}her{/i} anymore, they're looking for a body."
    "My mouth's gone dry. I don't want to be here."
    "She should be in a limo on her way to a new home, not me."

    mm "Nagen honey, remember to breathe. We're not going to get out of the car until you're ready."

    #[BG: Manor Exterior]

    scene backgroundnhouse
    
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

    mm "Surprise!"

    hide sprite MMBase
    show sprite KenzoBase

    kan "What part of this arrangement involved you coming here?"

    n "I knew it! He wasn't expecting us at all!"

    hide sprite KenzoBase
    show sprite MMBase

    mm "Well, he was expecting you."

    hide sprite MMBase
    show sprite KenzoBase

    kan "...that's the kid?"

    hide sprite KenzoBase
    show sprite MMBase

    mm "He claims otherwise, but yes, this is him."
    mm "Don't worry, in this big ol' house, you'll hardly notice us."

    hide sprite MMBase
    show sprite KenzoBase

    kan "Us?"
    kan "You're the one who insisted on abandoning your old identity and with it, any connection to me."
    kan "You made that very clear."

    hide sprite KenzoBase
    show sprite MMBase

    mm "I'm not going to leave my kid in some strange place all by himself."

    n "I'm not you kid! And you're not a mom."

    mm "Of course I'm a mom."
    mm "We'll work out the details later."
    mm "I have a full day ahead of me dropping off the rest of the rugrat felons, but I'll be back before you know it."

    hide sprite MMBase
    show sprite KenzoBase

    kan "I agreed to claim to be taking care of the child."
    kan "You said nothing about living here."

    hide sprite KenzoBase
    show sprite MMBase

    mm "I feel like you're hearing me, but you're not understanding."
    mm "I am a new mom and we will talk about this later."
    mm "I'll see you soon, Nagen."

    hide sprite MMBase

    "What happened to not leaving me alone in a strange place?"
    "The man sighs and lets me in anyway."
    "Everything I own now fits inside my backpack, but I’m not sure where to put it."
    "He just stares at the closed door, potentially regretting his decision to let me in."

    #BG Interior

    menu:

        "Where am I staying?":

            show sprite KenzoBase

            kan "Here, apparently."

            n "...In the hallway?"

            kan "Second floor, east wing, third room on the left side."
            kan "It should have nothing terribly breakable in it."
            kan "Just don't touch anything outside of that room."

            n "...okay."

            "I go to leave, but he stops me."

            kan "She didn't mention there were... others."

            n "That's... kind of a long story."

            kan "Follow me, we need to talk."

            call prologue2

        "Who are you?":

            show sprite KenzoBase

            kan "I'm a software engineer."

            n "That's it?"
            n "I find it really hard to believe Maimai would obsessively pursue some software engineer."
        
            kan "...that was my own doing."
            kan "I made the mistake of confusing a dark-web serial killer with an ARG and tried to set a trap for her so to speak."

            n "You asked Maimai to target you on purpose!?"

            kan "In a way, yes. Though it's usually incredibly difficult to get her to show herself."
            kan "The question is, why is she risking that for you and your friends?"

            call prologue2

        "Why are you doing this?":

            show sprite KenzoBase

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

            call prologue2

label prologue2:

    "I follow him into a cluttered study"
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

    "The lingering winter nips at my cheeks as I watch the last of my things get packed into the cab."
    "A familiar feeling of helplessness washes over me."
    "There’s nothing else I can do."

    hide sprite KenzoBase
    show sprite MMBase

    mm "Hey, it’s going to be okay. Boarding school isn’t that bad."

    n "You don’t know that."

    mm "Excuse me mister, but I have been to my fair share of reform schools."

    n "Clearly they worked wonders."

    hide sprite MMBase
    show sprite KenzoBase

    kan "All the more reason not to be scared."
    kan "This is only to show the courts you can behave for a long period of time."

    n "...can’t I just stay here with you guys instead?"

    kan "I thought you hated being cooped up here."

    hide sprite KenzoBase
    show sprite MMBase

    "I do."
    "I do hate it, but at least I know what to expect when I’m here."

    mm "You can come back during the break and I’ll be going with you the first day to make sure the place is on the up and up."

    hide sprite MMBase
    show sprite KenzoBase

    kan "I assure you, it’s a legitimate establishment."
    kan "I wouldn’t send him off if I wasn’t familiar with the staff."

    "That’s supposed to make me feel better?"

    scene backgroundcar

    n "I hate this."

    mm "I know. Come on, the year will be over before you know it."

    hide sprite MMBase

    "She herds me into the car with a forced smile on her face."

    scene backgroundcarin

    "We drive a few hours to get to the school."
    "It’s one of the few buildings that survived the riots."

    scene backgroundschool

    "I heard it was a library donated to the DVP for renovation and now it’s become this."
    "I would have preferred the library."
    "It’s no surprise, really, that this is where they planned to test their stupid program."
    "What confuses me is that I’m expected to act like an ordinary student."
    "I mean, our names were never released to the public, so it could work."
    "Something just seems... off"

    scene backgroundhall1

    "Each classroom has a transparent door with an electronic display built-in."
    "It feels more like an observation tank than a classroom."

    show sprite MMBase

    mm "The building had been a library since the 1600s."
    mm "I never got to see the inside because the previous owner was such a nut job."

    n "That’s supposed to make me feel better?"

    mm "No, but do you think these bowties proofread every book in the building before bringing you in here?"
    mm "Who knows what you could find!"

    "I appreciate she’s trying to make this sound like an adventure, but it doesn’t change how... empty the school feels."
    "The second floor is for more specialized classes."
    "Along the west corridor are rooms for the fine arts and along the east is a giant computer lab."
    "Large bay windows look out to the central courtyard."
    "We finally arrive at a large mahogany office door."

    mm "This is it."
    mm "Promise you’ll be on your best behavior?"

    n "...why are you asking me that now?"

    "She searches for the right words to say."

    mm "I didn’t want you to spend your time at the mansion worrying about school."
    mm "This place is the safest place for you to be right now, even if it’s upsetting at times."
    mm "Until they grant me full guardianship, my hands are tied."

    n "...I promise I’ll try."

    "Maimai escorts me into the office."

    hide sprite MMBase
    # Principal office
    "A woman gestures for us to sit down. She takes her place behind a massive desk with a stack of forms for us to review."
    "The nameplate in front of her reads in gold letters 'Principal Vivaldi Tahani'"

    n "....."

    "Vivaldi Tahani, the chief officer sent to hunt down Lethe and her conspirators."
    "She was at the scene when Lethe... when she died."
    "I wouldn't have come if I knew she'd be here."
    "She's the last person I want to talk to."

    show sprite VBase

    v "Is something wrong?"

    "It's like she doesn't even care."

    hide sprite VBase
    show sprite MMBase

    mm "He’s just nervous because it’s a new school."
    mm "You know teenagers, all salty about change and stuff."

    "The principal is cold and composed, much like a statue."
    "I can’t help glaring at her. The DVP had handed me over to the woman who set up Lethe and sabotaged our siege of Guwon."
    "How could she be so indifferent? Doesn’t she recognize me at all?!"

    mm "So you’re the principal?"
    mm "That’s uh, quite a shift from being a police officer."

    hide sprite MMBase

    "I've never seen Maimai so nervous before."
    "Is she scared of this woman? Or just psychics in general?"
    "She hands us papers to sign, with Maimai trying to stay as far away from the woman's hands as possible."
    "My phone is confiscated and replaced with a cheap knock-off to use while on campus."

    show sprite VBase

    v  "Detective. I grew tired of locating criminals after they committed crimes."

    hide sprite VBase

    "Locating? Is that what she calls what she did? Locating criminals?"
    "Lethe was- She watched them kill her with that indifferent stare on live television."
    "We get up to leave. I can’t hold my tongue any longer."

    scene backgroundP3

    n "You ruined my life."

    mm "Nagen, please."

    n "No, because of her stupid feud, I lost both my mentor and my best friend in one night."
    n "Just because I have to be here doesn’t mean I have to play along with her revenge fantasy."

    v "This isn’t supposed to be a punishment, Mr. Tesuta. Your school life will be what you make of it."
    v "I trust you will do everything in your power to avoid ending up in my office again. Good day to you both."

    scene backgroundhall2

    "I practically get pushed out of the room by Maimai."
    "The wooden doors slam shut, but her hands never leave my shoulders."

    show sprite MMBase

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

    "We go back to the car to get the last of my things."
    "She wraps me in a huge hug and I become very aware of the car coming up to the roundabout."

    n "Maimai, please-"

    mm "Be safe. Call me if anything happens."
    mm "I want to hear from you at least once a week, mister."
    mm "I mean it. Don’t go forgetting about me, okay?"

    n "Okay, okay, people are staring."

    "I brush her off and collect my bags."

    n "I’ll miss you too."

    hide sprite MMBase

    "I really don’t want to go, but I can’t keep putting it off."
    "We say our final goodbyes and I watch as the car drives off. Tomorrow will be my first day of school."
    "I can see other kids unloading their luggage and milling about the grounds. Now would be a good chance to find my friends."

    scene backgroundschool

    show sprite NBase

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

                    hide sprite NBase

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
    g "But this will give you a baseline affinity of 0 with all students"

    # Else

label FindPeople:

scene backgroundschool

#If Friends = 3  show menu keep looking or go to meeting
if friend >= 3:
    menu:
        "Keep Looking Around":
            call FindPeople1
        "Start Meeting":
            jump Meeting
else:
        call FindPeople1

#else show menus
label FindPeople1:
    menu:
        "Lecture Hall":
            scene backgroundcharm

            $ friend += 1
        
            "I arrive at the room where the student council meets."
            "Everything looks too new, too clean, like no one has set foot in here since the school opened."
            "I stand for a while, admiring the leather office chair at the end of the table possibly meant for the student council president."
            "I would give anything to be in charge and shape the future of this school."
            "It may take a while, but I'm sure I can get there."

            show sprite HBase

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

            h "Yeah, I'm surprised they're letting us go to school together."
            h "My lawyer said they were going to separate us and we weren't allowed to see each other again. I wonder what changed?"

            menu:
                "Pretend to speculate":
                    $ Intel += 1

                    n "I don't know, maybe Uitto worked her magic and cried us into a lighter sentence."

                    h "We could do that? Shoot, if I'da knew, I woulda taken a lemon into the courtroom or something."
                    h "I mean, yeah I was kinda scared, but I totally coulda cried my way to freedom."

                    "He's as determined as ever."

                    n "I was thinking more along the lines of using her Proficiency. It was Diplomacy, remember?"

                    "He stares at me blankly."

                    n "She could talk people into doing things for her."

                    h "Right, she was a Charisma major at the time."
                    h "Oh! That reminds me."
                    h "There's been a rumor going around that you can change your Major, have you heard anything about that?"

                    n "No, I haven't."

                    h "Oh, that sucks. I was hoping you could explain it to me."
                    h "Something to do with how Proficiencies can apply to different Majors depending on how they're used."
                    h "But I just don't get injured easily. I don't see how that would make me smarter or more likable."

                    "That is odd, I'll have to look into that."

                    jump h_intro

                "Ask how he's doing":
                    $ Charm += 1
                    $ hRep += 1

                    n "Crazy, right? But it's good to see you. How have you been?"

                    h "I'm living in a group home right now. It's not too bad, a little cramped, but they were willing to take me."

                    n "That's kinda surprising."

                    h "Well, I mean, it's like a rehab center for troubled kids."
                    h "We have to go to classes, and therapy sessions, and they;ve got this little reward system and junk."
                    h "I had to work really hard just to be able to leave the building on my own."

                    n "Oh, well, I mean that's good to hear. Is it nice?"

                    h "I only have the bottom half of a bedroom door, and one of the other kids punched a hole in the wall last week."
                    h "But the grown-ups are nice, they give me plenty of space... But it's like a respect thing, not 'cause they're scared."

                    "Well that's good. He has a bad habit of lashing out if people get too close too suddenly."
                    "That thing about the kid punching the wall kinda concerns me though."

                    n "I'm glad that's working out for you."
                    n "My foster family's a little... strange. They live in this huge house, but they don't really take care of it."
                    n "It's like living in a museum. Lots of dusty old expensive things I'm not allowed to touch."

                    jump h_intro

                "Lawyers are dumb":
                    n "Why would they tell you that?"
                    n "It wasn't a standard case, it's not like he could flip through a handbook and find the standard punishment on taking over a city."
                    
                    h "Well, no, I guess not."

                    n "He was probably trying to scare you or something. That's so unethical..."
                    n "I think."
                    n "I'm not sure to be honest. See, this is why I chose to represent myself."

                    h "You shoulda been my lawyer instead, I'm sure you were awesome."

                    n "I hope so."

                    h "What do you mean? You're here, aren't you? That means you won, right?"

                    n "Something like that; I'm on probation. Do you think the others are here?"

                    h "I mean, it's possible. They had Proficiencies too... Maybe we could start our club back up!?"

                    menu:
                        "Maybe":
                            $ Hero += 1

                            n "As tempting as that sounds, it'd be best if we lay low for a while. At least wait and see how things pan out for us here."

                            h "What's bread got to do with this?"

                            "I must look like I'm about to clock him or something because he starts laughing like a mad man."

                            h "Dude, I;m just kidding, cool your jets."

                            n "You know how I feel about puns."

                            h "Yeah, yeah; look I can't make any promises, but I'll try."

                            n "To knock it off with the puns, or to keep out of trouble?"

                            h "Both."

                            jump h_intro

                        "No":
                            n "I don't know. I mean, we can't use the same group name, and it wouldn't feel right without Odori anyway."

                            h "Yeah, that's true."

                            "Odori was the one who brought us all together in the first place."
                            "The Liberation Front was her dream, and a part of it died with her."

                            h "Hey man, are you okay?"

                            jump h_intro
                        
                        "Yes":
                            $ Villain += 1

                            n "Shh, keep your voice down. We can't have the DVP finding out about this."

                            h "I gotcha. Well, let me know if anything changes. I got your back, man."

                            n "Oh, and Hiro?"

                            h "Hmm?"

                            n "This time we're doing things my way."

                            jump h_intro

            label h_intro:
            
            hide sprite HBase

            "I've spent way too long listening to what other people tell me to do."
            "Once I've finished scoping out the school, I'm breaking out the strategy board."
            "I should get going. There's still more of the school to see."

            call FindPeople

        "Field":
            scene backgroundfield

            "A few years ago, I probably wouldn't be anywhere near here. Maybe this year will be different."
            "In the corner of my eye, I see a girl in black spandex bound over, a pile of papers in her hands."

            show sprite Marikobase

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

                            jump m_intro

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

                            jump m_intro

                        "Uninterested":
                            $ Intelligence += 1

                            n "I never really had a lot of free time back then."

                            "Between Odori's hero club and my dad's endless examinations, I didn't have a lot of time for anything."
                            "I was constantly underslept to the point that anything involving standing seemed taxing."

                            m "Right, I don't suppose your mind has changed all of a sudden either?"

                            n "Not especially, no."

                            "She breathes a huge sigh of relief. Still a little anxious, but no longer petrified."

                            m "Then I'll be on my way. Byeee!"

                            "She immediately turns around and leaves. I doubt she'll be coming my way anytime soon."

                            jump m_intro

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

                    jump m_intro
            
            label m_intro:

            "I should look around some more."

            call FindPeople

        "Hallway":
            scene backgroundhall1

            "The grounds of this school are a lot larger than I anticipated."
            "I'll need at least an hour before classes start in order to figure out where I'm going."
            "I wander into a back hallway on the second floor."
            "I assume all of the art classes will be taking place based on the glass display cases."
            "With all the classrooms locked, there isn't much to see right now."
            "Though I don't seem to be the only person wandering around campus right now."
            "He has a beaten-up piece of paper in his hand and seems lost."
            "When he looks up at me, I feel a chill run down my spine."

            #[Show Yoku sprite]

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
                    $ yRep -= 1

                    n "Just looking for where my new classes are going to be. And talking to you, I guess."

                    y "...you can't be serious."

                    n "What?"

                    y "I thought this was supposed to be a school for the e-e-elite, not a co-common murderer."

                    n "First of all; common!? I know having a good memory isn't the most exciting Proficiency, but it's better than your Music Man."
                    n "Secondly, being involved in the Guwon Riots has nothing to do with how capable I am as a student."
                    n "The definition of 'elite' here is slightly above average, don't delude yourself."

                    y "So defensive over your Pr-proficiency, yet you're going to g-ggloss over the murderer comment?"

                    n "....."

                    "Okay, so I'm a little self-conscious about my so-called 'powers'."
                    "But it isn't like I think being able to remember everything is pointless or lame, it's served me fairly well."
                    "The thing is, my Proficiency is artificial."
                    "Unlike child prodigies like Yoku, my father had to spend every waking moment forcing my brain to process memories the way it does."

                    y "Hh-ow long are you going to keep staring into space?"

                    n "Sorry, that happens sometimes."

                    y "As much as I'd like to continue this ffffascinating discussion, I have business eh-elsewhere."
                    y "Until next time."

                    jump y_intro

                "I'm lost":
                    $ yRep += 1

                    y "...obviously."

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

                            jump y_intro

                        "What are you doing here?":
                            $ Intelligence += 1

                            y "I was looking for the auditorium, I he-heard that this school was going to provide a Wurlitzer."
                            y "As the future's leading co-com-composer, I'd like to find it."

                            n "A Wurlitzer?"

                            y "Like a giant music box, an orchestra without... people."

                            "I've never seen someone so disgusted at the mention of other human beings. And I thought I was antisocial, dang."

                            n "What do you need a Wurlitzer for?"

                            y "I've composed for a number of high scale events, but it's been a while since I've had a steady stream of clientele."
                            y "Making everything on my own will expedite the progress."

                            jump y_intro

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

                            jump y_intro

            label y_intro:

            "He didn't seem to have that much to say to me. That's fine, I'm not here to make new friends."
            "The sooner I can find a way out of here, the better." 

            call FindPeople

        "Courtyard":
            scene backgroundcourtyard

            "I decide to check the back of the school."
            "Sun pours down into the center of the courtyard. It should feel warm and inviting."
            "Devoid of any activity, it's unsettling. I feel like I shouldn't be here."
            "I'm not alone, though. In the corner of my eye, I see a girl with a brilliant stream of scarlet hair."
            "She's looking out towards the sky with a forlorn grimace."

            n "Hey... uh, come here often?"

            u "No way, Nagen!?"

            "Her voice is definitely familiar. She turns on me with a wicked grin."

            show sprite UBase

            u "Did you seriously just hit on me? Good god, man, keep it together. You've been here, what, one day?"

            "Oh no."

            n "Uitto, I didn't realize it was you!"

            u "That's supposed to make me feel better?"

            n "No. I mean kinda. I wasn't even flirting, I just-"

            u "Stop, stop. You're just digging yourself deeper, short stack."

            n "I'm not that short!"

            u "Still shorter than me."

            n "You're in heels!"

            u "I'm 5' 7” without them."

            n "....."

            u "That's what I thought."

            n "You're evil."

            u "Only when I want to be."

            "I'll be honest, out of everyone, I'm not surprised she made it."
            "When we were kids, they used to call her 'The Closer'."
            "She could talk her way into and out of any situation and was a headliner in the pageant circuit."
            "It's not surprising she's taller than me either, just disappointing."
            "I had hoped to be taller than at least one of my friends."

            u "Oh quit pouting. Size isn't everything, y'know."

            n "Knock it off, wench."

            u "Oooh, 'wench', going old English on me are we? What's next, 'harlot' or hauling myself to a nunnery?"

            n "Don't tempt me."

            u "With a sharp tongue like that, I'm surprised you're here."
            
            n "Really? You were worried about me?"

            u "I'm serious, between the three of you, you're the last person I expected to see on the outside."
            u "Jona's an idiot and Hiro's basically harmless, but you?"
            u "You're smart and you're really bad about pretending to be nice."

            n "Yeah, well, so are you."

            u "Yes, but I'm a poor defenseless girly that was bossed around by a scary guy with piercings and torn up pants."

            n "You're hideously manipulative. Is that really the story you went with?"

            u "Story? It's the truth."
            u "You're the one that pitched a fit over not being leader, you should be flattered I gave you credit."
            u "Unless you told them something else..."

            menu:
                "I missed you":
                    $ uRep += 1

                    u "Ugh, don't be gross."

                    n "I'm serious! I thought I'd never see you again."

                    u "Yeah, me too..."
                    u "Listen, if anything I said got you in trouble, I'm sorry."
                    u "I was just trying to think of what you guys would probably say and stick with the most common stuff."
                    u "Well, you and Hiro. I figured you both would probably lie to protect the other."

                    n "So you lied to protect us?"

                    u "And Jona would just lie to lie. All of us were doomed, it was just a matter of damage control."

                    n "Well that's a defeatist attitude."

                    u "Yeah, being defeated tends to do that to a person."

                    jump u_intro

                "It doesn't matter":
                    $ uRep -= 1

                    n "We're all here now, so why does it matter?"

                    u "All of us?"

                    n "Yeah; you, me, Hiro, and Jona."

                    u "That's not... How do you know they're here?"

                    n "Didn't they tell you?"

                    u "They? Please tell me this is one of your paranoid delusions."

                    n "No, the DVP's Secretary of BS told me during her dumb monologue."
                    
                    u "....."

                    n "Didn't she talk to you?"

                    u "....."

                    jump u_intro

                "Of course I did":
                    $ Charm += 1

                    n "You were not a defenseless girly that was bossed around by a scary dude with awesome piercings."
                    n "And these are my favorite jeans!"

                    u "You're right! Who'd believe you?"

                    n "Nah, I went with the silent, brooding approach. The less you say, the better."

                    u "You're joking, right? Brooding definitely, but silent?"

                    n "Hey, I'm hella stoic."

                    u "Nagen, your oversharing's one evil laugh away from a cartoon monologue. I mean, seriously, you need help. No offense."

                    n "You wound me. My fragile ego can not handle an ounce of criticism."
                    n "End your vicious slander or I shall end you. Muahahaha."

                    u "I wilt not be-est tamed or commanded, foul villain. I wilt doeth what I wanteth."

                    jump u_intro

            label u_intro:
            
            n "We'll be meeting in the office room on the third floor."

            u "We?"

            n "I'm looking for the others right now. We're going to talk about our next move."

            u "Nagen, what are you talking about? We shouldn't be doing anything right now."
            u "You know what's on the line."

            n "Uitto, you gotta trust me on this, I know what I'm doing."

            #[Vision Branch]

            n "Well, yeah... Uitto, is something wrong?"

            u "How did you know where to find me?"

            n "Well, I didn't know you were here. I've just been kinda wandering around." 
            n "We're meeting in 313 by four at the latest. Make sure you're there."

            u "...yeah... whatever you say."

            #[Return to Main Branch]

            hide sprite UBase

            "There are still other places to look at. I should go."

            call FindPeople

        "Stage":
            #[BG: Theater]

            "I'm honestly surprised they bothered to build this when there was a functional amphitheater on the grounds."
            "There's only enough seating for twenty to thirty people, but the walls are decorated to create the illusion of a vast balcony."
            "At least they didn't fill the fake seats with human silhouettes."
            "The stage itself is polished and well lit. It has more than enough space for rehearsals."

            show sprite KBase

            k "Isn't it beautiful?"
            k "I was so worried when they picked this place that they'd shove us into a dingy room and call it 'rehearsal' space."

            n "It's a little small, don't you think?"

            k "Compared to the pathetic platform most bars offer, this is an opera house."
            k "There's even changing stalls! We'll be able to do great things with it."

            n "We?"

            k "Aren't you a fellow performer? You're all dressed up and studying the stage."
            k "What else am I supposed to think; that you're just some Intelligence Major?"

            n "I {i}am{/i} an Intelligence Major."

            k "Oh..."

            n "Nagen Tesuta, proficient in memorization, can't get more common than that."

            k "N-nagen!? I- Oh my goodness, I didn't know it was you."
            k "I'm so sorry, you must think I'm a monster."

            "No harm was done, but it would be fun to mess with her a bit."

            n "It's okay. Since we're going with blind assumptions, I'm guessing Charisma Major?"

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

                    jump k_intro

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

                    k "...is that your backwards way of complimenting me?"

                    n "I can forwards compliment you too if you want. You're just so fun to mess with, it's hard not to."

                    k "Fun? After you've seen one of my performances, you may compliment me."
                    k "O-otherwise it would just feel like empty pandering."

                    "Says the person who was fishing for compliments five minutes ago."

                    jump k_intro

                "And your Proficiency is...":
                    $ Vigor += 1

                    k "I specialize in vocal manipulation. My range is A0 to C8 in relation to a piano."
                    k "No other singer can compare to me without the use of technology."

                    n "That doesn't sound like a Charm Proficiency."

                    k "Because it's not."
                    k "Not every Vigor Major you meet is going to be some meathead jock."
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

                    jump k_intro

            label k_intro:
            
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

            hide sprite KBase

            "She blows me a kiss and runs off before I can finish objecting."

            call FindPeople
        
        "AV Room":
            #[BG: AV Room]

            "I stumble across a dingy room tucked in the back of the second floor."
            "The furniture here is considerably older than the classrooms and in worse condition."
            "If it wasn't for a small, glass-paneled recording booth, I would have assumed this room was for storage."
            "Through the windows, I can see purple egg crate walls lined with foam."
            "A mic dangles from the booth's ceiling, hooked up to three different computers."
            "I try to go inside, but the door is locked."

            #[Show Kazz Sprite]

            kk "What are you doing here? No one's supposed to be here, bromigo."

            n "You're here, aren't you?"

            kk "I asked if I could check out the recording booth before I finished setting up in my room."
            kk "I guess there are rules against soundproofing the dorms."
            kk "I'll be so bummed if the quality of my content worsens 'cause of cheap equipment."

            n "What does that have to do with me being here?"

            kk "If something breaks or goes missing, I'll be the first person they blame."
            kk "I didn't mean to offend you, but my faith in humanity took a bummer turn by at least 46% this year."
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

            n "...yeah."

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
                    kk "Busy work like that is just fluff that diversifies the grad points so one bad exam doesn't force you to repeat a grade."
                    kk "I did fine on exams, the assignments were a waste of everyone's time."
                    kk "I gave my homework to a willing volunteer and just copied their work in my handwriting."
                    kk "But apparently, that wasn't a 'real' problem."

                    n "To be fair, that doesn't seem like a transferable occurrence."
                    n "Not everyone in my class cheated on tests or had bad grades."

                    kk "I guess that's true, but it seemed logical at the time."
                    kk "Dyre was an argumentative shit-head, all the teachers hated him, but they couldn't get rid of him because of his grades."
                    kk "Still, I hope this place won't be boring. The least they could do after busing us here is to make it interesting."

                    jump kk_intro

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

                    jump kk_intro

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

                    jump kk_intro

            label kk_intro:
            
            kk "It's so trippy though, 91% of the people I've met here used to go to Estella."
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
            
            #[Hide sprite]

            "He still looks worried, but I'm already out the door."

            call FindPeople

        "Nurse's Office":
            scene backgroundnurse

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
            show sprite MuBase
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

            "That's something I can sympathize with as a fellow Intelligence Major. When they ran out of things to teach you, they'd give you busy work."
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

                    n "...why'd a girl ask you that?"

                    mu "I. Don't. Know."
                    mu "People hear my Proficiency and think it's permission to ask and show me all the gross things they're too scared to talk to an actual doctor about."

                    n "Oh."

                    mu "People will ask me weird stuff no matter what I do."
                    mu "At least this way it's less people and I won't have to read essays."

                    jump mu_intro

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

                    jump mu_intro
                
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

                    jump mu_intro

            label mu_intro:

            mu "Why did you come here anyway? Have any allergies or scripts the nurse needs?"

            n "No. Just figuring out where everything is."
            n "If they make us participate in P.E., I'll end up here eventually."
            n "I have a strange knack for getting hit in the face with sports equipment."

            mu "Wait, no way. Were you the kid that got a bloody nose from a sprout ball?"

            n "They're harder than they look."

            mu "They're made of yarn, man, it doesn't get cushier than that man."
            mu "I thought Dyre was exaggerating all those times. That's too rich."

            "I don't think he's going to stop laughing any time soon."

            n "Well, now I know where the nurse is supposed to be. I'll be going now."

            mu "Hey, hey; watch out for flying pompoms. Wouldn't want you to have to check in on your first day."

            n "Hilarious."

            "nfortunately, I've been injured by less threatening objects."
            "What he said in jest could very well happen if I run into the wrong cheerleader."

            hide sprite MuBase

            call FindPeople

        "Next":
            call FindPeople2

label FindPeople2:
    menu:
        "Back":
            call FindPeople1
        "Pond":
            pass
        "Roof":
            pass
        "Library":
            pass
        "Studio":
            pass
        "Gym":
            pass
        "Cafe":
            pass
        "Next":
            call FindPeople3

label FindPeople3:
    menu:
        "Back":
            call FindPeople2
        "Lab":
            pass
        "Classroom":
            pass
        "Stuco Room":
            pass
        "Forbidden Door":
            pass
        "Ampitheater":
            pass

label Meeting:
    pass