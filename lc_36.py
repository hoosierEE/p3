# https://leetcode.com/problems/valid-sudoku/
from typing import List

import numpy as np

class Solution:
    def check(self,x):
        y = np.sort(np.ravel(x[x>="1"]))
        return y == sorted(set(y))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = np.array(board)
        for i in range(9):
            if not self.check(b[i,:]): return False #rows
            if not self.check(b[:,i]): return False #cols
        for i in range(3):
            for j in range(3):
                bb = b[i*3:i*3+3,j*3:j*3+3]
                if not self.check(bb):
                    return False

        return True

if __name__ == "__main__":
    ins = [
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]],

        [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]],

        [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
    ]
    outs = [
        True,
        False,
        False,
    ]

    for i,o in zip(ins,outs):
        s = Solution().isValidSudoku(i)
        if s != o:
            print(f'{i} => {s}  ({o})')
