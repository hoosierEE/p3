# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #idea:
        #min(max-scanLR, max-scanRL) - heights
        l,r = [],[]
        ml,mr = 0,0
        for h in height[::-1]:
            mr = max(mr,h)
            r.append(mr)

        for h in height:
            ml = max(ml,h)
            l.append(ml)

        water = 0
        for lh,rh,h in zip(l,r[::-1],height):
            water += max(0,min(lh,rh)-h)

        return water





if __name__ == "__main__":
    ins = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
    ]
    outs = [
        6,
        9,
    ]

    for i,o in zip(ins,outs):
        s = Solution().trap(i)
        if s != o:
            print(f'{i} => {s}  (expected: {o})')
