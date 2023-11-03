from queue import PriorityQueue



def min_cost( O, C, T, L ):
    n=len(O)
    Result=[None for _ in range(n)]
    for i in range(n):
        Result[i]=(O[i],C[i])
    Result.sort()


 
    x=min_costt(Result,T,L)

    return x

def min_costt(T,limit,lenght):
    n=len(T)
    MIN=PriorityQueue()
    min=10**10
    i=0
    j=0
    while i<n and j<n:
        
        distance=T[i][0]
        cost=T[i][1]
        if distance-limit<=0:
            MIN.put((0,cost,i))
            i+=1
        elif distance-limit-T[j][0]>0:
            sum,saved,x=MIN.get()
            if x>j:
                MIN.put((sum,saved,x))
            j+=1
        else:
            if MIN.empty():
                break
            sum,saved,x=MIN.get()
            if x<j:
                continue
            else:

                MIN.put((sum,saved,x))
                if distance+limit>=lenght:
                    if saved<cost:
                        price=sum+saved
                    else:
                        price=sum+cost
                    if price<min:
                        min=price
                else:
                    a=limit+limit
                    if distance+a>=lenght:
                        price=sum+saved+cost
                        if price<min:
                            min=price
                    if saved<cost:
                        MIN.put((sum+saved,cost,i))
                    else:
                        MIN.put((sum+cost,saved,i))
                i+=1
    return min
