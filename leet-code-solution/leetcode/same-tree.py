class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(node1,node2):
            if not node1 and not node2:
                return True
            if not  node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
           
          
            l= helper(node1.left,node2.left)
            r= helper(node1.right,node2.right)
            return l and r
        return helper(p,q)


            
       