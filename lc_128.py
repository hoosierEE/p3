# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        starts = {None:0} #unique IDs of consecutive runs
        a = sorted(set(nums))
        n = len(a)
        st = 0
        for i in range(n-1):
            if a[i]+1 != a[i+1]:
                st = None
                continue
            if st is None:
                st = i
            starts[st] = starts.get(st,1)+1

        del starts[None]

        vs = sorted(starts.values())
        if vs:
            return vs[-1]
        return 1


if __name__ == "__main__":
    # expect = [[100,4,200,1,3,2],
    #           [0,3,7,2,5,8,4,6,0,1],
    #           [1,2,0,1]]
    # actual = [4,9,3]
    given = [[1,2,0,1]]
    answer = [3]
    for g,a in zip(given,answer):
        r = Solution().longestConsecutive(g)
        if r!=a:
            print(g)
            print(f'got {r} but expected {a}')
