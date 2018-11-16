import Queue
import sys
#ulimit -s 30788


class stack(list):
    add=list.append


def scc(G,GT,MAXN):
    sccs,seen=[],set()
    for u in dfssort(G):
        if u in seen:
            continue
        C=walk(GT,u,seen)
        
        seen.update(C)
        sccs.append(C)
    return sccs

def dfs_topsort(G):
    visited,res=set(),[]
    def recurse(u):
        if u in visited:
            return
        visited.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
        #print res
    for u in range(1,MAXN):
        recurse(u)
        #print res
    res.reverse()
    return res

def dfssort(G):
    res,visited=[],set()
    Q=stack()
    for i in range(1,MAXN):
        if i in visited:
            continue
        visited.add(i)
        Q.add(i)
        while Q:
            #print Q
            u=Q[-1]
            visited.add(u)
            i=0
            if len(G[u])>0:
                for v in G[u]:
                    if v in visited:
                        i+=1
                    else:
                        visited.add(v)
                        Q.add(v)
                        break
                    if i==len(G[u]):
                        Q.pop()
                        res.append(u)
                    #res.reverse()
            else:
                Q.pop()
                res.append(u)
                
    res.reverse()           
    return res
    
def stack_dfs(G):
    res,newh=[],[]
    S=set()
    for u in range(1,MAXN):
        if u in S:
            continue
        S.add(u)
        newh=list(traverse(G,u,stack))
        #print newh
        #newh=newh[::-1]
        for i in newh[::-1]:
            if i not in res:
                res.append(i)
        #print res
    res=res[::-1] 
    return res
        
    
            
def traverse(G,s,qtype=set):
    S,Q=set(),qtype()
    Q.add(s)
    while Q:
        u=Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u
    
        
def walk(G,s,S):
    P,Q=dict(),set()
    P[s]=None
    Q.add(s)
    while Q:
        # P
        u=Q.pop()
        for v in G[u]:
            if not (v in S or v in P):
                Q.add(v)
                P[v]=u
    return P
def iter_dfs(G):
    S,Q=set(),[]
    Q.append(1)
    while Q:
        u=Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u
    

    
                
    
if __name__ == "__main__":
    #sys.setrecursionlimit(70000)
    MAXN1=875715
    MAXN=MAXN1
    fr=open('Scc.txt')
    arr1=fr.readlines()
    G= [[] for i in range(MAXN)]
    GT= [[] for i in range(MAXN)]    
    #ver1=set()
    edges,tedges=[],[]
    #ver=[]
        
    for line in arr1:
        line=line.split()
        i=int(line[0])
        j=int(line[1])
        #ver1.add(i)
        G[i].append(int(line[1])) 
        GT[j].append(int(line[0]))
        
    #sccs=scc(G,GT) 
    #print G   
    #print GT
    #
    #print dfs_topsort(G)
   
    #print scc(G, GT)
    a=[]
    sccs=scc(G,GT,MAXN)
    n=len(sccs)
    for i in range(n):
        #print len(sccs[i])
        a.append(len(sccs[i]))
    
    a.sort(reverse=True)
    #print a
    for j in range(5):
        print a[j]
    #res=stack_dfs(G, 1)
    #print walk(G, 1, S)
    #print list(iter_dfs(G, 1))
    
    #a=stack_dfs(G)
    #print dfssort(G)