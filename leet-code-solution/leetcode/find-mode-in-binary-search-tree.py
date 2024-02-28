# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter=Counter()
        def helper(node):
            if not node:
                return
            if node:
                counter[node.val]+=1
            helper(node.left)
            helper(node.right)
            return counter

        helper(root)
        ans=[]
        maxi=max(counter.values())
        for key,val in counter.items():
            if val==maxi:
                ans.append(key)


        print(helper(root))
        return ans
        