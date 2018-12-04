from __future__ import division, print_function, unicode_literals
import numpy as np
import json
import matplotlib.pyplot as plt

json_file='dataset/yelp_academic_dataset_user.json'

valid_users = []

with open(json_file, 'r') as json_data:
    cnt = 0
    for line in json_data:
        data = json.loads(line)
        cnt += 1
        #if 5 <= len(data['friends']) and len(data['friends']) <= 30:
        #    valid_users.append(data)
        #    print(data['user_id'], cnt, len(data['friends']))
        if data['friends'] == 'None':
            valid_users.append(0)
            print(data['user_id'], cnt, 0)
        else:
            valid_users.append(len(data['friends'].split(',')))
            print(data['user_id'], cnt, len(data['friends'].split(',')))

print(len(valid_users))

with open('friends_count.txt', 'w') as f:
    for item in valid_users:
        f.write("%d\n" % item)

plt.hist(np.array(valid_users), bins=50)
plt.show()
