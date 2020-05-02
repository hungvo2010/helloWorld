def maximumSum(a, m):
    n=len(a)
    arr=[0 for i in range(m)]
    for i in a:
        arr[i%m]+=1
    sumx=-math.inf
    maxx=-math.inf
    for i in range(m):
            if sumx>0:
                sumx+=arr[i]
            else:
                sumx=arr[i]
            if sumx>maxx and sumx<m:
                maxx=sumx
    return maxx 