from typing import List

# See details here https://wenshengchen.com/2019/12/04/412-fizz-buzz.html
class Vector2D:
    ptr, stk, v

    def __init__(self, v: List[List[int]]):
        self.ptr = 0
        self.stk = [v[ptr]]
        self.v = v

    def next(self) -> int:
        self.hasNext()

    def hasNext(self) -> bool:
        if not stk:
            if ptr < len(v) - 1:
                ptr += 1


## TEST CASES
Vector2D iterator = Vector2D([[1,2],[3],[4]]);

assert iterator.next() == 1
assert iterator.next() == 2
assert iterator.next() == 3
assert iterator.hasNext() == True
assert iterator.hasNext() == True
assert iterator.next() == 4
assert iterator.hasNext() == False
print('All Passed!')
