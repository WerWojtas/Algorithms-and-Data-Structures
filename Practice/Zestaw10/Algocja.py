"""Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami.
Każde miasto jest otoczone murem i ma tylko dwie bramy—północną i południową. Z każdej bramy prowadzi
dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też
być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicji
Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić algorytm, który
stwierdza czy odpowiednia trasa gońca istnieje"""

def Algocja(G,CITIES):
    n=len(G)
    M_COUNT=[0 for _ in range(n)]
    CIT=["O" for _ in range(n)]

    for i in range(len(CITIES)):
        CIT[CITIES[i]]="M"
    m_count=0

    for i in range(n):
        if CIT[i]=="M":
            m_count+=1
        M_COUNT[i]=m_count

    o_quantity=n-len(CITIES)
    o_count=-1
    O_NEIGHBOURS=[[] for _ in range(o_quantity)]
    O=[[] for _ in range(o_quantity)]
    MERGE=[None for _ in range(o_quantity)]
    ADDED=[False for _ in range(n)]
    for i in range(n):
        if CIT[i]=="O":
            o_count+=1
            for j in range(len(G[i])):
                if CIT[G[i][j]]=="O":
                    nr_oazy=G[i][j]-M_COUNT[G[i][j]]
                    O_NEIGHBOURS[o_count].append(nr_oazy)
        else:
            if CIT[G[i][0]]=="O" and CIT[G[i][1]]=="O":
                oaza1=G[i][0]-M_COUNT[G[i][0]]
                oaza2=G[i][1]-M_COUNT[G[i][1]]
                O[oaza1].append(oaza2)
                O[oaza2].append(oaza1)
            elif CIT[G[i][0]]=="M" and CIT[G[i][1]]=="O":
                if ADDED[G[i][0]]==False:
                    count=1
                    oaza=G[i][1]-M_COUNT[G[i][1]]
                    miasto=G[i][0]
                    ADDED[miasto]=True
                    while CIT[miasto]!="O":
                        if G[miasto][0]==i:
                            miasto=G[miasto][1]
                        else:
                            miasto=G[miasto][0]
                        ADDED[miasto]=True
                        count+=1
                    for k in range(count):
                        miasto=miasto-M_COUNT[miasto]
                        O[oaza].append(miasto)
                        O[miasto].append(oaza)


            elif CIT[G[i][0]]=="O" and CIT[G[i][1]]=="M":
                if ADDED[G[i][1]]==False:
                    count=1
                    oaza=G[i][0]-M_COUNT[G[i][0]]
                    miasto=G[i][1]
                    before=i
                    ADDED[miasto]=True
                    while CIT[miasto]!="O":
                        if G[miasto][0]==before:
                            before=miasto
                            miasto=G[miasto][1]
                        else:
                            before=miasto
                            miasto=G[miasto][0]
                        ADDED[miasto]=True
                        count+=1
                    miasto=miasto-M_COUNT[miasto]
                    for k in range(count):
                        O[oaza].append(miasto)
                        O[miasto].append(oaza)


    MERGE=DFS(O_NEIGHBOURS)
    print(O)
    print(MERGE)
    MERGED=[None for _ in range(o_quantity)]
    for i in range(len(MERGE)):
        MERGE[i].sort()
        a=MERGE[i][0]
        leng=len(O[a])
        for j in range(1,len(MERGE[i])):
            b=MERGE[i][j]
            for g in range(len(O[b])):
                O[a].append(O[b][g])
            O[b]=[]
            MERGED[b]=a
    
        NEW_TAB=[]
        ADD_TAB=O[a][leng:]
        print(O)
        for j in range(leng):
                NEW_TAB.append(O[a][j])
        O[a]=NEW_TAB+ADD_TAB

    for i in range(o_quantity):
        for j in range(len(O[i])):
            if MERGED[O[i][j]]!=None:
                O[i][j]=MERGED[O[i][j]]

    print(O)
    for i in range(o_quantity):
        if len(O[i])%2!=0:
            return False
    return True


    

            

