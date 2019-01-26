
from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    parent_stack = [] # a list (stack) of parents in the path (need to be able to go back up the path)
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        child_tree = tree.root
        while child_tree != None:
            parent = child_tree
            parent_stack.append(parent)
            if item < child_tree.item: # If smaller ... 
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        # Ignore the case where the item is equal.
        
    #
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #

    if not parent_stack: # empty
        return None # Tree has just one node. It's not unbalanced.
    else:
        node = parent_stack.pop() # get most recent node in the path (starting from the bottom)
        lh = tree.recurse_height(node.left) # get the heights of subtrees
        rh = tree.recurse_height(node.right)
        # while not empty and AVL balanced (linear search)
        while parent_stack and abs(lh-rh) < 2: 
            node = parent_stack.pop() # get the next node (go up the path)
            lh = tree.recurse_height(node.left) # calculate heights
            rh = tree.recurse_height(node.right) # TO-DO: refactor to not repeat these tree lines twice

        # check if this is the unbalanced node or if you just ran out of parents
        if 1 < abs(lh-rh):
            return node.item
        else:
            return None
