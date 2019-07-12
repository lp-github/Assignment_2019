import scipy
import scipy.cluster.vq
import scipy.spatial.distance
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

EuclDist = scipy.spatial.distance.euclidean
def gapStat(data, resf=None, nrefs=10, ks=range(2,10)):
    '''
    Gap statistics
    '''
    # MC
    shape = data.shape
    if resf == None:
        x_max = data.max(axis=0)
        x_min = data.min(axis=0)
        dists = np.matrix(np.diag(x_max-x_min))
        rands = np.random.random_sample(size=(shape[0], shape[1], nrefs))
        for i in range(nrefs):
            rands[:,:,i] = rands[:,:,i]*dists+x_min
    else:
        rands = resf
    gaps = np.zeros((len(ks),))
    gapDiff = np.zeros(len(ks)-1,)
    sdk = np.zeros(len(ks),)
    for (i,k) in enumerate(ks):
        print('k=\t%d'%k)
        (cluster_mean, cluster_res) = scipy.cluster.vq.kmeans2(data, k)
        Wk = sum([EuclDist(data[m,:], cluster_mean[cluster_res[m],:]) for m in range(shape[0])])
        WkRef = np.zeros((rands.shape[2],))
        for j in range(rands.shape[2]):
            (kmc,kml) = scipy.cluster.vq.kmeans2(rands[:,:,j], k)
            WkRef[j] = sum([EuclDist(rands[m,:,j],kmc[kml[m],:]) for m in range(shape[0])])
        gaps[i] = scipy.log(scipy.mean(WkRef))-scipy.log(Wk)
        sdk[i] = np.sqrt((1.0+nrefs)/nrefs)*np.std(scipy.log(WkRef))

        if i > 0:
            gapDiff[i-1] = gaps[i-1] - gaps[i] + sdk[i]
    return gaps, gapDiff

mean = (1, 2)
cov = [[1, 0], [0, 1]]
#np.random.multivariate_normal(1.1, [[0,1],[1,0]])
Nf = 1000
dat1 = np.zeros((5000,2))
dat1[0:1000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean = [5, 6]
dat1[1000:2000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean = [3, -7]
dat1[2000:3000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean=[10,10]
dat1[3000:4000,:] = np.random.multivariate_normal(mean, cov, 1000)
mean=[8,8]
dat1[4000:5000,:] = np.random.multivariate_normal(mean, cov, 1000)
#plt.plot(dat1[::,0], dat1[::,1], 'b.', linewidth=1)
#plt.legend()
gaps,gapsDiff = gapStat(dat1)
#%matplotlib inline
f, (a1,a2) = plt.subplots(2,1)
a1.plot(gaps, 'g-o')
a2.bar(np.arange(start=2,stop=2+len(gapsDiff),step=1),gapsDiff)
f.show()
plt.show()

print(gaps,gapsDiff)
'''
centers = [[1, 1], [-1, -1], [1, -1]]

n_clusters = len(centers)
centers=[]
for i in range(0,3):
    for j in range(0,3):
        centers.append([i,j])

for i in range(5,7):
    for j in range(5,7):
        centers.append([i,j])
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.05)

gaps,gapsDiff=gapStat(X,ks=range(2,20,1))

#km=train_cluster(train_vecs=X)
#print(km.n_clusters)
#labels=km.labels_
plt.scatter(X[:,0],X[:,1])
print(gaps,gapsDiff)
plt.show()
'''