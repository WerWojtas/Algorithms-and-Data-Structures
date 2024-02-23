"""Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową."""


def DFS(G,start,end,t):     # Rozwiązanie w którym nie dostajemy pułapu samolotu, pułap wyznaczany jest jako przedział możliwych pułapów
    n=len(G)                # przy każdej krawędzi wychodzącej ze start. Wykorzystuje algorytm DFS bez tablicy visited, wchodzę do
    PATH=[]                 # wierzchołków tylko jeśli pułap na to pozwala - jako kolejny pułap biorę część wspólną pułapu wejściowego
    def DFS_Visit(G,u,height_start,dist):     # i wyjściowego. Jeśli algorytm znajdzie wierzchołek końcowy przelot jest możliwy
        nonlocal end,height_end,flag,dista
        if flag==1:
            return True
        for i in range(len(G[u])):
            edge=G[u][i]
            vertex=edge[0]
            cost=edge[1]
            height=(cost-t,cost+t)
            if ((height_start[0]<=height[0] and height[0]<height_start[1]) or (height[0]<=height_start[0] and height_start[0]<height[1])) and vertex!=parent[u]:
                x=max(height_start[0],height[0])
                y=min(height_start[1],height[1])
                height_next=(x,y)
                parent[vertex]=u
                dist+=1
                print(height_next,vertex)
                if vertex==end:
                    x=end
                    height_end=height_next
                    flag=1
                    dista=dist
                    return
                else:


             
                    DFS_Visit(G,vertex,height_next,dist)



    parent=[None for _ in range(n)]
    distance=1
    flag=0
    height_end=0
    dista=0


    for i in range(len(G[start])):
        edge_start=G[start][i]
        vertex_start=edge_start[0]
        cost_start=edge_start[1]
        height_start=(cost_start-t,cost_start+t)
        if DFS_Visit(G,vertex_start,height_start,distance)==True:
            a=end
            for i in range(dista-2):
                PATH.append(a)
                a=parent[a]
                PATH=PATH[::-1]
            return height_end,PATH
            



T=[[(1,7),(3,4),(5,5)],
   [(0,7),(2,9),(7,30)],
   [(1,9)],
   [(0,4),(4,22)],
   [(3,22),(5,9)],
   [(0,5),(4,9),(7,3),(6,12)],
   [(5,12),(8,6)],
   [(1,30),(5,3),(8,7)],
   [(7,7),(6,6)]]

print(DFS(T,0,2,3))
