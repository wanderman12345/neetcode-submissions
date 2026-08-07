# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = 0

        def DFS(root):
            if root == None:
                return 0
            l = DFS(root.left)
            r = DFS(root.right)
            self.height = self.height = max(self.height, abs(l-r))
            return 1 + max(l,r)

        if not root:
            return True

        DFS(root)
        return self.height <= 1
        
        