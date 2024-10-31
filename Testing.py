def max_subarray_sum(input):
    n = len(input)
    max_number = 0
    max_ending_here = input[0]
    for i in range(1, n):
        max_ending_here = max(max_ending_here + input[i], input[i])
        if max_ending_here > max_number:
            max_number = max_ending_here
    return max_number

input = [-1, -3, 5, -4, 3, -6, 9, 2]
print(max_subarray_sum(input))




# import math
#
# def mean(x):
#     return sum(x) / len(x)
#
# def sd(x):
#     m = mean(x)
#     ss = sum((i - m) ** 2 for i in x)
#     return math.sqrt(ss / len(x))
#
# def corr(x, y):
#     n = len(x)
#     mean_x = mean(x)
#     mean_y = mean(y)
#
#     cov_xy = (sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))*1.0/n
#     sd_x = sd(x)
#     sd_y = sd(y)
#
#     corr_xy = cov_xy/(sd_x * sd_y)
#     return corr_xy

# X = [1, 3, 5, 7]
# Y = [2, 4, 6, 8]
# print(corr(X, Y))

# def pearson_correlation(x, x):
#     if len(x) != len(y):
#         raise ValueError("Lists X and Y must have the same length")
#
#     n = len(x)
#     mean_x = sum(x) / n
#     mean_y = sum(y) / n
#
#     numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
#     denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n))
#     denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n))
#     denominator = (denominator_x * denominator_y) ** 0.5
#
#     if denominator == 0:
#         return 0  # Tránh lỗi chia cho 0 khi các phần tử không có sự biến đổi
#
#     return numerator / denominator
#
#
# # Ví dụ sử dụng
# X = [1, 2, 3, 4, 5]
# Y = [5, 4, 3, 2, 1]
# print(pearson_correlation(X, Y))


# import math
# def smallest_multiple(n):
#     ans = 1
#     for i in range(1, n + 1):
#         ans = int((ans * i) / math.gcd(ans, i))
#     return ans


# def max_three(input):
#     input.sort()
#
#     max_product = input[-1] * input[-2] * input[-3]
#     if max_product > 0:
#         return max_product
#     else:
#         if input[-1] <= 0:
#             return input[0] * input[1] * input[2]
#         else:
#             return input[-1] * input[0] * input[1]



# def intToRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90,
#            100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL",
#            "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = 12
#     result = ""
#
#     while number:
#         div = number // num[i]
#         number %= num[i]
#
#         while div:
#             result += sym[i]
#             div -= 1
#         i -= 1
#
#     return result
#
# print(intToRoman(30))

# def maxMatrixSum(matrix):
#     totalRows = len(matrix)
#     cols = len(matrix[0])
#
#     def helper(row, visitedColumns):
#         if row == totalRows:
#             return 0  # Base case: no more rows to process
#
#         maxSum = float('-inf')  # Initialize maxSum to the smallest possible value
#
#         for col in range(cols):
#             if col not in visitedColumns:  # Avoid using the same column
#
#                 visitedColumns.append(col)
#
#                 currentSum = matrix[row][col] + helper(row + 1, visitedColumns)
#                 if currentSum > maxSum:
#                     maxSum = currentSum  # Update maxSum with the highest value
#
#                 visitedColumns.remove(col)
#
#         return maxSum
#
#     return helper(0, [])

# def maxMatrixSum(matrix):
#     totalRows = len(matrix)
#     cols = len(matrix[0])
#
#     def helper(row, visitedColumns):
#         if row == totalRows:
#             return 0  # Base case: no more rows to process
#
#         maxSum = float('-inf')  # Initialize maxSum to the smallest possible value
#
#         for col in range(cols):
#             if col not in visitedColumns:  # Avoid using the same column
#                 newVisitedColumns = visitedColumns.copy()
#                 newVisitedColumns.append(col)
#
#                 currentSum = matrix[row][col] + helper(row + 1, newVisitedColumns)
#                 if currentSum > maxSum:
#                     maxSum = currentSum  # Update maxSum with the highest value
#
#         return maxSum
#
#     return helper(0, [])


