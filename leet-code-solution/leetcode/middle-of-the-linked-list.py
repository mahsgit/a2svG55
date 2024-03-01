# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, val=0):
        self.val = val
        self.next = next

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        dummy=head
        while  dummy:
            dummy=dummy.next
            size+=1
        
        for i in range(size//2):
            head=head.next

        return head
        