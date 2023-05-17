"""Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
grafie skierowanym.
"""

def TOP(G):
    n=len(G)
    def DFS_Visit(G,vertex):
        VISITED[vertex]=True
        for i in range(len(G[vertex])):
            vertex2=G[vertex][i]
            if VISITED[vertex2]==False:
                DFS_Visit(G,vertex2)
        
        SORTED.append(vertex)

    VISITED=[False for _ in range(n)]
    SORTED=[]

    for i in range(n):
        if VISITED[i]==False:
            DFS_Visit(G,i)
    
    SORTED=SORTED[::-1]
    for i in range(n-1):
        if SORTED[i+1] not in G[SORTED[i]]:   # tak też można
            return False
    return True

    
