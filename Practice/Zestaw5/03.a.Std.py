"""Najdłuższy podciąg rosnący"""


def podciąg(T):   # O(n^2)
    n=len(T)
    F=[1 for _ in range(n)]
    F[0]=1

    for i in range(n):
        for j in range(i):
           
            if T[j]<T[i] and F[j]+1>F[i]:
                F[i]=F[j]+1


    print(max(F))


T=[2,4,3,1,5,2,7,8,3]
podciąg(T)

def podciąg2(T):  #O(n) wykorzystanie binary_search
    n=len(T)
    TAILS=[None for _ in range(n)]
    TAILS[0]=T[0]
    lenght=1
    flag=0
    for i in range(n):
        print(TAILS)
        if T[i]>TAILS[flag]:
            flag+=1
            TAILS[flag]=T[i]
            lenght+=1
        else:
            print("T")
            ind=binary_search(TAILS,T[i],0,lenght-1)
            TAILS[ind]=T[i]
   

    return lenght
    


def binary_search(T,number,left,right):
    while left<right:
        mid=(left+right)//2
        if T[mid]<number:
            left=mid+1
        else:
            right=mid
    return left



print(podciąg2(T))

