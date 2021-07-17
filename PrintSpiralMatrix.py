# Print a matrix in spiral form
# Solution
# Print spiral matrix (m row x n column) with four direction RIGHT, DOWN, LEFT, UP and repeat the next loop inside
# Need to control the point printed and number of point print for each round of RIGHT, DOWN, LEFT and UP


def print_spiral_matrix(arr, m, n):
    # counting point printed
    k = 1
    # row i and j
    round = 0
    while k <= m*n:
        round += 1
        # calculate number point of RIGHT
        left_j = round
        right_j = n - round + 1
        down_i = m - round + 1
        up_i = round
        i = j = round
        print()
        print("Round {} - Left {} Right {} Down {} Up {}".format(round, left_j, right_j, down_i, up_i))
        # print to right
        while (j<=right_j) and (k <= m*n):
            # print("{} Round: {} RIGHT Row: {} - Column: {} ".format(k, round, i,j))
            print(arr[i - 1][j - 1], end=" ")
            k += 1
            j += 1
        # print down
        j -= 1
        i += 1
        while (i<=down_i) and (k <= m*n):
            # print("{} Round: {} DOWN Row: {} - Column: {} ".format(k, round, i,j))
            print(arr[i - 1][j - 1], end=" ")
            k += 1
            i += 1
        i -= 1
        j -= 1
        while (j>=left_j) and (k <= m*n):
            # print("{} Round: {} LEFT Row: {} - Column: {} ".format(k, round, i,j))
            print(arr[i - 1][j - 1], end=" ")
            k += 1
            j -= 1
        j += 1
        i -= 1
        while (i>up_i) and (k <= m*n):
            # print("{} Round: {} UP Row: {} - Column: {} ".format(k, round, i,j))
            print(arr[i - 1][j - 1], end=" ")
            k += 1
            i -= 1



# print_spiral_matrix([[1,2,3], [4,5,6], [7,8,9]], 3, 3)
print_spiral_matrix([[11,12,13,14,15,16,17], [21,22,23,24,25,26,27], [31,32,33,34,35,36,37], [41,42,43,44,45,46,47], [51,52,53,54,55,56,57]], 5, 7)