# def maxMatrixSum(matrix):
#     n = len(matrix)
#     full_mask = (1 << n) - 1  # All bits set for n items
#     dp = [-1] * (1 << n)  # DP array to store the max sums for each subset mask
#
#     def dfs(row, mask):
#         if mask == full_mask:  # Base case: all rows are used
#             return 0
#         if dp[mask] != -1:  # If already computed
#             return dp[mask]
#
#         max_sum = 0
#         for col in range(n):
#             if not (mask & (1 << col)):  # If col is not used in the current mask
#                 # Try picking matrix[row][col] and add its value to the solution
#                 new_sum = matrix[row][col] + dfs(row + 1, mask | (1 << col))
#                 max_sum = max(max_sum, new_sum)
#
#         dp[mask] = max_sum  # Memoize the result
#         return dp[mask]
#
#     return dfs(0, 0)


# def maxMatrixSum(matrix):
#     n = len(matrix)
#     memo = {}
#
#     def dfs(row, visited):
#         if row == n:  # All rows have been processed
#             return 0
#         if (row, tuple(visited)) in memo:
#             return memo[(row, tuple(visited))]
#
#         max_sum = 0
#         for col in range(n):
#             if not visited[col]:  # Check if the column is unvisited
#                 visited[col] = True  # Mark the column as visited
#                 current_sum = matrix[row][col] + dfs(row + 1, visited)  # Recur for the next row
#                 max_sum = max(max_sum, current_sum)  # Take the maximum sum
#                 visited[col] = False  # Backtrack by unmarking the column
#
#         memo[(row, tuple(visited))] = max_sum
#         return max_sum
#
#     return dfs(0, [False] * n)


# print(maxMatrixSum([[-5,2,3,4],[6,7,8,9],[10,-1,12,13],[14,15,-4,16]]))

# def isPalindrome(phrase):
# 	n = len(phrase)
# 	j = n - 1
# 	i = 0
# 	while (i < j):
# 		if (not phrase[i].isalnum()):
# 			i += 1
# 		if phrase[i].isspace():
# 			i += 1
# 		if (not phrase[j].isalnum()):
# 			j -= 1
# 		if phrase[j].isspace():
# 			j -= 1
# 		if phrase[i].lower() == phrase[j].lower():
# 			i += 1
# 			j -= 1
# 		else:
# 			return False
# 	return True
#
# phrase = 'Yo! Banana boy.'
# print(isPalindrome(phrase))

# def generate(numRows):
# 	result = []
# 	last_row = []
# 	for i in range(numRows):
# 		if (len(last_row) == 0):
# 			result.append([1])
# 			last_row = [1]
# 		else:
# 			temp_row = [1]
# 			for j in range(len(last_row) - 1):
# 				temp_row.append(last_row[j] + last_row[j + 1])
# 			temp_row.append(1)
# 			result.append(temp_row)
# 			last_row = temp_row
# 	return result

# print(generate(5))


# roman_map = {
#         'I': 1, 'V': 5, 'X': 10,
#         'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }
#
# # Initialize result
# sum = 0
# i = 0
# while i < len(s):
#     if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
#         sum += roman_map[s[i + 1]] - roman_map[s[i]]
#         i += 2
#     else:
#         sum += roman_map[s[i]]
#         i += 1
#
# return sum


