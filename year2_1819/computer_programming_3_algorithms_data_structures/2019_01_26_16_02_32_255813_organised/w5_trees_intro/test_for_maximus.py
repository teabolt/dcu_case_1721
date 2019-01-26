
#
#   Test whether the BST is maximal
#
def is_maximal(bst):
    height = bst.height()
    count = bst.count()
    return 2**height - 1 == count

    