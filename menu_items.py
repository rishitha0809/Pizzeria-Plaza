import pandas as pd
from save_to_csv import save_csv


categories = ['pizza', 'drinks', 'sides']
pizza = {'margherita' : 5, 'chicken' : 9, 'hawaiian' : 6, 'farm fresh' : 10, 'peri peri chilli' : 7}
drinks = {'coke' : 2 , 'fanta' : 2, 'mountain dew' : 2, 'pepsi' : 2 , '7up' : 2}
sides = {'garlic bread' : 4 , 'chicken wings' : 6, 'cheese balls' : 5}



def generate_items(category, cat_dict):
    items = []
    for item_name, item_price in cat_dict.items():
        item_cat = categories[category]
        item_id = f"{item_cat[:2]}{item_name[:2]}{0}{category+10}"

        items.append((item_id, item_name, item_cat, item_price))
    return items

pizza_entries = generate_items(0, pizza)
drinks_entries = generate_items(1, drinks)
sides_entries = generate_items(2, sides)

all_items = pizza_entries + drinks_entries + sides_entries



columns = ['item_id', 'item_name', 'item_cat', 'item_price']
menu_df = pd.DataFrame(all_items, columns=columns)

save_csv('menu_items', menu_df)
print('saved')
