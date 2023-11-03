"""(mnożenie macierzy) Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności."""


def macierze(T):
    n=len(T)
    F=[[0 for _ in range(n)]for _ in range(n)]


    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            print(F,i,j)
            F[i][j]=float("inf")
            for k in range(i,j):
                F[i][j]=min(F[i][j],F[i][k]+F[k+1][j]+T[i][0]*T[k][1]*T[j][1])
                print(F[i][j],k)

    return F[0][n-1]


T=[[10,100],[100,5],[5,10]]
print(macierze(T))


"""Tworzymy funkcję kwadratową wynikową. F(i,j) - najmniejsza liczba mnożeń potrzebna do obliczenia iloczynu macierzy od i do j włącznie. Dla
każdego indeksu i iterując od n-2 przechodzimy po możliwych przedziałach(j) i dla każdego z nich sprawdzamy wartość mnożeń dla każdej możliwej
liczby k - jest to liczba w środku przedziału. Ilość mnożeń to min z aktualnej ilości lub Ilości mnożeń od i do k, od k+1 do j i pomnożenia tych
dwóch wynikowych macierzy. Zaczynając od najmniejszych przedziałów zawsze mamy zapewnione, że obliczyliśmy ilość dla wszystkich przedziałów w i
do j. Złożoność czasowa O(n^3) bo mamy 3 pętle for, złożoność pamięciowa O(n^2) bo tworzymy tablicę n^2.""",