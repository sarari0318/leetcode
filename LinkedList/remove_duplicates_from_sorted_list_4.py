class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        '''
        Parameters
        ----------
            head: ListNode 
        Returns
        -------
            head: ListNode
            ⇨ return the linked list deleted all nodes that have duplicate numbers and sorted.
        '''

        if head is None:
            return None

        # ダミーノードを生成
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur.next:
            head = cur.next
            # 数字の重複がある限り、headを進める
            while head.next and head.val == head.next.val:
                head = head.next

            if cur.next != head:
                cur.next = head.next

            else:
                cur = cur.next

        return dummy.next