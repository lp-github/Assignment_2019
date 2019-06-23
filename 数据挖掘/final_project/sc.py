from sklearn.cluster import KMeans
import multiprocessing
from sklearn.metrics import silhouette_score   
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np
def train_cluster(train_vecs, model_name=None, start_k=2, end_k=20):
    print('training cluster')
    scores = []
    models = []
    for i in range(start_k, end_k):
        kmeans_model = KMeans(n_clusters=i )
        kmeans_model.fit(train_vecs)
        score = silhouette_score(train_vecs,kmeans_model.labels_,metric='euclidean')
        scores.append(score)  # 保存每一个k值的score值, 在这里用欧式距离
        print('{} Means score loss = {}'.format(i, score))
        models.append(kmeans_model)

    best_model = models[scores.index(max(scores))]
    return best_model

centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
centers=[]
for i in range(0,3):
    for j in range(0,3):
        centers.append([i,j])
for i in range(5,7):
    for j in range(5,7):
        centers.append([i,j])
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.1)

km=train_cluster(train_vecs=X)
print(km.n_clusters)
labels=km.labels_
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()

'''
mean = (1, 2)
cov = [[1, 0], [0, 1]]
#np.random.multivariate_normal(1.1, [[0,1],[1,0]])
Nf = 1000
dat1 = np.zeros((4000,2))
dat1[0:1000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean = [5, 6]
dat1[1000:2000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean = [3, -7]
dat1[2000:3000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean=[10,10]
dat1[3000:4000,:] = np.random.multivariate_normal(mean, cov, 1000)

km=train_cluster(train_vecs=dat1)
print(km.n_clusters)
labels=km.labels_
plt.scatter(dat1[:, 0], dat1[:, 1], c=labels)
plt.show()
'''