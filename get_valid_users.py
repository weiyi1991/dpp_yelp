import numpy as np
import json
import pickle

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

json_file_in ='dataset/yelp_academic_dataset_user.json'
json_file_out ='dataset/valid_user.json'
valid_user_pickle = 'dataset/valid_users.pkl'

valid_users = []
with open(json_file_in, "r") as input:
	with open(json_file_out, "w") as output:
		cnt = 0
		for line in input:
			data = json.loads(line)
			if(data['friends'] != 'None'):
				if(len(split(data['friends'])) > 4 and len(split(data['friends'])) < 11 and data['review_count'] > 5):
					print cnt
					cnt += 1
					d = {}
					d['user_id'] = data['user_id']
					d['review_count'] = data['review_count']
					d['useful'] = data['useful']
					d['fans'] = data['fans']
					d['friends'] = data['friends']
					#output.write(line)
					valid_users.append(data['user_id'])
					json.dump(d, output)
					output.write('\n')

with open(valid_user_pickle, 'wb') as f:
	pickle.dump(valid_users, f)
