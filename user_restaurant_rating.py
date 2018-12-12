#Group all the review of 1 user into 1 line
import json

test_file ='used_review.json'
out_file = 'user_restaurant_rating.json'
list = []

#list of all user-res-rating.
with open(test_file, "r", encoding="utf8") as input:
	for line in input:
		data = json.loads(line)
		user = data['user_id']
		restaurant = data['business_id']
		rating = data['stars']
		d = [user,restaurant,rating]
		list.append(d)

all = {}

#group user into one line
for user, restaurant, rating in list:
     user_data = all.setdefault(user, {})
     user_data.setdefault(restaurant,[]).append(rating)

#write to json
with open(out_file,'w') as output:
	for i,k in all.items():
		d={}
		d['user_id'] = i
		res = []
		stat = []
		for j,l in k.items():
			res.append(j)
			for m in l:
				stat.append(m)
		d['business_id'] = res
		d['stars'] = stat
		json.dump(d, output)	
		output.write('\n')
