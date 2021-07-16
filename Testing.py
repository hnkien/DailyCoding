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

# a= "HelloWorld"
# print("#".join(a))


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

import random
for i in range(100):
    print(random.randint(5,10), end=' ')