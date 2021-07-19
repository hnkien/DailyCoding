def partition(arr):
    low, mid, high = 0, 0, len(arr) - 1
<<<<<<< HEAD
    while mid < high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            print(arr)
        elif arr[mid] == 'B':
            arr[mid], arr[high] = arr[high], arr[mid]
            mid += 1
            high -= 1
            print(arr)
=======
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
        elif arr[mid] == 'B':
            arr[mid], arr[high] = arr[high], arr[mid]
            # mid += 1
            high -= 1
>>>>>>> 30d0db1d8e373b1e0740f40f90ce3260c9c99e8d
        else:
            mid += 1
    return arr

<<<<<<< HEAD
arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(arr)
print(partition(arr))
=======

arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(arr)
print(partition(arr))


>>>>>>> 30d0db1d8e373b1e0740f40f90ce3260c9c99e8d
