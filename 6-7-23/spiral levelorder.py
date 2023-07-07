def spiralLevelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]
    level = 0

    while queue:
        level += 1
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level % 2 == 0:
            current_level.reverse()

        result.extend(current_level)

    return result
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Generate spiral level order traversal
spiral_order = spiralLevelOrder(root)
print(spiral_order)
