"""Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
wychodząca z t.
1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n
2
)).
2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej."""

def ujście_On2(GRAPH):     # Szukanie ujścia Złożoność O(n^2)
    n=len(GRAPH)
    for i in range(n):
        flag=0
        for j in range(n):
            if GRAPH[i][j]==True:
                flag=1
                break
        if flag==0:
            vertex=i
            break

    for i in range(n):
        if i==vertex:
            continue
        elif GRAPH[i][vertex]==False:
            return None
    return vertex

def ujście_On(GRAPH):   # Metoda "wężyka" - kiedyś trafimy na wiersz z samymi zerami. Złożoność O(n) - najgorsza O(2n)
    n=len(GRAPH)
    point1=0
    point2=0
    while point2!=n-1:
        if T[point1][point2+1]==0:
            point2+=1
        elif T[point1+1][point2]==0:
            point1+=1
        else:
            return None
    return point1


T=[[0,0,0,1,0,0,0,0],
   [0,0,0,1,0,0,0,0],
   [0,0,0,1,0,0,0,0],
   [0,0,0,0,0,0,0,0],
   [0,0,0,1,0,0,0,0],
   [0,0,0,1,0,0,0,0],
   [0,0,0,1,0,0,0,0],
   [0,0,0,1,0,0,0,0]]

print(ujście_On(T))