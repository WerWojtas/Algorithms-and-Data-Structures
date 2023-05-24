"""Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
malejących wagach (jeśli ścieżki nie ma to zwracamy ∞)."""


def malejące(G,start,end):
    n=len(G)
    LOW=[10**10 for _ in range(n)]
    LOW[start]=0

    def DFS_Visit(G,vertex,cost_before):
        nonlocal end
        for i in range(len(G[vertex])):
            edge=G[vertex][i]
            neighbour=edge[0]
            cost=edge[1]
            if LOW[vertex]+cost<LOW[neighbour] and cost_before>cost:
                if neighbour==end:
                    LOW[end]=LOW[vertex]+cost
                else:
                    LOW[neighbour]=LOW[vertex]+cost
                    DFS_Visit(G,neighbour,cost)
                    
    DFS_Visit(G,start,10**10)

    print(LOW[end])


T=[[(1,15),(2,5)],
   [(0,5),(3,20),(4,13)],
   [(0,30),(6,7)],
   [(1,20),(4,4)],
   [(1,13),(3,4),(5,40)],
   [(4,40),(6,2)],
   [(2,7),(5,2),(7,1)],
   [6,1]]

malejące(T,0,7)