# from collections import deque
#
#
# def min_steps_bfs(N):
#     # BFS initialization
#     queue = deque([(N, 0)])  # (current_number, steps_count)
#     parent = {N: None}  # To track the parent number for each number
#     visited = set([N])  # To avoid revisiting numbers
#
#     # BFS loop
#     while queue:
#         current, steps = queue.popleft()
#
#         # If we've reached 1, reconstruct the path and return the result
#         if current == 1:
#             path = []
#             while current is not None:
#                 path.append(current)
#                 current = parent[current]
#             path.reverse()  # Reverse to get the path from N to 1
#             return steps, path
#
#         # Option 1: Decrement the current number
#         if current - 1 not in visited:
#             visited.add(current - 1)
#             queue.append((current - 1, steps + 1))
#             parent[current - 1] = current  # Keep track of how we reached this state
#
#         # Option 2: Replace current with the largest divisor (larger between a and b where a * b = current)
#         for i in range(2, int(current ** 0.5) + 1):
#             if current % i == 0:
#                 # Replace with divisor i
#                 # if i not in visited:
#                 #     visited.add(i)
#                 #     queue.append((i, steps + 1))
#                 #     parent[i] = current
#
#                 # Replace with current // i (other divisor)
#                 other_divisor = current // i
#                 if other_divisor not in visited:
#                     visited.add(other_divisor)
#                     queue.append((other_divisor, steps + 1))
#                     parent[other_divisor] = current
#
#
# # Example usage
# N = 101
# steps_needed, path = min_steps_bfs(N)
# print(f"Minimum steps to reduce {N} to 1: {steps_needed}")
# print(f"Path: {path}")


# def min_steps_to_one_dp(N):
#     # Initialize dp and parent arrays
#     dp = [float('inf')] * (N + 1)
#     parent = [0] * (N + 1)  # This will store the number from which 'i' was reached
#
#     dp[1] = 0  # Base case: It takes 0 steps to reduce 1 to 1
#
#     for i in range(2, N + 1):
#         # Option 1: Decrementing by 1
#         if dp[i] > dp[i - 1] + 1:
#             dp[i] = dp[i - 1] + 1
#             parent[i] = i - 1  # We came to 'i' from 'i - 1'
#
#         # Option 2: Replacing with larger factor
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 # if dp[i] > dp[j] + 1:  # From factor j
#                 #     dp[i] = dp[j] + 1
#                 #     parent[i] = j
#
#                 if dp[i] > dp[i // j] + 1:  # From factor i // j
#                     dp[i] = dp[i // j] + 1
#                     parent[i] = i // j
#
#     # Reconstruct the path of steps
#     steps = []
#     current = N
#     while current > 0:
#         steps.append(current)
#         current = parent[current]
#
#     steps.reverse()  # Reverse to get the path from N to 1
#     return dp[N], steps
#
#
# # Example usage
# N = 100
# steps_needed, path = min_steps_to_one_dp(N)
# print("Minimum steps to reduce", N, "to 1:", steps_needed)
# print("Path:", path)


# from collections import deque
#
# def min_steps_to_one(N):
#     # BFS initialization
#     queue = deque([(N, 0)])  # (current number, steps taken)
#     visited = set([N])  # To keep track of visited numbers
#
#     while queue:
#         current, steps = queue.popleft()
#
#         # If we've reached 1, return the steps count
#         if current == 1:
#             return steps
#
#         # Option 1: Decrement by 1
#         if current - 1 not in visited:
#             visited.add(current - 1)
#             queue.append((current - 1, steps + 1))
#
#         # Option 2: Check for factorization
#         for i in range(2, int(current ** 0.5) + 1):
#             if current % i == 0:  # i * (current // i) = current
#                 larger_factor = current // i
#                 if larger_factor not in visited:
#                     visited.add(larger_factor)
#                     queue.append((larger_factor, steps + 1))
#
# # Example usage:
# N = 100
# print(min_steps_to_one(N))  # Output: 4 (10 -> 5 -> 4 -> 2 -> 1)


# def min_steps_to_one_dp(N):
#     # Initialize dp array, where dp[i] is the minimum steps to reduce i to 1
#     dp = [float('inf')] * (N + 1)
#     dp[1] = 0  # Base case: It takes 0 steps to reduce 1 to 1
#
#     for i in range(2, N + 1):
#         # Option 1: Decrementing by 1
#         dp[i] = dp[i - 1] + 1
#
#         # Option 2: Replacing with larger factor
#         for j in range(1, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 # dp[i] = min(dp[i], dp[j] + 1)  # Factor j
#                 dp[i] = min(dp[i], dp[i // j] + 1)  # Factor i // j
#
#     return dp[N]
#
# # Example usage
# N = 100
# print(min_steps_to_one_dp(N))  # Output: 4


