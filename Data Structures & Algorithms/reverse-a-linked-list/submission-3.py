# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #i need two things to start with a dummy node and an temporay variable
        #because i cant be tapering the head anymore 
        prev=None
        temp=head
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev



    
        