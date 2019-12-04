# See details here https://wenshengchen.com/2019/12/04/206-reverse-linked-list.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        oldHead = head
        newHead = head.next
        oldHead.next = None

        while newHead:
            newHead2 = newHead.next
            newHead.next = oldHead
            oldHead = newHead
            newHead = newHead2
        
        return oldHead
        
## TEST CASES
test = Solution()
testHead = ListNode(1)
testHead.next = ListNode(2)
testHead.next.next = ListNode(3)
answer = test.reverseList(testHead)
assert answer.val == 3
assert answer.next.val == 2
assert answer.next.next.val == 1

answer = test.reverseList(None)
assert answer == None
print('All Passed!')
