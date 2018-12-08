from __future__ import division
import json
import numpy
import pickle

def split(a):
	result = [x.strip() for x in a.split(',')]
	return result


def get_cat_rating(fid, restaurants, ratings):
    '''
    get the reviewed restaurants category and its corresponding rating stars by user fid.
    fid - user id
    restaurants - restaurant info dict
    ratings - rating info dict
    '''
    business = ratings[fid]['business_id'] # get the reviewed restaurants by fid
    rate_list = ratings[fid]['stars']
    fid_category = []
    fid_star = []
    fid_price = []
    for idx, bid in enumerate(business):
        cats = restaurants[bid]['category']
        for cat in cats:
            if cat != 'Restaurants' and cat != 'Food':
                fid_category.append(cat.lower())
                fid_star.append(float(rate_list[idx]))
                if restaurants[bid]['price']  == None:
                    fid_price.append(2.0) # if none price given, set to 2
                else:
                    fid_price.append(float(restaurants[bid]['price']))
    return fid_category, fid_star, fid_price

def most_common(lst):
    '''
    return the most common elements of a list
    '''
    return max(set(lst), key=lst.count)

def get_most_cat_rate(category, star):
    '''
    return the most common category reviewed by user, compute its rating stars

    category - business category label list, label may repeat cause it didn't get merged
    star - rating star for each business category
    '''
    common_ele = most_common(category)
    cnt = 0 # number of appearance of the most common category
    common_star= 0.0 # total review stars of the most common category
    common_price = 0.0 # total price range of the most common category
    for i, ele in enumerate(category):
        if ele == common_ele:
            cnt += 1
            common_star += star[i]
            common_price += price[i]

    average_stars = common_star / cnt # feature #1
    return common_ele, average_stars


if __name__ == '__main__':
    user_pickle = 'dataset/users.pkl'
    rating_pickle = 'dataset/ratings.pkl'
    restaurant_pickle = 'dataset/restaurants.pkl'

    ratings = pickle.load(open(rating_pickle, 'r'))
    users = pickle.load(open(user_pickle, 'r'))
    restaurants = pickle.load(open(restaurant_pickle, 'r'))

    # list to store features and label for each user
    feat_table = []
    # compute feature vector for each user
    for uid in users.keys():
        features = {}
        print 'uid: ', uid
        friends = users[uid]['friends'] # get his friends
        # get the most common category
        category = []
        star = []
        price = []
        fid_review_cnt = []
        fid_useful_cnt = []
        fid_fans_cnt = []
        fid_valid_list = [] # store valid friends, as key in the users dict
        for fid in friends:
            # if fid not in our used user list or ratings list, skip
            if fid not in users.keys() or fid not in ratings.keys():
                #friends.remove(fid)
                continue
            # get category list, rating star list for fid reviewed business
            fid_category, fid_star, fid_price = get_cat_rating(fid, restaurants, ratings)
            category = category + fid_category
            star = star + fid_star
            price = price + fid_price
            # get review count, useful number, fans number of user fid
            fid_valid_list.append(fid)
            fid_review_cnt.append(float(users[fid]['review_count']))
            fid_useful_cnt.append(float(users[fid]['useful']))
            fid_fans_cnt.append(float(users[fid]['fans']))
        # if neither of the friends are in our used_user list, skip
        if len(category) == 0:
            continue
        common_ele = most_common(category)
        cnt = 0 # number of appearance of the most common category
        common_star= 0.0 # total review stars of the most common category
        common_price = 0.0 # total price range of the most common category
        for i, ele in enumerate(category):
            if ele == common_ele:
                cnt += 1
                common_star += star[i]
                common_price += price[i]

        average_stars = common_star / cnt # feature #1
        review_count = cnt  # feature #2
        average_price = common_price / cnt # feature #3
        # get fid of most review_count, most useful_count, most fans
        fid_review = fid_valid_list[fid_review_cnt.index(max(fid_review_cnt))]
        fid_useful = fid_valid_list[fid_useful_cnt.index(max(fid_useful_cnt))]
        fid_fans = fid_valid_list[fid_fans_cnt.index(max(fid_fans_cnt))]
        # get most review_count fid's category and ratings list, get the ratings for the most common category
        fid_review_category, fid_review_star, fid_review_price = get_cat_rating(fid_review, restaurants, ratings)
        _, rate_review = get_most_cat_rate(fid_review_category, fid_review_star) # feature #4
        fid_useful_category, fid_useful_star, fid_useful_price = get_cat_rating(fid_useful, restaurants, ratings)
        _, rate_useful = get_most_cat_rate(fid_useful_category, fid_useful_star) # feature #5
        fid_fans_category, fid_fans_star, fid_fans_price = get_cat_rating(fid_fans, restaurants, ratings)
        _, rate_fans = get_most_cat_rate(fid_fans_category, fid_fans_star) #feature #6
        print uid, average_stars, review_count, average_price, rate_review, rate_useful, rate_fans

        features['uid'] = uid
        features['category'] = common_ele
        features['stars'] = average_stars
        features['review_count'] = review_count
        features['price'] = average_price
        features['rate_review'] = rate_review
        features['rate_useful'] = rate_useful
        features['rate_fans'] = rate_fans
        # get category of uid, if uid reviewed on that category, count as true
        if uid not in ratings.keys():
            features['label'] = 0
        else:
            uid_category, _, _ = get_cat_rating(uid, restaurants, ratings)
            if common_ele in uid_category:
                features['label'] = 1
            else:
                features['label'] = 0

        feat_table.append(features)

    with open('dataset/features.pkl', 'wb') as f:
        pickle.dump(feat_table, f)

    with open('dataset/features.json', 'wb') as f:
        for item in feat_table:
            json.dump(item, f)
            f.write('\n')
