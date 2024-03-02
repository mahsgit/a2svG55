# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # curr=head
        # prev=None
        # while curr:
        #     while curr.val==left:
        #         curr=curr.next
        #     while curr.val==right:
        #         nextnode=curr.next
        #         curr.next=prev
        #         prev=curr
        #         curr=nextnode
        #     curr=curr.next
        # return head
        curr=head
        res=[]
        while curr:
            res.append(curr.val)
            curr=curr.next
        res1=res[:left-1]
        res2=res[right:]
        resmiddle=res[left-1:right]
        resmiddle=resmiddle[::-1]
        new=res1+resmiddle+res2

        curr=ListNode("dummy")
        curr=head
        for val in new:
            curr.next=ListNode(val)
            curr=curr.next

        return head.next


            
        