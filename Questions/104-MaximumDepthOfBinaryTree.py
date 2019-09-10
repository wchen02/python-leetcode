# See details here https://wenshengchen.com/2019/09/09/104-maximum-depth-of-binary-tree.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

## TEST CASES
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

test = Solution()
answer = test.maxDepth(None)
assert answer == 0
node1.right = node2
node2.left = node3
answer = test.maxDepth(node1)
assert answer == 3

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node8
node3.left = node6
node3.right = node7
node6.right = node9
answer = test.maxDepth(node1)
assert answer == 4
print('All Passed!')
