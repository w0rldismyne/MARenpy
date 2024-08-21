label JonaVisit:

    if jTurn == 0:
        jump Jona1
    elif jTurn == 1:
        jump Jona2
    elif jTurn == 2:
        jump Jona3
    elif jTurn == 3:
        jump Jona4
    elif jTurn == 4:
        jump Jona5
    else:
        jump JonaF

label Jona1:
    scene backgroundcafe

    "I find Jona sketching in the corner of the school’s cafe. At this point, it’s safe to say he lives here more than his dorm."

    n "Hey."

    j "....."

    n "Are you mad at me too?"

    j "Inking."

    n "...I’m sorry, what?"

    "He sets down his pen and leans back in his chair with a hefty sigh. His arms go limp at his sides."

    j "I can’t talk and ink at the same time. It ruins the quality of the lines."

    n "What are you working on anyway?"

    "I try to get a look, but he slams the notebook shut."

    j "Just some sketchbook assignment my guardian gave me to ‘get to know me better’."

    n "You’re putting more effort into it than I would. Are you being graded on it or something?"

    j "No... At least, I don’t think so. She’s an art teacher, so it’s possible. I just figured I’d make it look nice since she wants to see it."

    n "I just don’t understand how Maimai thinks she can swoop in with this ‘mom’ person and it’ll erase everything. Sure, she’s nice to me, but she’s still a known killer. It’s weird, right?"

    j "......"

    n "She keeps messaging me asking how school is."
    n "She has nothing to gain by putting on this act. I don’t know what to do."

    j "I don’t know, unless you want to avoid her. That would be the easiest way to handle it."

    n "Like I said, she seeks me out, man."

    j "Can’t relate."

    "He opens a large pot of ink and splatters the paper."

    j "Mrs. Miki doesn’t talk at all and my mom liked her space."
    j "She was like a curled up spider, you wanted to poke it to see if it was alive, even though it would hurt you."

    "He shakes his head. I had the misfortune to meet his mom once. It was on a day he was supposed to go to the doctor and he forgot to go straight home."
    "I’d never seen someone so unkempt before, it was like she left her hair in a ponytail twenty-four seven."
    "She brutally chewed him out in front of all of us and said our ‘stupid’ club was a waste of time."
    
    n "Really? She seemed so possessive, I assumed she was some helicopter parent. I mean, mine were-"

    "He starts laughing his ass off."

    j "Her? Hover? The only reason she got that mad was when I inconvenienced her."

    n "Inconvenience her how?"

    j "It was a pretty long list. Some things contradicted each other."
    j "Like I wasn’t supposed to have friends at the house, but I was supposed to have, and I quote, a ‘social life’."

    menu:
        "Sounds like my mom.":
            $ jRep -= 1

            j "...how?"

            n "My mom wanted nothing to do with me. I saw her once before she started teaching our class. She had to tell me who she was."

            j "But they didn’t share any of the same colors. Mrs. Tesuta was callus and distant, but she never got mad. Believe me, I tried, she was unshakeable."

            n "You don’t think that was weird?"

            j "Super weird, but that’s what I’m saying. Mrs. Tesuta was weird, mine..."

            "It looks like he’s having trouble finding the words."

            j "She was like Lethe, only she didn’t stop fighting until I left."

            n "What’s that supposed to mean?"

            j "If you don’t get it, then either you don’t want to or you’re trying not to think about it. Either way, forget it."
        "And when she was happy?":
            $ jRep += 1

            j "I never saw her happy. I’d see her smile, but you can’t be happy with a gray or green aura. It just means you know how to fake it."

            n "What’s a green aura?"

            j "Anger... I think. People are hard to decode and I don’t have a handbook, so I have to go by actions."
            j "People yell and hit things with a green aura, so anger seemed likely."

            n "And gray?"

            j "...it’s a curse."

            n "...what?"

            j "It’s like the black spot, a permanent stain on the soul up until death. It’s opaque and masks other colors, bleeding into other emotions."

            n "That’s terrifying."

            j "The only way to get rid of it is with an equally powerful emotion. Anger’s easy to trigger, but it never lasts, and the gray creeps back..."
        "Why'd you invite us?":
            $ Charm += 1

            j "I’d rather get yelled at than be in the house alone day after day. Didn’t matter anyway, everyone always declined."

            n "Hiro had to take care of his dad and I was a walking lab rat, we didn’t exactly have a choice."

            j "I’m not mad about it. I get everyone was busy with their own things."
            j "I ended up working on the sets for the theater since they’d stay open late."
            j "I wouldn’t have access to the tools I needed for my inventions without them. So it all worked out in the end."

            n "Still, I wish we could’ve done more stuff together when everything was normal."

            j "You can’t focus on the past like that. It’s not like you can change it. You’ll only make yourself miserable."

            n "...I guess."
    $ jTurn += 1
    $ Charm += 1
    
    j "I wonder if they’re contagious, the negative emotions people have. Can people catch them like a virus?"

    n "Well, laughter and yawning are contagious, I suppose people’s moods could work the same way."

    j "Then that would make me a carrier, wouldn’t it?"

    n "Of what?"

    j "Nagen, so many people I know have gray auras. First my mom, then Lethe, and now the people closest to me."
    j "I’m not entirely sure how it works, but I know it’s a bad omen."

    n "It doesn’t work that way. It’s not an actual virus, it’s just human emotions."

    j "People have died from lesser things."

    n "That’s pretty cryptic."

    j "Sorry. I just don’t like not knowing how to fix things. All these people problems are way too complicated and it’s frustrating."

    n "I know the feeling."

    j "Just promise me you won’t go gray on me."

    n "I’m not really sure what that means."

    j "....."
    j "I don’t know. Whatever you’re doing right now seems to work, so, more of that."

    n "Okay dude, I promise."

    return
