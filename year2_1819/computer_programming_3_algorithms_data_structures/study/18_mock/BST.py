#!/usr/bin/env python3

class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    def height(self):
        return self.r_height(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def inorder(self):
        return self.r_inorder(self.root)

    def r_inorder(self, ptr):
        if ptr != None:
            self.r_inorder(ptr.left)
            print(ptr.item)
            self.r_inorder(ptr.right)

    def r_postorder(self, ptr):
        if ptr != None:
            self.r_postorder(ptr.left)
            self.r_postorder(ptr.right)
            print(str(ptr.item) + " ", end="")


    def postorder(self):
        self.r_postorder(self.root)
        print()

    def r_count_leaves(self, ptr):
        if ptr is None:
            return 0
        elif ptr.left is None and ptr.right is None:
            return 1
        else:
            return self.r_count_leaves(ptr.left) + self.r_count_leaves(ptr.right)

    def count_leaves(self):
        return self.r_count_leaves(self.root)


def testLeafcount():
    bst = BST()
    items = list(map(int, input().split()))
    for item in items:
        bst.add(item)
    print(bst.count_leaves())



def testPostorder():
    bst = BST()
    items = list(map(int, input().split()))
    for item in items:
        bst.add(item)
    bst.postorder()



def q1e_inorder():
    bst = BST()
    bst.inorder()
    items = list(map(int, input().split()))
    for item in items:
        bst.add(item)
    bst.inorder()


def q1d_height():
    bst = BST()
    items = list(map(int, input().split()))
    assert bst.height() == 0
    bst.add(items[0])
    assert bst.height() == 1
    for item in items[1:]:
        bst.add(item)
    print(bst.height())


def main():
    # q1d_height()
    # q1e_inorder()
    # testPostorder()
    testLeafcount()


if __name__ == '__main__':
    main()