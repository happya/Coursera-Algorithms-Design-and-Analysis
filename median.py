
def max_heapify(a,start,end):
    l=2*start+1 
    r=l+1
    if l<=end and a[l]>a[start]:
        largest=l
    else: 
        largest=start
    if r<=end and a[r]>a[largest]:
        largest=r
    if not largest==start:
        a[start],a[largest]=a[largest],a[start]
        max_heapify(a,largest,end)

def min_heapify(a,start,end):
    l=2*start+1 
    r=l+1
    if l<=end and a[l]<a[start]:
        smallest=l
    else: 
        smallest=start
    if r<=end and a[r]<a[smallest]:
        smallest=r
    if not smallest==start:
        a[start],a[smallest]=a[smallest],a[start]
        max_heapify(a,smallest,end)
        
def heap_sort(a):
    n=len(a)
    for j in range(n/2,-1,-1):
        #print j
        max_heapify(a,j,n-1)
        
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        max_heapify(a,0,i-1)
    return a

def find_m(x):
    n=len(x)
    print n
    m,Hlow,Hhigh=[],[],[]

    for i in range(n):
        xi=x[i]
        #print i,xi
        nlow=len(Hlow)
        nhigh=len(Hhigh)
        #print nlow,nhigh
        if i==0:
            m.append(xi)
            Hhigh.append(xi)
            nhigh=1
            continue
        elif i==1:
            m.append(min(m[0],xi))
            Hhigh[0]=max(m[0],xi)
            Hlow.append(m[1])
            nhigh=1
            nlow=1
            continue
        elif xi>Hhigh[0]:
            Hhigh.append(xi)
            nhigh+=1
            for j in range(nhigh/2,-1,-1):
                min_heapify(Hhigh,j,nhigh-1)
            
        else:
            Hlow.append(xi)
            nlow+=1
            for j in range(nlow/2,-1,-1):
                max_heapify(Hlow,j,nlow-1)
            
            #print "h",Hhigh
            
        
            #print Hhigh,Hlow
        if i%2==0:
            while (nhigh<=i/2):
                Hlow[-1],Hlow[0]=Hlow[0],Hlow[-1]
                Hhigh.append(Hlow.pop())
                nhigh+=1
                nlow-=1
            #print Hhigh,nhigh,Hlow,nlow
                for j in range(nhigh/2,-1,-1):
                    min_heapify(Hhigh,j,nhigh-1)
                for j in range(nlow/2,-1,-1):
                    max_heapify(Hlow,j,nlow-1)
            m.append(Hhigh[0])
                
        else:
            #print i,nlow,Hlow
            while (nlow<(i+1)/2):
                Hhigh[-1],Hhigh[0]=Hhigh[0],Hhigh[-1]
                Hlow.append(Hhigh.pop())
                nhigh-=1
                nlow+=1
            #print Hhigh,nhigh,Hlow,nlow
                for j in range(nhigh/2,-1,-1):
                    min_heapify(Hhigh,j,nhigh-1)
                for j in range(nlow/2,-1,-1):
                    max_heapify(Hlow,j,nlow-1)
            m.append(Hlow[0])
        #print Hhigh,Hlow,m[i]
    return m

if __name__ == "__main__":
    fr=open('Median.txt')
    x=[]
    arr1=fr.readlines()
    for line in arr1:
        line=line.split()
        x.append(int(line[0]))
        
    test1=[11,3,6,9,2,8,4,10,1,12,7,5]
    test2=[1,2,4,3,5,6,8,7,9]
    m=find_m(x)
    mmod=sum(m)%10000
    print m,mmod
            
             
    