def array_plus_array(arr1, arr2):
    sum = 0
    for i in arr1:
        sum += int(i)
    for j in arr2:
        sum += int(j)
    return sum

def solution (arr1, arr2):
    return sum(arr1 + arr2)

print(array_plus_array([1,2,3],[4,5,6]))
print(array_plus_array([-1, -2, -3], [-4, -5, -6]))

print(solution([1,2,3],[4,5,6]))
print(solution([-1, -2, -3], [-4, -5, -6]))