# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # cornercase: head is None
        if head is None:
            return None

        cur = head
        pre, post = None, head.next

        while cur:
            cur.next = pre
            pre = cur
            cur = post

            if post:
                post = post.next

        return pre