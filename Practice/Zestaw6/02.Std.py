""" (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim."""

def klocki(T):
    n=len(T)
    F=[1 for _ in range(n)]
    F[0]=1

    for i in range(1,n):
        for j in range(i):
            if zawiera(T[j],T[i]):
                F[i]=max(F[i],F[j]+1)
    print(F)
    result=n-max(F)

    return result
                     

def zawiera(k1,k2):
    if k1[0]<=k2[0] and k1[1]>=k2[1]:
        return True
    return False


T=[(0,5),(0,15),(1,10),(0,4),(2,10),(1,3),(5,8),(6,7),(1,2)]
print(klocki(T))
