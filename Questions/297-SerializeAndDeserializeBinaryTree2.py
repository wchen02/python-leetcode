from collections import deque

# See details here https://wenshengchen.com/2019/09/10/297-serialize-and-deserialize-binary-tree.html
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root: 
            return ''

        result = []
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
        
    def deserialize(self, data):
        if not data: 
            return None

        nodes = data.split(",")
        root = TreeNode(nodes[0])

        q = deque([root])
        i = 1
        
        while q:
            node = q.popleft()
            
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
            
        return root

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

test = Codec()
serialized1 = test.serialize(None)
deserialized1 = test.deserialize(serialized1)
serialized2 = test.serialize(deserialized1)
assert serialized1 == serialized2

node1.right = node2
node2.left = node3
serialized1 = test.serialize(node1)
deserialized1 = test.deserialize(serialized1)
serialized2 = test.serialize(deserialized1)
assert serialized1 == serialized2

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node8
node3.left = node6
node3.right = node7
node6.right = node9
serialized1 = test.serialize(node1)
deserialized1 = test.deserialize(serialized1)
serialized2 = test.serialize(deserialized1)
assert serialized1 == serialized2
print('All Passed!')
