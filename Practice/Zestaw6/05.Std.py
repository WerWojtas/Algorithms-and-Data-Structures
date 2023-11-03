"""Proszę zaproponować algorytm dla dwuwymiarowej
wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
przedmiotu pi dane sa nastepujace trzy liczby:
1. v(pi) – wartość przedmiotu,
2. w(pi) – waga przedmiotu, oraz
3. h(pi) – wysokość przedmiotu.
Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
jego poprawność."""

def knapskack3(T,max_weight,max_height):
    n=len(T)
    F=[[[0 for _ in range(max_height+1)]for _ in range(max_weight+1)] for _ in range(n)]

    for height in range(T[0][2],max_height+1):
        for weight in range(T[0][1],max_weight+1):
            F[0][weight][height]=T[0][0]


    for height in range(max_height+1):
        for weight in range(max_weight+1):
            for item in range(1,n):
                F[item][weight][height]=F[item-1][weight][height]
                if weight-T[item][1]>=0 and height - T[item][2]>=0:
                    F[item][weight][height]=max(F[item][weight][height],F[item-1][weight-T[item][1]][height-T[item][2]]+T[item][0])

    print(F)

    return F[n-1][max_weight][max_height]

T=[(2,5,4),(5,1,1),(10,3,5),(12,6,6),(1,8,3)]

print(knapskack3(T,10,12))
