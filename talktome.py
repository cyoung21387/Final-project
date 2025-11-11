"""
Final lab
Name: Christian Young
Title: Talk to me
    This is a chat machine that allows you to speak to different characters and carry on conversations with them.

"""
import time
import random

def typing (line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the delay (in seconds) to control typing speed


def yodawho ():
    return ["The one you dislike most, who is, hmm?\n", "With which fictional being most you resonate, hmm?\n", "Most likely to be arrested for stealing toilet paper, who do you know, hmmm?\n", "From a favorite movie of yours, name a character, you must?\n"]
def yodawhat ():
    return ["To break down the front door of a house, use what would you, hmm?\n", "An object that holds magical powers, name it you must.\n", "In your favorite sport, used an object is. Name it, you shall?\n", "Daily you use an object, yes? Name it now, you must?\n"]
def yodawhere ():
    return ["Go you have always wanted, where is it, hmm?\n", "For peace and quiet, go where would you, yes?\n", "Your favorite place to spend time, where is, hmmm?\n", "For adventure and exploration, go where would you, hmm?\n"]
def yodawhy ():
    return ["Become a Jedi, why do you wish, hmm?\n", "Into your house, break someone would, why, hmmm?\n", "Seven voice messages and missed calls, your mother leaves… why, hmm? Trouble sensed, she has.\n", "With toothbrushes and Ladder logic, Darth Maul attacks CEI… why, hmm? Strange, this is. Powerful the plan must be.\n"]
def yodahow ():
    return ["Into Area 51, break how would you, hmm? Secrets it holds, yes…\n", "Jar Jar, a Sith he seems… defeat him, how would you, hmmm?\n", "Lead America as president, how would you, yes? Strong the Force in politics must be.\n", "A starship, build you would… with tennis racket and dairy-free cheese block?\n"]
def yodares ():
    return ["A story that is, I suppose. Interesting, it surely is.\n", "Inspirational, this story is. Mmm.\n", "Such a story, heard I have not. Grave danger in your training, I sense.\n", "Foreshadow the Jedi you shall be, this story does.\n"]

def gandalf():
    stats = dict()
    line = "Hello my dear friend! I have something important to tell you.\n"
    typing(line)
    user = input()
    line = "I am taking the hobbits to eisengard. Would you like to accompany us on our unfathomable quest of adventure?\n"
    typing(line)
    try:
        user = input('y/n: ')
        if user == "y":
            line = "wonderful! first on a scale of 1 to 10, 1 being scared and 10 being heroic how comfertable are you around orcs?\n "
            typing (line)
            user = int(input())
            stats['orcs'] = user
            line = 'What about trolls?\n'
            typing (line)
            user = int(input())
            stats['trolls'] = user
            line = "And what about gobblins?\n"
            typing (line)
            user = int(input())
            stats['gobblins'] = user
            line = "Very well, how good are you at riding ponies?\n"
            typing (line)
            user = int(input())
            stats['ponies'] = user
            line = "Tell me, have you ever met a elf before?\n"
            typing (line)
            user = input()
            line = "Alright, on a scale of 1 to 10 how would you feel about fighting one?\n"
            typing (line)
            user = int(input())
            total = sum(stats.values())
            average = total / len(stats)
            if average <= 5 :
                line = (f"Based on your answers with a confidence of {average}, you are a helpless pice of rubbish trash.\n")
                typing (line)
                line = ("You wouldn't last 5 minutes out there in the world of danger and adventure.\n")
                typing (line)
                line = ("I say to you sir, good day.\n")
                typing (line)
            if average >= 5.1 :
                line = (f"Based on your answers with a confidence of {average}, You are worthy of this quest.\n")
                typing (line)
                line = ("Take only what you need with you.\n")
                typing (line)
                line = ("Would you like a list of things you need to pack?\n")
                typing (line)
                user = input("(y/n): ")
                if user == "y" :
                    line = ("Satchel\nTooth past\ntooth brush\nchicken\nBlues clues\nsword\ntoilet paper\nsmoking pipe\nweed\nbeer\ncocaine\ncontract that you didn't read\nlife insurance policy\na will saying that if anything happens to you, all of your belongings go to me!\n")
                    typing (line)
                line = ("Alright, now it is time to ebark on our quest of adventure!!!!\n")
                typing (line)
                line = ("Are you ready?\n")
                typing (line)
                user = input("(y/n): ")
                if user == "y" :
                    line = ("Very good! Pack your things and I'll see you out there! We very much shall pass!!!!!!!!\n")
                    typing (line)
                if user == "n" :
                    line = ("Why on earth not?\n")
                    typing (line)
                    user = input()
                    line = ("That is a stupid reason.\nNow you have wasted my time.\nI say to you sir good day.\n")
                    typing (line)


        if user == "n":
            line = ("Very well. I say to you good sir, carry on!\n")
            typing (line)
    except:
        line = ("Please type y or n for yes or no.\n")
        typing (line)



def mickey():
    line = ("Well boy! Welcome to the Micky Mouse club house!\n")
    typing (line)
    line = ("How are you doing today?\n")
    typing (line)
    user = input()
    line = ("Well thats nice now isn't it.\noh no, I just got a call from goofy.\nHe feel on his bike and can't get up\nHe must have skiped leg day.\nsay, would you be willing to come help me save goofy?\n")
    typing (line)
    user = input("(y/n): ")
    if user == "y":
        line = ("Oh Boy! thats great!\nFirst things first, we are gonna need some tools to help goofy.\nI'm gonna offer 4 items for each sceaniro and your gonna pick one!\n")
        typing (line)
        line = ("First we need to find him! Pick one of the four items listed below:\n(1): Drone\n(2): car\n(3): wrench\n(4): plunger\n")
        typing (line)
        user = int(input("Type number here: "))
        if user == 1:
            line = ("Hopfully your a good pilot, here ya go.\nALright your doing it...........THERE HE IS!!!!!\nLets go get him!\n")
            typing (line)
            line = ("Looks like he is hurt. choose one of these four items to help him:\n(1): band aid\n(2): Baseball bat\n(3): AK-47\n(4): steal his bike\n")
            typing (line)
            user = int(input("type number here: "))
            if user == 1:
                line = ("Perfect! Thats just what he needed.\nSay, do you know how to ride a bike?\n")
                typing (line)
                user = input("(y/n): ")
                if user == "y":
                    line = ("Perfect!\nThank you so much for your help and..........What are slaping him in the rear for he ain't a horse.\nThat's it Your fired you little #@!&#@!$@!\n")
                    typing (line)
                    user = None
                if user == "n":
                    line = ("Are you serious?\n")
                    typing (line)
                    user = input()
                    line = ("What is wrong with you?\n")
                    typing (line)
                    user = input()
                    line = ("Well why don't you go home and learn to ride a bike like the rest of the kids that watch this show and then come back!\n")
                    typing (line)
                    user = None
            if user == 2:
                line = ("ah.... What are you gonna do with that?\n")
                typing (line)
                user = input()
                line = ("Are you sure?\n")
                typing (line)
                user = input()
                line = ("This is a flippin childrens movie.......Stop beating goofy, don't hit me, AWWWWWWWWWWWWW\n")
                typing (line)
                user = None
            if user == 3:
                line = ("Um..... Thats a sure interesting chice you made there.\nDon't draw unless you ready boy, I gotta Glock in my pocket and I ain't afraid to use it.\n You wanna go?\n")
                typing (line)
                user = input("(y/n): ")
                if user == "y":
                    line = ("ALright, On three........one........two.......THREE***BANG****\nAnd thats why they call it my club house!\n")
                    typing (line)
                    user = None
                if user == "n":
                    line = ("Great! Now im gonna call the cops! Thanks for coming to Mickey Mouse the club house!\n")
                    typing (line)
                    user = None
            if user == 4:
                line = ("Oh no, you stole his bike.\nDon't worry goofy, My sniper missed you but hopfully he wont miss this guy.\n")
                typing (line)
                user = None


        if user == 2:
            line = ("ALright here's the keys.\nYour going a little fast now, slow it down.\nHey watch out for that TREE\nAWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.\n Police: Sir your under arrest. Lean over the car I'm taking you into custody.\nMickey: Well, at least thats better than all the other kids that watch my show.\nMickey: I hope they dont find the sniper I hired to shoot down goofy.")
            typing (line)
        if user == 3:
            line = ("Well, Im not sure what your gonna do with the wrench............why are you looking at me like that.\nHold on now son, you sure you wanna play this game.\nI got a Glock in my back pocket and I'm not affraid to use it.\n******BANG*****\nThats why they call it my club house.\n")
            typing (line)
        if user == 4:
            line = ("Why on earth would you pick the plunger.\nYou could have picked litterally anything else.\nYour grounded.\n")
            typing (line)


    if user == "n":
        line = ("Well your just a pice of crap now arn't you.")
        typing (line)
        user = input()
        line = ("Well, it's the truth ain't it.")
        typing (line)
        line = ("I guess we'll agree to disagree you old fart.\n You best be on your way now before I get my boys from the hood up in hear to teach you a lesson.\nDont forget to vist my club house again, It will probably be your last.\n")
        typing (line)


def yoda():
    story = list()
    line = ("Welcome to the Jedi Temple, hmm? Jedi training, receive you would like? Yes, hmmm.\n")
    typing (line)
    user = input("(y/n): ")
    if user == "y":
        line = ("Splendid, hmm. Teach you the first lesson of the Jedi, I will. Begin it does… with looking within, oneself must.\n")
        typing (line)
        line = random.choice(yodawho())
        typing (line)
        user = input()
        story.append(user)
        line = random.choice(yodawhat())
        typing (line)
        user = input()
        story.append(user)
        line = random.choice(yodawhere())
        typing (line)
        user = input()
        story.append(user)
        line = random.choice(yodawhy())
        typing (line)
        user = input()
        story.append(user)
        line = random.choice(yodahow())
        typing (line)
        user = input ()
        story.append(user)
        line = ("See you now, I do, and your story. Your story, it is:\n")
        typing (line)
        who = story[0]
        what = story[1]
        where = story [2]
        why = story [3]
        how = story [4]
        line = (f"{who} at {where} decided to {what} because {why}, and to accomplish this {how}.\n")
        typing (line)
        line = random.choice(yodares())
        typing (line)
        line = ("Understand the importance of your story, do you?\n")
        typing (line)
        user = input ("(y/n): ")
        if user == "y":
            line = ("Very good, hmm. Begin your training, we will!\n")
            typing (line)
            user = None
        if user == "n":
            line = ("Too old you are, and understanding you lack. Train you, I no longer can.\n")
            typing (line)
            user = None
    if user == "n":
        line = ("Agree with your decision, the Council does. Good day, and farewell… hmmm.\n")
        typing (line)



def jarvis():
    line = ("Hello sir, It's good to see you again!\nI have an extencive data base with access to any and all systems.\nOut of the three options below who's system would you like to hack into?\n")
    typing (line)
    line = ("(1) The President\n(2) A Friend\n(3) Dave Oliver\n")
    typing (line)


def menu():
    while True:
        print ('Main Menu:\n')
        print ('Gandalf the grey (1)')
        print ('Mickey Mouse (2)')
        print ('Yoda (3)')
        print ('Jarvis (4)')
        print ('Exit (5)\n')

        try:
            choise = int(input("Type number here: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue


        if choise == 1:
            gandalf()
            continue
        if choise == 2:
            mickey()
            continue
        if choise == 3:
            yoda()
            continue
        if choise == 4:
            jarvis()
            continue
        if choise == 5:
            print ("Chat has been closed. Have a good day!")
            break


def main():
    line = ('Choose a character you will like to speak with!\n')
    typing (line)
    menu()
main()