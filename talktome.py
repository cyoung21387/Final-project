"""
Final lab
Name: Christian Young
Title: Talk to me
    This is a chat machine that allows you to speak to different characters and carry on conversations with them.

"""
def gandalf():
    print ("Hello my dear friend! I have something important to tell you.")
    user = input()
    print ("input reciveed")


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
            print ('Successssssssssssssssssssss')
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
            break


def main():
    menu()
main()
