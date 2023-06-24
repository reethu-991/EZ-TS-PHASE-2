class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
        if root:
            #1st recur on left child
            inorder(root.left)
            #then print the data of node
            print(root.val,end=' ')
            #now recur on right child
            inorder(root.right)
def postorder(root):
        if root:
             #1st recur on left child
             postorder(root.left)
            # recur on right child
             postorder(root.right)
            # print the data of node
             print(root.val,end=' ')
           
def preorder(root):
        if root:
            
        #1st  print the data of node
            print(root.val,end=' ')
         #then  recur data on left child
            preorder(root.left)
        #now recur on right child
            preorder(root.right)

root= node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print('inorder')
inorder(root)
print()
print('postorder')
postorder(root)
print()
print('preorder')
preorder(root)
