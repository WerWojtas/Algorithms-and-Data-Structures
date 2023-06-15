from queue import PriorityQueue

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
        return None
    if x.rank>y.rank:
        y.parent=x
        return x.value
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
    return y.value

def Kruskal(G,n):
    MST=[None for _ in range(n)]
    EDGES=[]
    sum=0
    Q=PriorityQueue()

    for vertex1 in range(n):
        for j in range(len(G[vertex1])):
            vertex2=G[vertex1][j][0]
            if vertex1<vertex2:
          
                Q.put((G[vertex1][j][1],vertex1,vertex2))

    verticle_nodes=[Node(i) for i in range(n) ]

    while not Q.empty():
        wage,vertex1,vertex2=Q.get()
  
        node1=verticle_nodes[vertex1]
        node2=verticle_nodes[vertex2]
      
        add=union(node1,node2)
        if add!=None:
            sum+=wage
            EDGES.append((vertex1,vertex2))
          
    print(EDGES)
    print(sum)
