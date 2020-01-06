from typing import List

# See details here https://wenshengchen.com/2020/01/04/285-inorder-successor-in-bst.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev == p:
                return root                
            prev = root
            root = root.right
        return None
    
    def inorderSuccessor2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return None
        
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

## TEST CASES
test = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
p = root.left
root.right = TreeNode(3)
assert test.inorderSuccessor(root, p).val == 2

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
p = root.right
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
assert test.inorderSuccessor(root, p) == None

root = TreeNode(2)
p = root
root.right = TreeNode(3)
assert test.inorderSuccessor(root, p).val == 3

print('All Passed!')
