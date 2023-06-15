"""Kapitan pewnego statku zastanawia
się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
(n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
(to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
rozwiązującą problem kapitana.
"""


def Grafy(M,d):            # Wykorzystanie algorytmu DFS. Wchodzimy na pole tylko jeśli jest to możliwe (jeśli jeszcze na nim nie
    n=len(M)               # byliśmy i poziom wody jest odpowiedni).
    m=len(M[0])
    ŚCIEŻKI=[(1,0),(0,1),(-1,0),(0,-1)]
    def DFS_Visit(G,vertex):
        nonlocal d
        for i,j in ŚCIEŻKI:
            x=vertex[0]+i
            y=vertex[1]+j
            if x>=0 and j>=0 and x<n and y<m and G[x][y]>d and VISITED[x][y]==False:
                neighbour=(x,y)
                if neighbour==(n-1,m-1):
                    PARENT[n-1][m-1]=vertex
                    VISITED[x][y]=True
                    return
                else:
                    PARENT[x][y]=vertex
                    VISITED[x][y]=True
                    DFS_Visit(G,neighbour)
    
    VISITED=[[False for _ in range(m)] for _ in range(n)]
    PARENT=[[None for _ in range(m)] for _ in range(n)]          
    start=(0,0)
    VISITED[0][0]=True
    DFS_Visit(start)
    return True if VISITED[n-1][m-1]==True else False


