
def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    x = set()
    for row in edge_list:
        for element in row:
            x.add(element)
    length = len(x)
    # Insert code here
    for row in edge_list:
        lst = [0]*length
        for node in row:
            i = ord(node)-65
            lst[i] = 1
        adjacency_matrix.append(lst)    

    return adjacency_matrix
