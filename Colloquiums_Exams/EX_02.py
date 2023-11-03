# Weronika Wojtas
""" Algorytm dynamiczny. F[i][b] to najmniejsza wymagana wartość aby dojechać do planety i o pojemności baku b. Warunenk graniczny to dla każdej
pojemności baku zerowej stacji koszt dojechania to koszt zatankowania odpowiedniej ilości paliwa. Następnie dla każdej stacji oblicza on początkowo
koszt teleportacji do tej stacji, następnie przechodzi po wszystkich możliwych stacjach z których da się dolecieć do itej stacji i dla każdej z nich
przechodzi po wszystkich możliwych wartościach które można otrzymać po przeleceniu dystansu i po wszystkich wartościach baku z których można zacząć.
Oblicza minimalną wartość dla każdej stacji za pomocą wzoru. Na koniec zwraca min koszt dojazdu do ostatniej stacji.Złożoność O(nE)"""



def planets( D, C, T, E ):
    n=len(T)
    F=[[10**10 for _ in range(E+1)] for _ in range(n)]
    TELE=[[] for _ in range(n)]
    for i in range(E+1):
        F[0][i]=0
    for i in range(n):
        if T[i][0]!=i:
            TELE[T[i][0]].append((i,T[i][1]))
  

    
    for paliwo in range(E+1):
        F[0][paliwo]=paliwo*C[0]

    
    j=0
    for planet in range(1,n):
        for tele in range(len(TELE[planet])):
          
            F[planet][0]=min(F[TELE[planet][tele][0]][0]+TELE[planet][tele][1],F[planet][0])

        while D[planet]-D[j]>E+1:
            j+=1

        for before in range(j,planet):
            distance=D[planet]-D[before]
            if D[planet]-D[before]<=E+1:
                for paliwo_after in range(E+1-distance):
                    dotankować=paliwo_after+(D[planet]-D[before])
                   
                    for paliwo_before in range(E+1):
                        if paliwo_before<dotankować:
                           

                
                            F[planet][paliwo_after]=min(F[planet][paliwo_after],F[before][paliwo_before]+(dotankować-paliwo_before)*C[before])

  

    return min(F[n-1])           

