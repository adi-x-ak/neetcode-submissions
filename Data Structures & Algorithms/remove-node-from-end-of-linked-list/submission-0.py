# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next:
            candidate = prev.next
            checker = candidate

            # Move checker n - 1 steps ahead from candidate
            for _ in range(n - 1):
                checker = checker.next

            # If checker is at the last node,
            # candidate is the nth node from the end
            if checker.next is None:
                prev.next = candidate.next
                break

            prev = prev.next

        return dummy.next




        
