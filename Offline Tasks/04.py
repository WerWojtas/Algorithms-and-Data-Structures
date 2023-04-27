# We have a graph, a start and end vertex. We need find the edge after wchich removal the shortest path from start to end will increase. 


from collections import deque



def longer(G,s,t):
    dist,PATH=BFS_1(G,s,t)
    for i in range(1,dist+1):
        k1=PATH[i-1]
        k2=PATH[i]
        distance=BFS_2(G,s,t,k1,k2)
        if distance==-1:
            return(k1,k2)
        if distance>dist:
            return(k1,k2)
    return None






def BFS_1(macierz,start,end):      # BFS algorithm 
    Q=deque([])              
    lenght=len(macierz)
    visited=[False for _ in range(lenght)]
    parent=[None for _ in range(lenght)]
    dist=[0 for _ in range(lenght)]
    Q.append(start)
    visited[start]=True
    dist[start]=0
    while len(Q)!=0:
        v=Q[0]
        n=len(macierz[v])
        for i in range(n):
            u=macierz[v][i]
            if visited[u]==False:
                if u==end:
                    parent[end]=v
                    path=[end]
                    x=end
                    dist[end]=dist[v]+1
                    for i in range(dist[end]):
                        path.append(parent[x])
                        x=parent[x]
                    return dist[end],path
                Q.append(u)
                parent[u]=v
                visited[u]=True
                dist[u]=dist[v]+1
        Q.popleft()
    return 0,[]

def BFS_2(macierz,start,end,k1,k2):      
    Q=deque([])              
    lenght=len(macierz)
    visited=[False for _ in range(lenght)]
    dist=[0 for _ in range(lenght)]
    Q.append(start)
    visited[start]=True
    dist[start]=0
    while len(Q)!=0:
        v=Q[0]
        n=len(macierz[v])
        for i in range(n):
            u=macierz[v][i]
            if(v==k1 and u==k2)or(v==k2 and u==k1):
                continue
            if visited[u]==False:
                if u==end:
                    dist[end]=dist[v]+1
                    return dist[end]
                Q.append(u)
                visited[u]=True
                dist[u]=dist[v]+1
        Q.popleft()
    return -1
        
