from sys import exit

def diamond_vault():
    print("This room is full of diamonds and richities, how much do i take?")
    
    next = input(" >")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        print("Hmmmm, maybe i should take not anything and be a good boy!")
        print("OH NO!, IM BUSTED, the police are here what do i do?")
        print("1. Fight the police")
        print("2. RUN!")
        
        police = input(" >")
        
        if police == "1":
            print("You try to fight the cops but they overpower you, yer now stuck in a prison cell")
            print("Hold on, you get a box, a package and you open it, there's a note saying escape using the items, -d, although after you use one the rest disappear, choose well my friend")
            print("A. Metal breaker")
            print("B. Cop stunner")
            print("C. Teleporter")
            print("What do you choose?")
            
            jailbreak = input(" >")
            
            if jailbreak == "A":
                print("The metal breakers just a plastic toy, Bad luck my dude!")
            if jailbreak == "B":
                print("Hey cop, get over! here you say")
                print("What do ya want he says, look closely you say as he gets hypnotized, Now! Give me the keys boy, Yes sir!")
                print("He gives you the keys as you walk out, Hey! say all the cops but you just stun em'")
                print("Your out now, what do you do?")
                print("1. Have a coffee at starbucks")
                print("2. Get a burger at Mcdonald's")
                print("3. Get on a helicopter to panama")
                print("4. Jump in the gutter")
                print("5. Get in yer friends car")
                
                freedom = input(" >")
                
                if freedom == "1":
                    game_over("You go to starbucks and the counter-boy immediately recognizes you from the news, calls 911 in secret and now your in the most highly gaurded vault, Good Job!")
                if freedom == "2":
                    game_over("You go to Mcdonald's and the counter-boy immediately recognizes you from the news, calls 911 in secret and now your in the most highly gaurded vault, Good Job!")
                if freedom == "3":
                    print("You get on the helicopter and are on your way to panama, there noone recognizes you and you make up a story about being a hero and you become a trillionaire")
                    print("You live a happy life until death and you are remembered a 'here' if ya know what i mean")
                if freedom == "4":
                    game_over("You jump in the gutter for some odd reason? In the gutter you die cuz u cant get up and there are toxic gasses")
                if freedom == "5":
                    print("You and your friend get in a car and drive to argentina and scam people with your fake necklaces and become a trillionair")
                    print("One day you and your friend get in a arguement and he shoots, then the anti-robber jinx turns on and your friend is locked inside...WITH A BOMB, your scam is revealed after your death, Nice!")
                 
        if police == "2":
            print("You run away and have to take refuge")
            print("Suddenly there is a $500,000 bounty on you, what do you do?")
            print("1. Escape the country")
            print("2. Take help from a very shady guy")
            print("3. Turn yourself in")
            
            wanted = input(" >")
            
            if wanted == "1":
                game_over("You try to escape but border patrol catches you, Now your imprisoned for life, NICE!")
            if wanted == "2":
                print("The guy down the street offers to help you")
                print("Do you take it or not")
                print("Yes or no?")
                
                help = input(" >")
                if help == "no":
                    game_over("You turn down the offer and he gets pissed, he pulls out a minigun and shoots you, K.O.")
                if help == "yes":
                    print("You accept the offer instantly")
                    print("Great he says, let's do this!")
                    print("He takes you to a secret underground faculty where there are trains everywhere")
                    print("This is how i move me stock mate")
                    print("You live a happy life until death")
                if wanted == "3":
                    game_over("You turn yourself in and to the your shock, they shoot you, huh? I thought police couldn't do that, eh beats me, K.O.")
                    
    if how_much < 1000:
        print("Good lad! Your not greedy")
        exit(0)
    if how_much > 1000:
        print("Ya make off with a fortune")
        print("Buy yourself a new house and 20 cars")
        print("Your featured on 'World's 10 most richest people")
        missed("One day you boast about you're money TOO much and an assasin kills you in the middle of the night.")
    
  
                   
