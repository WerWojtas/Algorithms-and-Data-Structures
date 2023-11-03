"""Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
, jaki
można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki."""

def Forest(PROFIT):
    n=len(PROFIT)
    F=[0 for _ in range(n)]
    F[0]=PROFIT[1]
    if PROFIT[0]>PROFIT[1]:
        F[1]=PROFIT[0]
    else:
        F[1]=PROFIT[1]

    for i in range(2,n):
        F[i]=max(PROFIT[i]+F[i-2],F[i-1])

    return F[n-1]

T=[4,1,2,7,3,12,14]
print(Forest(T))
