# coding: utf-8

import igraph
igraph.plot()
g = igraph.Graph.GRG(25, 0.3)
igraph.summary(g)
print(g)
igraph.plot(g)
layout = g.lauout('kk')
layout = g.layout('kk')
igraph.plot(g, layout=layout)
igraph.plot(g, layout=layout)
p = igraph.plot(g, layout=layout)
p.redraw()
p.show()
p.redraw()
p.show()
p = igraph.plot(g, layout=g.lauout('random'))
p = igraph.plot(g, layout=g.layout('random'))
p.show()
p = igraph.plot(g, layout=g.layout('random_3d'))
p.show()
p = igraph.plot(g)
p.show()
get_ipython().run_line_magic('save', 'igraph_2 0-9999')
