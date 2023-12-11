# https://leetcode.com/problems/reverse-linked-list/
from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        r = [self.val]
        p = self.next
        while p:
            r.append(p.val)
            p = p.next
        return '['+', '.join([str(ri) for ri in r])+']'

def enlist(ls):
    '''turn python list into ListNode'''
    p = None
    while ls:
        p = ListNode(ls.pop(), p)

    return p



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        p = head
        while p:
            # p = ListNode(p.val, p)
            l.insert(0,p.val)
            p = p.next

        return enlist(l)



if __name__ == "__main__":
    ins = [
        [1,2,3,4,5],
    ]
    outs = [
        [5,4,3,2,1],
    ]


    for i,o in zip(ins,outs):
        s = Solution().reverseList(enlist(i))
        if str(s) != str(o):
            print(f'{i} => {s}  (should be {o})')
