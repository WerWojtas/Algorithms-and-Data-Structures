"""Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
stwierdza czy dany graf zawiera dobry początek"""



def good_start(G):           # Sortujemy graf topologicznie. Jeśli graf posiada dobry początek będzie to korzeń, z korzenia wykonujemy
    n=len(G)                  # DFS, sprawdzamy czy odwiedziliśmy wszystkie wierzchołki.
    VISITED=[False for _ in range(n)]
    SORTED=[]
    
    def DFS_Visit(G,vertex):
        VISITED[vertex]=True
        for j in range(len(G[vertex])):
            vertex2=G[vertex][j]
            if VISITED[vertex2]==False:
                DFS_Visit(G,vertex2)

        SORTED.append(vertex)

    for i in range(n):
        if VISITED[i]==False:
            DFS_Visit(G,i)
    x=len(SORTED)
    root=SORTED[x-1]
  

    VISITED=[False for _ in range(n)]
    DFS_Visit(G,root)
    for i in range(n):
        if VISITED[i]==False:
            return False
        
    return True


T=[[1,2],[3],[1,5],[4],[],[],[5]]
print(good_start(T))


        
                