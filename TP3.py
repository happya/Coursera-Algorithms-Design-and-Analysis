import randata
import random

def pick(a):
    n=len(a)
    if n>0:
        i=random.randrange(0,n)
        j=a[i]
        if j==i:
            return i
        elif j<i:
            pick(a[i+1:n-1])
            if j>1:
                pick(a[0:j-1])
        else:
            pick(a[j+1:n-1])
            pick(a[0:i-1])
            
if __name__ == "__main__":
    a=[0,-1,2,4,6,8,10,7]
    print pick(a)