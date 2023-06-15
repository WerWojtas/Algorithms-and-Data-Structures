def DFS(G):     # Algorytm DFS przeszukiwanie w głąb. Algorytm idzie tak długo aż będzie to możliwe po kolejnych sąsiadach kolejnych
    n=len(G)    # wierzchołków (rekurencja). Depth First Search Algorithm.
    def DFS_Visit(G,u):
        nonlocal time
        visited[u]=True
        time_array[u]=time
        time+=1
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                parent[v]=u
             
                DFS_Visit(G,v)
        

    time=0
    time_array=[-1 for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[False for _ in range(n)]


    for i in range(n):

        if visited[i]==False:
            DFS_Visit(G,i)
    print(time_array)
    print(parent)


def TOP(G,n):     # Algorytm sortowania topologicznego grafu acyklicznego skierowanego. Algorytm używa DFS, gdy wierzchołek zostanie
    n=len(G)      # "przetworzony" ( nie da się z niego już nigdzie przejść) dopisuje go na koniec listy sortowania. 
    def DFS_Visit(G,u):   # Algorytm można używać przy sortowaniu zadań które muszą zostać wykonane przed innymi lub do szukania
        nonlocal place,time # ścieżki Hamiltona w grafie skierowanym. Directed Acyclic Graph sorting algorithm.
        visited[u]=True
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                parent[v]=u
             
                DFS_Visit(G,v)
        time+=1
        time_array[u]=time
        sorted[place]=u
        place-=1


    time=0
    time_array=[0 for _ in range(n)]
    sorted=[0 for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[False for _ in range(n)]
    place=n-1


    for i in range(n):

        if visited[i]==False:
            DFS_Visit(G,i)
    print(sorted)
    print(time_array)
    print(parent)


def Euler(G,u):
    if is_euler==False:
        return None  
    n=len(G)
    PATH=[]
    Guardian=[0 for _ in range(n)]
    def DFS_Visit(G,vertex1,vertex2):
        if len(G[vertex2])>Guardian[vertex2]:
            swap(G[vertex2][Guardian[vertex2]],G[vertex2][(Guardian[vertex2]+1)])
            Guardian[vertex2]+=1
            Guardian[vertex1]+=1
            DFS_Visit(G,vertex2,G[vertex2][Guardian[vertex2]])

        PATH.append(vertex2)
        swap(G[vertex1][Guardian[vertex1]],G[vertex1][(Guardian[vertex1]+1)])
        Guardian[vertex1]+=1
        





def is_euler(G):
    n=len(G)
    for i in range(n):
        if len(G[i])%2!=0:
            return False
    return True

def swap(x,y):
    a=x
    x=y
    y=a



G=[[1,2],[2,4],[],[],[3,6],[],[4]]
T=[[1,3],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
H=[[1,2],[0,2,3,4],[0,1,3,5],[1,2,4,5],[1,3,5,6],[2,3,4,7],[4,7],[5,6]]

#print(Euler(H,0))

#TOP(G,7)
DFS(T)


    
