'''


Please note that:

- The aim of this Package was to prove that I could do some Object Oriented programming,
which I feel I did on a very basic level. The code works (very minimally) is however still full of bugs,
inefficiencies (Why would you ever do that whole API-request just to calculate the total of calories?),
needs logging, testing, input validation...

'''


import pandas as pd
import requests
import json
from recipe.recipe import Recipe, Health, reasons_to_hire_me




if __name__ == "__main__":


    while True:
        user_input = int(input('How many recipes do you want to eat?  '))
        if user_input > 10:
            print("That's a bit high no? Let's try a lower number")
            continue
        elif user_input < 2:
            print("I'm Hungry!")
            continue
        else:
            break

    df = pd.read_json('../data/open_recipes.json', lines=True)

    recipes = []
    for x in range(user_input):
        exec(f'df_row_{x} = df.iloc[{x}]')
        exec(f"recipes.append(Recipe(name= df_row_{x}['name'], ingredients=df_row_{x}['ingredients']))")


    my_health = Health()

    my_health.eat(recipes)

    reasons_to_hire_me()







