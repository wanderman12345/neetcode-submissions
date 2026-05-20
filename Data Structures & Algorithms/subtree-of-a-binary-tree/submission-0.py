# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        yes = [False]
        def sameTree(root, subRoot):
            if root == None and subRoot == None:
                return True
            if root != None and subRoot == None:
                return False
            if root == None and subRoot != None:
                return False
            if root.val != subRoot.val:
                return False

            l = sameTree(root.left, subRoot.left)
            r = sameTree(root.right, subRoot.right)
            return l and r

        def recur(root, subRoot):
            if sameTree(root, subRoot):
                yes[0] = True

            if root == None or subRoot == None:
                return 
          
            recur(root.left, subRoot)
            recur(root.right, subRoot)

        
        recur(root, subRoot)
        return yes[0]
            

        

        

        
        