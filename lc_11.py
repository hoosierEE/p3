from typing import List
from itertools import product

# # FIXME time limit exceeded
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         areas = []
#         n = len(height)
#         for i in range(n):
#             hi = height[i]
#             for j in range(i,n):
#                 areas.append((j-i) * min(hi,height[j]))

#         return max(areas)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        while left<=right:
            hl = height[left]
            hr = height[right]
            h = min(hl,hr)
            l = right-left
            if area<h*l:
               area = h*l
            if hl<=hr:
                left+=1
            else:
                right-=1
        return area


        

if __name__ == "__main__":
    ins = [[1,8,6,2,5,4,8,3,7]]
    outs = [49]

    for i,o in zip(ins,outs):
        s = Solution().maxArea(i)
        if s != o:
            print(s)
            print(o)



