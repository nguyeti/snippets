# Given the root to a binary tree, return the deepest node.
class Node:
    def __init__(self, dataval=None, left=None, right=None):
        self.dataval = dataval
        self.left = left
        self.right = right

    def __str__(self):
        return self.dataval

    def __repr__(self):
        return str(self.dataval)

def increment_depth(node_depth_tupple):
    node, depth = node_depth_tupple
    return (node, depth + 1)

def deepest(node):
    # The root node has no children
    if node and not node.left and not node.right:
        return (node, 1)
    
    # The root node only has a right children
    if node and not node.left:
        return increment_depth(deepest(node.right))
    
    if node and not node.right:
        return increment_depth(deepest(node.left))

    return increment_depth(max(deepest(node.left), deepest(node.right), key = lambda x: x[1]))
    
if __name__ == "__main__":
    node_3_left = Node(30)
    node_2_left = Node(12, node_3_left)
    node_2_right = Node(778)
    no_children_node = Node(3, node_2_left, node_2_right)
    
    print(deepest(no_children_node))