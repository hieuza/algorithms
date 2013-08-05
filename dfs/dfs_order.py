#!/usr/bin/env python
# hieuza@gmail.com
# 03.Dec.2012
# updated: 03.Aug.2012, iterative DFS

# depth-first-search ordering
# preorder, postorder and reversed postorder
from graph import Graph
import time

class DFSOrder(object):
	def __init__(self, g, recursive=True):
		self.g = g
		self.recursive = recursive

		# queues of visited vertices
		self.preorder = []
		self.postorder = []

		visited = [False] * g.N

		for u in xrange(self.g.N):
			if not visited[u]:
				if self.recursive:
					self.dfs(u, visited)
				else:
					self.iterative_dfs(u, visited)

		# stack of post visited vertices
		self.reversed_postorder = self.postorder[:]
		self.reversed_postorder.reverse()


	def dfs(self, u, visited):
		visited[u] = True

		self.preorder.append(u)

		for v in self.g.adjacency(u):
			if not visited[v]:
				self.dfs(v, visited)

		self.postorder.append(u)


	# dfs started from vertex u
	def iterative_dfs(self, u, visited):
		stack = [u]
		visited[u] = True
		self.preorder.append(u)

		bNextStackElem = False
		while len(stack) > 0: # stack is not empty
			s = stack[-1] # peek the top of the stack

			bNextStackElem = False
			for v in self.g.adjacency(s):
				if bNextStackElem:
					break

				if not visited[v]:
					stack.append(v) # push to the top of stack
					visited[v] = True
					self.preorder.append(v) 

					# first time visit the node
					# will process it in next while iterator
					bNextStackElem = True
					continue

			if not bNextStackElem:
				self.postorder.append(s)
				stack.pop()


from graph import simple_graph
def test(n):
	g = Graph(n, weighted=False, directed=True)

	g.random_generate(max_degree=20)

	# print g

	# g = simple_graph()

	p = []
	for r in [True, False]:
		try:
			t0 = time.time()
			dfsorder = DFSOrder(g, recursive=r)
		except RuntimeError as e:
			print 'RuntimeError:', e
			continue
		finally:
			print 'running time:', ('%.5f' % (time.time() - t0))

		if n < 20:
			print '     preorder:', dfsorder.preorder
			print '    postorder:', dfsorder.postorder
			print 'rev-postorder:', dfsorder.reversed_postorder
		p.append([dfsorder.preorder, dfsorder.postorder,\
					dfsorder.reversed_postorder])

	if len(p) == 1: # only iterative result
		print 'Iterative running completed'
	else:
		# check if iterative and recursive results are the same
		pre1, post1, rev1 = p[0]
		pre2, post2, rev2 = p[1]

		if (pre1 != pre2 or post1 != post2 or rev1 != rev2):
			print "wrong iterative algorithm"
		else:
			print "OK for this test"


if __name__ == '__main__':
	import sys

	n = 5
	if len(sys.argv) > 1:
		n = int(sys.argv[1])

	test(n)

