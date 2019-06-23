from sklearn.cluster import KMeans
import multiprocessing
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
def train_cluster(train_vecs, model_name=None, start_k=2, end_k=20):
    print('training cluster')
    SSE = []
    SSE_d1 = [] #sse的一阶导数
    SSE_d2 = [] #sse的二阶导数
    models = [] #保存每次的模型
    for i in range(start_k, end_k):
        kmeans_model = KMeans(n_clusters=i )
        kmeans_model.fit(train_vecs)
        SSE.append(kmeans_model.inertia_)  # 保存每一个k值的SSE值
        print('{} Means SSE loss = {}'.format(i, kmeans_model.inertia_))
        models.append(kmeans_model)
    # 求二阶导数，通过sse方法计算最佳k值
    SSE_length = len(SSE)
    print('d1:\t')
    for i in range(1, SSE_length):
        SSE_d1.append((SSE[i - 1] - SSE[i]) / 2)
        print(SSE_d1[-1])
    print('d2:\t')
    for i in range(1, len(SSE_d1) - 1):
        SSE_d2.append((SSE_d1[i - 1] - SSE_d1[i]) / 2)
        print(SSE_d2[-1])
    best_model = models[SSE_d2.index(max(SSE_d2)) + 1]
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
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.15)

km=train_cluster(train_vecs=X)
print(km.n_clusters)
labels=km.labels_
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()