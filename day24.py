class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def lcd(root,p,q):
    if not root or root ==p or root ==q:
        return root
    #recursively search for p and q in the left and right subtress
    left=lcd(root.left,p,q)
    right=lcd(root.right,p,q)

    #if left and right are notnull return root
    if left and right:
        return root
    return left if left else right #if it contains only left value then it will return left else right value will be return
root = Treenode(3)
root.left = Treenode(5)
root.right = Treenode(1)
root.left.left = Treenode(6)
root.left.right = Treenode(2)
root.right.left = Treenode(0)
root.right.right = Treenode(8)
root.left.right.left = Treenode(7)
root.left.right.right = Treenode(4)

p=root.left
q=root.right
lca=lcd(root,p,q)
print(lca.val)


""" if curr node is none return none if it is p or q return the node because 
one of the node is the ancestors itself .search the left &right & search the 
ancestors for p & q and return the node"""