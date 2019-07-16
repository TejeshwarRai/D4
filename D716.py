from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 0, 2, 4, 5]
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.scatter(x, y)
# plt.title("k - means")
# plt.show()
#

data = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500]
       ]



clusters = 2
model = KMeans(n_clusters=clusters)
model.fit(data)

predictions = model.predict(data)
print(predictions)
