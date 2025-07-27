import random
import pandas as pd
from datetime import datetime, timedelta

from save_to_csv import save_csv


order_id = None
cust_df = pd.read_csv('csv_files\customers.csv')
cust_id = cust_df['cust_id'].tolist();


def gen_order_id(used_ids):
    while True:
        new_id = random.randint(10000, 99999)
        if new_id not in used_ids:
            used_ids.add(new_id)
            return new_id


payment_mode = ['cash', 'credit card', 'debit card']


#order_date
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 11, 30)
num_days = (end_date - start_date).days + 1

list_of_dates = [start_date + timedelta(days=i) for i in range(num_days)]
formatted_dates = [day.strftime('%d-%m-%Y') for day in list_of_dates]

#order_time
start_time = datetime.strptime('12:00', '%H:%M')
end_time = datetime.strptime('22:00', '%H:%M')
num_minutes = int((end_time - start_time).total_seconds() / 60) + 1

list_of_times = [start_time + timedelta(minutes=random.randint(0, num_minutes)) for _ in range(num_minutes)]
formatted_times = [time.strftime('%I:%M %p') for time in list_of_times]


#generating the dataframe
max_orders_per_customer = 12
max_customers_per_day = 40
num_orders = 700
max_orders_per_customer = 5

order_ids_set = set()
orders = []

menu_df = pd.read_csv('csv_files\menu_items.csv')
item_id_list= menu_df['item_id'].tolist()

row_id = 1
orders = []
for _ in range(num_orders):

    row_id+=1
   
    customer = random.choice(cust_id)
    while cust_id.count(customer) >= max_orders_per_customer:
        customer = random.choice(cust_id)

    order_date = random.choice(list_of_dates)
    while formatted_dates.count(order_date) >= max_customers_per_day:
        order_date = random.choice(formatted_dates)

    order_time = random.choice(list_of_times)
    payment_mode_selected = random.choice(payment_mode)
    order_id = gen_order_id(order_ids_set)

    ordered_at = datetime.combine(order_date, order_time.time())

    # Randomly choose 1-5 items
    num_items_ordered = random.randint(1, 4)
    items_ordered = random.sample(item_id_list, num_items_ordered)

    # Random quantity for each item
    quantities = [random.randint(1, 3) for _ in range(num_items_ordered)]

    # Append to the order_df
    for item, quantity in zip(items_ordered, quantities):
        orders.append((
            row_id,
            order_id,
            ordered_at,
            customer,
            item,
            quantity,
            payment_mode_selected
        ))

order_df = pd.DataFrame(orders, columns=['row_id','order_id', 'ordered_at', 'cust_id', 'item_id', 'quantity', 'payment_mode']) 


save_csv('orders', order_df)

print(order_df)




