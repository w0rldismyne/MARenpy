#11111
label chapter1_day1_event_morning:

    play music "music/CryingOverYou.mp3"

    scene backgroundC1_T
    #Set a wait time
    scene backgroundroom

    kk "Good morning, brotato chips!"
    kk "We’re going to start this school year with a banging opening ceremony in the amphitheater before classes start."
    kk "You got one hour to be up and ready this morning."
    kk "And now, a request from the heart, an original mix by your’s truly to start your day with fighting spirit."

    "I wake up to a song I’ve never heard blaring from an old radio alarm clock."
    "My dorm is uncomfortably cold compared to my bed, but I have to cross the room in order to turn it off."

    n "Ugh, where’s the off switch on this thing?"

    "From outside my door, I can hear a rush of activity and a loud bang."

    play music "music/TheChase.mp3"

    h "Come on, Nagen, we got to get going if we want to sit together."

    n "Just save me a seat, I’ll meet up with you later."

    j "I tried that, he wouldn’t stop knocking until I opened the door. Do NOT let him in."

    h "If I don’t bug you guys, you’ll just go back to sleep and we’ll be laaate."

    "The banging increases tenfold."

    j "I can’t stop him. His desire to be annoying is too strong."

    h "Open the doooor."

    "I get dressed in record time and slip out before either of my friends can barge in."

    scene backgrounddorm

    "Jona could only restrain one of Hiro’s arms at a time."
    "It was a valiant effort, but he could be dragged wherever Hiro wanted to go."

    show JFrustrated

    j "Where’s your school stuff?"

    n "In my locker, you nut case."

    hide JFrustrated
    show JDepressed at right with move

    j "Sorry."

    hide JDepressed
    show HBase at left

    h "Come on, Uitto’s saving us a spot with her giraffe legs. We gotta go."

    hide HBase
    hide JDepressed

    scene backgroundamp
    play music "music/TheLoyalist.mp3"

    "I’m hoping that means she’s ready to talk to me, but when we get to the amphitheater, Hiro and Jona immediately sit on either side of her."
    "She’s ignoring me in favor of her own reflection."

    show HBase at left

    h "You can sit next to me."

    hide HBase
    show UBase at center

    u "Did you get ready together or something? What took you so long?"

    show JDepressed at right

    j "I didn’t unpack anything yesterday, sorry."

    u "Next time, just send someone ahead. You know I hate-"

    hide JDepressed
    show KBase at right

    play music "music/WeAre.mp3"

    k "Well well well, your entourage is real after all."

    "Uitto lets out an ugly sigh."

    hide UBase
    show UBase at left with move
    show KBase at right

    k "Though I suppose anyone can catch attention with the amount of makeup you put on. Careful not to touch, boys, I heard she doesn’t use sealing spray."

    u "They could care less what I’m wearing, and so should you. This thing you’re doing, it’s not cute. Just go sit down somewhere, these seats are clearly taken."
    
    "She sounds so tired. I’m able to grab her attention and silently ask if she knows this girl from before."
    "Uitto pantomimes a long winded ‘no’. Kitsune, completely oblivious, sits on Jona’s other side."

    k "I could have my fans follow me around all the time, but I was afraid it would make me too unapproachable."
    k "People could get the wrong idea and think I’m a stuck up attention hog."
    
    u "People will think a lot of things no matter what you do. I retired so I could stop worrying about my image."
    
    "I can practically hear the wheels turn as Kitsune tries to think of a comeback."

    n "Did you want to watch the assembly with us?"
    
    k "H-hunh?"

    n "Isn’t that why you came here?"

    k "N-no-"

    n "Then why did you sit down?"

    k "I just wanted to talk to Uitto, so-"

    n "What exactly did you want her to say to you?"

    k "....."

    hide KBase

    play music "music/TheLoyalist.mp3"

    "She gets up quietly and leaves to sit with some other girls."

    u "Thank god. I seriously don’t know what I’d do without you guys."

    h "Why didn’t you just tell her to go away?"

    u "It’s the first day of school."
    u "I’m not going to shit on someone’s self esteem for seeking validation, that’d be pointlessly cruel."
    u "It just sucks that the one person who wanted to talk to me just wanted to compete."

    show HBase at right
    hide UBase

    "We’re interrupted by a comical scale of trumpets as the vice principal bounds on stage. Principal Vivaldi follows close behind in silence."

    show IkBase at left
    
    ik "Welcome, everyone! I hope you all had a good night’s sleep!"

    "No one responds."

    ik "We’ll work on that later. Right now, we wanted to remind you all of a few important school rules before classes start."
    ik "With a lot of hard work, we hope this place can become like home to you."

    show VBase at center
    
    v "All students are to remain on campus at all times."
    v "That means staying out of the wooded areas surrounding the school."
    v "It’s easy to get lost out there and we don’t want anyone to get hurt."
    
    ik "There is a zero tolerance policy toward anyone who commits an act of violence or aggression."
    ik "Hurting another student, or threatening another student, will result in immediate detention."
    
    v "Finally, no student is allowed in the computer lab without an instructor present."
    v "This is to ensure a safe environment."
    v "It is also the reason many of your electronic devices were confiscated before entering the dorms."
    v "We apologize for any inconveniences this might have caused."
    
    "They didn’t even let me transfer my music onto their cheap burner phone. At least I know my stuff’s safe with Maimai."
    
    ik "Now to end on a happier note, here’s Mariko with some announcements about school clubs."

    show MBase at right
    
    m "How’s everyone feeling this morning!?"

    play music "music/leaf.mp3"

    hide IkBase
    hide VBase
    hide MBase
    show MBase at center
    
    "We murmur amongst ourselves with one brave soul demanding more sleep."
    
    m "Sleep is for the weak willed! You lot have spent the last year and a half lazing around already."
    m "If we’re going to make it through another year, we have to face it with fist full of fire!"
    
    "Her little speech inspires laughter. It may not have been the reaction she wanted, but it’s lifted the mood."
    
    m "A-anyway, the point is, this year could really suck if we don’t have the right attitude going in."
    m "Anyone that wants to make a club has to gather at least three interest members before all the faculty advisors get snatched up!"
    m "So, if you have the guts, you should join the cheer squad."
    
    "She scans the crowd. With each passing moment, her bravado falters. She’s shaking."
    
    m "I-if you do, you can learn how to do this."

    hide MBase

    scene backgroundC1_2
    
    "She launches into a backhandspring and lands perfectly on her feet."
    "Without music, her routine feels awkward, and I can tell her nerves are getting to her."
    "It makes it all the more horrifying when something cracks during her floor routine."
    "She fumbles to the ground the minute she tries to stand."

    scene backgroundamp

    show ReBase at left
    
    re "Mariko!"
    
    "Her friend rushes out to get her, followed by Mu at a lethargic pace. Mariko tries to shoo them away."

    show MBase at center
    
    m "I’m fine. God, this is embarrassing."

    show MuBase at right
    
    mu "Stop trying to put weight on it, stupid, there’s a reason you lost some range of motion."
    
    m "I said I’m fine. People are staring."
    
    "Rei swiftly hoists Mariko onto her back."

    hide MBase
    hide MuBase
    show ReBase
    
    re "Just humor us and let us take a look at it later."
    
    "She turns to us with a grin."
    
    re "She’s a-okay everyone! If you’re interested in joining, talk to me or Mariko!"

    hide ReBase
    
    "Mariko buries her face into Rei’s back as she’s carried off stage."
    "Everyone claps out of pity. The second hand embarrassment is palpable."
    #( Vision Bonus Day 1, Immediately following Opening Ceremony)

    play music "music/TheLoyalist.mp3"

    if Vision >= 10:
    
        n "Watching people flounder like that never gets less painful."

        show HBase

        h "Hey, she tried her best. Hopefully she gets some more members soon."

        n "You're seriously going to support her?"

        h "...yeah? You got something against cheerleaders?"

        hide HBase
        show UBase

        u "To be fair, that was a pretty cringey performance. Can you imagine a whole team of that?"

        hide UBase
        show JHappy

        j "I'd stop skipping pep rallies if it was just watching people fall on their faces. Maybe they could add pies or something."

        hide JHappy
        show UBase

        u "No. You just described clowns. I don't do clowns."

        hide UBase

        n "....."

        show HBase

        h "Hey, you okay, man?"

        hide HBase

        n "Yeah... yeah, I just... it felt weird coming from you is all. Sorry."

    return

label chapter1_day1_event1:
    scene backgroundschool

    play music "music/Lights.wav"

    "After the assembly, we’re handed our class schedules. I’m stuck with English, P.E., Science, and Proficiency Management."
    "They wanted me to take the Intelligence course, but I can always switch it if I want to."
    
    menu:
        "Vigor":
            $ Vigor += 1
            call chapter1_day1_event1_classes_vigor

        "Charisma":
            $ Charm += 1
            call chapter1_day1_event1_classes_charm

        "Intelligence":
            $ Intel += 1
            call chapter1_day1_event1_classes_intelligence

        "Vision":
            $ Vision += 1
            call chapter1_day1_event1_classes_vision

    return

