# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n)
        # add lists
        head = l1
        while l1.next and l2.next:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        l1.val += l2.val
        if l2.next:
            l1.next = l2.next
            
        # carry over values
        cur = head
        while cur.next:
            if cur.val > 9:
                cur.next.val += cur.val//10
                cur.val = cur.val%10
            cur = cur.next
        if cur.val > 9:
            cur.next = ListNode(cur.val//10)
            cur.val %= 10
        
        return head
        