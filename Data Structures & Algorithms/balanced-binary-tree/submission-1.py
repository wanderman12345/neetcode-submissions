# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        out = [True]
        def recur(root):
            if root == None:
                return 0
                                
            left = recur(root.left)
            right = recur(root.right)

            if abs(left-right) > 1:
                out[0] = False

            return 1 + max(left, right)

        recur(root)
        return out[0]
            