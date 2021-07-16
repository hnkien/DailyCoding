import heapq
import itertools

'''
    heapq library of python - https://docs.python.org/2/library/heapq.html
'''

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.frequency)
        inorder(root.right)

class Node():
    def __init__(self, d, f):
        self.data = d
        self.frequency = f
        self.left = None
        self.right = None

def greedy_huffman():
    while(len(pq) > 1):
        left = pop_task()
        right = pop_task()
        freq = left.frequency + right.frequency
        z = Node(None, freq)
        z.left = left
        z.right = right
        add_task(z, z.frequency)

    return pop_task()

if __name__ == '__main__':
    a = Node('a', 42)
    b = Node('b', 20)
    c = Node('c', 5)
    d = Node('d', 10)
    e = Node('e', 11)
    f = Node('f', 12)

    add_task(a, a.frequency)
    add_task(b, b.frequency)
    add_task(c, c.frequency)
    add_task(d, d.frequency)
    add_task(e, e.frequency)
    add_task(f, f.frequency)

    tree = greedy_huffman()
    inorder(tree)