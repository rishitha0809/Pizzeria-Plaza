import calendar
from orders import list_of_dates
import random
import pandas as pd
from datetime import datetime
from save_to_csv import save_csv


#staff

staff= {
    'waiter': ['John', 'Alice', 'Bob', 'Eva', 'David'],
    'chef': ['Michael', 'Sophia', 'Daniel', 'Olivia', 'James'],
    'manager': ['Emma', 'William'],
    'cleaner': ['Henry', 'Charlotte', 'Jack', 'Jill']
}

staff_list = [[key, *value] for key, value in staff.items()]

def generate_staff_ids(position, count):
    staff_ids = []
    for _ in range(count):
        random_number = random.randint(10, 99)
        staff_id = position[:4].upper() + str(random_number)
        staff_ids.append(staff_id)
    return staff_ids

all_staff_ids = []
for position, *names in staff_list:
    position_staff_ids = generate_staff_ids(position, len(names))
    all_staff_ids.extend(list(zip(names, position_staff_ids)))
                         
staff_df = pd.DataFrame(all_staff_ids, columns=['staff_name', 'staff_id'])

staff_df['position'] = [position for position, *_ in staff_list for _ in range(len(staff[position]))]


hourly_rates = {'waiter': 8, 'chef': 10, 'manager': 10, 'cleaner': 8}
staff_df['hourly_rate'] = staff_df['position'].map(hourly_rates)

shift_ids = ['SHMO001', 'SHEV002']

def gen_rota_id(day, shift_id, staff_id):
    return f'{day.upper()[:3]}{shift_id[2:4]}{staff_id[-2:]}'


# Generate data for rota and shift
rota_list = []
shift_list = []
for date in list_of_dates:
    day = date.strftime("%A")
    for shift_id in shift_ids:
        
        # Ensure one manager and 2 chefs, cleaners, waiters per shift
        staff_per_position = {'manager': 1, 'chef': 2, 'cleaner': 2, 'waiter': 2}
        for position, count in staff_per_position.items():
            available_staff = staff_df[staff_df['position'] == position]
            selected_staff = random.sample(available_staff['staff_id'].tolist(), count)

            
            
            for staff_id in selected_staff:
                rota_id = gen_rota_id(day, shift_id, staff_id)
                rota_list.append((rota_id, date, shift_id, staff_id))
        
    #shift_list.append(( shift_id, day))
                

rota_df = pd.DataFrame(rota_list, columns=['rota_id', 'date', 'shift_id', 'staff_id'])
shift_df = pd.DataFrame(shift_list, columns=['shift_id', 'shift_day'])

save_csv('rota', rota_df)
#save_csv('shift', shift_df)
save_csv('staff', staff_df)

print('saved')
