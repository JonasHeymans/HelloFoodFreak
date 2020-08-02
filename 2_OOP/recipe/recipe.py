import json
import requests


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



            print(f'I just ate a {arg.name}, which contained {num_calories :.2f} calories.')

        print(f"\nI now ate in total {self.total_calories_eaten:.2f} calories! It was very tasty, as is everything from Hellofresh! I love Hellofresh, Hellofresh is the best!\n"
              f"They must have such smart people working for them. \n")  # especially the ones who do code review

def make_hyperlink(link, text):
    hyperlink_format = '<a href="{link}">{text}</a>'

    print(hyperlink_format.format(link=link, text=text).str.read())










