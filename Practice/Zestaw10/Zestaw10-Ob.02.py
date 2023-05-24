"""Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci macierzowej (domknięcie przechodnie grafu G, to graf nad tym
samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma krawędź z u do v wtedy i
tylko wtedy, gdy w G istnieje ścieżka z u do v."""


def domknięcie(G):
    n=len(G)
    VISITED=[False for _ in range(n)]

    def DFS_Visit(G,vertex,place):
        VISITED[vertex]=True
        for i in range(n):
            if G[vertex][i]==True:
                neighbour=i
                if VISITED[neighbour]==False:
                    SPÓJNE[place].append(neighbour)
                    DFS_Visit(G,neighbour,place)


    SPÓJNE=[]
    place=-1
    for i in range(n):
        if VISITED[i]==False:
            place+=1
            SPÓJNE.append([])
            SPÓJNE[place].append(i)
            DFS_Visit(G,i,place)
    
    M=[[False for _ in range(n)] for _ in range(n)]
    print(SPÓJNE)
    for i in range(len(SPÓJNE)):
        for j in range(len(SPÓJNE[i])):
            for k in range(j+1,len(SPÓJNE[i])):
                M[j][k]=True
                M[k][j]=True

    print(M)



T=[[False,True,True,False,False,False],
   [True,False,False,False,False,False],
   [True,False,False,False,False,False],
   [False,False,False,False,False,False],
   [False,False,False,False,False,True],
   [False,False,False,False,True,False]]

domknięcie(T)
