"""Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza."""



def Szachownica(G):    
    n=len(G)    
    def DFS_Visit(G,vertex):
        for i,j in ŚCIEŻKI:
            if i+vertex[0]>=0 and i+vertex[0]<n and j+vertex[1]>=0 and j+vertex[1]<n:
                vertex_next=(i+vertex[0],j+vertex[1])
                if COST[vertex_next[0]][vertex_next[1]]>COST[vertex[0]][vertex[1]]+G[vertex_next[0]][vertex_next[1]]:
                    if vertex_next==(n-1,n-1):
                        COST[vertex_next[0]][vertex_next[1]]=COST[vertex[0]][vertex[1]]+G[vertex_next[0]][vertex_next[1]]
                        parent[vertex_next[0]][vertex_next[1]]=vertex
                    else:

                        COST[vertex_next[0]][vertex_next[1]]=COST[vertex[0]][vertex[1]]+G[vertex_next[0]][vertex_next[1]]
                        parent[vertex_next[0]][vertex_next[1]]=vertex
                        DFS_Visit(G,vertex_next)



        
            
        
    
    ŚCIEŻKI=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    parent=[[None for _ in range(n)] for _ in range(n)]
    COST=[[10**10 for _ in range(n)] for _ in range(n)]
    COST[0][0]=0


    DFS_Visit(G,(0,0))
    x=(n-1,n-1)
    PATH=[]
    while x!=(0,0):
        PATH.append(x)
        x=parent[x[0]][x[1]]
    PATH=PATH[::-1]
    print(COST)
    print(PATH)



T=[[0,2,3,4],
       [5,1,7,8],
       [0,4,8,2],
       [1,1,2,4]]
    
Szachownica(T)

# Rozwiązanie polega na wykorzystaniu idei algorytmu DFS dla tablicy. Tworzę tablicę krotek z możliwymi przejściami króla, 
# wykonuję algorytm dfs dla Tablicy dwuwymiarowej(bez visited). Na kolejne pole przechodzę tylko wtedy jeśli mogę zmniejszyć
# wartość w tablicy koszt dla tego pola. Po wykonaniu algorytmu dla pola end będziemy mieć jak najmniejszy koszt.