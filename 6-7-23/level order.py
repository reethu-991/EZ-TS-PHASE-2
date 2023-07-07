
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):
    q = [root]
    while len(q) != 0:
        ele = q.pop(0)
        if ele.left != None:
            q.append(ele.left)
        if ele.right != None:
            q.append(ele.right)
        print(ele.data)

# Create the tree nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Call the levelorder function with the root of the tree
levelorder(root)
