"""Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb."""

def żaba(T):
    n=len(T)
    

    def f(i,e,jumps):
        nonlocal n
   
        if i ==n-1:
            return jumps
        sum=10**10
        for j in range(i+1,i+e+1):
            if j==n:
                break
            elif e-(j-i)>=0:
                sum=min(sum,f(j,e-(j-i)+T[j],jumps+1))
        return sum
    
    return f(0,T[0],0)

T=[7,0,3,3,3,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(żaba(T))




    