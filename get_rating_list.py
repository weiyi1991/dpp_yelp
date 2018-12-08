'''
	Read used_restaurant_rating.json, parse the attribute, save the used user list and used restaurant in pickle files.
	The used user list and used restaurant list is in set data structure for search efficiency.
'''

import numpy as np
import json
import pickle

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

json_file_in ='dataset/user_restaurant_rating.json'
rate_pickle = 'dataset/ratings.pkl'
ratings = {} # rating dict, key is uid, value is the rating info dict with uid

with open(json_file_in, "r") as input:
	cnt = 0
	for line in input:
		cnt += 1
		data = json.loads(line)
		# parse each line of rating record, get its uid, bid, rate
		rate = {} # rating info dict, has two keys: bid, stars
		rate['business_id'] = data['business_id']
		rate['stars'] = data['stars']
		ratings[data['user_id']] = rate
		print cnt, data['user_id'], rate
	print "rating number: ", len(ratings)

with open(rate_pickle, 'wb') as f:
	pickle.dump(ratings, f)
