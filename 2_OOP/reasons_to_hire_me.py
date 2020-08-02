import random
import time

def reasons_to_hire_me():
    import webbrowser
    answer = input("Do You Want to Hear The Best Reasons to Hire me? (Y/N) ")
    counter = 0
    while True:
        # Stop looking up all the possibilities here you  dirty cheater!
        hiring_reasons = [['Allow me to give you a short summary','https://www.youtube.com/watch?v=_ogB0X02Gwg&feature=youtu.be&t=2',''],
                        ["I'll come and sing for you",'https://youtu.be/X6VphXQ4Bro?t=6',''],
                          ["Well, I'm an innovative thinker, work hard but most importantly", 'https://www.youtube.com/watch?v=DYjE6dmFiek&feature=youtu.be&t=55', 'But like.. a lot a lot...'],
                       ["I'm sure I am...",'https://www.youtube.com/watch?v=62XB9IbMnxQ&feature=youtu.be&list=RD62XB9IbMnxQ&t=39',"the one you're looking for HelloFresh!"],
                        ['Because','https://youtu.be/oJN6jUCy208?t=114',"I'm up all night to get data"]]

        reason = random.choice(hiring_reasons)

        if answer.upper() == "Y":
            print(reason[0])
            time.sleep(2)
            webbrowser.open(reason[1])
            time.sleep(2)
            print(reason[2])
        elif answer.upper() == 'N':
            webbrowser.open('https://youtu.be/DlIfd0IaA4k?t=39')
            break
        else:
            print("I did not understand your answer but of course you do!")
            print(reason[0])
            time.sleep(2)
            webbrowser.open(reason[1])
            time.sleep(2)
            print(reason[2])

        if counter == 10:
            print("I think it time to send me that offer my friend...")
            print('https://www.linkedin.com/in/jonas-heymans/')
            break


        time.sleep(4)
        answer = input("\nWanna Hear Another? ;) (Y/N)  ")
        if answer.upper() == 'Y':
            continue
        elif answer.upper() == "N":
            # Nope, not a bug because why wouldn't you!?
            continue

        counter += 1