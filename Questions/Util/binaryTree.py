from collections import deque

# See details here https://wenshengchen.com/2019/09/10/297-serialize-and-deserialize-binary-tree.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root: 
            return '[]'
        
        result = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append('null')

        while result and result[-1] == 'null' and result[-2] == 'null':
            result.pop()
            result.pop()

        return '[' + ','.join(result) + ']'

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if data == '[]':
            return None

        nodes = data[1:-1].split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while i + 1 < len(nodes):
            node = q.popleft()
            if nodes[i] != 'null':
                node.left =  TreeNode(int(nodes[i]))
                q.append(node.left)

            if nodes[i+1] != 'null':
                node.right = TreeNode(int(nodes[i+1]))
                q.append(node.right)

            i += 2

        return root