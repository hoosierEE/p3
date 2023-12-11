from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o = {
            '+':lambda y,x:x+y,
            '-':lambda y,x:x-y,
            '*':lambda y,x:x*y,
            '/':lambda y,x:trunc(x/y),
        }
        stk = []
        for x in tokens:
            if x in o:
                stk.append(o[x](stk.pop(),stk.pop()))
            else:
                stk.append(int(x))
        return stk.pop()

def main():
    t = [(6,["4","13","5","/","+"]),
         (22,["10","6","9","3","+","-11","*","/","*","17","+","5","+"])]
    for x in t:
        print(x[0], Solution().evalRPN(x[1]))

if __name__ == "__main__":
    main()
