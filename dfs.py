from collections import defaultdict
from typing import Dict,List
dag = '''
     .------.
0--->1<--.  |
|        |  |
`--->2-->3  |
     |      |
     `-->4<-'
'''
class Graph:
 def __init__(self,edges):
  self.edges = edges
  self.nodes = sorted({x for y in edges for x in y})
  self.g = defaultdict(list)
  for (a,b) in edges:
   self.g[a].append(b)
  self.start = sorted({
   x for x in self.g.keys() if x not in {a for b in self.g.values() for a in b}
  })

def dfsr(G,v):
 visited = []
 def _dfs(G,v):
  visited.append(v)
  for edge in G[v]:
   if edge not in visited:
    _dfs(G,edge)
 _dfs(G,v)
 return visited

def dfsi(G,v):
 visited = []
 S = [v]
 while len(S):
  v = S[0]
  S=S[1:]
  if v not in visited:
   visited.append(v)
   for edge in G[v]:
    S = [edge]+S
 return visited

if __name__ == "__main__":
 edges = [(0,1), (0,2), (2,3), (1,4), (2,4), (3,1)] #(a,b) == (a->b)

 g = Graph(edges)
 start = 2
 print('starting at',start)
 print(dag)
 print('iterative:',dfsi(g.g,start))
 print('recursive:',dfsr(g.g,start))

 g2 = Graph(edges+[(3,2)]) #self-loop
 print(dag.replace('2--','2<='))
 print('iterative:',dfsi(g2.g,start))
 print('recursive:',dfsr(g2.g,start))
