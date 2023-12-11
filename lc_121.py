from typing import List
import numpy as np

# # TLE
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         p = prices
#         r = prices[::-1]
#         mis = [min(x,*p[:i or 1]) for i,x in enumerate(p)]
#         mas = [max(x,*r[:i or 1]) for i,x in enumerate(r)][::-1]
#         return max(b-a for a,b in zip(mis,mas))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i]-buy)

        return profit


if __name__ == "__main__":
    ins = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],
        [2,4,1],
        [2,1,2,0,1],
        [1],
        [2,1,2,1,0,1,2],
        [3,3,5,0,0,3,1,4],
    ]
    outs = [5,0,2,1,0,2,4]

    for i,o in zip(ins,outs):
        s = Solution().maxProfit(i)
        if s != o:
            print(f'{i} => {s}  ({o})')
