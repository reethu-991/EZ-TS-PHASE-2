class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    #set current to root of binary tree
    current=root
    stack=[] #intilize stack
    done=0
    while True:
        #reach the left most node of the current
        if current is not None:
            # place pointer to a tree node on the stack
            #before traversing the nodes left subtree
            stack.append(current)
            current=current.left
            #backtrack from empty subtree and visit node    
            #at the top of the stack;
            #however ,if the stack is empty y r done
        elif stack:
             current=stack.pop()
             print(current.data,end=' ')

             #wehave visited the node and its left
             #subtree now its right subtrees turn
             current=current.right
        else:
            break
    print()
#input
''' bt is
        1
       / \
    2
   / \
 4    5   '''

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
inorder(root)