label chapter1_day1_event1_classes_vigor:
    scene backgroundamp
     
    "I decide to drop in on Professor Inukai's lecture."
    "Out of all the teachers, he seems the most relaxed and quite frankly, that's what I need right now."
    "Due to the good weather, class is being held outside."
    "No pencils or paper or devices, just all of us gathered in the first two rows while he tries to focus his ideas into an hour and a half."
    "It’s only the first day of class and there’s already a classroom wide brawl."

    show HBase at right
     
    h "Nagen, thank god! See, I told you guys there are more people on my side."

    show MBase at left
     
    m "Cyberdork isn't a Vigor Major, he doesn't count."

    h "He does too! Now that we have even teams, we can go back to normal exercises."

    m "Group team building is normal! Us girls have always had to pick up the slack around here. The least you could do in return is fall in line."

    show ReBase at center
    
    re "That wasn't the nicest way to put it, but she's right."

    hide ReBase
    hide MBase
    hide HBase
    
    "Hiro tears away from me to argue. They’re talking over Professor Inukai the whole time."
    "Completely lost, I gravitate to the two people who aren't up in arms."
    
    n "Shoma, what the hell's going on?"

    show ShBase at center
    
    sh "Well, Mariko and Hiro used to be class reps, but there's not enough students to justify splitting the class by gender."
    sh "So now they're trying to figure out who gets to be in charge."
    
    n "That's not good."
    
    show KBase at left

    k "Says you. Every minute they argue is another minute we don't have to do lunges or mindless exercises. This course was always a joke."
    
    "Shoma nods. I feel out of place sitting alongside them. Second guessing my decision, I go to leave, but Hiro calls out to me again."

    hide KBase
    hide ShBase
    show HBase at center
    
    h "Wait, Nagen, don't go! You gotta stay. I didn't mean to ignore you."
    
    n "Dude, I don't think I belong here, the culture shock alone..."

    show HBase at right
    show IkBase at center

    ik "This isn't going to be a traditional Vigor class. That means no 'teams' or competitions."
    
    m "But, but what about nationals-"

    h "You have to be joking!"

    show KBase at left
    
    k "Then what's the point-"

    hide KBase
    hide MBase
    
    ik "Now, now guys, I'm sure we can find a way to make everyone happy."
    
    "Mariko and Hiro are glaring daggers at each other with Rei caught in between them."
    "Shoma tunes everyone out and starts sewing small patterns into the hem of his coat."
    "Kitsune looks about as uncomfortable as I feel. All of them are ignoring the teacher."
    
    n "Don't you have a lesson plan or something?"
    
    ik "I have a few ideas, but there's not a lot in the books to base them on. So I don't know-"

    show HBase at right
     
    h "This is supposed to be the fun 'no homework' class. Y'know, strength training and junk."

    show MBase at left
    
    m "We're the school's breadwinners. That's why we use class time to prepare for competitions."
    
    ik "There actually won't-"
    
    h "We're all going to get stuck doing the same thing."
    h "That's why it should be something fun, not repeating the same flips and twists over and over again!"
    
    m "I never said we had to do cheer."
    
    h "You were thinking it!"

    hide HBase
    show ReBase at right
    
    re "Guys, please."

    hide Mbase
    show KBase at left
    
    k "What a colossal waste of time. I knew I should have ditched."

    hide KBase
    hide HBase
    hide ReBase
    show IkBase
    
    ik "Please don't!"
    
    "This is a nightmare. The teacher is in way over his head and clearly doesn't know how to hold a class..."
    "Hiro, please forgive me for what I'm about to do."
    
    n "What's going to be on the test?"
    
    "I feel three different people glare at me. Rei watches on with pity in her eyes."

    hide IkBase
    show HBase
    
    h "Dude!"

    show ShBase at left
    
    sh "Test? What test?"

    hide ShBase
    hide HBase
    show IkBase
    
    ik "Excellent questions! Umm, since there's no curriculum guidelines for what I want to do, I'm having to make everything from scratch."
    ik "So we're kinda playing it by ear."
    
    n "But there is going to be a test?"

    show HBase at right
    
    h "DUDE!"

    show IkBase
    
    ik "Yes. Today we'll be assessing how bad the damage is."

    show ReBase at left
    
    re "Damage!?"

    hide ReBase
    hide HBase
     
    ik "Not like that. Sorry, poor word choice. Umm, you all were chosen by Estella for your unique abilities and were forced to put all your eggs in one basket."
    ik "And then they sold the baskets like they were their eggs."
    ik "But they didn't teach you anything about chickens or farming or anything."
    ik "So you could be making bad eggs right now, and putting them in a basket with a hole in it."
    ik "Does that make any sense?"
    
    "It was definitely long."
    
    n "What exactly do you want us to do?"
    
    ik "A pretest of sorts. Everyone take a clipboard and pencil."
    ik "After this, we'll all do ten laps around the field."
    ik "Me included. No point in making you guys do something I wouldn't do myself."
    
    "With some minor complaints, everyone completes a variety of benign physical exams."
    "The teacher forgot to bring something to write down everyone's results, so I’m put in charge of remembering everyone's numbers."
    "He could have borrowed something from the other students, but I think he was looking for something for me to do."
    "I'm not sure what this is all for, but at least it’s not boring."
    
    ik "Alright, everyone, huddle up!"
    
    "He waits patiently for everyone to calm down."
    
    ik "Competitions, while they make for good advertising for schools, they're hell on your body. I'll text you this week's homework once I've finished crunching the numbers."
    ik "What is smarter when things are okay?"
    
    Everyone "?????"
    
    "It takes a couple tries, but he finally gets us to yell back."
    
    Everyone "The mind?"
    
    ik "What is smarter when things are going wrong?"
    
    Everyone "...the body?"
    
    ik "We'll keep working on that."

    hide IkBase

    return

label chapter1_day1_event1_classes_charm:
    scene backgroundcharm

    "Ms. Yamamoto writes a single thing on the board at the beginning of class before her lecture; a chapter number."
    "When Uitto complained about her class, I was honestly expecting more of a spinstery type of  woman."
    "Instead, the class is taught by a tiny woman looking for the world like a Victorian child up past their bedtime."
    "The minute she opens her mouth, she commands the room."

    show SaBase
    
    sa "My lectures are, and only will be, a summary of the most important things you'll need to know."
    sa "If that is not enough for you, or you're hopelessly confused, read the chapter."
    sa "If I find you in my office crying about how you don't understand the material, the first thing I'm going to ask is if you read the chapter and you will definitely be instructed to read it again."
    sa "I would strongly suggest downloading the book now to save yourself the tissue cost."
    sa "You'll find the link on my faculty page. It will be free for the duration of the course, but if you want to keep it after, you'll have to pay full price."
    sa "I may not be a sadist, but I am a capitalist at heart. That said, I notice some of you here aren't actually enrolled in the course..."
    
    "She’s staring directly at me as she says this."
    
    sa "Feel free to take a seat closer to the front."
    sa "If this is how you want to spend your freetime, you might as well get a good seat."
    
    "I refuse to move. Most of us are crowded into the back rows anyway. Like hell I’m going to call attention to myself and put myself where everyone can see me."
    
    sa "Suit yourself."
    
    "She shuffles to a luxurious fainting couch and crawls up onto the fluffy cushion."
    "Once stretched out on the chair, she begins her lecture."
    "I’m surprised how captivating she can be without moving a muscle."
    
    sa "Now then, the reason you're here is up until now, you have excelled using the invisible tools that are social and emotional intelligence."
    sa "They are skills that anyone can learn, seldom are taught, and are easily abandoned."
    sa "In spite of that you have, through the years, demonstrated desirable attributes when it comes to communicating with others."
    sa "You must understand this, because unlike Vigor or Intelligence Majors, the societal validity of your powers are dependent on how others treat you."
    sa "At this point, success in whatever path you choose is best measured by social prowess."
    sa "Focus your sights less on the immediate gratification of popularity and more on the ambitions it can serve."
    sa "World leaders, Nobel Prize winners, CEOs and religious zealots; all were given platforms to make change by other people."
    sa "Before you can be given your own platforms, you must earn and maintain your influence over others."
    sa "This week, I want you to study how you interact with others."
    sa "Really try to pinpoint what behaviors or habits bring you the most success versus the ones that create a wall between you and your target."
    sa "Take note, especially of the methods you favor and any body language you use."
    sa "To get a good start, I want you to get into groups of three."
    sa "Two of you will talk while the third records any patterns of effective communication, like touch or mirroring."

    hide SaBase
    show NBase
    
    nk "What do you mean mirroring?"

    hide NBase
    
    "Ms. Yamamoto points to the blackboard."

    return

label chapter1_day1_event1_classes_intelligence:
    scene backgroundlibrary
    
    "I arrive at my class as printed on my schedule."
    "Intelligence Majors typically dominate most academic institutions, so it’s especially odd to have us all crammed in the same class together like this."
    
    show KkBase

    kk "And Nagen makes five; that's everyone then."

    hide KkBase
    show YBase
    
    y "Judging by the setting, I suppo-ose this will be more of a theory than i-independent practice."

    hide YBase
    
    "He begrudgingly shoves his instrument case under the table."

    show MhBase
    
    mh "Aww, that's no fun. Ah well, what can you do?"

    hide MhBase
    show MuBase
    
    mu "Are we going to be tested on everyone's subjects? If so, that's what, twenty-five exams?"

    hide MuBase
    show MhBase
    
    mh "Make that twenty, taking tests isn't a subject I don't think."

    hide MhBase
    
    n "Literally, there are so many college courses on data collection and human psychology it's not even funny."

    show MuBase
    
    mu "At least psych would be useful."

    hide MuBase
    show YBase
    
    y "Not for Chisei, or any other creatives for that matter. How un-nfortunate."

    hide YBase
    show KkBase
    
    kk "Umm, dudes, where's the teacher?"

    hide KkBase
    
    "Class should have started ten minutes ago. We look around, but we can't find any evidence of the teacher's stuff either."
    "We are in the right room, I’m sure of it."
    
    show MhBase

    mh "Maybe Yaguchi's just late?"

    hide MhBase
    show YBase
    
    y "Unacceptable. Every-y teacher has the ability to directly contact us. If he was running behind, he shhhhould have told us."
    
    hide YBase
    show KkBase

    kk "So, like, free period then?"
    
    n "No, hell no, if we have to be here, so does he."

    hide KkBase
    show MuBase
    
    mu "Worried you'll get a zero are you?"

    hide MuBase
    
    n "Yeah?! I'm not going to get marked off points for being absent when he's the one who didn't show up!"

    show MhBase
    
    mh "Maybe he's in his office? Let's go catch him red-handed!"

    hide MhBase
    show KkBase
    
    kk "Red handed doing what?"

    hide KkBase
    show YBase
    
    y "Neglecting his duties."

    hide YBase
    show KkBase
    
    kk "You guys really want to provoke a brotentate of this place over grades?"

    hide KkBase
    show MuBase
    
    mu "Nagen, you know where everything is, right? Where's his office at?"

    hide MuBase
    show KkBase
    
    kk "We're really doing this?"

    hide KkBase
    
    n "I'm bad at giving directions, but I can show you where it is."
    
    scene backgroundyoffice

    play music "music/TheChase.mp3"
    
    "Everyone gathers behind me as we march into Mr. Yaguchi's office."
    "The place is littered with pieces of scrap metal and welding equipment."
    "The walls are decorated with a series of screens that vary in shape and size."
    "If I hadn't read the sign on the door, I might have confused him with another student."
    "He can't be that much older than us. He doesn't ever bother to look up from his work as we burst into his office."
    
    n "This looks like a security office."

    show YaBase
    
    ya "That's because it's what I was hired for. I agreed to babysit you until they found proper tutors that wanted to work with you."
    
    "He gestures to one of the monitors."
    
    ya "I know you showed up, so don't worry about participation points or whatever they're called; you'll all get A's."
    
    "He continues working on a large hard drive, soldering bits of copper to each other in incomprehensible patterns."
    
    hide YaBase
    show YBase

    y "Is that all?"

    hide YBase
    show YaBase
    
    ya "Yeah. I'm not going to assign a bunch of busy work for you to finish just to see if you will."
    ya "Just stay out of trouble. Go study whatever you want, or don't."

    hide YaBase
    show YBase
    
    y "Aren't you g-going to... teach us?"

    hide YBase
    show YaBase
    
    ya "What the hell could I teach you? I'm a metal head engineer, none of that fits under your umbrellas. And y'all too specialized to pick one to study up on."
    ya "So what am I supposed to do if you ask a question, Google it? You could do that yourself and cut out the middle man."
    
    n "So you're too stupid to teach us."
    
    "He sets down his tools with a grim expression."
    
    ya "Do you know anything about graduate level robotics or thermodynamics?"
    
    n "No."
    
    ya "Are any of you remotely interested in doing it as a career?"
    
    "We all shake our heads."
    
    ya "Then by your definition, Mr. Reverse Psychology, you’re stupid."
    ya "You don't know something you have no interest in, which makes you stupid because I know it. Does that make it true?"
    ya "You a stupid kid?"
    
    n "N-no!"
    
    ya "Then don't go around comparing intelligence to how much you know like you're collecting Pokémon cards."
    ya "What good is understanding astrophysics when what makes you happy is making sandwiches?"
    ya "That's what being smart is, figuring out what makes you happy and how to get it."
    
    hide YaBase
    show MuBase

    mu "What would make me happy is a teacher who does his job."
    
    hide MuBase
    show YaBase

    ya "Jesus, college kids would just take the day off when their teacher's absent."
    ya "Can't you just take a day off?"

    hide YaBase
    show YBase
    
    y "....."

    hide YBase
    show MhBase
    
    mh "....."

    hide MhBase
    
    "No one's answering, which in itself is an answer, I guess."
    "I'm just glad I'm not the only one that feels guilty if I'm not working on something."
    
    show KkBase

    kk "Is that gonna be an essay prompt or something?"

    hide KkBase
    show YaBase

    play music "music/Lights.wav"
    
    ya "Sit down, all of you."
    ya "I'm going to ask you something, and I'm afraid I already know the answer."
    ya "How many of you actually want to have a job in the field you were assigned?"
    ya "Not because you were told to or it's easy for you, but because you enjoy it."
    
    "Only Yoku and Mu raise their hands. I can see Momoko thinking about it, but even she isn’t sure."
    
    ya "See, the problem with labeling you kids by what you find easy to understand is you get pigeonholed into a lifestyle that isn't sustainable."
    ya "As soon as you get to the higher level stuff, it's going to be real work to keep progressing, and that's going to be hell if the end result isn't what makes you happy."
    ya "If you're just here to make someone else proud of you, then just stop. Stop measuring your self-worth by milestones other people set for you."
    ya "It's not worth the stress. Trust me."
    
    n "So what, we're just supposed to peak in highschool?"
    
    ya "With as much grace and dignity as you can muster."
    ya "You only got a few more years of this micro society to go before people stop keeping tabs on you and you gotta worry about real shit."
    ya "Don't spend it all working your ass off for no reason, have fun for God's sake."
    
    kk "Well that's just depressing."
    
    ya "What's depressing is the army of kids that feel like failures when they remind people they're human."
    ya "I saw a kid have a breakdown because he got an 89 on one test. It's not like getting A’s ever made him happy either."
    ya "All demanding perfection ever does is take the joy from your accomplishments."
    ya "It took me almost a decade to undo what that kind of thinking did to me."
    ya "The least I can do is put a tourniquet on your bleeding hearts before you completely fall apart in your thirties."
    
    hide YaBase
    show MuBase

    mu "And how do you plan to do that?"

    hide MuBase
    show YaBase
    
    ya "For starters, getting you to do things outside of your Proficiency."

    hide YaBase
    show YBase
    
    y "Uh... w-what?"
    
    n "You're putting all your self-esteem into one thing. That's a shit idea. God forbid you go deaf, what would you do?"
    
    "Yoku visibly pales."

    hide YBase
    show YaBase
    
    ya "That's an extreme example, but you get the idea."
    ya "Having a Proficiency should be a perk, not a life sentence."
    ya "So we're going to mix it up, each of you is going to pick a random thing and we'll all look into it together."
    ya "It can literally be anything-"

    hide YaBase
    show MhBase
    
    mh "Cosmetology!"

    hide MhBase
    show YaBase
    
    ya "....."

    hide YaBase
    show MhBase
    
    mh "I, uh, please? It's just a hobby right now, but I'd like to be able to do more than dye extensions if I could."

    hide MhBase
    
    n "I don't think-"

    show YaBase
    
    ya "Perfect, we'll start with that."

    hide YaBase
    show MuBase
    
    mu "...really?"

    hide MuBase
    show YaBase
    
    ya "She had an idea first. If you come up with anything, send it my way and we'll rotate through the year."
    
    "I have no idea what to pick. At least Kazz and Momoko have some idea of what they want to learn. That'll buy me a few weeks."

    hide YaBase
    show MuBase
    
    mu "I don't understand how this is better than studying in the nurse's office."

    hide MuBase
    show YBase
    
    y "Be-ethoven went deaf a-and continued to compo-ose. As long as I can see and fffeel, I can still write mu-usic."
    
    hide YBase

    "This is going to be a long year."

    return

