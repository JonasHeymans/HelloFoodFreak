'''


Please note that:

- The aim of this Package was to prove that I could do some Object Oriented programming,
which I feel I did on a very basic level. The code works (very minimally) is however still full of bugs,
inefficiencies (Why would you ever do that whole API-request just to calculate the total of calories?),
needs logging, testing, input validation...

'''


import pandas as pd
from recipe.recipe import Recipe, Health
from reasons_to_hire_me import reasons_to_hire_me




if __name__ == "__main__":

    while True:
        user_input = int(input('How many meals do you want to eat?  '))
        if user_input > 10:
            print("That's a bit high no? Let's try a lower number")
        elif user_input < 2:
            print("I'm Hungry!")
        else:
            break


    df = pd.read_json('data/open_recipes.json', lines=True)

    recipes = []
    for x in range(user_input):
        exec(f'df_row_{x} = df.iloc[{x}]')
        exec(f"recipes.append(Recipe(name= df_row_{x}['name'], ingredients=df_row_{x}['ingredients']))")


    my_health = Health()

    my_health.eat(recipes)

    reasons_to_hire_me()



'''
Improvements

- Giving the user the choice to select the meals she wants to eat (eg. "I'm feeling Thai today") 
- Improving clean code practices
- Making it relevant for business purposes
- Expanding the Health class with eg. Sports, which lowers the amount of calories (because you burn calories)
- ... Not really a lot of interesting improvements. This project, more than Sales Prediction, was aimed to show
my capabilities in OOP. It might be expanded to be a meal tracker or something like that, but that was not my intent

'''

