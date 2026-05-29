# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3
        arr = []
        i = head
        while i:
            arr.append(i)
            i = i.next

        l = 0
        r = len(arr)-1
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l == r:
                break
            arr[r].next = arr[l]
            r -= 1

        arr[l].next = None
        


        
  
         




        
        