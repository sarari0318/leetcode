# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        # return the node where the cycle begins
        # Pre: head
        # Post: node
        
        # x: from head to the node where the cycle begin(cy_begin)
        # y: from cy_begin to the node where slow == fast(overlap)
        # z: from overlap to tail
        # ⇨ 2(x+y) = x+y+z+y
        # ⇨ x = z
        
        # first step: find the node where fast overlap slow
        # second step: find the node where slow overlap head
        
        # testcase:
        # first step!!
        # fast: 3, slow: 3
        # fast: 0, slow: 2
        # fast: 2, slow: 0
        # fast: -4, slow: -4 ⇨ the node where fast overlap slow!!!
        
        # second step!!
        # slow: -4, head: 3
        # slow: 2, head: 2 ⇨ the node where slow overlap head!!!
        # return this node!!
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        else:
            return None
                
        while head != slow:
            head = head.next
            slow = slow.next
            
        
        return head