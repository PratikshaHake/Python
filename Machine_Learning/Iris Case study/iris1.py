import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris=load_iris()

print("Feature names of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

test_index=[1,51,101]

train_target=np.delete(iris.target,test_index)
train_data=np.delete(iris.data,test_index,axis=0)

test_target=iris.target[test_index]
test_data=iris.data[test_index]

classifier=tree.DecisionTreeClassifier()

classifier.fit(train_data,train_target)

print("Values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))