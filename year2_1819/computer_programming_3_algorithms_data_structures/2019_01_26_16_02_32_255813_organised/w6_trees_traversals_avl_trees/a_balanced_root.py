
def is_avl(bst):
    # Determine whether this bst is AVL balanced or not.
    if bst.root == None:
        return True # vacuously true
    else:
        return abs(bst.r_height(bst.root.left) - bst.r_height(bst.root.right)) < 2