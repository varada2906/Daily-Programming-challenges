class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def is_valid_bst(root):
#func validate is given to check if the current node and its subtress satisfy bst
    def validate(node,low=float('-inf'),high=float('inf')):
#An empty node means its a valid subtree
        if not node:
            return True
#The currents nodes value must be within the range[low,high]
        if node.val<=low or node.val>=high:
            return False
#recursively searching in left & right subtrees with updated ranges
        return(validate(node.left,low,node.val) and validate(node.right,node.val,high))
    return validate(root)
root =Treenode(2)
root.left=Treenode(1)
root.right=Treenode(3)

print(is_valid_bst(root))




