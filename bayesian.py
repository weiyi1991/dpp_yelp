import numpy as np 
import json
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB
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
	
def train_using_Gaussian_bayesian(X_train,Y_train,type): 

	clf_GB = GaussianNB()

	clf_GB.fit(X_train, Y_train)
	
	if type == 'normal':
		clf_GB = make_pipeline(preprocessing.StandardScaler(), clf_GB)
	
	elif type == 'minmax':
		GB_minmax_scale = make_pipeline(preprocessing.MinMaxScaler(), clf_GB)
	
	acc_scores = cross_val_score(clf_GB, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_GB, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores
	
def main(): 

	in_file = r'features.json'

	X,Y = importdata(in_file) 
	
	acc_scores_GB_un,f1_scores_GB_un  = train_using_Gaussian_bayesian(X, Y, 'un') 
	print "Mean of accurate Gaussian bayesian using unprocessed data: %0.2f (+/- %0.2f)" % (acc_scores_GB_un.mean(), acc_scores_GB_un.std()) 
				
	print "Mean of F1 score using Gaussian bayesian using unprocessed data: %0.2f (+/- %0.2f)" % (f1_scores_GB_un.mean(), f1_scores_GB_un.std()) 
				
				
	# acc_scores_GB_normal,f1_scores_GB_normal  = train_using_Gaussian_bayesian(X, Y, 'normal') 
	# print("Mean of accurate Gaussian bayesian using normal scaled data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_GB_normal.mean(),acc_scores_GB_normal.std()),end="\n\n" )
				
	# print("Mean of F1 score using Gaussian bayesian using normal scaled data:{:.2f} (+/-: {:.2f})"
		# .format(f1_scores_GB_normal.mean(),f1_scores_GB_normal.std()),end="\n\n" )

	# acc_scores_GB_minmax,f1_scores_GB_minmax  = train_using_Gaussian_bayesian(X, Y, 'minmax') 
	# print("Mean of accurate Gaussian bayesian using minmax scaled data: {:.2f} (+/-: {:.2f})"
		# .format(acc_scores_GB_minmax.mean(),acc_scores_GB_minmax.std()),end="\n\n" )
				
	# print("Mean of F1 score using Gaussian bayesian using minmax scaled data: {:.2f} (+/-: {:.2f})"
		# .format(f1_scores_GB_minmax.mean(),f1_scores_GB_normal.std()),end="\n\n" )				

if __name__=="__main__": 
	main() 
