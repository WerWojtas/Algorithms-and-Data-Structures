"""Dany jest ciąg przedziałów postaci [ai
, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków."""

def przedział1(T,a,b):
    n=len(T)
    F=[False for _ in range(b-a+1)]

    for i in range(n):
        if T[i][0]==a:
            F[T[i][1]-a]=True


    for i in range(a+1,b+1):
        print(i)
        for j in range(1,n):
          
            if T[j][1]==i:
            
                if F[T[j][0]-a]==True:
              
                    F[i-a]=True

    print(F)
    
    return F[n-1]

T=[(2,4),(3,8),(4,5),(4,7),(1,10),(7,12),(12,16)]

print(przedział1(T,2,12))

