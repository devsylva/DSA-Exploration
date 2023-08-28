class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert(self, data):
        self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Creating a binary tree
my_tree = BinaryTree(10)

# Inserting elements into the tree
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(3)
my_tree.insert(8)

# Performing an inorder traversal
print("Inorder Traversal:", end=" ")
my_tree.inorder_traversal(my_tree.root)
