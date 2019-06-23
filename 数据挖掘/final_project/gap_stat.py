import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans, MeanShift
import gap_statistic
from gap_statistic import OptimalK


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

res= gap_statistic.KMeans.fit_predict(X=X)