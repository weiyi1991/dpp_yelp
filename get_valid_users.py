import numpy as np
import json

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result

json_file_in ='yelp_academic_dataset_user.json'
json_file_out ='yelp_academic_dataset_valid_user.json'
	
with open(json_file_in, "r", encoding="utf8") as input:
	with open(json_file_out, "w", encoding="utf8") as output:
		for line in input:	
			data = json.loads(line)	
			if(data['friends'] != 'None'):
				if(len(split(data['friends'])) > 5 and len(split(data['friends'])) < 20 and data['review_count'] > 5):
					output.write(line)	
			

