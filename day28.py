class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# isMirror function is used to verify if two subtrees are mirror images of each other
def isMirror(leftSub, rightSub):
  
    # Both are null, so they are mirror images
    if leftSub is None and rightSub is None:
        return True

    # One of them is null, so they aren't mirror images
    if leftSub is None or rightSub is None:
        return False

    # Check if the current nodes are equal  and their subtrees are mirrors
    return (leftSub.data == rightSub.data) and \
           isMirror(leftSub.left, rightSub.right) and \
           isMirror(leftSub.right, rightSub.left)

def isSymmetric(root):#this is used to check if the given subtress are symmetirc of each other.
  
    # If tree is empty, it's symmetric
    if root is None:
        return True

    # Check if the left and right subtrees are 
    # mirrors of each other
    return isMirror(root.left, root.right)

if __name__ == "__main__":
  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(isSymmetric(root)) #True
