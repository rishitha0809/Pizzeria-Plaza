from recipe_ing import details
from save_to_csv import save_csv
import random
import pandas as pd

inventory_list = []



for inv_id, (ing_id, _) in enumerate(details.items(), start=12300):
    qty = random.randint(1, 100)
    inventory_list.append((inv_id, ing_id, qty))

inventory_df = pd.DataFrame(inventory_list, columns=['inv_id', 'ing_id', 'qty'])
save_csv('inventory', inventory_df)
