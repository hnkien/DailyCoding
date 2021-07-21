class DataWrap:

    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return len(self.data) > len(other.data)

import heapq
# Create list of strings
my_strings = ["write", "go", "run", "come"]
# Initialising
sorted_strings = []
# Wrap strings and push to heap
for s in my_strings:
    heapObj = DataWrap(s)
    heapq.heappush(sorted_strings, heapObj)
# Print the heap
for myObj in sorted_strings:
    print(myObj.data, end="\t")