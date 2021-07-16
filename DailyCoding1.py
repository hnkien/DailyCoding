# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def check_sum(arr:list, k:int) -> int:
    arr_set = set()
    for i in arr:
        if i in arr_set:
            return (True, k-i, i)
        else:
            arr_set.add(k-i)
    return (False, k, 0)


print (check_sum([10, 15, 3, 7], 17))
