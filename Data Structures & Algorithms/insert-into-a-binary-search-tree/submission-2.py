# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # follow the BST and find a slot that you want to insert in.
        if root == None:
            return TreeNode(val)

        def DFS(root, val):
            if val < root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    return
                else:
                    DFS(root.left, val)
            elif val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                    return     
                else:     
                    DFS(root.right, val)
        
        DFS(root, val)
        return root
        

        
        
        