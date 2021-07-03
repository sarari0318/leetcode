# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        '''
        Parameters
        ----------
            head: ListNode 
        Returns
        -------
            head: ListNode
            ⇨ return the linked list deleted all duplicates and sorted.
        '''
        
        if head is None:
            return None
        cur = head
        
        
        while cur and cur.next:
            # 数字に被りがあるとき、
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head
