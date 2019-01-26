
def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list = []
    
    # Insert code here
    for row in adjacency:
        lst = []
        for i,item in enumerate(row):
            if item != 0:
                lst.append(chr(65+i))
        edge_list.append(lst)         

    return edge_list