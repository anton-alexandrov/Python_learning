#O(n**2)
def selection_sort(A):


    for k in range (0,len(A)):
        for i in range(1, len(A)-k):
            if A[i] < A[i-1]:
                A[i], A[i-1]=A[i-1],A[i]
    return A


print (selection_sort([4,3,2,5,1]))

print (selection_sort([0,1,2,3,4,5,6]))

print (selection_sort([10,9,8,7,6,5,4,3,2,1]))