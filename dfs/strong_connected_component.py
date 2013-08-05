#!/usr/bin/env python
# hieuza@gmail.com
# 03.Dec.2012

# strong connected components in directed graph
# Kurasaju algorithm

# 1. R = reversed postorder of reversed graph
# 2. for each vertex u in R,
#    the reached vertices from u is a strong connected component
from dfs_order import DFSOrder
from graph import Graph

def scc(g):
	reversed_dfs = DFSOrder(g.reverse(), recursive=False)

	visited = [False] * g.N
	comp = [0] * g.N
	num_comp = 0

	for u in reversed_dfs.reversed_postorder:
		if not visited[u]:
			num_comp += 1

			mark_component(g, u, visited, comp, num_comp)


	print '#SCC:', num_comp
	# components

	cpnts = dict()
	for c in xrange(1, num_comp + 1):
		cpnts[c] = []

	for u in xrange(g.N):
		cpnts[comp[u]].append(u)

	vrts = cpnts.values()

	vrts.sort(key=lambda x: len(x))

	for x in vrts[-5:]:
		print '#vertices:', len(x)
		# print x



# update: 04.Aug.2013
# remove recursion
def mark_component(g, u, visited, comp, num_comp):
	visited[u] = True
	comp[u] = num_comp
	stack = [u]

	while len(stack) > 0:
		u = stack.pop()
		for v in g.adjacency(u):
			if not visited[v]:
				visited[v] = True
				stack.append(v)
				comp[v] = num_comp
				# mark_component(g, v, visited, comp, num_comp)


def read_graph():
	input_file = "/tmp/SCC.txt"
	n = 875715
	g = Graph(n, weighted=False, directed=True)

	fd = open(input_file, 'r')
	for l in fd:
		ss = l.split()
		u = int(ss[0])
		v = int(ss[1])
		g.add_edge(u, v)

	return g


def test(n):
	g = Graph(n, weighted=False, directed=True)

	g.random_generate()

	print g

	scc(g)

	g.visualize()


if __name__ == '__main__':
	import sys

	if 0:
		n = 5
		if len(sys.argv) > 1:
			n = int(sys.argv[1])

		test(n)

	# sys.setrecursionlimit(1000000)
	g = read_graph()
	scc(g)
