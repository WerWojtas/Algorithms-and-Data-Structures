def magic( C ):
    n=len(C)
   
    F=[0 for _ in range(n)]
    SWAP=[[] for _ in range(n)]

    for i in range(n):
        for j in range(1,4):
            if C[i][j][1]!=-1:
                if C[i][0]-C[i][j][0]<=10:
                    SWAP[C[i][j][1]].append([i,C[i][0]-C[i][j][0]])



    for i in range(1,n):
        F[i]=-10**10
        for j in range(len(SWAP[i])):
            if F[SWAP[i][j][0]]+SWAP[i][j][1]>=0:
                F[i]=max(F[i],F[SWAP[i][j][0]]+SWAP[i][j][1])


    return F[n-1] if F[n-1]!=-10**10 else -1
