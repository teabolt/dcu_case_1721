#!/usr/bin/env python3

"""Binary Search Tree implementation and methods"""


import sys


class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

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

    def r_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)
            
    def count(self): return self.r_count(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): return self.r_height(self.root)

    def r_pre_order(self, ptr):
        if ptr == None: # no node (empty tree case)
            return None # exit the function
        elif ptr.left == None and ptr.right == None: # node is a leaf (no children)
            print(ptr.item, end=' ') # the node's data
            return None
        else:
            print(ptr.item, end=' ') # parent
            self.r_pre_order(ptr.left) # left child
            self.r_pre_order(ptr.right) # right child

    def pre_order(self):
        """Traverse the tree (print each element once) using a preorder (parent first, then the children) (pre(before)-in(middle)-post(after) -> p...parent - when printed, in context of children)
        (left to right traversal: left child is printed before right child). 
        Recursive implementation"""
        self.r_pre_order(self.root)
        print() # final newline

    def r_post_order(self, ptr):
        if ptr == None:
            return
        elif ptr.left == None and ptr.right == None:
            print(ptr.item, end=' ')
            return
        else:
            self.r_post_order(ptr.left)
            self.r_post_order(ptr.right)
            print(ptr.item, end=' ')

    def post_order(self):
        """Traverse the tree using a post-order (children first, then parent) (left to right)"""
        self.r_post_order(self.root)
        print()


def main():
    # testPreorder()
    # testPostorder()
    

def testPreorder():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST()
    for num in nums:
        tree.add(num)

    print("Print the elements of the tree in order:")
    tree.pre_order()

def testPostorder():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST()
    for num in nums:
        tree.add(num)

    print("Print the elements of the tree post order:")
    tree.post_order()


if __name__ == "__main__":
    main()