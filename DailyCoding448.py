# This is your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def partition(arr):
    low, mid, high = 0, len(arr)//2, len(arr) - 1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
        elif arr[mid] == 'B':
            arr[mid], arr[high] = arr[high], arr[mid]
            mid += 1
            high -= 1
        else:
            mid += 1
    return arr

if __name__ == "__main__":
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    print(arr)
    print(partition(arr))
