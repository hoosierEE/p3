# TLE
# class Solution:
#   def canJump(self, nums: List[int]) -> bool:
#     z = [0]*len(nums)
#     for i,x in enumerate(nums):
#       tmp = ([0]*i+[1]*x+[0]*(len(nums)-i-x))
#       z = [(a|b) for a,b in zip(z,tmp)]
#     return all(z[:-1])

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    c = 0
    for x in nums:
      if c<0:
        return False
      c = max(c,x)-1
    return True
