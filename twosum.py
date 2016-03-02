
def merge_sort(a):   
    if len(a)<=1:
        return a
    num=len(a)/2
    left=merge_sort(a[:num])
    right=merge_sort(a[num:])
   
    #print b
    return merge(left, right)

def merge(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+=right[r:]
    #print result
    return result

def bsearch(a,start,end,n):
    while start<end:
        mid=(start+end)/2
        if a[mid]<n:
            start=mid+1
        elif a[mid]>n:
            end=mid
        else:
            return True
    return False
    
    
    
    




if __name__ == "__main__":
    fr=open('twosum.txt')
    d1=[]
    arr1=fr.readlines()
    for line in arr1:
        line=line.split()
        d1.append(int(line[0]))
    
    n=len(d1)
    sum1=set()
    s=merge_sort(d1)
    #s=merge_sort(d1)
    buckets={}
    for i in range(1000000):
        bn=abs(s[i])/10000
        if bn not in buckets:
            buckets[bn]=[]
        buckets[bn].append(s[i])
    print buckets[419700]   
   
    #print bsearch(s,0,n,12)
    '''
    for t in range(-10000,10001):
        if t not in sum1:
            for i in range(n):
                x=s[i]
                y=t-x
                #ymin=abs(-10000-x)%10000
                #ymax=abs(10000-x)%10000
                xbn=abs(x)/10000
                ybn=abs(y)/10000

                if ybn in buckets and xbn<=ybn and bsearch(buckets[ybn], 0, len(buckets[ybn]), y):
                    sum1.add(t)
                    print t
                    break
                    #print x,y,
                    #print t
                    
                #break
                    
    '''
          
    for i in range(n):
        x=s[i]
        xbn=x/10000
        ymin=abs(-10000-x)/10000
        ymax=abs(10000-x)/10000
        for j in range(ymin,ymax+1):
            if j in buckets and j>=xbn:
                for y in buckets[j]:
                    t=x+y
                    if t not in sum1 and t in range(-10000,10001):
                        sum1.add(t)
                        #print i,t
                                    
               
    print len(sum1)
    