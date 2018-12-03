from __future__ import division, print_function, unicode_literals
import numpy as np
import json

json_file='dataset/yelp_academic_dataset_user.json'

valid_users = []

with open(json_file, 'r') as json_data:
    cnt = 0
    for line in json_data:
        data = json.loads(line)
        cnt += 1
        if data['friends'] != 'None':
            valid_users.append(data)
            print(data['user_id'], cnt)
print(len(valid_users))
