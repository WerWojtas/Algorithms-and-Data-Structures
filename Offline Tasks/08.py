from queue import PriorityQueue 
from collections import deque


def plan(T):
    Plamy,Places=swap(T)
    paliwo=Plamy[0]
  
  
 
    i=1
    flag=1
    sum1=0
    n=len(T[0])
    Q=PriorityQueue()
    while paliwo<n-1:
       
        while i<len(Places) and Places[i]<=paliwo:
            Q.put(-Plamy[Places[i]])
            sum1+=(Plamy[Places[i]])
            i+=1
        quantity=Q.get()
 
        paliwo-=quantity
        flag+=1
       
        



    return flag

def swap(T):
    m=len(T)
    n=len(T[0])
    Plamy=[0 for _ in range(n)]
    Places=[]
       
    for i in range(n):
   
        if T[0][i]!=0 :
            sum=T[0][i]
            T[0][i]=0
            Q=deque()
            Q.append((0,i))
            while len(Q)!=0:
                x,y=Q.popleft()
           
                if x<m-1:
                    flag=x+1
                    if T[flag][y]!=0:
                        Q.append((flag,y))
                        sum+=T[flag][y]
                        T[flag][y]=0
                if y<n-1:
                    flag=y+1
                    if T[x][flag]!=0:
                        Q.append((x,flag))
                        sum+=T[x][flag]
                        T[x][flag]=0
                if x>0:
                    flag=x-1
                    if T[flag][y]!=0:
                        Q.append((flag,y))
                        sum+=T[flag][y]
                        T[flag][y]=0
                if y>0:
                    flag=y-1
                    if T[x][flag]!=0:
                        Q.append((x,flag))
                        sum+=T[x][flag]
                        T[x][flag]=0
                
                
     
    
         
            Plamy[i]=sum
            Places.append(i)
    
    return Plamy,Places
