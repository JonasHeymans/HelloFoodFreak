import json
import requests
import random
import time

from constants.constants import APPLICATION_ID, APPLICATION_KEY

HEADERS = {
    'Content-Type': 'application/json',
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY
}


class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.total_calories = self.get_total_calories(self.ingredients)


    def __repr__(self):
        return f"Recipe object with name: '{self.name}'"

    def get_total_calories(self, ingredients):
        """
        Natural language nutrition lookup API
        References:
        - https://gist.github.com/mattsilv/9dfb709e7609537ffd3b1b8c097e9bfb
        - https://gist.github.com/mattsilv/95f94dd1378d4747fb68ebb2d042a4a6

        Source: https://github.com/yenlow/eat/blob/ac754a64e7c7fcc07ac46ce1967ed39d278b61cc/NutritionIX.py
        """
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        body = {
            "query": ingredients,
            "timezone": "CEST"
        }

        response = requests.post(url=url, headers=HEADERS, json=body)
        content = json.loads(response.content)

        return sum([content['foods'][x]['nf_calories'] for x in range(len(content['foods']))])




class Health:
    def __init__(self):
        self.total_calories_eaten = 0

    def eat(self, *args):
        for arg in args[0]:
            num_calories = arg.total_calories
            self.total_calories_eaten += num_calories

            print(f'I just ate {arg.name}, which contained {num_calories :.2f} calories. It was very tasty.')

        print(f'I now ate in total {self.total_calories_eaten:.2f} calories! Nomnom\n')

def make_hyperlink(link, text):
    hyperlink_format = '<a href="{link}">{text}</a>'

    print(hyperlink_format.format(link=link, text=text).str.read())


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







