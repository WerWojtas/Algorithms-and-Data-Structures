"""Mamy x przedziałów chcemy wybrać jak najwięcej nie pokrywających się przedziałów."""

def przedziały(T):
    n=len(T)
    for i in range(n):
        T[i]=(T[i][1],T[i][0])
    T.sort()
    Result=[]
    sum=1
    przedział=T[0]
    Result.append((T[0][1],T[0][0]))
    for i in range(1,n):
        if przedział[0]>T[i][1]:
            continue
        else:
            sum+=1
            Result.append((T[i][1],T[i][0]))
            przedział=T[i]


T=[(0,5),(1,3),(1,7),(3,6),(5,8),(7,9)]

przedziały(T)

"""Wybieramy najwcześniej kończący się przedział, usuwamy powstałe konflikty, powtarzamy operacje."""
