def spacetravel( n, E, S, a, b ):

    Planets=[[] for _ in range(n)]
    road=len(E)
    for i in range(road):
        v=E[i][0]
        u=E[i][1]
        cost=E[i][2]
        Planets[v].append((u,cost))
        Planets[u].append((v,cost))
    how_many_stars=len(S)
    star=S[0]
    for i in range(1,how_many_stars):
        Planets[star].append((S[i],0))
        Planets[S[i]].append((star,0))
        
    distance=Dijkstra(Planets,a,b,len(Planets))
    return distance if distance!= 10**10 else None
            
    

def Dijkstra(G,start,end,n):
    DISTANCE=[10**10 for _ in range(n)]
    VISITED=[False for _ in range(n)]
    DISTANCE[start]=0
    Q=[(DISTANCE[start],start)]
    heapq.heapify(Q)
    while len(Q)!=0:
        distance,vertex=heapq.heappop(Q)
        for i in range(len(G[vertex])):
            neighbour,cost=G[vertex][i]
            if VISITED[neighbour]==False and DISTANCE[neighbour]>distance+cost:
                DISTANCE[neighbour]=distance+cost
                heapq.heappush(Q,(DISTANCE[neighbour],neighbour))
        VISITED[vertex]=True

    return DISTANCE[end]

  """Algorytm wyszukuje najkrótszej ścieżki za pomocą algorytmu Dijkstry. Na początku algorytm zamienia dane na listę krawędzi,
następnie dodaje krawędzie o koszcie zero między planetami leżącymi blisko osobliwości (łączy jedną planetę ze wszystkimi innymi
aby graf utworzony z tych planet był spójny). Najkrótsza ścieżka jest znajdowana za pomocą algorytmu Dijkstry i zwracana. """
