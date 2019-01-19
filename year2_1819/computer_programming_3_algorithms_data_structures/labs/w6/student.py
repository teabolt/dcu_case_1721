#!/usr/bin/env python3


import sys


class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    """ An implementation of a Binary Search Tree
     """
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for x in lst:
                self.add(x)

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): return self.r_height(self.root)


def is_avl(tree):
    """Return true if 'tree', an AVL tree of max. height 3, is an AVL balanced tree, false otherwise"""
    # Determine whether this bst is AVL balanced or not.
    if tree.root == None:
        return True # vacuously true
    else:
        return abs(tree.r_height(tree.root.left) - tree.r_height(tree.root.right)) < 2


def rotation_type(bst):
    """'bst' is a tree with three nodes that just became unbalanced.
    Return a string indicating the type of rotation that would fix the unbalance:
    'll', 'rr', 'lr', 'rl' ('l'=left, 'r'=right)"""
    # General solution for tree with any height: use height()
    # Specific solution for tree with height 3: if statements and checks for None pointers.
    # s = ''
    # lh = bst.r_height(bst.root.left)
    # rh = bst.r_height(bst.root.right)
    # # Height 3 specific sol: check one side for height only (the other must be 0), pick non-zero
    # if lh < rh:
    #     unbal_node = bst.root.right
    #     s += 'r'
    # else:
    #     unbal_node = bst.root.left
    #     s += 'l'
    # lh = bst.r_height(unbal_node.left)
    # rh = bst.r_height(unbal_node.right)
    # if lh < rh:
    #     s += 'r'
    # else:
    #     s += 'l'
    # return s

    # Descend down the path, checking which branch is unbalanced and adding appropriately
    # the tree is assumed to be unbalanced - else wrong answers are given if it is balanced
    rotation = []
    ptr = bst.root # the unbalanced node
    while ptr != None: # keep going until at the very bottom
        lh = bst.r_height(ptr.left) # get heights of sub-trees
        rh = bst.r_height(ptr.right)
        # the taller of the two branches is the unbalanced one (exceeds 1 in height differences)
        if lh < rh:
            rotation.append('r')
            ptr = ptr.right
        elif rh < lh:
            rotation.append('l')
            ptr = ptr.left
        else: # equal, probably a leaf
            ptr = ptr.right # just take a random branch (ptr will become None)
    return ''.join(rotation)
    # this is probably inefficient due to many height checks

#
#   AVL tree. The add method contains an AVL fix section which restructures the tree
#               if it is unbalanced.
#           There is no delete method.
#
#           Also, you should note that this is an educational example. A real world implementation would
#           not find the height as shown, instead each node would store balance information so that it
#           could be looked up rather than discovered.
#           Note that finding the height as done here is an O(n) operation.
#           Maintaining and updating the balance is an O(1) operation.
#
#           For more details see
#               https://en.wikipedia.org/wiki/AVL_tree#Balance_factor
#
class AVLTree:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            parent_stack = [] # Use a list as a stack to hold parents
            child_tree = self.root
            while child_tree != None:
                parent_stack.append(child_tree) # remember the parent for the path back (when checking for AVLness).
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree is pointing to the new node, but we've gone too far
            # we need to get to the parent to change its pointer
            parent = parent_stack[-1]       # The parent is the last item on the parent stack
            node = Node(item, None, None)
            if item < parent.item: # left?
                parent.left = node
            elif item > parent.item: # right?
                parent.right = node
            else:
                # Else this item is already in the tree and so not added
                return

            # The item has been added, now see if we are AVL unbalanced - go back up the tree.
            while node != None:
                if abs(self.recurse_height(node.left) - self.recurse_height(node.right)) > 1:
                    # Found an out of order node! Need to fix
                    # First get the three nodes to restructure
                    top = node
                    mid = top.left if item < top.item else top.right
                    bot = mid.left if item < mid.item else mid.right

                    # Work out which rotation we need to do. (which one is in the middle)
                    if top.item < mid.item < bot.item:
                        # mid in the middle => put on top
                        new_top = mid
                        top.right = mid.left
                        mid.left = top
                    elif bot.item < mid.item < top.item:
                        # Right rotation
                        new_top = mid
                        top.left = mid.right
                        mid.right = top
                    elif mid.item < bot.item < top.item:
                        # double 1
                        new_top = bot
                        mid.right = bot.left
                        top.left = bot.right
                        bot.left = mid
                        bot.right = top
                    else:# top.item < bot.item < mid.item:
                        # double 2
                        new_top = bot
                        mid.left = bot.right
                        top.right = bot.left
                        bot.left = top
                        bot.right = mid

                    # Make the parent of top point to the new top
                    top_parent = None if len(parent_stack) == 0 else parent_stack.pop()
                    if top_parent == None:
                        self.root = new_top
                    elif top.item < top_parent.item:
                        top_parent.left = new_top
                    else:
                        top_parent.right = new_top
                    break

                # Carry on up the path be getting the parent from the stack (which was built on the way down)
                node = None if len(parent_stack) == 0 else parent_stack.pop()

                # solution here:
                # if node == None:
                #     return None
                # else:
                #     return node.item


    def recursive_contains(self, item, ptr):
        """ returns a pointer to the node rather than a boolean, None if not present """
        if ptr == None:
            return None
        else:
            if item == ptr.item:
                return ptr
            elif item < ptr.item:
                return self.recursive_contains(item, ptr.left)
            else:
                return self.recursive_contains(item, ptr.right)

    def contains(self, item):
        """ returns a pointer to the node rather than a boolean, None if not present """
        return self.recursive_contains(item, self.root)

    def recurse_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.recurse_height(ptr.left), self.recurse_height(ptr.right))

    def height(self): return self.recurse_height(self.root)

    def recurse_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return self.recurse_str(ptr.left) + str(ptr.item) + "," + self.recurse_str(ptr.right)
            
    def __str__(self):
        return self.recurse_str(self.root)

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    parent_stack = [] # a list (stack) of parents in the path (need to be able to go back the path)
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
        return None # just added a Node
    else:
        node = parent_stack.pop() # get most recently added node (starting from the bottom of the tree)
        lh = tree.recurse_height(node.left)
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

def main():
    #testIsavl()
    #testRotationtype()
    testAddunbalanced()


def testAddunbalanced():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = AVLTree()
    for n in nums[:-1]:
        tree.add(n)

    # Using the student's function, add the item to the tree
    x = add(tree, nums[-1])
    print(x)

def testRotationtype():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums)

    print(rotation_type(tree))

def testIsavl():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums)

    if tree.height() > 3:
         print("error ... your tree is too tall")
    else:
         print(is_avl(tree))


if __name__ == "__main__":
    main()