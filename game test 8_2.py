#Thief tree 1 cq24


#needed imports
import sys, time, random

#defined blocks of story


def beginning() :
    prnt(f"Welcome, {name.capitalize()} to the Global Adventurer's Guild - Master Enterprise, also known as GAG-ME. ")
    prnt('My name is Miss Shin Giver and I will be taking you through a series of trials to determine if you are ready to be full guild members! ')
    prnt('Are you ready to start? \n')
    start = textinput('Please type yes or no: ').strip()
    #beginning the game
    while start != 'yes' and start != 'no': start = textinput('Please type yes or no: ').strip()
    if start.lower() == 'yes':
        prnt('Great, let\'s begin! ')
        prnt('Be you a valiant Warrior? Perhaps a brilliant Wizard? Surely not a dastardly Rogue! \n')
    #end screen if they don't wnat to play
    elif start.lower().strip() == 'no':
        prnt('Fine, I didn\'t want to play with you anyway. You die ')
        prnt('The End ')
        prnt('Loser ')
        quit()
    background = True
    #To ensure valid option is selected for background
    while background != "fighter" and background != "caster" and background != 'rogue' : background = textinput("Please enter fighter, caster, or rogue: ")
    #Fighter start
    if background == "fighter":
        fighter()
    #caster start
    elif background == "caster" :
       caster()
    #rogue start
    elif background == "rogue"  :
        rogue()


#Fighter Trees
def fighter():
    prnt(f"{titlef} I like to stab things with my possessed sword! \n")
    prnt("Miss Shin Giver: That's great. Pick up your sword and prepare for your first quest! \n")
    prnt(f"{titlef} I am ready! Will I be slaying foul demons to protect the city? \n")
    prnt("Miss Shin Giver: No. You must travel to Mike's Dive, a local bar in town, and rid Not Mike's cellar of the rodent infestation that  plagues his establishment! \n")
    prnt("You travel across town as requested. \n")
    prnt("You enter the tavern called Mike's Dive. A grisled, middle-aged man stands behind the bar cleaning a mug. He greets you as you enter. \n")
    prnt("How will you respond?\n1. Cut to the chase.\n2. Order a drink. \n3. Be discreet. \n")
    f1 = inpt("Please select option 1, 2, or 3: ")
    if f1 == '1' :
        prnt(f"{titlef} Greetings Mike, I have come from GAG-ME with orders to kill your cellar rats.\n{titlef} Show me the way so that I might complete my mission and leave this disgusting establishment. \n")
        prnt("Bartender: Would you keep it down? I don't want my patrons knowing about our little problem here and you just announced it to half the city. And my name's not Mike.\nNot Mike: You might not have tact, but you definitelly seem well equipped to handle the pests. Follow me down to the basement.\n He leads you around the bar, through the tiny kitchen and into the cellar. He then excuses himself back to his duties. \n")
        prnt("How will you proceed?\n1. Be cautious\n2. Be deceptive\n3. Be bold ")
        f1_1 = inpt("\nPlease select option 1, 2, or 3: ")
        if f1_1 == '1' :
            torchcellar()             
        elif f1_1 == '2' :
            hidecellar()
        elif f1_1 == '3' :
            weponcellar()    
    elif f1 == '2' :
        prnt("Bartender, pour me a round and keep them coming. I have enough gold to drink this place empty\nThe bartender pours you a round of house whiskey. The stuff tastes like the worst whiskey you've ever tasted, but it goes down fast; too fast. \nOne drink becomes two, which becomes four, which leads to passing out on the floor. \nWhile you sleep, the rats crept up from the cellar, bit three patrons, and started the Mike's Tavern Rat Plague, later known as The Mikey Mouse Tragedy. \nYou have chosen poorly and have failed the GAG-ME initiations. You must return home in disgrace.")
        theend()
    else :
        prnt(f"{titlef}Hello there, I have been sent by the guild. They said you might need some assistance with a specific problem, if you catch my meaning. \nThe bartender leans over the rail\n Bartender: Thank the twelve gods you're here. Please, follow me this way. I'll take you right to where the problem festers. \nHe leads you around the bar, through the tiny kitchen and into the cellar. He then excuses himself back to his duties.")
        prnt("How will you proceed?\n1. Be cautious\n2. Be deceptive\n3. Be bold\n")
        f1_3 = inpt("Please select option 1, 2, or 3: ").strip()
        if f1_3 == '1' :
            torchcellar()
        elif f1_3 == '2' :
            hidecellar()
        elif f1_3 == '3' :
            weponcellar()