label chapter1_day1_event1_classes_vision:
    scene backgroundclass
    
    "The first thing that strikes me about the Vision class is how small it is."
    "I thought the courses would be more evenly distributed."
    "There are only four other students and all of them notice me immediately."

    show JHappy
    
    j "Nagen, did you get lost?"

    show ChBase at right

    ch "Maybe he is a fellow brood parasite."

    show JDepressed
    
    j "I don't think he's here to lay eggs, Chisei."

    show IBase at left
    
    i "He better not be."
    
    ch "What I mean is, maybe he has been lying about which major he belongs to."

    "Ichita and Jona hone in on me with renewed interest."

    i "Oh shoot, can you literally read minds or something?"
    
    ch "And I thought my ability was intrusive, you poor thing."

    show JFrustrated
    
    j "Who's thoughts have you been reading, young man?"
    
    n "N-no, I don't- There's no rule that says I can't be here."

    hide JFrustrated
    show JMad
    
    j "So you have tried to read my mind then."

    hide IBase
    show KiBase at left
    
    ki "Lay off the new kid, guys, he'll tell us in his own time. You're makin' him uncomfortable by swarmin' him like that."
    
    show JDepressed

    n "This isn't everyone, is it?"
    
    ki "’Fraid so. There might be a few border-liners who could qualify, but this is more than I was expectin' to be honest."

    hide KiBase
    hide JDepressed
    hide Chbase
    show VBase
    
    v "Indeed, it can be quite difficult for people to acknowledge the abnormal nature of their abilities."
    
    "A hush falls over the room as our principal stands where a teacher should be."
    "She gestures for us to sit down. It takes a bit to get everyone to settle."
    "If I knew she'd be teaching, I wouldn't have come."
    "Everyone is waiting for me to sit too. I'll stay for this one class."
    
    v "Coming here took a lot of courage."
    v "I've spent a great deal of my life trying to prove to others that my ability is real and there are others like me."
    v "The definition of what it means to be a Vision Major is vague by design, to accommodate any new proficiencies that may come along."
    v "I am most familiar with ones concerning the dead, but it is my goal for all of you to have better control over your abilities by the end of the year."
    
    n "What makes you qualified to teach? You were a police officer, not a scientist."
    
    v "Ms. Chisei, if you're comfortable with assisting me in this matter, I would appreciate it."

    hide VBase
    show ChBase at right
    
    ch "I am not sure what I can do, but okay."
    
    "She joins the teacher at the front of the room."
    
    v "Your left hand is prone to possession; may we borrow it?"

    "Chisei goes pale."

    ch "I, uh- Who is we?"
 
    "Vivaldi points to her broach."
 
    v "Takahara Kenji, 8th grade, he's agreed to help with our lessons."
  
    ch "Umm... Okay then."

    v "I will have Takahara read the last text on your phone, Mr. Tesuta, and have him transcribe it on the board using Chisei's hand. Is that agreeable to you?"

    hide VBase
    
    "I check my phone to make sure no one sent me anything embarrassing. The last thing I got was from Uitto confirming she had my new number."
    
    n "Yeah, go ahead."
    
    "I feel my phone vibrate in my pocket. A few seconds later, Chisei’s scribbling on the board."

    hide Chbase

    scene backgroundC1_3
    
    "She starts drawing a shaky stick figure drawing, her expression changing from confusion to horror."
    
    ch "Umm... is this going to be appropriate for class?"
    
    "I can't help but laugh. Jona grabs my shoulders."
        
    j "Dude, did you plan this?"
    
    n "No, man, Hiro must have sent me something after I checked it."

    scene backgroundclass

    hide JHappy
    show VBase
    
    v "That's enough, Takahara."
    
    "Chisei throws down the chalk, her face flushed."
    
    v "Thank you, Chisei, you may take your seat."

    hide VBase
    
    "Jona and I are trying our best not to laugh as Chisei speed-walks to her chair."

    show ChBase
    
    ch "That was unnecessary and you know it."

    hide ChBase
    
    "Vivaldi claps her hands together, silencing the room."
    
    show VBase

    v "As you can see, Vision Proficiencies are difficult to control."
    v "With a little patience and introspection, you can prevent them from dominating your life."
    v "In due time, your abilities could be refined as a tool you can use."
    v "However, it's best to keep our goals small at first."
    v "The smallest set back can feel devastating when we're setting our expectations based on how we view other people."
    
    "She turns and draws a small table on the board."
    
    v "Each of your abilities are unique, so it's been difficult to try to design exercises that will apply to all of you."
    v "We'll start by taking five minutes to write down all of the things about your power that upsets you."
    
    "She waits patiently for everyone to finish."
    
    v "Now, raise your hand if you wrote less than three things on your list."
    
    "No one raises their hand."
    
    v "Less than eight."
    
    "Still nothing."
    
    v "Eight or more."
    
    "Everyone raises their hand."
    
    v "Even though your abilities deal with the unseen, the effects they have on us are very real."
    v "The struggle with negative intrusive thoughts creates an illusion of isolation."
    v "As you can see, everyone in this room shares this struggle. You may put down your hands."
    
    "She proceeds to collect examples from the class to put into the first column of her table."
    
    v "Now, look at your own list without the context of your abilities, environment, and so on."
    v "If you feel comfortable, you can trade lists with someone to aid in this part of the exercise."
    v "I want you to break these items into two categories; things that can change, and things that can't."

    hide VBase
    
    "Jona stares at his piece of paper for a long time before taping on my shoulder."

    show JDepressed
    
    j "Do you, uh, could you trade with me?"

    hide JDepressed

    menu:
        "Trade":
            $ jRep += 1
    
            "I trade papers and look at his list. It’s surprisingly long."
            
            #/Hard to look at people/Getting stronger?/makes people uncomfortable/can't focus/useless/can't trust people/know things I shouldn't/can't turn it off/exhausting/manipulative/belonged to mom/
            #(Circle the ones that can be changed) 

        "Don't Trade":
            $ Vision +=1

            n "Sorry, I don't want anyone to look at this."
            
            "Probably should have thought of that before I wrote it for an assignment!"

    show VBase

    v "Now, throughout the week, I want you to document how often your abilities trigger."
    v "Include emotions, activities, environmental factors, and your reaction to the trigger."
    v "When we know what to expect, it's easier to de-escalate and disrupt the intrusive episodes."

    hide VBase
    show IBase
    
    i "What about the lists?"

    hide IBase
    show VBase
    
    v "Hold onto those in a safe place. We will use them again at a later date."

    hide VBase

    return

