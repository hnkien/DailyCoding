a = [1, 2, 3, 4, 5]
b = a.pop()
print(b)
a.append(6)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

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



