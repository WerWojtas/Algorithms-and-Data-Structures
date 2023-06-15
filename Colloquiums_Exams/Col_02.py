def beautree(G):
    n=len(G)
    EDGES=make_edges(G)
    leng=len(EDGES)
  
 
    EDGES.sort()

   

    for i in range(leng):
        if leng-i<n:
            return None
        sum=Kruskal(EDGES,n,i,leng)
        if sum!=-1:
            return sum
        
    return None

class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value

def find_root(x):
    if x.parent!=x:
        x=find_root(x.parent)
    return x.parent

def union(x,y):
    x=find_root(x)
    y=find_root(y)
    if x==y:
        return False
    if x.rank>y.rank:
        y.parent=x
        return True
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
    return True

def Kruskal(Q,n,x,leng):


    sum=0
    verticles=0
 
    verticle_nodes=[Node(i) for i in range(n)]
    for i in range(x,leng):
        if verticles==n-1:
            return sum
     
    
        wage,vertex1,vertex2=Q[i]
   
        if union(verticle_nodes[vertex1],verticle_nodes[vertex2])==False:
            return -1
        sum+=wage
        verticles+=1




def make_edges(G):
    n=len(G)
    EDGES=[]
    for vertex1 in range(n):
        for j in range(len(G[vertex1])):
            vertex2=G[vertex1][j][0]
            if vertex1<vertex2:
                EDGES.append((G[vertex1][j][1],vertex1,vertex2))
            
    return EDGES
  
  """Na początku algorytm zamienia reprezentacje grafu na listę krawędzi za pomocą funkcji make_edges. Następnie sortuje on tablicę
z uwzględnieniem wag krawędzi. W pętli for wykonuje algorytm Kruskala zaczynając od najmniejszej wagi. Jeśli algorytm kruskala nie 
zostanie przerwany do momentu znalezienia n-1 krawędzi (n to liczba wierzchołków) to znaczy, że znajazł on najlżejsze piękne
drzewo, ponieważ wszystkie mniejsze krawędzie nie były rozpatrywane przez algorytm Kruskala, a wszystkie większe są poza nim.
(Algorytm na swojej drodze nie pominął żadnej krawędzi). Jeśli jednak algorytm Kruskala zostanie przerwany wykonuje się on kolejny
raz, ale od następnej krawędzi w kolei. Złożoność algorytmu to O(VElogE)."""
