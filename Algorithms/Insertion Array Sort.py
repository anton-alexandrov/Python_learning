#O(n**2)
def insertion_sort(A):
    """"
    Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
    The array is virtually split into a sorted and an unsorted part.
    Values from the unsorted part are picked and placed at the correct position in the sorted part.
    """
    for k in range (1,len(A)):
        for i in range(k, 0, -1):
            if A[i]<A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]


    return A

print (insertion_sort([4,3,2,5,1]))

print (insertion_sort([0,1,2,3,4,5,6]))

print (insertion_sort([10,9,8,7,6,5,4,3,2,1]))