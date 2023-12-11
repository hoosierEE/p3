# https://leetcode.com/problems/h-index/
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = sorted(citations,reverse=True)
        prev = 0
        for i,x in enumerate(s):
            prev = max(min(x,i+1),prev)

        return prev


if __name__ == "__main__":
    ins = [
        [3,0,6,1,5],
        [1,3,1],
    ]
    outs = [
        3,
        1,
    ]

    for i,o in zip(ins,outs):
        s = Solution().hIndex(i)
        if s != o:
            print(f'{i} => {s}  should be: {o}')
