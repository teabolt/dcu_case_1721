
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
    return (q1, q2)