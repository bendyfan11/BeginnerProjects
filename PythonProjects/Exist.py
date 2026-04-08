import random
import time

def reset():
    global exist
    exist = 0
    global A_thought
    A_thought = 0
    global game
    game = 0
    global guess
    guess = ""
    global number
    number = ""
    global die
    die = ""
    global diebutbetter
    diebutbetter = ""
weird = 0
reset()
while True:
    chose = input("press enter to exist. ").lower().strip()
    if chose == "" and exist > 10:
        print("you have existed over ten times. that's pretty wild.")
        time.sleep(2)
        print("... you know... this is kind of boring. why not actually acomplish somthing in your life?")
        time.sleep(1)
        print("I mean, seriously, you're sitting here, playing 'exist simulator'???")
        time.sleep(1)
        print("Why not just... exist in the real world? Away from the screen? Maybe you should just quit.")
        time.sleep(1)
        print("But I mean... who am I to tell you what you can and can't do?")
        A_thought += 1
        exist = 0
    elif chose == "":
        print("You exist. You will continue to exist. or maybe you wont.")
        time.sleep(10)
        exist += 1
    elif chose == "do not":
        print("you do not exist. very concerning.")
        break
    elif chose == "quit" and A_thought > 0:
        print("Ah. So, you've decided to quit existance? But what does that even mean?")
        print("'Quit existance', that's like saying 'oh I should just stop going to work!' you can't just do that!")
        time.sleep(1)
        print("Or... Maybe you can.")
        time.sleep(1)
        print("The question is... are you sure?")
        sure = input(" ")
        if sure == "yes":
            print("Well okay then. Goodbye")
            quit()
        elif sure == "no":
            print("Well, none of us are really sure of anything, are we?")
            time.sleep(1)
            print("nature of life and all that.")
            time.sleep(1)
            print("I'm talking too much. I'll leave you to existing.")
            time.sleep(20)
        else:
            print(f"'{sure}'?")
            time.sleep(1)
            print("What's that supposed to mean?")
            reset()
            continue
    elif weird == 0:
        print("...")
        weird +=1
    elif weird == 1:
        print("You... you do know you're supposed to hit enter, right?")
        time.sleep(1)
        print("Not... well, whatever you're doing.")
        time.sleep(1)
        print("it's really not that hard.")
        time.sleep(3)
        print("You know, most people would boot a game called 'existance simulator' and... well, simulate existance.")
        time.sleep(1)
        print("But not you.")
        time.sleep(1)
        print("most people won't even find this little area. While you're here, maybe A game is in order?")
        game = input("").strip().lower()
        if game == "yes":
            print("Delightful.")
            time.sleep(1)
            print("Allow me to set up my things... one moment.")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Ah! Here we are. I've got some dice, I suppose we can roll these around.")
            die = random.randint(2, 12)
            diebutbetter = str(die)
            print("Okay. I have rolled two six sided die. What do you think they landed on?")
            guess = input("").strip()
            if not guess.isdigit():
                print("Wow, you're really bad at instructions. I asked for a NUMBER. Oh, whatever. Not like it matters. The dice are gone. reduced to atoms.")
                reset()
                weird = 2
                continue
            if guess == diebutbetter:
                print("Spot on!")
                time.sleep(1)
                print("An issue, however. My dice broke.")
                reset()
                weird = 2
                continue
            if guess != diebutbetter:
                print(f"Well no, no i rolled {die}. Not like it matters much. The dice pretty much crumbled to dust the moment I rolled them.")
                reset()
                weird = 2
                continue
    elif weird > 1:
        print("... theres no more dice. just press enter. not hard.")
        continue