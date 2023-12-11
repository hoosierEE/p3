from typing import List
from collections import defaultdict
# source: https://www.geeksforgeeks.org/topological-sorting/

# a topological sort based on DFS
def toposort(g)->list:
  def ts(stack:List,v,visited:List)->None: # mutates stack
    visited[v]=True
    for i in g[v]:
      if not visited[i]:
        ts(stack,i,visited)

    stack.append(v)
    return

  n=len(set(sum(map(list,edges),[]))) #number of nodes
  visited=[False]*n
  stack=[]
  for i in range(n):
    if not visited[i]:
      ts(stack,i,visited)

  return stack[::-1]

if __name__=="__main__":
  # build a directed graph
  edges=[(4,1), (4,0), (5,2), (5,0), (2,3), (3,1)] # edge list
  G=defaultdict(list)
  for a,b in edges: G[a].append(b)
  print(toposort(G))
