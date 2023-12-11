# https://leetcode.com/problems/3sum/
from typing import List

from collections import defaultdict

#time limit exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sums = defaultdict(set)
        for i in range(len(nums)): #sum pairs
            a = nums[i]
            if 0==a: continue
            for j in range(i+1,len(nums)):
                b = nums[j]
                if 0==b: continue
                sums[a+b].add((i,j))

        nsd = {x:set([i for i,y in enumerate(nums) if x==y][:3]) for x in set(nums) if -x in sums}
        res = set()
        if nums.count(0)>2:
            res.add((0,0,0))

        #FIXME: not passing tests
        for s in nsd:
            for ss in sums[s]:
                if nsd[s] not in ss:
                    idx = (nsd[s]|set(ss))
                    res.add(tuple((nums[i] for i in idx)))
                    break

        return [list(x) for x in sorted(res)]


# #time limit exceeded
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sums = defaultdict(set)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 sums[nums[i]+nums[j]].add((i,j))

#         res = set()
#         for i in range(len(nums)):
#             s = nums[i]
#             if -s in sums:
#                 for x in sums[-s]:
#                     if i not in x:
#                         ii,jj = x
#                         res.add(tuple(sorted((s,nums[ii],nums[jj]))))

#         return [list(x) for x in sorted(res)]




if __name__ == "__main__":
    ins = [
        [-1,0,1],
        [-1,-1,2,2,2,2,2,2],
        [3,0,-2,-1,1,2],
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]
    outs = [
        [[-1,0,1]],
        [[-1,-1,2]],
        [[-2,-1,3],[-2,0,2],[-1,0,1]],
        [[-1,-1,2],[-1,0,1]],
        [],
        [[0,0,0]],
        [[0,0,0]],
    ]


    for i,o in zip(ins,outs):
        s = Solution().threeSum(i)
        if s != o:
            print(f'{i} => {s}  should be: {o}')
