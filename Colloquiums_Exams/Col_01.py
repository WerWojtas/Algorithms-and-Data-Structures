# We have an array of natural numbers, p is the lenght of interval, k is the position after sorting an interval from the biggest to the smallest numbers.
# k<=p<=lenght of an array. Algorithm needs to count the sum of k numbers within all possible intervals among an array. For example T=[7,9,1,5,8,6,2,12] k=4 p=5.
# First interval: 7,9,1,5,8 sorted from the biggest 9,8,7,5,1 at position 4 -> 5. Second interval 9,1,5,8,6 -> sorted 9,8,6,5,1 at position 4 -> 5. 
# Third 1,5,8,6,2 sorted 8,6,5,2,1 position 4 ->2. Last interval 5,8,6,2,12 -> sorted 12,8,6,5,2 position 4 -> 5. Sum=17


def ksum(T, k, p):         #solution is creating new array for an interval and using quick_select algorithm to extract number
    n=len(T)
    sum=0
    for i in range(n-p+1):
        K=T[i:i+p]
        sum+=select(K,0,p-1,k-1)
    return sum


def partition(T,first,last):
    pivot=T[last]
    i=first-1
    for j in range(first,last):
        if T[j]>=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[last]=T[last],T[i+1]
    return i+1

def select(T, first, last, position):
    if first == last:
        return T[first]
    q = partition(T, first, last)
    if q == position:
        return T[q]
    elif position < q:
        return select(T, first, q - 1, position)
    else:
        return select(T, q + 1, last, position)
    
