import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import cross_val_score

# Function importing Dataset 
def importdata(file): 
	data = pd.read_csv(file,sep= ',') 	
	return data 

	
# Function to perform training with giniIndex. 
def train_using_gini(X_train, Y_train): 

	clf_gini = DecisionTreeClassifier(
			criterion = "gini",random_state = 100) 
	clf_gini.fit(X_train, Y_train) 
	acc_scores = cross_val_score(clf_gini, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_gini, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores
	
# Function to perform training with entropy. 
def train_using_entropy(X_train,Y_train): 

	clf_entropy = DecisionTreeClassifier( 
			criterion = "entropy", random_state = 100)

	clf_entropy.fit(X_train, Y_train)
	acc_scores = cross_val_score(clf_entropy, X_train, Y_train, cv=5)
	f1_scores = cross_val_score(clf_entropy, X_train, Y_train, 
								cv=5, scoring='f1_macro')
	
	return acc_scores, f1_scores

def main(): 

	in_file = r'features.csv'
	data = importdata(in_file) 
	
	X = data.values[:, 2:8] #Features
	Y = data.values[:, 8] #Label
	
	#Convert Y into type int
	Y = Y.astype('int')

	acc_scores_gini,f1_scores_gini = train_using_gini(X, Y) 
	print("Mean of accurate using gini: {:.3f} (std: {:.3f})"
				.format(acc_scores_gini.mean(),acc_scores_gini.std()),end="\n\n" )
				
	print("Mean of F1 score using gini: {:.3f} (std: {:.3f})"
				.format(f1_scores_gini.mean(),f1_scores_gini.std()),end="\n\n" )
	
	acc_scores_entropy,f1_scores_entropy  = train_using_entropy(X, Y) 
	print("Mean of accurate using entropy: {:.3f} (std: {:.3f})"
				.format(acc_scores_entropy.mean(),acc_scores_entropy.std()),end="\n\n" )
				
	print("Mean of F1 score using entropy: {:.3f} (std: {:.3f})"
				.format(f1_scores_entropy.mean(),f1_scores_entropy.std()),end="\n\n" )

if __name__=="__main__": 
	main() 
