def search (root,key):
    #base case: root is null or key is present
    if root is None or root.val==key:
        return root
    #key is greater than roots key
    if root.val<key:
        return search(root.right,key)
    #key is smaller than rootskey
    return search(root.left,key)



































































































































































































