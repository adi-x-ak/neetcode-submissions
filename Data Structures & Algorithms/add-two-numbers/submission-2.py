# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #so lets start creating a dummy node and curr pointer that will help us 
        dummy=ListNode(0)
        curr=dummy
        #since its addition and we can expect a acarry 
        carry=0

        #now lets write the the main logic
        while l1 is not None or l2 is not None or carry!=0:
            if l1 is not None:
                value1=l1.val
            else:
                value1=0
            if l2 is not None:
                value2=l2.val
            else:
                value2=0
            total=value1+value2+carry
            digit=total%10
            carry=total//10
            curr.next=ListNode(digit)
            curr=curr.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return dummy.next

        