label Jona2:
    scene backgroundamp

    "I haven’t been able to find Jona in any of his usual haunting grounds."
    "Suddenly, a large clatter sounds from behind the theater stage. I can hear someone rooting around in the garbage. It can’t be..."
    "I follow the sound and sure enough, my childhood friend is dumpster diving."

    n "Dude! Seriously?"

    "The poor sap startles and hits his head on the lid."

    j "Don’t sneak up on me like that!"
    j "...how did you sneak up on me? I have, like, three trip wires around here."

    "Or when he’s not the one to plant them."

    n "What do you think you’re doing?"

    j "Well, they won’t let me leave campus to comb the junkyard, so this is the next best thing. Not a lot of stuff to go through, unfortunately. These people are hornier for recycling than I am."

    n "...uh hunh, right. And why do you need garbage?"

    j "Not garbage, junk. Junk is cleaner."

    n "But why?"

    j "I felt like making something for myself today to pull me out of this funk. Nothing’s better than trying to make something with found objects! All my best pieces started that way."

    n "Right... so this is a thing you do routinely?"

    j "Used to. I’d spend all my summers hanging out in the junkyard building stuff. Other people do it too, it’s not that weird."

    n "No, no I get that. It’s just... you’re in a dumpster, dude."

    j "It’s not like there’s rotten food in here, or at least there shouldn’t be."
    j "Have you seen a baby around here? I think I found a diaper."

    n "Get out of there, man."

    j "Wait for it... Ah hah!"

    "He leaps out with something in hand."

    n "What is it?"

    j "It’s a music box!"

    "He proudly displays a dismembered porcelain ballerina atop a glass case."

    j "It still works too!"

    "He winds up the machine. A warped melody is released from the contraption."

    j "It might need a new comb, but that’s an easy fix."

    menu:
        "Throw it away":
            $ jRep -= 1

            n "It was in the trash for a reason."

            j "It was in the trash because no one wanted it."

            n "That’s a reason, isn’t it?"

            j "Just because one person doesn’t see value in it, doesn’t make it worthless. That’s not a good reason to just throw it away with a bunch of broken wood."

            n "If I look  in your room, am I going to find a bunch of useless shit in there?"

            j "...you will with that attitude."
            j "What’s gotten into you lately? You never used to care this much about what I’ve been up to."

            n "All that shit you were talking about earlier, being quiet all of the sudden; it’s gotten me worried."

            j "I’m worrying you? By doing what?"
            j "Last I checked, you were the one poking the hornet’s nest that is the hierarchy of high school."
            j "We’re a bunch of weirdos and freaks, what makes you think you can win a popularity contest?"

            n "I just don’t think holding onto all this junk is healthy."

            j "I didn’t ask for your opinion about how I have a shitty hobby. You could be joining me, but like always, you have to fixate on the negative."
            j "Out of the two of us, you’re the one who holds onto useless junk."

            n "Big talk coming from someone in a dumpster."

            j "I know where I belong; do you?"

            "I’m going to end up fighting in the garbage if I’m not careful. Just where does this asshole get off insinuating that I’m pessimistic?"

            j "You’re doing it again. I forgot how fragile your ego is."

            "He won’t be so smug when his stupid mask is shattered against the pavement."

        "Why that?":
            $ jRep += 1

            n "If you’re looking to build something, wouldn’t the scrapped set pieces be more useful?"

            j "If I wanted to start from scratch, yeah. But I don’t have a lot of room to work with. I was looking for something to brighten my dorm with."

            "That makes a little more sense."

            j "I tried to make one when I was younger. They have all these intricate moving parts, but you rarely see them under all the extra pieces."
            j "I don’t really know how to make music, they were more noise machines than anything else."

            n "I could’ve looked something up for you. All it takes is copying music onto a metal sheet. That’s well within my skill set."
            n "Even if I can’t make something, I can replicate it. At least, in theory."

            j "I suppose that’s all we’re good for, copying things that already exist."

            n "Way to trivialize my life’s work, pal."

            j "Sorry. I just wish I was more original. It’s not that I don’t try, I just don’t have that spark of inspiration other folks seem to have. In the end, I always fall into old habits."

            n "And one of those is digging through other people’s garbage."

            j "Funny. Like I said, I’d normally go to a junkyard where everything’s organized. This is more necessity than anything else."
        "You could buy a new one":
            $ Charm += 1

            j "You’re kidding, right? Do you know how expensive these things are?"

            n "It’s just a toy."

            j "Toy’s aren’t typically made of glass. At best, it’d be around three hundred dollars, but judging by the materials used, it’s closer to a couple thousand."

            n "No way."

            j "This place used to be a library, right?"
            j "I bet it got broken during the renovations and some worker assumed it was ‘just a toy’."

            n "I’m looking this up, there’s no way."

            "I hate being wrong. Why is the internet out of my reach at a time like this?"

            n "How could you tell just by looking at it?"

            j "I grew up with old people. Old people love retro collectible stuff. You’ll start picking up an eye for this kind of stuff too the longer you live with Ando."
            j "Rich people are big on tradition."

            n "What are you going to do with it?"

            j "Probably restore it. Or try to at least. The ballerina will have to stay as is. Besides, it gives it character."
            j "It’d be a shame to erase everything that made it unique."
    $ jTurn += 1
    $ Charm += 1

    j "I don’t like deception and all the messy things that come with it. With machines, the right answer is clear. Either it works or it doesn’t."
    j "People are more nuanced. It’s annoying."

    n "You’re preaching to the choir here, but where’s this coming from?"

    j "People have been asking me to change lately, a lot. And I get it, the I dress won’t get me a decent job blah, blah, blah. But it’s other things too."
    j "I just don’t know where the line between compromise and lying about who I am is."

    n "I am literally the worst person to go to about this kind of thing."

    j "Really? But you’re so good at it."
    j "It doesn't matter who you’re talking to, you just adapt into the role they need you to fill."

    n "That’s more reflex than anything. Most of the time, I feel like I’m on autopilot, but I’m still me."
    n "It’s not like I completely change for other people, I just mimic their social... behaviors? Rules? I’m not sure. Like I said, reflex."
    n "You grow up having to parade yourself to adults, you figure out real quick how to filter yourself."

    j "I see... So if you pretended to be someone else, even though you’re still you, that’s different from adapting to make people happy?"

    n "Yeah, I guess. Look, can we take this conversation to the cafe? I feel weird having a conversation with someone standing in a dumpster."

    j "Oh, right. Just give me a moment, I’ll catch up."

    "I get up to leave, but I’m sent sailing into the dirt by one of his trip wires."

    j "I knew I put a trip wire there!"

    n "Next time, no tripe wires. Hiro and I can stand watch if you really need to paw through garbage again."

    j "Not garbage, junk."

    "I don’t think we’ll ever fully agree on the matter, but at least I can convince him to forgo booby-trapping the dumpsters. For someone so harmless, he can be a real handful."

    return
