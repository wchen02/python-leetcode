from typing import List

# See details here https://wenshengchen.com/2020/02/24/951-flip-equivalent-binary-trees.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else:
            return False

## TEST CASES
test = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)
root1.right = TreeNode(3)
root1.right.left = TreeNode(6)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.left.right = TreeNode(6)
root2.right = TreeNode(2)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.right = TreeNode(7)
root2.right.right.left = TreeNode(8)

test.flipEquiv(root1, root2)
print('All Passed!')
