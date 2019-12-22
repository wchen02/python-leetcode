import collections

# See details here https://wenshengchen.com/2019/12/06/101-symmetric-tree.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodeQueue = collections.deque()

        if root != None:
            nodeQueue.append(root)

        while nodeQueue:
            innerLevel = []
            for _ in range(len(nodeQueue)):
                cur = nodeQueue.popleft()
                if cur:
                    innerLevel.append(cur.val)
                else:
                    innerLevel.append(None)
                
                if cur:
                    nodeQueue.append(cur.left)
                    nodeQueue.append(cur.right)
            
            innerEnd = len(innerLevel) - 1
            if cur != root and len(innerLevel) % 2 == 1:
                return False

            for j in range(len(innerLevel)//2):
                if innerLevel[j] != innerLevel[innerEnd-j]:
                    return False

        return True
        
## TEST CASES
test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
assert test.isSymmetric(root) == True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = None
root.left.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(3)
assert test.isSymmetric(root) == False

root = None
assert test.isSymmetric(root) == True
print('All Passed!')
