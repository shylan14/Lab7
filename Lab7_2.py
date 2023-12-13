import json
from datetime import datetime

users = ["Артур", "Кейт", "Аліса", "Майк"]

user_data_list = [{"name": user, "age": random.randint(1, 99)} for user in users]

current_date = datetime.now().strftime("%d;%m;%y")

final_dict = {"data": user_data_list, "created_at": current_date}

json_filename = f'users_data_{current_date}.json'

with open(json_filename, 'w') as json_file:
    json.dump(final_dict, json_file, indent=2)
