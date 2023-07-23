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
define mh = Character("Momoko Heiwei")
define y = Character("Yoku Teki")
define mu = Character("Murakami ")
define i = Character("Ichita")
define t = Character("Taiga Sakurai")
define ch = Character("Chisei Jikoma")
define s = Character("Setsuna")
define sh = Character("Shoma")
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
    jump sandbox # (Un)Comment "jump sandbox" to switch between sandbox and the game.

# Opening video goes here.

label prologue:

#background Interrogation Room

"My whole life, I feel like I've been dragged around by my collar."
"I guess when most adults see a kid act out of line, they’re overwhelmed with a need to control the situation."
"Funny, seeing as that’s the very thing I’ve been fighting for: a chance to be in control of my life."

cop "Please state your name and registered Proficiency."

n "My name is Nagen Tesuta."
n "I possess an Intelligence Proficiency."
n "Anything I see, hear, or experience is recorded in perfect detail."