"""
Final lab
Name: Christian Young
Title: Talk to me
    This is a chat machine that allows you to speak to different characters and carry on conversations with them.

"""
import time


def typing (line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Adjust the delay (in seconds) to control typing speed


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
                line = ("You wouldent last 5 minutes out there in the world of danger and adventure.\n")
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
            line = ("Very well. I say to you good sir carry on!\n")
            typing (line)
    except:
        line = ("Please type y or n for yes or no.")
        typing (line)



def mickey():
    print ()


def yoda():
    print ()


def jarvis():
    print ()


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