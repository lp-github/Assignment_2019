'''
KL(k)=diff(k)/diff(k+1)
diff[k]=(k-1)^(2/p)W_(k-1)-k^(2/p)W_k
p:dimension of sample
W_k:sum of square of distance between sample points to cluster centers

input :
data m*n
labels:
'''
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_blobs
# X为样本特征，Y为样本簇类别， 共1000个样本，每个样本2个特征，共4个簇，簇中心在[-1,-1], [0,0],[1,1], [2,2]， 簇方差分别为[0.4, 0.2, 0.2]
X, y = make_blobs(n_samples=5000, n_features=2, centers=[[-1,-1], [0,0],[1,1], [2,2]], cluster_std=[0.4, 0.2, 0.2, 0.2], 
                  random_state =9)
#plt.scatter(X[:, 0], X[:, 1], marker='o')
print(type(X))
'''X=[
    [1.0,1.0],
    [1.1,1.0],
    [1.1,1.1],
    [2.0,2.0],
    [3.0,3.0],
    [4.0,4.0]
]'''
print(type(X))
plt.scatter(X[:, 0], X[:, 1], marker='o')
from sklearn.cluster import KMeans
km=KMeans(n_clusters=3)
y_pred = km.fit_predict(X)
centers=km.cluster_centers_
print(centers.shape)
print(km.inertia_)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

max_k=100
w=[]
diff=[]
kl=[]
for k in range(max_k+1):
    w.append(0)
    diff.append(0)
    kl.append(0)
for k in range(1,max_k+1,1):
    #print (k)
    km=KMeans(n_clusters=k)
    labels=km.fit_predict(X)
    w[k]=km.inertia_
    print("%d:\t%f"%(k,w[k]))
print()
for k in range(2,max_k,1):
    diff[k]=(k-1)*w[k-1]-k*w[k]
    print("%d:\t%f"%(k,diff[k]))
print()
preferk=-1
maxkl=-10000000.0
for k in range(2,9,1):
    
    kl[k]=abs(diff[k]/diff[k+1])
    if(maxkl < kl[k]):
        preferk=k
        maxkl=kl[k]
    print("%d :\t %f"%(k,kl[k]))
print("max k:%d"%preferk)
km=KMeans(n_clusters=preferk)
y_pred = km.fit_predict(X)
#print(km.inertia_)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()