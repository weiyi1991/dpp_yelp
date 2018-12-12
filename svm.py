from __future__ import division
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn import svm
from sklearn import metrics
import json

feature_json = 'features.json'
feats= np.zeros([181, 6])
labels = np.zeros(181, dtype=np.int)
with open(feature_json, 'r') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        feats[idx][0] = data['stars']
        feats[idx][1] = data['review_count']
        feats[idx][2] = data['price']
        feats[idx][3] = data['rate_review']
        feats[idx][4] = data['rate_useful']
        feats[idx][5] = data['rate_fans']
        labels[idx] = data['label']

# define classifiers without feature scaling
linear_svm = svm.SVC(kernel='linear', C=2, class_weight={0:2,1:1})
rbf_svm = svm.SVC(kernel='rbf', C=2, class_weight={0:2,1:1})
# classifier with standard scaling on features
linear_svm_scale = make_pipeline(preprocessing.StandardScaler(), svm.SVC(kernel='linear', C=2))
rbf_svm_scale = make_pipeline(preprocessing.StandardScaler(), svm.SVC(C=2))
# classifier with minmax scaling on features
linear_svm_minmax = make_pipeline(preprocessing.MinMaxScaler(), svm.SVC(kernel='linear', C=2))
rbf_svm_minmax = make_pipeline(preprocessing.MinMaxScaler(), svm.SVC(C=2))

# training classifier and compute scores
acc_linear = cross_val_score(linear_svm, feats, labels, cv=5)
print "Accuracy of unscaling linear svm: %0.2f (+/- %0.2f)" % (acc_linear.mean(), acc_linear.std() * 2)
f1_linear = cross_val_score(linear_svm, feats, labels, cv=5, scoring='f1_macro')
print "F1 of unscaling linear svm: %0.2f (+/- %0.2f)" % (f1_linear.mean(), f1_linear.std() * 2)

acc_rbf = cross_val_score(rbf_svm, feats, labels, cv=5)
print "Accuracy of standard scaling rbf svm: %0.2f (+/- %0.2f)" % (acc_rbf.mean(), acc_rbf.std() * 2)
f1_rbf = cross_val_score(rbf_svm, feats, labels, cv=5, scoring='f1_macro')
print "F1 of standard scaling rbf svm: %0.2f (+/- %0.2f)" % (f1_rbf.mean(), f1_rbf.std() * 2)

acc_linear = cross_val_score(linear_svm_scale, feats, labels, cv=5)
print "Accuracy of standard scaling linear svm: %0.2f (+/- %0.2f)" % (acc_linear.mean(), acc_linear.std() * 2)
f1_linear = cross_val_score(linear_svm_scale, feats, labels, cv=5, scoring='f1_macro')
print "F1 of standard scaling linear svm: %0.2f (+/- %0.2f)" % (f1_linear.mean(), f1_linear.std() * 2)

acc_rbf = cross_val_score(rbf_svm_scale, feats, labels, cv=5)
print "Accuracy of standard scaling rbf svm: %0.2f (+/- %0.2f)" % (acc_rbf.mean(), acc_rbf.std() * 2)
f1_rbf = cross_val_score(rbf_svm_scale, feats, labels, cv=5, scoring='f1_macro')
print "F1 of standard scaling rbf svm: %0.2f (+/- %0.2f)" % (f1_rbf.mean(), f1_rbf.std() * 2)


acc_linear = cross_val_score(linear_svm_minmax, feats, labels, cv=5)
print "Accuracy of minmax scaling linear svm: %0.2f (+/- %0.2f)" % (acc_linear.mean(), acc_linear.std() * 2)
f1_linear = cross_val_score(linear_svm_minmax, feats, labels, cv=5, scoring='f1_macro')
print "F1 of minmax scaling linear svm: %0.2f (+/- %0.2f)" % (f1_linear.mean(), f1_linear.std() * 2)

acc_rbf = cross_val_score(rbf_svm_minmax, feats, labels, cv=5)
print "Accuracy of minmax scaling rbf svm: %0.2f (+/- %0.2f)" % (acc_rbf.mean(), acc_rbf.std() * 2)
f1_rbf = cross_val_score(rbf_svm_minmax, feats, labels, cv=5, scoring='f1_macro')
print "F1 of minmax scaling rbf svm: %0.2f (+/- %0.2f)" % (f1_rbf.mean(), f1_rbf.std() * 2)
