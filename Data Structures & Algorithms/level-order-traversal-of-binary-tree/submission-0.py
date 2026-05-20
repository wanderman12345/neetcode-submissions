# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        out = []
        ''' we start with root in queue. 
        We do a while loop while something is in the queue
        we add before popping to out
        we then pop exact amoung in list and if children exist push children'''
        length = len(queue)
        while length > 0:
            roots = []
            for eachNode in queue:
                roots.append(eachNode.val)
            out.append(roots)
            # adds children to the queue
            for i in range(length):
                val = queue.pop(0)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            # obtain length of the queue
            length = len(queue)
        return out

    