class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if not root:
        return
    current = root
    s = []
    done = 0
    while (not done):
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s)>0):
                current = s.pop()
                print current.data
                current = current.right
            else:
               done = 1

def preOrder(root):
    if not root:
        return
    current = root
    s = []
    done = 0
    while(not done):
        if current is not None:
            print current.data
            s.append(current)
            current = current.left
        else:
            if(len(s)>0):
                current = s.pop()
                current = current.right
            else:
                done = 1

def postOrder(root):
    if not root:
        return
    visited = set()
    s = []
    node = root
    while s or node:
        if node:
            s.append(node)
            node = node.left
        else:
            node = s.pop()

            if node.right and not node.right in visited:
                s.append(node)
                node = node.right
            else:
                visited.add(node)
                print node.data
                node = None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print 'Inorder traversal is', inOrder(root)
    print 'Preorder traversal is', preOrder(root)
    print 'Postorder traversal is', postOrder(root)
