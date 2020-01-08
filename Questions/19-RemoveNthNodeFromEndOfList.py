from typing import List

# See details here https://wenshengchen.com/2020/01/07/19-remove-nth-node-from-end-of-list.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        walker = dummy
        walker2 = dummy

        while n:
            walker = walker.next
            n -= 1

        while walker.next:
            walker2 = walker2.next
            walker = walker.next

        walker2.next = walker2.next.next
        return dummy.next

## TEST CASES
test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

answer = test.removeNthFromEnd(head, 1)
assert answer.val == 1
assert answer.next.val == 2
assert answer.next.next.val == 3
assert answer.next.next.next.val == 4

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

answer = test.removeNthFromEnd(head, 2)
assert answer.val == 1
assert answer.next.val == 2
assert answer.next.next.val == 3
assert answer.next.next.next.val == 5

head = ListNode(1)
head.next = ListNode(2)

answer = test.removeNthFromEnd(head, 2)
assert answer.val == 2

head = ListNode(1)
answer = test.removeNthFromEnd(head, 1)
assert answer == None
print('All Passed!')
