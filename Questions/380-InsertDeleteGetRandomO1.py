from typing import List
from random import randint

# See details here https://wenshengchen.com/2019/12/22/380-insert-delete-get-random-o1.html
class DblyLinkedListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class RandomizedSet:
    def __init__(self):
        self.size = 0
        self.valMap = {}
        self.indexMap = { self.size: DblyLinkedListNode(-1) }

    def insert(self, val: int) -> bool:
        if val in self.valMap:
            return False

        prev = self.indexMap[self.size]
        node = DblyLinkedListNode(val)
        prev.next = node
        node.prev = prev

        self.size += 1
        self.indexMap[self.size] = node
        self.valMap[val] = self.size
        return True

    def remove(self, val: int) -> bool:
        index = self.valMap.get(val)
        if index == None:
            return False
        
        tail = self.indexMap[self.size]
        node = self.indexMap[index]
        tail.prev.next = None
        tail.prev = node.prev
        tail.next = node.next
        self.indexMap[index] = tail
        self.valMap[tail.val] = index
        del self.indexMap[self.size]
        del self.valMap[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        rand = randint(1, self.size)
        return self.indexMap[rand].val

## TEST CASES
randomSet = RandomizedSet()
assert randomSet.insert(1) == True
assert randomSet.remove(2) == False
assert randomSet.insert(2) == True
rand = randomSet.getRandom()
assert rand == 1 or rand == 2
assert randomSet.remove(1) == True
assert randomSet.insert(2) == False
assert randomSet.getRandom() == 2

randomSet = RandomizedSet()
assert randomSet.remove(0) == False
assert randomSet.remove(0) == False
assert randomSet.insert(0) == True
assert randomSet.getRandom() == 0
assert randomSet.remove(0) == True
assert randomSet.insert(0) == True

randomSet = RandomizedSet()
assert randomSet.insert(0) == True
assert randomSet.insert(1) == True
assert randomSet.remove(0) == True
assert randomSet.insert(2) == True
assert randomSet.remove(1) == True
assert randomSet.getRandom() == 2, randomSet.getRandom()

randomSet = RandomizedSet()
assert randomSet.insert(1) == True
assert randomSet.insert(10) == True
assert randomSet.insert(20) == True
assert randomSet.insert(30) == True
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
rand = randomSet.getRandom()
print(rand)
assert rand == 1 or rand == 10 or rand == 20 or rand == 30
print('All Passed!')
