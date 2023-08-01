# Students
define n = Character("Nagen Tesuta")
define u = Character("Uitto Hanatabe")
define j = Character("Jona Oshima")
define h = Character("Hiro Manuke")
define nk = Character("Nanase Keisan")
define r = Character("Rise Kisaki")
define m = Character("Mariko Genki")
define k = Character("Kitsune")
define kk = Character("Kazz Kataki")
define d = Character("Dyre Okami")
define a = Character("Apex")
define o = Character("Odori Hato")
define mh = Character("Momoko Heiwei")
define y = Character("Yoku Teki")
define mu = Character("Murakami ")
define i = Character("Ichita")
define t = Character("Taiga Sakurai")
define ch = Character("Chisei Jikoma")
define s = Character("Setsuna Hori")
define sh = Character("Shoma Nishimoto")
define ki = Character("Kietsu")
define re = Character("Rei Watabe")

# Teachers
define v = Character("Vivaldi Thani")
define ya = Character("Yaguchi")
define sa = Character("Sato")
define ik = Character("Inukai")

# Extras
define cop = Character("Cop")
define ka = Character("Koe Amagi")
define mm = Character("Mai Mai")
define kan = Character("Kenzo Ando")
define l = Character("Lethe")

# Used for player instructions
define g = Character("Game")

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
    $ uRep = 0

    # Character Flags
    $ uTurn = 0
return

# THE GAME STARTS HERE!
label start:

    call variables
    menu:
        "Prologue":
            pass
        "Sandbox":
            jump sandbox

# Opening video goes here.

label prologue:

#background Interrogation Room

"My whole life, I feel like I've been dragged around by my collar."
"I guess when most adults see a kid act out of line, they're overwhelmed with a need to control the situation."
"Funny, seeing as that's the very thing I've been fighting for: a chance to be in control of my life."

cop "Please state your name and registered Proficiency."

n "My name is Nagen Tesuta."
n "I possess an Intelligence Proficiency."
n "Anything I see, hear, or experience is recorded in perfect detail."

"I tap the side of my head."
"Having a great memory doesn't really make me smarter than anyone else, but the ability falls under the Intelligence Major."
"People are just so determined to classify things so they can feel important, they stop asking whether it's worth the effort."
"I mean, some people can go their whole lives without realizing they have a Proficiency."
"It's nothing special. The only reason I know about mine is because I was groomed to have it."

cop "Look, you and I both know it's not looking good for you."
cop "I mean, you've heard the charges: premeditated murder, inciting a riot, mayhem, and menticide."
cop "These are all with a registered Proficiency which will add twenty-five more years to your sentence."
cop "Don't even get me started on the use of deadly weapons."

ka "There's more than enough evidence to try you and your cohorts as adults."
ka "In the case of The Supreme Court vs. Lethe, vigilantism was determined to be a Class One felony."
ka "Some of her sympathizers, like you, seem to think they are above the law."
ka "If we were able to find her remaining supporters, it would be an excellent demonstration of goodwill."
ka "We all remember-"

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

#[BG: Interrogation Room]

"But that was the me of two years ago, the kid who grew up in a glass box waiting for my veins to stop burning."
"The unwilling test subject of the very people who stand before me claiming I'm the monster."
"Back before the Department of Villain Prevention was a governing body under Estella's control."

n "I know you. You were the prosecutor during Lethe's trial."
n "Trying to extort information out of a child for your old department? That's surprisingly underhanded of you."

ka "Then you understand what you're up against."
ka "Choosing to represent yourself in court only gave you a fool for a client."

"She's the prosecutor for my case!?"

ka "I'm just doing my job, Mr. Tesuta, in ensuring I have all the information I need for my case."

cop "Just make this easier on yourself and fold. It'll be better than what your friends are going through."

#[Player Choice]

#[A. Confess everything (-Hiro)]

n "Yeah, I did it, everything you said is true."
n "I helped start the riots to take down Estella and her talent mills."
n "You want the names of all the adults that worked with her, right?"
n "Fine. Just don't throw the book at me."
n "We both know this is shady as hell."
n "I'll parrot any garbage you want me to say after I get my sentence."

#[Fast forward past all other player choice options in this scene. All points will be put in Intelligence]

#[B. Refuse]

#[Return to Main Branch]

n "Good cop, bad cop? Really?"
n "I'm sorry, it's going to take more than a movie cliché to get me to tell anyone anything."
n "Also, I was never read my rights, so unless you want a mistrial, I suggest you start treating me like an adult before trying me like one."

cop "That's not how the system works, kid."

ka "No, he has a valid point. You want to be talked to like an adult? Fine."
ka "Mr. Tesuta, if you don't give us the information we need, there will be no 'deal'."
ka "The first step is pleading guilty in court. There is no workaround."

