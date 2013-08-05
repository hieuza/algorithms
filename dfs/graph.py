#!/usr/bin/env python
# hieuza@gmail.com
# 03.Dec.2012
 

# a class for graph
import random
import matplotlib.pyplot as plt
import networkx as nx

class Graph(object):
	def __init__(self, N, directed=True, weighted=False):
		self.adj = dict()
		# adj[u]: list of vertices v such that (u, v) are edges in G
		self.N = N
		self.E = 0
		self.directed = directed
		self.weighted = weighted

		# initialize the adjacency of all vertices
		for u in xrange(self.N):
			self.adj[u] = dict()

	def add_edge(self, u, v, w=None):
		if v not in self.adj[u]:
			self.E += 1

		self.adj[u][v] = w

		if not self.directed:
			self.adj[v][u] = w

	
	def remove_edge(self, u, v):
		if v in self.adj[u]:
			self.adj[u].pop(v)

			self.E -= 1

			if not self.directed:
				self.adj[v].pop(u)


	def is_connected(self, u, v):
		return v in self.adj[u]


	def adjacency(self, u):
		return self.adj[u]


	def reverse(self):
		g = Graph(self.N, self.directed, self.weighted)

		for u in self.adj.keys():
			for v, w in self.adj[u].items():
				g.add_edge(v, u, w)

		return g


	def construct_from_file(self, fd):
		N, E = [int(x) for x in fd.readline().split()]

		for _ in xrange(E):
			u, v = [int(x) for x in fd.readline().split()]
			self.add_edge(u, v)


	def __repr__(self):
		s = []
		s.append('%d, %d' % (self.N, self.E))

		for u in xrange(self.N):
			if self.weighted:
				s.append('%d: %s' % (u, str(self.adj[u])))
			else:
				s.append('%d: %s' % (u, str(self.adj[u].keys())))

		return '\n'.join(s)


	def random_generate(self, wmin=1, wmax=100, max_degree=-1):
		if max_degree == -1:
			max_degree = self.N - 1

		for u in xrange(self.N):
			for _ in xrange(random.randint(0, max_degree)):
				v = random.randint(0, self.N - 1)
				if v == u: continue

				w = random.randint(wmin, wmax)
				self.add_edge(u, v, w)


	def edges(self):
		"""all edges"""
		q = []
		for u in xrange(self.N):
			for v in self.adj[u]:
				q.append((u, v))

		return q


	def visualize(self):
		g = None
		if self.directed:
			g = nx.DiGraph()
		else:
			g = nx.Graph()


		g.add_edges_from(self.edges())

		nx.draw_random(g)
		plt.show()


# update: 03.Aug.2013
# make a simple directed graph
def simple_graph():
	n = 7
	"""
	+-----------------+
	|                 |
	v                 |
   [0] ---> [1] ---> [3] ---> [6]
	         |   _____^        |
	 	     | _/      _______/
		     v/       v
		    [2] ---> [4] ---> [5]
	"""
	g = Graph(n, directed=True, weighted=False)
	edges = [(0, 1), (1, 2), (1, 3), (2, 3),\
			(2, 4), (3, 6), (4, 5), (3, 0), (6, 4)]

	for u, v in edges:
		g.add_edge(u, v)
	# print g
	# g.random_generate()
	return g


def test(n):
	for weighted in [True, False]:
		g = Graph(n, directed=True, weighted=weighted)

		g.random_generate()

		print 'weighted graph:', weighted
		print g


if __name__ == '__main__':
	n = 5
	test(n)
