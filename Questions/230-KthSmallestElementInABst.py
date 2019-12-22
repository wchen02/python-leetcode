# See details here https://wenshengchen.com/2019/12/12/230-kth-smallest-element-in-a-bst.html
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []

        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        
        return result

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inOrder = self.inOrderTraversal(root)
        return inOrder[k-1]

## TEST CASES
test = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

answer = test.kthSmallest(root, 1)
assert answer == 1
print('All Passed!')