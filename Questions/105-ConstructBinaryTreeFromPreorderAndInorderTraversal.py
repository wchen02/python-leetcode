from typing import List, Dict

# See details here https://wenshengchen.com/2019/12/23/105-construct-binary-tree-from-preorder-and-inorder-traversal.html
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeHelper(pi: int, pe: int, ii: int) -> TreeNode:
            nonlocal inorderMap
            if pi == pe:
                return None
            
            root = TreeNode(preorder[pi])
            rootIdx = inorderMap[root.val]
            leftLength = rootIdx - ii
            root.left = buildTreeHelper(pi + 1, pi + 1 + leftLength, ii)
            root.right = buildTreeHelper(pi + 1 + leftLength, pe, ii + 1 + leftLength)

            return root        
        inorderMap = { val:idx for idx, val in enumerate(inorder) }
        return buildTreeHelper(0, len(preorder), 0)
        
## TEST CASES
test = Solution()
node = test.buildTree([3,9,20,15,7], [9,3,15,20,7])
assert(node.val) == 3
assert(node.left.val) == 9
assert(node.right.val) == 20
assert(node.right.left.val) == 15
assert(node.right.right.val) == 7
print('All Passed!')
