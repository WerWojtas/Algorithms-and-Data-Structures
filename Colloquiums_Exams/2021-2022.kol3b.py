
import heapq

def airports( G, A, s, t ):
    G.append([])
    n=len(G)
    for i in range(n-1):
        G[i].append((n-1,A[i]))
        G[n-1].append((i,A[i]))

    
    return Dijkstra(G,n,s,t)
    



def Dijkstra(G,n,start,end):
    DISTANCE=[10**10 for _ in range(n)]
    VISITED=[False for _ in range(n)]
    DISTANCE[start]=0
    Q=[(DISTANCE[start],start)]
    heapq.heapify(Q)
    while len(Q)!=0:
        distance,vertex=heapq.heappop(Q)
        for i in range(len(G[vertex])):
            neighbour,cost=G[vertex][i]
            if VISITED[neighbour]==False and DISTANCE[neighbour]>distance+cost:
                DISTANCE[neighbour]=distance+cost
                heapq.heappush(Q,(DISTANCE[neighbour],neighbour))
        VISITED[vertex]=True

    return DISTANCE[end]


