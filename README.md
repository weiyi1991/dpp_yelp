## User Dining Preference Prediction Based on Social Network Reviews

Team project of CSI 535 Data mining.

### Problem and research question definition:

The YELP dataset provides millions of reviews for the restaurant. We are curious about how do users decide to dine in a a certain type of restaurants based on their friend reviews. To put it in another word, given the reviews of one’s friends, we would like to predict the user’s dining preference to a certain type of restaurant. This project can help us discover the latent correlation between the user’s decision and the influence of social network reviews.


### Usage Instruction
Make sure you have installed [scikit-learn](https://scikit-learn.org/stable/index.html) on your python environment and we use Python2.
1. Download the Yelp dataset. extract all the files to `dataset/`.
2. Feature extraction (If you want to just run the classifiers, skip it, just use the extracted `features.json`). First run `get_*.py` to shrink the original dataset to a smaller size and store the useful information. Then run `feature_extrac.py` to extract feature matrix and labels. It will take a long time, we recommend you use our already extracted features `features.json`.
3. Run `svm.py`, `tree.py`, `bayesian.py` to get the prediction accuracy and F1-score on the dataset.
