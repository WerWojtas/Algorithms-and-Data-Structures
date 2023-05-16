"""Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
1
samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego."""



def DFS(G,start,end):     
    n=len(G)
    def DFS_Visit(G,u):
        nonlocal end
        for i in range(len(G[u])):
            v=G[u][i]
            vertex=v[0]
            cost=v[1]
            print(u,vertex,cost)
            print(PAYMENT)
            if PAYMENT[vertex]>PAYMENT[u]+cost:
                PAYMENT[vertex]=PAYMENT[u]+cost
                DFS_Visit(G,vertex)
  
    PAYMENT=[10**10 for _ in range(n)]

    PAYMENT[start]=0


    DFS_Visit(G,start)
    print(PAYMENT)
    return PAYMENT[end]

T=[[(1,0)],
   [(0,0),(2,1),(5,0)],
   [(1,1),(3,1)],
   [(2,1),(4,1)],
   [(3,1),(7,1),(8,1),(9,0)],
   [(1,0),(6,0)],
   [(5,0),(7,0)],
   [(6,0),(4,1)],
   [(4,1),(10,1)],
   [(4,0),(10,0)],
   [(9,0),(8,1)]]

DFS(T,0,10)



    
