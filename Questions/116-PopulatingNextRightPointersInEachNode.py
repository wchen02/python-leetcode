# See details here https://wenshengchen.com/2019/12/30/73-set-matrix-zeroes.html
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                head = head.next
            
            leftmost = leftmost.left

        return root

## TEST CASES
test = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

test.connect(root)
assert root.next == None
assert root.left.next.val == 3
assert root.left.left.next.val == 5
assert root.left.right.next.val == 6
assert root.right.left.next.val == 7
print('All Passed!')
