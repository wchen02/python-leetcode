# See details here https://wenshengchen.com/2019/12/06/237-delete-node-in-a-linked-list.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None: 
        if node.next:
            node.val = node.next.val 
            node.next = node.next.next 

## TEST CASES
test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
test.deleteNode(head)
assert head.val == 2
assert head.next.val == 3
assert head.next.next.val == 4

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
test.deleteNode(head.next)
assert head.val == 1
assert head.next.val == 3
assert head.next.next.val == 4

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
test.deleteNode(head.next.next)
assert head.val == 1
assert head.next.val == 2
assert head.next.next.val == 4

head = ListNode(1)
head.next = ListNode(2)
test.deleteNode(head)
assert head.val == 2
print('All Passed!')
