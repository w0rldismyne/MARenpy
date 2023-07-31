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
"She was everyone's hero, especially mine…"

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
