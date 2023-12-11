class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [x for x in s.lower() if x.isalnum()]
        return t==t[::-1]



if __name__ == "__main__":
    ins = ['A man, a plan, a canal: Panama!']
    outs = [1]

    for i,o in zip(ins,outs):
        s = Solution().isPalindrome(i)
        if s != o:
            print(s)
            print(o)
