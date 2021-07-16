# This problem was asked by Google.
#
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#
# In this example, assume nodes with the same value are the exact same node objects.
#
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_nodes(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes

    def get_length(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def add_node(self, node):
        node.next = self.head
        self.head = node


def intersect_linkedlist(list1, list2):
    node1 = list1.head
    node2 = list2.head

    len1 = list1.get_length()
    len2 = list2.get_length()

    if len1 > len2:
        k = len1 - len2
        while k > 0 and node1 is not None:
            node1 = node1.next
            k -= 1
    elif len2 > len1:
        k = len2 - len1
        while k > 0 and node2 is not None:
            node2 = node2.next
            k -= 1

    while (node1 is not None) and (node2 is not None) and (node1.data != node2.data):
        node1 = node1.next
        node2 = node2.next

    return node1.data

my_list1 = LinkedList()
my_list1.add_node(Node("10"))
my_list1.add_node(Node("8"))
my_list1.add_node(Node("7"))
my_list1.add_node(Node("3"))

my_list2 = LinkedList()
my_list2.add_node(Node("10"))
my_list2.add_node(Node("8"))
my_list2.add_node(Node("99"))

print(intersect_linkedlist(my_list1, my_list2))
