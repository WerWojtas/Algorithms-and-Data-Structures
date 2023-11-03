"""Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną 
ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)."""

def monety(T,kwota):
    n=len(T)
    F=[0 for _ in range(kwota+1)]

    for i in range(1,kwota+1):
        F[i]=10**10
        for j in range(n):
            if i-T[j]>=0:
                F[i]=min(F[i],F[i-T[j]]+1)

    print(F)

    return F[kwota]

T=[1,5,8]
print(monety(T,15))