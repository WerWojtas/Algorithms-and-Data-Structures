"""Mamy n miast rozłożonych na układzie współrzędnych. Chcemy znaleźć taką drogę, aby zacząć w mieście 0, skończyć w mieście 0 i odwiedzić każde
miasto. Każde miasto możemy odwiedzić tylko raz. Jaką drogę wybrać, aby była najkrótsza? Współrzędne x są parami różne."""

"""Wersja bitoniczna problemu: wybieramy miasto n-1 które jest najdalej oddalone od miasta 0. Wtedy szukamy dwóch dróg, jedna porusza się ciągle
z rosnącym x, druga ciągle z malejącym. Chcemy znaleźć najkrótszą taką drogę"""

def komi_woj(CITIES):
    n=len(CITIES)
    DISTANCE=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            DISTANCE[i][j]=distance(CITIES[i][0],CITIES[i][1],CITIES[j][0],CITIES[j][1])
    


    F=[[10**10 for _ in range(n)] for _ in range(n)]
    F[0][1]=DISTANCE[0][1]
    def rekurencja(i,j,F,DISTANCE):
        if F[i][j]!=10**10:
            return F[i][j]
        if i==j-1:
            best=10**10
            for city in range(j-1):
                best=min(best,rekurencja(city,j-1,F,DISTANCE)+DISTANCE[city][j])
            F[i][j]=best
        else:
            F[i][j]=rekurencja(i,j-1,F,DISTANCE)+DISTANCE[j-1][i]
        return F[i][j]


    for i in range(n):
        for j in range(i+1,n):
            rekurencja(i,j,F,DISTANCE)
            print(F[i][j],i,j,n)

    return  min(F[i][n-1]+DISTANCE[i][n-1] for i in range(n-1))





def distance(x1,y1,x2,y2):
    dist=(abs(x1-x2)**2+abs(y1-y2)**2)**(1/2)
    return dist

T=[(0,6),(1,0),(2,3),(5,4),(6,1),(7,5),(8,2)]

print(komi_woj(T))

"""Na początku tworzymy funkcję distance w której ustawiamy odległość między wszystkimi dwoma miastami. Tworzymy funkcję F(x,y) w której zapisywać
będziemy min trasę z miasta zero do x i z miasta 0 do y która zawiera wszystkie miasta od 0...y. Tworzymy funkcję rekurencyjną, 
która obliczy wartość F dla każdego x,y. Jeżeli funkcja F została już obliczona po prostu ją zwracamy. Jeżeli miasto i=j-1, oznacza
to, że przed chwilą wykonaliśmy skok z i do j-1 i teraz musimy znaleźć drugą drogę. Szukamy jej po wszystkich miastach do j-1. Będzie to 
najmniejsza wartość z wykonania rekurencji dla wszystkich miast i miast j-1, to znaczy najkrótsza odległość z miasta 0 do miasta city
i miasta 0 do miasta j-1. Jeśli nie wykonaliśmy takiego skoky wystarczy, że obliczymy wartość funkcji dla j-1 oraz i, a następnie dodamy
do tego odległość j-1,j. Dzieje się tak ponieważ szukamy tras bitonicznych, czyli takich które poruszają się wzdłuż x. Jeśli i jest znacząco
mniejsze niż j do najbliższa odległość do j będzie z j-1. Wykonujemy rekurencje dla każdego miasta i, oraz większego od niego miasta j.
Teraz mamy obliczone wszystkie najmniejsze trasy z miasta 0 do miasta n i z miasta 0 do każdego miasta. Wynikiem jest min z funkcji F oraz 
dystansu po wszystkich miastach i."""