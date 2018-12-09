import pandas as pd 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

# Function importing Dataset 
def importdata(file): 
	data = pd.read_csv(file,sep= ',') 	
	return data 

	
# Function to perform training with entropy. 
def train_using_Gaussian_bayesian(X_train,Y_train): 

	clf_GB = GaussianNB()

	clf_GB.fit(X_train, Y_train)
	
	acc_scores = cross_val_score(clf_GB, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_GB, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores

def main(): 

	in_file = r'features.csv'
	data = importdata(in_file) 
	
	X = data.values[:, 2:8] #Features
	Y = data.values[:, 8] #Label
	
	#Convert Y into type int
	Y = Y.astype('int')
	
	acc_scores_GB,f1_scores_GB  = train_using_Gaussian_bayesian(X, Y) 
	print("Mean of accurate Gaussian bayesian: {:.3f} (std: {:.3f})"
				.format(acc_scores_GB.mean(),acc_scores_GB.std()),end="\n\n" )
				
	print("Mean of F1 score using Gaussian bayesian: {:.3f} (std: {:.3f})"
				.format(f1_scores_GB.mean(),f1_scores_GB.std()),end="\n\n" )

if __name__=="__main__": 
	main() 