#fighter torch in not mikes cellar
def torchcellar() :
    prnt("Noticing the cellar is dark, you pull a torch from your pack and light it. With sword in one hand and torch in the other, you make your way toward the back of the cluttered cellar. \n")
    prnt("Your footsteps echo throughout the cellar as you make your way through the cluttered mess.\n The torchlight flickers and steadies as you come into view of a large rodent of unusual size.\nIt's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height.\nIt releases a gurgling hiss and pounces toward you.\n")
    prnt("How will you react?\n1. Torch\n2. Sword\n")
    f1_1_1 = inpt("Please select option 1 or 2: ").strip()
    #to verify valid selection
    if f1_1_1 == '1' :
        prnt("You swing your torch at the creature.\n")
        prnt("The torch strikes the rat's face, but it does minimal damage and the creature recovers quickly.\nWith a ferocious roar, the rat leaps at you and sinks it's teeth into your left arm. \nIt tears away a large chunk of flesh as it lands on the ground next to your feet. \nYou let out a scream of pain and drop the torch to the ground.\nIn an explosion of anger and adrenalyn, you swing your sword at the creatures neck.\nThe attack hits a critical point in the rat's neck and the monster slumps to the ground.\nAfter a few more blows, just to make sure the creature is dead, you sit down to the ground to inspect your wound.\n")
        prnt("Your arm wound is severe and you appear to have been infected by the bite.\n")
        prnt("What will you do?\n1. Bandage\n2. Consult your sword\n")
        f1_1_1_1 = inpt("Please select 1 or 2: ")
        if f1_1_1_1 == '1' :
            prnt("You bandage your arm wound and return to the GAG-ME barracks to report your mission as a success to Miss Shin Giver.\n")
            afb1()
        elif f1_1_1_1 == '2' :
            prnt("Unsure what to do next, you consult your cursed sword and inquire about what should be done regarding your wounds.\nMaroon wisps of magic energy dance across the face of the blade. \nYou speak outloud to the sword while explaining what happened and asking it what to do next.\nCursed Sword: You're probably not going to survive walking back to the guild with a wound like that.\nCursed Sword: I believe there was a medic upstairs wearing a healer's guild ring. Go up there and politely demand any healing potions they might have. \nCursed Sword: They always have one or two in their inventory. And stop whining! I hate it when you flesh golems whine.\n")
            prnt("Leaving a trail of blood droplets in your wake, you limp back up the stairs and into the tavern's lobby. \nPsychically guided by the sword, you make your way to the medic's table. The woman cleric has close cropped hair and a larger than average nose. \nShe looks you up and down as you approach, but you can tell from her motions that she is intoxicated.\n Before you even have a chance to speak she looks at you and slurs.\nCleric: I don't have healing powers left today. If you need help, I'll sell you one of my potions for 8 gold pieces.\n You only have 10 gold in total, so losing 8 would be devastating to your bank roll. Your sword whispers in your head\nCursed Sword: Kill her and take it!")
            prnt("How will you aquire the treatment?\n1. Pay\n2. Beg\n3. Take\n")
            f1_1_1_1_2 = inpt("Please select 1, 2 or 3: ").strip()
            if f1_1_1_1_2 == '1' : 
                prnt(f"You ignore the sword, pay the 8 gold, and take the healing potion.\nYou pop the cork off the healing potion and down the liquid in one fluid action. You feel a slight burning in your belly as the magic potion does its work, but it tastes like cinnamon whiskey, so it’s not completely awful. The cleric drunkenly counts out the 8g in front of you. Spitefully, you tip her brand new mug of ale over, spilling the contents on her as you make your way out of the tavern. \nFeeling rejuvenated, and broke, you make your way back to the guild to report back to Miss Shin Giver. Upon arriving you find Miss Shin Giver waiting for you. {msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance. \nFirst rats and now sewers? You came here to be an adventurer, not pest control! Maybe you can investigate a rumor you picked up while walking through the tavern. Some bandits just outside of town will be much more challenging.")
                healed = choice("1 Get to work 2 Investigate the bandits")
                if healed == '1':
                   prnt("You head directly to the sewer entrance.\nThe sewer entrance is in the side of an outer city wall. The door opens to a black tunnel made of stone. Sewage water slowly flows down the center of the tunnel and comes to around 9 inches deep at the center. You light a torch and make your way into the tunnel. The smell is nauseating and you do your best to stay to the side of the tunnel, avoiding the sewage as much as possible. You come to a split in the tunnel and decide to investigate.  On the right path, you see scratch marks and dents in the tunnel structure. A creature with large claws could have made these marks. On the left path, the sewage seems to stand still. There may be a blockage further up the sewer.") 
                   sewersplit = choice("1 Go right 2 Go left")
                   if sewersplit == '1':
                       assholebrokeright()
                   else:
                       assholebrokeleft()             
                else:
                    assholebandits()
            elif f1_1_1_1_2 == '2' : 
                prnt('You ignore the sword, beg the cleric for mercy, and "accidentally" fall on her, smearing blood on her nice tunic.\n')
                quit()
            elif f1_1_1_1_2 == '3' : 
                prnt("The sword hasn't led you wrong yet. You draw your sword and stab the cleric in the chest.\n")
                quit()
    elif f1_1_1 == '2' :
        prnt("You swing your sword at the creature.\nYour first strike hits home and the rat cries out in pain.\nThe creature attempts to bite your sword arm, but your armor absorbs the blow.\nA second blow from your sword glances off the shoulder of the creature.\nThe rat lunges for your right leg, but you bring your sword blade down through the creatures neck. It drops to the ground lifeless. \nYou clean your blade and quickly survey the rest of the cellar. After a moment, you are certain that the threat has been eliminated.\n")
        prnt("With your foe vanquised what will you do?\n1. Report to GAG-ME\n2. Ask your sword's advice\n")
        f1_1_1_2 = inpt("Please select option 1 or 2: ")
        if f1_1_1_2 == '1' :
            prnt("You return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15.\n")
            prnt("Miss Shin Giver: There have been complaints about a creature in the sewer eating people's pets.\nMiss Shin Giver: Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.\nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
            prnt("With your objective clear what should you do next?\n1. Get started right away\n2. Go shopping first\n")
            f1_1_1_2_1 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_1_2_1 == '1' :
                prnt("You head directly to the sewer entrance.\n")
                quit()
            elif f1_1_1_2_1 == '1' :
                prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!\n")
                quit()
        elif f1_1_1_2 == '2' :
            prnt("You consult your cursed sword and inquire about what you should do next.\nMaroon wisps of magic energy dance across the face of the blade. You speak outloud to the sword while explaining what happened and asking it what to do next.\nCursed Blade: This mission was too easy. If we really want to stand out at exemplary adventurers, we need to go above and beyond the standard mission. \nCursed Blade: I believe I sensed some scoundrels outside in the alley just a could blocks down. Let's go teach them a lesson before we head back to the guild!")
            prnt("How will you proceed?\n1. Ignore the sword\n2. Take the advice\n")
            f1_1_1_2_2 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_1_2_2 == '1' :
                prnt("You ignore the sword and head back to the guild to report back to Miss Shin Giver.\n")
                quit()
            elif f1_1_1_2_2 == '2' :
                prnt("The sword is making good sense. Bubbling with confidence, you leave the tavern and head to the alley that was just a few buildings down the road.\n")
                quit()  
#fighter hides in not Mikes cellar
def hidecellar() :
    prnt("Confident in your abilities, you begin mimicking squeaking noises to call out the rats in question.\nYou crouch at the waist and make squeaking noises as you move throughout the cellar. \nThe clicks and trills that come from your mouth begin to foster a response from a creature somewhere in the room. \nYou make your way toward the back of the cellar and your eyes adjust to the dim lighting.\nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. \nThe giant rat easily reaches your waist level in height. It releases a gurgling hiss and pounces toward you.")
    prnt("How will you react?\n1. Hide\n2. Fight\n")
    f1_1_2 = inpt("Please select option 1 or 2: ").strip()
    if f1_1_2 == '1' :
        prnt("You run away and dive behind a stack of crates.\nHidden behind a stack of crates, you collect your thoughts and survey the area. \nYou slowly raise your head over the crate to see if you can find the rat, but the creature is no where to be found. \nSlowly, you fully stand up to get a better view. A sharp pain strikes your ankle! \nThe rats paw slid in between the crates to claw at you! \nYou bring the sword down on the arm of the rat, cutting it clean off. It screeches in pain and reels away from crate. \nSeizing the opportunity, you hurdle the crate and bring your sword down on the creature's skull. \nThe blow killed the giant rat instantly, but hurdle caused you to land on your bad ankle; twisting it and doing more damage.\nYour ankle wound seems minimal.\n")
        prnt("With the creature slain, what will you do next?\n1. Report back\n2. Consult your sword\n")
        f1_1_2_1 = inpt("Please select option 1 or 2: ").strip()
        if f1_1_2_1 == '1' :
            prnt("You bandage the wound on your ankle and report your mission as a success to Miss Shin Giver.\nYou safely make it back to the guild hall. \nThe guild healer is attending to other patients, so you decide to wrap the leg up with clean bandages and get some rest. \nThe next morning, you visit Miss Shin Giver to receive your next test. \nMiss Shin Giver: There have been complaints about a creature in the sewer eating people's pets. \nMiss Shin Giver: Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.\n")
            prnt("What will do now?\n1. Get to work\n2. Shop first/n")
            f1_1_2_1_1 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_2_1_1 == '1' :
                prnt("You head directly to the sewer entrance.")
                quit()
            elif f1_1_2_1_1 == '2' :
                prnt("You head to the market to pick up supplies for your sewer run. The last thing you need is sewage getting into your leg wound.")
                quit()
        elif f1_1_2_1 == '2' :
            prnt("Unsure what to do next, you consult your cursed sword and inquire about what should be done regarding your wounds.\nMaroon wisps of magic energy dance across the face of the blade. You speak outloud to the sword while explaining what happened and asking it what to do next.\nCursed Blade: It isn't your fault that your ankle was injured, it's the barkeeps fault. \nCursed Blade: I bet he won't even offer to pay for a healer to fix it. \nCursed Blade: The only way we can get our due is by stealing something of value from this cellar. Let's look around!\n")
            prnt("Will you listen to the sword?\n1. Ignore it\n2. Take the advice\n")
            f1_1_2_1_2 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_2_1_2 == '1' :
                prnt("You ignore the sword and head back to the guild to report back to Miss Shin Giver.\n")
                quit()
            elif f1_1_2_1_2 == '2' :
                prnt("The sword is right! That barkeep did look super stingy! \nYou start cracking open crates until you find one that has just what you're looking for. \nA lantern with several gems adorning the base of the item was tucked at the bottom of a crate that held family heirlooms. You don't need a stupid lantern. You have torches. \nBut you could probably sell this piece for a pretty penny. Compensation in hand, you head back to the guild to report your misison success to Miss Shin Giver")
                quit()
    elif f1_1_2 == '2' :
        prnt("You stand firm and draw your sword from its sheath, but it is just a moment too late. \nThe giant rat strikes you with its claw and carves into your left thigh. Sword now in hand, you slash at the rat. \nYou exchange blows with each other until the rat finally collapses to the ground. \nYou are victorious, but at a cost. You have sustained several injuries, but luckily none of them were bites. \nThe last thing you need is to catch a disease on your first mission. Breathing heavily, you assess your wounds.\n The wounds are severe and there is heavy blood loss.")
        prnt("What will you do?\n1. Bandage the wound\n2. Consult your sword\n")
        f1_1_2_2 = inpt("Please select option 1 or 2: ").strip()
        if f1_1_2_2 == '1' :
            prnt(" With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs.\nQuickly losing blood, you slowly limp your way back to the lobby of the tavern. \nThe concern on Not Mike's face is evident as he sees you enter the room. On the far side of the tavern, a woman with close cropped hair and a larger than average nose empties the last of her ale mug. \nEven in your current state and from this distance, you can tell that she is intoxicated, but she also wears a Healer's Guild Ring.\n")
            prnt("What will you do?\n1. Get to the guild\n2. Seek out the cleric\n")
            f1_1_2_2_1 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_2_2_1 == '1' :
                prnt("You ignore the drunk patrons and head back to the guild for medical attention.")
                quit()
            elif f1_1_2_2_1 == '2' :
                prnt("With blurred vision, you stumble toward the cleric in hopes for healing.")
                quit()
        elif f1_1_2_2 == '2' :
            prnt("Unsure what to do next, you consult your cursed sword and inquire about what should be done regarding your wounds.\nMaroon wisps of magic energy dance across the face of the blade. You speak outloud to the sword while explaining what happened and asking it what to do next.\nCursed Blade: You're probably not going to survive walking back to the guild with a wound like that. I believe there was a medic upstairs wearing a healer's guild ring.\nCursed Blade: Go up there and politely demand any healing potions they might have. They always have one or two in their inventory.\nCursed Blade: And stop whining! I hate it when you flesh golems whine.\nLeaving a trail of blood droplets in your wake, you limp back up the stairs and into the tavern's lobby. \nPsychically guided by the sword, you make your way to the medic's table. The woman cleric has close cropped hair and a larger than average nose. \nShe looks you up and down as you approach, but you can tell from her motions that she is intoxicated. Before you can even speak she gives you a dismissive glance. \nCleric: I don't have healing powers left today. If you need help, I'll sell you one of my potions for 8 gold pieces. \nYou only have 10 gold in total, so losing 8 would be devastating to your bank roll. Your sword whispers in your head. \nCursed Blade: Kill her and take it!")
            prnt("What will you do?\n1. Pay\n2. Beg \n3. Heed the sword\n")
            f1_1_2_2_2 = inpt("Please select option 1 or 2: ").strip()
            if f1_1_2_2_2 == '1' :
                prnt("You ignore the sword, pay the 8 gold, and take the healing potion.")
                quit()
            elif f1_1_2_2_2 == '2' :
                prnt('\nYou ignore the sword, beg the cleric for mercy, and "accidentally" fall on her, smearing blood on her nice tunic.')
                quit()
            elif f1_1_2_2_2 == '3' :
                prnt("The sword hasn't led you wrong yet. You draw your sword and stab the cleric in the chest.")
                quit()
#fighter draws weapon in not mikes cellar
def weponcellar() :
    prnt("Caution is for the weak hearted! These are rats and you fear no such vermin. \nYou begin moving boxes around in order to locate the pests. What good is a sword when a boot will do?\nAs you toss boxes around the room, you hear a strange chitter from behind a box ahead. \nSteel toed boot ready for stomping, you toss aside the crate that separates you from the target, and find a large monstrosity of a rat! \nIt's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
    prnt("How will you react?\n1. Draw your weapon\n2. Punch\n")
    f1_1_3 = inpt("Please select option 1 or 2: ").strip()
    if f1_1_3 == '1' :
        prnt("You draw your sword from its sheath, but it is just a moment too late. The giant rat strikes you with its claw and carves into your left thigh. \nSword now in hand, you slash at the rat. You exchange blows with each other until the rat finally collapses to the ground. \nYou are victorious, but at a cost. You have sustained several injuries, but luckily none of them were bites. \nThe last thing you need is to catch a disease on your first mission. Breathing heavily, you assess your wounds.\nYour wounds are severe and there is heavy blood loss.")
        prnt("What will you do?\n1. Bandage\n2. Consult your sword")
        f1_1_3_1 = inpt("\nPlease select option 1 or 2: ").strip()
        if f1_1_3_1 == '1':
            prnt("With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs.\nQuickly losing blood, you slowly limp your way back to the lobby of the tavern. \nThe concern on Not Mike's face is evident as he sees you enter the room. On the far side of the tavern, a woman with close cropped hair and a larger than average nose empties the last of her ale mug. \nEven in your current state and from this distance, you can tell that she is intoxicated, but she also wears a Healer's Guild Ring.")
            prnt("What will you do? \n1. Head toward the guild\n2. Go to the cleric")
            f1_1_3_1_1 = inpt("\nPlease select option 1 or 2: ").strip()
            if f1_1_3_1_1 == '1' :
                prnt("You ignore the drunk patrons and head back to the guild for medical attention.")
                quit()
            elif f1_1_3_1_1 == '2' :
                prnt("With blurred vision, you stumble toward the cleric in hopes for healing.")
                quit()
        elif f1_1_3_1 == '2' :
            prnt("Unsure what to do next, you consult your cursed sword and inquire about what should be done regarding your wounds.\nMaroon wisps of magic energy dance across the face of the blade. \nYou speak outloud to the sword while explaining what happened and asking it what to do next. \nCursed Blade: You're probably not going to survive walking back to the guild with a wound like that. I believe there was a medic upstairs wearing a healer's guild ring. \nCursed Blade: Go up there and politely demand any healing potions they might have. They always have one or two in their inventory. \nCursed Blade: And stop whining! I hate it when you flesh golems whine. \nLeaving a trail of blood droplets in your wake, you limp back up the stairs and into the tavern's lobby. \nPsychically guided by the sword, you make your way to the medic's table. The woman cleric has close cropped hair and a larger than average nose. \nShe looks you up and down as you approach, but you can tell from her motions that she is intoxicated. Before you can even speak she addressed you. \nCleric: I don't have healing powers left today. If you need help, I'll sell you one of my potions for 8 gold pieces. \nYou only have 10 gold in total, so losing 8 would be devastating to your bank roll. Your sword whispers in your head. \nCursed Blade: Kill her and take it!")
            prnt("What will you do?\n1. Pay\n2. Beg\n3. Heed your sword")
            f1_1_3_1_2 = inpt("\nPlease select option 1, 2 or 3: ").strip()
            if f1_1_3_1_2 == '1' :
                prnt("You ignore the sword, pay the 8 gold, and take the healing potion.")
                quit()
            elif f1_1_3_1_2 == "2" :
                prnt('\nYou ignore the sword, beg the cleric for mercy, and "accidentally" fall on her, smearing blood on her nice tunic.')
                quit()
            elif f1_1_3_1_2 == "3" :
                prnt("The sword hasn't led you wrong yet. You draw your sword and stab the cleric in the chest.")
                quit()
    elif f1_1_3 == '2' :
        prnt("You punch the rat right in his whiskery face!\nYour fist strikes the rat's face, but it does minimal damage and the creature recovers quickly. \nWith a ferocious roar, the rat leaps at you and sinks it's teeth into your left arm. It tears away a large chunk of flesh as it lands on the ground next to your feet. \nYou let out a scream of pain and drop the torch to the ground.\nThe World Goes Dark.")
        prnt(f"\n{titlef}......It wasn't supposed to end like this.....")
        time.sleep(3)
        prnt("THE END")
        time.sleep(5)
        quit()  
#asshole fighter
def afb1():
    prnt(f"You safely make it back to the guild hall, but the infection sets in fast. The guild healer sees to your wounds and administers a poultice. \nAfter a good night's rest, the healer says that you are fit enough to carry on with more mission tests, but you will be sickly for the next week or so. \nIt is recommended that you return to the healer if the infection does not go away within 3 days. You visit Miss Shin Giver. \n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
    afb1_1 = inpt("What will you do? \n1. Get to work\n2. Shop first\nPlease select option 1 or 2: ")
    if afb1_1 == '1':
        prnt("You head directly to the sewer entrance.\nThe sewer entrance is in the side of an outer city wall. The door opens to a black tunnel made of stone. Sewage water slowly flows down the center of the tunnel and comes to around 9 inches deep at the center. \nYou light a torch and make your way into the tunnel. The smell is nauseating and you do your best to stay to the side of the tunnel, avoiding the sewage as much as possible. \nYou come to a split in the tunnel and decide to investigate. \nOn the right path, you see scratch marks and dents in the tunnel structure. A creature with large claws could have made these marks. On the left path, the sewage seems to stand still. There may be a blockage further up the sewer.")
        assholepoisoned()
    elif afb1_1 == '2':
        prnt("With hopes of purchasing a cure for your ailment, you decide to make a stop at the local alchemist first.\nYou are still infected. The local alchemist is an eccentric gnome named Sir Mix Alott. After you give him a brief explanation of what happened, he claims to have the perfect tincture to completely cure you. The tincture would cost 10 gold pieces, which is currently all you have in your possession.")
        a = choice("1 Pay 2 Go without")
        if a == '1':
            prnt(f"You pay the 10 gold and immediately drink the tincture. You make eye contact with Sir Mix Alott\n{titlef}If this doesn’t work, I’m going to beat my refund out of you! \nYou head to the sewer entrance. \nThe sewer entrance is in the side of an outer city wall. The door opens to a black tunnel made of stone. Sewage water slowly flows down the center of the tunnel and comes to around 9 inches deep at the center. \nYou light a torch and make your way into the tunnel. The smell is nauseating and you do your best to stay to the side of the tunnel, avoiding the sewage as much as possible. \nYou come to a split in the tunnel and decide to investigate. \nOn the right path, you see scratch marks and dents in the tunnel structure. A creature with large claws could have made these marks. \nOn the left path, the sewage seems to stand still. There may be a blockage further up the sewer.")
            b = choice("1 Take the right path 2 Take the left path")
            if b =='1':
                assholebrokeright()
            else:
                assholebrokeleft()    
        else:
            prnt("You head to the sewer without treatment.\nThe sewer entrance is in the side of an outer city wall. The door opens to a black tunnel made of stone. Sewage water slowly flows down the center of the tunnel and comes to around 9 inches deep at the center. \nYou light a torch and make your way into the tunnel. The smell is nauseating and you do your best to stay to the side of the tunnel, avoiding the sewage as much as possible. \nYou come to a split in the tunnel and decide to investigate. \nOn the right path, you see scratch marks and dents in the tunnel structure. A creature with large claws could have made these marks. On the left path, the sewage seems to stand still. There may be a blockage further up the sewer.")
            assholepoisoned()

def assholepoisoned():
    ap1 = choice("1 Go right 2 Go left")
    if ap1 == "1" :
        prnt("You are still infected. You follow the path to the right. Long thick strands of webbing begin to appear in the sewer tunnel as you make your way toward what appears to be a monster’s nest. As you round a corner, a giant phase spider comes into view. It is currently feeding on something.")
        ap2 = choice("1 Attack 2 Report back")
        if ap2 == "1":
            print("Attack the phase spider!\nYou draw your weapon and charge forward to attack the spider. Your first attack strikes true and your sword buries itself deep into the spider’s abdomen. \nUnfortunately, it is not enough to kill the spider. The monstrosity turns quickly and leaps at you. \nWith your wounds still fresh and your body currently fighting infection, you are unable to dodge the attack. \nThe spider lands on you; sinking its fangs into your chest and bringing your to the ground. Within moments, the spiders venom circulates through your body and you die.")
            theend()
        elif ap2 == "2":
            prnt(f"You are still infected. You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the nest of the phase spider can be found and she dismisses you to get some rest. \nThe next day, you wake and report to Miss Shin Giver. \n{msg}This will be your final mission to attain admittance into the guild as a full member. Most of what we do here at the guild is finding and collecting magic items. It appears that one such item has come into close proximity of Cheddar and we have been tasked to collect it. \n{msg}A woman that goes by the name Pan Dora recently stole an item from the Collective and has hidden away to a secret cabin in the woods west of Cheddar. We wouldn’t normally ask a new recruit to assist in such a case, but this is an all hands on deck scenario. There are over 500 cabins in the woods, so the chance of you actually finding her is 1 in 500. So you should be fine. Here are directions to the cabin we would like you to investigate. Return here after you have cleared that cabin.")
            ap3 = choice("1 Get to work 2 Consult sword")
            if ap3 == '1':
               assholepoisonedcabin()
            elif ap3 == '2':
                prnt("You are still infected. The Global Adventurer’s Guild is starting to sound more like the Global Lame Guild. You ask your sword if you should really go to the cabin or if there is something else you should do. \nCursed Sword: There won’t be much to kill in an empty cabin. We need to destroy some evil people! Let’s get those bandits we heard about that are hiding in the woods. I bet we could kill them and rid the world of more evil! \nYou can still feel the infection coursing through your veins, but there's not time for weakness.")
                ap4 = choice("1 Go to the cabin 2 Search for bandits")
                if ap4 == "1":
                    assholepoisonedcabin()
                elif ap4 == '2': 
                    assholebandits()
    elif ap1 == "2":
        prnt("You are still infected. You follow the path to the left. The blockage seems to be further up the tunnel that expected. You pass through several intersections before finally finding the source of the back up. \nA giant ooze, the exact dimensions of the sewer and roughly 2 meters thick, moves slowly in your direction. Sewage is backed up behind it and floating pieces of trash are visible in the gelatinous ooze. There is also a giant gem in the center of the creature that may require rescuing.")
        ap2 = choice("1 Attack 2 Report back 3 Go back to the fork")
        if ap2 == '1':
            prnt("You draw your weapon and charge forward to attack the ooze. Your sword slices through the ooze with easy, but you appear to be doing minimal damage. \nCursed Blade: What are you doing? Kill it already! \nYou shove your sword and arm deep into the center of the dark green ooze, attempting to stab its central nerve system, if it has one. The ooze latches onto your arm, sucking you in. \nAlready fatigued from the infection you’re battling, you do not have the strength to oppose the ooze. It sucks you into its center where you begin to suffocate. \nCursed Blade: Oh shit. Not again.")
            theend()
        elif ap2 == "2":
            prnt(f"You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the ooze creature is hiding. {msg}Thank you for your report but you have failed the mission. An ooze wouldn’t come out of the sewers each night to steal animals for meals. It would simply go up and down the sewer. \nShe looks you up and down. \nThe infection appears to have gotten worse and you failed your last mission. You are dismissed from the trials. \nYou have failed.")
            theend()
        else:
            assholepoisoned()
def assholepoisonedcabin() :
    prnt("You are still infected. You leave the city of Cheddar and follow the directions to the cabin. \nThe infection appears to be running its course, but you are stronger than a little rat poison. You continue to the cabin.\nAs you draw nearer, you see smoke coming from the chimney. Of course there had to be someone here. You approach the cabin.\nIf life has taught you anything, the element of surprise is a huge advantage, but it’s also smart to be safe sometimes. ")
    ap4 = choice("1 Kick the door in 2 Peek in the window")
    if ap4 == "1":
        prnt(f"There was ever only one real option here. You kick the door with all your might and then charge into the small cabin. \nPan Dora the witch stands momentarily stunned by the fireplace. Just as you close the distance to the witch, a monkey jumps at you and begins biting at your sword arm. \nYou try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. Pan Dora begins to cast a spell.\nYou cannot let her finish casting that spell, so with a thought, you activate the magic properties of the sword and charge forward. The monkey does not release you, but you can deal with the pain as you move forward to attack. \nInvisible blade in hand, you thrust forward, landing a deadly blow to the witch’s stomach. Pan Dora falls to the ground, but not before finishing her incantation. \nPan Dora: You may have killed me, but I have accelerated the infection in your blood. You have only moments to live. Was it worth it? Pain coursing through your body, you finally shake the monkey free and raise your blade. \n{titlef}You can’t kill me. I’m invincible. \nYou let the blade fall on her for a killing blow. \nMuch to your disappointment, you are not invincible. The infection does claim your life as you fall to the ground, cursed sword in hand.")
        theend()
    elif ap4 == '2':
        prnt("You are still infected. You peek in the window and see Pan Dora stirring a pot of something you hope to be stew. On the table, there is a small box with magic rune work inscribed on the sides you can see. Next to the magic box, there is what appears to be a healing potion. It appears there are only two ways into this cabin. One through the front door for a full on attack, or you can try to be sneaky and crawl through the window.")
        ap5 = choice("1 Front door 2 Window")
        if ap5 == "1":
            prnt("You are still infected. You kick the door with all your might and then charge into the small cabin. Pan Dora the witch stands momentarily stunned by the fireplace.\nJust as you close the distance to the witch, a monkey jumps at you and begins biting at your sword arm. You try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. \nPan Dora begins to cast a spell. \nYou cannot let her finish casting that spell, so with a thought, you activate the magic properties of the sword and charge forward. The monkey does not release you, but you can deal with the pain as you move forward to attack. \nInvisible blade in hand, you thrust forward, landing a deadly blow to the witch’s stomach. Pan Dora falls to the ground, but not before finishing her incantation. \nPan Dora: You may have killed me, but I have accelerated the infection in your blood. You have only moments to live. Was it worth it?\nPain coursing through your body, you finally shake the monkey free and slowly walk over to the table that housed the Pan Dora’s Box. You grab the potion from the table \n{titlef}It was totally worth it. \nYou drink the contents of the potion. \nYou are healed of your wounds and infection. Pan Dora dies. The monkey with boots escapes. You collect Pan Dora’s Box and head back to the guild to report your success.")
            win()
        elif ap5 == "2":
            prnt(f"You attempt to sneak through the window. You slowly open it, ducking back down every time the window makes a creaking noise. The process is painfully slow and the window is incredible noisy, but Pan Dora the witch does not seem to notice. \nOnce the window is open wide enough for you to crawl through, you hoist yourself through the window and roll into the cabin. Quickly, you lift your head back up to check on the location of the witch. \nPan Dora is no longer at the fire. While you were rolling into the cabin, she must have moved. You scan the room quickly to find her. Halfway through the scan, a monkey jumps at you and begins biting at your sword arm. \nYou try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. Pan Dora begins to cast a spell. {pd}Do you think you’re a rogue or something? I heard you opening that window the whole time. Now you pay the price!\nPain surges through your body as Pan Dora finishes casting her spell. You fall to the ground as she lets out a hideous cackle.\nYou die.")
            theend()

def assholebandits():
    prnt("The bandits are tough to find. You search through the woods for hours to no avail. Exhausted, you sit down on the side of a grassy knoll. A voice comes from behind you. \rMysterious Voice: Excuse me, friend. Are you lost? My boys and I were looking some new blood in the gang. Would you like to join? \nIt’s the bandits! You found them and they want to recruit you!")
    a = choice("1 Attack 2 Join")
    if a == "1":
        prnt("In a sudden burst of fury, you charge the lead bandit. His face is one of complete and udder shock as you ram your cursed sword into his chest.\nTwo of his companions draw their swords, but you are faster. \nCursed Blade: Awww yeah. This is how we do it!\nThe blade revels as it slices into another bandit. \nYou are able to cut down four bandits in total before exhaustion begins to set in. The two remaining bandits circle you and your cursed blade. One bandit lunges forward. You are able to parry his blow, but the second bandit lands an attack.\nWith a powerful backswing, you fell the second attacker, but that allowed the first attacker to run you through. With his blade through your chest, you twist to the side and ram your own sword through his heart. \nAll the bandits are dead, but you have sustained too many wounds to get back to the city. You die.")
        theend()
    else:
        prnt("Joining the bandits seems like a better fit. Quite honestly, it’s like being an adventurer but without all the stupid rules. You meet the rest of the gang and find it easy to fit in with the rest of the group. \nYou could see yourself as a part of a bandit gang, as long as they don’t ask you to do anything too morally awful. You also could easily kill the bandit leader while sleeping and head back to the city guard to turn the bandits in and collect the bounty.")
        b = choice("1 Join 2 Collect the bounty")
        if b == "1":
            prnt("You decide to stay with the bandits. You do some cool Robin Hood shit by stealing for the rich and keeping it for yourself. Technically, you’re poor, so it tracks. You stay in the bandit life until the adventurer’s guild finally sends out a team to put it to an end.\nYour cursed sword alerted you before the Adventurer’s Guild arrived, allowing you to escape and head back to the city where you become a mercenary. \nHaving extent knowledge of banditry allows you to become a successful caravan guard and you are well regarded among all the merchants. You never get rich, but you retire with enough gold to live out your days in comfort.")
            theend()
        else:
            prnt("You wait until nightfall. Your cursed sword tells you when the bandits, including the one on watch, have all fallen asleep. \nYou make your way to the leader’s tent where you easily dispatch him while he sleeps. Quietly, you sneak out of the bandit camp and head back to the city of Cheddar.\nYou bring the guards to the bandit camp where you assist in the arrest of the bandits. You are paid a bounty of 100 gold for slaying the bandit leader and assisting in the arrest.\nCursed Blade: Being a bounty hunter is way easier and more profitable than being an adventurer. Let’s do this instead. \nRemembering that the Global Adventurer’s Guild requested that you go search through a piss filled sewer, you decide to listen to the sword and collect a second bounty from the city guard. \nAnd so began your wonderful career in bounty hunting.")
            theend()
def assholebrokeright():
    prnt("You follow the path to the right. Long thick strands of webbing begin to appear in the sewer tunnel as you make your way toward what appears to be a monster’s nest. \nAs you round a corner, a giant phase spider comes into view. It is currently feeding on something.")
    a = choice("1 Attack 2 Report back")
    if a == '1':
        assholebroke1a()
    else:
        prnt(f"You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the nest of the phase spider can be found and and let her know that you killed the creature. he dismisses you to get some rest.\nThe next day, you wake and report to Miss Shin Giver. \n{msg}This will be your final mission to attain admittance into the guild as a full member. Most of what we do here at the guild is finding and collecting magic items. It appears that one such item has come into close proximity of Cheddar and we have been tasked to collect it. \n{msg}A woman that goes by the name Pan Dora recently stole an item from the Collective and has hidden away to a secret cabin in the woods west of Cheddar. We wouldn’t normally ask a new recruit to assist in such a case, but this is an all hands on deck scenario. There are over 500 cabins in the woods, so the chance of you actually finding her is 1 in 500. So you should be fine.\n{msg}Here are directions to the cabin we would like you to investigate. Return here after you have cleared that cabin.")
        assholecabinbroke()
def assholebrokeleft():
    prnt("You follow the path to the left. The blockage seems to be further up the tunnel that expected. You pass through several intersections before finally finding the source of the back up. \nA giant ooze, the exact dimensions of the sewer and roughly 2 meters thick, moves slowly in your directly. Sewage is backed up behind it and floating pieces of trash are visible in the gelatinous ooze. There is also a giant gem in the center of the creature that may require rescuing.")
    c = choice("1 Attack 2 Report back 3 Go back and take the right path")
    if c == '1':
        prnt(f"You draw your weapon and charge forward to attack the ooze. Your sword slices through the ooze with easy, but you appear to be doing minimal damage. \nCursed Blade: What are you doing? Kill it already! \nYou shove your sword and arm deep into the center of the dark green ooze, attempting to stab its central nerve system, if it has one. The ooze latches onto your arm, sucking you in. \n{titlef}Not today you jiggly bastard!\nWith superhuman might you pull your arm free of the gelatinous ooze. You activate the magic properties of your cursed blade. \nThe sword turns invisible and as you slice through the ooze, it begins to sizzle and burn away to nothingness. \nAfter a miserably long time spent slashing this monster into ooze puddles, you are victorious. You claim your prize, pocketing the giant gem.")
        d = choice("1 Report back 2 Go back and take the right patch")
        if d == "1":
            prnt(f"You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the ooze creature is hiding. \n{msg} Thank you for your report but  you have failed the mission. An ooze wouldn’t come out of the sewers each night to steal animals for meals. It would simply go up and down the sewer. \nShe looks you up and down.\nPanicked that she may kick you out of the trials, you show Miss Shin Giver the giant gem that you collected from the Ooze. She inspects the gem and then turns back to you.\n{msg}This gem shows that while you technically failed the mission, you were able to bring value to the guild through your actions. If you give me the gem, you can stay in the trials. If you would prefer to keep the gem, you may leave. I will even tell you what the next mission is. \n{msg}This will be your final mission to attain admittance into the guild as a full member. Most of what we do here at the guild is finding and collecting magic items. It appears that one such item has come into close proximity of Cheddar and we have been tasked to collect it.\n{msg}A woman that goes by the name Pan Dora recently stole an item from the Collective and has hidden away to a secret cabin in the woods west of Cheddar. We wouldn’t normally ask a new recruit to assist in such a case, but this is an all hands on deck scenario. There are over 500 cabins in the woods, so the chance of you actually finding her is 1 in 500. So you should be fine.\n{msg}Here are directions to the cabin we would like you to investigate. Return here after you have cleared that cabin.")
            e = choice("1 Give her the gem and head to the cabin 2 Keep the gem")
            if e == '1':
                assholecabinbroke()
            else:
                prnt("You keep the gem and leave the barracks. You might not be an adventurer, but you have a giant gem that is going to earn you a ton of gold. \nCursed Blade: Good riddance to those GAG-ME suckers. Let’s kill some evil people on the way to the gem merchant! \nAnd you and your creepy, cursed sword lived happily ever.")
                theend()
        else:
            prnt("You go retrace your steps to the fork.")
            assholebrokeright()
    elif c == '2':
        prnt(f"You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the ooze creature is hiding. \n{msg}Thank you for your report but you have failed the mission. An ooze wouldn’t come out of the sewers each night to steal animals for meals. It would simply go up and down the sewer. \nShe looks you up and down.\nYou are covered in sewer filth and smell awful. You are clearly not what the guild is looking for in a candidate. You are dismissed from the trials. You have failed.")
        theend()
    else:
        prnt("You go retrace your steps to the fork.")
        assholebrokeright()
def assholebroke1a():
    prnt("You draw your weapon and charge forward to attack the spider. Your first attack strikes true and your sword buries itself deep into the spider’s abdomen. Unfortunately, it is not enough to kill the spider. The monstrosity turns quickly and leaps at you. \nYou dive to the side, dodging the attack from the creature. You roll into a defensive stance and prepare to attack. Your next attack cripples one of the spider’s front legs, causing it to stumble and screech in pain. \nThe spider recovers quickly and leaps at you a second time, spitting its venom as it closes in. You dodge to your left, swinging your blade down into the creature’s head just as it lands. \nThe spider dies as it collapses to the ground next to you. \nAnother mission is complete. You head back to the guild to report your success.")
    prnt(f"You make it back to the guild safely and report your findings to Miss Shin Giver. You tell her exactly where the phase spider can be found and let her know you killed the creature. She congratulates you on your success and gives you your next mission. \n{msg}This will be your final mission to attain admittance into the guild as a full member. Most of what we do here at the guild is finding and collecting magic items. It appears that one such item has come into close proximity of Cheddar and we have been tasked to collect it. \n{msg}A woman that goes by the name Pan Dora recently stole an item from the Collective and has hidden away to a secret cabin in the woods west of Cheddar. We wouldn’t normally ask a new recruit to assist in such a case, but this is an all hands on deck scenario. There are over 500 cabins in the woods, so the chance of you actually finding her is 1 in 500. So you should be fine.\n{msg}Here are directions to the cabin we would like you to investigate. Return here after you have cleared that cabin.")
    assholecabinbroke()
def assholecabinbroke():
    prnt("You leave the city of Cheddar and follow the directions to the cabin. It is dark and eerie outside when you arrive at the cabin, but you are feeling healthy and confident in your assignment.\nAs you draw nearer, you see smoke coming from the chimney. Of course there had to be someone here. You approach the cabin. \nIf life has taught you anything, the element of surprise is a huge advantage, but it’s also smart to be safe sometimes.")
    a = choice("1 Kick in the door 2 Peek in the window")
    if a == '1':
        prnt(f"You kick the door with all your might and then charge into the small cabin. \nPan Dora the witch stands momentarily stunned by the fireplace. Just as you close the distance to the witch, a monkey jumps at you and begins biting at your sword arm. \nYou try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. Pan Dora begins to cast a spell. \nOn the table, there is a small box with magic rune work inscribed on the sides you can see; Pan Dora's Box. That box holds great magic, but Pan Dora is currently casting a spell.")
        b = choice("1 Attack Pan Dora 2 Go for Pan Dora's box ")
        if b == '1':
            prnt(f"You ignore Pan Dora’s Box and go for the witch. \nYou cannot let her finish casting that spell, so with a thought, you activate the magic properties of the sword and charge forward. The monkey does not release you, but you can deal with the pain as you move forward to attack. \nInvisible blade in hand, you thrust forward, landing a deadly blow to the witch’s stomach. Pan Dora falls to the ground, but not before finishing her incantation. \nA beam of energy shoots from Pan Dora’s hand toward you. Without hesitation  you bring your arm up and use the boot wearing monkey to block the blast. The monkey immediately releases your arm and falls to the ground.\nYou make your way toward the table to collect the box just as the monkey collects itself and escapes through the kicked in door.\nPan Dora dies. \nThe monkey with boots escapes. \nYou collect Pan Dora’s Box and head back to the guild to report your success.")
            win()
        else:
            prnt("You ignore Pan Dora and go for the box. \nYou fling the monkey to the side just before you reach the table. Pan Dora fires an energy beam spell at you, but it misses. She screams “Don’t touch that!” just as you grab Pan Dora’s Box and activate the runes on the side.\nThe monkey lets out a scream. The box begins to vibrate and shoot violet light out from the runes. \nPan Dora: Well shit.  \nThe cabin explodes. \nYou die.")
            theend()
    else:
        prnt("You peek in the window and see Pan Dora stirring a pot of something you hope to be stew. On the table, there is a small box with magic rune work inscribed on the sides you can see; Pan Dora's Box.\nIt appears there are only two ways into this cabin. One through the front door for a full on attack, or you can try to be sneaky and crawl through the window.")
        b = choice("1 Kick in the door 2 Sneak through the window")
        if b == '1':
            prnt(f"You kick the door with all your might and then charge into the small cabin. \nPan Dora the witch stands momentarily stunned by the fireplace. Just as you close the distance to the witch, a monkey jumps at you and begins biting at your sword arm. \nYou try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. Pan Dora begins to cast a spell.\nYou cannot let her finish casting that spell, so with a thought, you activate the magic properties of the sword and charge forward. The monkey does not release you, but you can deal with the pain as you move forward to attack.\nInvisible blade in hand, you thrust forward, landing a deadly blow to the witch’s stomach. Pan Dora falls to the ground, but not before finishing her incantation.\nPan Dora: You may have killed me, but I have cursed your blood. You have only moments to live. Was it worth it? \nPain coursing through your body, you finally shake the monkey free and slowly walk over to the table that housed the Pan Dora’s Box. You grab the potion from the table \n{titlef}It was totally worth it. \nYou drink the contents of the potion. \nYou are healed of your wounds and infection. \nPan Dora dies. \nThe monkey with boots escapes. \nYou collect Pan Dora’s Box and head back to the guild to report your success.")
            win()
        else:
            prnt("You attempt to sneak through the window. You slowly open it, ducking back down every time the window makes a creaking noise. The process is painfully slow and the window is incredible noisy, but Pan Dora the witch does not seem to notice. \nOnce the window is open wide enough for you to crawl through, you hoist yourself through the window and roll into the cabin. Quickly, you lift your head back up to check on the location of the witch.\nPan Dora is no longer at the fire. While you were rolling into the cabin, she must have moved. You scan the room quickly to find her. Halfway through the scan, a monkey jumps at you and begins biting at your sword arm.\nYou try to shake the monkey free, but it holds tight with its hand while it begins to kick you with its booted feet. Pan Dora begins to cast a spell.\nPan Dora: Do you think you’re a rogue or something? I heard you opening that window the whole time. Now you pay the price!\nPain surges through your body as Pan Dora finishes casting her spell. You fall to the ground as she lets out a hideous cackle.\nYou die.")
            theend()




#Caster Trees
def caster():
    prnt(f'{titlec}I use dark magic that I received from my creepy, potentially evil gods to strike down my enemies.\nMiss Shin Giver: That\'s slightly concerning, but I appreciate your morbid honesty. Now prepare for your first task.\n{titlec}I was born prepared. Actually, I was born in a barn. Would you like to hear the story?\nMiss Shin Giver: No. You must travel to Mike\'s Dive, a local bar in town, and rid Not Mike\'s cellar of the rodent infestation that plagues his establishment!\nYou travel across town as requested.\nYou enter the tavern called Mike\'s Dive. A grisled, middle-aged man stands behind the bar cleaning a mug. He greets you as you enter.')
    c1 = inpt("How will you approach your mission?\n1. Try to collect the rats souls\n2. Burn this mother down\n3.  Order a drink and get to work\nPlease select option 1, 2 or 3: ").strip()
    #To ensure valid selection
    ansck3(c1)
    if c1 == '1' :
        soulscaster() 
    elif c1 == '2' :
        prnt(f"Dear god, man. This place is awful. No wonder you have rats. The only true solution is to burn this whole place to the ground. Everyone, stand back. \n{titlec}I call upon the fires of the Nine Hells to aid me!\nAs you throw back the nearest table and raise your hands toward the sky, you feel the flames of the Nine Hells begin to fill your inner being. \nThe chaos lashes out in all directions, setting flame to the tables and chairs. Laughing with maniacal glee, you feel the warmth of the fire grow closer to your legs. \nThen, in a moment of realization and panic, your clothes catch fire. You burn to death with the rest of the patrons at Mike's Dive Tavern. You have chosen poorly and have failed the GAG-ME initiations. You died.")
        theend()
    #elif c1 == '3' :

def casterhidecellar():
    prnt("Hidden behind a stack of crates, you collect your thoughts and survey the area. You slowly raise your head over the crate to see if you can find the rat, but the creature is no where to be found. Slowly, you fully stand up to get a better view. \nA sharp pain strikes your ankle! The rats paw slid in between the crates to claw at you!\nYou throw up a magic shield to block any additional incoming damage. The rats claws at the magic shield and you gain enough time to prepare the next spell.\n Using gravity magic, you life the largest nearby crate into the air and then smash it down on the body of the rat. With a large crunch, the creature's neck is broken and it falls dead to the ground. With the battle having come to conclusion, you sit down on the ground to inspect your wound.\nYour ankle wound seems minimal. ")
    chc1 = inpt("What will you do?\n1. Bandage\n2. Harvest the rat\nPlease select option 1 or 2:")
    ansck2(chc1)
    if chc1 == '1':
        prnt("You bandage the wound on your ankle and report your mission as a success to Miss Shin Giver.\nYou safely make it back to the guild hall. The guild healer is attending to other patients, so you decide to wrap the leg up with clean bandages and get some rest.\nThe next morning, you visit Miss Shin Giver to receive your next test.  \nMiss Shin Giver: There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.  \nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
        chc2 = inpt("With your objective clear, what will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2:")
        ansck2(chc2)
        if chc2 == '1':
            prnt("You head directly to the sewer entrance.")
            quit()
        elif chc2 == '2':
            prnt("You head to the market to pick up supplies for your sewer run. The last thing you need is sewage getting into your leg wound.")
            quit()
    elif chc1 == '2':
        prnt("Limping, you make your way to the dead creature and harvest its heart and eyes for future spell components. \nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nYou safely make it back to the guild hall. The guild healer puts a new wrap on you leg and checks your for other wounds. You assure the healer that most of the blood is not from you and then report back to Miss Shin Giver. \nMiss Shin Giver: If you are up for it, there have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \nMiss Shin Giver:You do not have to engage. Here is a note with directions to the sewer entrance.")
        chc2 = inpt("With your objective clear, what will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2:")
        ansck2(chc2)
        if chc2 == '1':
            prnt("You head directly to the sewer entrance.")
            quit()
        elif chc2 == '2':
            prnt("You are not up for it! You need to get some rest and read your spellbook to identify what spells these components can be used for.")
            quit()
#souls tree caster
def soulscaster() :
    prnt(f"{titlec}Are you the tavern owner here? I have come to kill some critters and collect their souls for my patron. Could you guide me to their location?\nBartender: Collecting souls for your patron? They're rats. What do you want with rat souls? Do they even have souls? You know what? It doesn't matter. Why don't you follow me down to the cellar? \nHe leads you around the bar, through the tiny kitchen and into the cellar. He then excuses himself back to his duties.")
    souls = inpt("How will you proceed?\n1. Summon a feline familiar\n2. Create a protective rune\n3. Create some light\nPlease select option 1, 2 or 3: ").strip() 
    ansck3(souls)
    if souls == '1' :
        prnt("You hate rats. But rats hate cats. So the only option is to summon a demon cat familiar from the nether realms and set him loose.\nOne quick encantation later and a twisted tabby cat spawns to life. You command it to go deeper into the darkness and bring you the rat heads.\nAs the tabby cat dissappears into the darkness beyond, you begin to hear a low growl from the summoned feline entity. \nThe low growl turns into a series of hisses and then a screetch for help. \nA terrified cat comes barreling back into view and scampers behind your legs to hide.\nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        souls1 = inpt("How will you react?\n1. Sic the cat\n2. Run away\nPlease select option 1 or 2: ")
        ansck2(souls1)
        if souls1 == '1' :
            prnt("You command the cat to attack the giant rat and protect you.\nYour tabby cat rushes forward and attacks the giant rat. It does some serious kitty ninjutsu cool shit. \nThe creature gets distracted by the epic attacks and you have enough time to prepare your next spell. You fire off a blast of Magic Projectiles and it sparks an extra surge of wild magic! \nA Fireball trails after the Magic Projectiles and incinerates the back half of the rat. The tabby cat bounces happily back toward you and purs as it rubs against your leg. \nThis adventuring thing is going to be easy. Naming the tabby cat is going to be the hard part.")
            souls11 = inpt("With the danger gone, what will you do with the tabby cat?\n1. Dismiss the tabby cat\n2. Keep it and brainstorm names\nPlease selection option 1 or 2: ")
            ansck2(souls11)
            if souls11 == '1' :
                prnt("You dismiss the tabby cat back to the nether realms and harvest the heart and eyes of the giant rat for future spell components. Then, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15.\nMiss Shin Giver: There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
                souls111 = inpt("With your objective clear, what will you do?\n1. Get to work\n2. Go shopping\nPlease select option 1 or 2: ").strip()
                ansck2(souls111)
                if souls111 == "1" :
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif souls111 == '2' :
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()
            elif souls11 == '2' :
                prnt("You decide to keep the cat as a familiar. You test out a few names, 'Mittens', 'Buttons', 'Scrap', but none of them quite fit. \nYou'll have to think on it more. Then, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nAs you make your way back to the guild, your new kitty familiar sees something in an alley. It lets out a vicious hiss and then darts into the alley to attack whatever is in there.\n")
                souls112 = inpt("How will you react?\n1. Dismiss the tabby\n2. Help your companion\nPlease choose option 1 or 2: ")
                ansck2(souls112)
                if souls112 == '1' :
                    prnt("Cats are stupid after all and you don't have time for this. You dismiss the cat familiar and head back to the guild to report your mission success to Miss Shin Giver.")
                    quit()
                elif souls112 == '2' :
                    prnt("Oh no! The kitty is in trouble! Without hesitation, you dart into the alley to assist the kitty in its endeavor.")
                    quit()
        elif souls1 == '2' :
            prnt("This is not what you sign up for! You run away.\nYour fear of rats overwhelms you and you flee the cellar. You make it back to the guild barracks and tell them that you failed the mission. \nDisappointed in your performance, the guild dismisses you from duty and sends you home. Your patron still demands souls, but your failures haunt you and you are unable to fulfill your duties. \nWhile you sleep, your patron sends the tabby cat into your house to exact their penance. The tabby cat kills you without hesitation. You die.") 
            theend()
    elif souls == '2' :
        prnt("The cellar is dark and spooky, just the way you like it. You begin to draw magic runes on the cement floor. Any creature that steps on this rune is going to be incinerated with the fires of the Nine Hells.\nHaving completed the runework on the floor, you light a torch with the bright blue flame of the eternal souls, and then you begin further into the cellar. After a dozen careful steps through the clutter, you hear the growl of a large creature of some sort. \nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        souls2 = inpt("How will you react?\n1. Cast\n2. Run to the Runes\nPlease select option 1 or 2: ").strip()
        ansck2(souls2)
        if souls2 == '1' :
            prnt("You stand firm and begin casting Soul Blast on the creature.\nYou release the cast of your spell, but it is just a moment too late. The giant rat strikes you with its claw and carves into your left thigh. In an explosion of anger and adrenalyn, you thrust your right arm forward and cast Magic Projectiles. The energy darts shoot forward from your palm and blast the creature in several different places.\nThe creature lets out a cry of pain and then drops to the ground dead. You sit down on the ground to inspect your wound.")
            spellcellar()
        if souls2 == '2' :
            prnt("You quickly turn on your heels and run back toward the entrance of the cellar, and the runes.\nYou sprint back toward the door and jump over the runes that you placed on the floor. The giant rat that was quick on your heels does not make the same jump and steps directly on the runes. \nNecrotic tendrils shoot up from the ground and latch onto the rat. The rat collapses immediately to the ground and begins to dissolve before your eyes. Another soul has been paid toward your patron's debt.")
            souls22 = inpt("With the rat dead so quickly, you find yourself with a few moments before you need to report back. \nWhat will you do with your time?\n1. Harvest the rats bits\n2. Search the cellar for goodies\nPlease select option 1 or 2: ").strip()
            ansck2(souls22)
            if souls22 == '1' :
                prnt("The only thing that remains of the giant rat is its head. After a moments contemplation, you decide to harvest the eyes and tongue of the giant rat. You never know when you'll need good rat eyes for spell components. You wrap the loot in a rag and place the items in your satchel.\nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test.  \nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15. \nMiss Shin Giver : There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
                souls221 = inpt("You instructions clear, What will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2: ").strip()
                ansck2(souls221)
                if souls221 == '1' :
                    prnt("You head directly to the sewer entrance.")
                    quit()
                if souls221 == '2' :
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()
            elif souls22 == '2' :
                prnt("The rat menace of Mike's Dive has been eliminated with plenty of time to spare. You decide to spend some of that extra time searching through the cellar for potential goodies. \nA crate that was tucked away in the back of the cellar has the goodies you were looking for! A secret stache of 10 gold, which brings your total bankroll up to 20gp, a healing potion, and a magic pointy hat. You're not certain what the hat does yet, but you're sure you can figure it out.\nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver. You make your way back to the guild and report your mission success to Miss Shin Giver. \nMiss Shin Giver: If you are up for it, there have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.\nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
                souls222 = inpt("You instructions clear, What will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2: ").strip()
                ansck2(souls222)
                if souls222 == '1' :
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif souls222 == '2' :
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what this pointy hat does.")
                    quit()
    elif souls == '3' :
        prnt("It's a little too dark in this cellar. With a few well practiced encantations, you cast a light spell to get a better view of the cluttered cellar. No rats can hide forever.\nYou climb across crates, casting your create light spell and adding the bright blue flames of the eternal souls to different points on the ceiling and wall. \nPrimarily focused on the effort of casting the spells, you fail to see the monstrosity of a rat behind the crate you are standing on. \nIt isn't until the creatures lets out a blood curdling growl that you notice it tensing for an attack. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        souls31 = inpt("How will you react?\n1. Kick it\n2. Run\nPlease select option 1 or 2: ").strip()
        ansck2(souls31)
        if souls31 == '1' :
            prnt("You kick at the creature's mouth with your shoe.\nYour kick hits home but the rat does not seem to notice. The creature's mouth opens at the perfectly wrong time and clamps down on your foot. The bite sinks into you foot and you let out a howl of pain. \nIn an explosion of and adrenalyn, you thrust your right arm forward and cast Magic Projectiles. The energy darts shoot forward from your palm and blast the creature in several different places.\nThe creature lets out a cry of pain and then drops to the ground dead. You sit down on the ground to inspect your wound.Your wound is severe and you appear to have been infected by the bite.")
            souls311 = inpt("What will you do?\n1. Bandage\n2. Seek your patrons aid\nPlease select option 1 or 2: ").strip()
            ansck2(souls311)
            if souls311 == '1':
                prnt("With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs.With the infection rapidly taking hold, you slowly limp your way back to the lobby of the tavern. The concern on Not Mike's face is evident as he sees you enter the room. \nOn the far side of the tavern, a woman with close cropped hair and a larger than average nose empties the last of her ale mug. Even in your current state and from this distance, you can tell that she is intoxicated, but she also wears a Healer's Guild Ring.")
                souls3111 = inpt("What will you do?\n1. Get to GAG-Me\n2. Seek aid from the cleric").strip()
                ansck2(souls3111)
                if souls3111 == '1' :
                    prnt("You ignore the drunk patrons and head back to the guild for medical attention.")
                    quit()
                elif souls3111 == '2' :
                    prnt("With blurred vision, you stumble toward the cleric in hopes for healing.")
                    quit()
            elif souls311 == '2':
                prnt("Hesitantly, you pray to your patron for healing. You're already in debt to this god, so what's a few more souls owed? After a painful amount of time, the skin around the wound begins to repair itself. \nThe skin that now covers the wound is not human flesh. It appears to be scaly in nature. You're sure this is fine... right? You return to the GAG-ME barracks and report your mission success to Miss Shin Giver.")
                quit()
                
        elif souls31 == '2':
            prnt("You jump away from the creature and attempt to flee.\n")
            spellcellar()
    
def spellcellar():
    prnt("You sit down on the ground to inspect your wound.\nYour wounds are severe and there is heavy blood loss. ")
    spellcellar1 = inpt("What will you do?\n1. Bandage yourself\n2. Get help\nPlease select option 1 or 2: ")
    ansck2(spellcellar1)

    if spellcellar1 == '1':
        prnt("With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs.\nQuickly losing blood, you slowly limp your way back to the lobby of the tavern. The concern on Not Mike's face is evident as he sees you enter the room. On the far side of the tavern, a woman with close cropped hair and a larger than average nose empties the last of her ale mug. \nEven in your current state and from this distance, you can tell that she is intoxicated, but she also wears a Healer's Guild Ring.")
        spellcellar11 = inpt("What will you do?\n1. Get to the guild\n2. Seek healing from the cleric\nPlease select option 1 or 2: ")
        ansck2(spellcellar11)
        if spellcellar11 == '1':
            prnt("You ignore the drunk patrons and head back to the guild for medical attention.")
            quit()
        elif spellcellar11 == '2' :
            prnt("With blurred vision, you stumble toward the cleric in hopes for healing.")
            quit()
    elif spellcellar1 == '2':
        prnt("Hesitantly, you pray to your patron for healing. You're already in debt to this god, so what's a few more souls owed? After a painful amount of time, the skin around the wound begins to repair itself. \nThe skin that now covers the wound is not human flesh. It appears to be scaly in nature. You're sure this is fine... right?\nYou return to the GAG-ME barracks and report your mission success to Miss Shin Giver. As you leave the tavern, you notice that the sunlight is brighter and hurts your eyes. You wait for a moment for your sight to adjust, but it does not. You must have been in the cellar longer than you had originally thought. \nYou make your way back to the guild and report your mission success to Miss Shin Giver.\nMiss Shin Giver: If you are up for it, there have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.\n Miss Shin Giver:  You do not have to engage. Here is a note with directions to the sewer entrance.")
        spellcellar12 = inpt("What will you do?\n1. Get to work\n2. Rest first\n3. See a healer\n Please select option 1, 2 or 3: ")
        ansck3(spellcellar12)
        if spellcellar12 == '1' :
            prnt("You head directly to the sewer entrance.") 
            quit()
        elif spellcellar12 == '2' :
            prnt("You are NOT up for it! You need some rest. You go to your room and rest on your bunk. You can deal with the sewer creature after some sleep.")
            quit()
        elif spellcellar12 == '3':
            prnt("You are sort of up for it. You decide to head to the sewer, but only after making a pitstop at the healer to see about this blinding sunlight issue and have them double check your leg.")
            quit()
        #elif souls2 == '2' :
    #elif souls == '3' :

def mage():
    prnt("I will take two shots of your finest whiskey and directions to the cellar. There are rodents that shall meet their doom this evening.\nThe bartender pours two shots of what can only be described as wagon wheel grease and then escorts you around the bar, through a tiny ktchen, and into the cellar. He then excuses himself back to his duties.")
    magetree = inpt("How will you deal with the infestation?\n1. Some light and a spell\n2. Try to tame the rats\r3. Summoning\nPlease select option 1, 2 or 3:")
    ansck3(magetree)
    if magetree == 1:
        prnt("Noticing the cellar is dark, you pull a torch from your pack and light it. With a spell readied in one hand and torch in the other, you make your way toward the back of the cluttered cellar.\nThe noisy bar patrons upstairs drown the sound of your footsteps as you make your way through the cluttered mess.\nThe torchlight flickers and steadies as you come into view of a large rodent of unusual size. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        mage1 = inpt("How will you react?\n1. Torch\n2. Spell\nPlease select option 1 or 2:")
        ansck2(mage1)
        if mage1 == '1':
            prnt("You swing your torch at the creature.\nThe torch strikes the rat's face, but it does minimal damage and the creature recovers quickly. With a ferocious roar, the rat leaps at you and sinks it's teeth into your left arm. It tears away a large chunk of flesh as it lands on the ground next to your feet. \nYou let out a scream of pain and drop the torch to the ground. \nIn an explosion of anger and adrenalyn, you thrust your right arm forward and cast magic projectiles. The energy darts shoot forward from your palm and blast the creature in several different places. 'nThe creature lets out a cry of pain and then drops to the ground dead. ")
            spellcellar()
        elif mage1 == '2':
            prnt("You cast your prepared Fireblast at the creature.\nYou release the cast of your spell, but it is just a moment too late. The giant rat strikes you with its claw and carves into your left thigh. \nIn an explosion of anger and adrenalyn, you thrust your right arm forward and cast Magic Projectiles. The energy darts shoot forward from your palm and blast the creature in several different places.\nThe creature lets out a cry of pain and then drops to the ground dead. ")
            spellcellar()
    elif magetree == 2:
        prnt("Finally alone, you know exactly what to do. Nana told you stories about Fleter Floutist that played to flute to lead the rats away from town, and you have an instrument of your own. You pull the kazoo from your pack and begin playing.\nThe notes from your kazoo fill the air, drowning out the noises from the bar patrons above.\nJust at the point of crescendo, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height.\n It releases a gurgling hiss and pounces toward you.")
        mage1 = inpt("What do you think?\n1. It's not working\n2. It's working\nPlease select option 1 or 2:")
        ansck2(mage1)
        if mage1 == 1:
            prnt("You think it's not working! You run and take cover.")
            casterhidecellar()
        elif mage1 == 2:
            prnt("You think it's totally working! You continue to play and walk backward toward the door.\nYou continue to kazoo your tune as you turn your back to the rat and lead it out of the cellar. Unfortunately, your Nana's stories may have been exaggerated. The rat jumps on your back and begins biting your neck. You die. \nThe Global Adventurer's Guild creates an award for your labeled \"Dumbest Death Award\" and they hang it on the barracks wall.")
            theend()
    elif magetree == 3:
        prnt("Time to fight fire with fire. You begin casting the same spell you cast at Cousin Larry's wedding. Summoned with magical powers, a swarm of your own rats appear around you. They follow you as you move slowly further into the cellar.\nWith your rat army prepared for rat war, you confidently move toward the back of the cellar. As you near the back wall, you begin to hear a deep growl from the darkness ahead. \nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        mt31 = inpt("What will you do?\n1. Attack\n2. Run\nPlease select option 1 or 2: ")
        if mt31 == "1":
            prnt("You command your rat army to attack! Your rat army rushes forward and attacks the giant rat. The creature gets distracted by the horde of tiny rats, and you have enough time to prepare your next spell. \nYou blast the rat with a spell you call the Cone of Ice Scream and shards of sharp ice blast the rat in the head and chest. The rat collapses immediately to the ground. Another soul has been paid toward your patron's debt.\nYou dismiss the army of rats and think fondly of Cousing Larry's wedding. After a moment of reflection, you decide to harvest the heart and eyes of the giant rat for future spell components. \nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver. \nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 15.")
            mt311 = inpt("What will you do now?\n1. Harvest spell components\n2. Loot the room\nPlease select option 1 or 2: ")
            if mt311 == '1':
                prnt("You dismiss the army of rats and think fondly of Cousing Larry's wedding. After a moment of reflection, you decide to harvest the heart and eyes of the giant rat for future spell components. \nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 15.\nMiss Shin Giver: There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \nMiss Shin Giver: You do not have to engage. Here is a note with directions to the sewer entrance.")
                mt3111 = inpt("What will you do now?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2:")
                if mt3111 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif mt3111 == '2':
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()        
            elif mt311 == "2":           
                prnt("The rat menace of Mike's Dive has been eliminated with plenty of time to spare. You decide to spend some of that extra time searching through the cellar for potential goodies. \nA crate that was tucked away in the back of the cellar has the goodies you were looking for! A secret stache of 10 gold, which brings your total bankroll up to 20gp, a healing potion, and a magic pointy hat. You're not certain what the hat does yet, but you're sure you can figure it out.\nWith your new magic item tucked safely away in your pack, you travel back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \nMiss Shin Giver: Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 25. ")
                mt3112 = inpt("What will you do now?\n1. Get to work\n2. Go to the magic shop first\nPlease select option 1 or 2: ")
                if mt3112 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif mt3112 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what this pointy hat does.")
                    quit()
        elif mt31 == '2':
            prnt("This rat it too big! You turn and run away.")
            casterhidecellar()
            
#Rogue trees
def rogue():
    print(f"{titler}I shoot people from the shadows using a crossbow, but I'm really sorry about it.\n{msg}So you're a sneaky one? Great! Ready your bow and prepare for your first task.\n{titler}Ugh. I traveled all day. Do I have time to take a shower first?\n{msg}No. You must travel to Mike's Dive, a local bar in town, and rid Not Mike's cellar of the rodent infestation that plagues his establishment!\nYou travel across town as requested. You enter the tavern called Mike's Dive. A grisled, middle-aged man stands behind the bar cleaning a mug. He greets you as you enter.")
    r1 = inpt("Now that you've arrived how will you approach the problem?\n1. Direct\n2. On a full stomach\n3. With some levity\n Please select option 1, 2 or 3:")
    if r1 == '1':
        thief()
    elif r1 == '2':
        prnt(f"{titler}What is that intoxicating aroma? Is someone cooking in the back? I'll take a large order of stew.\nThe bartender looks you up and down with a concerned expression and then disappears into the kitchen. Within moments, he is back with a simmering bowl of stew and a chunk of harden bread. He sets both on the counter and then begins to pour you a mug of ale. He sits the mug in front of you.\nNot Mike: The ale is on the house. You're going to need it.\nThe stew itself has a chorus of new and interesting flavors. Just before the last bite of stew is enters your mouth, you feel the rumble in your stomach. The violent gurgles of bubbling innards signals that it may be time to visit the privvy.\nAfter nine hours of absolutely destroying the outhouse in the most unholy fashion imaginable, you collapse to the earth just outside the tavern and pass out due to exhaustion.\nYou have chosen poorly and have failed the GAG-ME initiations. You must return home in disgrace.")
        theend()
    elif r1 == '3':
        puns()

def thief():
    prnt(f"{titler}Hi there. I was hired to come to your bar and kill some rodents. Could you show me to your cellar?\nNot Mike: Thank the twelve gods you're here. Please, follow me this way. I'll take you right to where the problem festers.\nHe leads you around the bar, through the tiny kitchen and into the cellar. He then excuses himself back to his duties.")
    th1 = inpt("How will you handle the infestation?\n1. Make some light\n2. Sneak\n3. Bait\nPlease select option 1, 2 or 3: ")
    if th1 == '1':
        prnt("Noticing the cellar is dark, you pull a torch from your pack and light it. A crossbow will not be very effective against the tiny creatures, so by the light of the torch, you start constructing a makeshift trap to capture the vermin.\nHaving completed the trap on the floor, you begin further into the cellar. After a dozen careful steps through the clutter, you hear the growl of a large creature of some sort. Just then, a rodent of unusual size bursts from behind a crate and comes into view. \nIt's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        th2 = inpt("How will you react?\n1. Torch\n2. Run\nPlease select option 1 or 2 :")
        if th2 == '1':
            prnt("You stand firm and swing your torch at the creature.\nThe torch strikes the rat's face, but it does minimal damage and the creature recovers quickly. With a ferocious roar, the rat leaps at you and sinks it's teeth into your left arm.\nIt tears away a large chunk of flesh as it lands on the ground next to your feet. You let out a scream of pain and drop the torch to the ground. \nIn an explosion of anger and adrenalyn, you draw your dagger and thrust it into the eye of the giant rat. The creature lets out a cry of pain and then drops to the ground dead. \nYou sit down on the ground to inspect your wound.\n Your arm wound is severe and you appear to have been infected by the bite.")
            th3 = inpt("What will you do?\n1. Bandage\n2. Search for treatment in the basement\nPlease select option 1 or 2: ")
            if th3 == '1':
                prnt("You bandage your arm wound and return to the GAG-ME barracks to report your mission as a success to Miss Shin Giver.\nYou safely make it back to the guild hall, but the infection sets in fast. The guild healer sees to your wounds and administers a poultice. After a good night's rest, the healer says that you are fit enough to carry on with more mission tests, but you will be sickly for the next week or so. \nIt is recommended that you return to the healer if the infection does not go away within 3 days.You visit Miss Shin Giver to receive your next test. \n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.\n{msg} You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Stop by a shop\nPlease select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("With hopes of purchasing a cure for your ailment, you decide to make a stop at the local alchemist first.")
                    quit()
            elif th3 == '2':
                prnt(" You begin looking through crates and boxes to see if you can find something to treat the wound.\nAs you search through the crates, a wave of dizziness hit you. The infection has spread quickly and the room spins. You collapse onto the floor and the world goes black. The infection spreads and you die.")
                theend()
        elif th2 == '2':
            prnt("You quickly turn on your heels and run back toward the entrance of the cellar, and the trap.\nYou sprint back toward the door and jump over the trap that you placed on the floor. The giant rat that was quick on your heels does not make the same jump and steps directly on the trap. While the trap was designed for much smaller prey, it somehow still works by closing in on the front leg of the creature. \nThe creature falls to the ground, giving you enough time to load and fire your cross bow point blank into the creature's skull.")
            th3 = inpt("With your mission accomplished what will you do?\n1. Back to GAG-ME\2. Loot the cellar\n Please select option 1 or 2:")
            if th3 == '1':
                prnt(f"The mission is complete and you took no injuries. You wonder if there is a reward for being the first initiate back after the first mission. You run as fast as you can back to the GAG-ME barracks to report your success back to Miss Shin Giver.\nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 15.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Go shopping first\n Please select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()
            elif th3 == '2':
                prnt(f"The rat menace of Mike's Dive has been eliminated with plenty of time to spare. You decide to spend some of that extra time searching through the cellar for potential goodies.\nA crate that was tucked away in the back of the cellar has the goodies you were looking for! A secret stache of 10 gold, which brings your total bankroll up to 20gp, a healing potion, and a quiver stocked with 10 magic arrows. You're not certain what each arrow does yet, but you're sure you can figure it out. \nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\n\n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 25.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Go shopping first\n Please select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what these 10 magic arrows do.")
                    quit()
    elif th1 == '2':
        prnt("Quietly, you tip-toe through the cluttered cellar, being certain not to step on anything that would make a noise and startle the rats. The trick is to find the nest and catch them by surprise.\nQuieter than a mouse, you creep through the cellar. Your eyes begin to adjust to the darkness in the room and you make out a set of large crates at the back of the room.\nYou sneakily round the corner of a large crate and find a rodent of unusual size gnawing at something on the ground. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. By the mercy of the gods, it didn't notice you and you have the element of surprise!")
        th2 = inpt("How will you deal with the rat?\n1. Dagger\n2. Crossbow\nPlease select option 1 or 2:")
        if th2 == '1':
            prnt("You draw your dagger and sneak attack this monstrosity!\nYou attack with your dagger, but the blade misses the beasts spine and does not kill the creature. The giant rat turns and strikes you with its claw, carving into your left thigh. \nDagger still in hand, you slash at the rat. You exchange blows with each other until the rat finally collapses to the ground. You are victorious, but at a cost. \nYou have sustained several injuries, but luckily none of them were bites. The last thing you need is to catch a disease on your first mission. Breathing heavily, you assess your wounds.\nYour wounds are severe and there is heavy blood loss.")
            th3 = inpt("What will you do?\n1. Bandage\n2. Seek healing\n Please select option 1 or 2:")
            if th3 =='1':
                prnt(f"With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs. You return to the GAG-ME barracks and report your mission success to Miss Shin Giver.As you make your way back to the barracks, the world begins to spin around your. The bloodloss has taken its toll and you crumble to the ground unconcious. You awake back at the guild hall. You appear to be in the medica, resting in one of the beds. The healer approaches you to tell you that someone found you passed out on the street. \nYour money was stolen before the good samaritan found you and brought you back to the guild. Probably some thieving street urchins. You have been asleep for two days, but if you are feeling up for it, Miss Shin Giver has a new quest for you.\n{msg}I am glad to see you back on your feet. If you're feeling up to the task, I have a new quest for you. There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Look for your gold\nPlease select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("You head back to the streets to find out which thief stole your gold.")
                    quit()
            elif th3 == '2':
                prnt(f"You limp back upstairs and approach the nearest group of people.\n {titler}Healer? Is anyone here a healer?\nA woman with close-cropped hair and a larger than average nose: I'm a healer. \nRelieved to have such a stroke of good fortune, you make your way toward her table. She looks you up and down as you approach, but you can tell from her motions that she is intoxicated. I \nHealer: I don't have healing powers left today. If you need help, I'll sell you one of my potions for 8 gold pieces.")
                th4 = inpt("What will you do?\n1. Pay\n2. Charm\nPlease select option 1 or 2:")
                if th4 == '1':
                    prnt("Reluctantly, you give the drunk healer your 8 gold pieces.")
                    quit()
                elif th4 == '2':
                    prnt(f"With all the charm that you can muster, you smile at her\n{titler}I do not have any money at the moment, but if you do this for me, I will owe you a favor. I'll do anything you please as long as it doesn't involve quitting the Global Adventurer's Guild.")
                    quit()
        elif th2 == '2':
            prnt("You draw and load your crossbow, then you sneak attack this monstrosity!\nWith a steady hand and a clear shot, you left fly the crossbow bolt. It strikes true and hits the creature directly between the eyes. It falls limp to the ground a twitches a couple times. This adventuring thing is going to be a piece of pie.")
            if th3 == '1':
                prnt(f"The mission is complete and you took no injuries. You wonder if there is a reward for being the first initiate back after the first mission. You run as fast as you can back to the GAG-ME barracks to report your success back to Miss Shin Giver.\nYou safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 15.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Go shopping first\n Please select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()
            elif th3 == '2':
                prnt(f"The rat menace of Mike's Dive has been eliminated with plenty of time to spare. You decide to spend some of that extra time searching through the cellar for potential goodies.\nA crate that was tucked away in the back of the cellar has the goodies you were looking for! A secret stache of 10 gold, which brings your total bankroll up to 20gp, a healing potion, and a quiver stocked with 10 magic arrows. You're not certain what each arrow does yet, but you're sure you can figure it out. \nThen, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver.\n\n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse. \nThis brings your total gold count to 25.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Go shopping first\n Please select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what these 10 magic arrows do.")
                    quit()
    elif th1 == '3':
        prnt("You unwrap the wheel of moldy cheese that you stole from the kitchen as you passed through. Just as you hoped, the smell of the cheese is rancid. You begin crumbling the cheese and letting it drop to the floor around you. This should bring the vermin out of hiding.Noiselessly, you make your way deeper into the cellar, sprinkling cheese crumbs along the way. After a dozen careful steps through the clutter, you hear the growl of a large creature of some sort. \nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        th2 = inpt("How will you react?\n1. Fight\n2. Run\nPlease select option 1 or 2:")
        if th2 == '1' :
            prnt("You drop your cheese and load your crossbow. \nYou load your crossbow, but it is just a moment too late to squeeze a shot off. The giant rat strikes you with its claw and carves into your left thigh. \nCrossbow still in hand, you drop to the ground and take aim. You fire the crossbow point blank and strike the rat directly in the head. The creature falls dead onto the lower half of your body.  \nBreathing heavily, you push the creature off your persons and sit up in order to assess your wounds. Your wounds are severe and there is heavy blood loss.")
            th3 = inpt("What will you do?\n1. Bandage\n2. Seek healing\n Please select option 1 or 2:")
            if th3 =='1':
                prnt(f"With shaky hands, you bandage the thigh wound as tightly as possible and begin to limp back up the stairs. You return to the GAG-ME barracks and report your mission success to Miss Shin Giver.As you make your way back to the barracks, the world begins to spin around your. The bloodloss has taken its toll and you crumble to the ground unconcious. You awake back at the guild hall. You appear to be in the medica, resting in one of the beds. The healer approaches you to tell you that someone found you passed out on the street. \nYour money was stolen before the good samaritan found you and brought you back to the guild. Probably some thieving street urchins. You have been asleep for two days, but if you are feeling up for it, Miss Shin Giver has a new quest for you.\n{msg}I am glad to see you back on your feet. If you're feeling up to the task, I have a new quest for you. There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                th4 = inpt("What will you do?\n1. Get to work\n2. Look for your gold\nPlease select option 1 or 2:")
                if th4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif th4 == '2':
                    prnt("You head back to the streets to find out which thief stole your gold.")
                    quit()
            elif th3 == '2':
                prnt(f"You limp back upstairs and approach the nearest group of people.\n {titler}Healer? Is anyone here a healer?\nA woman with close-cropped hair and a larger than average nose: I'm a healer. \nRelieved to have such a stroke of good fortune, you make your way toward her table. She looks you up and down as you approach, but you can tell from her motions that she is intoxicated. I \nHealer: I don't have healing powers left today. If you need help, I'll sell you one of my potions for 8 gold pieces.")
                th4 = inpt("What will you do?\n1. Pay\n2. Charm\nPlease select option 1 or 2:")
                if th4 == '1':
                    prnt("Reluctantly, you give the drunk healer your 8 gold pieces.")
                    quit()
                elif th4 == '2':
                    prnt(f"With all the charm that you can muster, you smile at her\n{titler}I do not have any money at the moment, but if you do this for me, I will owe you a favor. I'll do anything you please as long as it doesn't involve quitting the Global Adventurer's Guild.")
                    quit()
        elif th2 == '2' :
            prnt("You throw the cheese at the creature and run back toward the entrance.\nRunning through the dark, you forget the bags of potatoes that lay on the floor between you and the exit. You trip and collapse to the floor, knocking the wind out of your chest. You brace yourself for the attack, but it doesn't come. Bravely, you turn your head back and open your eyes. \nThe rat is gone. You breathe out a sigh of relief and then start to climb back to your feet. That's when the low growl comes from just behind your head. \nYou turn back toward the exit to find a snarling giant rat that promptly takes a bite of your face. You die.")
            theend()

def puns() :
    prnt(f"\n{titler}Mike, is it? Do you know what a rat's favorite game is? \n{titler}Cocks Crossbow \n{titler}Hide and Squeak. Now, show me where they're hiding.\nThe bartender lets out an audible groan signifying his displeasure with your joke, and then takes a long drink from the mug of ale he was filling for a customer. Af long akward moment passes.\nNot Mike: Follow me. \nHe leads you around the bar, through the tiny kitchen and into the cellar. He then excuses himself back to his duties.")
    p1 = inpt("How will you proceed?\n1. Scavange\n2. Get some light\n3. Cautious\n Please select option 1, 2 or 3:")
    if p1 == '1':
        prnt("You begin looking through the crates and bags that lay around the cellar. Maybe there are rats in them, or maybe something even better. The bartender probably shouldn't have left you alone in here.\nYou hit the jackpot! One of the crates is holding 50 gold pieces, a healing potion, and a magic dagger! It would be reasonable to believe that the rats stole these before you got here, right? \nJust as you are placing the last of your findings into your coin pouch, you hear a growl behind you.\n A rodent of unusual size bursts from behind a nearby crate. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        p2 = inpt("What will you do?\n1. Dodge\n2. Draw\nPlease select option 1 or 2:")
        if p2 == '1':
            prnt("Surprised by the creature, you dive to the side to avoid the attack.\nYou dive behind a stack of crates where you collect your thoughts and survey the area. You load your crossbow and then slowly raise your head over the crate to see if you can find the rat. The creature is no where to be found. \nSlowly, you fully stand up to get a better view. \nA sharp pain strikes your ankle! The rats paw slid in between the crates to claw at you!\nInstinctively, you roll onto the crate and lean over the edge to get a clear shot at the rat. You fire the crossbow point blank and strike the rat directly in the head. \nThe creature slumps over to the ground dead. With the battle having come to conclusion, you sit down on the ground to inspect your wound. Your ankle wound seems minimal. ")
            p3 = inpt("What will you do\n1. Bandage\n2. Inspect the dagger\nPlease select option 1 or 2: ") 
            if p3 == '1':
                prnt(f"You bandage the wound on your ankle and report your mission as a success to Miss Shin Giver.You safely make it back to the guild hall. The guild healer is attending to other patients, so you decide to wrap the leg up with clean bandages and get some rest. The next morning, you visit Miss Shin Giver to receive your next test.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                p4 = inpt("What will you do?\n1. Get to work\n2. Shop\nPlease select option 1 or 2:")
                if p4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif p4 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what this magic dagger does.")
                    quit()
            elif p3 == '2':
                prnt(f"Something strange about this dagger catches your attention. You decide to investigate the dagger and see what is different about it.\nThe dagger seems to have magic properties, but you do not recognize the arcane runes that are etched into the blade. It looks like you're going to have to figure it out by testing the dagger, or take it to a magic dealer. There is an incantation on the base of the handle. This incantation reads, ")
                prnt("Together, forever, we shall be.\nIn terror, our enemies will flee.\nWeapons and treasures may flow free.\nBut you shall have none but me.").title()
                p4 = inpt("What will you do?\n1. Read it aloud\n2. Nope. Nope. Nuh uh.\nPlease select option 1 or 2: ")
                if p4 == '1':
                    prnt("You decide to chant the incantation out loud three times.")
                    count = 0
                    while count < 3:
                        prnt(f"{titler}Together, forever, we shall be.\n{titler}In terror, our enemies will flee.\n{titler}Weapons and treasures may flow free.\n{titler}But you shall have none but me.").title()
                        count = count + 1
                    quit()
                elif p4 =='2':
                    prnt("You decide not to speak the incantation aloud. It seems dangerous. Ankle now bandaged, you decide to head back to the guild and store the dagger away for safe keeping. You need to report your mission success back to Miss Shin Giver.")
                    quit()
        elif p2 == '2':
            prnt("Surprised by the creature, you draw your newly found dagger. The creature lands on you as you plunge the dagger into the creature's side. \nThe blow isn't fatal and the giant rat takes a bite out of your right shoulder. You howl in pain as you stab the dagger in and out of the creature's side. The creature spits out a mixture of blood and phlegm on your face before it pulls itself off you. \nThe giant rat limps a few steps away and collapses. Breathing heavily, you watch the creature closely for a long moment to make sure it no longer is breathing, then you and assess your wounds. \nYour arm wound is severe and you appear to have been infected by the bite. Something strange about this dagger catches your attention.")
            p3 = inpt("What will you do\n1. Bandage\n2. Inspect the dagger\nPlease select option 1 or 2: ") 
            if p3 == '1':
                prnt(f"You decide to ignore it for the time being, bandage your arm wound, and return to the GAG-ME barracks to report your mission as a success to Miss Shin Giver.\nYou safely make it back to the guild hall, but the infection sets in fast. The guild healer sees to your wounds and administers a poultice. After a good night's rest, the healer says that you are fit enough to carry on with more mission tests, but you will be sickly for the next week or so. It is recommended that you return to the healer if the infection does not go away within 3 days. You visit Miss Shin Giver to receive your next test.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                p4 = inpt("What will you do?\n1. Get to work\n2. Shop\nPlease select option 1 or 2:")
                if p4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif p4 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what this magic dagger does.")
                    quit()
            elif p3 == '2':
                prnt(f"You decide to investigate the dagger and see what is different about it.\nThe dagger seems to have magic properties, but you do not recognize the arcane runes that are etched into the blade. It looks like you're going to have to figure it out by testing the dagger, or take it to a magic dealer. There is an incantation on the base of the handle. This incantation reads, ")
                prnt("Together, forever, we shall be.\nIn terror, our enemies will flee.\nWeapons and treasures may flow free.\nBut you shall have none but me.").title()
                p4 = inpt("What will you do?\n1. Read it aloud\n2. Nope. Nope. Nuh uh.\nPlease select option 1 or 2: ")
                if p4 == '1':
                    prnt("You decide to chant the incantation out loud three times.")
                    count = 0
                    while count < 3:
                        prnt(f"{titler}Together, forever, we shall be.\n{titler}In terror, our enemies will flee.\n{titler}Weapons and treasures may flow free.\n{titler}But you shall have none but me.").title()
                        count = count + 1
                    quit()
                elif p4 =='2':
                    prnt("You decide not to speak the incantation aloud. It seems dangerous. Arm now bandaged, you decide to head back to the guild and store the dagger away for safe keeping. You need to report your mission success back to Miss Shin Giver.")
                    quit()         
    elif p1 == '2':
        prnt("Noticing the cellar is dark, you pull a torch from your pack and light it. With crossbow in one hand and torch in the other, you make your way toward the back of the cluttered cellar.\nAfter a dozen careful, soundless steps through the clutter, you hear the growl of a large creature of some sort. \nJust then, a rodent of unusual size bursts from behind a crate and comes into view. It's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. \nIt releases a gurgling hiss and pounces toward you.")
        p2 = inpt("How will you react?\n1. Torch\n2. Crossbow\nPlease select option 1 or 2: ")
        if p2 =='1':
            prnt(f"You swing your torch at the creature.\n{titler}You're fired.\nThe torch strikes the rat's face. \nThe torch does minimal damage and the creature recovers quickly. With a ferocious roar, the rat leaps at you and sinks it's teeth into your left arm. \nIt tears away a large chunk of flesh as it lands on the ground next to your feet. You let out a scream of pain and drop the torch to the ground. \nIn an explosion of anger and adrenalyn, you draw your dagger and thrust it into the eye of the giant rat. The creature lets out a cry of pain and then drops to the ground dead. You sit down on the ground to inspect your wound.\nYour arm wound is severe and you appear to have been infected by the bite.")
            p3 = inpt("What will you do?\n1. Bandage\n2. Search the basement\nPlease select option 1 or 2: ")
            if p3 == '1':
                prnt(f"You bandage your arm wound and return to the GAG-ME barracks to report your mission as a success to Miss Shin Giver.\nYou safely make it back to the guild hall, but the infection sets in fast. The guild healer sees to your wounds and administers a poultice.\nAfter a good night's rest, the healer says that you are fit enough to carry on with more mission tests, but you will be sickly for the next week or so. \nIt is recommended that you return to the healer if the infection does not go away within 3 days. You visit Miss Shin Giver to receive your next test. \n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild.\n{msg} You do not have to engage. Here is a note with directions to the sewer entrance.")
                p4 = inpt("What will you do?\n1. Get to work\n2. Go shopping\nPlease select option 1 or 2:")
                if p4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif p4 == '2':
                    prnt("With hopes of purchasing a cure for your ailment, you decide to make a stop at the local alchemist first.")
                    quit()
            elif p3 == '2':
                prnt("You begin looking through crates and boxes to see if you can find something to treat the wound.\nAs you search through the crates, a wave of dizziness hit you. The infection has spread quickly and the room spins. You collapse onto the floor and the world goes black. The infection spreads and you die.")
                theend()
        elif p2 == '2':
            prnt(f"You shoot the crossbow bolt at the creaure.\n{titler}You had better...bolt!\nYou fire the crossbow point blank and strike the rat directly in the head. The creature slumps over to the ground dead.\n You spin the crossbow around in a circle and hum your personal victory tune. \n{titler}Doo doo doo dunnn dunnn dun dundun!\nThe mission is complete and you took no injuries. You wonder if there is a reward for being the first initiate back after the first mission. You run as fast as you can back to the GAG-ME barracks to report your success back to Miss Shin Giver.You safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15.\n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. \n{msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
            p3 = inpt("What will you do?\n1. Get to work\n2. Go shopping\nPlease select option 1 or 2: ")
            if p3 == '1':
                prnt("You head directly to the sewer entrance.")
                quit()
            elif p3 == '2':
                prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                quit()
    elif p1 == '3':
        prnt("With all the clutter on the ground, the rats could be hiding anywhere. You know that they're icky and full of diseases, so you climb on top of the nearest box you can find and begin scanning the darkness, looking for signs of pests.\nYou make your way from crate to crate, never touching the floor, until you near the back of the cellar. From your vantage point, you can see a rodent of unusual size gnawing at something on the ground.\nIt's sickly green eyes indicate a disease of sorts. The giant rat easily reaches your waist level in height. By the mercy of the gods, it didn't notice you and you have the element of surprise!")
        p2 = inpt("What will you do?\n1. Shoot it\n2. Escape\nPlease select option 1 or 2: ")
        if p2 == '1':
            prnt("You shoot the crossbow bolt at the creaure.With a steady hand and a clear shot, you left fly the crossbow bolt. It strikes true and hits the creature directly between the eyes. It falls limp to the ground a twitches a couple times. This adventuring thing is going to be a piece of pie.\n")
            p3 = inpt("With your foe vanquised, what will you do?\n1. Report back\n2. Search the cellar\nPlease select option 1 or 2:")
            if p3 == '1':
                prnt(f"The mission is complete and you took no injuries. You wonder if there is a reward for being the first initiate back after the first mission. You run as fast as you can back to the GAG-ME barracks to report your success back to Miss Shin Giver.You safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15. \n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. {msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                p4 = inpt("What will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2: ")
                if p4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif p4 == '2':
                    prnt("With 15 gold pieces in your coin purse, you decide to stop by the market before heading to the sewer entrance. Let's see what 15GP will get you!")
                    quit()
            elif p3 == '2':
                prnt(f"The rat menace of Mike's Dive has been eliminated with plenty of time to spare. You decide to spend some of that extra time searching through the cellar for potential goodies.\nA crate that was tucked away in the back of the cellar has the goodies you were looking for! A secret stache of 10 gold, which brings your total bankroll up to 20gp, a healing potion, and a quiver stocked with 10 magic arrows. \nYou're not certain what each arrow does yet, but you're sure you can figure it out. Then, you return to the GAG-ME barracks and report your mission success to Miss Shin Giver. You safely make it back to the GAG-ME barracks and visit Miss Shin Giver to receive your next test. \n{msg}Well, aren't you just the overachiever. Great work on being so quick. Here's a bonus of 5 gold pieces to add to your coin purse.\nThis brings your total gold count to 15. \n{msg}There have been complaints about a creature in the sewer eating people's pets. Your assignment is to discover what the creature is and potentially where it resides, then report back to the guild. {msg}You do not have to engage. Here is a note with directions to the sewer entrance.")
                p4 == inpt("What will you do?\n1. Get to work\n2. Go shopping first\nPlease select option 1 or 2: ")
                if p4 == '1':
                    prnt("You head directly to the sewer entrance.")
                    quit()
                elif p4 == '2':
                    prnt("You decide to stop by a magic item dealer on your way to the sewer. You want to find out what these 10 magic arrows do.")
                    quit()
        elif p2 == '2':
            prnt("This is not what you signed up for. You turn around and sneak back out of the cellar. Your fear of rats overwhelms you and you flee the cellar. You make it back to the guild barracks and tell them that you failed the mission. \nDisappointed in your performance, the guild dismisses you from duty and sends you home. After leaving the guild with nothing more than the a bed roll and a sack of coins, you begin the long journey home. \nAlong the way, a band of young children meet you on the streets and ask you for coins. When you tell them that you do not have any coins to spare, they stab you.\nA lot. \nYou die.")
            theend()


#utilty functions
#Make text right speed
def prnt(str) :
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#make input text match print text speed
def inpt(str) :
    if '3' in str: a = 1
    else :  a = 2
    for letter in str:
        if letter != ':':
            sys.stdout.write(letter)
            time.sleep(0.05)
            sys.stdout.flush()
        else : 
            prnt(': ') 
            break    
    if a == 1:
        str = input("")
        str = ansck3(str)
        return str
    else:
        str= input("")
        str = ansck2(str)
        return str
def textinput(str)   :
    for letter in str:
        if letter != ':':
            sys.stdout.write(letter)
            time.sleep(0.05)
            sys.stdout.flush()
        else : 
            prnt(': ') 
            break    
    str = input("").lower().strip()
    return str
#Parse options to make coding faster
def choice(str):
    str = str.replace("1", "\n1.").replace("2","\n2.").replace("3","\n3.")
    prnt("\nWhat will you do?" + str)
    if '3' in str: 
        str = inpt("\nPlease select option 1, 2, or 3: ")
        return str
    else:
        str = inpt("\nPlease select option 1 or 2: ")
        return str
#Functions to verify valid entry
def ansck2(str) :
    while str != '1' and str != '2' :
        str = input("Sorry, I need you to type 1 or 2: ").strip().lower()
        return str
    return str
def ansck3(str) :
    while str != '1' and str != '2' and str != '3' :
        str = input("Sorry, I need you to type 1, 2 or 3: ").strip().lower()
        return str  
    return str
#End screen
def theend() :
    time.sleep(3)
    prnt("\nTHE END")
    time.sleep(5)
    quit()
def win():
    prnt(f"You return to GAG-ME with Pan Dora’s Box. Miss Shin Giver greets you at the door and calls attention to all current initiates. \n{msg}You have successfully completed your mission and will now graduate as a full guild member! \nMiss Shin Giver rewards you with a purse filled with 200 gold pieces and your own GAG-ME cloak with the Cheddar division emblem embroidered on the back. \nCongratulations {name.capitalize()} you have officially completed training! Welcome to GAG-ME!")
    theend()

#start
name = textinput("Hello! What's your name: ")
titlef = (f"{name.capitalize()} the Valiant: ")
titlec = (f"{name.capitalize()} the Wise: ")
titler = (f"{name.capitalize()} the Clever: ")
msg = "Miss Shin Giver: "
pd = "Pan Dora: "
beginning()
