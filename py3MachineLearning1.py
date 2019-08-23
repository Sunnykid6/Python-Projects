from sklearn import tree

'''
smooth = 0
bumpy = 1
'''
features = [[140, 0], [130, 0], [150, 1], [170, 1]]

'''
apple = 2
orange = 3
'''
labels = [2, 2, 3, 3]

'''
clf = classifier
making a decision tree
'''
clf = tree.DecisionTreeClassifier()

'''
Training algorithm... "fit" Find pattern in data
'''
clf = clf.fit(features, labels)

'''
predicting what the thing should be based on the training data
'''
print(clf.predict([[150, 1]]))
