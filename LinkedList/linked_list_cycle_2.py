# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        '''
        Parameters
        ----------
            head: ListNode 
        Returns
        -------
            head: ListNode
            ⇨ return the node where the cycle begins. If there is no cycle, return null.
        '''
        
        # 進む速さの異なる２つのポインタを用意
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        # そもそもCycleが存在しなければ、
        else:
            return None
          
        # 「始点からCycleの始まりのノードまでの距離」 と
        # 「slowとfastの合流点から端までの距離」 が等しいので、
        # heahを始点から、slowをfastとの合流点からそれぞれスタート      
        while head != slow:
            head = head.next
            slow = slow.next
                
        return head