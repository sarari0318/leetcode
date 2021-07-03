# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        '''
        Parameters
        ----------
            l1: ListNode 
            l2: ListNode 
        Returns
        -------
            dummy.next: ListNode
            ⇨ add the two numbers and return the sum as a linked list.
        '''

        # ダミーノードを生成
        dummy = ListNode()
        cur = dummy
        # 繰り上げる値
        carry = 0

        while l1 or l2 or carry:
            total = carry
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0

            # totalを10で割った商をcarry, 余りをtotalへ
            carry, total = divmod(total, 10)

            cur.next = ListNode(total)
            cur = cur.next

            if l1 is None and l2 is None:
                break
            elif l1 and l2 is None:
                l1 = l1.next
            elif l1 is None and l2:
                l2 = l2.next
            else:
                l1 = l1.next
                l2 = l2.next

        return dummy.next