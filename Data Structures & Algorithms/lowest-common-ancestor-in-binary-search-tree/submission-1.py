# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def recur(root, p, q):
            if root == None:
                return 

            if root.val < p.val and root.val < q.val:
                return recur(root.right, p, q)

            elif root.val > p.val and root.val > q.val:
                return recur(root.left, p, q)

            elif root.val >= p.val and root.val <= q.val:
                return root
       
        if p.val < q.val:
            lowest = p
            highest = q
        else:
            lowest = q
            highest = p

        return recur(root, lowest , highest)

            

            
