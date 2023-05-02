# Heap Sort Algorithm

def heapify(T, n, i=0):     # Reapiring heap. Computational complexity - O(logn).
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and T[largest] < T[left]:
        largest = left

    if right < n and T[largest] < T[right]:
        largest = right

    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, n, largest)


def build_heap(T):         # Building heap. Computational complexity - O(nlogn).
    n = len(T)
    for i in range((n-2)//2, -1, -1):
        heapify(T, n, i)


def heap_sort(T):        # Heap-sort. Computational complexity - O(nlogn).
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
