import numpy as np
import json
import pickle

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

json_file_in ='dataset/used_user.json'
user_pickle = 'dataset/users.pkl'
users = {} # user dict, key is uid, value is the user info dict with uid

with open(json_file_in, "r") as input:
	cnt = 0
	for line in input:
		cnt += 1
		data = json.loads(line)
		# parse each line of user record, get its uid, frineds, rate
		user = {} # user info dict, has 4 keys: friends, review_count, useful_count, fans
		user['friends'] = split(data['friends'])
		user['review_count'] = data['review_count']
		user['useful'] = data['useful']
		user['fans'] = data['fans']
		users[data['user_id']] = user
		print cnt, data['user_id'], user
	print "user number: ", len(users)

with open(user_pickle, 'wb') as f:
	pickle.dump(users, f)
