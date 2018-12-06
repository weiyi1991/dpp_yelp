import json

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result
	
json_file_in_user ='yelp_academic_dataset_valid_user.json'

user_list = []

c = 0

with open(json_file_in_user, "r", encoding="utf8") as input:
	for line in input:
		if c < 10001:
			data = json.loads(line)	
			friend = split(data['friends'])
			user_list.append(data['user_id'])
			for i in friend:
				user_list.append(i)
			c+=1
		else:
			break

user_list = list(set(user_list)) #remove duplicates
		
# for i in res_list:
	# print(i)

json_file_in_review ='yelp_academic_dataset_res_review.json'
json_file_out ='yelp_academic_dataset_valid_user_review_small.json'
n = 0	
with open(json_file_in_review, "r", encoding="utf8") as input:
	with open(json_file_out, "w", encoding="utf8") as output:
		for line in input:	
			data = json.loads(line)	
			if data['user_id'] in user_list:
				output.write(line)	
				print(n)
				n+=1

			