"So it's her way or no way, hunh? Fine, whatever, she has her reasons; I have mine."

#[Player Choice]

#[A. I have to protect my teammates (+Hero, +Vis)]

n "I'll plead guilty in court, but I and I alone am guilty of these charges."
n "I cannot say the same of my friends; they genuinely believed in what Lethe told them..."

"If I lie, I could be held in contempt of the court, but if I play the 'scapegoat', maybe they can get out of here unscathed."
"Either way, someone has to answer for what we did."

#[B. I don't have a choice (+Villain, +Vig)]

n "Under the advice of my legal counsel, I will."

"Maimai would be heartbroken if I got locked away. She's been through this before."
"I practically have a walkthrough written on my sleeve."

cop "Do you believe you are guilty of these crimes?"

n "....."

"I've talked too much already. Isn't the confession enough?"

#[C. It's all part of the plan (+Int)]

n "I'll cooperate."

"It's too dangerous to make a move now. Best to play along for now."

#[D. I need to lighten my sentence (+Chr)]

n "...okay..."

"I hang my head at a 30-degree angle and feign the slightest tremor in my shoulders."
"The more sympathy I can gain, the better."
"No one will want to hear my side of the story if I act like the violent criminal they think I am."

#[Return to Main Branch]

n "I fully understood the ramifications of my actions and stand at the mercy of the court."
n "I aided in the brainwashing of my classmates and tried to conquer the Guwon Province for my own benefit."

cop "That's all we need to hear."

ka "Not quite. I still have a few questions for Mr. Tesuta."
ka "The Junior Gladiators started as a club at your school, later to fall down a path of destruction."
ka "And yet, no one can tell us whose fault this was."
ka "In your estimation, who was the leader during the attack?"

#[Player Choice]

#[A. The one who told us to kill (+Chr)]

n "Lethe was. She wanted to create a group of youth vigilantes to gain back public support."
n "It wasn't until after she died that we realized she was the one who started the chaos."

"Chaos is putting it lightly."
"She tried to get people to lynch anyone who was above average at... well... anything."
"It nearly destroyed the nation."
"Of course, if you really look at it, she wasn't wrong."
"Proficiencies were dangerous to the general public, but so is a pen if you use it right."
"These people, however, just want to confirm what they already believe, so I'll just tell them what they want to hear."

#[B. The one who gathered the army (+Hero, +Vig)]

n "Hiro Morine was our leader. He insisted on it constantly."
n "If it wasn't for him, we wouldn't have gathered nearly as much support."

"He wasn't a very good leader after that..."
"Actually, I was the one who did all the real work, but he meant well."
"He was the first one of us to get captured by these hypocrites."
"Even after getting dragged down, he insisted on taking credit for what happened. I hope he's okay."

#[C. The one who planned the attack (+Int)]

n "I was. I deliberately withheld information from my peers, knowing it would sway their decision to stay."
n "In the end, I was the only one standing."

"Well, not exactly standing. Let's just say, I don't handle failure very well."
"I was lucky Maimai was crazy enough to spare my life."
"If I manage to get out of this, I should thank her properly."

#[D. The club president (+Vis)]

n "Odori Hato was our leader. She's the one who brought Lethe's attention to our club."
n "Odori just wanted to help us and a cheesy superhero club was her answer."

"After Lethe died, she insisted we continue with our plans so that everyone would be happy again."
"It's amazing how far out of hand things got."

cop "Do you know where Ms. Hato is?"

n "No, she's not with us anymore."

"I want to believe she's still out there, but…"

#[Return to Main Branch]

ka "You were apprehended by Vivaldi Thani before you were able to carry out your plan to completion, correct?"

n "Yes."

ka "What did you intend to do once you took over the city?"

#[Player Choice]

#[A. Fortify the city against my enemies (+Villain, +Vig)]

n "I just wanted a place where I could feel safe. Anyone there was free to leave, but they chose to stay."
n "They took up arms, and I had to defend myself."

ka "According to eyewitness testimonies, you sought out innocent civilians who were in hiding and killed them on sight."
ka "We found seventeen assault rifles in your room. Were these also for your defense?"

n "Yes."

"It's not like I bought the guns online or anything. Guwon was already a dangerous place to live."
"If you were alone on the street for over twelve hours, you could get killed or worse."
"Wandering around the city with a gun was safer than going back home anyway."
"I had all kinds of other machines I was playing with that I got from the junkyard, but that's not what they care about."

ka "Did you use any of these guns against another person?"

n "Yes."

#[B. Rebuild the city (+Hero, +Int)]

n "Before making any plans, I would have had to reverse the damage that had been done."
n "I was in command of over five hundred people; they needed a place to live once the dust settled."

