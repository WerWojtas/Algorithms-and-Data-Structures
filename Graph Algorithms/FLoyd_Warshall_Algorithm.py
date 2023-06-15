# Algorytm wykonujemy dla Grafu o reprezentacji macierzowej złożoność O(n^3). Szuka najkrótszych ścieżek między wszystkimi wierzchołkami
# dla grafów gęstych najoptymalniejsze rozwiązanie


def Floyd_Warshall(M):
    n=len(M)
    PARENT=[[None for _ in range(n)] for _ in range(n)]  # Na początku tworzymy tablicę PATHS z wagami i PARENT z rodzicami
    PATHS=[[10**10 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
      
            if M[x][y]!=None:
                PARENT[x][y]=x
                PATHS[x][y]=M[x][y]

    print(PARENT)
    print(PATHS)

    for t in range(n):        # Algortym wykonuje n razy operacje zamiany macierzy, jeśli odległość między wierzchołkami x,y jest dłuższa
        for x in range(n):    # niż odległość między x -> t -> y to zamieniamy odległość na powyższą, oraz rodzica
            for y in range(n):
                if PATHS[x][y]>PATHS[x][t]+PATHS[t][y]:
                    PATHS[x][y]=PATHS[x][t]+PATHS[t][y]
                    PARENT[x][y]=PARENT[t][y]

    x=4
    PATH=[]
    while x!=1:           # tak możemy odtworzyć ścieżkę (tu z 1 do 4)
        PATH.append(x)
        x=PARENT[1][x]

    PATH=PATH[::-1]
    print(PATH)



T=[[None,2,1,1,None,None],
 [2,None,3,None,None,5],
 [1,3,None,None,4,None],
 [1,None,None,None,2,None],
 [None,None,4,2,None,None],
 [None,5,None,None,None,None]]

Floyd_Warshall(T)