def bred_bank():
    print("Welcome to the bred bank, we sell bread, we sell loafs, we got bred on deck and bred on the floor, TOASTED!")
    print("UMmm hi you say, what do you want today? the cashier asks? Ummm I'd like a :")
    print("Baugette")
    print("Briorche")
    print("Cottage loaf")
    print("Pretzels")
    print("Which one do you take?")
    
    bred_choice = input(" >")
    
    if bred_choice == "Baugette":
        print("Yea I'd like a baugette please.")
        print("How many loafs sir?")
        
        next = input(" >")
        how_much_baugette = int(next)
        
                  
        
        print("You awkwardly look at each other until he says ummm u gunna order or not?")
        
        if how_much_baugette > 5:
            print("How much you want man? You tryna finish ma stock or what?")
            exit(0)
        if how_much_baugette < 5:
            print("You goin' on a diet or what?")
            exit(0)
        
    if bred_choice == "Briorche":
        print("You really crave some of that lovely Briorche")
        print("So when he turns away you flip some Briorche in your pocket")
        print("Although the man on cams sees this and he isn't amused")
        print("He comes out and empty's your pocket's")
        print("You find it very awkward to stand there as you try to explain")
        print("Tell it to the judge kid!")
        game_over("You fail the court trial and sentenced to 2 years in prison and 4 years of community service, nice!")
        
    if bred_choice == "Cottage loaf":
        print("Ok so you would like some Cottage loaf right? Yes.")
        print("How much do you want?")
        
        next = input(" >")
        
        how_much_cottage_loaf = int(next)
           
        if how_much_cottage_loaf < 5:
            print("You go down  and scorf it up with some tea, Yummy!")
           
        if how_much_cottage_loaf > 5:
            print("Why you want so much bread mate?")
            print("For my sister in england you say as you pay")
            print("Final bill's 10 Pounds")
            print("10 POUNDS?! What an outrage you mumble")
            print("OH NO! I'm going to miss my flight, it's nearly 11:30")
            print("There are 2 airlines to england, which one do you take?")
            print("1. British Airways")
            print("2. Gremlin airwyas")
            
            airline = input(" >")  
            
            if airline == "1":
                print("Welcome to British Airways")
                print("Because of less seats you are all upgraded to first class completely free!")
                print("You enjoy a lovely flight and enjoy a lovely holiday in england with your sister")
                print("What a vacation!")
                
            if airline == "2":
                print("Welcome to Gremlin airways")
                print("Welcome to a horribly cramped, decaying aeroplane")
                print("No idea why you chose it")
                print("Seats are decaying and everyone is falling out")
                print("What do you do, Take a Parachute or Believe in the pilots")
                
                aeroplane_decaying = input(" >")
                
                if aeroplane_decaying == "Parachute":
                    print("You jump up to take a parachute but the flight attendent makes you sit down")
                    game_over("Soon the wing breaks and the plane falls HEADFIRST....into a volcano")
                
                elif aeroplane_decaying == "Believe":
                    print("No i should believe in the pilots you say")
                    game_over("1 minute later the plane crashed, Nice!")
                    
                    
    
    if bred_choice == "Pretzels":
        print("Pretzels ey, how many, they come in packets of 30")
        print("How much is 70 packets?")
        print("Lemme just check on the calculator")
        print("What is 30 * 70?", 30 * 70)
        print("Oh so its 2100")
        print("Why do ya want so many pretzels mate?")
        print("1. Make an excuse")
        print("2. Tell truth")
        print("3. Gnaw on a pickle")
        print("4. Pull out a gun")
        print("5. Throw a bomb")
        print("6. Rob the store")
        print("7. Smash a brick on your head")
        
        pwetzels = input(" >")
        
        if pwetzels == "1":
            print("Huh of for charity, you say")
            print("Must not tell him i plan to eat all of em by myself")
            print("Man i know when a person is lying he says")
            print("OH NO! You think, Tell me what you need em for.")
            print("What do you do -- Tell truth or Tell him to mind his own business")
            
            chatty_cashier = input(" >")
            
            if chatty_cashier == "Tell truth":
                print("Look man i just love Pretzels OKAY?")
                print("He laughs as he packs em")
                print("Thanks sir BYE!")
                
            elif chatty_cashier == "Mind your own buisness":
                print("Just mind your own buisness dude.")
                print("OK! man jeezz")
                print("He now charges you extra")
                game_over("Because of this everytime you wanna buy something he charges extra so you go bankrupt and then die cause you could not buy food, Nice!")
                
        if pwetzels == "2":
            print("Look man i just love Pretzels OKAY?")
            print("He laughs as he packs em")
            print("Thanks sir BYE!")
             
        if pwetzels == "3":
            print("As soon as he asks you this question, you GNAW on a pickle, i don't know why, something must be wrong with you.")
        
        if pwetzels == "4":
            print("You pull out a gun")
            print("HEYYYY woah woah i was just kidding man.")
            print("Is it a toy or real gun")
            
            gun = input(" >")
            
            if gun == "toy":
                print("Chill bro, it's just a toy gun.")
                print("Oh1 You nearly got me there")
         
            if gun == "real":
                print("It's a real one suckaaaa.")
                print("You gunna die nowwww")
                print("Good night bruv, SECURITY!!!! He yells")
                print("They come running in and you shoot them too.")
                print("But then the police show up and you're dooooomed.")
                game_over("You're put in the highest security prison ever, sentenced for life")
                
        
        if pwetzels == "5":
            print("Bomb attack you say.")
            print("The cashier rolls his eyes.")
            print("It's a toy bomb he says.")
            print("Security! IT'S A PRANK, PLEASE, ok what did you say, a prank?")
            
            prank_or_not == input(" >")
            
            if prank == "yes":
                print("Okay fine, here's your pretzels, Goodbye!")
                
            if prank == "no":
                print("No it isn't! HUH! SECURITY!!!! SORRY SORRY JOKE JOKE OMG.")
                
                
        if pwetzels == "6":
            print("Ok I'mma rob the store now.")
            print("Huh? What did you say, uhhh nothing, just a joke.")
            print("OK here are yer pretzels, goodbye!, byeeeeee.")
            print("IN the night you come, sneakily and trip off the fire alarm, ya doofus, now what you gunna do?")
            print("1. Run")
            print("2. Face the fire.")
            
            fire_alarm_tipped = input(" >")
            
            if fire_alarm_tipped == "1":
                print("You run and make it away.")
                print("This becomes a worldwide sensation overnight.")
                print("And on your deathday, you reveal that it was you who did this.")
                not_missed("Little to no people attend your funeral")
                
                
            if fire_alarm_tipped == "2":
                not_missed("You take the blame, you are sentenced to life in prison, NICE!")
                
                
        if pwetzels == "7":
            game_over("You smash a brick on your head for some reason?")
            
            
            
            
