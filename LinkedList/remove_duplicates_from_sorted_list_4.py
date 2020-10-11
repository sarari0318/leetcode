class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur.next:
            head = cur.next
            while head.next and head.val == head.next.val:
                head = head.next

            if cur.next != head:
                cur.next = head.next

            else:
                cur = cur.next

        return dummy.next