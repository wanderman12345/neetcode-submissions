# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def recur(root, maxVal):
            if root == None:
                return
            
            if root.val >= maxVal:
                count[0] += 1
                maxVal = root.val

            recur(root.left, maxVal)
            recur(root.right, maxVal)

        recur(root, root.val)
        return count[0]

