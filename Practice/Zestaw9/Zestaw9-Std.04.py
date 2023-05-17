"""Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
implementacji)
"""

from queue import PriorityQueue
from math import log2 as lg


def Iloczyn(G,start,end):
    n=len(G)
    
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    distance=[10**10 for _ in range(n)]
    distance[start]=1

    Q=PriorityQueue()
    Q.put((distance[start],start))
    while not Q.empty():
        dist,vertex=Q.get()
        for i in range(len(G[vertex])):
            neighbour,cost=G[vertex][i]
            print(neighbour)
            if visited[neighbour]==False and dist*cost<distance[neighbour]:
                distance[neighbour]=dist*cost
                parent[neighbour]=vertex
                Q.put((distance[neighbour],neighbour))
        visited[vertex]=True
    return distance[end]

        
def Iloczyn2(G,start,end):
    n=len(G)
    
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    distance=[10**10 for _ in range(n)]
    distance[start]=1

    Q=PriorityQueue()
    Q.put((distance[start],start))
    while not Q.empty():
        dist,vertex=Q.get()
        for i in range(len(G[vertex])):
            neighbour,cost=G[vertex][i]
            if visited[neighbour]==False and lg(dist)+lg(cost)<lg(distance[neighbour]):
                distance[neighbour]=dist*cost
                parent[neighbour]=vertex
                Q.put((distance[neighbour],neighbour))
        visited[vertex]=True
    return distance[end]

T=[[(1,2),(2,20)],
   [(0,2),(3,3)],
   [(0,20),(3,18)],
   [(1,3),(2,18),(4,4)],
   [(3,4),(5,13),(6,1)],
   [(4,13),(6,15)],
   [(4,1),(5,15),(7,3)],
   [(6,3)]]

print(Iloczyn2(T,0,7))