label Jona3:

    scene backgrounddorm

    "Jona invited me to hang out in his dorm room while he works on fixing up the old music box we found."
    "His room looks more like a workshop with all the disassembled junk he had strewn about."
    "While poking around his collection, I find a half finished 3D puzzle to mess around with."

    j "Have you thought of where you’re going to when we graduate? Not job wise, but literally where you’re going to live?"

    n "I try not to dwell on it much. Mr. Ando’s fine with me staying so long as I’m invisible to him. Though I’ll probably be kicked out after that."

    j "Maimai won’t let that happen, she cares about you too much to leave you alone on the street. She’s weird like that."

    n "True."
    n "Why do you ask?"

    j "The situation with my guardians is... complicated."
    j "I know I don’t fully understand sign language, but they’re definitely hiding things from each other, and I’ve tried not to get involved."
    j "I don’t think I can avoid it much longer."

    n "What, do you think they’re cheating on each other or something?"

    "He fumbles with his tools. What an odd thing to get flustered over."

    j "What? No, no it’s something else. Ms. Miki had shown me a bunch of old pictures of her family."
    j "I guess she had this kid brother that went missing when he was four."

    n "...that sucks."

    j "We look a lot alike."

    n "Oh. Oh shit-"

    j "Not me, we have different eye colors, I checked."

    n "Dude, don’t scare me like that."

    j "It would have been crazy if it was true though, almost like a fairytale. To find out I secretly had a big sister that was missing me while I was living somewhere else."
    j "She’d be so happy to be vindicated after years of fruitless searching... Wearing color contacts doesn’t hurt, does it?"

    "He can’t seriously be thinking of conning this woman, is he?"

    menu: 
        "Be yourself":
            $ jRep += 1

            n "Don’t do it."

            j "Do what?"

            n "Don’t buy contacts so you can look more like this lady’s brother. She’s going to find out you’re lying and it’s going to be a disaster."

            j "But what if I was really careful-"

            n "It’s not going to work. Trust me, you do not want it to work."
            n "Imagine having to lie twenty-four seven, never being able to relax, just because someone’s crazy enough to believe it. It’s not worth it."

            j "It’s not like I’m that important to being with. If it brings someone back from the dead and makes people happy, why does it matter that it’s a lie?"
            
            n "There’s no way that’s your only motivation."

            j "So I might benefit a little too, that means everyone wins."

            n "And if your ‘sister’ isn’t cool with hanging out with your old murder buddies - me - what are you going to do?"
            n "You can’t just ditch her after building up an elaborate lie like that. It would kill her all over again."

            j "It’d be better than trying to figure out what I’m going to do on my own."
        "You'd need more than contacts":
            $ Charm += 1

            n "If you’re serious about pulling this off, you need to do serious research on her family, her parents, as far back as you can go."

            j "I barely remember anything about when I was four, why would someone else?"

            n "I can."

            j "....."

            n "Point taken. Either way, if he’s got weird allergies or phobias, you’re going to need to know."

            j "This is starting to sound really complicated."

            n "Stealing someone’s identity usually is. Most catfishes are protected by the internet, you’re going for real life on a continuous basis. It’s going to be difficult."

            j "Who said anything about stealing? This was practically given to me, I’m just trying to figure out if I want the part."

            n "You should figure that out soon. There’s only so long you can keep your goggles on."
        "They're pricey":
            $ jRep -= 1

            n "You got sixty bucks to spare?"

            j "Th-that much?"

            n "For convincing ones? At least sixty?"

            j "Who has that kinda money laying around for that kind of stuff?"

            n "You could get a part time job."

            j "Those rarely work out for me. They always want me to take off the mask and goggles, I won’t be able to convince them to leave it, and I inevitably get fired."

            n "Is keeping that junk worth getting fired over?"

            j "I get overwhelmed by all the people staring. Pretty sure I have tan lines from weaving them all the time."

            "It has been a couple years since started hiding his face like that. I wonder..."

            j "Please stop looking at me like that. I’m not taking them off."

    j "There has to be something easier I can do. We only stay in the dorms for a short while, I’m really not looking forward to heading back in the winter with all the tenseness."

    n "Have you thought about talking with ‘chairwoman’ Amagi?"

    j "Are you crazy? I’m pretty sure she hides lasers or something behind those stupid spectacles."
    j "We’re nothing but pawns to her. She’d never acknowledge my existence, let alone talk to me."

    n "Well, yeah she’s an insufferable bitch, but when I met her, she did nothing but talk about how right she was. It should be easy to find out what she’s fighting about that way."

    j "I guess..."

    n "I mean, what’s the worst that could happen?"

    j "I get passed around the foster system like a rotten potato until I turn eighteen or end up in juvie."

    n "You just have to be really careful."

    j "Or I could mind my own business and wait for it to pass."
    j "Not everything gets better by poking your nose into other people’s business."

    n "You were just talking about doing just that."

    j "Th-that was different. I was just speculating, you’re the one coming up with the ten page escape plan."

    n "What’s your problem?"

    j "Ever since we’ve gotten here, you’ve done nothing but tell me what to do. It’s... odd. I get having people bossing us around again is weird."
    j "That doesn’t mean you have to do it too."

    "I don’t have anything I can say. All my friends have been worrying about the future and there’s nothing I can do to fix it, fine."
    "He can enjoy his junk and I’ll find a way out of this mess on my own."

    n "Clearly whatever you’ve been doing has been working so well for you in the past, so far be it for me to try and change anything."

    return
