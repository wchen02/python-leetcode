# See details here https://wenshengchen.com/2019/12/18/328-odd-even-linked-list.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        even = head.next
        oddWalker, evenWalker = head, even

        while evenWalker and evenWalker.next:
                oddWalker.next = oddWalker.next.next
                oddWalker = oddWalker.next

                evenWalker.next = evenWalker.next.next
                evenWalker = evenWalker.next
        
        oddWalker.next = even
        return head

## TEST CASES
test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

answer = test.oddEvenList(head)
assert answer.val == 1
assert answer.next.val == 3
assert answer.next.next.val == 5
assert answer.next.next.next.val == 2
assert answer.next.next.next.next.val == 4

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

answer = test.oddEvenList(head)
assert answer.val == 1
assert answer.next.val == 3
assert answer.next.next.val == 5
assert answer.next.next.next.val == 2
assert answer.next.next.next.next.val == 4
assert answer.next.next.next.next.next.val == 6
print('All Passed!')