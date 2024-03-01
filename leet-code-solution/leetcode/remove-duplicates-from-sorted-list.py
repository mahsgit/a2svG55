# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        temp=head
        while curr:
            temp=curr.next

            while temp and  curr.val==temp.val:
                temp=temp.next
            curr.next=temp
            curr=temp
            
        return head
        