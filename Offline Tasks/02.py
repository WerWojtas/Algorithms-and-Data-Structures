# We have an array of natual numbers. We need to collect numbers entering from the left or right side of an array. Each time we collect a number the previous
# numbers are being degraded to 0. For example: T=[3,5,2,6,9,1,8]. After collecting 5 -> T=[0,0,2,6,7,1,8]. After collecting -> T=[0,0,2,6,0,0,0].
# Each time we collect a number the rest of numbers is being reduced by 1. The algorithm must find the biggest possible sum of collected numbers.
# Example: S=[1,7,3,4,1] Collect 7, S=[0,0,2,3,0] Collect 7+3, S=[0,0,1,0,0], Collect 7+3+1=11

def heapify(T,n,i):                     # heap_sort solution. Building a heap -> extracting the biggest element -> repairing a heap.
    l = (2*i)+1
    r = (2*i)+2
    maxi=i
    if l < n and T[l] > T[maxi]:
        maxi=l
    if r < n and T[r] > T[maxi]:
        maxi = r
    if maxi != i:
        T[i], T[maxi] = T[maxi], T[i]
        heapify(T,n,maxi)


def snow(S):
    sum=0
    n=len(S)
    for i in range((n-2)//2,-1,-1):
        heapify(S,n,i)
    for i in range(n):
        if S[0]-i<0:
            break
        sum+=S[0]-i
        S[0]=0
        heapify(S,n,0)
    return sum                      
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  def snow( S ):                # merge_sort solution with partition optimalization. Using a partition to divide numbers into larger and smaller -> if the smallest
    n=len(S)                    # element from the larger group is bigger that quiantity of them sorting only the larger group -> adding elements to sum as long as
    sum=0                       # numbers are bigger than 0.
    pivot = S[n-1]
    min=10**10
    i = -1
    for j in range(0, n-1):
        if S[j] >= pivot:
            i += 1
            if S[j]<min:
                min=S[j]
            S[i], S[j] = S[j], S[i]
    S[i+1], S[n-1] = S[n-1], S[i+1]
    if i+1>=min:
        S=S[:i+1]
    merge_sort(S)
    for i in range(len(S)):
        if S[i]-i>0:
            sum+=S[i]-i
        else:
            break

    
    return sum

def merge_sort(T):

    n=len(T)
    if n==1:
        return T
    else:
        mid=n//2
        T1=T[:mid]
        T2=T[mid:]
        T1=merge_sort(T1)
        T2=merge_sort(T2)
        x=y=z=0
        n1=len(T1)
        n2=len(T2)
        while x<n1 and y<n2:
            if T1[x]>T2[y]:
                T[z]=T1[x]
                x+=1
            else:
                T[z]=T2[y]
                y+=1
            z+=1
        if x==n1:
            for i in range(z,n):
                T[i]=T2[y]
                y+=1
        elif y==n2:
            for i in range(z,n):
                T[i]=T1[x]
                x+=1
    return T
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  def snow(S):                       # counting_sort solution. Create an array for each number -> each number from starting array is being counted -> adding
    n=len(S)                         # numbers to sum as long as the last number is bigger than 0.
    maxi=0
    sum=0
    maxi=max(S)
    K=[0 for _ in range(maxi+1)]
    for i in range(n):
        K[S[i]]+=1
    flag=0
    for i in range(maxi,0,-1):
        if i-flag<=0:
            break
        if K[i]==0:
            continue
        for j in range(1,K[i]+1):
            if i-flag<=0:
                break
            sum+=i-flag
            flag+=1

    return sum


