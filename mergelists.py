# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional
class ListNode:
 def __init__(self, val=0, next=None):
  self.val = val
  self.next = next
 def __repr__(self):
  return f'({self.val} {self.next})'


class Solution:
 def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  if not list1: return list2
  if not list2: return list1
  head = ListNode()  # keep a reference to head of list
  tmp = head
  while list1 and list2:  # until one list is empty
   if list1.val < list2.val:
    tmp.next = list1
    list1 = list1.next  # behead l1
   else:
    tmp.next = list2
    list2 = list2.next  # behead l2

   tmp = tmp.next

  # append with remaining elements
  if list1: tmp.next = list1
  else: tmp.next = list2
  return head.next


def enlist(ls):
 head = ListNode()
 r = head
 for x in ls:
  r.next = ListNode(x)
  r = r.next
 return head.next


def test(l1,l2):
 e1 = enlist(l1)
 e2 = enlist(l2)
 # print(f'{e1=} {e2=}')
 print(Solution().mergeTwoLists(e1,e2))


if __name__ == "__main__":
 test([], [])
 test([1,2],[1,2])
 test([7,8],[3,5,6])
 test([1,2,3], [0])
 test([], [0,1])
 test([1,2], [])
