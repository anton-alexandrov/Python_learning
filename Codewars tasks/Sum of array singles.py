def repeats(arr):
    my_list = []
    duplicates = []
    for k in range (0, len(arr)):
        if arr[k] not in arr[k+1:] and arr[k] not in duplicates:
            my_list.append(arr[k])
        else:
            duplicates.append(arr[k])
    return (sum(my_list))




print(repeats([4,5,7,5,4,8]))#,15)
