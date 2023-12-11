# https://leetcode.com/problems/sliding-window-maximum

# time limit exceeded for big list with k=50000
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i in range(0,len(nums)-k+1):
            s.append(max(nums[i:i+k]))
        return s

if __name__ == "__main__":
    ins = [([1,3,-1,-3,5,3,6,7],3)]
    outs = [([3,3,5,5,6,7])]

    for i,o in zip(ins,outs):
        s = Solution().maxSlidingWindow(*i)
        if s != o:
            print(s)
            print(o)
