# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def multiple(arr : list) -> list:
    print(arr)
    n = len(arr)
    arr_left = []
    tmp = 1
    for i in range(n):
        arr_left.append(tmp)
        tmp *= arr[i]
    # print(arr_left)

    arr_right = []
    tmp = 1
    for i in range(n):
        arr_right.insert(0, tmp)
        tmp *= arr[n-i-1]
    # print(arr_right)

    # products = []
    # for num1, num2 in zip(arr_left, arr_right):
    #     products.append(num1 * num2)
    # return products

    # better way
    return [a * b for a, b in zip(arr_left, arr_right)]

print (multiple([1, 2, 3, 4, 5]))