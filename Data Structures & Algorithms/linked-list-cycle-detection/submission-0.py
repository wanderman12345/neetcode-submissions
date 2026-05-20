# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique = set()
        s = head
        while s:
            if s not in unique:
                unique.add(s)
            else:
                return True
            s = s.next
        return False
        