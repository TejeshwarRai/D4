from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

irisData = load_iris()
print(irisData)
print(type(irisData))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(irisData.data)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(irisData.target)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(irisData.target_names)

model = tree.DecisionTreeClassifier()

model.fit(irisData.data, irisData.target)

# print(model)

inputData = [5.5, 2.6, 4.4, 1.2]
predictedClass = model.predict([inputData])
print(predictedClass)

data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("iris dataset tree")
graph.view()
