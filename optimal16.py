def optcost(freq,i,j):
    if j<i:
        return 0
    if j==i:
        return freq[i]
    fsum=sum(freq,i,j)
    min=999999999999
    for r in range(i,j+1):
        cost=(optcost(freq,i,r-1)+optcost(freq,r+1,j))
        if cost<min:
            min=cost
    return min+fsum
def optimlsearchtree(keys,freq,n):
    return optcost(freq,0,n-1)
def sum(freq,i,j):
    s=0
    for k in range(i,j+1):
        s+=freq[k]
    return s
if __name__=='__main__':
    keys=[10,12,20]
    freq=[34,8,50]
    n=len(keys)
    print("cost of optimal bst is",optimlsearchtree(keys,freq,n))
