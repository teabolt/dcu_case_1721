#!/usr/bin/env python3

import sys
import igraph as ig


# Binary Tree code


# Random weighted graph generator


# DFS, BFS, dijkstra shortest path, prim's MST


# Different representations, including edge list, adjacency matrix/list


# Draw the graph


# Graph representing something through attributes (Google Maps, social network)


def main():
    vertex_no = int(input('Enter vertex number: '))
    edges_input = input('Enter edges (space-separated, colon between source and target: ')
    edges = [tuple([int(edge) for edge in input_edge.split(':')]) for input_edge in edges_input.split()]
    g = ig.Graph()
    g.add_vertices(vertex_no)
    g.add_edges(edges)

    print(ig.summary(g))
    print(g.get_edgelist())


if __name__ == '__main__':
    main()