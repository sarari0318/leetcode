class ListNode:
    def __init__(self, x):
        self.val = x
        self.head = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        '''
        Parameters
        ----------
            head: ListNode 
        Returns
        -------
            bool
            ⇨ return true if there is a cycle in the linked list. Otherwise, return false.
        '''

        if head is None:
            return False

        # 進む速さの異なる２つのポインタを用意
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            # ２つのポインタが重なる時があれば
            if slow == fast:
                # サイクルが存在する
                return True

        return False