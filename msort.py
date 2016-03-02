def merge_sort(a):   
    if len(a)<=1:
        return a
    num=len(a)/2
    left=merge_sort(a[:num])
    right=merge_sort(a[num:])
   
    print left,right
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

if __name__ == "__main__":
    a=[5,3,8,9,1,7,0,2,6,4]
    print a 
    print merge_sort(a)
    