label Jona4:
    scene backgroundcafe

    "I hadn’t hung out with Jona after he got all weird about asking me for help with his family issues."
    "I have enough on my plate without adding some manufactured rhetoric about how I butt into other people’s business."
    "So it’s really weird having him seek me out for a change."

    n "What do you want?"

    j "You’re really starting to worry me."

    n "I’m worrying you? Do tell."

    j "I did tell you."

    n "I was using a sarcastic figure of speech"

    j "Oh."

    n "And last I checked, you dislike ‘people’ problems, so go ingenting them for all the people around you?"

    j "I’m not inventing problems, I just notice them. And you are not taking failure well."

    n "I have NOT FAILED-"

    j "Yeah, you have. We all sucked and let everybody down, and you’re the only one who can’t seem to accept that."

    "I punch him in the face. His decora shit slices open my knuckles though, so I’d call it even. He apparently doesn’t."

    j "What sane person would try and punch this thing? You have no idea how long it took to customize this!"

    "The wind is knocked out of me as his shoulder collides with my stomach. He pins down my right arm with his boot, waiting for me to catch my breath."

    n "You’ve been a doormat our entire lives, why do you suddenly give a shit now?"

    "It hurts to breathe. I may not be built for combat, but like hell am I giving up."

    j "What have I got to lose? You’re no better than me at this point."

    "He’s so focused on keeping my shoulder pinned that I’m able to shake my leg around his other foot to knock him to the ground."
    "I hear something shatter next to me and a string of curses from Jona."

    n "I never said I was better than you."

    j "You didn’t have to. It was obvious the only reason you guys hung out with me was to feel better about yourselves."

    "I really don’t have a good argument against that; he’s right. Having some mousey kid follow us around was a nice ego boost. We mostly included him in our plans to give him something to do."

    n "What do you want from me, man, I’m only human."

    "At least that gets him laughing. Only for a bit though, his laughter stopping the instant he sees his goggles shattered on the ground."

    n "Dude, I’m sorry-"

    j "Don’t look at me!"

    "He frantically gathers the pieces, intermittently checking the integrity of his mask. Unfortunately for him, I’ve already seen what he was trying to hide."

    n "Other than your eyes still being purple, is there something I’m supposed to be alarmed by?"

    "He looked normal to me. A little better than normal, actually. It’s a little hard to tell with that stupid mask blocking the rest of his face."

    j "Stooop, stop looking at me. You’re starting to do the thing."

    n "The thing?"

    "Why can’t he put his hands down for five seconds?"

    j "That! Tilting your head to the side all slack-jawed. Please stop."

    "I reluctantly tear my eyes away. I’m normally one to stare. What has gotten into me?"

    n "You didn’t used to cover your face like that."

    j "I didn’t need to before. Well, maybe mom wanted me to hide a lot sooner."
    j "It just didn’t bother me as much back then, being able to draw people in without trying, but you know what people say about Charm Majors."

    n "Well, yeah, but you’re a Vision- Wait, you’re not actually a Charisma Major, are you?"

    j "Unconfirmed. My mother wasn’t chomping at the bit to get me screened for something she didn’t want either of us to use."
    j "Besides, I don’t need a test to tell me people act differently around me when they can see my face."

    "There’s only one person I’ve ever heard of who had a Proficiency that worked that way; the infamous Siren."
    "But Siren was a tragic and fragile figure in the history of the Karmic Gladiators and Jona’s mom was..."
    "Well, there’s no delicate way to put it, she was crazy. Could they really be the same person?"

    menu:
        "There's no way":
            $ jRep -= 1

            n "Dude, your mom was crazy, you’ve said so yourself. It probably just seems like she was right because she conditioned you to believe so."
            n "Of course people are going to freak out when they see your face, you always hide it."
            
            j "You don’t understand, I don’t want you to understand, that would be... You made me go off topic, I came here to see if you were okay."

            n "Clearly I’m the poster child for well adjusted teens."

            j "You know what I mean."

            n "So your plan was what exactly? Thought you could talk me out of reforming the LF or something?"

            j "N-no. I thought... You seem to be making the same mistakes. I just wanted to try and stop you from spiraling again."

            n "What part of this looks like spiraling to you?"

            j "The unwavering fixation on a single goal to the point of neglecting everything else in your life. You know you do this a lot when things get stressful."
            j "I don’t want you going all tunnel vision and forget to eat and stuff."

            n "I’m not- This time is different, okay?"
        "It's none of my buisness":
            $ Charm += 1

            n "Who told you we only hung out with you to boost our egos?"

            j "You’re still hung up on that?"

            n "It’s not common for you to pick up on subtle social cues. I’m not denying it entirely, it just seems like an odd conclusion for you to come to solo."

            j "It wasn’t any one person. Kids don’t pull punches when they want to tear someone down. I mean, yeah, I’m a pretty literal person, but Odori helped me recognize certain phrases."
            j "Worlds like ‘specially’ aren’t usually compliments if they come from your peers."
            j "She said I’d get made fun of less if I hung out with you guys since you wanted to keep me around."

            n "That’s a surprisingly harsh thing for her to say."

            j "Well, she tried being tactful, I think, then she gave up and told me point blank what was going on. I thought doing whatever you guys wanted would get me somewhere, but here we are."

            "Here we are indeed. At this time last year, I thought I’d be ruling my own city. Instead, I’m in high school."
        "Play along":
            $ jRep += 1

            n "Your secret’s safe with me. I mean, I don’t know if it’s a secret or anything, I just assume that if you’re lying about your major..."

            j "Thanks, man. I appreciate it."

            "He straps on his busted goggles and sighs in defeat. Only one lens in still in place, though it’s obscured by a spider web of breaks."

            n "Even when the lenses are intact, do they really work?"

            j "...not really, but they help filter out the light and dulls most colors. It just makes things easier to deal with. I got a spare, don’t worry."

            n "So how does being a Charisma Major make you sensitive to light and color?"

            j "It doesn’t that’s just part of being me."

            n "And the aura thing?"

            j "I see the tone of people’s voices as flashes of color. But it’s not exactly ‘seeing’ since the goggles can’t filter it out. But I still see it?"
            j "Calling it a Proficiency makes it seem cooler than it is and it makes for a great cover as a ‘Vision’ Major."

            n "Is avoiding getting labeled as a Charisma Major really worth all this trouble?"

            j "It’s all I’ve known. Besides, the less connection I have with my mother in the eyes of the public, the easier things will be for me. It’s the same for you, isn’t it?"

            n "I mean, my dad was an evil bastard, but I don’t care if people compare us. I’ve surpassed him in every way by design."
            n "Besides, I’d like to believe the things I’ve done and will do are more important than who my mad scientist parents were."
    $ jTurn += 1
    $ Charm += 1

    n "I just wish people would stop pointing out everything I’ve messed up and then asking me why I can’t get over it. I can’t get over it?"
    n "Everyone else can’t seem to shut up about it long enough for me to finally move on and do something new."
    n "The worst offenders being my own friends."

    j "Well, of course everyone keeps bringing it up; we’re back where we started. Only this time, we have less than what we started with."

    n "Yeah, and?"

    j "Back then all we did was complain until you and Odori convinced us to do something about it."
    j "Now we’re starting over, but you’re skipping the complaining step. It’s like you’re fighting just to fight."

    n "That’s what’s got you concerned? That I’m not complaining enough?"

    j "I don’t know why you keep trying to fight these kids yourself. If it’s for the sake of fighting, then what happens when we’ve beaten them all? That’s what I’m worried about."
    j "People who fight just to keep fighting, they shut down the moment they stand still. I’ve seen it more than once."

    "I’m not used to seeing Jona so morose. It’s unsettling."

    n "I’m just doing this to protect people. I’m not stirring up shit to keep busy."

    j "...okay."

    n "I’m serious! Come on, let’s go get patched up before someone sees us. I really don’t want to get detention over something dumb like this. I’m sure Hiro has something we can use."

    j "...sure."
