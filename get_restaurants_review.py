import json

# def split(a):
	# result = [x.strip() for x in a.split(',')]
	# return result
	
json_file_in_res ='yelp_academic_dataset_restaurants.json'

res_list = []

with open(json_file_in_res, "r", encoding="utf8") as input:
	for line in input:
		data = json.loads(line)	
		res_list.append(data['business_id'])

res_list = list(set(res_list)) #remove duplicates
		
# for i in res_list:
	# print(i)

json_file_in_review ='yelp_academic_dataset_review.json'
json_file_out ='yelp_academic_dataset_res_review.json'
n = 0	
with open(json_file_in_review, "r", encoding="utf8") as input:
	with open(json_file_out, "w", encoding="utf8") as output:
		for line in input:	
			data = json.loads(line)	
			if data['business_id'] in res_list:
				output.write(line)	
				print(n)
				n+=1

			
