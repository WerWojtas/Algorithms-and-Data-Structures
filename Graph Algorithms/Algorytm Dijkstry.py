from queue import PriorityQueue

def Dijkstra(G,start,n):            # <-----------------Algorytm Dijkstry, służy do znalezienia najkrótszej ścieżki w grafie ważonym
    d=[(10**10) for i in range(n)]  # przy nieujemnych wagach. Wsadzamy wierzchołek startowy do kolejki priorytetowej, patrzymy na wszystkich jego
    s=[False for _ in range(n)]     # sąsiadów, jeśli ścieżką z wierzchołka rozpatrywanego + cost możemy dojść krócej niż aktualnie
    Q=PriorityQueue()               # ustawioną ścieżką zmieniamy dystans na wierzch. rozpatrywany + cost. Jeśli możemy zmniejszyć
    d[start]=0                      # dystans do sąsiada i sąsiad jeszcze nie został rozpatrzony wkładamy go do kolejki razem z 
    Q.put((d[start],start))         # dystansem. W każdej iteracji PriorityQueue wybierze wierzchołek o najkrótszym aktualnym dystansie
                      # wierzchołek który wyciągamy z kolejki po przeglądnięciu wszystkich sąsiadów zostaje przetworzony
    while not Q.empty():
        dist,v=Q.get()
        for j in range(len(G[v])):
            neighbour=G[v][j][0]
            cost=G[v][j][1]
            if s[neighbour]==False and d[neighbour]>dist+cost:
                d[neighbour]=dist+cost
                Q.put((d[neighbour],neighbour))
        s[v]=True
    
    return d







