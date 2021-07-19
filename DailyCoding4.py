# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def first_missing_integer(arr):
    arr = [a for a in arr if a>0]
    l = len(arr)
    # print(l)
    brr = [i+1 for i in range (l+1)]

    for a in arr:
        if a < l+1:
            brr[a-1] = 0

    for b in brr:
        if b != 0:
            return b

    return b[l]

print (first_missing_integer([3,4,-1,1]))
print (first_missing_integer([1,2,0]))