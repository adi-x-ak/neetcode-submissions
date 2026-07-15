# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # curr = l1

        # s1 = ""

        # while curr:
        #     s1 += str(curr.val)
        #     curr = curr.next

        # n1 = int(s1[::-1])


        # curr2 = l2

        # s2 = ""

        # while curr2:
        #     s2 += str(curr2.val)
        #     curr2 = curr2.next

        # n2 = int(s2[::-1])

        # n3 = n1+n2

        # s3 = str(n3)

        # s4 = s3[::-1]

        # curr3 = ListNode(0)
        # curr4 = curr3

        # for i in range(len(s4)):
        #     curr4.next = ListNode(int(s4[i]))
        #     curr4 = curr4.next

        

        # return curr3.next

        dummy = ListNode(0)

        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        