label chapter1_day1_event2:
    scene backgroundhall1
    
    play music "music/Interloper.mp3"
    #BG: Hallway
    "It’s surreal being thrown back into school life without my friends in every class."
    "Back at Estella, we had been clumped together for everything year after year. Hearing the bell ring is a relief."

    "The hallways swarm with a stampede of students."
    "No doubt many of my classmates had also packed up several minutes before the bell, waiting for the floodgates to open."
    "As I wade through the crowd to meet up with my friends, the PA system sparks to life."

    PA "Attention all students."

    "That voice isn't human. Or, if it is, it’s distorted beyond recognition. The disturbing pitch is enough to interrupt everyone's conversations."

    PA "I would like to commend you all for overcoming your fears to be here today."
    PA "Many of us are still recovering from the Guwon Riots."
    PA "Our bodies, families, and minds have been torn apart, which is why it pains me to announce this school is not the safe haven it appears to be."
    PA "No doubt you've noticed the surrounding town has been abandoned, evacuated, no signs of reconstruction for miles."
    PA "It's the ideal place to put a school; if you don't want your students to leave."

    "A staff member bolts out of the classroom and down the hall."

    "Mr. Yaguchi tries to cover the voice from the PA with his own instructions, but it’s too late."

    PA "Nagen Tesuta, Uitto Hanatabe, Jona Oshima; you have five days to turn in your leader, Hiromichi Morine."
    PA "If he is not restrained on the practice field by then, the punishment will be tenfold."
    PA "Only the valiant shall escape the shore of corpses."

    "The message cuts out."
    "I assume, on blind faith alone, that whoever is responsible will be caught."
    "Everyone is staring. Everyone knows. They may not have beforehand, but now it’s like being under a spotlight."

    scene backgroundC1_1

    re "It's not true, is it?"

    "Rei, my old classmate, refuses to be shepherded away from us by her friends."

    re "Guys, tell them you had nothing to do with riots. There has to be a mistake. We were all together. We-"

    mu "Why did you think they were missing during the evacuation?"

    re "Nagen was sick, and I saw Hiro."

    "Rei glares at Mu with tears in her eyes."

    re "He came back to get us. The gym wasn't safe so we had to relocate, isn't that right? Hiro, tell them, please. Tell them the truth."

    j "Do you want him to tell the truth or tell them he wasn't involved? He can't do both."

    n "Jona, stop helping."

    scene backgroundhall1

    show ReBase

    re "You lied to us!?"

    hide ReBase
    show YBase

    y "So wher-re are the other-rs?"

    hide YBase

    n "There were no 'others', it was just us."

    show DBase

    d "All of you knew. You knew, and then you just show up here like nothing happened? How long were you planning to lie to us?"

    hide DBase
    show TBase

    t "Does it matter? What's done is done."

    hide TBase
    show IBase

    i "Do you want to take your licks all at once or in small doses throughout the year?"

    hide IBase
    show ChBase

    ch "Violence begets more violence."
    ch "Demanding retribution will only further the cycle, no matter how deserved."
    ch "Deliverance should only have been provided to the ones it was owed."

    hide ChBase
    show UBase

    u "We don't owe you shit."
    u "You don't like that we're here? Fine!"
    u "Then leave us the fuck alone." 
    u "We didn't come here to start shit, we came because we were forced to."
    u "If anyone lays a hand on Hiro, I'll claw your eyes out."

    hide UBase
    show ReBase

    re "...you're not even going to apologize?"

    hide ReBase

    "Rei pleads with her last bit of hope. Everyone else looks on with a mixture of grief and loathing."
    "Uitto stands between us, acting as a rage-filled human shield. I can hear staff thundering down the stairs after us."

    menu:

        "Apologize":
            $ reRep += 1
            $ jRep -= 1

            n "Rei, I never meant to hurt you guys, I swear. I'm sorry."

            show JMad

            j "But it's not our fault they have survivor's guilt."

            hide JMad

            n "Seriously dude, not helping."

        "Stay silent":
            $ Reputation -= 1

            n "....."

            show HBase

            h "I'm the one that owes you an apology."

            hide HBase
            show UBase

            u "Hiro, no."

            hide UBase
            show HBase

            h "But they're right; I failed as your leader. I should have taken better care of you all. I'm sorry."

            hide HBase

    show VBase

    play music "music/Still.mp3"

    v "Children, please disperse. If you have any concerns with your current situation, you are to bring them to me. That goes for all of you."

    hide VBase

    "Why am I getting scolded? I didn't do anything. They're the ones that swarmed around us like piranhas."
    "Whoever targeted us doesn't just want justice, they want to humiliate us."
    "For that, I’ll make certain their plan backfires. After the halls have emptied, I turn to my teammates."

    n "I'm going to find who did this."

    show UBase

    u "Good. Then we'll be able to show them what happens when you fuck with the 'bad' kids."

    n "We?"

    u "Did you not want my help?"

    n "I didn't mean it like that, I just thought you hated me."

    u "I don't hate you, dummy. Yeah, I'm still pissed that you ratted on us, but no one gets away with threatening my friends."

    hide UBase
    show HBase

    h "Guys, we can't go around talking like this, people hate us enough as is. We're supposed to be laying low, remember?"

    hide HBase
    show JFrustrated

    j "We've already been exposed and you're their main target, Hiro. Are you suggesting we sit back and watch you get attacked?"

    hide JFrustrated
    show HBase

    h "No one said anything about being attacked."

    hide HBase
    show UBase

    u "Either way, a bounty's on your head, and it made everyone think it was okay to come for you."

    n "I'm not saying we have to start a fight with them, but Uitto's right. If we don't see this through, other people could jump on the bandwagon."
    n "With one message, they've butt fucked my campaign and our chances at going through school under the radar." 
    n "I'm going to find them and shut them down."

    u "The lil' bitch gotta pay."

    hide UBase
    show HBase

    h "You two are impossible."

    hide HBase
    show JDepressed

    j "I'm not against helping, if you have a use for me that is."

    hide JDepressed
    show HBase

    h "Guys... Okay, fine. But no one gets hurt. We got a reputation to fix."

    hide HBase

    g "Reputation can be gained or lost during events. You can increase your reputation by helping other students."
    g "This is not the same as alignment. A villainous character can have a good reputation."

    n "I make no promises. The message had to go through the PA system. We should start there."

    show NBase

    nk "....."

    hide NBase

    return

label chapter1_day1_event3:
    play music "music/leaf.mp3"
    scene backgroundavroom

    #[BG: PA Room (interior)]

    "Good, it's still unlocked."
    "The teachers' must have forgotten to lock it when they came back for us."
    "The recording box is sweltering, how long has this equipment been running?"

    g "Click on items to see if it leads to any clues."

    call chapter1_point_and_click

    scene backgroundhall2

    show UBase

    u "There's not much here."

    hide UBase
    show JFrustrated

    j "The teachers' might have confiscated everything already."

    hide JFrustrated
    show KkBase

    kk "Nonononono; what are you doing!? No one's allowed in the booth!"

    hide KkBase
    show JDepressed

    j "I'm very much outside the booth. It's too small to fit all of us."

    hide JDepressed
    show KkBase

    kk "Bro, just, okay?"

    "Kazz runs in and turns off the overhead mic. Has that been on the whole time?"

    kk "I get you're ticked off, but don't drag my equipment into this. I already lost half my tech today, I can't lose Pepper too."

    hide KkBase
    show UBase

    u "Pepper?"

    hide UBase
    show KkBase

    kk "My boom mic. Now get out. I'm the only one who's managed to keep PA privileges and I plan to keep it that way."

    hide KkBase
    show HBase

    h "Alright, fine. We'll leave you alone with... Pepper."

    hide HBase

    "I think I have enough to start questioning people, but where to start?"

    g "When questioning students, allies can be used to quickly gather testimonies from students they share a class with."
    g "Be careful using second-hand testimonies; sometimes things get lost in translation."
    g "Hanging out with classmates will give you bonuses in their Major."
    g "Each Major has different strengths; experiment to see which works best for you."

    return

label chapter1_point_and_click:
    while check_book is False or check_cd is False or check_mic is False or check_laptop is False:
        call screen chapter1_point_and_click_objects
        label chapter1_point_and_click_interaction_complete:
            pass
    return

screen chapter1_point_and_click_objects:

    modal True

    if check_book is False:
        imagebutton:
            focus_mask True
            idle "images/Interactables/announcementlistidle.png"
            hover "images/Interactables/announcementlist.png"
            action SetVariable("check_book", True), Hide("chapter1_point_and_click_objects"), Jump("chapter1_point_and_click_objects_book")

    if check_cd is False:
        imagebutton:
            focus_mask True
            idle "images/Interactables/cdsidle.png"
            hover "images/Interactables/cds.png"
            action SetVariable("check_cd", True), Hide("chapter1_point_and_click_objects"), Jump("chapter1_point_and_click_objects_cd")

    if check_mic is False:
        imagebutton:
            focus_mask True
            idle "images/Interactables/microphoneidle.png"
            hover "images/Interactables/microphone.png"
            action SetVariable("check_mic", True), Hide("chapter1_point_and_click_objects"), Jump("chapter1_point_and_click_objects_mic")

    if check_laptop is False:
        imagebutton:
            focus_mask True
            idle "images/Interactables/laptopidle.png"
            hover "images/Interactables/laptop.png"
            action SetVariable("check_laptop", True), Hide("chapter1_point_and_click_objects"), Jump("chapter1_point_and_click_objects_laptop")

label chapter1_point_and_click_objects_book:

    "A list of morning announcements. It matches everything Kazz read this morning, including the club ads."

    jump chapter1_point_and_click_interaction_complete

label chapter1_point_and_click_objects_cd:

    "I can't make sense of this organizational system. Why aren't they alphabetized?"

    jump chapter1_point_and_click_interaction_complete

label chapter1_point_and_click_objects_mic:

    "It's wired directly into the school's speakers. There's no way to record with it as it is."

    jump chapter1_point_and_click_interaction_complete

label chapter1_point_and_click_objects_laptop:

    "Nothing is queued to play. The browser history isn't terribly exciting. Just a bunch of Google searches on troubleshooting home assistants."
    
    jump chapter1_point_and_click_interaction_complete

label chapter1_day1_event_night:
    scene backgroundroomn
    play music "music/WhereS.mp3"

    #(AN: A black text box with blue writing will be used for a nameless dialog titled "Dark". These lines are not voiced, but are part of Nagen's internal dialogue.)
    #[BG: Nagen's room Night]

    "I’ve done a decent job distracting myself today, but it's getting late."
    "Everyone I know has gone to bed. My arms are tired from recreating the oldest recognized constellations on my ceiling with glow in the dark stickers."
    "I lay there, tracing the patterns with my eyes until the stickers lose their glow." 
    "In the darkness, I fall victim to my overactive mind."

    Dark "Everything is ruined. They're coming after Hiro and then you're next."

    "My chest burns."

    Dark "You need a new plan. Then a plan for when that one fails and then another."

    "I need to sleep. I have class in six hours. Just stop thinking and sleep already."

    Dark "You don't deserve sleep. Not until you fix everything you've broken."

    "The pain is sudden. It feels like I've been stabbed with a screwdriver. I search my chest, but nothing looks any different than yesterday."

    Dark "Even your body's broken."

    "Even though I know it's my imagination, I turn on the light and check again, just in case."

    return

#22222
label chapter1_day2_event_morning:
    play music "music/CryingOverYou.mp3"
    scene backgroundroom

    "I don't remember falling asleep. The room is eerily quiet. Did I seriously wake up before my alarm? I roll over and stared blankly at the clock... Nine thirty..."

    n "Shit!"

    "My alarm says it's going off, but no sound is coming out. I fall out of bed in a panic."

    return

