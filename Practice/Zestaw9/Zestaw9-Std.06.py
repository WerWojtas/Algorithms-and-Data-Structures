"""Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
poprawny)."""

from queue import PriorityQueue
from copy import deepcopy


def Autobusy(G,start,end):   # Algorytm Dijkstry z małą zmianą, jeśli Alicja jedzie pierwsza to liczymy co drugi koszt zaczynając od
    n=len(G)                # pierwszej trasy, jeśli Ben to samo ale zaczynając od drugiej
    for i in range(n):
        G.append([])
        for j in range(len(G[i])):
            G[i+n].append((G[i][j][0],0))
    print(G)
            

    
    """Alice,parent1=Dijkstra(G,start,n,1)
    Ben,parent2=Dijkstra(G,start,n,0)
    if Alice[end]<Ben[end]:
        pointer=end
        PATH=[]
        while pointer!=start:
            PATH.append(pointer)
            pointer=parent1[pointer]
        PATH=PATH[::-1]
        return "Alice", PATH

    else:
        pointer=end
        PATH=[]
        while pointer!=start:
            PATH.append(pointer)
            pointer=parent2[pointer]
        PATH=PATH[::-1]
        return "Ben",PATH"""

    





def Dijkstra(G,start,n,case):            # <-----------------Algorytm
    d=[(10**10) for i in range(n)]
    s=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    Q=PriorityQueue()
    d[start]=0
    Q.put((d[start],start))
    if case==1:
        flag=0
    else:
        flag=1
    while not Q.empty():
        dist,v=Q.get()
        flag+=1
        for j in range(len(G[v])):
            neighbour=G[v][j][0]
            if flag%2==0:
                cost=0
            else:
                cost=G[v][j][1]
            if s[neighbour]==False and d[neighbour]>dist+cost:
                d[neighbour]=dist+cost
                parent[neighbour]=v
                Q.put((d[neighbour],neighbour))
        s[v]=True
    return d,parent

def Dijkstra(G,start,n,case):            # <-----------------Algorytm
    d=[(10**10) for i in range(n)]
    s=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    Q=PriorityQueue()
    d[start]=0
    Q.put((d[start],start))
    if case==1:
        flag=0
    else:
        flag=1
    while not Q.empty():
        dist,v=Q.get()
        flag+=1
        for j in range(len(G[v])):
            neighbour=G[v][j][0]
            if flag%2==0:
                cost=0
            else:
                cost=G[v][j][1]
            if s[neighbour]==False and d[neighbour]>dist+cost:
                d[neighbour]=dist+cost
                parent[neighbour]=v
                Q.put((d[neighbour],neighbour))
        s[v]=True
    return d,parent

T=[[(1,5),(4,2)],
   [(0,5),(2,20)],
   [(1,20),(3,3)],
   [(2,3),(6,9),(7,4)],
   [(0,2),(5,4)],
   [(4,4),(6,6)],
   [(5,6),(3,9)],
   [(3,4)]] 

print(Autobusy(T,0,7))