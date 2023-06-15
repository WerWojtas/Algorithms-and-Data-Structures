"""Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
innych w acyklicznym grafie skierowanym?"""

from collections import deque

def BFS(G,start):           # po prostu BFS
    n=len(G)
    DISTANCE=[10**10 for _ in range(n)]
    VISITED=[False for _ in range(n)]
    PARENT=[None for _ in range(n)]
    Q=deque()
    Q.append(start)
    DISTANCE[start]=0
    VISITED[start]=True
    while len(Q)!=0:
        vertex=Q[0]
        for i in range(len(G[vertex])):
            vertex2=G[vertex][i]
            if VISITED[vertex2]==False:
                Q.append(vertex2)
                VISITED[vertex2]=True
                PARENT[vertex2]=vertex
                DISTANCE[vertex2]=DISTANCE[vertex]+1

        Q.popleft()

    end=6
    PATH=[]
  
    while end!=start:
        PATH.append(end)
        if PARENT[end]==None:
            print("brak ścieżki")
            return
        else:
            end=PARENT[end]

    PATH=PATH[::-1]
  


T=[[1,2],[3],[1,5],[4],[],[],[5]]
BFS(T,0)



