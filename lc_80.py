#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2,len(nums)):
            # print(nums)
            # print((' '*(i*3+1))+'i')
            # print((' '*(j*3+1))+'j')

            if nums[j-2:j].count(nums[i]) < 2:
                nums[j] = nums[i]
                j+=1

            # print(nums[:j])
            # print()

        return j


if __name__ == "__main__":
    ins = [
        [1,2,3],
        [1,1,1],
        [1,1,1,1],
        [1,1,2,2,2,3,3],
        [0,0,1,1,1,1,2,3,3],
        [0,1,1,1,2,3,3,4],
        [0,1,2,2,2,2,2,3,4,4,4],
    ]
    outs = [
        3,
        2,
        2,
        6,
        7,
        7,
        7,
    ]

    for nums,o in zip(ins,outs):
        i = nums[::]
        s = Solution().removeDuplicates(nums)
        r = nums[:s]
        if o!=s or not all(r.count(i)<3 for i in set(r)):
            print(f'{i} => {r} {s}  ({o})')
