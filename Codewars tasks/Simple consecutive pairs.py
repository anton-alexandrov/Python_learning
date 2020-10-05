def pairs(ar):
    first_list = []
    second_list = []
    count = 0
    for x in range (0, len(ar)):
        if x%2 == 0:
            first_list.append(ar[x])
        else:
            second_list.append(ar[x])
    for k in range (0, min(len(first_list), len(second_list))):
        if abs(first_list[k]-second_list[k])==1:
            count+=1
    return count

def solution (arr):
    return sum(abs(a - b) == 1 for a, b in zip(arr[::2], arr[1::2]))

print(pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]))
print(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]))
print(pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]))# 0)
print(pairs([-55, -56, -7, -6, 56, 55, 63, 62]))# 4)
print(pairs([73, 72, 8, 9, 73, 72]))#, 3)

my_list = [1, 2, 5, 8, -4, -3, 7, 6, 5]
for a,b in zip(my_list[::2], my_list[1::2]):
    print(abs(a-b))