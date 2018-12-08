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

json_file_in ='dataset/used_restaurants.json'
restaurant_pickle = 'dataset/restaurants.pkl'

restaurants = {} # restaurants dict, key is bid, value is a restaurant info dict with bid
with open(json_file_in, "r") as input:
	cnt = 0
	for line in input:
		cnt += 1
		data = json.loads(line)
		# parse each line of business record, get its bid, category, price
		rest = {} # restaurant info dict, has two keys - category, price
		rest['category'] = split(data['categories'])
		if data.get('attributes') is not None:
			price = data['attributes'].get('RestaurantsPriceRange2')
			if price is not None:
				rest['price'] = price
			else:
				rest['price'] = None
		else:
			rest['price'] = None
		restaurants[data['business_id']] = rest
		print cnt, data['business_id'], rest
	print "restaurant number: ", len(restaurants)

with open(restaurant_pickle, 'wb') as f:
	pickle.dump(restaurants, f)
