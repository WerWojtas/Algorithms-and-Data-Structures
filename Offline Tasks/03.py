# We have an array of strings. A string is equivalent to another string if they are the same or the opposite of the string is the same. For example: cat and cat, or
# cat and tac are equivalent. The power of the string is the number of other equivalent strings in the array. An algorithm needs to find the strongest string.

def strong_string(T):    #quick_sort solution. It sorts strings alfabetical and counts the number of eqivalent strings.
    n=len(T)
    for i in range(n):
        a=T[i]
        x=len(a)
        if a[0]>a[x-1]:
            T[i]=a[::-1]
    quick_sort(T,0,n-1)
    maxi=0
    flag=1
    for i in range(n-1):
        if T[i]==T[i+1]:
            flag+=1
        else:
            if maxi<flag:
                maxi=flag
            flag=1
    if maxi<flag:
        maxi=flag
    return maxi
    
def quick_sort(T,first=0,last=0):
    if first<last:
        pi=partition(T,first,last)
        quick_sort(T,first,pi-1)
        quick_sort(T,pi,last)

def partition(T,first,last):
    pivot=T[last]
    i=first-1
    for j in range(first,last):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[last]=T[last],T[i+1]
    return i+1
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  def strong_string(T):               # radix_sort solution. Sorts by lenght -> sort alfabetical -> count.
    lenght_T=len(T)
    max_lenght=0
    for i in range(lenght_T):
        if len(T[i])>max_lenght:
            max_lenght=len(T[i])
    S=[[] for _ in range(max_lenght+1)]
    for i in range(lenght_T):
        S[len(T[i])].append(T[i])
    maxi=0
    for i in range(len(S)):
        if S[i]==[]:
            continue
        
        else:
            K=S[i]
            n=len(K)
            if n<maxi:
                continue
            m=len(K[0])
            for i in range(n):
                a=K[i]
                if ord(a[0])<ord(a[m-1]):
                    a=a[::-1]
                    K[i]=a
            Radix_sort(K,n,m)
            flag=1
            for j in range(n-1):
                x=K[j]
                y=K[j+1]
                if x==y or x==y[::-1]:
                    flag+=1
                else:
                    if flag>maxi:
                        maxi=flag
                    flag=1
            if flag>maxi:
                maxi=flag
    return maxi

    





def Radix_sort(T,n,m):
    for i in range(m-1,-1,-1):
        counting_sort(T,i,n)




def counting_sort(T,j,n):
    S=[[] for _ in range(26)]
    for i in range(n):
        a=T[i]
        S[ord(a[j])%26].append(a)
    counter=0
    for i in range(19,26):
        if S[i]==None:
            continue
        for g in range(len(S[i])):
            b=S[i]
            T[counter]=b[g]
            counter+=1
    for i in range(0,19):
        if S[i]==None:
            continue
        for g in range(len(S[i])):
            b=S[i]
            T[counter]=b[g]
            counter+=1
    

