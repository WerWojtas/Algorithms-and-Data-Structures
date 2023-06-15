from queue import PriorityQueue

def Prim(G,start,n):                    # Kopia algorytmu Dijkstry tylko zamiast dodawania kosztu po prostu przeglądamy wagi 
    WAGA=[10**10 for i in range(n)]  
    VISITED=[False for _ in range(n)]    
    PARENT=[None for _ in range(n)]
    Q=PriorityQueue()              
    WAGA[start]=0                     
    Q.put((WAGA[start],start))    
    TREE=[None for _ in range(n)]
    sum=-1
                      
    while not Q.empty():
        _,v=Q.get()
        sum+=1
        print(v)
        if VISITED[v]==False:
            for j in range(len(G[v])):
                neighbour=G[v][j][0]
                waga=G[v][j][1]
                if VISITED[neighbour]==False and waga<WAGA[neighbour]:
                    WAGA[neighbour]=waga
                    PARENT[neighbour]=v
                    Q.put((WAGA[neighbour],neighbour))
            TREE[v]=PARENT[v]
            VISITED[v]=True
    
    return TREE
