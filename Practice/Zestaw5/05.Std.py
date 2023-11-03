"""Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
na k spójnych podciągów: (a0, . . . , a`1
), (a`1+1, . . . , a`2
), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości."""

def maximin(T,k):
    n=len(T)
    F=[[0 for _ in range(k+1)]for _ in range(n)]
    S=[0 for _ in range(n)]
    F[0][1]=T[0]
    S[0]=T[0]

    for i in range(n):
        F[i][1]=F[i-1][1]+T[i]
        S[i]=S[i-1]+T[i]

    for podział in range(2,k+1):
        for i in range(podział-1,n):
            for j in range(podział-2,i):
                F[i][podział]=max(F[i][podział],min(F[j][podział-1],S[i]-S[j]))

    return F[n-1][k]

"""Tablica F[i][t] oznacza maksymalną wartość podziału ciągu T[0..i] na t części. Dla każdego i F[i][1] dzielimy na jedną część(podciąg = cały ciąg)
więc maksymalna wartość jego podziału to suma wszystkich elementów. Ustawiamy więc wartości w tablicy F, dodatkowo tworzymy tablicę S, która
przetrzymuje nam sumy takie jak F[i][1], będzie nam to potrzebne w późniejszej części zadania. Następnie iterujemy po wszystkich
podziałach zaczynając od podziału na 2 el, dla każdego podziału iterujemy po wszystkich indeksach zaczynając od podział-1 ponieważ wtedy do
indeksu podział-1 mamy najmniejszą możliwą ilość elementów do podziały. Np t=5 więc zaczynamy od i=4 bo nie da się podzielić i=3 czyli 4 elementów
na 5 części. Dla każdego i iterujemy po wszystkich j zaczynając od podział-2, ponieważ za pomocą j będziemy obliczać największą możliwą wartość
na podział-1 części więc aby to zrobić indeks j musi być co najmniej podział -2 (wtedy od 0 do j mamy dokładnie podział-1 elementów).
Następnie dla każdego j wyliczamy min z wartości F[j][podział-1] czyli największej wartości podziału na podział-1 części do indeksu j.
Ostatni podział jest to suma elementów od j do i czyli S[i]-S[j], bierzemy mniejszą z wartości. Gdy wyliczymy je wszystkie bierzemy max z nich
wszystkich i wpisujemy do F[i][podział]. Złożoność obliczeniowa to O(n^3). """