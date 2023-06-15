
from queue import PriorityQueue


def silnie_spójne_składowe(G):        # Wierzhołki u i v należą do silnie spójnych składowych jeśli istnieje droga z u do v
    n=len(G)                          # i droga z v do u (graf skierowany). Wykonujemy DFS i zapisujemy czasy przetworzenia
    u=0                               # następnie odwracamy graf skierowany i wykonujemy DFS zaczynając od wierzhołków z 
    TIME=DFS_czas_przetworzenia_DAG(G,u)  # największym (tu najmniejszym aby PriorityQueue działało) czasem przetworzenia
    H=[[] for _ in range(n)]              # Wierzchołki należące do tego samwgo wykonania DFS należą do tej samej silnie spójnej skł
    for i in range(n):
        for j in range(len(G[i])):
            H[G[i][j]].append(i)
    print(H)
    visited=[False for _ in range(n)]

    def DFS_Visit(G,vertex):
        visited[vertex]=True
        for i in range(len(G[vertex])):
            vertex1=G[vertex][i]
            print(vertex1)
            if visited[vertex1]==False:
                DFS_Visit(G,vertex1)
        Silnie.append(vertex)
    
    Spójne=[]
    for i in range(n):
        _,vertex=(TIME.get())
        print(vertex)
        if visited[vertex]==False:
            Silnie=[]
            DFS_Visit(H,vertex)
            Spójne.append(Silnie)


        
    
        




def DFS_czas_przetworzenia_DAG(G,n):   
    Q=PriorityQueue()  
    n=len(G)
    def DFS_Visit(G,u):
        nonlocal time
        visited[u]=True
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
             
                DFS_Visit(G,v)
        time-=1
        Q.put((u,time))
        time_array[u]=time


    time=n
    time_array=[0 for _ in range(n)]
    visited=[False for _ in range(n)]



    for i in range(n):

        if visited[i]==False:
            DFS_Visit(G,i)
    print(time_array)
    return Q


def DFS_Visit(G,vertex,visit):
    visit[vertex]=True
    for i in range(len(G[vertex])):
        vertex1=G[vertex][i]
        if visit[vertex1]==False:
            DFS_Visit(G,vertex,visit)
    

    




G=[[1],[2],[0,3,8],[4,6],[5],[3],[5],[8],[9],[5,10],[7,3]]
silnie_spójne_składowe(G)
