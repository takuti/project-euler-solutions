# coding: utf-8

import sys

class Node:
  edges_to = []
  edges_cost = []
  done = False
  cost = -1

def main():
  if len(sys.argv) != 2:
    print 'Please give input filename.'
    quit()

  lines = map(lambda l: map(int, l.rstrip().split(' ')), open(sys.argv[1]).readlines())
  costs = []
  for l in lines:
    costs.extend(l)

  n_rows = len(lines)
  n_nodes = len(costs) + 1
  nodes = [Node() for i in range(n_nodes)]
  nodes[0].edges_to = [1]
  nodes[0].edges_cost = [costs[0]]
  idx = 1
  for row in range(1, n_rows):
    for i in range(row):
      left = idx + row
      right = left + 1
      nodes[idx].edges_to = [left, right]
      nodes[idx].edges_cost = [costs[left-1], costs[right-1]]
      idx += 1

  nodes[0].cost = 0 # start node

  while True:
    done_node = None
    for node in nodes:
      if node.done or node.cost < 0: continue # already done or unreachable
      if done_node == None: # since the graph is directed, only not-done (below) nodes are considered
        done_node = node
    if done_node == None: break # all nodes are done
    done_node.done = True
    for i in range(len(done_node.edges_to)):
      to = done_node.edges_to[i]
      cost = done_node.cost + done_node.edges_cost[i]
      if nodes[to].cost < 0 or cost > nodes[to].cost:
        nodes[to].cost = cost

  max_cost = float('-inf')
  for i in range(n_nodes-n_rows, n_nodes):
    if nodes[i].cost > max_cost: max_cost = nodes[i].cost
  print max_cost

if __name__ == '__main__':
  main()
