
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.pairwise import pairwise_distances_argmin
import matplotlib.pyplot as plt
import my_s_dbw as sdbw
import myS_Dbw as sdbw_f
#import matplotlib.pyplot as plt

np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
centers=[]
for i in range(0,3):
    for j in range(0,3):
        centers.append([i,j])
for i in range(5,7):
    for j in range(5,7):
        centers.append([i,j])
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.5)


score=sdbw.S_Dbw_score(X,labels_true,centers)
print(score)

def findBestKByS_DbwEstimator(data,min_k=2,max_k=100):
    preferk=-1
    min_score=100000
    for k in range(min_k,max_k+1,1):
        k_means = KMeans(init='k-means++', n_clusters=k, n_init=10)
        labels=k_means.fit_predict(X)

        k_means_cluster_centers = k_means.cluster_centers_
        k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)

        KS = sdbw_f.S_Dbw(X, k_means_labels, k_means_cluster_centers)
        score=KS.S_Dbw_result()
        #score2=sdbw.S_Dbw_score(X,labels,k_means_cluster_centers)
        print('herek:%d\tscore:%f'%(k,score))
        if(score < min_score):
            min_score=score
            preferk=k
    return preferk
preferk=findBestKByS_DbwEstimator(X,min_k=2,max_k=20)
print("prefer k:\t%d"%preferk)
km=KMeans(n_clusters=preferk)
y_pred = km.fit_predict(X)
#print(km.inertia_)
print(km.cluster_centers_)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
#print(KS.S_Dbw_result())