label chapter1_day2_event1:
    play music "music/TheLoyalist.mp3"
    scene backgroundhall2

    "By the time I look presentable, first period is over and everyone's milling about the halls."

    show JHappy

    j "You're alive! No one else wanted to pair up with me, I had to work in a group of three because of you."

    hide JHappy
    show UBase

    u "If you're going to ditch, you could at least text us first. We were worried about you."

    n "Sorry, I set my alarm, but-"

    hide UBase

    "Across the hall someone slams a locker door shut. Kazz is pacing around while his friends watch with varying degrees of interest."

    show MBase

    m "Seriously, Kazz, what's with killing the broadcast? I was almost late to class because of you."

    hide MBase
    show KkBase

    kk "I appreciate your concern, but you're at an eight and I need you at a five or less, my dude. We can't all be eights. Mu, please try again."

    hide KkBase
    show MuBase

    mu "I am trying. I've called, like, ten times. It's not down here."

    hide MuBase
    show KkBase

    kk "Have you actually called ten times or are you estimating?"

    hide KkBase
    show TBase

    t "He could call forty and it wouldn't matter if it died in the middle of the night."
    t "I'm sure it'll turn up eventually. You can live a few days without your phone, can't you?"

    hide TBase
    show KkBase

    kk "I can see my life flash before my eyes. So many choice memes."

    hide KkBase
    show KBase

    k "...My demo reels."

    hide KBase
    show KkBase

    kk "...The embarrassing pictures of Dyre."

    hide KkBase
    show TBase

    t "How embarrassing?"

    hide TBase
    show KkBase

    kk "Don't know; he hasn't seen them yet... I think."

    hide KkBase
    show KBase

    k "Dyre didn't take your phone, ding dong, it's obviously one of them."

    hide KBase

    "Kitsune glares at us."

    show MBase

    m "Let's not jump to thinking it's stolen. It's probably under his pillow or something stupid."

    hide MBase
    show HBase

    h "Exactly, there's no reason for us to take Kazz's phone. All of us have the same crappy model anyway."

    hide HBase
    show KBase

    k "She would. She's been so jelly of me ever since we got here and now she's trying to sabotage my debut a second time!"

    hide KBase
    show UBase

    u "....."

    n "Second time?"

    u "...Yeah, I was hoping you'd know what they're talking about. You sure I never complained about a mouthy, white-haired peacock?"

    n "Nope, I got nothing."

    u "Well, if Nagen doesn't remember it, it didn't happen."

    hide UBase
    show KBase

    "Kitsune trembles, her jaw clenched tight."

    k "You take that back, you self-centered harlot."

    hide KBase
    show UBase

    u "Honey, it's not a bit we're doing."
    u "I honestly don't remember what you're talking about and we have zero interest in that nerd's little trinket."

    hide UBase
    show HBase

    "Hiro steps between the two feuding girls with a stern expression."

    h "No one here has stolen anything."
    h "If you want our help looking for Kazz's phone, that's one thing, but don't go blaming us for everything that goes wrong just because you can."
    h "Kazz, what does it look like?"

    hide HBase
    show KkBase

    kk "Black with an hourglass full of skulls on the back."

    hide KkBase

    #[Player Choice]
    #A. We'll keep an eye out ( No quest for now, we gotta slim down the scope )

    #kk "Really? Thanks so much, really, that thing's the second most important thing in the world to me."

    #t "What's the first, friendship?"

    #kk "If you're going to make fun of my brolosophy, you'll never earn the power of friendship."

    n "I haven't seen it."

    show MuBase

    mu "That's what everyone's been saying."

    hide MuBase

    n "I don't know what else to tell you, man."

    show MBase

    m "Come on guys, let's check somewhere else. We might have better luck if we split up."

    hide MBase

    "The bell rings, leaving us only five minutes until our next class. As the others depart, Jona shakes his head."

    show JDepressed

    j "Things would be so much easier if some of us were nicer."

    hide JDepressed
    show HBase

    h "Hey!"

    hide HBase
    show JFrustrated

    j "I'm not bagging on you, man, but I'm not spending any of my breaks looking for someone else's stuff."
    j "One of you two should do it, you were the meanest."

    n "What did I do?"

    hide JFrustrated
    show UBase

    u "Defended me it seems, but hey, I'm not complaining."
    u "Anyway, Jona, no one promised we'd find it."

    hide UBase

    #[If Quest 1 = Y]

    # g "During your time at school, some students will ask for your help. Helping other students is a great way to improve your reputation. Some students will have rewards in exchange for your help." 
    #[Main Branch]

    show NBase

    nk "....."

    hide NBase

    "We splinter off into our respective classes. I do my best not to nod off during Ms. Sato's lecture on symbolism."

    return

label chapter1_day2_event2:
    play music "music/Lights.wav"
    scene backgroundclass

    "Jona and I have found a quiet corner to hide in for science."
    "It’s just far enough away from the teacher to overlook, but not so far away we'll get targeted for being 'too quiet'."

    show JMad

    j "...I'm just saying if I wanted a handwritten font, I would just write by hand."

    n "I don't know what to tell you, man, I'm not the one who typed up the syllabus."

    "He gets hung up on the strangest things."

    n "I got other things to worry about."

    hide JMad
    show JRelax

    j "Like that girl that's been following you around?"

    n "...What girl?"

    j "If I knew who she was, I'd have used her name."

    n "Well what did she look like?"

    hide JRelax
    show JDepressed

    j "....."
    j "Purple blob."

    n "Everything looks purple through your goggles."

    j "You've been so jumpy lately, I assumed you already knew."

    "I peer out the doorway of the classroom and see a handful of kids lingering in the hallway."
    "I pull out my phone, ready to dial Hiro. If someone was following me then-"

    hide JDepressed
    show JHappy

    j "Gotcha!"

    "He cackles behind his mask."

    n "Dude!"

    j "Man, you've gotten gullible lately."

    "He shakes his head."

    hide JHappy
    show JRelax

    j "Why would someone follow you around? All you do is sit around on the computer all day."

    n "I do other stuff!"

    hide JRelax

    "The asshole keeps laughing as we pack up our stuff to leave."
    "He runs out the door and before I can catch up to him, I feel my arm jerk back."

    scene backgroundhall1

    show SBase

    s "....."

    "She stares at me with blank indifference, refusing to let go of my arm. I'm surprised a girl so small can be so strong."

    s "Well, say something."

    hide SBase

    "I’m confused until her friend scurries up next to her. With shaking hands, she holds out a to-go cup to me."

    show NBase

    nk "The, uh, the cafe gave me the wrong order."

    "Setsuna lets go of my arm and rolls her eyes."

    nk "It's coffee... I don't know if you'd like it. But, um, you can have it if you want."

    "I take the cup from her, but she keeps standing there, staring at the floor."

    n "...Thank you?"

    "I can tell there’s something else she wants to say, but she’s too nervous."

    nk "And, um, if you're not too busy..."

    "Wait a minute, no way."

    nk "Would you please join us on the temp council?"

    "Oh."

    hide NBase
    show SBase

    s "That's what you wanted to ask him?"

    hide SBase
    show NBase

    nk "We got your application form."
    nk "The rest of us are running unopposed, so we've already started as acting chairs, it should be the same for everyone."
    nk "So, since you're also unopposed, we were wondering-"

    hide NBase
    show SBase

    s "No. No. No. We weren't wondering anything."
    s "Kietsu and I have things under control and we've already received multiple application forms for president, so it isn't the same."

    hide SBase
    show NBase

    nk "'Not Nagen' isn't a viable candidate, no matter how many times people submit it!"

    hide NBase
    show KiBase

    ki "I don't see what the big deal is."

    hide KiBase
    show SBase

    s "Really!? You don't see-"

    hide SBase

    #(Setsuna and Kietsu, feel free to adlib here. Setsuna against Nagen joining, Kietsu for Nagen joining. At least 3-4 sentences.) 
    "As the two start fighting, Nanase pulls me aside and speaks in a rushed whisper."

    show NBase

    nk "We haven't been able to get anything done since the start of school."
    nk "Every time the vice chair has an idea, the treasurer shuts it down."
    nk "It's going to be like this for months if something doesn't change."
    nk "Please help us."

    n "And you're sure you want my help?"

    nk "You're the only candidate that wants the job."
    nk "If I ask someone else to run, then neither of you would be able to do anything until the election."

    "So she doesn't have a choice."

    nk "Besides, wouldn't you rather know what you're getting into before your station is permanent?"

    "Fair, if I can't get those two clowns to listen to me now, I might want to rethink my plan."

    n "I'll do it."

    "She beams and then shouts over her shoulder."

    nk "Working together will be so fun, I'm so glad you joined us!"

    hide NBase
    show SBase

    s "Now wait a second, we didn't vote."

    hide SBase
    show NBase

    nk "Rules are rules. If running unopposed, any member of the council can assume their role before the election."
    nk "We don't get a say in who that is. Our hands are tied."

    hide NBase
    show SBase

    s "We don't even have official meetings yet."

    hide SBase
    show KiBase

    ki "We never had enough members to need to."
    ki "I can add him to the group text."
    ki "Madam historian can help you with the rest."
    ki "We're trying to think of something to bring up morale around campus like a banquet or-"

    hide KiBase
    show SBase

    s "We don't have enough money for any of that."

    hide SBase

    "As Nanase herds the two away, she looks back over her shoulder and winks. I hope I'm not making a mistake."

    #(Vision Bonus: Day 2 Event 2, After Nanase say 'Our hands are tied'.)
    if Vision >= 10:
    
        n "Hey, how's the leg doing?"

        show NBase

        nk "My leg?"

        "She looks at her knees with a frown, then whispers."

        nk "Is it that noticeable?"

        hide NBase
        show SBase

        s "I thought so, come on Kietsu. Let's leave 'em alone for now."

        hide SBase
        show KiBase

        ki "Nanase, make sure to add him to the group chat for me, okay?"

        hide KiBase
        show SBase

        s "What group chat? Even if there was a group chat, we haven't agreed he's on the council yet!"

        hide SBase

        "They keep bickering as they walk away."

        show NBase

        nk "As long as I don't run, I should be fine. I'll just have to speed walk in gym for a while."
        nk "But, um, could you not mention it in front of other people?"
        nk "It's kind of embarrassing and I don't want everyone to start worrying about me."

        n "Yeah, no problem."

        hide NBase

        "She leaves, taking small, methodic steps as she goes. It must still hurt pretty bad, but why is she keeping it a secret?"

    return

label chapter1_day2_event3:
    play music "music/TheySay.mp3"
    scene backgroundnurse

    "I hover around the door to the nurse's office; it doesn't look like anyone's inside."
    "Well, I don't feel like I'm going to die or anything."
    "I guess I'll come back later."
    "I turn around to leave and come face to chest with one of Kazz's friends."

    show MuBase

    mu "You again? Do you need something?"

    n "Me? Nooo. Go ahead."

    "He shakes his head with a frown and brushes past me into the office."

    hide MuBase

    "Wait a minute, the nurse is gone... how is he able to get in?"

    return

label chapter1_day2_event_night:
    play music "music/WhereS.mp3"
    scene backgroundroomn

    "Another day has come and gone."
    "I try to drown out my thoughts with the tinny music on my phone, but not too far in, my mind wanders."
    "Why target Hiro?"

    scene backgroundfb1

    Dark "He was the leader of our army."

    "But he wasn't terrible. He at least tried to make an effort to call people by name, even when they couldn't respond."

    scene backgroundfb2

    Dark "He never listened."

    "As the days went by, Uitto started reporting the wounded to me."
    "He wouldn't take his headphones off and she didn't feel like fighting with him over bad news."
    "I was the strategist anyway; his duty as a recruiter had long since finished."

    scene backgroundfb3

    Dark "Something was off."

    "He never changed into the uniform we gave him."
    "All of us were still mourning Lethe at the time... but I don't think he changed his clothes at all after his first mission."
   
    scene backgroundblack
    with fade

    return