# from collections import deque
# def interleave_stack(stack):
#     if len(stack) <= 1:
#         return stack
#
#     # Initialize a queue
#     queue = deque()
#     n = len(stack)
#     half = n // 2
#
#     # Step 1: Move all elements from the stack to the queue
#     while stack:
#         queue.append(stack.pop())
#
#     # Step 2: Push the first half back to the stack
#     for _ in range(half):
#         stack.append(queue.pop())
#
#     # Step 3: Interleave elements from the stack and queue
#     for _ in range(half):
#         queue.append(stack.pop())  # Put the first half back in reverse order
#
#     # Now, interleave from the queue
#     while queue:
#         stack.append(queue.popleft())  # First half
#         if queue:
#             stack.append(queue.popleft())  # Second half
#
#     return stack
#
#
# # Example usage
# stack = [1, 2, 3, 4, 5]
# print("Original Stack:", stack)
# interleave_stack(stack)
# print("Interleaved Stack:", stack)


# import re
# chuoi = "The swordfish is a keyworde for this sword."
# ket_qua = re.findall(r'\Bword\B', chuoi)
# print(ket_qua)

# chuoi = "Phạm vi từ 10-20 và 30-40."
# ket_qua = re.findall(r'(\d+)-(\d+)', chuoi)
# print(ket_qua)


# chuoi = "Giá là 100 USD, 200 EUR, và 300 JPY."
# # ket_qua = re.findall(r'\d+(?= USD)', chuoi)
# # print(ket_qua)
#
# ket_qua = re.findall(r'\b\d+\b(?! USD)', chuoi)
# print(ket_qua)


# chuoi = "Giá là USD 100 và EUR 200."
# ket_qua = re.findall(r'(?<=USD )\d+', chuoi)
# print(ket_qua)
#
#
# ket_qua = re.findall(r'(?<!USD )\d+', chuoi)
# print(ket_qua)


# import sys
#
# # Hàm kiểm tra hệ thống có phải là Little Endian hay không
# def is_little_endian():
#     return sys.byteorder == 'little'
#
# # Hàm chuyển đổi Little Endian sang Big Endian và ngược lại
# def swap_endian(num):
#     return ((num >> 24) & 0x000000FF) | \
#            ((num >> 8)  & 0x0000FF00) | \
#            ((num << 8)  & 0x00FF0000) | \
#            ((num << 24) & 0xFF000000)
#
# # Kiểm tra hệ thống
# if is_little_endian():
#     print("System is Little Endian")
# else:
#     print("System is Big Endian")
#
# # Thử chuyển đổi Endian
# x = 0x12345678
# print(f"Original: 0x{x:08X}")
# swapped = swap_endian(x)
# print(f"Swapped: 0x{swapped:08X}")


# a = [1, 2, 3, 4, 5]
# b = a.pop()
# print(b)
# a.append(6)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)

# a = "Hello World"
# b = a[1:5]
# print(b)

# import random
# print(random.randint(0,9))


# import heapq
# h = []
# print(h is None)
# heapq.heappush(h, 5)
# heapq.heappush(h, 7)
# heapq.heappush(h, 1)
# heapq.heappush(h, 3)
# print(heapq.heappop(h))
# print(h[0])
# print(heapq.heappop(h))

# import heapq
# class RoomTime:
#     def __init__(self, st, et):
#         self.start = st
#         self.end = et
#
#     def __str__(self):
#         return "{} -> {}".format(self.start, self.end)
#
#     def __lt__(self, other):
#         return self.start <= other.start
#
# rt1 = RoomTime(0, 30)
# rt2 = RoomTime(5, 10)
# rt3 = RoomTime(15, 20)
# rt = [rt1, rt2, rt3]
# heapq.heapify(rt)
# print(rt1)
# for x in rt:
#     print(x)


# import heapq as hq
# # the dictionary to be as heap
# my_dict = {'z': 'zebra', 'b': 'ball', 'w': 'whale',
# 		'a': 'apple', 'm': 'monkey', 'c': 'cat'}
# # conversion to tuple
# my_list = [(k, v) for k, v in my_dict.items()]
# print("Before organizing as heap :", my_list)
# # arrange as min-heap
# hq.heapify(my_list)
# print("After organizing as heap :", my_list)
# # re convert to dictionary
# my_dict = dict(my_list)
# print("Resultant dictionary :", my_dict)


