from typing import List

# See details here https://wenshengchen.com/2019/12/21/251-flatten-2d-vector.html
class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.j = -1
        self.i = 0
        self.v = v

    def next(self) -> int:
        self.hasNext()
        self.j += 1
        return self.v[self.i][self.j]

    def hasNext(self) -> bool:
        if self.i >= len(self.v):
            return False
        
        if self.j+1 >= len(self.v[self.i]):
            self.i += 1
            self.j = -1
            return self.hasNext()
        else:
            return True

## TEST CASES
iterator = Vector2D([[1,2],[3],[4]])
assert iterator.next() == 1
assert iterator.next() == 2
assert iterator.next() == 3
assert iterator.hasNext() == True
assert iterator.hasNext() == True
assert iterator.next() == 4
assert iterator.hasNext() == False

iterator = Vector2D([[],[1]])
assert iterator.next() == 1
assert iterator.hasNext() == False

iterator = Vector2D([[1],[]])
assert iterator.next() == 1
assert iterator.hasNext() == False

iterator = Vector2D([[1,2],[],[3]])
assert iterator.hasNext() == True
assert iterator.hasNext() == True
assert iterator.next() == 1
assert iterator.next() == 2
assert iterator.next() == 3
assert iterator.hasNext() == False
print('All Passed!')
