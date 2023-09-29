# Students
define a = Character("Apex")
define ch = Character("Chisei Jikoma")
define d = Character("Dyre Okami")
define h = Character("Hiro Manuke")
define i = Character("Ichita Kinoshita")
define j = Character("Jona Oshima")
define k = Character("Kitsune")
define kk = Character("Kazz Kataki")
define ki = Character("Kietsu")
define m = Character("Mariko Genki")
define mh = Character("Momoko Yoshino")
define mu = Character("Oshin Murakami")
define n = Character("Nagen Tesuta")
define nk = Character("Nanase Keisan")
define o = Character("Odori Hato")
define r = Character("Rise Kisaki")
define re = Character("Rei Watabe")
define s = Character("Setsuna Hori")
define sh = Character("Shoma Nishimoto")
define t = Character("Taiga Sakurai")
define y = Character("Yoku Teki")
define u = Character("Uitto Hanatabe")
# Teachers
define ik = Character("Inukai")
define sa = Character("Sato")
define v = Character("Vivaldi Thani")
define ya = Character("Yaguchi")

# Extras
define cop = Character("Cop")
define Dark = Character("Nagen Tesuta")
define e = Character("Estella")
define Everyone = Character("Everyone")
define Hiyoko = Character("Hiyoko")
define ka = Character("Koe Amagi")
define kan = Character("Kenzo Ando")
define Kanon = Character("Kanon")
define Kiki = Character("Kiki")
define l = Character("Lethe")
define mm = Character("Mai Mai")
define Nurse = Character("School Nurse")
define PA = Character("PA")
define q = Character ("???")
define Ty = Character("Ty")

# Used for player instructions
define g = Character("Game")

#backgrounds
image backgroundpolice = "Backgrounds/PoliceRoom.png"
image backgroundblack = "Backgrounds/black.png"
image backgroundamp = "Backgrounds/ampetheater.jpg"
image backgroundbad = "Backgrounds/badforrest.png"
image backgroundcafex = "Backgrounds/cafeexterior.jpg"
image backgroundcafe = "Backgrounds/cafeint.jpg"
image backgroundcar = "Backgrounds/Car.jpg"
image backgroundcarin = "Backgrounds/CarInt.jpg"
image backgroundcharm = "Backgrounds/CharmClass.png"
image backgroundclass = "Backgrounds/class.jpeg"
image backgroundcourtyard = "Backgrounds/Courtyard.png"
image backgrounddorm = "Backgrounds/Dorms.jpeg"
image backgroundfield = "Backgrounds/Field.png"
image backgroundclearing = "Backgrounds/ForestClearing.png"
image backgroundhall1 = "Backgrounds/hallway1.jpeg"
image backgroundhall2 = "Backgrounds/hallway2.jpeg"
image backgroundlake = "Backgrounds/Lake.png"
image backgroundlibrary = "Backgrounds/Library.png"
image backgroundmariko = "Backgrounds/MarikoStage.png"
image backgroundroom = "Backgrounds/NagensRoom.png"
image backgroundnhouse = "Backgrounds/nagenhouse.jpg"
image backgroundnurse = "Backgrounds/NursesOffice.png"
image backgroundpond = "Backgrounds/Pond.jpg"
image backgroundroof = "Background/roof.jpg"
image backgroundhide = "Background/RoofHideout.png"
image backgroundparty = "Background/roofparty.jpg"
image backgroundschool = "Background/School.png"
image backgroundlab = "Background/science.jpg"
image backgroundsew = "Background/sew.jpg"
image backgroundstage = "Background/stage.png"
image backgroundstuco = "Backgrounds/stuco.png"

#Sprites

#Koe
image sprite KoeBase = "Sprites/KoeSprites/koe1.png"
#Cop
image sprite CopBase = "Sprites/Cop/cop1.png"
#Maimai
image sprite MMBase = "Sprites/MaiMai/MMBase.png"
#Apex
image sprite ABase = "Sprites/Apex/Apexspritebase.png"
image sprite ASad = "Sprites/Apex/Apexspritesad.png"
#Chisei
image sprite ChBase = "Sprites/Chisei/Chiseibase.png"
#Ichita
image sprite IBase = "Sprites/Ichita/ichitabase.png"
#Kenzo
image sprite KanBase = "Sprties/Kenzo/kenzoSprite.png"
#Kitsune
image sprite KBase = "Sprites/Kitsune/KitsuneN.png"
#Mariko
image sprite MBase = "Sprites/Mariko/Marikobase.png"
#Momoko
image sprite MhBase = "Sprites/Momoko/momokobase.png"
#Mu
image sprite MuBase = "Sprites/Mu/Mu1.png"
#Rei
image sprite ReBase = "Sprites/Rei/Rei.png"
#Setsuna
image sprite SBase = "Sprites/Setsuna/setsunabase.png"
#Shoma
image sprite ShBase = "Sprites/Shoma/ShomaN.png"

#Teachers
#Sato
image sprite SaBase = "Sprites/Fox/basespritesox.png"
#Vivaldi
image sprite VBase = "Sprites/Vivaldi/ViBase.png"

label variables:
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
return

# THE GAME STARTS HERE!
label start:

    call variables
    menu:
        "Chapter 1":
            jump chapter_one
        "Prologue":
            pass
        "Sandbox":
            jump sandbox

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

    "*It's not like I really have a choice anyway.*"

    cop "Then it's settled. A follow-up hearing will be scheduled in one year to document your progress."
    cop "In the meantime, you will be appointed a guardian from the DVP to take care of you during your time in the program."

    "Unbelievable. Fucking unbelievable."
    "I thought for once I could outsmart these assholes and get out of all this. No, this is not over."
    "A year is a long time. I'm sure I will be able to think of something."

    cop "Your guardian is waiting."

    hide spirte CopBase

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