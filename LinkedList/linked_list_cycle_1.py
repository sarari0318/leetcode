class ListNode:
    def __init__(self, x):
        self.val = x
        self.head = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False