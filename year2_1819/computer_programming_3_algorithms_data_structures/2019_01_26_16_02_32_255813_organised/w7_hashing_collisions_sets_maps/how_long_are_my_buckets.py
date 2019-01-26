
from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
            
    def average_bucket_length(self):
        count = 0
        bucket_count = 0
        for bucket in self.table:
            if bucket == None:
                continue
            else:
                count += len(bucket)
                bucket_count += 1

        return count / bucket_count