def DFS(G):     
    n=len(G)    
    def DFS_Visit(G,u):
        nonlocal spójne
        visited[u]=True
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                MERGE[spójne].append(v)
                DFS_Visit(G,v)
        

    visited=[False for _ in range(n)]
    MERGE=[]
    spójne=-1


    for i in range(n):

        if visited[i]==False and len(G[i])>0:
            MERGE.append([])
            spójne+=1
            MERGE[spójne].append(i)
            DFS_Visit(G,i)
    return MERGE
                


    
    
E = [[1,10], [0,2], [1,3,9,14], [2,8,4], [3,7,5], [4,6], [5,14,7,15], [4,6,14,8], [3,7,14], [2,10,14,12], [0,9,11],
[10,13], [9,14], [11,15], [2,8,7,9,6], [13,6]]
C = [1, 11, 13, 12, 15, 5]

print(Algocja(E,C))
            
            
"""Rozwiązanie polega na przetworzeniu wszystkich miast w krawędzie a następnie połączeniu wszystkich wierzchołków oaz które mają
między sobą krawędzie. Pierwszym krokiem jest utworzenie paru pomocniczych tablic.O to graf połączonych miast. CIT jest tablicą 
mówiącą czy dany wierzchołek
jest miastem czy nie, M_COUNT to tablica zliczająca ile do tej pory miasto wystąpiło (np, że w wierzchołku nr 4 wystąpiły jak dotąd
dwa miasta). Tworzymy też tablicę O_NEIGHBOURS która posłuży nam jako graf połączeń oaz, zliczamy ile mamy oaz i tworzymy tablicę
ADDED. Dzięki niej będziemy rozróżniać czy już dodaliśmy dane miasto czy jeszcze nie w momencie kiedy miasto jest połączone z innym.
Przekształcamy miasta na oazy według algorytmu: jeśli trafiliśmy na oazę przeszukujemy jej sąsiadów i dodajemy ich (tylko inne oazy)
do grafu oaz. Indeks w grafie połączonych miast (czyli wynikowym grafie O oraz grafie oaz O_NEIGHBOURS) poszczególnych sąsiadów odpowiada wzorowi nr oazy sąsiada=nr z jakim oaza matka jest połączona -
- ilość miast jakie wystąpiły do indeksu z jakim matka jest połączona np oaza o indeksie 4 ma 3 sąsiadów, jednym z nich jest oaza
o indeksie 7, aby znaleźć jej indeks w grafie oaz musimy zobaczyć ile miast pojawiło się do indeksa 7, a następnie odejmujemy je od
siódemki. Jeśli trafiliśmy na miasto mamy 3 możliwości - miasto połączone jest z dwoma oazami, wtedy za pomocą powyższego wzoru
określamy ich indeksy i dodajemy połączenie między nimi w grafie wynikowym, miasto może być połączone z jedną oazą i miastem (pozostałe
dwie możliwości). Nie rozpatrujemy przypadku w którym miasto łączy sie z dwoma innymi miastami bo taki przypadek "załatwimy" rozpatrując
dwa poprzednie. Jeśli jednym z sąsiadów miasta jest drugie miasto dodajemy sąsiada do tablicy ADDED(aby drugi raz go nie rozpatrywać)
i "idziemy" po sąsiadach tak długo aż nie trafimy na oazę (pamiętając pierwszą z nich), jednocześnie zwiększamy licznik miast które
minęliśmy. Gdy trafimy na oazę dodajemy do grafu wynikowego tyle połączeń ile mieliśmy miast.

Gdy już stworzymy graf połączonych miast łączymy ze sobą oazy które mają wspólną ścieżkę (bo możemy przechodzić po nich dowolną ilość
razy). Do tego celu wykorzystujemy nasz graf połączonych oaz O_NEIGHBOURS. Używamy na nim DFS i zapisujemy spójne składowe grafu.
Następnie każdą spójną składową sortujemy(zrobiłam to sortem wbudowanym ale równie dobrze można zaimportować strukturę kopca, chodzi o
to aby mieć najmniejszy element). Scalamy wszystkie elementy do najmniejszego. Przechodzimy przez wszystkie spójne składowe i dodajemy
do elementu merge połączenia a następnie "oczyszczamy" oazę którą aktualnie scaliliśmy (czyli po prostu usuwamy z niej wszystkie krawędzie
przypisując jej pustą tablicę). Ostatnim krokiem jest aktualizacja połączeń za pomocą tablicy merge, ale nie jest to wymagane do zadania.
Sprawdzamy czy w powstałym grafie każdy wierzchołek jest parzysty. Jeśli tak cykl Eulera istnieje."""