#33333
label chapter1_day3_event_morning:
    play music "music/CryingOverYou.mp3"
    scene backgroundroom

    "Uggh"
    "I have gym today."

    return

label chapter1_day3_event1:
    play music "music/CoolNights.mp3"
    scene backgroundcafe

    "P.E. is always the worst."
    "I have to change in and out of sweat soaked clothes and half the guys in my class have yet to discover deodorant."
    "After class gets out, I’m left with two options; feel gross the rest of the day or shower in public..."
    "I’m in the middle of regretting my decision at the lunch table when Uitto snaps her fingers in front of me."

    show UBase

    u "Essays! If you help Hiro with his writing assignments, I will consider that an adequate apology."

    n "Hunh? Really, that's the blackmail you're going to go with? I expected you to draw out the silent treatment a little longer."

    u "Well, Hiro's too embarrassed to ask for help and the workload is stressing him out."
    u "I'm sure if you were the one to offer a hand, he would gladly accept."

    n "I'm not letting him copy my homework again."

    u "Of course not, but you could proof read his stuff for him."
    u "You know how defensive he gets over his dyslexia and we'll be stuck writing papers for the next three years..."

    n "I hate editing."

    u "I know."

    n "....."

    n "Fine."

    "She beams that sickeningly sweet smile of hers as Jona and Hiro join us at our table."

    u "Nagen, isn't there something you wanted to say?"

    n "Uitto's blackmailing me into being your study buddy for English."

    u "Excuse me?"

    hide UBase
    show HBase

    h "Uitto, I told you I’m fine."

    hide HBase
    show JHappy

    j "Considering how often you correct Word, I think she's justified in her efforts."

    hide JHappy

    n "And just because I agreed to do something doesn't mean I'm going to lie about why I'm doing it."
    n "You are blackmailing me, and I'm not going to risk taking the blame if he doesn't want my help."

    show UBase

    u "But there shouldn't be a problem with accepting help from a friend, right Hiro?"

    hide UBase
    show HBase

    h "...No. Which means there's nothing more to talk about."

    hide HBase
    show JMad

    j "You're ly-"

    hide JMad
    show HBase

    h "Nothing more to talk about, Jona. Nothing."

    "The poor guy is getting treated like a toddler. I have to do something."

    n "Whose idea was it to put P.E. at the beginning of the day? Now half the class is going to reek and be sore all day."

    hide HBase
    show JMad

    j "The uniforms have no sleeves!"
    j "It's so freaking cold, but they won't let me wear my jacket because it's not school appropriate gym wear."

    hide JMad
    show UBase

    u "It is basically a trench coat."

    hide UBase
    show JHappy

    j "Exactly! It covers more than half of what the girls wear. How is that inappropriate?"

    hide JHappy

    "The two go on an hour-long tangent about the odd uniform restrictions, completely forgetting about Hiro. Hiro breathes a sigh of relief."

    return

label chapter1_day3_event2:
    play music "music/Sappheiros.mp3"
    scene backgroundnurse

    "I can't keep putting off going to the nurse."
    "The pain in my chest won't go away and it's started to climb up my neck and shoulder."
    "When I finally work up the courage to go to the office, I don't see the nurse, just him."

    show MuBase

    mu "What's the matter? You look pale. Well, paler than usual."

    hide MuBase

    n "Nothing, really. I'll just come back later."

    "I can hold out a little while longer."

    show MuBase

    mu "She's not going to be in for two weeks. That's why I'm here."

    hide MuBase

    n "That long?"

    show MuBase

    mu "She works for two other schools and a hospital."
    mu "I'm here to book appointments and keep idiots with colds from bothering her."
    mu "So, why do you need the nurse, you've been by the office at least three times."

    hide MuBase

    n "It's nothing."

    "I turn to leave."

    show MuBase

    mu "Shoved something in your penis or anus?"

    hide MuBase

    n "WHAT!? NO! What the hell are you writing down!?"

    show MuBase

    mu "Well, you clearly need medical help and you won't tell me what it is."
    mu "Usually when that happens, it's something sex related."

    hide MuBase

    n "That's not what's going on damn it!"

    "He looks at me expectantly, his eraser poised over the paper."
    "The longer it takes for me to answer, the more he'll think I’m lying."

    n "Just put down port care."

    "He sets down the pencil."
    "If I didn't know any better, I'd think he was concerned."

    show MuBase

    mu "Is it hurting?"

    hide MuBase

    n "Why do you care? I thought you hated me."

    show MuBase

    mu "So? I'm not a monster."
    mu "If something's wrong, I can call the nurse, but she'll want to know what's wrong with it first."

    hide MuBase

    "I reluctantly agree to have him take a look, peeling open the front breast pocket of my under shirt while he gloves up."
    "The disk embedded in my chest aches as he pushes down and around it."
    "He hisses, probably because the whole area is swollen and warm."

    show MuBase

    mu "For starters, I think it's flipped."
    mu "I can try flipping it back over by hand, but it'll hurt."
    mu "Like, a lot. Why do you have one of these anyways?"

    hide MuBase

    n "I hate needles. This made life easier."

    "With the number of drugs my father wanted to test on me, it was better to have a direct line to the heart than to dig around my arms looking for IV access in between scar tissue."

    show MuBase
    mu "I guess what I should have asked is do you still need it?"
    mu "Cause if it's broken, it'll have to come out anyway."
    hide MuBase

    "Obviously, I'd rather not touch it at all."
    "It's why I spent the last two months pretending like it wasn't there."
    "But the thought of going back under a scalpel scares the shit out of me."

    n "Please, just, try to fix it."

    "He nods and dials the nurse on speaker phone."
    "Of course, the first thing she tells him to do is grab an inch-long needle."
    play music "music/WeAre.mp3"
    "The minute I see a glimmer of silver, I feel my knees give out."

    Nurse "What happened?"

    show MuBase

    mu "I forgot to make him sit down. I'm so sorry."

    hide MuBase

    "He keeps waving the damn thing in the air as he panics."
    "When I wake up again, I have two lines coming out of my chest and an antibiotic running above my head."
    "He sheepishly informs me that the nurse will be by in two days to see me in person."

    return

label chapter1_day3_event3:
    play music "music/CosimoFogg.mp3"
    scene backgroundhall2

    "As I drop off the last of my stuff into my locker, I hear an ear shattering screech."

    show MBase

    m "Really? Like, for real for real, you'll do it?"

    hide MBase
    show SBase

    s "I can't guarantee I'll be any good at it, but if all you need is a third person, I can fill in until you find someone that wants to be a cheerleader."

    hide SBase
    show MBase

    m "Thank you!"

    hide MBase
    show SBase

    s "It's just until you can find more members!"

    hide SBase

    "So Mariko's still scraping together her squad. And with that, I get an awful idea."

    n "Have you tried asking Uitto?"

    show MBase

    m "No... Why, do you think she'd be interested?"

    "A whole bunch of manic girls chattering about school spirit and teamwork would be her living nightmare."
    "It’s also the perfect way to get back at her for earlier."

    n "I know she's looking for a club to join, but so far she's had problems finding a place to fit in."
    n "Talking to new people doesn't come naturally to her."

    hide MBase
    show SBase

    s "She does avoid the other girls in our class like the plague."

    hide SBase
    show MBase

    m "I see what you're trying to pull, Tesuta."
    m "The poor girl must be so shy!" 
    m "Don't worry, even if she doesn't join, we'll make sure she feels welcome."

    "Mwahahaha."

    n "Thanks guys!"
    n "Oh! And please don't mention I said anything about this to you guys."
    n "If she knows I asked you to talk to her, she'll think it's a prank and avoid you even more."

    m "Of course! It'll be our little secret!"

    hide MBase

    return

label chapter1_day3_event_night:
    play music "music/WhereS.mp3"
    scene backgroundroomn
    
    "My shoulder is still kinda sore, but I can rest a little easier knowing that I’m not crazy."
    "I honestly expect people to have formed a lynch mob or something by now."
    "Granted, being casually avoided doesn't feel great either, but it's better than what I expected."
    "If you had told us when we ran away we would have come here, I think Hiro would’ve been the only one to go through with it."

    scene backgroundfb4

    Dark "He couldn't sneak out."

    "A week after we ran away, we realized he only brought a few things in his backpack. He said it was because he forgot when we were leaving."
    "That's when Lethe asked if he left a note."

    scene backgroundfb5

    Dark "They made him go back."

    "He was too scared to grab his stuff, of course he didn't leave a note. I emptied out one of my pistols and lent it to him so he could feel safe."
    "Odori even checked the cylinder to make sure. The house should have been empty when he went."

    scene backgroundfb6

    Dark "He came back empty handed."

    "I tried asking him what happened, but he wouldn't answer me."
    "Everything became about saving as many of our classmates as he could."
    "He didn't want anyone to get hurt again."

    scene backgroundblack
    with fade

    return

#44444
label chapter1_day4_event_morning:
    play music "music/CryingOverYou.mp3"
    scene backgrounddorm

    "As annoying as it was, I kind of miss Kazz's broadcast."
    "It beats waking up to an empty room knowing I have to read old Shakespeare in front of everyone."

    return

label chapter1_day4_event1:
    play music "music/WeAre.mp3"
    scene backgroundcourtyard

    "I decide to eat lunch early today."
    "Jona has run off to work on god knows what and Uitto is getting chased around by the cheer squad."
    "That leaves me alone in the courtyard with Hiro."
    "He’s bouncing around, boxing his shadows, carefree as ever."

    show HBase

    h "You know what I miss the most? Fricken Naga Rangers."
    h "I've looked all over the stupid library-school thing and there isn't a single movie or comic book to be found."

    n "Probably because it's an old library."
    n "Besides, even if you found a DVD, there's nothing here that would play."
    n "The closest thing we got is the CRT TV in the junk pile on the roof and that'll only take tapes."

    h "I guess you're right. Man, this is like getting marooned on an island!"

    n "It's almost as if they want you to spend your freetime learning."

    "He turns to me with a look of pure terror."

    h "This place will be the death of me."

    n "Really? That's what rattles you?"

    h "What do you mean?"

    n "Compared to cryptic death threats, homework seems like the least of your worries."

    h "I don't remember anything about a death threat, just some coward begging for an unfair fight. I mean, seriously."

    "He laughs a bit."

    h "I'm not going to give some rando the satisfaction of scaring me. If they really wanted to face me, they should have stepped forward and said it to my face."

    play music "music/Still.mp3"

    if Villain <= Hero:

        h "I'll be fine, you guys worry too much. I don't need to be guarded 24/7."

        n "I'm not guarding you. I just thought it'd be nice to have lunch-"

        h "You've barely eaten anything though."

        "Crap, he caught me."

        n "Okay, so maybe we're taking turns shadowing you a bit, but can you blame us? I don't want you getting hurt when there's something I can do."

        h "We all made our own choices, Nagen."

        "Yeah, but if he knew everything Odori and I knew, I don't think he'd have followed along with our plans."

        h "We thought we were helping people. I'm sure everyone will understand that eventually. It's just going to be a little harder now."

    else:

        h "I wonder if it would be better to just turn myself in."

        n "What!?! No, no way."

        h "But think about it, Nagen. If we agree to meet with this person, it'll show we don't mean anybody any harm."

        n "We're not just going to roll over and let these people kick us while we're down."

        h "They're scared of us, Nagen."

        n "Not nearly enough, it seems."
        n "If they were really scared of us, they wouldn't have deigned to threaten us in the first place."
        n "No, they have to think they have some kind of edge on us. The sooner we squash it, the better."

        h "I just think it would do us some good to show our classmates we were human under our masks, just like them."

        n "You're talking like you want to quit being a hero."

        h "....."

        n "Did you let them trash your gear?"

    h "Man, this conversation got super heavy fast. I know this is a fancy boarding school or whatever, but is it so hard for us to have one normal day?"

    n "The minute I find a Monster and a console, I'll let you know."

    h "Dude, I'd take a plug and play at this point. I don't understand how they expect us to be better versions of ourselves when there's nothing to do."

    n "You could always try this."

    "I hand him a colorful novel with a Naga Ranger cover. His excitement is extinguished the moment he opens it."

    h "Aw man, it's a book-book."

    n "This place is basically a library. It's full of them."

    h "Hardy-har, Nagen, reading's only fun for you because you think it's easy."

    "What's that supposed to mean? As vast as the collection is, there is quite a number of fictional books."

    hide HBase

    "And I've even found something from his favorite series. It seems I'll have to find something else to hold his attention."

    return

