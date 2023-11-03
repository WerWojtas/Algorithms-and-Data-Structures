def dominance(P):
  n=len(P)
  T_X=[0]*(n+1)
  T1_X=[0]*(n+1)
  T1_Y=[0]*(n+1)

  for x,y in P:
    T_X[x]+=1
    T1_X[x]+=1
    T1_Y[y]+=1

  
  for i in range(1,n+1):
    T1_X[i]+=T1_X[i-1]


  for i in range(n-1,0,-1):
    T1_Y[i]+=T1_Y[i+1]

  max_sum=0

  for x,y in P:
    sum=T1_X[x]-T1_Y[y]+1-T_X[x]
    if sum>max_sum:
      max_sum=sum

    

    
  return max_sum
