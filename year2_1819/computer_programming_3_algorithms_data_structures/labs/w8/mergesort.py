#!/usr/bin/env python3

import random
from Queue import Queue



def split(q):
    """ A split function which will split a queue into two.
        The function returns a tuple containing the two queues.
    """
    # while the queue is not empty keep on dequeuing
    # *alternate* at each dequeue to which queue the element will be enqueued
    q1 = Queue()
    q2 = Queue()
    # 'alternator' setup
    qs = [q1, q2] # access the correct queue
    i = 0         # index variable
    while not q.isempty():
        item = q.dequeue()  # get the item
        queue = qs[i%2]     # get the right queue reference
        queue.enqueue(item) # add to the 'split' queue
        i += 1              # next alternation
    
    # this is probably not in place :(
    # maybe a version where you 'split' the queue based on length would be in place :-) ?!?!?!

    # for i, queue in enumerate(qs):
    #     print('****', i)
    #     while not queue.isempty():
    #         print(queue.dequeue())

    return (q1, q2)


def merge(q1, q2, q):
    """ this function will merge q1 and q2 into q.
        Assuming that q1 and q2 are sorted, this function will
        return q such that q contains the combined elements of q1 and q2 and
        q will also be sorted.
        
        The function returns nothing. The result will be contained in the queue parameter.
    """
    # q is empty in the beginning
    assert q.isempty()
    # keep going until one queue is exhausted
    while not (q1.isempty() or q2.isempty()): # de Morgan's law finally put to use
        # add the smaller of the two, 'progress' the queue when add
        if q1.first() <= q2.first():    # in place?
            q.enqueue(q1.dequeue())
        else:   # q1.first > q2.first
            q.enqueue(q2.dequeue())

    # exhaust the (other) queue
    while not q1.isempty():
        q.enqueue(q1.dequeue())

    while not q2.isempty():
        q.enqueue(q2.dequeue())

    return None


def mergesort(q):
    if len(q) < 2:
        return # Base case. No work to do for one element.

    # Split q into two smaller queues
    q1, q2 = split(q) # You will supply the split function
    # Actually, this time, the spilt function will be supplied by Charlie
    # Note that the original queue should now be empty

    # recursively sort these as well
    mergesort(q1)
    mergesort(q2)

    # Now, merge these together back into q
    merge(q1, q2, q) # student supplies merge function.


#
#   Make a queue from a lst
#
def make_q(lst):
    q = Queue()
    for x in lst:
        q.enqueue(x)
    return q


def issorted(q):
    last = q.dequeue()
    while not q.isempty():
        if last > q.first():
            return False # Two elements out of order
        last = q.dequeue() # student fix: lst -> last?

    return True # We got here and so all elemets must have been in order.


def main():
    # testSplit()
    testMerge()


def testMerge():
    lst = [10 * x for x in range(101)]
    random.shuffle(lst)

    q = make_q(lst)

    mergesort(q) # This uses the student's merge function to sort q

    if issorted(q):
        print("Test passed")
    else:
        print("Your merge function didn't work.")


def testSplit():
    lst = [10 * x for x in range(10)]
    q = make_q(lst)
    # Call the student's split function
    q1, q2 = split(q)
    if abs(len(q1) - len(q2)) > 1:
        print("The lengths of your two queues should not differ by more than 1.")
    elif len(q1) + len(q2) > len(lst):
        print("There are too many elements in your queues")
    elif len(q1) + len(q2) < len(lst):
        #print(len(q1), len(q2), len(lst))
        print("There are too few elements in your queues")
    else:
        # There are the right number of elements, check if the elements themselves are correct
        qlist = []
        # First add everything from q1
        while not q1.isempty():
            qlist.append(q1.dequeue())
        # Now add everything from q2
        while not q2.isempty():
            qlist.append(q2.dequeue())

        # Check the elements match
        if sorted(qlist) == sorted(lst): # Easiest way to compare two lists for contents is to sort them both.
            print("All tests passed")
        else:
            print("Your queues do not contain the right elements")


if __name__ == "__main__":
    main()