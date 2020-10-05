#O(n**2)
import time
start_time = time.time()
def selection_sort(A):
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element
    (considering ascending order) from unsorted part and putting it at the beginning.
    The algorithm maintains two subarrays in a given array.
    """

    for k in range (0,len(A)):
         for i in range(k, len(A)):
            if A[i]<A[k]:
                A[k],A[i] = A[i],A[k]
    return A



    return A

print (selection_sort([4,3,2,5,1,6]))
print("--- %s seconds ---" % (time.time() - start_time))

#print (selection_sort([0,1,2,3,4,5,6]))

#print (selection_sort([10,9,8,7,6,5,4,3,2,1]))