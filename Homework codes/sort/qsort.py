import randata

def partition1(a,p,r):
    x=a[p]
    i=p+1
    for j in range(p+1,r+1):
        if a[j]<x:
            a[j],a[i]=a[i],a[j]
            i+=1
    a[p],a[i-1]=a[i-1],a[p]
    return i-1

def partition2(a,p,r):
    a[p],a[r]=a[r],a[p]
    return partition1(a,p,r)

def partition3(a,p,r):
    m=(p+r)/2
    print a[p],a[m],a[r]
    xmin=min(a[p],a[m],a[r])
    xmax=max(a[p],a[m],a[r])
    
    if (a[p]==xmin)|(a[p]==xmax):
        
        if (a[r]==xmax)|(a[r]==xmin):
            a[p],a[m]=a[m],a[p]
        else:
            a[p],a[r]=a[r],a[p]
    print a[p],a[m],a[r]
    return partition1(a, p, r) 
        
    
    
    
    
            
        
            #print i

         
def quick_sort(a,left,right):
    n1,nl,nr=0,0,0
    if left<right:
        q=partition3(a,left,right)
        n1=right-left
        nl=quick_sort(a,left,q-1)
        nr=quick_sort(a,q+1,right)
    return n1+nl+nr
    
        
    
    
    
if __name__ == "__main__":
    #a=randata.getrandata(10)
    #print a
    a=[3,8,7,1,2,5,6,4]
    fr=open('QuickSort.txt')
    arr1=fr.readlines()
    a2=[]
    for line in arr1:
        line=line.strip()
        a2.append(int(line))
    n=len(a2)
        
    print quick_sort(a2, 0, n-1)
    #print num
    print a2