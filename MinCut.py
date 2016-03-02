import random
import copy

def contract(ver,edge):
    while len(ver)>2:
        index=random.randrange(0,len(edge))
        [u,v]=edge.pop(index)
        ver.remove(v)
        newEdge=list()
        for i in range(len(edge)):
            if edge[i][0]==v:
                edge[i][0]=u
            elif edge[i][1]==v:
                edge[i][1]=u
            if edge[i][0]!=edge[i][1]:
                newEdge.append(edge[i])
        edge=newEdge
    return(len(edge))

if __name__ == "__main__":
    fr=open('kargerMinCut.txt')
    arr1=fr.readlines()
    ver=list()
    edges=list()
    for line in arr1:
        line=line.split()
        ver.append(int(line[0]))
        for j in range(1,len(line)):
            if [int(line[j]),int(line[0])] not in edges and [int(line[0]),int(line[j])] not in edges:
                edges.append([int(line[0]),int(line[j])])
            
#print len(edges)
    result=list()
    for i in range(20000):
        v=copy.deepcopy(ver)
        edge=copy.deepcopy(edges)
        r=contract(v, edge)
        result.append(r)
    print(min(result))
    #print result