# f = open("Testing2.py", "r", encoding="utf-8")
# for line in f:
#     print(line)
#


# a = {"1": "a", "2": "b", "3": "c"}
# print("1" in a)
# print("4" in a)
# print("a" in a)


# a= "alice,20,800,mtv"
# b=a.split(",")
# print(b)
# print(type(b))
# print(hash(a))

# t = ('a', 'b', 'c', 'd', 'e')
# print(id(t))
#
# t = ('A',) + t[1:]
# print(t) #should print ('A', 'b', 'c', 'd', 'e')
# print(id(t))


# values = [(x,y) for x in range(5) for y in range(3)]
# values = [[y*3 for y in range(x)] for x in range(5)]
# values = {x*x for x in range(5)}
# values = {x: pow(10, x) for x in range(5)}
# print(type(values))
# print(values)


# scores = [('John', 95), ('Danny', 98), ('Aaron', 90), ('Leo', 94)]
# a= sorted(scores, reverse=True)
# print(a)
# b= sorted(scores, key=lambda x: x[1], reverse=True)
# print(b)


# limit = 10
# # Use a generator function
# def integer_generator():
#     n = 0
#     while n < limit:
#         n += 1
#         yield n
# int_gen = integer_generator()
# int_sum0 = sum(int_gen)
# print(int_sum0)
#
# # Use generator expression
# int_sum1 = sum(x for x in range(1, limit+1))
# print(int_sum1)


# board = [[-1 for i in range(8)] for i in range(8)]
# print(board)

# a = [1,2,3,4]
# print(*a)

# a = "HelloWorld"
# b = "#" + "#".join(a) + "#"
# print(b)


# import heapq
# a = [3, 5, 1, 2, 6, 8, 7]
# heapq.heapify(a)
# print(a)
#
# b = heapq.heappop(a)
# print(b)
# print(a)
#
# heapq.heappush(a, 4)
# print(a)
#
# results="""\
# Christania Williams      11.80
# Marie-Josee Ta Lou       10.86
# Elaine Thompson          10.71
# Tori Bowie               10.83
# Shelly-Ann Fraser-Pryce  10.86
# English Gardner          10.94
# Michelle-Lee Ahye        10.92
# Dafne Schippers          10.90
# """
# top_3 = heapq.nsmallest(3, results.splitlines(), key=lambda x: float(x.split()[-1]))
# print("\n".join(top_3))


# lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
# heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
# print(heap)


# import heapq
#
# class DataWrap:
#     def __init__(self, data):
#         self.data = data
#
#     def __lt__(self, other):
#         return len(self.data) < len(other.data)  # Create list of strings
#
# my_strings = ["write", "go", "run", "come"]  # Initialising
# sorted_strings = []  # Wrap strings and push to heap
# for s in my_strings:
#     heapObj = DataWrap(s)
#     heapq.heappush(sorted_strings, heapObj)  # Print the heap
#
# for myObj in sorted_strings:
#     print(myObj.data, end=" ")


# irregular_list = [[1, 2, 3], [3, 6, 7], [7, 5, 4],7]
# # Using lambda arguments: expression
# flatten_list = lambda irregular_list:[element for item in irregular_list for element in flatten_list(item)] if type(irregular_list) is list else [irregular_list]
#
# print("Original list ", irregular_list)
# print("Transformed List ", flatten_list(irregular_list))


# import random
# for i in range(100):
#     print(random.randint(5,10), end=' ')

#
# def function(a):
#     return a*a
#
# x = map(function, (1,2,3,4))  #x is the map object
# print(x)
# print(type(x))
#
# z= list(x)
# print(type(z))
# print(z)
#
# # Note: x only dispatch once time, y variable below is None
# y = set(x)
# print(type(y))
# print(y)
#
#
# tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
# newtuple = tuple(map(lambda x: x+3 , tup))
# print(newtuple)
#
#
# def func(x):
#     if x>=3:
#         return x
# y = filter(func, (1,2,3,4))
# print(y)
# print(list(y))
#
#
# from functools import reduce
# reduce(lambda a,b: a+b,[23,21,45,98])
#
#
# double = lambda x: x * 2
# print(double(10))
#
# sequences = [10,2,8,7,5,4,3,11,0, 1]
# filtered_answer = filter (lambda x: x > 6, sequences)
# print(list(filtered_answer))
#


