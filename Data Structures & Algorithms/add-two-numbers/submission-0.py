# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1

        s1 = ""

        while curr:
            s1 += str(curr.val)
            curr = curr.next

        n1 = int(s1[::-1])


        curr2 = l2

        s2 = ""

        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next

        n2 = int(s2[::-1])

        n3 = n1+n2

        s3 = str(n3)

        s4 = s3[::-1]

        curr3 = ListNode(0)
        curr4 = curr3

        for i in range(len(s4)):
            curr4.next = ListNode(int(s4[i]))
            curr4 = curr4.next

        

        return curr3.next

        
