'''

Creating an


'''

import datetime
import random
import json

def generate_random_date():
    start_date = datetime.date(2019, 7, 1)
    end_date = datetime.date(2020, 7, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    return start_date + datetime.timedelta(days=random_number_of_days)


if __name__ == "__main__":
    with open('Pycharmprojects/HelloFoodFreak/data/open_recipes.json') as json_file:
        data = json.load(json_file)
    print(data)

