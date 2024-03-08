# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]
        path=[]
        def helper(root):
            if not root:
                return
                
            path.append(root.val)
            
            if not root.left and not  root.right:
                var=int(''.join(map(str,path[::])))
                ans.append(var)
                

            helper(root.left)
            helper(root.right)
            path.pop()
        
        helper(root)
        return  sum(ans)


        