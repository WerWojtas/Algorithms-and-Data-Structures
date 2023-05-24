"""Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi
mają się odbywać po trasach zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji.
Król chce, żeby każde miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić,
czy da się wynająć odpowiednie odcinki autostad. Należy jednak pamiętać o następujących ograniczeniach:
1. w Bitocji wszystkie autostrady są jednokierunkowe,
2. z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
miast,
3. do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
miast,
Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.
Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych cen i należy wybrać wspólną cenę
dla wszystkich wynajętych odcinków.
"""

from time import sleep

def good_start(G):          
    n=len(G)                  
    VISITED=[False for _ in range(n)]
    SORTED=[]
    
    def DFS_Visit(G,vertex):
        VISITED[vertex]=True
        for j in range(len(G[vertex])):
            vertex2=G[vertex][j][0]
            if VISITED[vertex2]==False:
                DFS_Visit(G,vertex2)

        SORTED.append(vertex)

    for i in range(n):
        if VISITED[i]==False:
            DFS_Visit(G,i)
   
    x=len(SORTED)
    root=SORTED[x-1]
    flag2=0
    sum=0
    pprice=()
    print(SORTED)


    VISITED=[False for _ in range(n)]
    def DFS_Visit2(G,vertex,flag,price_before):
        nonlocal n,flag2,sum,pprice
        if flag2==1:
            return
 
        VISITED[vertex]=True

     
        for j in range(len(G[vertex])):
            neighbour=G[vertex][j][0]
            price=G[vertex][j][1]
            if VISITED[neighbour]==False and ((price_before[0]<=price[0] and price_before[1]>price[0]) or 
                                              (price[0]<=price_before[0] and price[1]>price_before[0])):
                next_price=(max(price_before[0],price[0]),min(price_before[1],price[1]))
                DFS_Visit2(G,neighbour,flag+1,next_price)
                VISITED[neighbour]=False
        if flag==n-1:
            flag2=1
            pprice=price_before
            return
        sum+=1

    
        
        
    DFS_Visit2(G,root,0,(0,10**10))
    print(sum)
    print(pprice)
    if flag2==1:
        return True
    return False
    

        



T=[[(1,(2,12))],
   [(2,(5,8))],
   [(3,(6,10)),(4,(9,14))],
   [],
   [(5,(0,10)),(3,(2,10))],
   [(0,(3,8))],
   [(0,(0,20))]]


print(good_start(T))
    
    