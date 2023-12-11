#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j,N = 1,len(nums)
        for i in range(1,N):
            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j+=1

        return j



if __name__ == "__main__":
    ins = [
        ([2,2,3,3]),
        ([0,0,1,2,2,3,4]),
    ]
    outs = [
        [2,3],
        [0,1,2,3,4],
    ]

    for nums,o in zip(ins,outs):
        i = nums[::]
        s = Solution().removeDuplicates(nums)
        r = nums[:s]
        if r != o:
            print(f'{i} => {r}  ({o})')
