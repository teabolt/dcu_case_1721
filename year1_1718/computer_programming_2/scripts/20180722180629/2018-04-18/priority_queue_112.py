#!/usr/bin/env python3

class PQ(object):
    """Implement a priority queue ADT as a maximum heap (binary tree) data structure
    (implemented as a dictionary wrapper)"""

    def __init__(self):
        """Create a new empty priority queue"""
        self.d = {} # heap map: node number -> value
        self.N = 0 # number of nodes

    def __str__(self):
        """String representation: dictionary mapping nodes to values 
        To-do: full blown-out binary graph graphic of the priority queue"""
        return str(self.d)

    def exch(self, A, B):
        """(In-place) swap values at two notes A and B"""
        self.d[A], self.d[B] = self.d[B], self.d[A] # swap with multiple assignment

    def insert(self, v):
        """Add a new value to the priority queue"""
        self.N += 1 # go to next free node
        self.d[self.N] = v # add value
        self.swim(self.N) # let the value swim up to its correct position, to ensure heap property

    def swim(self, N):
        """Let node value at node N reach its correct position in a heap tree by going up the tree.
        Position is 'correct' if the heap property is satisfied, eg: every parent is greater than or equal than each of its children"""
        # keep going as long as not at root node or child is greater than parent (violated heap property)
        while N > 1 and self.d[N//2] < self.d[N]:
            self.exch(N, N//2) # swap/swim the value up
            N = N//2 # update the node to look at

    def delMax(self):
        """Remove and return the maximum/forefront element of the priority queue(root node of the heap)"""
        m = self.d[1] # retrieve max
        self.exch(1, self.N) # swap root and 'smallest' nodes
        del(self.d[self.N]) # remove smallest node (has max value)
        self.N -= 1 # decrement node number
        self.sink(1) # let value sink
        return m # return max

    def bigger(self, A, B):
        """Return the bigger of two (children) nodes"""
        # handle the case of a child not being present (right child)
        try:
            return max([A, B], key=self.d.__getitem__)
        except KeyError:
            return A

    def sink(self, N):
        """Let value at node N go down the heap tree('sink') to reach its correct position,
        such that the heap property is satisfied"""
        # while not at lowest node (still have children) and smaller than the bigger of (both of) your children, keep going
        while N*2 <= self.N and self.d[N] < self.d[self.bigger(2*N, 2*N+1)]:
            # swap with the bigger of the two children (let it satisfy the heap property)
            B = self.bigger(2*N, 2*N+1)
            self.exch(N, B) # swap parent with bigger of its children
            N = B # update the node

    def is_empty(self):
        """Return true if priority queue has no nodes"""
        return self.N == 0 # or self.d == {}, or self.size() == 0

    def size(self):
        """Return the size (number of nodes) of the priority queue"""
        return self.N # or len(self.d)

    def getMax(self):
        """Return the value of the maximum element of the priority queue, without removing the element"""
        return self.d[1] # root element is the maximum in a max heap