# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        res=[]
        while curr:
            res.append(curr.val)
            curr=curr.next
        res.sort()

        
        
        head = ListNode("dummy")
        curr = head

        for val in res:
            curr.next = ListNode(val)
            curr = curr.next

        return head.next

        