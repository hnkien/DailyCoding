# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def multiple(arr : list) -> list:
    n = len(arr)
    arr_left = []
    arr_right = []
    tmp_left = 1
    tmp_right = 1
    for i in range(n):
        if i==0:
            arr_left.append(tmp_left)
        if i==n-1:
            arr_right.append(tmp_right)
        tmp_left = 1
        arr_left.append(tmp)

print (multiple([1, 2, 3, 4, 5]))