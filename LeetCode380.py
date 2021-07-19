# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet(object):

    def __init__(self):
        self.d = {}
        self.ar = []
        self.size = -1

    def insert(self, val):
        if (val not in self.d):
            self.size += 1
            self.d[val] = self.size
            self.ar.append(val)
            return True
        return False

    def remove(self, val):
        if (val in self.d):
            index = self.d[val]
            temp = self.ar[self.size]
            self.ar[self.size] = self.ar[index]
            self.ar[index] = temp
            self.d[self.ar[index]] = index
            self.ar.pop(self.size)
            del self.d[val]
            self.size -= 1
            return True
        return False

    def getRandom(self):
        return self.ar[random.randint(0, self.size)]
