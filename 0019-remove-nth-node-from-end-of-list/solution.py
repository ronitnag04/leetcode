# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        
        slow = fast = last = head
        while n:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        while fast:
            last = slow
            slow = slow.next
            fast = fast.next
        last.next = slow.next
        return head