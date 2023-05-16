# Klasyczny algorytm BFS przechodzi jak fala po całym grafie. Wybieramy wierzchołek -> dodajemy go do kolejki -> patrzymy na wszystkich
# jego sąsiadów, jeśli ich nie odwiedziliśmy dodajemy ich do kolejki - > usuwamy wierzchołek którego sąsiadów rozpatrywaliśmy z kolejki

from time import sleep
from collections import deque


def BFS(macierz,start):      # Algorytm BFS, przechodzi po całym grafie, można nim sprawdzić najkrótszą ścieżkę do wierzchołka, czy 
    Q=deque([])              # graf jest spójny (tablica visited musi być cała w True), i odległość wierzchołków. Złożoność O(V^2)
    n=len(macierz)           # reprezentacja macierzowa
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    dist=[0 for _ in range(n)]
    distance=0
    Q.append(start)
    visited[start]=True
    dist[start]=0
    while len(Q)!=0:
        v=Q[0]
        distance+=1
        for i in range(n):
            if macierz[v][i]==True and visited[i]==False:
                Q.append(i)
                parent[i]=v
                visited[i]=True
                dist[v]=distance
        Q.popleft()



def BFS_list(GRAPH,start):     # ALgorytm BFS reprezentacja listowa złożoność(V+E)
    Q=deque([]) 
    n=len(GRAPH)
    VISITED=[False for _ in range(n)]
    PARENT=[None for _ in range(n)]
    DIST=[0 for _ in range(n)]
    distance=0
    Q.append(start)
    VISITED[start]=True
    DIST[start]=0
    while len(Q)!=0:
        vertex1=Q[0]
        distance+=1
        for i in range(len(GRAPH[vertex1])):
            vertex2=GRAPH[vertex1][i]
            if VISITED[vertex2]==False:
                Q.append(vertex2)
                PARENT[vertex2]=vertex2
                VISITED[vertex2]=True
                DIST[vertex2]=distance
        Q.popleft()
    

def BFS_1(macierz,start,end):      # wyszukaj najkrótszej drogi od wierzchołka start do end i podaj tą drogę, reprezentacja macierzowa
    Q=deque([])              
    n=len(macierz)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    dist=[0 for _ in range(n)]
    Q.append(start)
    visited[start]=True
    dist[start]=0
    while len(Q)!=0:
        v=Q[0]
        for i in range(n):
            if macierz[v][i]==True and visited[i]==False:
                if i==end:
                    parent[i]=v
                    path=[]
                    dist[i]=dist[v]+1
                    x=end
                    for i in range(dist[i]):
                        path.append(parent[x])
                        x=parent[x]
                    path=path[::-1]
                    print(path)
                    return dist[i]
                Q.append(i)
                parent[i]=v
                visited[i]=True
                dist[i]=dist[v]+1
        Q.popleft()
    

T=[[0,True,False,False],
   [False,0,False,True],
   [False,False,0,False],
   [True,False,True,0]]

print(BFS_1(T,0,2))
