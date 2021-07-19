class Stack:
    def __init__(self, n):
        self.size = n
        self.top = -1
        self.data = []

    def pop(self):
        if not self.is_empty():
            item = self.data[self.top]
            self.data.pop(self.top)
            self.top -= 1
            return item
        else:
            return None

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, item):
        if self.is_full():
            return False
        else:
            self.top += 1
            # print(self.top)
            self.data.append(item)
            return True

    def is_full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.data[self.top]
        else:
            return None


    def reverse(self):
        aLL = LinkedList(None)
        while not self.is_empty():
            aNode = Node(self.pop())
            aLL.insertNode(aNode)
        llNode = aLL.head
        while llNode is not None:
            self.push(llNode.data)
            llNode = llNode.next



class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head

    def traverseList(self):
        llNode = self.head
        while llNode is not None:
            print(llNode.data, end=" ")
            llNode = llNode.next

    def insertNode(self, node):
        node.next = self.head
        self.head = node


if __name__ == "__main__":
    aStack = Stack(5)

    aStack.push(1)
    aStack.push(2)
    aStack.push(3)

    # while not aStack.is_empty():
    #     print(aStack.pop())

    aStack.push(4)
    aStack.push(5)

    # while not aStack.is_empty():
    #     print(aStack.pop())

    aStack.push(6)
    aStack.push(7)

    # print(aStack.peek())

    aStack.reverse()
    while not aStack.is_empty():
        print(aStack.pop())