ka "That's all?"

n "Well, we would have needed a hospital next as well as to secure some kind of agricultural production to feed everyone."
n "That alone would have taken months, and who knows what other problems may have arisen."

"What can I say, I read way too many doomsday zombie comics as a kid."
"If I wanted to be a good leader, I had to make sure my people were provided for."

ka "This would be the same city you planned to bomb, correct?"

n "I wouldn't say that bombing the entire city was the plan, but I would say that arming every soldier with TNT definitely reduced the number of casualties on our end."

"I tried my best to keep everyone safe, even if it meant lying. I can't let them down now."

#[C. Rebuild society in my vision (+Villain, +Vis)]

n "Guwon was an experiment to see if we truly were capable of reshaping society."
n "It was supposed to show the might of our nation's youth, that we were something bigger than everyone else said we were."
n "The experiment failed."

"I would have loved to see it spread past Guwon, but the opportunity never presented itself."

ka "Lethe had similar ideals. She thought that turning citizens against each other would weed out the weak."

n "No. Lethe thought society was beyond saving and proved that one spark could bring it crumbling down, which is why you have a job today."
n "I believe that people can coexist, we just need to modify a few rules."

"Lethe was right, the system had become too polluted, but destroying the world isn't the answer."
"If you try to kill a virus, it will come back stronger and nothing will change."
"In order to take it down, you have to integrate into its life cycle and prevent it from reproducing."
"I just tried to do so from the wrong angle. Next time, I won't be so sloppy."

#[D. I don't know (+Hero, +Chr)]

n "....."

cop "Mr. Tesuta, please answer the question."

n "...I didn't. I mean, part of me thought it would never work... I just... did what I always did..."
n "I never questioned why or what came next."

ka "And what would that be?"

n "Hunh? Oh… nothing. Nothing was planned after that… I just did what I was told."

"I just wanted to make everyone happy."
"I thought if we took down the city together, we'd get some kind of happily ever after."
"That's just not how the world works. There is no 'after'."
"Just now and everything that has since passed. I have to do what I can so that 'now' doesn't get me killed."

#[Return to Main Branch]

ka "And what exactly was your end goal in all of this?"

n "Excuse me?"

ka "Why did you attack Guwon in the first place? Such extreme actions had to come from somewhere."
ka "It's not every day a middle school student attempts to destroy a city."

n "Guwon had to be brought down!"

ka "Why?"

#[Player Choice]

#[A. It was corrupt (+Hero)]

n "Guwon's entire economy was based around the manufacturing and propagation of Proficiencies."
n "They treated us like livestock! We were paraded about as status symbols and meal tickets"
n "No one cared what happened to us."

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

#[B. It was convenient (+Villain)]

n "Where else was I supposed to start? Guwon was my home."
n "I had never been outside of my hometown and it was as good a place as any."

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

#[C. It was safest (+Villain)]

n "Guwon is water locked, it would be the easiest to fortify."
n "With what Odori had planned, we couldn't just set up shop anywhere. It had to be someplace secure."

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

#[D. To end the war (+Hero)]

n "Everyone was fighting each other, not just us."
n "This is just an isolated incident among many that happened during the battle between Lethe and the Karmic Gladiators."
n "Even after she was gone, people were still fighting each other."
n "I believe it's the entire reason your department exists, madam Vice President."

ka "Our department exists to regain peace, not to insight riots in the streets."

n "Then why did it take our riots for you to turn your attention to Guwon?"
n "It was home to a well-known weapons manufacturer at the time."
n "Once we cut off their exports, suddenly you guys were able to regain control of the populace."

ka "We needed to restore order. Doing so takes time and hard work."
ka "We turned our attention to Guwon next due to the number of casualties, not because of any vigilante interference."

"She spits out the words as if they're acid." 
"I's clear I'm getting nowhere with this woman."

n "Casualties were bound to happen, you're assuming our activities caused more."

#[Return to Main Branch]

ka "I rest my case. It is clear that Nagen Tesuta is guilty of all crimes, and shows no remorse for what he has done."

"Wait a minute, that's it!"

n "Objection."

cop "That's not how an interrogation works, Mr. Tesuta."

n "S-sorry. It's just, wasn't the purpose of this case to determine whether or not the Junior Gladiators lead to people dying?"
n "None of the prosecution's questions have been relevant to the charges at hand; they've been about my character."
n "In fact, all of Ms. Amagi's questions were about proving that my group was malicious and dangerous to society."

ka "This is outrageous and highly unprofessional."

n "If this is indeed a trial to prove that my group committed atrocities in Guwon Province, then there is more than enough evidence to support the charges."
n "However, it seems the prosecution wants to prove that my friends and I are, to put it plainly, evil."
n "And for that, there is not enough evidence."
