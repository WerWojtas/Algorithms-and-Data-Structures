def partition(T, first, last):
    pivot = T[last]
    i = first-1
    for j in range(first, last):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[last] = T[last], T[i+1]
    return i+1


def quicksort(T, first=0, last=0):      # Quick_Sort algorithm
    if first < last:
        pi = partition(T, first, last)
        quicksort(T, first, pi-1)
        quicksort(T, pi+1, last)
        
        
def select(A, first, last, position): # Quick_select slgorithm
    if first == last:
        return A[first]
    q = partition(A, first, last)
    if q == position:
        return A[q]
    elif position < q:
        return select(A, first, q - 1, position)
    else:
        return select(A, q + 1, last, position)
