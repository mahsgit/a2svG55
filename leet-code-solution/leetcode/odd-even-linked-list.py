# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        if not odd:
            return head
        even=head.next
        evenhead=head.next
        # while odd and odd.next:
        #     odd.next=odd.next.next
        #     odd=odd.next
        #     if even and even.next:
        #          even.next=even.next.next
        #          even=even.next

        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=evenhead
        return head

        