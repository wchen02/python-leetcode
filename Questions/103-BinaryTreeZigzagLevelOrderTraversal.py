from typing import List

# See details here https://wenshengchen.com/2019/12/24/103-binary-tree-zigzag-level-order-traversal.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        stk = [root]
        leftToRight = True
        result = []

        while stk: 
            level = []
            tempStk = []
            for _ in range(len(stk)):
                node = stk.pop()
                level.append(node.val)

                if leftToRight:
                    if node.left:
                        tempStk.append(node.left)
                    if node.right:
                        tempStk.append(node.right)
                else:
                    if node.right:
                        tempStk.append(node.right)
                    if node.left:
                        tempStk.append(node.left)
            leftToRight = not leftToRight
            stk = tempStk
            result.append(level)

        return result

## TEST CASES
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
test = Solution()
answer = test.zigzagLevelOrder(root)
assert answer == [
  [3],
  [20,9],
  [15,7]
], answer

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(10)
root.left.right = TreeNode(11)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
test = Solution()
answer = test.zigzagLevelOrder(root)
assert answer == [
  [3],
  [20,9],
  [10,11,15,7]
], answer

assert test.zigzagLevelOrder(None) == []
print('All Passed!')
