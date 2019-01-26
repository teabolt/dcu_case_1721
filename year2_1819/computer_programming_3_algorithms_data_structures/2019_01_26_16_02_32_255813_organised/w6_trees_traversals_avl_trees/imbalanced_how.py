
def rotation_type(bst):
    # Descend down the path, checking which branch is unbalanced and adding appropriately
    # the tree is assumed to be unbalanced - else wrong answers are given if it is balanced
    rotation = []
    ptr = bst.root # the unbalanced node
    while ptr != None: # keep going until at the very bottom
        lh = bst.r_height(ptr.left) # get heights of sub-trees
        rh = bst.r_height(ptr.right)
        # the taller of the two branches is the unbalanced one (exceeds 1 in height differences)
        if lh < rh:
            rotation.append('r')
            ptr = ptr.right
        elif rh < lh:
            rotation.append('l')
            ptr = ptr.left
        else: # equal, probably a leaf
            ptr = ptr.right # just take a random branch (ptr will become None)
    return ''.join(rotation)