# from queue import LifoQueue
# s = LifoQueue()
# s.put("1")
# s.put("2")
# s.put("3")
# s.put("4")
# print(s.get())
# print(s.get())
# print(s.get())
# print(s.get())
# print(s.get())
#
#
# from collections import deque
# q = deque()
#
# q.append('eat')
# q.append('sleep')
# q.append('code')
#
# print(q)
# # while len(q)>0:
# #     print(q.pop())
#
# while len(q)>0:
#     print(q.popleft())


# nested_list = [['cherry', 7], ['apple', 1000], ['anaconda', 160]]
#
# a = max(nested_list, key=lambda x: x[1])
# print(a)
#
# b = min(nested_list, key=lambda x: x[1])
# print(b)
#
# print(nested_list)
# c = sorted(nested_list, key=lambda x: x[1])
# print(c)


# a = [1,2,3,4,5,6,7,8,9,10]
# b = sum([i for i in a if i % 2 ==0 and i> 4])
# print(b)
#
# num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(num_list)
#
# obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# print(obj)

#
# # Transpose of Matrix using Nested Loops
# transposed = []
# matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
#
# for i in range(len(matrix[0])):
#     transposed_row = []
#
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)


# Transpose of a Matrix using List Comprehension
# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# transpose = [[row[i] for row in matrix] for i in range(2)]
# print (transpose)


# import queue
# a = queue.Queue()
# a.put(1)
# a.put(2)
# a.put(3)
# while not a.empty():
#     print(a.get())

# import queue
# a = queue.LifoQueue()
# a.put(1)
# a.put(2)
# a.put(3)
# while not a.empty():
#     print(a.get())


# import sys
# print(sys.maxsize)


# from itertools import chain
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]
# l = chain (l1,l2,l3)
# print(type(l))
# print (l)
#
# for i in chain(l1, l2, l3):
#     print(i) # 1,2,3,4,5,6,7,8,9
#
# print(list(chain(l1, l2, l3))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(chain(l1, l2, l3))) # 45


# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in zip(*lst):
#     print(i)
# # (1, 4, 7)
# # (2, 5, 8)
# # (3, 6, 9)


# from operator import add
#
# print([i for i in map(pow, (2,3,10), (5,2,3))])
# # [32, 9, 1000]
#
# print([i for i in map(add, map(pow, (2,3,10), (5,2,3)), (2,2,2))])
# # [34, 11, 1002]


# from itertools import islice
# a = range(10)
# i = iter(a)
# print(list(islice(i, 1, 3))
# print(list(islice(i, 1, 3))
# print(list(islice(i, 1, 3))
# print(list(islice(i, 1, 3))
# #[1, 2]
# #[4, 5]
# #[7, 8]
# #[]


# names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob']
# s = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
# print(s)

# dct = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# freq_dict = {k.lower() : dct.get(k.lower(), 0) + dct.get(k.upper(), 0) for k in dct.keys()}
# print(freq_dict)
# # {'a': 17, 'z': 3, 'b': 34}


# numbers = [0, 1, 2, 3, 4]
# squared_numbers_map = list(map(lambda x: x**2, numbers))
# # for num in enumerate(squared_numbers_map):
# #     print(num)
#
# for num in enumerate(numbers):
#     print(num)
#     print(type(num))


# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(lambda s: s[::-1], animals)
# a = list(iterator)
# print(a)


