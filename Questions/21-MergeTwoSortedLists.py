from typing import List

# See details here https://wenshengchen.com/2020/02/17/23-merge-k-sorted-lists.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        walker = l3

        while l1 and l2:
            if l1.val < l2.val:
                walker.next = ListNode(l1.val)
                l1 = l1.next
            else:
                walker.next = ListNode(l2.val)
                l2 = l2.next
            walker = walker.next

        walker.next = l1 if l1 is not None else l2

        return l3.next

## TEST CASES
test = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = test.mergeTwoLists(l1, l2)
assert l3.val == 1
assert l3.next.val == 1
assert l3.next.next.val == 2
assert l3.next.next.next.val == 3
assert l3.next.next.next.next.val == 4
assert l3.next.next.next.next.next.val == 4
print('All Passed!')
