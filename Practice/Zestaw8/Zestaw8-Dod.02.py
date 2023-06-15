"""Proszę podać algorytm, który mając na wejściu graf G reprezentowany
przez listy sąsiedztwa sprawdza, czy jest nieskierowany (czyli czy dla każdej krawędzie u → v istnieje także
krawędź przeciwna)"""

def nieskierowany(G):     # Tworzymy macierz krawędzi, jeśli w macierzy pojawia się krawędź wsteczna (prow)
    n=len(G)
    T=[[False for _ in range(n)] for _ in range(n)]
    flag1=0
    flag2=0
    for vertex in range(n):
        print(vertex,G[vertex])
        for j in range(len(G[vertex])):
            flag1+=1
            vertex2=G[vertex][j]
            T[vertex][vertex2]=True
            if T[vertex2][vertex]==True:
                flag2+=1
    return True if flag2==flag1/2 else False

H=[[1,2],[0,2,3,4],[0,1,3,5],[1,2,4,5],[1,3,5,6],[2,3,4,7],[4,7],[5,6]]
print(nieskierowany(H))
            