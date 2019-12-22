# See details here https://wenshengchen.com/2019/12/09/234-palindrome-linked-list.html
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        totalNodes = len(nums)
        for i in range(totalNodes//2):
            if nums[i] != nums[totalNodes-1-i]:
                return False

        return True

## TEST CASES
test = Solution()
root = ListNode(1)
root.next = ListNode(2)
assert test.isPalindrome(root) == False

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(2)
root.next.next.next = ListNode(1)
assert test.isPalindrome(root) == True
print('All Passed!')
