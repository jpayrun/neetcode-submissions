# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        cur = head
        while cur:
            cur = cur.next
            len+=1
        if n == len:
            return head.next
        i = 0
        cur = head
        while i < len - n - 1:
            cur = cur.next
            i+=1
        if not cur.next:
            cur.next = None
        else:
            cur.next = cur.next.next
        return head
        