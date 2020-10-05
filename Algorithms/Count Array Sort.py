#O(n)
import time
start_time = time.time()

def count_sort (A):
    F = [0]*len(A)

    for i in range (0, len(A)):
        F[A[i]] += 1
    sorted_list = []
    for n in range(0, len(F)):
        for i in range (0, F[n]):
            sorted_list.append(n)
    print(f'F[n] = {F[n]}, n = {n}')

    return sorted_list

def count_sort_from_set (A):
    F = set(A)
    print(F)
    value = 1
    count = 0
    m = (value, count)

    for n in A:

        if n == value:
            count+=1
        else:
            value = n
            count = 1
    print(value, count)


print (count_sort([4,3,2,5,1,1, 6]))
#print (count_sort_from_set([4,3,2,5,1,1, 6]))

print("--- %s seconds ---" % (time.time() - start_time))

print (count_sort([0,1,2,3,4,5,6]))

print (count_sort([1,9,8,7,6,5,4,3,2,1]))