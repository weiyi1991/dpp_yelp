## User Dining Preference Prediction Based on Social Network Reviews

Team project of CSI 535 Data mining.

### Problem and research question definition:

The YELP dataset provides millions of reviews for the restaurant. We are curious about how do users decide to dine in a a certain type of restaurants based on their friend reviews. To put it in another word, given the reviews of one’s friends, we would like to predict the user’s dining preference to a certain type of restaurant. This project can help us discover the latent correlation between the user’s decision and the influence of social network reviews.


### TODO
- [ ] Data preprocessing
- [ ] Feature extraction, label preparation.
- [ ] Training/testing set preparation
- [ ] Train classifier
- [ ] Evaluation

### Usage Instruction
1. Download the Yelp dataset. extract all the files to `dataset/`
2. Extract the users records that has `'friends'`, which are `879891` in total. Take users with 5-10 friends
3. Business to category `'RestaurantsPriceRange2'`
4. Review that contains the bus_id and user_id in our selected records.
5. Features: average_stars in the review.json, number of friend reviews for the business category, average price range of a restaurant category your friends reviewed, highest number of review friend rating, friend rating who has the highest useful count, friend rating who has the most fans.
6. Labels: compute average rating of that user on a specific category, if >3.0, mark as `Ture`.
