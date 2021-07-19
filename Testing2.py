class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue implementation in Python

class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

class LinkedList:
    def __init__(self):
        self.head = None


linked_list = LinkedList()
node1 = Node(1)
linked_list.head = node1
second = Node(2)
third = Node(3)

# Connect nodes
linked_list.head.next = second
second.next = third

# Print the linked list item
while linked_list.head != None:
    print(linked_list.head.data, end=" ")
    linked_list.head = linked_list.head.next



# s = "HelloWorld"
# i = s[::-1]
# print(i)
#
# def factorial(n):
#     fac = 1
#     for i in range(2,n+1):
#         fac = fac * i
#     return fac
# print(factorial(5))


# d = { 'a': 1, 'b' : 2, 'c': 3}
# print(d.get('a'))
#
# print(d.get('d'))
# d['a'] = 3
# print(d.get('a'))

# s = "Cong Hoa Xa Hoi Chu Nghi Viet Nam"
# lst = s.split()
# print(lst)



# def check_unique_string(s):
#     m = len(s)
#     a = [i for i in s]
#     b = set(a)
#     print(a)
#     print(b)
#     n= len(b)
#     if m == n:
#         return True
#     else:
#         return False
#
# print(check_unique_string("hello"))
# print(check_unique_string("helo"))


