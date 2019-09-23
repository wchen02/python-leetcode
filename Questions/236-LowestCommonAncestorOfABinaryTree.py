from Util.binaryTree import TreeNode, Codec
from typing import Dict
from collections import deque

# See details here https://wenshengchen.com/2019/09/23/236-lowest-common-ancestor-of-a-binary-tree.html
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q == p:
            return q

        if q == root or p == root:
            return root

        nodeParent = { root.val: root }
        nodeStack = [root]
        
        while nodeStack:
            walker = nodeStack.pop()
            if walker.left:
                nodeParent[walker.left.val] = walker
                nodeStack.append(walker.left)
            if walker.right:
                nodeParent[walker.right.val] = walker
                nodeStack.append(walker.right)
        
        ancestorDict = { root.val: root }
        while p != root:
            ancestorDict[p.val] = nodeParent.get(p.val)
            p = nodeParent.get(p.val)

        while not ancestorDict.get(q.val):
            q = nodeParent.get(q.val)
        
        return q

## TEST CASES
test = Solution()
codec = Codec()

root = codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
p = TreeNode(5)
q = TreeNode(1)
answer = test.lowestCommonAncestor(root, p, q)
assert answer.val == 3

root = codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
p = TreeNode(5)
q = TreeNode(4)
answer = test.lowestCommonAncestor(root, p, q)
assert answer.val == 5

root = codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
p = TreeNode(3)
q = TreeNode(3)
answer = test.lowestCommonAncestor(root, p, q)
assert answer.val == 3

root = codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
p = TreeNode(0)
q = TreeNode(0)
answer = test.lowestCommonAncestor(root, p, q)
assert answer.val == 0
print('All Passed!')
