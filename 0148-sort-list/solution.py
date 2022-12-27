# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        l = l[::-1]
        t = head = ListNode(l.pop())
        while l:
            head.next = ListNode(l.pop())
            head = head.next
        
        return t
        