import numpy as np # You can set an alias for the library you imported
from sklearn.datasets import load_iris
from sklearn import tree
'''
This imports is for visualizing the 
decision tree later on

https://medium.com/@rnbrown/creating-and-visualizing-decision-trees-with-python-f8e8fa394176
https://github.com/scikit-learn/scikit-learn/blob/1495f6924/sklearn/tree/export.py#L655
'''
from sklearn.externals.six import StringIO  
import pydotplus

iris = load_iris()
'''
the first entry of each kind of flower
is at 0, 50, and 100. We'll omit these to 
use as a tester after the training data to 
ensure we are on the right track. We'll also
omit other random numbers for checking.
'''
test_idx = [0, 50, 100, 16, 25, 62, 32, 75, 99, 121]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

'''
this is the testing data
'''
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(clf.predict(test_data))


dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,  
			    feature_names=iris.feature_names, class_names=iris.target_names,
                filled=True, rounded=True,
                impurity=False,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_pdf("iris.pdf")

# Examples of how to use the data set

'''
this prints out the features that describes the flowers

print (iris.feature_names)
'''

'''
this prints out the species of flower

print (iris.target_names)
'''

'''
this prints out the data for that flower

print (iris.data[0])
'''

'''
this prints out the number for the flower 
in the target names

setosa = 0
versiclor = 1
virginica = 2

print (iris.target[0])
'''


'''
this iterates over the data set and tells you which example
what label is hsould get based on the target name
and the features of that flower

for i in range(len(iris.target)):
	print ("Example %d: label %s, feature %s" % (i, iris.target[i], iris.data[i]))
'''
