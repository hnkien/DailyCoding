# Given a linkedlist, remove the duplicate element from the list
# 1->2->3->2->4 to 1->2->3->4

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node

    def addNode(self, data):
        aNode = Node(data)
        aNode.next = self.head
        self.head = aNode

    def printList(self):
        aNode = self.head
        while aNode is not None:
            print("{0} -> ".format(aNode.data), end="" )
            aNode = aNode.next

    def dedupList(self):
        aSet = set()
        # aNode = self.head
        preNode = self.head
        aNode = preNode.next
        while aNode is not None:
            if aNode.data in aSet:
                aNode = aNode.next
            else:
                aSet.add(aNode.data)
                preNode.next =aNode
                preNode = aNode
                aNode = aNode.next

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(2)
    n5 = Node(3)
    n6 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    ll = LinkedList(n1)
    ll.printList()
    print()
    ll.dedupList()
    ll.printList()