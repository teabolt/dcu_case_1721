class Queue:
    def __init__(self, capacity = 4):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0

    def count(self):
        # counts the number of items in a queue?
        if self.front <= self.back: # back is after or at front
            return self.back - self.front # difference
            # 0 -> no items
        else: # front is after back
            # happens if front moves up from 0
            # and back circles back to the start from adding items
            # self.back-self.front will be negative.
            # Will subtract from the capacity
            return self.back - self.front + len(self.data)

    def isempty(self):
        return self.front == self.back

    def enqueue(self, item):
        # -1 buffer space
        # for zeroed indices?
        if self.count() < len(self.data) - 1: 
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
            # incr (mod capacity)
            # point to new back
            # if at the end, go to the front
            # have space so override anything old
        else: # simply don't add any more items, keep all the same
            print("Queue Full")

    def dequeue(self):
        if self.count() > 0:
           item = self.data[self.front]
           self.front = (self.front + 1) % len(self.data)
           # point to new front
           # reset if at the end
           return item
        else:
            return None
            # do nothing just return None