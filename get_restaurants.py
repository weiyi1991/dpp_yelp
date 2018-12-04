import numpy as np
import json

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

json_file_in ='yelp_academic_dataset_business.json'
json_file_out ='yelp_academic_dataset_restaurants.json'

with open(json_file_in, "r", encoding="utf8") as input:
	with open(json_file_out, "w", encoding="utf8") as output:
		for line in input:
			data = json.loads(line)
			if(data['categories'] != None):
				for i in split(data['categories']):
					if(i == 'Restaurants' or i == 'Food'):
						output.write(line)
						break
