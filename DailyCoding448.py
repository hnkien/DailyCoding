def partition(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
        elif arr[mid] == 'B':
            arr[mid], arr[high] = arr[high], arr[mid]
            # mid += 1
            high -= 1
        else:
            mid += 1
    return arr


arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(arr)
print(partition(arr))


