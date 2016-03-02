# -*- coding:utf-8 -*-
'''
    
    dijkstra 算法计算最短路径，通过优先队列Q实现
    subroutine dij(G,s)返回以s为源点，到途中所有点的最短路径
    优先队列Q的每个结点保存vertice和s到该vertice的最短距离
    在所有未访问的点中，
    从Q的栈顶取出结点v和s到v的最短距离值
        对所有从v出发的边的终点y，更新dis[y]=min(dis[y],dis[v]+l(v->y))
    
'''

class stack(list):
    add=list.append
    
    
def dij(G,s):
    '''
    dis保存源点到所有点的最短距离值
    '''
    dis=[1000000 for i in range(VN)]  #距离值初始化
    dis[0]=0
    dis[s]=0
    '''
       优先队列Q的每个结点保存vertice和s到该vertice的最短距离
    '''
    Q=stack()
    Q.add([s,dis[s]])
    '''
        从Q的栈顶取出结点v和s到v的最短距离值
        对所有从v出发的边的终点y，更新dis[y]=min(dis[y],dis[v]+l(v->y))
    '''
    while Q:
        node=Q.pop()
        v,dsv=node[0],node[1]
        for i in range(len(G[v])):
            y=G[v][i]
            vout,dvy=y[0],y[1]
            if dis[vout]>dsv+dvy:       
                dis[vout]=dsv+dvy
                Q.add([y[0],dis[vout]])
    return dis
        

    




if __name__ == "__main__":
    fr=open('dijtest1.txt')
    VN=15
    arr1=fr.readlines()
    G= [[] for i in range(VN)]
    for line in arr1:
        line=line.split()
        ver=int(line[0])
        outver=len(line)-1
        G[ver]=[[] for i in range(outver)]
        for i in range(1,len(line)):
            outv=int(line[i].split(',')[0])
            outd=int(line[i].split(',')[1])
            G[ver][i-1].append(outv)
            G[ver][i-1].append(outd)
    #print G
    dis=dij(G,13)
    #print dis[7],dis[37],dis[59],dis[82],dis[99],dis[115],dis[133],dis[165],dis[188],dis[197]
    print "The shortest distance between ver#13 and ver#5 is %d."%(dis[5])