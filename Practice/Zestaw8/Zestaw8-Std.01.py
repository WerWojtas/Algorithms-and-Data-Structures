# Sprawdzanie czy graf jest dwudzielny
from collections import deque

def Dwudzielny(GRAPH):     # ALgorytm BFS reprezentacja listowa złożoność(V+E). Idziemy BFSem i oznaczamy wierzchołki dwoma liczbami
    Q=deque([])            # (jeśli wierzchołek ma wartość 0 to wszystkie jego dzieci muszą mieć wartość 1), jeśli da się tak oznaczyć
    n=len(GRAPH)           # graf aby żadni sąsiedzi nie mieli przypisanego tego samego nr to jest dwudzielny
    VISITED=[False for _ in range(n)]
    PARENT=[None for _ in range(n)]
    COLORS=[None for _ in range(n)]
    start=0
    Q.append(start)
    VISITED[start]=True
    while len(Q)!=0:
        vertex1=Q[0]
        print(COLORS)
        for i in range(len(GRAPH[vertex1])):
            vertex2=GRAPH[vertex1][i]
            print(vertex1,vertex2)
            if VISITED[vertex2]==False:
                Q.append(vertex2)
                PARENT[vertex2]=vertex1
                VISITED[vertex2]=True
                if COLORS[vertex1]==0:
                    COLORS[vertex2]=1
                else:
                    COLORS[vertex2]=0
            else:
                if COLORS[vertex2]==COLORS[vertex1]:
                    return False
        Q.popleft()
    return True


T=[[1,2,3,5],[0,2,4],[0,1,3,5],[0,2,4],[1,3,5],[0,2,4]]
print(Dwudzielny(T))
