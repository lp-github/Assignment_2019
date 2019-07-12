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
X, y = make_blobs(n_samples=100, n_features=3, centers=[[-10,-10,-10], [0,0,0],[10,10,10], [20,20,20]], cluster_std=[0.4, 0.2, 0.2, 0.2], 
                  random_state =9)
centers = [[1, 1], [-1, -1], [1, -1]]
centers=[]
for i in range(-5,5):
    for j in range(-5,5):
        centers.append([i,j])
print(len(centers))
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.15)
#plt.scatter(X[:, 0], X[:, 1], marker='o')
#np.array(la)
#a.tolist();
print(type(X))
'''X=[
    [1.0,1.0],
    [1.1,1.0],
    [1.1,1.1],
    [2.0,2.0],
    [3.0,3.0],
    [4.0,4.0]
]
X=np.array(X)'''
print(type(X))
plt.scatter(X[:, 0], X[:, 1], marker='o')
from sklearn.cluster import KMeans
km=KMeans(n_clusters=3)
y_pred = km.fit_predict(X)
centers=km.cluster_centers_
print(centers.shape)
print(km.inertia_)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#plt.show()

def findBestKByKLEstimator(data,min_k=-1,max_k=-1):
    assert(type(data)==list or type(data)==np.ndarray)
    if(type(data)==list):
        data=np.array(data)
    if(min_k==-1):
        min_k=2
    if(max_k==-1):
        print('if')
        max_k=len(data)-1
    n_samples=len(data)
    n_dim=data.shape[1]
    print('mink:\t%d'%min_k)
    print('maxk:\t%d'%max_k)
    print('n_samples:\t%d'%(len(data)-1))
    assert(min_k>=2 and max_k<=n_samples-1 and min_k < max_k)
    w=[]
    diff=[]
    kl=[]
    #####################################init #########################
    for k in range(max_k+2):
        w.append(0)
        diff.append(0)
        kl.append(0)
    #####################################w from min_k-1 to max_k +1 availabel from 1 to len(data);
    for k in range(min_k-1,max_k+1+1,1):
        #print (k)
        km=KMeans(n_clusters=k)
        labels=km.fit_predict(X)
        w[k]=km.inertia_
        print("%d:\t%f"%(k,w[k]))
    print()
    ######################################diff min_k to max_k+1 rely on w min_k-1 to max_k+1
    #diff[k]=(k-1)^(2/p)W_(k-1)-k^(2/p)W_k
    for k in range(min_k,max_k+1+1,1):
        diff[k]=pow((k-1),2/n_dim)*w[k-1]-pow(k,2/n_dim)*w[k]
        print("%d:\t%f"%(k,diff[k]))
    print()
    preferk=-1
    maxkl=-10000000.0
    ######################################kl min_k to max_k rely on diff min_k to max_k+1
    for k in range(min_k,max_k+1,1):
        
        kl[k]=abs(diff[k]/diff[k+1])
        if(maxkl < kl[k]):
            preferk=k
            maxkl=kl[k]
        print("%d :\t %f"%(k,kl[k]))
    print("max k:%d"%preferk)
    return preferk

#def findBestKBy
preferk=findBestKByKLEstimator(data=X,max_k=150)
#preferk=4
km=KMeans(n_clusters=preferk)
y_pred = km.fit_predict(X)
#print(km.inertia_)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

