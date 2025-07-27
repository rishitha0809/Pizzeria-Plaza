import pandas as pd
import random
import string
from save_to_csv import save_csv

def gen_cust_id():
    used_ids=[]
    while True:
        new_id = ''.join(random.choice(string.hexdigits) for _ in range(8))
        if new_id not in used_ids:
            used_ids.append(new_id)
            return new_id

cust_names = pd.read_csv('csv_files\customer_names.csv')
names = cust_names['names'].tolist()
genders = ['male', 'female']

def generate_customer_df(num_customers):
    data = {
        'cust_id': [gen_cust_id() for _ in range(num_customers)],
        'cust_name': random.choices(names, k=num_customers),
        'gender': random.choices(genders, k=num_customers),
        'age': [random.randrange(15, 80) for _ in range(num_customers)]
    }
    return pd.DataFrame(data)

customer_df = generate_customer_df(len(cust_names))

#save_csv('customers', customer_df)

print('saved')
  
