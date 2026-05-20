# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers to change the next values  and merge
        l = list1
        r = list2
        start = ListNode()
        n = start
        while l and r:
            if l.val < r.val:
                n.next = l
                l = l.next
            else:
                n.next = r
                r = r.next
            n = n.next
        while l:
            n.next = l 
            l = l.next
            n = n.next
        while r:
            n.next = r
            r = r.next
            n = n.next

        return start.next
