import pandas as pd
import random
from save_to_csv import save_csv
from datetime import datetime, timedelta

ingredients = {

    'margherita' : {'cheese' : 4 , 'herbs' : 1, 'dough' : 3},
    'chicken' : {'cheese' : 4 , 'herbs' : 1, 'dough' : 3, 'chicken' : 2},
    'hawaiian' : {'cheese' : 4 , 'herbs' : 1, 'dough' : 3, 'pineapple' : 2},
    'farm fresh' : {'cheese' : 4 , 'herbs' : 1, 'dough' : 3, 'veggies' : 2},
    'peri peri chilli' : {'cheese' : 4 , 'herbs' : 1, 'dough' : 3, 'spices' : 1, 'chillies' : 2},
    'garlic bread' : {'dough' : 2, 'garlic' : 1, 'butter': 1},
    'chicken wings': {'chicken' : 5, 'sauces' : 2, 'spices' : 1, 'herbs' : 1},
    'cheese balls' : {'cheese' : 3, 'dough' : 2}
}


details = {
    'ING001': ['spices', 0.15, 2],
    'ING002': ['herbs', 0.10, 2],
    'ING003': ['dough', 0.35, 80],
    'ING004': ['veggies', 1.00, 80],
    'ING005': ['garlic', 0.25, 10],
    'ING006': ['butter', 0.40, 20],
    'ING007': ['chicken', 0.9, 80],
    'ING008': ['chicken', 0.50, 50],
    'ING009': ['cheese', 0.25, 30],
    'ING0010': ['chillies', 0.50, 10],
    'ING0011': ['pineapple', 0.75, 20]
}

details_list = [[key, *value] for key, value in details.items()]

columns = ['ing_id', 'ing_name', 'ing_price', 'ing_weight']
ingredients_df = pd.DataFrame(details_list, columns=columns)

recipe_id = 1200
r = []

recipe_names = list(ingredients.keys())

recipe_df = pd.DataFrame({'recipe_id': [recipe_id + i for i in range(len(recipe_names))],
                          'recipe_name': recipe_names})

save_csv('recipe', recipe_df)