# def median_of_medians(nums, start, end, k):
#     """
#     Tìm phần tử thứ K nhỏ nhất trong đoạn con từ nums[start] đến nums[end]
#     """
#     if end - start <= 5:
#         nums[start:end + 1] = sorted(nums[start:end + 1])
#         return nums[start + k - 1]
#
#     # Chia thành các nhóm 5 phần tử
#     medians = []
#     for i in range(start, end + 1, 5):
#         group = nums[i:min(i + 5, end + 1)]
#         group.sort()
#         medians.append(group[len(group) // 2])
#
#     # Tìm trung vị của các trung vị
#     pivot = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2 + 1)
#
#     # Phân hoạch (in-place)
#     low = []
#     high = []
#     pivot_list = []
#
#     for i in range(start, end + 1):
#         if nums[i] < pivot:
#             low.append(nums[i])
#         elif nums[i] > pivot:
#             high.append(nums[i])
#         else:
#             pivot_list.append(nums[i])
#
#     # Xử lý đệ quy theo các trường hợp
#     if k <= len(low):
#         return median_of_medians(low, 0, len(low) - 1, k)
#     elif k <= len(low) + len(pivot_list):
#         return pivot
#     else:
#         return median_of_medians(high, 0, len(high) - 1, k - len(low) - len(pivot_list))
#
#
# def find_kth_smallest(nums, k):
#     """
#     Tìm phần tử thứ K nhỏ nhất trong danh sách
#     """
#     return median_of_medians(nums, 0, len(nums) - 1, k)
#
#
# # Ví dụ
# nums = [3, 7, 8, 5, 2, 1, 9, 6, 4]
# k = 3
# result = find_kth_smallest(nums, k)
# print("Phần tử thứ", k, "nhỏ nhất là:", result)


# import csv_to_sqlite
#
# # all the usual options are supported
# options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
# input_files = ["/Users/hypercloud/Downloads/Testing/TuDien/dictionary.csv"] # pass in a list of CSV files
# csv_to_sqlite.write_csv(input_files, "/Users/hypercloud/Downloads/Testing/TuDien/english_dict.sqlite", options)


# import sqlite3
# import json
#
# conn = sqlite3.connect('english_ordia.db')
# conn.execute("CREATE TABLE dictionary (english text, ordia text);")
# with open('/Users/hypercloud/Downloads/Testing/TuDien/En-Or_word_pairs.json', 'r') as json_file:
#     data = json.load(json_file)
#     i = 0
#     print(type(data))
#     for key in data:
#         if key and data[key]:
#             i += 1
#             # print(key)
#             # print(data[key])
#             # if i > 10:
#             #     break
#
#             conn.execute("INSERT INTO dictionary (english, ordia) VALUES (?, ?)", (key, data[key]))
#     print(i)
# conn.commit()
# conn.close()


# import sqlite3
#
# conn = sqlite3.connect('english_spanish.db')
# conn.execute("CREATE TABLE dictionary (english text, spanish text);")
# with open('/Users/hypercloud/Downloads/Testing/TuDien/EnglishSpanish.txt', 'r') as text_file:
#     lines = text_file.readlines()
#     count = 0
#     # Strips the newline character
#     for line in lines:
#         count += 1
#         # print("Line{}: {}".format(count, line.strip()))
#         parts = line.split("\t")
#         print(parts)
#         conn.execute("INSERT INTO dictionary (english, spanish) VALUES (?, ?)", (parts[0], parts[1]))
#         # if count > 20:
#         #     break
#
# print(count)
# conn.commit()
# conn.close()

#
# import sqlite3
# conn = sqlite3.connect('persian_english.db')
# conn.execute("CREATE TABLE dictionary (persian text, english text);")
#
# with open('/Users/hypercloud/Downloads/Testing/TuDien/EnglishPersian.txt', 'r') as text_file:
#     lines = text_file.readlines()
#     count = 0
#     # Strips the newline character
#     for line in lines:
#         # print("Line{}: {}".format(count, line.strip()))
#         parts = line.split("|")
#         if len(parts) <2:
#             continue
#
#         # print(parts)
#         count += 1
#         english = parts[1].strip()
#         persian = parts[2].strip()
#         print(english, ':', persian)
#         conn.execute("INSERT INTO dictionary (persian, english) VALUES (?, ?)", (persian, english))
#         # if count > 50:
#         #     break
#
# print(count)
# conn.commit()
# conn.close()
