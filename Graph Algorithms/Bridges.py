

def Mosty(G):     # Algorytm znajdowania mostów za pomocą DFS. Wykonujemy DFS raz i zapisujemy czasy przetworzenia wierzchołków
    n=len(G)      # w tablicy time, oraz LOW, następnie wykonujemy funkcję low która dla każdego wierzchołka ustawia jego wartość tablicy LOW
    def DFS_Visit(G,u):  # na najmiejszą z wartości LOW jego sąsiadów (oprócz rodzica). Jeśli wartość tablicy LOW wierzchołka jest
        nonlocal time    # równa początkowemu czasowi przetworzenia (nie została zmieniona w funkcji low) i wierzchołek ma rodzica, to
        visited[u]=True  # wierzchołek oraz jego rodzic są mostem
        time_array[u]=time
        LOW[u]=time
        time+=1
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                parent[v]=u
                DFS_Visit(G,v)

    time=0
    time_array=[-1 for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    LOW=[0 for _ in range(n)]
    
    for i in range(n):
        if visited[i]==False:
            DFS_Visit(G,i)
        
    
    Bridges=[]
    def low(G,vertex):
        flag=0
        for i in range(len(G[vertex])):
            vertex2=G[vertex][i]
            if vertex2!=parent[vertex] and LOW[vertex2]<LOW[vertex]:

                LOW[vertex]=LOW[vertex2]
        if flag==0 and parent[vertex]!=None:
            Bridges.append((vertex,parent[vertex]))
    
    for i in range(n):
        low(G,i)


        
    return Bridges if len(Bridges)!=0 else None
    
    

    
T=[[1,2],[0,2],[0,1,3],[2,4,5],[3,5],[3,4],[7],[6]]
T=[[1],[2],[3],[]]
print(Mosty(T))
