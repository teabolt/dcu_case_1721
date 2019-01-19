# coding: utf-8

import igraph
igraph.__version__
import numpy
numpy.__version__
import matplotlib
matplotlib.__version__
igraph.Graph
help(igraph.Graph)
g = igraph.Graph()
g
dir(g)
g.vs()
g.vcount()
g.vcount
g.radius()
g.subgraph()
g.subgraph
g
print(g)
g[name]
g['name']
# GraphSummary
g.add_vertex()
g.add_vertices(2)
print(g)
g.__str__()
g._add_vertices()
g.add_vertices()
g.add_vertices(1)
print(g)
# IGRAPH PROPS NUMVERTICES NUMEDGES -- GRAPH NAME
g.add_edges()
g.add_edge()
g.add_edge(source=0, target=1)
print(g)
g.add_edges([10, 0])
g.add_edges([(10, 0)])
g.add_edges([(1, 0)])
g
print(g)
g.add_edges([(1, 0)])
g
print(g)
# undirected graph
# repeat edges
g.add_edges([(2, 1], (3, 2), (3, 0)])
g.add_edges([(2, 1), (3, 2), (3, 0)])
g
print(g)
# show edges
g.alpha()
g.get_eid()
g.get_eid(0)
g.get_eid(0, 1)
g.get_eid(0, 1)
g.get_eid(1, 0)
g.get_eid(0, 1)
g.delete_edges([0, 1])
print(g)
g.delete_vertices(3)
print(g)
g.add_vertex()
g
print(g)
g.add_edge(target=3, source=0)
print(g)
igraph.summary(g)
igraph.__build_date__
g.get_edgelist()
g.get_edgelist()
print(g)
bt = igraph.Graph.Tree(10, 2)
bt
bt.__str__()
bt.get_edgelist()
tt = igraph.Graph.Tree(25, 3)
igraph.summary(tt)
tt.get_edgelist()
grg = igraph.Graph.GRG(25, 0.5)
igraph.summary(grg)
grg.get_edgelist()
grg2 = igraph.Graph.GRG(25, 0.5)
grg2
igraph.summary(grg2)
igraph.summary(grg)
grg.isomorphic(grg2)
grg
summary(grg)
igraph.summary(grg)
grg
grg.get_edgelist()
igraph.summary(g)
g
g.get_edgelist()
g.vs()
g.es()
g.vs
g.vs["value"] = [4, -2, 5, 3]
igraph.summary(g)
g.es["weight"] = [-34, 14, 24]
igraph.summary(g)
g.es[0].attributes()
g.es[0]['weight'] = -35
g.es[0].attributes()
g.es
g.es()
g.get_edgelist()
g.es[0]
g.es[1]
g.es[2]
g.es[3]
g.es[3].source
g.es[2].source
g.es[2].target
g.es[2].index
g.es[2].tuple
g.add_edge(0, 2)
g.es[2].tuple
g.es[3].tuple
g.vs[0]
g.vs[3]
g.vs[4]
g.vs[3].tuple
dir(g.vs[3])
g.vs[3].neighbors()
g.vs[3].attributes()
g["name"] = "my sample graph"
igraph.summary(g)
g.vs[2].attributes()
g.vs[2]['value']
del g.vs[2]['value']
g.vs[2].attributes()
g.pagerank()
g.degree()
g.layout()
layout = g.layout("kk")
igraph.plot(g, layout=layout)
import igraph
igraph.plot(g, layout=layout)
get_ipython().run_line_magic('save', 'igraph_1.py 0-99999')
