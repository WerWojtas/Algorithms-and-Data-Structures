"""Problem plecakowy tylko możemy rozdzielać przedmioty (np płyny)"""

def plecak(ITEMS,PRICES,max_weight):
    n=len(ITEMS)
    T=[None for _ in range(n)]
    for i in range(n):
        T[i]=(ITEMS[i]/PRICES[i],ITEMS[i])

    T.sort()
    weight=0
    sum=0
    i=0
    while weight<max_weight:
        if weight+ITEMS[i]>max_weight:
            sum+=(max_weight-weight)*T[i][0]
            weight=max_weight
        else:
            weight+=T[i][1]
            sum+=T[i][0]*T[i][1]
    return sum

i = [10,5,10]
p = [1, 4, 10]
m = 10
print(plecak(i, p, m))


