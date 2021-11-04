#! Study binary tree

"""This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a
string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following `Node` class

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')),
Node('right'))
assert deserialize(serialize(node)).left.left.val ==
'left.left'

```"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


node = Node(16)

node.left = Node(32)
node.left.left = Node(43)
node.right = Node(31)



def inorder(node):
    if node:
        # Recursively call inorder on the left subtree until it reaches a leaf node
        inorder(node.left)

        # Once we reach a leaf, we print the data
        print(node.data)

        # Now, since the left subtree and the root has been printed, call inorder on right subtree recursively until we reach a leaf node.
        inorder(node.right)
inorder(node)


'''Algorithm

    Create the binary tree using the Node class.
    Serializing:
        To serialize the tree into a string, I considered the null nodes as #.
        Starting from root, Depth First Search is used to traverse through the tree.
        If a node exists, its value is appended to the string and the left sub tree is traversed.
        This process continues until there are no more children left. Then a '#' is appended to the array and the recursive function is exited.
        Then the right sub tree is traversed and the same process is followed.
        The final resulting is string is returned.
    Deserializing:
        To deserialize a string to form a tree, the first word in the space seperated string is considered as the root.
        When a '#' is encountered, it is considered as a empty node and None is returned.
        In the remaining cases, a new node with the value as the word is formed and the remaining string is traversed.
        This function is called recursively until the end of the string is reached.
'''