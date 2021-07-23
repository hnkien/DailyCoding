# Returns true if there exists a subsequence of `A[0…n]` with the given sum
def subsetSum(A, n, sum, lookup):
    # return true if the sum becomes 0 (subset found)
    if sum == 0:
        return True

    # base case: no items left, or sum becomes negative
    if n < 0 or sum < 0:
        return False

    # construct a unique key from dynamic elements of the input
    key = (n, sum)

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
        # Case 1. Include the current item `A[n]` in the subset and recur
        # for the remaining items `n-1` with the decreased total `sum-A[n]`
        include = subsetSum(A, n - 1, sum - A[n], lookup)

        # Case 2. Exclude the current item `A[n]` from the subset and recur for
        # the remaining items `n-1`
        exclude = subsetSum(A, n - 1, sum, lookup)

        # assign true if we get subset by including or excluding the current item
        lookup[key] = include or exclude

    # return solution to the current subproblem
    return lookup[key]

if __name__ == '__main__':

    # Input: a set of items and a sum
    A = [7, 3, 2, 5, 8]
    sum = 14

    # create a dictionary to store solutions to subproblems
    lookup = {}

    if subsetSum(A, len(A) - 1, sum, lookup):
        print("Subsequence with the given sum exists")
    else:
        print("Subsequence with the given sum does not exist")



# Returns true if there exists a subsequence of the list with the given sum using bottom up
def subsetSum2(A, sum):
    n = len(A)

    # `T[i][j]` stores true if subset with sum `j` can be attained
    # using items up to first `i` items
    T = [[False for x in range(sum + 1)] for y in range(n + 1)]

    # if the sum is zero
    for i in range(n + 1):
        T[i][0] = True

    # do for i'th item
    for i in range(1, n + 1):
        # consider all sum from 1 to sum
        for j in range(1, sum + 1):
            # don't include the i'th element if `j-A[i-1]` is negative
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find the subset with sum `j` by excluding or including the i'th item
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]

    # return maximum value
    return T[n][sum]

