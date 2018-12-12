import pandas as pd 
import numpy as np 
import json
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing

# Function importing Dataset 
def importdata(file): 
	feats= np.zeros([181, 6])
	labels = np.zeros(181, dtype=np.int)
	with open(file, 'r') as f:
		for idx, line in enumerate(f):
			data = json.loads(line)
			feats[idx][0] = data['stars']
			feats[idx][1] = data['review_count']
			feats[idx][2] = data['price']
			feats[idx][3] = data['rate_review']
			feats[idx][4] = data['rate_useful']
			feats[idx][5] = data['rate_fans']
			labels[idx] = data['label']
	return feats,labels

	
# Function to perform training with giniIndex. 
def train_using_gini(X_train, Y_train,type): 

	clf_gini = DecisionTreeClassifier(
			criterion = "gini", max_depth = 100, random_state = 100) 
	clf_gini.fit(X_train, Y_train) 
	
	if type == 'normal':
		clf_gini = make_pipeline(preprocessing.StandardScaler(), clf_gini)
	
	elif type == 'minmax':
		clf_gini = make_pipeline(preprocessing.MinMaxScaler(), clf_gini)
		
	acc_scores = cross_val_score(clf_gini, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_gini, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores
	
# Function to perform training with entropy. 
def train_using_entropy(X_train,Y_train,type): 

	clf_entropy = DecisionTreeClassifier( 
			criterion = "entropy", max_depth = 100, random_state = 100)

	clf_entropy.fit(X_train, Y_train)
	
	if type == 'normal':
		clf_entropy = make_pipeline(preprocessing.StandardScaler(), clf_entropy)
	
	elif type == 'minmax':
		clf_entropy = make_pipeline(preprocessing.MinMaxScaler(), clf_entropy)	
	
	acc_scores = cross_val_score(clf_entropy, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_entropy, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores

def main(): 

	in_file = r'features.json'
	X,Y = importdata(in_file) 

	acc_scores_gini_un,f1_scores_gini_un = train_using_gini(X, Y, 'un') 
	print"Mean of accurate Gini using unprocessed data: %0.2f (+/- %0.2f)" % (acc_scores_gini_un.mean(), acc_scores_gini_un.std()) 
				
	print"Mean of F1 score Gini using unprocessed data: %0.2f (+/- %0.2f)" % (f1_scores_gini_un.mean(), f1_scores_gini_un.std()) 
	
	# acc_scores_gini_normal,f1_scores_gini_normal = train_using_gini(X, Y,'normal') 
	# print("Mean of accurate Gini using normal scale data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_gini_normal.mean(),acc_scores_gini_normal.std()),end="\n\n" )
				
	# print("Mean of F1 score Gini using normal scale data: {:.2f} (+/-: {:.2f})"
		# .format(f1_scores_gini_normal.mean(),f1_scores_gini_normal.std()),end="\n\n" )	
				
	# acc_scores_gini_minmax,f1_scores_gini_mixmax = train_using_gini(X, Y,'minmax') 
	# print("Mean of accurate Gini using normal scale data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_gini_minmax.mean(),acc_scores_gini_minmax.std()),end="\n\n" )
				
	# print("Mean of F1 score Gini using normal scale data: {:.2f} (+/-: {:.2f})"
		# .format(f1_scores_gini_mixmax.mean(),f1_scores_gini_mixmax.std()),end="\n\n" )	
	
	
	acc_scores_entropy_un,f1_scores_entropy_un  = train_using_entropy(X, Y, 'un') 
	print "Mean of accurate Entropy using unprocessed data: %0.2f (+/- %0.2f)" % (acc_scores_entropy_un.mean(), acc_scores_entropy_un.std())
				
	print "Mean of F1 score Entropy using unprocessed data: %0.2f (+/- %0.2f)" % (f1_scores_entropy_un.mean(), f1_scores_entropy_un.std())
				
	# acc_scores_entropy_normal,f1_scores_entropy_normal  = train_using_entropy(X, Y, 'normal') 
	# print("Mean of accurate Entropy using unprocessed data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_entropy_normal.mean(),acc_scores_entropy_normal.std()),end="\n\n" )
				
	# print("Mean of F1 score Entropy using unprocessed data: {:.2f} (+/-: {:.2f})"
		# .format(f1_scores_entropy_normal.mean(),f1_scores_entropy_normal.std()),end="\n\n" )
				
	# acc_scores_entropy_minmax,f1_scores_entropy_minmax  = train_using_entropy(X, Y, 'minmax') 
	# print("Mean of accurate Entropy using unprocessed data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_entropy_minmax.mean(),acc_scores_entropy_minmax.std()),end="\n\n" )
				
	# print("Mean of F1 score Entropy using unprocessed data: {:.2f} (+/-: {:.2f})"
		# .format(f1_scores_entropy_minmax.mean(),f1_scores_entropy_minmax.std()),end="\n\n" )				
				
				

if __name__=="__main__": 
	main() 
