"""Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
{1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.
"""

def DFS(G,start,end):     
    n=len(G)
    flag=0
    def DFS_Visit(G,u):
        nonlocal end,flag
        for i in range(len(G[u])):
            print(COST,u)
            edge=G[u][i]
            vertex=edge[0]
            cost=edge[1]
            if COST[u]>cost:
                if vertex==end:
                    flag=1
                    parent[end]=u
                    return True
                COST[vertex]=cost
                parent[vertex]=u
                DFS_Visit(G,vertex)
        

    parent=[None for _ in range(n)]
    COST=[10**10 for _ in range(n)]


    DFS_Visit(G,start)

    if flag==1:
        PATH=[]
        x=end
        while x!=start:
            PATH.append(x)
            x=parent[x]
        PATH.append(start)
        PATH=PATH[::-1]
        print(PATH)
        return True
    return False


T=[[(1,5)],
   [(0,5),(2,8),(3,4)],
   [(1,8)],
   [(1,4),(5,3)],
   [(6,7)],
   [(3,3)],
   [(4,7),(8,0)],
   [(8,1)],
   [(7,1),(6,0)]]

print(DFS(T,0,6))