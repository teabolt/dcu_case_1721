
def detect_loop(lst):
    if lst.head == None:
        return False
    ptr = lst.head
    while ptr != None:
        if ptr.next == lst.head:
            return True
        ptr = ptr.next
    return False