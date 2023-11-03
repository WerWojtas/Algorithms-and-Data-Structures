""" Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A."""

def prom(T,L):
    n=len(T)

    def f(i,pok_1,pok_2):
        if pok_1+T[i]<=L and pok_2+T[i]<=L:
            return max(f(i+1,pok_1+T[i],pok_2),f(i+1,pok_1,pok_2+T[i]))
        elif pok_1+T[i]<=L:
            return f(i+1,pok_1+T[i],pok_2)
        elif pok_2+T[i]<=L:
            return f(i+1,pok_1,pok_2+T[i])
        else:
            return 0