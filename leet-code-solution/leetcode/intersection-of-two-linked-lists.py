# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1=set()
        list2=[]
        ans=[]
        while headA:
            list1.add(headA)
            headA=headA.next
            
        while headB:
            if headB in list1:
                return headB
            headB=headB.next
        return None
        

        