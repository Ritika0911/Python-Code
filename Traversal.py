class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print 'Preorder Traversal is', printPreorder(root)
    print 'Inorder Traversal is', printInorder(root)
    print 'Postorder Traversal is', printPostorder(root)
