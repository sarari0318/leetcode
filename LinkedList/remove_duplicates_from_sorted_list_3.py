# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # cornercase: head is None
        if head is None:
            return None
        cur = head
        
        # prepare pointer: cur
        # if cur.val is equal to cur.next.val
        # ⇨ enter cur.next.next into cur.next
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head
    
    # testcase1: 
    # cur 1->1->2
    # ① cur.val == cur.next.val ⇨ cur 1->2
    # ② cur = cur.next ⇨ cur 2
    # head 1->2
    
    # testcase2:
    # cur 1->1->2->3->3
    # ① cur.val == cur.next.val ⇨ cur 1->2->3->3
    # ② cur = cur.next ⇨ cur 2->3->3
    # ③ cur = cur.next ⇨ cur 3->3
    # ④ cur.val == cur.next.val ⇨ cur 3
    # head 1->2->3