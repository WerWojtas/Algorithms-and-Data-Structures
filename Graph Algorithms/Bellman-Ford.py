def Bellman_Ford(G,start):    # Algorytm znajdowania najkrótszej ścieżki w grafie skierowanym ważonym z wagami ujemnymi.
    n=len(G)                  # Złożoność O(VE) - wykonujemy V-1 iteracji dla każdej krawędzi znajdując najkrótszą ścieżkę
    distance=[10**10 for _ in range(n)] # Wykonujemy V-1 iteracji w których dla każdego wierzchołka "relaksujemy go"->jeśli
    parent=[None for _ in range(n)]     # możemy zmniejszyć dystans do niego to zmiejszamy ten dystans
    distance[start]=0                   # po wykonaniu wszystkich iteracji drogi do każdego wierzchołka powinny być jak najkrótsze.
    for i in range(1,n):                # Optymalizacja: jeśli algorytm w danej iteracji nie zmieni nic w tablicy znaczy, że nie ma
        flag=0                          # już nic do zmiany i można go przerwać. Po zakończeniu relaksacji sprawdzamy czy graf ma cykl
        for vertex1 in range(n):        # ujemny - > jeszcze raz staramy się zmniejszyć dystans do krawędzi, jeśli to możliwe to graf
            for j in range(len(G[vertex1])): # ma cykl ujemny i ścieżka taka jest niemożliwa (zamkniemy się w cykly).
                edge=G[vertex1][j]
                vertex2=edge[0]
                if distance[vertex2]>distance[vertex1]+edge[1]:
                    distance[vertex2]=distance[vertex1]+edge[1]
                    parent[vertex2]=vertex1
                    flag=1
        if flag==0:
            break
                
    
    for vertex1 in range(n):
        for j in range(len(G[vertex1])):
            edge=G[vertex1][j]
            vertex2=edge[0]
            if distance[vertex2]>distance[vertex1]+edge[1]:
                return "Graf ma cykl ujemny"
    return distance
                
T=[[(1,1),(2,4)],[(2,-2)],[(3,2)],[(4,-3),(8,8)],[(5,4)],[(6,-2)],[(7,1)],[],[(7,1)]]
print(Bellman_Ford(T,0))

