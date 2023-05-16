"""Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
graf reprezentowany jest przez macierz sasiedztwa A."""

from collections import deque

def Cycle4(GRAPH):
    n=len(GRAPH)
    LIST=[[] for _ in range(n)]
    NEIGHBOURS=[[None for _ in range(n)]for _ in range(n)]
    for vertex in range(n):
        for j in range(n):
            if GRAPH[vertex][j]==True:
                LIST[vertex].append(j)

    print(LIST)
    for vertex in range(n):
        for i in range(len(LIST[vertex])):
            neighbour1=LIST[vertex][i]
            for j in range(i+1,len(LIST[vertex])):
                neighbour2=LIST[vertex][j]
                if NEIGHBOURS[neighbour1][neighbour2]!=None:
                    return (neighbour1,vertex,neighbour2,NEIGHBOURS[neighbour1][neighbour2])
                else:
                    NEIGHBOURS[neighbour1][neighbour2]=vertex
                    print(i,j,vertex)
    


    



T=[[False,True,False,False,False,False,False],
   [True,False,True,True,False,False,False],
   [False,True,False,False,True,True,False],
   [False,True,False,False,True,False,False],
   [False,False,True,True,False,False,False],
   [False,False,True,False,False,False,True],
   [False,False,False,False,False,True,False]]

print(Cycle4(T))
    