label Jona5:

    scene backgroundstage

    "Today I have to help Jona paint sets for an upcoming dance recital. Well, technically I don’t have to, I’ve chosen to. It’s the least I can do after breaking his goggles."
    "He has me painting all the built pieces with base coats while he constructs the rest."

    j "How’s your hand?"

    n "Better. I got it wrapped up pretty good, but Hiro’s pissed at me of course. Even though you started it."

    j "I didn’t- You punched me, which clearly means I was partially right. You’re not handling this well on your own."

    n "It’s just a minor setback; I can fix this."

    j "Well, yeah, but what if you can’t? Things could be stuck this way forever. I mean, what about this is fixable?"

    menu:
        "The future":
            $ jRep += 1
            j "....."

            n "Not in a cheery way, but like... Like where you’re going to go after we graduate. That’s an easy fix."

            j "Nagen, I already told you, I don’t know where I’m going to go."

            n "Just stay with me."

            j "What?"

            n "I gotta move out after graduation anyways, and getting a place is easier if two people are shipping in."

            if jRep >= 3:
                j "....."

                n "I mean, we’ll both need to work to make ends meet, but we can swing it."

                j "You really want to do this?"

                n "Of course. Unless you think it’s a bad idea?"

                j "N-no, that sounds great! I could finally get a cat and an actual art space."

                n "Please don’t spend all our money on art supplies."

                j "No promises."
            else:
                j "That’s a horrible idea. Why would you suggest that so soon after getting into a fight with me?"
                j "Are you some kind of yandere stalker? That would explain so much."
                    
                n "Slow down there, I was just speculating."

                j "Putting all your faith into fantasies isn’t going to get you anywhere, Nagen. I’m trying to be realistic here."
                j "What are you going to do if all of this falls through?"

                "Jona is the least realistic person I know. I’ve never seen him so certain something would go wrong."

                n "It warms my heart to not be the paranoid one for once. Fine, say we fail to find Apex and take the fall for everything..."

                j "We fail to find Apex and take the fall for everything."

                "I can’t even laugh at the absurdity of all this. I just feel tired and numb thinking about ending up at the back end of this."
            n "That’s simply not an option."

            j "Your aura’s getting grayer."

            n "I’m fine, don’t worry about me."

            j "...that’s what they all said. You can’t fix everything, Nagen. The sooner you accept that, the easier it gets."
        "School":
            $ Charm += 1
            
            n "We’re a part of the first graduating class at this school. We get to establish the status quo, the traditions. Plus lord over our peers."

            j "Yeah, you’re the only one putting any importance on this role as student body president. You’re competing with nerds for the attention of other nerds."

            n "But I can make everyone here listen to me even if they don’t want to!"

            j "....."

            n "Look, I know it’s not the most exciting thing to most people, but it’s one of the few things I have control of."
            n "There has to be something you’re interested in that you can force people to care about."

            j "That’s what school means to you?"

            n "It’s a two way street. We put up with teachers and we make them put up with our shit. All of it."

            j "Hmm... As insulting as Rise’s attempt at an art show was, it would be nice to display some of my more finished works."

            n "There you go! We could make an art club or something."

            j "Or something..."
        "Apex":
            $ jRep -= 1

            j "What, change Apex? Like with the power of friendship and shit?"

            n "Nonono, like take her out. Apex is the reason everything went to shit. Once she’s out of the question, it’s all smooth sailing."

            j "No. Nope, no, nuh uh. There’s such a thing as personal responsibility. I’m pissed Apex is stirring up shit too, but ‘getting rid of her’ isn’t going to repair anything."
            j "It just changes it. I thought you’d have figured that out from last time."

            n "Eliminating Estella Prep helped a lot of kids. We just haven’t met them yet. It’s the same with Apex. If we let her run loose, who knows what she’ll do?"

            j "Or we can focus on helping the people closest to us and then worry about the others."

            n "My point is, we have to at least try and do something. Otherwise, nothing’s going to change for sure."
    j "...right."
    j "So Hiro’s mad at you, hunh?"

    n "Dude, he’s furious. The whole reason why I avoided going to Mu was to avoid getting lectured, but this was ten times worse."

    j "Did he try to kiss it and make it better?"

    n "No! He asked me what happened and when I told him what happened, he said you were right."

    j "Bwahahaha! Did you punch him too?"

    n "...no, not like I ever could. He said I was on alert and he was going to be, and I quote, ‘keeping a closer eye on me’."
    n "The one cool thing about school was that I wasn’t supposed to be grounded."

    j "You know we only give you a hard time because we’re worried about you."

    n "I’m supposed to be the one looking out for you guys."

    j "Which is total bullshit considering all of us are older and taller than you."

    n "You didn’t have to bring up being taller."

    j "My point is, we’re allowed to be worried about you, especially when you’re taking on everything by yourself. It’s not that I don’t believe in you or anything."
    j "It’s just frustrating to see you acting like you’re in this alone."

    n "You’re such a hypocrite, you know that?"

    j "Right back at you, asshat."

    n "Maybe things won’t get better, but trying to fix things makes me feel better."

    j "Good, then you can put that energy to work painting the rest of this"

    "He finishes hammering the last nail on a giant rolling staircase."
    "I’m not surprised he’s finished building it before I’m done painting, but I’m a little offended that he expects me to finish it today."

    n "That thing is monstrous, you have to be kidding."

    j "Don’t get all pessimistic on me now. We have a lot of work to do before nightfall."

    "It’s times like these that I’m glad I have a photographic memory. I’ll only be glancing at the assigned reading tonight."
    
label JonaF:
    scene backgroundfield

    "Jona sent me a text saying he was too busy to hang out right now."
    "I guess I'll see him later."
    return