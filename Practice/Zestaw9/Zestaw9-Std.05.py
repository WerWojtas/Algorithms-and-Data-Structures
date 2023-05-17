"""Przewodnik chce przewieźć grupę K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów.
Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
dostali się z A do B."""

from collections import deque

def przewoźnik(G,start,end):
    n=len(G)
    def DFS_Visit(G,vertex):
        for i in range(len(G[vertex])):
            edge=G[vertex][i]
            vertex2=edge[0]
            cost=edge[1]
            low_path=min(LOW[vertex],cost)
            if LOW[vertex2]<low_path and vertex2!=PARENT[vertex]:
                if vertex2==end:
                    LOW[end]=low_path
                    PARENT[end]=vertex
                else:
                    LOW[vertex2]=low_path
                    PARENT[vertex2]=vertex
                    DFS_Visit(G,vertex2)
                
                

        

    PARENT=[False for _ in range(n)]
    LOW=[-1 for _ in range(n)]
    LOW[start]=10**10


    DFS_Visit(G,start)
    print(LOW[end])


T=[[(1,5),(4,2)],
   [(0,5),(2,1)],
   [(1,1),(3,3)],
   [(2,3),(6,9),(7,4)],
   [(0,2),(5,4)],
   [(4,4),(6,6)],
   [(5,6),(3,9)],
   [(3,4)]]

przewoźnik(T,0,7)
