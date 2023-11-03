"""Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2))."""



def podciąg(A,B):
    n=len(A)

    F=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if A[i]==B[0]:
            F[i][0]=1
        if B[i]==A[0]:
            F[0][i]=1
    
    for i in range(1,n):
        for j in range(1,n):
            if A[i]==B[j]:
                F[i][j]=F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])

    print(F[n-1][n-1])

A=[8,2,6,3,10,5,7,9,16,15]
B=[12,45,8,4,3,15,7,28,9,3]

podciąg(A,B)