def dragon_room():

    print("Oh what a nice room with some cupcakes, OH WAIT, OH NO THERE IS A DRAGON HERE, WHAT DO I DO NOW?")
    print("You see the dragon is gaurding a trapdoor, i need to get it to move.")
    dragon_moved = False
    print("Fight")
    print("Run away")
    
    face_to_face_with_a_dragon = input(" >")
    if face_to_face_with_a_dragon == "Fight":
    
        print("Ok im going to fight this dragon, what should i fight it with though?")
        print("1. Bow and arrow")
        print("2. Sword and shield")
        print("3. Papaya milkshake?")
        print("4. Breakfast eggs")
             
        weapon_of_choice = input(" >")
        
        if weapon_of_choice == "Bow and arrow":
            print("You shoot the dragon's eyes and it's pissed.")
            print("The dragon now moves and fly's away as it wrinces in pain.")
            dragon_moved = True
            print("Now do you go through the trapdoor or not?")
                    
            trapdoor_free = input(" >")
                    
            if trapdoor_free == "No":
                print("I mean what was the point of that?")
                        
            if trapdoor_free == "Yes":
                print("You head down and find a alchemy lab, niceeeee!")
                print("Over here you meet a wizard who is brewing something by the alchemy potions.")
                print("Anger him")
                print("Befriend")
                
                alchemy_wizard = input(" >")
                
                if alchemy_wizard == "Anger":
                    game_over("You piss him off and he kills you with a potion.")   
                    
                if alchemy_wizard == "Befriend":
                    print("You befriend and tell him that you killed the dragon.")
                    print("He thanks you as he was apparently stuck there for 50 years")
                    print("You and the wizard are now friends for life, Yay!")
                    
        if weapon_of_choice == "Sword and shield":
            print("You stab the dragon's eyes and it's pissed.")
            print("The dragon now moves and fly's away as it wrinces in pain.")
            dragon_moved = True
            print("Now do you go through the trapdoor or not?")
                    
            trapdoor_free = input(" >")
                    
            if trapdoor_free == "No":
                print("I mean what was the point of that?")
                        
            if trapdoor_free == "Yes":
                print("You head down and find a alchemy lab, niceeeee!")
                print("Over here you meet a wizard who is brewing something by the alchemy potions.")
                print("Anger or befriend him")
                
                alchemy_wizard = input(" >")
                
                if alchemy_wizard == "Anger":
                    game_over("You piss him off and he kills you with a potion.")   
                    
                if alchemy_wizard == "Befriend":
                    print("You befriend and tell him that you killed the dragon.")
                    print("He thanks you as he was apparently stuck there for 50 years")
                    print("You and the wizard are now friends for life, Yay!")
                    
        if weapon_of_choice == "Papaya milkshake":
            game_over("You splash papaya milkshake on the dragon and it whoomps you, NICE!")
            
        if weapon_of_choice == "Breakfast eggs":
            game_over("I don't know what was going through your no-existent mind when you tried to throw breakfast eggs at it")
    
    if face_to_face_with_a_dragon == "Run away":
        missed("You turn to run away only to find some tribals face to face with you, they tie you up and cook you, well at least you tasted nice")
            
def not_missed(why):
	print(why, "Not missed at all LOL")

def game_over(why):
    print(why, "You wont be missed")
    exit(0)
                    
def start():
    print("You are in a tower")
    print("How did i get here?")
    print("Those people must have kidnapped me!")
    print("Ehh let's try to get home")
    print("Do you go down or right or left")
    
    tower = input(" >")
    
    if tower == "down":
        dragon_room()
    elif tower == "right":
        diamond_vault()
    elif tower == "left":
        bred_bank()
    else:
        game_over("You stumble around and die off thirst")
        
def missed(why):
	print(why, "You will be missed")
	exit(0)
       
start()
        