from typing import List

# See details here https://wenshengchen.com/2020/01/13/138-copy-list-with-random-pointer.html
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList2(self, head: 'Node') -> 'Node':
        if not head: return head

        hashmap = {}
        hashmap[None] = None
        walker = head

        while walker:
            hashmap[walker] = Node(walker.val)
            walker = walker.next

        walker = head
        while walker:
            node = hashmap[walker]
            node.next = hashmap[walker.next]
            node.random = hashmap[walker.random]
            walker = walker.next

        return hashmap[head]

    def copyRandomList(self, head: 'Node') -> 'Node':       
        if not head: return head

        walker = head
        while walker:
            next = Node(walker.val)
            next.next = walker.next
            walker.next = next
            walker = next.next

        walker = head
        while walker:
            walker.next.random = walker.random.next if walker.random else None
            walker = walker.next.next

        oldWalker = head
        head2 = head.next
        newWalker = head.next
        while oldWalker:
            oldWalker.next = oldWalker.next.next
            newWalker.next = newWalker.next.next if newWalker.next else None
            oldWalker = oldWalker.next
            newWalker = newWalker.next

        return head2

## Test Cases
test = Solution()
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

answer = test.copyRandomList(head)
assert answer.val == head.val
assert answer.random == head.random
assert answer.next.val == head.next.val
assert answer.next.random.val == head.next.random.val
assert answer.next.next.val == head.next.next.val
assert answer.next.next.random.val == head.next.next.random.val
assert answer.next.next.next.val == head.next.next.next.val
assert answer.next.next.next.random.val == head.next.next.next.random.val
assert answer.next.next.next.next.val == head.next.next.next.next.val
assert answer.next.next.next.next.random.val == head.next.next.next.next.random.val

head = Node(1)
head.next = Node(2)
head.random = head.next
head.next.random = head.next

answer = test.copyRandomList(head)
assert answer.val == head.val
assert answer.random.val == head.random.val
assert answer.next.val == head.next.val
assert answer.next.random.val == head.next.random.val

head = Node(3)
head.next = Node(3)
head.next.next = Node(3)
head.next.random = head

answer = test.copyRandomList(head)
assert answer.val == head.val
assert answer.random == head.random
assert answer.next.val == head.next.val
assert answer.next.random.val == head.next.random.val
assert answer.next.next.val == head.next.next.val
assert answer.next.next.random == head.next.next.random
print('All Passed!')
