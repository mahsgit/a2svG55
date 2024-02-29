# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque()
        ans=[]
        temp=[]
        if root:
            que.append(root)
        while que:
            for i in range(len(que)):
                node=que.popleft()
                temp.append(node.val)
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
            ans.append(temp)
            temp=[]
        for i in range(1,len(ans),2):
            ans[i].reverse()


        return ans

    