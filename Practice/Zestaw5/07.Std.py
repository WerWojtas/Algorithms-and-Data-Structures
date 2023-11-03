"""Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie."""

def szachownica(T):
    n=len(T)
    F=[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][0]=F[i-1][0]+T[i][0]
        F[0][i]=F[0][i-1]+T[0][i]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j]=min(F[i-1][j],F[i][j-1])+T[i][j]

    return F[n-1][n-1]




    