class TreeNode:
  def __init__(self, data):

      self.data = data
      self.left = None
      self.right = None

def insert (root, data):
    if root is None:
        return TreeNode(data)
    else:
        if data < root.data:
            root.left  = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorderTraversal(root):
     if root:
         inorderTraversal(root.left)
         print(root.data)
         inorderTraversal(root.right)
         
root=  TreeNode(50)
root.left = TreeNode(20)
root.right =TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(55)
root.right.right = TreeNode(35)

print("inorderTraversal:")
inorderTraversal(root)

