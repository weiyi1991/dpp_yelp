import numpy as np
import json
import pickle

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

#json_file_in ='dataset/used_restaurants.json'
json_file_in ='dataset/user_restaurant_rating.json'

used_users = set([])
used_restaurants = set([])
category = set([])
with open(json_file_in, "r") as input:
	cnt = 0
	for line in input:
		print cnt
		cnt += 1
		data = json.loads(line)
		categories = split(data['user_id'])
		for cate in categories:
			if cate not in category:
				category.add(cate)
	print "category number: ", len(category)
