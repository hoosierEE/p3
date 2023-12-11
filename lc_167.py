# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            s = numbers[l]+numbers[r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                return [l+1,r+1]


        

        # # slow!
        # for i,x in enumerate(numbers):
        #     y = target-x
        #     if y in numbers[i+1:]:
        #         return [i+1, numbers[i+1:].index(target-x)+i+2]


if __name__ == "__main__":
    ins = [
        ([1,0,0,1],2),
        ([-2,0,2],0),
        ([2,7,11,15],9),
        ([0,1,1,1,1,0,1,2,3],0),
        ([0,0,1,2,3],0),
        ([2,3,4],6),
        ([-1,0],-1),
    ]
    outs = [
        [1,4],
        [1,3],
        [1,2],
        [1,6],
        [1,2],
        [1,3],
        [1,2],
    ]

    for i,o in zip(ins,outs):
        s = Solution().twoSum(*i)
        if s != o:
            print(f'{i} => {s}  (expected: {o})')
