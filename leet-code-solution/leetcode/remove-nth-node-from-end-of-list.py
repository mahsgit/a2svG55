# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        ans=[]
        while curr :
            ans.append(curr.val)
            curr=curr.next

        l=len(ans)-n

        curr=ListNode("dummy")
        curr=head
        for i,val in enumerate(ans):
            if i==l:
                continue
            curr.next=ListNode(val)
            curr=curr.next
        return head.next

        
        