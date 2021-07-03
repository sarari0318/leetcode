# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        '''
        Parameters
        ----------
            head: ListNode
        Returns
        -------
            pre: ListNode
            ⇨ return the reversed list.
        '''

        if head is None:
            return None

        '''
        None ⇨ head ⇨ head.next
         pre    cur     post
        '''
        cur = head
        pre, post = None, head.next

        while cur is not None:
            # 前後のノードを入れ替える
            cur.next = pre
            pre = cur
            cur = post

            if post is not None:
                post = post.next

        return pre