
#
#   Arrange a list so that when added to a tree will cause the tree to be completely balanced
#
def r_make_list(lst):
    N = len(lst)
    if N == 0:
        return lst
    elif N == 1:
        return lst
    elif N == 2:
        return lst
    else:
        mid = N//2
        return [lst[mid]]+r_make_list(lst[:mid])+r_make_list(lst[mid+1:])
 
 
def make_list(lst):
    return r_make_list(sorted(lst))