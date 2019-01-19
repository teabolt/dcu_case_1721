#!/usr/bin/env python3

import random


class Node(object):
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST(object):
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
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.
    
    ###

    def rcount(self, ptr, lo, hi):
        if ptr == None:
            # I have no items, so obviously nothing is in range
            return 0
        else:
            v = ptr.item
            if lo <= v <= hi:   # in range
                # I'm in range, and what's more, the guys on the left and right might have more things like me!
                return 1 + self.rcount(ptr.left, lo, hi) + self.rcount(ptr.right, lo, hi)
            elif v < lo:        # too small
                # I'm too small to be in range, but the guy on the right with bigger guys might have what you need
                return self.rcount(ptr.right, lo, hi)
            elif hi < v:        # too big
                # I'm too large to be in the range, but the guy on the left with smaller guys might have what you need
                return self.rcount(ptr.left, lo, hi)
            # OR
            # else:
            #       return self.rcount(ptr.left, lo, hi) + self.rcount(ptr.right, lo, hi)
            # Assuming this is O(n), above might be O(log n) with balanced BST.

    def count(self, lo, hi):
        """Return an integer count of how many elements are in the range between 'lo' and 'hi' values, inclusive.
        Empty tree's count is 0, for any range.
        Recursive implementation. Recurse on root, using 'rcount' method.
        Assuming 'lo' < 'hi'"""
        return self.rcount(self.root, lo, hi)

    def rheight(self, ptr):
        if ptr == None:
            # I am empty. I have no height
            return 0
        elif ptr.left == None and ptr.right == None:
            # I am a leaf. I have height one.
            return 1
        else:
            # Check the heights of both left and right subtrees
            lh = self.rheight(ptr.left)
            rh = self.rheight(ptr.right)
            # Whichever subtree is tallest, is the one whose height we care about
            if lh < rh:
                # my node contributes 1 to the tallest sub-tree's height, resulting in this tree
                return 1 + rh
            else:   # lh > rh or lh == rh
                return 1 + lh
            # (alternatively, use max to get the tallest sub-tree of the two)
        # OR if ... None
        # else: return max(self.rheight(ptr.left)+1), self.rheight(ptr.right)+1)
        # include the node in counts of tallest, use maximum function

    def height(self):
        """Return the height of a BST. Recursive implementation.
        BST with one node is assumed to be of height 1."""
        return self.rheight(self.root)

    def rtotal(self, ptr):
        if ptr == None:
            return 0
            # I am empty. My count but my count stays at zero...
        else:
            return ptr.item + self.rtotal(ptr.left) + self.rtotal(ptr.right)
            # My number + ask the left guy to count his numbers + ask the right gal to count her numbers

    def total(self):
        return self.rtotal(self.root)

def r_make_list(lst):
    N = len(lst)
    if N == 0:
        return lst
    elif N == 1:
        return lst
    elif N == 2:
        return lst
    else:
        mid = N//2
        return [lst[mid]]+r_make_list(lst[:mid])+r_make_list(lst[mid+1:])


def make_list(lst):
    return r_make_list(sorted(lst))


def main():
    # testCount()
    # testHeight()
    # testTotal()
    testBalanced()

def testBalanced():
    random.seed(0)
    
    for length in [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 50, 100]:
        # Make a random lst
        lst = random.sample(range(length), length)

        # Use the students function to arramge the list
        new_list = make_list(lst) # get the student's lst

        # Make sure they have the same elements
        if sorted(lst) != sorted(new_list):
            print("You have somehow changed the elements of the list. You are only supposed to change the order.")
        else:
            # Create a BST
            tree = BST()
            # and add in the elements from the list
            for element in new_list:
                tree.add(element)
            # Show the lst
            print(lst)
            # And some data ... the height, the count and whether or not balanced.
            # print(tree.max_height(), tree.count(), tree.is_balanced())


def testTotal():
    t = BST()
    assert t.total() == 0
    t.add(2)
    assert t.total() == 2
    a = [4, 1, 6, -1, 7, 3]
    for e in a:
        t.add(e)
    assert t.total() == 2 + sum(a)

def testHeight():
    t = BST()
    assert t.height() == 0
    t.add(1)
    assert t.height() == 1
    for e in [2, 7, 4, 8, 5]:
         t.add(e)
    assert t.height() == 5
    t.add(0)
    assert t.height() == 5
    t.add(6)
    assert t.height() == 6
    t.add(9)
    assert t.height() == 6

def testCount():
    t = BST()
    assert t.count(3, 5) == 0
    for e in [2, 7, 4, 8, 5]:
        t.add(e)
    assert t.count(3, 5) == 2
    assert t.count(10, 12) == 0
    assert t.count(-1, 1) == 0
    assert t.count(2, 8) == 5


if __name__ == '__main__':
    main()