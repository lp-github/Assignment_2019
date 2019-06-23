import numpy as np
def S_Dbw_score(data,labels,cluster_centers):
    '''
        data: np.array
        labels: list
        cluster_centers:list
    '''
    n,d = data.shape
    num_clusters=len(cluster_centers)
    var_data=[0]*(d)
    var_data_norm2=0
    var_cluster=[[0]*(d)]*num_clusters
    var_cluster_norm2=[0]*num_clusters
    ###calculate center of dataset
    center=[0]*d
    for i in range(0,d,1):
        for j in range (0,n,1):
            center[i]+=data[j][i]
        center[i]/=n
    ###calculate variance of dataset
    for i in range(0,d,1):
        for j in range(0,n,1):
            tmp = (data[j][i]-center[i])
            var_data[i]+= tmp*tmp
        var_data[i]/=n
    ###calculate variance of clusters
    for c in range(0,num_clusters,1):
        num_in_c=0
        for nn in range(0,n,1):
            if not labels[nn]==c:
                continue
            num_in_c+=1
            for dd in range(0,d,1):
                tmp==data[nn][dd]-cluster_centers[c][dd]
                var_cluster[c][dd]+=tmp*tmp
        for dd in range(0,d,1):
            var_cluster[c][dd]/=num_in_c
    ###calculate variance norm2 of dataset
    for i in range(0,d,1):
        var_data_norm2+=var_data[i]*var_data[i]
    var_data_norm2=np.sqrt(var_data_norm2)
    ###calculate variance norm2 of clusters
    for c in range(0,num_clusters,1):
        for dd in range(0,d,1):
            var_cluster_norm2[c]+=var_cluster[c][dd]*var_cluster[c][dd]
        var_cluster_norm2[c]=np.sqrt(var_cluster_norm2[c])
    ###calculate scatt
    scatt=0
    for i in range(num_clusters):
        scatt+=var_cluster_norm2[i]/var_data_norm2
    scatt/=num_clusters
    ###calculate stdev
    stdev=0
    for i in range(num_clusters):
        stdev+=var_cluster_norm2[i]
    stdev=np.sqrt(stdev)
    stdev/=num_clusters

    ###calculate density
    density=[0]*num_clusters
    for i in range(num_clusters):
        dens=0
        c_tmp=cluster_centers[i]
        for nn in range(n):
            if not labels[nn]==i:
                continue
            node_tmp=data[nn]
            #distance
            dis=0
            for dd in range(d):
                tmp=c_tmp[dd]-node_tmp[dd]
                tmp=tmp*tmp
                dis+=tmp
            dis=np.sqrt(dis)
            if dis <= stdev:
                dens+=1
        density[i]=dens
    ###calculate density of middle
    density_mid=[[0]*num_clusters]*num_clusters
    for i in range(num_clusters):
        center1=cluster_centers[i]
        for j in range(i,num_clusters,1):
            if(i==j):
                continue
            center2=cluster_centers[j]
            centerm=[0]*d
            for dd in range(d):
                centerm[dd]=(center1[dd]+center2[dd])/2
            dens=0
            for nn in range(n):
                if not(labels[nn]==i or labels[nn]==j):
                    continue
                node_tmp=data[nn] 
                dis=0
                for dd in range(d):
                    tmp=node_tmp[dd]-centerm[dd]
                    tmp=tmp*tmp
                    dis+=tmp
                dis=np.sqrt(dis)
                if(dis <= stdev):
                    dens += 1
            density_mid[i][j]=dens
            density_mid[j][i]=dens
    ###calculate dens_bw
    dens_bw=0
    for i in range(num_clusters):
        for j in range(num_clusters):
            if i==j :
                continue
            dens_bw = dens_bw + density_mid[i][j]/max(density[i],density[j])
    dens_bw = dens_bw/num_clusters/(num_clusters-1)
    return dens_bw+scatt