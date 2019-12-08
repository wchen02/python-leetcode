# See details here https://wenshengchen.com/2019/12/07/108-convert-sorted-array-to-binary-search-tree.html
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        
## TEST CASES
test = Solution()
answer = test.sortedArrayToBST([-10,-3,0,5,9])
assert answer.val == 0
assert answer.left.val == -3
assert answer.left.left.val == -10
assert answer.right.val == 9
assert answer.right.left.val == 5

answer = test.sortedArrayToBST([-10,-3,0,5])
assert answer.val == 0
assert answer.left.val == -3
assert answer.left.left.val == -10
assert answer.right.val == 5

answer = test.sortedArrayToBST(None)
assert answer == None
print('All Passed!')
