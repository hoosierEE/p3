#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sz = len(nums)
        count = nums.count(val)
        while val in nums:
            del nums[nums.index(val)]

        return sz-count


if __name__ == "__main__":
    ins = [
        ([3,2,2,3],3),
        ([0,1,2,2,3,0,4,2],2),
    ]
    outs = [
        [2,2],
        [0,1,4,0,3],
    ]

    for (nums,val),o in zip(ins,outs):
        i = nums[::]
        s = Solution().removeElement(nums,val)
        r = sorted(nums[:s])
        if r != sorted(o):
            print(f'{i} => {r}  ({sorted(o)})')