label chapter1_day4_event2:
    play music "music/Lights.wav"
    scene backgroundcharm

    "I didn't think too many people would be interested in clubs, especially with so few students here."
    "Maybe that's still true."
    "Why else would my friends and I get accosted by club leaders?"

    show MhBase

    mh "Come on, you guys, this is the smartest idea I've had in a while."
    mh "But it'll only work if we have enough members."

    hide MhBase
    show UBase

    u "I don't think anyone will join if we're in your club, no offense."

    n "Why don't you ask some of the Charisma Majors?"

    hide UBase
    show MhBase

    mh "I already tried, but they hear 'gaming club' and think it's for dorks."

    hide MhBase
    show HBase

    h "Gaming? Like video games?"

    hide HBase
    show MhBase

    mh "I asked the teachers if I could bring my old GameStation collection, y'know, since it predates the internet."
    mh "They said yes, if I share it with club members."

    hide MhBase

    h "What games do you have?"

    "Before Momoko can seal the deal, Chisei bellows from down the hall."

    show ChBase

    ch "Hark, deceiver!"

    "She’s not terribly fast, but she makes up for it by shouting as she walks."

    ch "You promised a fair duel."
    ch "I thought such trickery was beneath you."

    hide ChBase
    show MhBase

    mh "This isn't one of your plays. All's fair in love and war, baby."

    hide MhBase
    show UBase

    u "Don't we get a say in this?"

    hide UBase
    show MhBase

    mh "I just need names to put on a paper. You don't even have to show up. It's the least you could do."

    hide MhBase
    show HBase

    h "What's that supposed to mean?"

    "Oh no. That's not good."

    hide HBase
    show MhBase

    mh "What, I'm not allowed to bring up that you're a criminal at all now? It was just a joke."

    hide MhBase

    h "I'm not a criminal!"

    "Chisei joins our group slowly, although much more hesitant than before."

    show MhBase

    mh "My guy, you put mind control devices on people, that's gotta be a crime. Just own it."

    hide MhBase
    show HBase

    h "We were trying to protect people."

    hide HBase
    show MhBase

    mh "Yeah, we all felt really protected wearing bombs. Just ask Chisei."

    hide MhBase
    show ChBase

    ch "Please do not."

    "Our eyes are collectively drawn to her scars."

    n "We didn't- There shouldn't have-"

    hide ChBase
    show MhBase

    mh "They tried to take it off by force aaaand boom."

    hide MhBase
    show ChBase

    ch "I said stop!"

    hide ChBase
    show MhBase

    mh "...But everyone already knows."

    hide MhBase
    show ChBase

    ch "Our time here should not be defined by our scars or misplaced guilt."
    ch "And if I hear you trying to use other people's lives as a weapon in an argument, I-"
    ch "Well I do not know what I can do, but I will most certainly sever my connection to you."

    hide ChBase

    "I don't think I've ever seen Chisei this angry before."
    "Momoko apologizes, but there’s little she can say to pacify her."
    "Honestly, I’m mostly in shock and I can sense the others were as well."
    "The Education Collar was never meant to do that kind of damage. There shouldn't have been anything in it that could do that."

    show HBase

    h "What club are you running?"

    "Leave it to Hiro to just side step around a heavy topic."

    hide HBase
    show ChBase

    ch "You do not have to ask just because you feel sorry for me."

    hide ChBase
    show HBase

    h "You're a writer aren't you? Is it a reading club or something?"

    "He soldiers on, and eventually her mood lightens."

    hide HBase
    show ChBase

    ch "No, a drama club."

    hide ChBase
    show HBase

    h "So you need actors and junk? I could do that, if you actually want me in your club."

    "She pulls out a crumpled piece of paper from her backpack."
    "All things considered, it seems she has more than enough people to form her club."

    hide HBase
    show ChBase

    ch "We do not have a set meeting time yet, but I would like to accommodate everyone's schedule if I can."

    hide ChBase

    "She collects his signature and leaves with a small smile on her face."

    show JDepressed

    j "Were they only interested in Hiro? I guess some things never change."

    hide JDepressed
    show HBase

    h "What do you mean? We're all going to join again, aren't we?"

    hide HBase
    show JFrustrated

    j "Do I want to repaint the same sets over and over again? Not for free."

    hide JFrustrated
    show HBase

    n "I was never in drama club to begin with. It was just you guys."

    h "I guess we just used to talk about it a bunch..."
    h "Right!"
    h "You had that weird performance anxiety thing."

    hide HBase
    show UBase

    u "Pfft."

    n "SOCIAL anxiety."
    n "Thousands of eyes, all pointed at you, actively judging every syllable you say. Not for me. I get enough of that at home."

    hide UBase
    show HBase

    h "Whatever, point is you clam up in front of a crowd."
    h "I guess it's just me and Uitto this time."

    hide HBase
    show UBase

    u "Actually, I'm with Nagen on this one."
    u "I'm not just retiring from the pageant circuit, I'm retiring from performing entirely."
    u "One of the reasons I'm here is the school can't use me on the stage or in photos."

    hide UBase
    show HBase

    h "Oh... So it's just going to be me?"

    n "It'll be okay. By the time they want to meet up, we'll have caught your anonymous attacker."

    h "That's... okay, I guess."

    hide HBase
    show UBase

    u "You'll be fine, you'll see!"

    return

label chapter1_day4_event_night:
    play music "music/Nostalgia.mp3"
    scene backgroundroomn

    "Over the last few days, it’s felt like things are almost normal now."
    "At least, for me it feels normal."
    "None of the kids really wanted to hang out with the 'teacher's pet'."
    "The things I wanted to talk about didn't make sense to other kids and I couldn't figure out how to find common ground."
    "It's why I was so jealous of Hiro when we were kids."
    "He didn't have to try to make friends. He just had them."
    "I lashed out so much back then."

    scene backgroundfb8

    Dark "He never fought back."

    "No matter how much I fought or yelled, he'd just smile at me like whatever we were fighting over wasn't a big deal."
    "It frustrated the hell out of me that I couldn't shake him."
    "Our arguments got so bad, the school had to get involved."

    scene backgroundfb9

    Dark "I watched him drive off with his dad."

    "That night, he had called me, asking for my help fixing something."
    "I don't know why Odori gave him my number, but I had the upper hand for once."
    "I'm ashamed now at how long I let him dangle."
    "How could I have known?"
    "All he asked for was a needle and thread, I didn't know why it was so urgent that I met up with him."
    "I thought he ripped his pants or something."

    Dark "He never told me what happened."

    scene backgroundfb11

    "His face... it was unrecognizable."
    "He wanted me to give him stitches, like I'd seen in a documentary, but bones were broken."
    "We should have gone to the ER, but he was afraid of getting in trouble."

    h "It'll heal. It always heals, but if things aren't in the right place, it'll heal wrong."
    h "I can't do it myself this time, it's kinda hard to see right now."
    h "Please, you're the smartest person I know."

    "I couldn't convince him to see a doctor, so I did the best I could."
    
    scene backgroundblack

    "It's my fault it didn't heal like it should."
    "By the time I was finished, I was shaking, but he just laughed."

    h "I can't keep getting into fights at school, Nagen."

    Dark "It's the only scar he has."

    "By Monday, all that was left was a gash where the stitches hadn't lined up quite right."
    "No one at school thought anything of it when he said he fell."
    "I wonder how often he got hurt and we just didn't know."

    scene backgroundblack
    with fade

    return

#55555
label chapter1_day5_event_morning:
    play music "music/CryingOverYou.mp3"
    scene backgroundroom

    "For the first time since school began, I wake up to the radio blaring at top volume."

    kk "Good morning, amibros!"
    kk "That’s right, we're back on the air!"
    kk "Thank you to everyone who sent in requests while we worked out the kinks."
    kk "It's going to take me a while to go through all of them, but I promise I'll do my best to get to each one."
    kk "Starting us off, we've got a request from the heart. 'Hurt' by Midday Maniacs."

    "I drag myself out of bed and remind myself it's just one more day of classes before the weekend."

    return

label chapter1_day5_event1:
    play music "music/TheLoyalist.mp3"
    scene backgroundhall1

    "I’m on my way to lunch when I catch Kitsune in the halls."
    "She has her locker wide open with an assortment of compacts at her feet."
    "She keeps pulling at her bangs and making wild faces in the mirror."
    "Maybe I could sneak past her if I just-"

    show KBase

    k "Nagen..."

    "Damn it."

    k "Do you think I'm pretty?"

    "Her voice doesn't carry the same saccharine tone it usually holds."
    "Still, growing up with Uitto, I've come to recognize a loaded question when I hear it."

    n "Why do you want my opinion?"

    k "I assumed you like girls and I feel like my makeup is making my face look gross, but I don't know how to fix it."
    k "So then I thought maybe it's all in my head and I actually look fine."

    n "You could always not wear makeup."

    k "My hair's white. If I don't at least fill in my brows, I look sick."

    "She sighs."

    k "I'm supposed to have pictures taken today. Does it really look that bad?"

    n "I didn't say it looked bad."

    k "No, but you didn't answer my initial question either."

    "She bends down and picks up her discarded makeup, muttering something about needing more highlighter."

    n "You're not ugly."

    "She smacks the top of her head on the locker as she stands."

    k "-stupid platform lady-stilts."
    k "What kind of vague nonsense are you trying to pull here?"

    n "That's why I asked if you really wanted my opinion."
    n "I don't think you're ugly, which is why you shouldn't be fishing for compliments."

    k "I wasn't-"

    "She cuts herself off, unable to think of a reasonable defense."

    k "Okay, so maybe there was a bit of coaching on my part. What else am I supposed to do, let people ignore me?"

    "She slams the door to her locker shut."

    k "I did not spend this much time getting ready just to fade into the background."
    k "Ugh! I can't be bummed like this or it's going to show up in all my headshots."
    k "Thanks anyway, Nagen."
    k "I gotta go get my manic pixie energy back. Good luck today."

    hide KBase

    "She runs off down the hall without a backpack or anything."

    n "Thanks... I think."

    return

