# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.out = []

        def DFS(root):
            if root == None:
                return
            DFS(root.left)
            DFS(root.right)
            self.out.append(root.val)

        DFS(root)
        return self.out
        