
def even_count(ll):
    pointer = ll.head
    even_counter = 0
    while pointer != None:
        if pointer.item % 2 == 0:
            even_counter += 1
        pointer = pointer.next
    return even_counter