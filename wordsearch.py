from typing import List
import numpy as np

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:

    b = np.array(board)
    r,c = b.shape
    coords = np.array([[-1,0],[1,0],[0,-1],[0,1]])
    for letter in set(word):
      if letter not in b:
        return False

    if word in b: # single letter shortcut
      return True

    def successors(v:'visited', w:'word so far', rc:'pair'):
      '''coords to try after landing on rc'''
      cs = coords+rc
      # filter out visited and invalid coordinates
      return [(v,w,(x,y)) for (x,y) in cs if x>=0 and y>=0 and x<r and y<c and word.startswith(w+b[(x,y)]) and (x,y) not in v]

    _fringe = [([tuple(x)], b[tuple(x)], tuple(x)) for x in np.array(np.nonzero(b==word[0])).T] #starting point(s)
    for fr in _fringe:
      fringe = [fr]
      while fringe:
        for (v,w,x) in successors(*fringe.pop()):
          if w+b[x] == word:
            return True

          fringe.append((v+[tuple(x)],w+b[x],x)) #DFS
          # fringe.insert(0,(v+[tuple(x)],w+b[x],x)) #BFS

    return False


tests = [
  ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True),
  ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
  ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
  ([["a","a"]], "aaa", False), #False
  ([["a","b"],["c","d"]], "acdb", True), #True
  ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "QQ", False), #False
  ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False), #False
]

if __name__ == "__main__":
  for b,w,t in tests:
    if t!=Solution().exist(b,w):
      print(t)
  # print([t==Solution().exist(b,w) for b,w,t in tests])
  print('done!')
