# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        cur = head
        fast = head.next
        while cur and fast and fast.next:
            if cur.val == fast.val:
                return True
            cur = cur.next
            fast = fast.next.next
        return False