label chapter1_day5_event2:
    if Vision >= 10:
        play music "music/TheySay.mp3"
        #[BG: Courtyard]

        "I still have a little time before lunch. For some reason, there’s something bothering me about the cheerleaders."
        "Rei might still be mad at me, so my best option is Setsuna."

        show SBase

        n "Hey, you joined the cheerleaders, didn't you?"

        s "Kind of. It's just until they find people who want to join."

        n "Did she have you pierce your ears?"

        s "...Yeah. Why?"

        "She shows me her fresh piercings; a bright red star within a glittered bead."
        "Inside was a pinpoint dot that easily could be mistaken for the stem of the earring."

        n "Your ears were already pierced, why didn't she just hand you a pair?"

        s "She insisted. Besides, I thought it would be cool to have another set."
        s "It was like, a right of passage or whatever. I can always take them out in a few weeks once they've healed."

        n "DON'T!"

        s "Hunh?"

        n "Whatever you do, don't take those out. How many girls did she pierce with that thing?"

        s "I don't know, at least the whole team. A few chickened out halfway through."
        s "Why? Did someone get an infection or something?"

        n "No, not exactly. It's just a gut feeling I have... do you think you can get that piercing gun to Nocturn?"

        s "...Who?"

        n "Professor Yaguchi."

        s "I already told him about it, but yeah, I can see if I can confiscate it. What's gotten into you?"

        n "What do you mean?"

        s "You're acting like we're friends. I mean, we've known each other less than a week."
        s "You didn't seem the type to be so... familiar."

        n "I'm just... trying my best to be a good student council president."

        "I can't explain exactly why, but I feel like she's someone I can trust to look into this."
        "At least she seems to buy my excuse."

        n "Thanks for hearing me out."

    return

label chapter1_day5_event3:
    play music "music/CoolNights.mp3"
    scene backgroundcharm

    show UBase

    u "NAGEN!"

    "Uitto storms toward me as soon as the bell rings."

    u "Why are there a bunch of go-go juice girls trying to be besties with me all of a sudden!?"

    "Uh oh."

    n "Mariko, that backstabbing rat. She said she wouldn't say anything."

    u "...you asked the head cheerleader to be friends with me?"

    n "Wait, if she didn't tell you, then who?"

    u "Rei. She was just 'so excited' that I had taken an interest."
    u "And I could take 'as much time as I need' getting to know everyone on the team."
    u "She tried to put a friendship bracelet on me!"

    "I really shouldn't laugh, but I can't help it."

    u "It's not funny!"

    n "You're right, I'm sorry."

    u "Then quit giggling."

    n "I- You gotta stop looking at me like that first."

    u "And here I was almost touched that you were worried about my social life."

    n "Come on, how is this any different than you piloting Hiro around the school?"

    u "Because- look, I may make light of stuff, but I'd never..."
    u "I wasn't trying to make fun of him, I was trying to help."
    u "Why'd you even bother asking them to be friends with me?"
    u "You trying to get rid of me or something?"

    n "What? No."

    u "Good. I don't need friends other than you guys anyway."

    "She always says stuff like that, but that was when she still had Odori to rely on."
    "Lately she seems to be pushing everyone away indiscriminately."

    u "Hey now, don't go looking at me like that. Quit thinking about sad shit."

    n "When's your cheer uniform coming in?"

    u "Don't push it, Tesuta."

    if Vision >= 10:
        n "Did they pick out a set of earrings for you too?"

        u "Ugh, they tried, but they're so not my style."
        u "Besides, they have this weird right of passage thing where they do the piercing themselves."
        u "I saw what happened when Jona pierced your lip; no way I'm letting an amateur anywhere near my ears."

        n "If you didn't get them, then how..."

        u "How what? How'd I wear earrings as a kid?"
        u "Clip ons or super glue; sometimes both."
        u "You're not the only one who hates needles."
        u "I'm just a better fighter than you. Why'd you want to know?"

        n "I just could have sworn you had piercings."

        u "...Nagen, I can't believe I'm saying this, but your memory's wrong. See for yourself."

        "Sure enough, there’s not a single hole."

        u "Are you feeling okay?"

        n "I have been feeling kind of sick lately. Maybe I've been spiking a temp without realizing it."

        u "Maybe you should get some rest."

        "Never in a million years have I misremembered something. What's wrong with me?"

    n "Are they being nice to you at least?"

    u "...Yeah, annoyingly so. At least I know you set them up to it instead of some ulterior motive."

    hide UBase

label chapter1_day5_event4:
    play music "music/Interloper.mp3"
    scene backgroundcafexn

    "Jona and I are on the way to the cafeteria when we run into Uitto."

    show UBase
    
    "She seems scared."

    u "Where's Hiro?"

    hide UBase
    show JRelax

    j "He's supposed to be with you. You're the one that shares last period with him."

    hide JRelax
    show UBase

    u "I know that, but he didn't show. I thought he ditched class to hide with you guys."

    "I haven't seen him all day. I just assumed Uitto had been with him instead."
    "Unease settles into my stomach as I dial his number on my burner phone. No answer."

    n "Did that idiot really try and turn himself in?"

    "Uitto goes pale."

    hide UBase
    show JRelax

    j "I'm sure someone has seen him. Before we panic, we should try finding him first."

    hide JRelax
    show UBase

    u "Right, we'll cover more ground if we split up. Whoever finds him should call the others."

    hide UBase

    "Before I can get a word in, they run off. By now, he should be at the field where we were supposed to surrender."
    "The question is, who's behind this?"

    return

label chapter1_day5_event_night:
    play music "music/TheySay.mp3"
    scene backgroundroomn
    
    u "Knock, knock! Ready for 'movie' night?"

    "Uitto’s carrying her pillow under her arm and a few bags of chips in the other. She looks like she’s ready for bed."

    u "Jona found one of those retro TV's with the tape thingy-"

    j "Tape deck."

    u "Whatever it's called, it's built in. We thought we could have a little slumber party, like in the old days."

    j "I'll change later. I can't sleep in clothes that have outside smell on them."

    h "A sleepover, seriously?"

    j "It'd be unnerving to sleep by yourself after everything that happened, don't you think?"

    n "It couldn't hurt."

    h "But you guys could get in serious trouble if they catch you, especially you, Uitto."

    u "There's no rules about sleeping in someone else's dorms."

    j "Not yet."

    u "And we plan on taking full advantage of that loophole."

    u "So come on, Nagen, let's head to your room, this stuff's getting heavy."

    n "My room?"

    j "It's already clean, isn't it?"

    n "...Yeah."

    h "Alright, yeah, let's go!"

    j "...You don't want to grab a change of clothes?"

    h "...No? All my stuff can double as sleep clothes."

    h "Why wear anything else when you can be comfortable all the time?"

    n "You're the only human being alive that's comfortable all the time."

    "Everyone crams themselves into my tiny dorm. Because, of course, after only a week of being here, I have the cleanest room."
    "We fight to find an outlet for the TV, opting to balance it on a pile of textbooks so everyone can see."

    h "We'll get the spooky tape out of the way and then have fun, right?"

    u "Of course, no ending the night on a bummer."

    j "No bummers!"

    scene backgroundstatic

    "I slide the tape in and watch as static peels away to reveal a grainy image of a familiar logo."

    q "Mariko Genki, your bravery during the riots has not gone unnoticed. We would like to give you the support to protect the people you care about most."
    q "All you have to do is help us eliminate a loose end that threatens our operation. You deserve to be recognized as a true hero."
    q "We know you'll make the right choice. Sincerely, Apex of the Karmic Gladiators."

    "The video is consumed by static once more."

    scene backgroundroomn

    h "...the Karmic Gladiators sent her? Why!? We were junior heroes for them."

    n "The DVP is busy rounding up Lethe's old pawns, which means this could have come from the members who opposed her or..."

    u "Or her allies that think we turned on them to get out of trouble."

    j "Which we kind of did."

    "None of that explains how they found us, or why they didn't target us directly. And that name..."

    n "I don't remember her ever mentioning an 'Apex'. Did any of you know a hero by that name?"

    u "No, but they could have changed their name after the media turned on Lethe."

    u "It's not uncommon to rebrand after a scandal."

    j "Or maybe it's a title? Like captain or boss?"

    h "A new leader that doesn't like us... that can't be good."

    play music "music/VHS.mp3"

    "The tape sputters and then a curtain displays on the screen. Slowly a girl, suspended by ribbons, is lowered into the frame."

    play music "music/#28.mp3"

    scene backgroundC1_4

    if Villain > Hero:
    #[If Villain]
    
        a "Hello, my lovelies. If you're seeing this, then that means my first champion failed. Well, I guess she's not much of a champion anymore, is she?"
        a "It takes more than a kind heart to be a true hero, I suppose. We need more heroes; brilliant beacons that act as ideal examples of who we should be."
        a "It feels like, somewhere along the way, we started to abandon those ideals in favor of more 'interesting' role models."
        a "Well, look where that's gotten us. We've tolerated awful, toxic people for so long for the sake of entertainment."
        a "Bad guys think they get to be heroes just because they tell us they are. Well, no more! I'm going to start over, with new heroes, better heroes."
        a "Once they've proven to me they can face injustice head on, they will be welcomed as the true guardians of Valhalla."
        a "As for you... Well, if you truly regret the harm you've caused, you'll accept your punishment with dignity."
    else:
    #[Move to Main Branch] 
    #[If Hero]
        a "Hello, my lovelies. Congratulations are in order."
        a "After all, you brave young heroes just fought your first villain!"
        a "I should have known that broken thing was unsuited for the job. I do hope it was a little fun for you at least."
        a "Think of her like a salad, a promissory note of more to come. With everyone so out of practice, it's only fair to start small."
        a "How I long for the days when costumed heroes and villains could battle for dominance in broad daylight."
        a "All this sneaking around that has to be done now, just to keep others from intervening, it's demeaning to both of us."
        a "One day, there will be a place where real heroes receive the respect they deserve."
        a "I wonder; will you ever be worthy of Valhalla, or will my champions steal your places in paradise?"
        a "After all, if you can't figure out how to entertain me, you're of no use to anyone."

    #[Move to Main Branch]
    #[Main Branch]
    
    a "For now, false heroes, I bid you adieu. ...oh, and Mariko, since you're watching this too."
    a "Just know, there's a lot of people counting on you to fail."
    a "Au Revoir."

    scene backgroundstatic

    play music "music/VHS.mp3"

    "She disappears behind the static. We sit there drowning in white noise for a few moments before Uitto turns off the TV."

    play music "music/INeedTo.mp3"

    scene backgroundroomn

    u "'False Heroes', just who does she think she is?"

    h "She kept saying 'they', does that mean there's going to be more threats?"

    n "...it's entirely possible, but we're not going to get any answers stressing out about it tonight."

    play music "music/WeAre.mp3"

    u "Right!? This could be the only night we get away with this, so we gotta make the most of it!"

    j "I've got puzzles, games, old DnD stuff, and a bunch of old sci-fi movies."

    h "Please tell me you got Were-Sheep. I need a good laugh right now."

    j "Of course."

    u "Put it on, put it on!"

    n "That barely qualifies as sci-fi, but if you must subject me to bad movies, I guess that one's passible."

    h "Wooton!!!"

    "We marathon B-grade movies long into the night. The next day, we find out that Mariko won’t be coming back to class for a long time."

    scene backgroundC1_E

    g "Chapter One End"

    return