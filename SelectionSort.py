def mergeSort(arr: list) -> None:
    cur_pos = 0
    n = len(arr)
    while cur_pos < n:
        min_value = arr[cur_pos]
        i = cur_pos + 1
        min_pos = cur_pos
        while i < n:
            if arr[i] < min_value:
                min_value = arr[i]
                min_pos = i
            i += 1
        if min_pos != cur_pos:
            arr[cur_pos], arr[min_pos] = arr[min_pos], arr[cur_pos]
        cur_pos += 1

arr = [6, 5, 12, 10, 9, 1]
mergeSort(arr)
print(arr)

