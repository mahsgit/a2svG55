# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left=float('-inf')
        right=float('inf')
        def helper(left,right,node):
            if not node:
                return True
            if not(left<node.val<right):
                return False

            l=helper( left,node.val,node.left)
            r=helper(node.val,right,node.right)
            return l and r
        return helper(left,right,root)

         

            
        