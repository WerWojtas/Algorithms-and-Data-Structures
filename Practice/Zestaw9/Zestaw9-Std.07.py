from queue import PriorityQueue

"""Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu"""

def podróżnik(G,COST,start,end,bak):            
    n=len(G)                                   
    T=[[[] for _ in range(bak+1)] for _ in range(n)]  
    for vertex in range(n):                           
        for j in range(len(G[vertex])):               
            miasto=G[vertex][j][0]             
            kilometry=G[vertex][j][1]           
            for quantity in range(bak+1):      
                if kilometry<=quantity:         
                    T[vertex][quantity].append((miasto,quantity-kilometry,0))
    for vertex in range(n-1):
        for quantity in range(bak+1):
            for quantity2 in range(quantity+1,bak+1):
                T[vertex][quantity].append((vertex,quantity2,(quantity2-quantity)*COST[vertex]))
    print(T)
    x=Dijkstra(T,n+1,bak,end,start)
    print(x)
                
def Dijkstra(G,n,bak,end,start):            # <-----------------Algorytm 
    d=[[10**10 for _ in range(bak+1)] for _ in range(n)]
    s=[[False for _ in range(bak+1)] for _ in range(n)]
    Q=PriorityQueue()
    d[start][0]=0
    Q.put((d[start][0],(start,0)))
    while not Q.empty():
        dist,vertex=Q.get()
        miasto=vertex[0]
        opcja=vertex[1]
        print(miasto,opcja)
        for i in range(len(G[miasto][opcja])):
            neighbour=G[miasto][opcja][i]
            miasto1=neighbour[0]
            opcja1=neighbour[1]
            cost=neighbour[2]
            if s[miasto1][opcja1]==False and d[miasto1][opcja1]>dist+cost:
                d[miasto1][opcja1]=dist+cost
                Q.put((d[miasto1][opcja1],(miasto1,opcja1)))
        s[miasto][opcja]=True
    return d[end][0]


x = [[(1,2), (2,1)],
     [(2,1), (0,2)],
     [(3,2), (0,1), (1,2)],
     [(2,2)]]
p = [1,100,100,100]


podróżnik(x,p,0,3,100)

"""Algorytm Dijkstry z "rozmnożonymi" wierzchołkami. Każdy wierzchołek rozdzielamy na tyle podwierzchołków jaki może być stan 
kanistra. Indeksy pierwszej podtablicy T wskazują na nr wierzchołka z którego rozmnażaliśmy, indeksy drugiej podtablicy stan baku
z jakim zamierzamy opuścić wierzchołek (np stan baku 4 litry w mieście - wierzchołku o nr 3 będzie opisany jako T[3][4]. Następnie
do każdego podwierzchołka dodajemy krawędzie na zasadzie - przeglądamy wszystkie krawędzie wierzchołka matki, jeśli
quantity (ilość paliwa w baku) pozwala nam na przejechanie do miasta sąsiada robimy połączenie z odpowiednim wierzchołkiem w mieście
sąsiedzie. Np z miasta 1 istnieją 2 drogi do miasta 2 z kosztem 3 i miasta 3 z kosztem 1, zatem wierzchołka oznaczającego bak
0 nie łączymy z niczym, wierzchołek pierwszy miasta 1 łączymy z wierzchołkiem zerowym miasta 3, wierzchołek 2 z wierzchołkiem
zerowym miasta 2 i pierwszym miasta 3 itd. Koszt takich połączeń ustawiam na 0. Następnie dodaje krawędzie między wierzchołkami
w miastach. Z wierzchołków o mniejszej wartości baku da się przeskoczyć do każdego o większej, koszt takiego połączenia to koszt
tankowania baku (czyli wartość oczekiwana-wartość akutalna)*koszt tankowania w danym mieście. Na tak przygotowanym grafie odpalam
algorytm Dijkstry zaczynając od startowego wierzchołka i 0 wartości baku (są połączenia do każdej innej wartości baku z kosztem)
Algorytm Dijkstry wcześniej przekształciłam aby pasował do macierzy sześciennej. Zwracam tablicę koszt dojazdu do miasta końca przy
pustym baku(wtedy jest to najbardziej optymalne)"""