# 2 wersja zadania bez łączenia wierzchołków oaz. Interesuje nas tylko czy liczba krawędzi w wierzchołkach które powinny zostać połączone
# jest parzysta. Pierwszy krok jest taki sam, w drugim korku odpalamy DFS na grafie oaz i dzielimy go na spójne składowe. Przechodzimy
# po każdej z nich i zliczamy krawędzie należących do nich elementów - jeśli liczba krawędzi w spójnej składowej jest parzysta
# mamy cykl Eulera

def Algocja2(G,CITIES):
    n=len(G)
    M_COUNT=[0 for _ in range(n)]
    CIT=["O" for _ in range(n)]

    for i in range(len(CITIES)):
        CIT[CITIES[i]]="M"
    m_count=0

    for i in range(n):
        if CIT[i]=="M":
            m_count+=1
        M_COUNT[i]=m_count

    o_quantity=n-len(CITIES)
    o_count=-1
    O_NEIGHBOURS=[[] for _ in range(o_quantity)]
    O=[[] for _ in range(o_quantity)]
    MERGE=[None for _ in range(o_quantity)]
    ADDED=[False for _ in range(n)]
    for i in range(n):
        if CIT[i]=="O":
            o_count+=1
            for j in range(len(G[i])):
                if CIT[G[i][j]]=="O":
                    nr_oazy=G[i][j]-M_COUNT[G[i][j]]
                    O_NEIGHBOURS[o_count].append(nr_oazy)
        else:
            if CIT[G[i][0]]=="O" and CIT[G[i][1]]=="O":
                oaza1=G[i][0]-M_COUNT[G[i][0]]
                oaza2=G[i][1]-M_COUNT[G[i][1]]
                O[oaza1].append(oaza2)
                O[oaza2].append(oaza1)
            elif CIT[G[i][0]]=="M" and CIT[G[i][1]]=="O":
                if ADDED[G[i][0]]==False:
                    count=1
                    oaza=G[i][1]-M_COUNT[G[i][1]]
                    miasto=G[i][0]
                    ADDED[miasto]=True
                    while CIT[miasto]!="O":
                        if G[miasto][0]==i:
                            miasto=G[miasto][1]
                        else:
                            miasto=G[miasto][0]
                        ADDED[miasto]=True
                        count+=1
                    for k in range(count):
                        miasto=miasto-M_COUNT[miasto]
                        O[oaza].append(miasto)
                        O[miasto].append(oaza)


            elif CIT[G[i][0]]=="O" and CIT[G[i][1]]=="M":
                if ADDED[G[i][1]]==False:
                    count=1
                    oaza=G[i][0]-M_COUNT[G[i][0]]
                    miasto=G[i][1]
                    before=i
                    ADDED[miasto]=True
                    while CIT[miasto]!="O":
                        if G[miasto][0]==before:
                            before=miasto
                            miasto=G[miasto][1]
                        else:
                            before=miasto
                            miasto=G[miasto][0]
                        ADDED[miasto]=True
                        count+=1
                    miasto=miasto-M_COUNT[miasto]
                    for k in range(count):
                        O[oaza].append(miasto)
                        O[miasto].append(oaza)


    MERGE=DFS(O_NEIGHBOURS)
    for i in range(len(MERGE)):
        sum=0
        for j in range(len(MERGE[i])):
            element=MERGE[i][j]
            sum+=len(O[element])
        if sum%2!=0:
            return False
    return True


    

            

def DFS(G):     
    n=len(G)    
    def DFS_Visit(G,u):
        nonlocal spójne
        visited[u]=True
        for i in range(len(G[u])):
            v=G[u][i]
            if visited[v]==False:
                MERGE[spójne].append(v)
                DFS_Visit(G,v)
        

    visited=[False for _ in range(n)]
    MERGE=[]
    spójne=-1


    for i in range(n):

        if visited[i]==False and len(G[i])>0:
            MERGE.append([])
            spójne+=1
            MERGE[spójne].append(i)
            DFS_Visit(G,i)
    return MERGE



                
print(Algocja2(E,C))
