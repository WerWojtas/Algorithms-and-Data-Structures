"""Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
podający kolejność wyłączania stacji."""

def PHONE(G):     # Używamy algorytmu DFS i wyłączamy wierzchołki przetworzone
    n=len(G)
    def DFS_Visit(G,u):
        visited[u]=True
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                parent[v]=u
             
                DFS_Visit(G,v)
        PATH.append(u)
        
    PATH=[]
    visited=[False for _ in range(n)]
    parent=[False for _ in range(n)]


    u=G[0][0]
    DFS_Visit(G,u)
    print(PATH)

H=[[1,2],[0,2,3,4],[0,1,3,5],[1,2,4,5],[1,3,5,6],[2,3,4,7],[4,7],[5,6]]
PHONE(H)
    
