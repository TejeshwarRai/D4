from sklearn.naive_bayes import GaussianNB

data = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500],
       ]

labels = [0, 0, 0, 0, 1, 1, 1, 1]

name = ['bike', 'car']

model = GaussianNB()

model.fit(data, labels)

sampleinp = [180,300]

predictedclass = model.predict([sampleinp])

print("predicted class is", predictedclass)
print("predicted class is", predictedclass[0])
print("predicted class is", name[predictedclass[0]])
# natural language/writing processing
